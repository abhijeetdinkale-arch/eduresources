import React from 'react';
import { Lock, ArrowUpRight } from 'lucide-react';

const COURSE_THEMES = {
  CSE111: {
    bg: 'bg-[#EDE8DC] dark:bg-[#15171C]',
    headerBg: 'from-[#3A4454] to-[#1E2530] dark:from-[#252C36] dark:to-[#12161D]',
    accent: '#3A4454',
  },
  CSE326: {
    bg: 'bg-[#F2ECE1] dark:bg-[#1A1614]',
    headerBg: 'from-[#6E4B3B] to-[#3B261D] dark:from-[#473026] dark:to-[#221611]',
    accent: '#6E4B3B',
  },
  MTH165: {
    bg: 'bg-[#ECEAE4] dark:bg-[#14181B]',
    headerBg: 'from-[#2F4858] to-[#1A2C38] dark:from-[#1D2D37] dark:to-[#0F1920]',
    accent: '#2F4858',
  },
  MTH174: {
    bg: 'bg-[#E8EEF8] dark:bg-[#0D1527]',
    headerBg: 'from-[#1E3A8A] to-[#0F172A] dark:from-[#172554] dark:to-[#090D16]',
    accent: '#1E3A8A',
  },
  CHE110: {
    bg: 'bg-[#E8F5E9] dark:bg-[#0B1E12]',
    headerBg: 'from-[#14532D] to-[#052E16] dark:from-[#0F391F] dark:to-[#031A0C]',
    accent: '#14532D',
  },
  ECE120: {
    bg: 'bg-[#FCE7F3] dark:bg-[#200A15]',
    headerBg: 'from-[#831843] to-[#500724] dark:from-[#5C0F2F] dark:to-[#2D0414]',
    accent: '#831843',
  },
  CSR101: {
    bg: 'bg-[#E0F2FE] dark:bg-[#061D2B]',
    headerBg: 'from-[#0E7490] to-[#155E75] dark:from-[#083344] dark:to-[#041D26]',
    accent: '#0E7490',
  },
  CSR102: {
    bg: 'bg-[#FEF3C7] dark:bg-[#261B05]',
    headerBg: 'from-[#B45309] to-[#78350F] dark:from-[#713F12] dark:to-[#381A05]',
    accent: '#B45309',
  },
  ECE131: {
    bg: 'bg-[#EDE9FE] dark:bg-[#13112E]',
    headerBg: 'from-[#4338CA] to-[#1E1B4B] dark:from-[#312E81] dark:to-[#0F0D2E]',
    accent: '#4338CA',
  },
  CSE105: {
    bg: 'bg-[#F1F5F9] dark:bg-[#0F172A]',
    headerBg: 'from-[#1E293B] to-[#0F172A] dark:from-[#1E293B] dark:to-[#020617]',
    accent: '#1E293B',
  },
  ECE181: {
    bg: 'bg-[#D1FAE5] dark:bg-[#042017]',
    headerBg: 'from-[#047857] to-[#064E3B] dark:from-[#065F46] dark:to-[#022C22]',
    accent: '#047857',
  },
  Physics: {
    bg: 'bg-[#EBE5DB] dark:bg-[#1A1413]',
    headerBg: 'from-[#7A3E32] to-[#451E16] dark:from-[#4E2720] dark:to-[#28130E]',
    accent: '#7A3E32',
  },
  INT335: {
    bg: 'bg-[#EBE9E1] dark:bg-[#141813]',
    headerBg: 'from-[#4B5842] to-[#273320] dark:from-[#2F372A] dark:to-[#171E14]',
    accent: '#4B5842',
  },
  DEFAULT: {
    bg: 'bg-[#EAE5D9] dark:bg-[#16161A]',
    headerBg: 'from-[#2D3142] to-[#1B1D28] dark:from-[#1E212D] dark:to-[#101117]',
    accent: '#2D3142',
  }
};

