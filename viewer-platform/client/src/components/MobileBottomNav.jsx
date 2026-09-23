import React from 'react';
import { Home, BookOpen, Sparkles, User, Sun, Moon, LogIn } from 'lucide-react';

export default function MobileBottomNav({
  currentView,
  onNavigateHome,
  onNavigateCatalog,
  onNavigateExams,
  onOpenPlans,
  onOpenLogin,
  user,
  darkMode,
  onToggleTheme,
  isSubscribed
}) {
  return (
    <nav className="fixed bottom-0 left-0 right-0 z-40 bg-paper-100/95 dark:bg-darkbg-900/95 backdrop-blur-md border-t border-paper-300/80 dark:border-darkbg-border safe-area-nav sm:hidden transition-colors shadow-2xl">
      <div className="grid grid-cols-5 h-14 items-center px-1">
        {/* Home */}
        <button
          onClick={onNavigateHome}
          className={`flex flex-col items-center justify-center py-1 rounded-lg transition-all ${
            currentView === 'home' && !user
              ? 'text-ink-900 dark:text-gold-400 font-semibold scale-105'
              : 'text-ink-500 dark:text-ink-400 hover:text-ink-900 dark:hover:text-paper-100'
          }`}
        >
          <Home className="w-5 h-5 mb-0.5" />
          <span className="text-[10px] tracking-tight">Home</span>
        </button>

        {/* Courses / Catalog */}
        <button
          onClick={onNavigateCatalog}
          className={`flex flex-col items-center justify-center py-1 rounded-lg transition-all relative ${
            currentView === 'catalog'
              ? 'text-ink-900 dark:text-gold-400 font-semibold scale-105'
              : 'text-ink-500 dark:text-ink-400 hover:text-ink-900 dark:hover:text-paper-100'
          }`}
        >
          <BookOpen className="w-5 h-5 mb-0.5" />
          <span className="text-[10px] tracking-tight">Courses</span>
          {currentView === 'catalog' && (
            <span className="absolute -bottom-1 w-1 h-1 bg-gold-500 rounded-full"></span>
          )}
        </button>

        {/* Practice Exams (NEW FEATURE) */}
        <button
          onClick={onNavigateExams}
          className={`flex flex-col items-center justify-center py-1 rounded-lg transition-all relative ${
            currentView === 'exams'
              ? 'text-amber-500 dark:text-amber-400 font-bold scale-105'
              : 'text-amber-600 dark:text-amber-400/80 hover:text-amber-500'
          }`}
        >
          <div className="relative">
            <span className="absolute -top-1 -right-2 px-1 py-0.2 rounded-full bg-amber-500 text-ink-950 font-black text-[7px] leading-tight animate-pulse">
              NEW
            </span>
            <Sparkles className="w-5 h-5 mb-0.5" />
          </div>
          <span className="text-[10px] tracking-tight font-semibold">Exams</span>
          {currentView === 'exams' && (
            <span className="absolute -bottom-1 w-1 h-1 bg-amber-500 rounded-full"></span>
          )}
        </button>

        {/* Pass / Plans */}
        <button
          onClick={onOpenPlans}
          className="flex flex-col items-center justify-center py-1 rounded-lg transition-all text-ink-500 dark:text-ink-400 relative"
        >
          <span className="text-xs font-mono font-bold mb-0.5">₹</span>
          <span className="text-[10px] font-medium tracking-tight">
            {isSubscribed ? 'Pro Pass' : 'Pass'}
          </span>
        </button>

        {/* Account / Login */}
        {user ? (
          <button
            onClick={onOpenLogin}
            className="flex flex-col items-center justify-center py-1 rounded-lg transition-all text-ink-700 dark:text-ink-300"
          >
            {user.picture ? (
              <img
                src={user.picture}
                alt={user.name || 'User'}
                className="w-5 h-5 rounded-full border border-gold-500 mb-0.5 object-cover"
              />
            ) : (
              <User className="w-5 h-5 mb-0.5 text-gold-500" />
            )}
            <span className="text-[10px] tracking-tight truncate max-w-[50px]">
              {user.name ? user.name.split(' ')[0] : 'Account'}
            </span>
          </button>
        ) : (
          <button
            onClick={onOpenLogin}
            className="flex flex-col items-center justify-center py-1 rounded-lg transition-all text-ink-700 dark:text-paper-200"
          >
            <LogIn className="w-5 h-5 mb-0.5" />
            <span className="text-[10px] tracking-tight">Sign In</span>
          </button>
        )}
      </div>
    </nav>
  );
}
