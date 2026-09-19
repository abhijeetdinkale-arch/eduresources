import React from 'react';
import { Folder, ArrowRight } from 'lucide-react';

const COURSE_INFO = {
  PHY110: {
    name: 'Engineering Physics & Derivations',
    desc: 'Complete course textbook, wave optics, lasers, fiber communication, quantum mechanics & solid state.',
    color: 'from-[#7A3E32] to-[#451E16] dark:from-[#4E2720] dark:to-[#28130E]',
    tag: '#PHY110-TEXTBOOK',
  },
  PHY175: {
    name: 'Engineering Physics Question Bank & Formulas',
    desc: 'High-yield 300+ MCQ question bank, unit cheatsheets, formula book & comprehensive solutions.',
    color: 'from-[#8A4A3C] to-[#55251B] dark:from-[#5A2C23] dark:to-[#31150F]',
    tag: '#PHY175-QB-FORMULAS',
  },
  CSE111: {
    name: 'Fundamentals of Computing & IT',
    desc: 'Binary arithmetic, logic gates, computer architecture, Linux OS & programming systems.',
    color: 'from-[#3A4454] to-[#1E2530] dark:from-[#252C36] dark:to-[#12161D]',
    tag: '#CSE111-COMPUTING',
  },
  CSE326: {
    name: 'Web Development & Modern Technologies',
    desc: 'Semantic HTML5, CSS3 Grid/Flexbox, JavaScript ES6+, DOM manipulation & full-stack blueprints.',
    color: 'from-[#6E4B3B] to-[#3B261D] dark:from-[#473026] dark:to-[#221611]',
    tag: '#CSE326-WEB-DEV',
  },
  MTH165: {
    name: 'Mathematics (Calculus, Integrals & Vectors)',
    desc: 'Differential calculus, multiple integrals, vector spaces, infinite series & ODEs with solutions.',
    color: 'from-[#2F4858] to-[#1A2C38] dark:from-[#1D2D37] dark:to-[#0F1920]',
    tag: '#MTH165-CALCULUS',
  },
  INT335: {
    name: 'Cloud Computing & Distributed Systems',
    desc: 'Virtualization, microservices, cloud deployment models, AWS/GCP paradigms & revision sets.',
    color: 'from-[#4B5842] to-[#273320] dark:from-[#2F372A] dark:to-[#171E14]',
    tag: '#INT335-CLOUD',
  },
  INT108: {
    name: 'Python Programming — Study Guide & Mastery',
    desc: 'Python fundamentals, OOP, data structures, NumPy, Pandas, file handling & regex.',
    color: 'from-[#3B5E55] to-[#1E352F] dark:from-[#254039] dark:to-[#0F1E1A]',
    tag: '#INT108-PYTHON',
  },
  ECE249: {
    name: 'Digital Electronics & Circuits Sample Papers',
    desc: 'Flip-flops, synchronous counters, finite state machines, microcontrollers & test papers.',
    color: 'from-[#4A3B6E] to-[#271E3D] dark:from-[#31264B] dark:to-[#160E24]',
    tag: '#ECE249-DIGITAL',
  },
  ECE279: {
    name: 'Electrical & Electronics Handwritten Notes',
    desc: 'Kirchhoff’s laws, AC circuit phasors, transformer principles & semiconductor diodes.',
    color: 'from-[#5E4E3B] to-[#352B1E] dark:from-[#3F3324] dark:to-[#1E170E]',
    tag: '#ECE279-NOTES',
  },
  MEC136: {
    name: 'Engineering Graphics & CAD Lecture PPTs',
    desc: 'Orthographic projections, isometric sections & AutoCAD standard drafting commands.',
    color: 'from-[#5E3B4E] to-[#351E2B] dark:from-[#402434] dark:to-[#1E0F18]',
    tag: '#MEC136-GRAPHICS',
  },
};