export default function DocumentCard({ doc, onSelect, user, onRequireLogin, index = 1 }) {
  const theme = COURSE_THEMES[doc.courseCode] || COURSE_THEMES.DEFAULT;
  const serialNo = String(index).padStart(2, '0');

  const handleClick = () => {
    if (!user) {
      onRequireLogin();
      return;
    }
    onSelect(doc);
  };

  return (
    <div
      onClick={handleClick}
      className={`group relative ${theme.bg} rounded-[28px] border border-paper-300/80 dark:border-darkbg-border p-5 transition-all duration-300 hover:shadow-ticket dark:hover:shadow-ticket-dark hover:-translate-y-1 cursor-pointer flex flex-col justify-between overflow-hidden`}
    >
      {/* Top Punch Hole Accents */}
      <div className="absolute top-4 left-4 punch-hole opacity-70"></div>
      <div className="absolute top-4 right-4 punch-hole opacity-70"></div>

      <div>
        {/* Ticket Art Header Preview */}
        <div className={`w-full h-36 rounded-2xl bg-gradient-to-br ${theme.headerBg} p-4 text-paper-50 flex flex-col justify-between shadow-inner relative overflow-hidden mb-4 border border-white/5`}>
          <img
            src="/logo.png"
            alt="Star watermark"
            className="absolute -right-6 -bottom-6 w-28 h-28 object-contain opacity-25 filter invert"
          />

          <div className="flex items-center justify-between z-10">
            <span className="text-[10px] font-mono tracking-widest uppercase bg-black/40 backdrop-blur-xs px-2 py-0.5 rounded-full text-paper-200 border border-white/10">
              PASS {serialNo} • {doc.courseCode}
            </span>
            <span className="text-[10px] font-mono text-paper-300 tracking-wider">
              EDUNET / 2026
            </span>
          </div>

          <div className="z-10">
            <span className="text-xs font-serif italic text-paper-300 block mb-0.5">
              Official University Material
            </span>
            <h4 className="text-sm font-bold text-paper-50 truncate tracking-tight font-sans">
              {doc.title}
            </h4>
          </div>
        </div>

        {/* Date / Metadata Stamp Line */}
        <div className="flex items-center justify-between border-b border-ink-900/10 dark:border-white/10 pb-2.5 mb-3 text-xs font-mono text-ink-600 dark:text-ink-400">
          <div className="flex items-center gap-2">
            <span className="font-bold text-ink-900 dark:text-paper-100">{serialNo}</span>
            <span className="text-paper-400 dark:text-ink-600">—</span>
            <span>10</span>
          </div>
          <span className="px-2 py-0.5 rounded text-[10px] font-mono font-medium tracking-wide uppercase bg-ink-900/5 dark:bg-white/5 text-ink-800 dark:text-paper-200 border border-transparent dark:border-white/10">
            {doc.category}
          </span>
          <span className="text-[10px] text-ink-400 dark:text-ink-500">2026</span>
        </div>

        {/* Main Editorial Typography */}
        <h3 className="text-lg font-cinzel font-bold text-ink-900 dark:text-paper-50 group-hover:text-terracotta-600 dark:group-hover:text-ochre-400 transition tracking-tight leading-snug line-clamp-2 mb-1.5">
          {doc.title}
        </h3>

        <p className="text-xs font-sans text-ink-600 dark:text-ink-400 line-clamp-2 mb-4 leading-relaxed">
          {doc.subtitle || `${doc.courseCode} official reference edition. Complete curriculum coverage and question blueprints.`}
        </p>
      </div>

      {/* Perforated Tear-off Ticket Bottom */}
      <div className="pt-3 border-t border-dashed border-ink-900/20 dark:border-white/15 flex items-center justify-between text-xs">
        <div className="flex flex-col">
          <span className="text-[9px] font-mono uppercase tracking-widest text-ink-400 dark:text-ink-500">
            TIKET / {doc.id.substring(0, 6).toUpperCase()}
          </span>
          {/* Simulated Barcode */}
          <div className="barcode text-[11px] font-bold text-ink-800 dark:text-paper-300 tracking-tight select-none">
            ||| | |||| | ||| |||| |
          </div>
        </div>

        <button
          onClick={(e) => {
            e.stopPropagation();
            handleClick();
          }}
          className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-semibold tracking-wide transition ${
            user
              ? 'bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 shadow-xs group-hover:shadow-md'
              : 'bg-paper-300 dark:bg-darkbg-700 hover:bg-paper-400 dark:hover:bg-darkbg-600 text-ink-900 dark:text-paper-200'
          }`}
        >
          {user ? (
            <>
              <span>OPEN</span>
              <ArrowUpRight className="w-3.5 h-3.5" />
            </>
          ) : (
            <>
              <Lock className="w-3 h-3 text-terracotta-600 dark:text-ochre-400" />
              <span>LOCK</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}
