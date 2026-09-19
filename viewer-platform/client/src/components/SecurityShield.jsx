import React, { useState, useEffect } from 'react';
import { EyeOff } from 'lucide-react';

export default function SecurityShield({ isViewingDocument }) {
  const [isShieldActive, setIsShieldActive] = useState(false);
  const [shieldReason, setShieldReason] = useState('');

  useEffect(() => {
    if (!isViewingDocument) {
      setIsShieldActive(false);
      return;
    }

    const handleBlur = () => {
      setIsShieldActive(true);
      setShieldReason('Screen Capture / Window Focus Loss Detected');
    };

    const handleFocus = () => {
      setTimeout(() => {
        setIsShieldActive(false);
      }, 300);
    };

    const handleVisibilityChange = () => {
      if (document.hidden) {
        setIsShieldActive(true);
        setShieldReason('Window Backgrounded / Screen Capture Prevented');
      } else {
        setTimeout(() => setIsShieldActive(false), 300);
      }
    };

    const handleKeyDown = (e) => {
      if (e.key === 'PrintScreen' || e.code === 'PrintScreen') {
        e.preventDefault();
        setIsShieldActive(true);
        setShieldReason('Screenshot Key (PrintScreen) Blocked');
        try {
          navigator.clipboard.writeText('');
        } catch {}
        return;
      }

      if ((e.ctrlKey || e.metaKey) && (e.key === 's' || e.key === 'S')) {
        e.preventDefault();
        alert('⚠️ Edu network materials are protected by academic copyright. Downloads are disabled.');
        return;
      }

      if ((e.ctrlKey || e.metaKey) && (e.key === 'p' || e.key === 'P')) {
        e.preventDefault();
        alert('⚠️ Printing documents is disabled for security.');
        return;
      }

      if (
        e.key === 'F12' ||
        ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'C' || e.key === 'c' || e.key === 'J' || e.key === 'j')) ||
        ((e.metaKey || e.altKey) && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'C' || e.key === 'c'))
      ) {
        e.preventDefault();
      }
    };

    const handleContextMenu = (e) => {
      e.preventDefault();
      return false;
    };

    window.addEventListener('blur', handleBlur);
    window.addEventListener('focus', handleFocus);
    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('keydown', handleKeyDown, true);
    document.addEventListener('contextmenu', handleContextMenu);

    return () => {
      window.removeEventListener('blur', handleBlur);
      window.removeEventListener('focus', handleFocus);
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      window.removeEventListener('keydown', handleKeyDown, true);
      document.removeEventListener('contextmenu', handleContextMenu);
    };
  }, [isViewingDocument]);

  if (!isShieldActive) return null;

  return (
    <div
      onClick={() => setIsShieldActive(false)}
      className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-paper-100/90 dark:bg-darkbg-950/90 backdrop-blur-2xl text-center p-6 cursor-pointer select-none transition-all duration-200"
    >
      <div className="bg-paper-50 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border rounded-[32px] p-8 max-w-md shadow-floating flex flex-col items-center relative overflow-hidden">
        {/* Star Logo */}
        <div className="w-14 h-14 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center mb-4 shadow-md p-2.5 animate-pulse">
          <img
            src="/logo.png"
            alt="Edu network star"
            className="w-full h-full object-contain filter invert dark:invert-0"
          />
        </div>

        <h3 className="text-xl font-cinzel font-bold text-ink-900 dark:text-paper-50 mb-1">
          Edu<span className="font-serif italic font-normal text-ink-600 dark:text-ink-400"> network</span>
        </h3>

        <p className="text-xs font-mono uppercase tracking-widest text-terracotta-600 dark:text-ochre-400 mb-3 font-semibold">
          • ARCHIVAL SHIELD ENGAGED •
        </p>

        <p className="text-xs font-sans text-ink-600 dark:text-ink-400 mb-5 leading-relaxed">
          {shieldReason || 'Screen capture and window unfocus detected.'}
        </p>

        <div className="bg-paper-200/80 dark:bg-darkbg-900 rounded-2xl p-4 text-[11px] text-ink-700 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border font-mono mb-6 w-full text-left space-y-1">
          <div>✦ Snipping & recording tools are shielded.</div>
          <div>✦ Anti-screenshot blur active.</div>
          <div>✦ Click anywhere inside to resume reading.</div>
        </div>

        <button
          onClick={() => setIsShieldActive(false)}
          className="w-full py-3 px-4 bg-ink-900 dark:bg-paper-100 hover:bg-black dark:hover:bg-white text-paper-50 dark:text-ink-900 rounded-full text-xs font-semibold tracking-wider uppercase transition shadow-md flex items-center justify-center gap-2"
        >
          <EyeOff className="w-4 h-4" />
          <span>Resume Safe Reading</span>
        </button>
      </div>
    </div>
  );
}
