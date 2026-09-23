import React from 'react';
import {
  LogOut,
  ChevronRight,
  ChevronLeft,
  Sun,
  Moon,
  Sparkles,
  ShieldCheck,
  CheckCircle2,
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function Navbar({
  currentView,
  onNavigate,
  onOpenLogin,
  onOpenPlans,
  darkMode,
  onToggleTheme,
  isSubscribed,
  onLogoClick,
  canGoBack = false,
  canGoForward = false,
  onHistoryBack,
  onHistoryForward,
}) {
  const { user, logout } = useAuth();
  const [logoClicked, setLogoClicked] = React.useState(false);

  const handleLogoClick = () => {
    setLogoClicked(true);
    setTimeout(() => setLogoClicked(false), 600);

    if (onLogoClick) {
      onLogoClick();
    } else {
      onNavigate('home');
    }
  };

  return (
    <header className="sticky top-4 z-40 max-w-7xl mx-auto px-4 sm:px-6">
      <div className="bg-paper-50/95 dark:bg-darkbg-900/95 backdrop-blur-md border border-paper-300/90 dark:border-darkbg-border rounded-full px-3 sm:px-6 py-2.5 shadow-pill dark:shadow-pill-dark flex items-center justify-between transition-all gap-2">
        {/* Left: Brand + Back/Forward History Controls */}
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          {/* Back & Forth Navigation Buttons */}
          <div className="flex items-center gap-0.5 sm:gap-1 bg-paper-200/90 dark:bg-darkbg-800 rounded-full p-0.5 sm:p-1 border border-paper-300 dark:border-darkbg-border shadow-xs">
            <button
              onClick={onHistoryBack}
              disabled={!canGoBack}
              className="p-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-25 transition text-ink-800 dark:text-paper-100"
              title="Go Back (Alt + ← / History Back)"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <button
              onClick={onHistoryForward}
              disabled={!canGoForward}
              className="p-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-25 transition text-ink-800 dark:text-paper-100"
              title="Go Forward (Alt + → / History Forward)"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>

          <div className="h-4 w-px bg-paper-300 dark:bg-darkbg-border hidden sm:block"></div>

          {/* Brand with Minimalist Floating Star Logo */}
          <button
            onClick={handleLogoClick}
            className="group relative flex items-center gap-2.5 sm:gap-3 text-left focus:outline-none select-none"
            title="Edu network"
          >
            {/* Logo Disc with clean small-to-big floating pop */}
            <div
              className={`w-7 h-7 sm:w-8 sm:h-8 rounded-full overflow-hidden flex items-center justify-center bg-ink-900 dark:bg-paper-50 border border-paper-300 dark:border-darkbg-border shadow-sm p-0.5 transition-all duration-300 ease-out ${
                logoClicked
                  ? 'scale-125 -translate-y-1 shadow-lg ring-2 ring-[#E5C05B]'
                  : 'group-hover:scale-110 group-hover:-translate-y-0.5'
              }`}
            >
              <img
                src="/logo.png"
                alt="Edu network star logo"
                className="w-full h-full object-contain filter invert dark:invert-0"
              />
            </div>

            <div className="flex items-baseline gap-1.5">
              <span className="font-bold text-ink-900 dark:text-paper-50 text-sm sm:text-base tracking-tight font-sans">
                Edu<span className="font-normal text-ink-600 dark:text-ink-400"> network</span>
              </span>
              <span className="hidden lg:inline-block text-[10px] font-mono tracking-widest text-ink-400 uppercase">
                • ARCHIVE / 2026
              </span>
            </div>
          </button>
        </div>

        {/* Center Links */}
        <nav className="hidden md:flex items-center gap-5 lg:gap-6 text-xs font-mono font-medium text-ink-600 dark:text-ink-400">
          <button
            onClick={() => onNavigate('home')}
            className={`transition tracking-wide ${
              currentView === 'home'
                ? 'text-ink-900 dark:text-paper-50 font-bold'
                : 'hover:text-ink-900 dark:hover:text-paper-50'
            }`}
          >
            HOME
          </button>
          <span className="text-paper-300 dark:text-ink-800">/</span>
          <button
            onClick={() => onNavigate('catalog')}
            className={`transition tracking-wide ${
              currentView === 'catalog'
                ? 'text-ink-900 dark:text-paper-50 font-bold'
                : 'hover:text-ink-900 dark:hover:text-paper-50'
            }`}
          >
            SUBJECT DOSSIERS
          </button>
          <span className="text-paper-300 dark:text-ink-800">/</span>
          <button
            onClick={() => onNavigate('exams')}
            className={`transition tracking-wide flex items-center gap-1.5 ${
              currentView === 'exams'
                ? 'text-amber-500 dark:text-amber-400 font-bold'
                : 'hover:text-amber-600 dark:hover:text-amber-300'
            }`}
          >
            <span>PRACTICE EXAM</span>
            <span className="px-1.5 py-0.2 rounded-full bg-amber-500 text-ink-950 font-black text-[9px] tracking-tighter uppercase animate-pulse">
              NEW
            </span>
          </button>

          {/* Only show pricing link if NOT subscribed */}
          {(!user || !isSubscribed) && (
            <>
              <span className="text-paper-300 dark:text-ink-800">/</span>
              <button
                onClick={onOpenPlans}
                className="text-ochre-500 font-bold hover:underline transition tracking-wide flex items-center gap-1"
              >
                <Sparkles className="w-3 h-3" />
                <span>SEMESTER PASS</span>
              </button>
            </>
          )}
        </nav>

        {/* Right Tools: Dark Mode Toggle + Student Pass / Status */}
        <div className="flex items-center gap-2 sm:gap-2.5 shrink-0">
          {/* Theme Toggle */}
          <button
            onClick={onToggleTheme}
            className="p-2 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-700 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border transition shadow-xs"
            title={darkMode ? "Switch to Light Paper Theme" : "Switch to Black Grainy Dark Theme"}
          >
            {darkMode ? <Sun className="w-3.5 h-3.5 text-ochre-400" /> : <Moon className="w-3.5 h-3.5" />}
          </button>

          {user ? (
            <div className="flex items-center gap-2 bg-paper-200/80 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border rounded-full py-1 pl-1.5 pr-3 shadow-xs">
              {user.picture ? (
                <img
                  src={user.picture}
                  alt={user.name}
                  className="w-6 h-6 rounded-full object-cover border border-ink-900/20 dark:border-paper-300/20"
                />
              ) : (
                <div className="w-6 h-6 rounded-full bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 flex items-center justify-center text-[10px] font-bold">
                  {user.name ? user.name[0].toUpperCase() : 'S'}
                </div>
              )}
              <div className="flex flex-col text-left">
                <div className="flex items-center gap-1">
                  <span className="text-[11px] font-bold text-ink-900 dark:text-paper-50 leading-tight truncate max-w-[70px] sm:max-w-[120px]">
                    {user.name}
                  </span>
                  {isSubscribed && (
                    <CheckCircle2 className="w-3 h-3 text-emerald-600 dark:text-emerald-400 shrink-0" title="Active Pass" />
                  )}
                </div>
                <span className="text-[9px] font-mono text-ink-600 dark:text-ink-400 truncate max-w-[70px] sm:max-w-[120px]">
                  {isSubscribed ? 'PRO PASS ACTIVE' : user.email}
                </span>
              </div>
              <button
                onClick={logout}
                className="ml-1 p-1 rounded-full text-ink-400 hover:text-terracotta-600 transition"
                title="Sign Out"
              >
                <LogOut className="w-3.5 h-3.5" />
              </button>
            </div>
          ) : (
            <button
              onClick={onOpenLogin}
              className="group flex items-center gap-1.5 sm:gap-2 pl-3 sm:pl-4 pr-2 sm:pr-3 py-1.5 rounded-full bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs font-semibold tracking-wide transition shadow-sm"
            >
              <span>Student Pass</span>
              <span className="w-5 h-5 rounded-full bg-[#E5C05B] text-ink-900 flex items-center justify-center transition-transform group-hover:translate-x-0.5">
                <ChevronRight className="w-3.5 h-3.5 stroke-[3]" />
              </span>
            </button>
          )}
        </div>
      </div>
    </header>
  );
}
