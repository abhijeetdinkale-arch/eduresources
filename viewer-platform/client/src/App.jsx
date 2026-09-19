import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Catalog from './components/Catalog';
import HomePage from './components/HomePage';
import Viewer from './components/Viewer';
import LoginModal from './components/LoginModal';
import PlansModal from './components/PlansModal';
import SecurityShield from './components/SecurityShield';
import { useAuth } from './context/AuthContext';
import { api } from './services/api';

export default function App() {
  const { user, isLoginModalOpen, setIsLoginModalOpen } = useAuth();
  const [currentView, setCurrentView] = useState('home');
  const [materials, setMaterials] = useState([]);
  const [loadingMaterials, setLoadingMaterials] = useState(true);
  const [activeDocument, setActiveDocument] = useState(null);
  const [activeCategory, setActiveCategory] = useState('All');
  const [isPlansModalOpen, setIsPlansModalOpen] = useState(false);
  const [isSubscribed, setIsSubscribed] = useState(true);

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

  // When user logs in, set view to catalog (or check subscription)
  useEffect(() => {
    async function checkUserSubscription() {
      if (user && user.email) {
        const subData = await api.checkSubscription(user.email);
        setIsSubscribed(subData.isSubscribed);
        setCurrentView('catalog'); // Directly go to catalog on login
      } else {
        setIsSubscribed(false);
        setCurrentView('home');
      }
    }
    checkUserSubscription();
  }, [user]);

  const handleSelectDocument = (doc) => {
    if (!user) {
      setIsLoginModalOpen(true);
      return;
    }

    if (!isSubscribed) {
      setIsPlansModalOpen(true);
      return;
    }

    setActiveDocument(doc);
  };

  const handleBackToCatalog = () => {
    setActiveDocument(null);
  };

  return (
    <div className={`min-h-screen flex flex-col font-sans transition-colors duration-300 ${darkMode ? 'dark text-[#F5F2EB]' : 'text-[#18181B]'}`}>
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
        /* Fullscreen Secure Document Viewer (No Watermarks) */
        <Viewer
          material={activeDocument}
          user={user}
          onBack={handleBackToCatalog}
        />
      ) : (
        /* Web Application Interface */
        <>
          <div className="pt-2">
            <Navbar
              currentView={currentView}
              onNavigate={(view) => {
                setCurrentView(view);
                setActiveDocument(null);
              }}
              onOpenLogin={() => setIsLoginModalOpen(true)}
              onOpenPlans={() => setIsPlansModalOpen(true)}
              darkMode={darkMode}
              onToggleTheme={toggleTheme}
              isSubscribed={isSubscribed}
            />
          </div>

          <main className="flex-1">
            {currentView === 'home' && !user ? (
              <HomePage
                onBrowseBooks={() => setCurrentView('catalog')}
                onOpenPlans={() => setIsPlansModalOpen(true)}
                onOpenLogin={() => setIsLoginModalOpen(true)}
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
              />
            )}
          </main>

          <footer className="border-t border-paper-300/80 dark:border-darkbg-border bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs py-10 mt-16 text-center text-xs text-ink-600 dark:text-ink-400 transition-colors">
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
