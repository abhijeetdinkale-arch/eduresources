import React, { useState, useEffect, useCallback, useRef } from 'react';
import Navbar from './components/Navbar';
import Catalog from './components/Catalog';
import HomePage from './components/HomePage';
import Viewer from './components/Viewer';
import LoginModal from './components/LoginModal';
import PlansModal from './components/PlansModal';
import SecurityShield from './components/SecurityShield';
import LogoSplash from './components/LogoSplash';
import MobileBottomNav from './components/MobileBottomNav';
import PracticeExamContainer from './components/PracticeExam';
import { useAuth } from './context/AuthContext';
import { api } from './services/api';

export default function App() {
  const { user, isLoginModalOpen, setIsLoginModalOpen } = useAuth();
  const [showSplash, setShowSplash] = useState(true);
  const [currentView, setCurrentView] = useState('home');
  const [materials, setMaterials] = useState([]);
  const [loadingMaterials, setLoadingMaterials] = useState(true);
  const [activeFolder, setActiveFolder] = useState(null);
  const [activeDocument, setActiveDocument] = useState(null);
  const [activeCategory, setActiveCategory] = useState('All');
  const [isPlansModalOpen, setIsPlansModalOpen] = useState(false);
  const [isSubscribed, setIsSubscribed] = useState(true);

  // History navigation stack for Back & Forward buttons
  const [canGoBack, setCanGoBack] = useState(false);
  const [canGoForward, setCanGoForward] = useState(false);
  const historyStackRef = useRef([]);
  const historyIndexRef = useRef(-1);
  const isInternalNavRef = useRef(false);

  // Dark mode theme state
  const [darkMode, setDarkMode] = useState(() => {
    const saved = localStorage.getItem('edunet_theme');
    return saved ? saved === 'dark' : true;
  });

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
      document.body.classList.add('dark');
      localStorage.setItem('edunet_theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      document.body.classList.remove('dark');
      localStorage.setItem('edunet_theme', 'light');
    }
  }, [darkMode]);

  const toggleTheme = () => {
    setDarkMode((prev) => !prev);
  };

  // Fetch all materials on mount
  useEffect(() => {
    async function fetchMaterials() {
      try {
        setLoadingMaterials(true);
        const data = await api.getMaterials();
        setMaterials(data.materials || []);
      } catch (err) {
        console.error('Failed to load materials:', err);
      } finally {
        setLoadingMaterials(false);
      }
    }
    fetchMaterials();
  }, []);

  // Check user subscription upon login
  useEffect(() => {
    async function checkUserSubscription() {
      if (user && user.email) {
        const subData = await api.checkSubscription(user.email);
        setIsSubscribed(subData.isSubscribed);
      } else {
        setIsSubscribed(false);
      }
    }
    checkUserSubscription();
  }, [user]);

  // Synchronize URL Hash and Browser History (Back / Next button support)
  const syncRouteFromHash = useCallback(() => {
    const hash = window.location.hash || '#/';

    // Update history stack tracking
    if (!isInternalNavRef.current) {
      const currentStack = historyStackRef.current.slice(0, historyIndexRef.current + 1);
      if (currentStack.length === 0 || currentStack[currentStack.length - 1] !== hash) {
        currentStack.push(hash);
        historyStackRef.current = currentStack;
        historyIndexRef.current = currentStack.length - 1;
      }
    }
    isInternalNavRef.current = false;

    setCanGoBack(historyIndexRef.current > 0 || window.history.length > 1);
    setCanGoForward(historyIndexRef.current < historyStackRef.current.length - 1);

    if (hash.startsWith('#/viewer/')) {
      const docId = decodeURIComponent(hash.replace('#/viewer/', ''));
      if (materials.length > 0) {
        const doc = materials.find((m) => m.id === docId);
        if (doc) {
          if (!user) {
            setIsLoginModalOpen(true);
            setCurrentView('catalog');
            setActiveFolder(doc.courseCode);
            setActiveDocument(null);
          } else {
            setActiveDocument(doc);
            setActiveFolder(doc.courseCode);
            setCurrentView('catalog');
          }
          return;
        }
      }
    } else if (hash.startsWith('#/exams') || hash.startsWith('#/practice-exam')) {
      setActiveDocument(null);
      setActiveFolder(null);
      setCurrentView('exams');
      return;
    } else if (hash.startsWith('#/catalog/')) {
      const folderCode = decodeURIComponent(hash.replace('#/catalog/', ''));
      setActiveDocument(null);
      setActiveFolder(folderCode);
      setCurrentView('catalog');
      return;
    } else if (hash === '#/catalog') {
      setActiveDocument(null);
      setActiveFolder(null);
      setCurrentView('catalog');
      return;
    } else if (hash === '#/' || hash === '' || hash === '#') {
      setActiveDocument(null);
      setActiveFolder(null);
      if (user) {
        setCurrentView('catalog');
      } else {
        setCurrentView('home');
      }
      return;
    }
  }, [materials, user, setIsLoginModalOpen]);

  // Listen to browser Back/Forward (hashchange and popstate)
  useEffect(() => {
    syncRouteFromHash();
    window.addEventListener('hashchange', syncRouteFromHash);
    window.addEventListener('popstate', syncRouteFromHash);

    return () => {
      window.removeEventListener('hashchange', syncRouteFromHash);
      window.removeEventListener('popstate', syncRouteFromHash);
    };
  }, [syncRouteFromHash]);

  // Navigate actions that write to browser history
  const handleNavigateHome = () => {
    window.location.hash = '#/';
  };

  const handleNavigateCatalog = () => {
    window.location.hash = '#/catalog';
  };

  const handleNavigateExams = () => {
    window.location.hash = '#/exams';
  };

  const handleOpenFolder = (code) => {
    window.location.hash = `#/catalog/${encodeURIComponent(code)}`;
  };

  const handleBackToFolders = () => {
    if (window.history.length > 1 && window.location.hash.startsWith('#/catalog/')) {
      window.history.back();
    } else {
      window.location.hash = '#/catalog';
    }
  };

  const handleSelectDocument = (doc) => {
    if (!user) {
      setIsLoginModalOpen(true);
      return;
    }

    if (!isSubscribed) {
      setIsPlansModalOpen(true);
      return;
    }

    window.location.hash = `#/viewer/${encodeURIComponent(doc.id)}`;
  };

  const handleBackFromViewer = () => {
    if (window.history.length > 1 && window.location.hash.startsWith('#/viewer/')) {
      window.history.back();
    } else {
      const folder = activeDocument?.courseCode || activeFolder;
      if (folder) {
        window.location.hash = `#/catalog/${encodeURIComponent(folder)}`;
      } else {
        window.location.hash = '#/catalog';
      }
    }
  };

  // Back & Forth History Handlers for Web Navbar
  const handleHistoryBack = useCallback(() => {
    if (historyIndexRef.current > 0) {
      isInternalNavRef.current = true;
      historyIndexRef.current -= 1;
      const targetHash = historyStackRef.current[historyIndexRef.current];
      window.location.hash = targetHash;
      setCanGoBack(historyIndexRef.current > 0);
      setCanGoForward(historyIndexRef.current < historyStackRef.current.length - 1);
    } else if (window.history.length > 1) {
      window.history.back();
    }
  }, []);

  const handleHistoryForward = useCallback(() => {
    if (historyIndexRef.current < historyStackRef.current.length - 1) {
      isInternalNavRef.current = true;
      historyIndexRef.current += 1;
      const targetHash = historyStackRef.current[historyIndexRef.current];
      window.location.hash = targetHash;
      setCanGoBack(historyIndexRef.current > 0);
      setCanGoForward(historyIndexRef.current < historyStackRef.current.length - 1);
    } else {
      window.history.forward();
    }
  }, []);

  // Keyboard navigation for history (Alt + Left / Alt + Right)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) {
        return;
      }

      if (e.altKey && e.key === 'ArrowLeft') {
        e.preventDefault();
        handleHistoryBack();
      } else if (e.altKey && e.key === 'ArrowRight') {
        e.preventDefault();
        handleHistoryForward();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleHistoryBack, handleHistoryForward]);

  return (
    <div className={`min-h-screen flex flex-col font-sans transition-colors duration-300 ${darkMode ? 'dark text-[#F5F2EB]' : 'text-[#18181B]'}`}>
      {/* Launch / Refresh Celestial Logo Splash Animation */}
      {showSplash && (
        <LogoSplash onComplete={() => setShowSplash(false)} />
      )}

      {/* Anti-Screen-Capture Focus Loss Protector */}
      <SecurityShield isViewingDocument={Boolean(activeDocument)} />

      {/* Login Modal */}
      <LoginModal
        isOpen={isLoginModalOpen}
        onClose={() => setIsLoginModalOpen(false)}
      />

      {/* Semester Pass & Plans Modal */}
      <PlansModal
        isOpen={isPlansModalOpen}
        onClose={() => setIsPlansModalOpen(false)}
        user={user}
      />

      {activeDocument ? (
        /* Fullscreen Secure Document Viewer with Adaptive Fitting, Continuous Vertical PDF Scroll & Dock */
        <Viewer
          material={activeDocument}
          user={user}
          onBack={handleBackFromViewer}
        />
      ) : (
        /* Web Application Interface */
        <>
          <div className="pt-2">
            <Navbar
              currentView={currentView}
              onNavigate={(view) => {
                if (view === 'home') handleNavigateHome();
                else if (view === 'exams') handleNavigateExams();
                else handleNavigateCatalog();
              }}
              onLogoClick={handleNavigateHome}
              onOpenLogin={() => setIsLoginModalOpen(true)}
              onOpenPlans={() => setIsPlansModalOpen(true)}
              darkMode={darkMode}
              onToggleTheme={toggleTheme}
              isSubscribed={isSubscribed}
              canGoBack={canGoBack}
              canGoForward={canGoForward}
              onHistoryBack={handleHistoryBack}
              onHistoryForward={handleHistoryForward}
            />
          </div>

          <main className="flex-1 pb-16 sm:pb-0">
            {currentView === 'exams' ? (
              <PracticeExamContainer
                onBackToCatalog={handleNavigateCatalog}
                onRequireLogin={() => setIsLoginModalOpen(true)}
                user={user}
              />
            ) : currentView === 'home' && !user ? (
              <HomePage
                onBrowseBooks={handleNavigateCatalog}
                onOpenPlans={() => setIsPlansModalOpen(true)}
                onOpenLogin={() => setIsLoginModalOpen(true)}
                onOpenExams={handleNavigateExams}
                user={user}
                isSubscribed={isSubscribed}
                materialsCount={materials.length}
              />
            ) : (
              <Catalog
                materials={materials}
                loading={loadingMaterials}
                onSelectDoc={handleSelectDocument}
                user={user}
                onRequireLogin={() => setIsLoginModalOpen(true)}
                activeCategory={activeCategory}
                onCategoryChange={setActiveCategory}
                activeFolder={activeFolder}
                onOpenFolder={handleOpenFolder}
                onBackToDossiers={handleBackToFolders}
              />
            )}
          </main>

          <MobileBottomNav
            currentView={currentView}
            onNavigateHome={handleNavigateHome}
            onNavigateCatalog={handleNavigateCatalog}
            onNavigateExams={handleNavigateExams}
            onOpenPlans={() => setIsPlansModalOpen(true)}
            onOpenLogin={() => setIsLoginModalOpen(true)}
            user={user}
            darkMode={darkMode}
            onToggleTheme={toggleTheme}
            isSubscribed={isSubscribed}
          />

          <footer className="border-t border-paper-300/80 dark:border-darkbg-border bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs py-10 mt-16 mb-14 sm:mb-0 text-center text-xs text-ink-600 dark:text-ink-400 transition-colors">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-3">
              <div className="flex items-center justify-center gap-2">
                <div className="w-5 h-5 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center p-1">
                  <img src="/logo.png" alt="Star" className="w-full h-full object-contain filter invert dark:invert-0" />
                </div>
                <span className="font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
                  Edu<span className="font-normal text-ink-600 dark:text-ink-400"> network</span>
                </span>
                <span className="text-[10px] font-mono text-ink-400 dark:text-ink-500">• ARCHIVE 2026</span>
              </div>
              <p className="max-w-md mx-auto text-ink-500 dark:text-ink-500 text-[11px] leading-relaxed">
                Official curriculum textbook archives & examination companion collections. All materials are proprietary.
              </p>
              <div className="barcode text-[11px] text-ink-400 dark:text-ink-600 tracking-widest pt-1 select-none">
                |||| | ||| |||| | ||||| |||
              </div>
            </div>
          </footer>
        </>
      )}
    </div>
  );
}
