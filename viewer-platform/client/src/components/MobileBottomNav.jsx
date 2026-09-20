import React from 'react';
import { Home, BookOpen, Sparkles, User, Sun, Moon, LogIn } from 'lucide-react';

export default function MobileBottomNav({
  currentView,
  onNavigateHome,
  onNavigateCatalog,
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

        {/* Pass / Plans */}
        <button
          onClick={onOpenPlans}
          className="flex flex-col items-center justify-center py-1 rounded-lg transition-all text-gold-600 dark:text-gold-400 relative"
        >
          <div className="w-6 h-6 rounded-full bg-gold-500/15 dark:bg-gold-400/20 flex items-center justify-center mb-0.5">
            <Sparkles className="w-3.5 h-3.5 animate-pulse" />
          </div>
          <span className="text-[10px] font-medium tracking-tight">
            {isSubscribed ? 'Pro Pass' : 'Pass'}
          </span>
        </button>

        {/* Theme Switcher */}
        <button
          onClick={onToggleTheme}
          className="flex flex-col items-center justify-center py-1 rounded-lg transition-all text-ink-500 dark:text-ink-400 hover:text-ink-900 dark:hover:text-paper-100"
        >
          {darkMode ? (
            <Sun className="w-5 h-5 mb-0.5 text-gold-400" />
          ) : (
            <Moon className="w-5 h-5 mb-0.5" />
          )}
          <span className="text-[10px] tracking-tight">{darkMode ? 'Light' : 'Dark'}</span>
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
