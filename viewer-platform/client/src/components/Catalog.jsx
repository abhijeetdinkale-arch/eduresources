import React, { useState, useMemo } from 'react';
import { Search, BookOpen, ArrowLeft, Folder, ShieldCheck } from 'lucide-react';
import DocumentCard from './DocumentCard';
import SubjectFolderCard from './SubjectFolderCard';

const CATEGORIES = [
  { id: 'All', label: '01 ALL EDITIONS' },
  { id: 'Textbook', label: '02 TEXTBOOKS' },
  { id: 'Exam Companion', label: '03 EXAM COMPANIONS' },
  { id: 'Question Bank', label: '04 QUESTION BANKS' },
  { id: 'Handwritten Notes', label: '05 NOTES' },
  { id: 'Sample Question Papers', label: '06 PAPERS' },
];

export default function Catalog({
  materials,
  loading,
  onSelectDoc,
  user,
  onRequireLogin,
  activeCategory = 'All',
  onCategoryChange,
  activeFolder: propActiveFolder,
  onOpenFolder,
  onBackToDossiers,
}) {
  const [searchQuery, setSearchQuery] = useState('');
  const [internalActiveFolder, setInternalActiveFolder] = useState(null);
  const activeFolder = propActiveFolder !== undefined ? propActiveFolder : internalActiveFolder;

  const handleOpenFolder = (code) => {
    if (onOpenFolder) {
      onOpenFolder(code);
    } else {
      setInternalActiveFolder(code);
    }
  };

  const handleBackToFolders = () => {
    if (onBackToDossiers) {
      onBackToDossiers();
    } else {
      setInternalActiveFolder(null);
    }
  };

  const selectedCategory = activeCategory;

  // Group materials by courseCode
  const courseGroups = useMemo(() => {
    const groups = {};
    for (const m of materials) {
      const code = m.courseCode || 'GENERAL';
      if (!groups[code]) groups[code] = [];
      groups[code].push(m);
    }
    return groups;
  }, [materials]);

  const courseCodes = useMemo(() => {
    return Object.keys(courseGroups).sort();
  }, [courseGroups]);

  // Filter materials inside opened folder
  const booksInActiveFolder = useMemo(() => {
    if (!activeFolder) return [];
    const list = courseGroups[activeFolder] || [];
    return list.filter((item) => {
      const matchesSearch =
        searchQuery.trim() === '' ||
        item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (item.subtitle && item.subtitle.toLowerCase().includes(searchQuery.toLowerCase()));

      const matchesCategory =
        selectedCategory === 'All' || item.category === selectedCategory;

      return matchesSearch && matchesCategory;
    });
  }, [activeFolder, courseGroups, searchQuery, selectedCategory]);

  // Filter subject folders on root view by search
  const filteredCourseCodes = useMemo(() => {
    if (searchQuery.trim() === '') return courseCodes;
    const q = searchQuery.toLowerCase();
    return courseCodes.filter((code) => {
      const matchesCode = code.toLowerCase().includes(q);
      const matchesAnyBook = (courseGroups[code] || []).some(
        (m) => m.title.toLowerCase().includes(q) || m.category.toLowerCase().includes(q)
      );
      return matchesCode || matchesAnyBook;
    });
  }, [courseCodes, courseGroups, searchQuery]);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
      {/* MINIMALIST LOGGED-IN HERO: BIG STAR LOGO + WELCOME */}
      <section className="bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs border border-paper-300/80 dark:border-darkbg-border rounded-[36px] p-8 sm:p-12 shadow-ticket dark:shadow-ticket-dark relative overflow-hidden text-center transition-colors">
        <div className="max-w-xl mx-auto flex flex-col items-center justify-center space-y-4 relative z-10">
          {/* BIG CELESTIAL STAR LOGO */}
          <div className="w-24 h-24 sm:w-28 sm:h-28 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center p-3 shadow-xl mb-1 ring-8 ring-ink-900/10 dark:ring-paper-50/10 animate-in zoom-in duration-300">
            <img
              src="/logo.png"
              alt="Edu network star logo"
              className="w-full h-full object-contain filter invert dark:invert-0"
            />
          </div>

          <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 text-xs font-mono tracking-wider">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
            <span>MEMBER ARCHIVES 2026 • DRM PROTECTED</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-cinzel font-black tracking-tight text-ink-900 dark:text-paper-50">
            Welcome{user?.name ? `, ${user.name.split(' ')[0]}` : ''}
          </h1>

          <p className="text-xs sm:text-sm font-sans text-ink-600 dark:text-ink-400 max-w-md mx-auto">
            Edu network • Select a subject dossier below to open your books and study materials.
          </p>
        </div>
      </section>

      {/* Navigation Breadcrumb & Search Bar */}
      <div className="space-y-4">
        <div className="flex flex-col md:flex-row gap-3 items-stretch md:items-center justify-between">
          {/* Breadcrumb / Back button */}
          <div className="flex items-center gap-3">
            {activeFolder ? (
              <button
                onClick={handleBackToFolders}
                className="flex items-center gap-2 px-4 py-2 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition shadow-xs border border-paper-300 dark:border-darkbg-border"
              >
                <ArrowLeft className="w-3.5 h-3.5" />
                <span>ALL SUBJECT DOSSIERS</span>
              </button>
            ) : (
              <div className="inline-flex items-center gap-2 text-xs font-mono text-ink-600 dark:text-ink-400 uppercase tracking-widest">
                <Folder className="w-4 h-4 text-ochre-500" />
                <span>SELECT A SUBJECT DOSSIER:</span>
              </div>
            )}

            {activeFolder && (
              <span className="text-xs font-mono px-3 py-1 rounded-full bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 font-bold">
                DOSSIER: {activeFolder}
              </span>
            )}
          </div>

          {/* Search Input */}
          <div className="relative flex-1 max-w-md">
            <Search className="w-4 h-4 text-ink-400 absolute left-4 top-1/2 -translate-y-1/2 pointer-events-none" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder={activeFolder ? `Search in ${activeFolder}...` : "Search course codes or topics (e.g. PHY110, CSE111)..."}
              className="w-full pl-11 pr-4 py-2.5 bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-xs border border-paper-300 dark:border-darkbg-border rounded-full text-xs text-ink-900 dark:text-paper-100 placeholder-ink-400 dark:placeholder-ink-500 focus:outline-none focus:ring-2 focus:ring-ink-900 dark:focus:ring-paper-200 transition shadow-xs"
            />
          </div>
        </div>

        {/* Category Tabs (Shown inside opened folder) */}
        {activeFolder && (
          <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none border-b border-paper-300/80 dark:border-darkbg-border pt-1">
            {CATEGORIES.map((cat) => (
              <button
                key={cat.id}
                onClick={() => onCategoryChange ? onCategoryChange(cat.id) : null}
                className={`px-3.5 py-1.5 rounded-full text-xs font-mono tracking-wider transition whitespace-nowrap ${
                  selectedCategory === cat.id
                    ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 font-bold'
                    : 'text-ink-600 dark:text-ink-400 hover:text-ink-900 dark:hover:text-paper-200 hover:bg-paper-200 dark:hover:bg-darkbg-800'
                }`}
              >
                {cat.label}
              </button>
            ))}
            <span className="ml-auto text-[11px] font-mono text-ink-400 dark:text-ink-500 hidden sm:inline">
              {booksInActiveFolder.length} EDITIONS IN THIS DOSSIER
            </span>
          </div>
        )}
      </div>

      {/* Main Content Area */}
      {loading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {Array.from({ length: 6 }).map((_, i) => (
            <div
              key={i}
              className="h-80 rounded-[32px] bg-paper-200/60 dark:bg-darkbg-850 animate-pulse border border-paper-300 dark:border-darkbg-border p-6"
            ></div>
          ))}
        </div>
      ) : activeFolder ? (
        /* STAGE 2: INSIDE SUBJECT FOLDER -> SHOW BOOKS */
        booksInActiveFolder.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 animate-in fade-in duration-200">
            {booksInActiveFolder.map((doc, idx) => (
              <DocumentCard
                key={doc.id}
                doc={doc}
                index={idx + 1}
                onSelect={onSelectDoc}
                user={user}
                onRequireLogin={onRequireLogin}
              />
            ))}
          </div>
        ) : (
          <div className="py-20 text-center bg-paper-100/80 dark:bg-darkbg-900/80 rounded-[32px] border border-paper-300 dark:border-darkbg-border">
            <BookOpen className="w-10 h-10 text-ink-400 dark:text-ink-500 mx-auto mb-3" />
            <h3 className="text-base font-cinzel font-bold text-ink-900 dark:text-paper-50 mb-1">
              No Editions Found in {activeFolder}
            </h3>
            <p className="text-xs text-ink-600 dark:text-ink-400 font-sans">
              Try choosing a different category tab or clearing the search filter.
            </p>
          </div>
        )
      ) : (
        /* STAGE 1: ROOT VIEW -> SHOW ALL SUBJECT CODE DOSSIER FOLDERS */
        filteredCourseCodes.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 animate-in fade-in duration-200">
            {filteredCourseCodes.map((code, idx) => (
              <SubjectFolderCard
                key={code}
                courseCode={code}
                materials={courseGroups[code] || []}
                index={idx + 1}
                onOpenFolder={(c) => handleOpenFolder(c)}
              />
            ))}
          </div>
        ) : (
          <div className="py-20 text-center bg-paper-100/80 dark:bg-darkbg-900/80 rounded-[32px] border border-paper-300 dark:border-darkbg-border">
            <Folder className="w-10 h-10 text-ink-400 dark:text-ink-500 mx-auto mb-3" />
            <h3 className="text-base font-cinzel font-bold text-ink-900 dark:text-paper-50 mb-1">
              No Subject Dossiers Matched
            </h3>
            <p className="text-xs text-ink-600 dark:text-ink-400 font-sans">
              Try searching with another course code (e.g. PHY110, CSE111, MTH165).
            </p>
          </div>
        )
      )}
    </div>
  );
}