export default function SubjectFolderCard({ courseCode, materials, onOpenFolder, index = 1 }) {
  const info = COURSE_INFO[courseCode] || {
    name: `${courseCode} Course Repository`,
    desc: 'Curated curriculum materials, textbooks, exam companion sets, and notes.',
    color: 'from-[#2D3142] to-[#1B1D28] dark:from-[#1E212D] dark:to-[#101117]',
    tag: `#${courseCode}`,
  };

  const count = materials.length;
  const serialNo = String(index).padStart(2, '0');
  const categories = Array.from(new Set(materials.map((m) => m.category)));

  return (
    <div
      onClick={() => onOpenFolder(courseCode)}
      className="group relative bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-xs rounded-[32px] border border-paper-300/80 dark:border-darkbg-border p-6 transition-all duration-300 hover:shadow-ticket dark:hover:shadow-ticket-dark hover:-translate-y-1.5 cursor-pointer flex flex-col justify-between overflow-hidden"
    >
      <div className="absolute top-4 left-4 punch-hole opacity-70"></div>
      <div className="absolute top-4 right-4 punch-hole opacity-70"></div>

      <div>
        <div
          className={`w-full h-36 rounded-2xl bg-gradient-to-br ${info.color} p-4 text-paper-50 flex flex-col justify-between shadow-inner relative overflow-hidden mb-4 border border-white/5`}
        >
          <img
            src="/logo.png"
            alt="Star watermark"
            className="absolute -right-6 -bottom-6 w-28 h-28 object-contain opacity-25 filter invert"
          />

          <div className="flex items-center justify-between z-10">
            <span className="text-[10px] font-mono tracking-widest uppercase bg-black/40 backdrop-blur-xs px-2.5 py-0.5 rounded-full text-paper-200 border border-white/10 flex items-center gap-1.5">
              <Folder className="w-3 h-3 text-ochre-400" />
              <span>DOSSIER {serialNo}</span>
            </span>
            <span className="text-[10px] font-mono text-paper-300 tracking-wider">
              {count} {count === 1 ? 'EDITION' : 'EDITIONS'}
            </span>
          </div>

          <div className="z-10">
            <span className="text-[10px] font-mono text-ochre-400 tracking-widest uppercase block mb-0.5">
              {info.tag}
            </span>
            <h4 className="text-xl font-cinzel font-black text-paper-50 truncate tracking-tight">
              {courseCode}
            </h4>
          </div>
        </div>

        <div className="flex items-center justify-between border-b border-ink-900/10 dark:border-white/10 pb-2.5 mb-3 text-xs font-mono text-ink-600 dark:text-ink-400">
          <div className="flex items-center gap-2">
            <span className="font-bold text-ink-900 dark:text-paper-100">{serialNo}</span>
            <span className="text-paper-400 dark:text-ink-600">—</span>
            <span>10</span>
          </div>
          <span className="text-[10px] font-mono text-ink-500 uppercase">OFFICIAL SYLLABUS</span>
          <span className="text-[10px] text-ink-400 dark:text-ink-500">2026</span>
        </div>

        <h3 className="text-base font-sans font-bold text-ink-900 dark:text-paper-50 group-hover:text-terracotta-600 dark:group-hover:text-ochre-400 transition tracking-tight leading-snug line-clamp-1 mb-1.5">
          {info.name}
        </h3>

        <p className="text-xs font-sans text-ink-600 dark:text-ink-400 line-clamp-2 mb-4 leading-relaxed">
          {info.desc}
        </p>

        <div className="flex flex-wrap gap-1.5 mb-4">
          {categories.slice(0, 3).map((cat) => (
            <span
              key={cat}
              className="px-2 py-0.5 rounded-md text-[10px] font-mono bg-paper-200/80 dark:bg-darkbg-900 text-ink-700 dark:text-paper-300 border border-paper-300/60 dark:border-darkbg-border"
            >
              {cat}
            </span>
          ))}
          {categories.length > 3 && (
            <span className="px-1.5 py-0.5 rounded-md text-[10px] font-mono bg-paper-200/80 dark:bg-darkbg-900 text-ink-500">
              +{categories.length - 3} more
            </span>
          )}
        </div>
      </div>

      <div className="pt-3 border-t border-dashed border-ink-900/20 dark:border-white/15 flex items-center justify-between text-xs">
        <div className="flex flex-col">
          <span className="text-[9px] font-mono uppercase tracking-widest text-ink-400 dark:text-ink-500">
            FOLDER / {courseCode}
          </span>
          <div className="barcode text-[11px] font-bold text-ink-800 dark:text-paper-300 tracking-tight select-none">
            ||| | |||| | ||| |||| |
          </div>
        </div>

        <button
          onClick={(e) => {
            e.stopPropagation();
            onOpenFolder(courseCode);
          }}
          className="flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide transition bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 shadow-xs group-hover:shadow-md"
        >
          <span>OPEN FOLDER</span>
          <ArrowRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" />
        </button>
      </div>
    </div>
  );
}
