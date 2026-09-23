import React, { useState } from 'react';
import {
  Sparkles,
  Timer,
  Award,
  BookOpen,
  ArrowRight,
  CheckCircle2,
  AlertCircle,
  HelpCircle,
  Zap,
  TrendingUp,
  Layers,
  ChevronRight,
  Star
} from 'lucide-react';
import { MTH165_MOCK_TESTS } from '../../data/mth165_mock_tests';

export default function ExamHub({ onStartExam, onBackToCatalog }) {
  const [selectedCourse, setSelectedCourse] = useState('MTH165');
  const [selectedCategoryFilter, setSelectedCategoryFilter] = useState('All');

  // Load saved test results from localStorage
  const getSavedResults = (testId) => {
    try {
      const raw = localStorage.getItem(`edunet_exam_result_${testId}`);
      if (raw) return JSON.parse(raw);
    } catch {}
    return null;
  };

  const coursesList = [
    { code: 'MTH165', name: 'Mathematics for Engineers', testsCount: 5, active: true, color: 'from-blue-600 to-indigo-600' },
    { code: 'PHY175', name: 'Engineering Physics & Waves', testsCount: 'Coming Soon', active: false, color: 'from-emerald-600 to-teal-600' },
    { code: 'CSE111', name: 'Fundamentals of Computing', testsCount: 'Coming Soon', active: false, color: 'from-amber-600 to-orange-600' },
    { code: 'CSE326', name: 'Web Development & Scripting', testsCount: 'Coming Soon', active: false, color: 'from-purple-600 to-pink-600' },
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10 space-y-8 animate-fadeIn">
      {/* 1. Header Banner with Quzi-inspired gradient card & NEW FEATURE badge */}
      <div className="relative rounded-3xl p-6 sm:p-10 overflow-hidden bg-gradient-to-br from-indigo-950 via-slate-900 to-zinc-950 border border-indigo-500/20 shadow-2xl text-white">
        {/* Ambient background glow */}
        <div className="absolute -right-20 -top-20 w-80 h-80 rounded-full bg-indigo-500/20 blur-3xl pointer-events-none"></div>
        <div className="absolute right-40 -bottom-20 w-80 h-80 rounded-full bg-amber-500/15 blur-3xl pointer-events-none"></div>

        <div className="relative z-10 max-w-3xl space-y-4">
          {/* Glowing Animated NEW FEATURE Badge */}
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-gradient-to-r from-amber-500/20 to-ochre-500/20 border border-amber-400/40 text-amber-300 text-xs font-mono font-bold tracking-wider shadow-sm">
            <span className="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
            <span>✨ NEW FEATURE • PRACTICE EXAMS SUITE</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-cinzel font-black tracking-tight leading-tight">
            Midterm Examination <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-white font-serif italic font-normal">
              Timed Mock Mastery
            </span>
          </h1>

          <p className="text-sm sm:text-base text-zinc-300 font-sans leading-relaxed max-w-2xl">
            Simulate real university midterm exam conditions with authentic previous year papers, precise <span className="text-amber-300 font-semibold">+1.0 / -0.25 negative marking</span>, interactive 30-question progress grid, and <span className="text-amber-300 font-semibold">step-by-step animated solutions</span>.
          </p>

          {/* Quick tags badge pill row (Quzi style) */}
          <div className="flex flex-wrap items-center gap-2 pt-2">
            <span className="px-2.5 py-1 rounded-full bg-white/10 text-white/90 text-[11px] font-mono border border-white/10">
              #LinearAlgebra
            </span>
            <span className="px-2.5 py-1 rounded-full bg-white/10 text-white/90 text-[11px] font-mono border border-white/10">
              #Eigenvalues
            </span>
            <span className="px-2.5 py-1 rounded-full bg-white/10 text-white/90 text-[11px] font-mono border border-white/10">
              #RolleTheorem
            </span>
            <span className="px-2.5 py-1 rounded-full bg-white/10 text-white/90 text-[11px] font-mono border border-white/10">
              #TaylorSeries
            </span>
            <span className="px-2.5 py-1 rounded-full bg-white/10 text-white/90 text-[11px] font-mono border border-white/10">
              #DefiniteIntegrals
            </span>
          </div>
        </div>
      </div>

      {/* 2. Course Selection Carousel / Grid (Quizzax style) */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Layers className="w-5 h-5 text-ink-700 dark:text-paper-300" />
            <h2 className="text-lg font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
              Select Examination Course
            </h2>
          </div>
          <span className="text-xs font-mono text-ink-500 dark:text-ink-400">
            5 MOCK TESTS ACTIVE
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
          {coursesList.map((c) => (
            <button
              key={c.code}
              onClick={() => c.active && setSelectedCourse(c.code)}
              disabled={!c.active}
              className={`text-left p-4 rounded-2xl border transition-all relative overflow-hidden ${
                selectedCourse === c.code && c.active
                  ? 'bg-paper-50 dark:bg-darkbg-800 border-amber-500/80 dark:border-amber-400/80 shadow-md ring-2 ring-amber-500/20'
                  : c.active
                  ? 'bg-paper-100/80 dark:bg-darkbg-900/80 border-paper-300 dark:border-darkbg-border hover:border-paper-400 dark:hover:border-darkbg-700'
                  : 'bg-paper-200/40 dark:bg-darkbg-950/40 border-dashed border-paper-300 dark:border-darkbg-border opacity-60 cursor-not-allowed'
              }`}
            >
              <div className="flex items-start justify-between mb-2">
                <span className="font-mono font-bold text-xs px-2 py-0.5 rounded bg-paper-200 dark:bg-darkbg-700 text-ink-900 dark:text-paper-100">
                  {c.code}
                </span>
                {selectedCourse === c.code && c.active && (
                  <CheckCircle2 className="w-4 h-4 text-amber-500 shrink-0" />
                )}
              </div>
              <p className="font-semibold text-xs sm:text-sm text-ink-900 dark:text-paper-100 leading-tight">
                {c.name}
              </p>
              <p className="text-[11px] font-mono text-ink-500 dark:text-ink-400 mt-2">
                {typeof c.testsCount === 'number' ? `${c.testsCount} Mock Papers Available` : c.testsCount}
              </p>
            </button>
          ))}
        </div>
      </div>

      {/* 3. MTH165 Midterm Mock Tests List */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Zap className="w-5 h-5 text-amber-500" />
            <h2 className="text-lg font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
              MTH165 Midterm Mock Examination Papers
            </h2>
          </div>
          <span className="text-xs font-mono text-amber-600 dark:text-amber-400 font-semibold">
            30 MCQs • 90 MINS • +1 / -0.25 NEGATIVE
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {MTH165_MOCK_TESTS.map((test, idx) => {
            const savedResult = getSavedResults(test.id);

            return (
              <div
                key={test.id}
                className="group relative bg-paper-50/90 dark:bg-darkbg-900/90 backdrop-blur-xs border border-paper-300 dark:border-darkbg-border rounded-3xl p-5 sm:p-6 shadow-ticket dark:shadow-ticket-dark hover:border-amber-500/60 dark:hover:border-amber-400/60 transition-all duration-300 flex flex-col justify-between"
              >
                <div className="space-y-3">
                  {/* Top Badge Row */}
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono uppercase tracking-wider font-bold px-2.5 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
                      MOCK TEST 0{idx + 1}
                    </span>
                    <span className="text-[11px] font-mono text-ink-500 dark:text-ink-400">
                      Code: {test.code}
                    </span>
                  </div>

                  {/* Title & Description */}
                  <h3 className="text-base sm:text-lg font-bold text-ink-900 dark:text-paper-50 leading-snug group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors">
                    {test.title}
                  </h3>
                  <p className="text-xs text-ink-600 dark:text-ink-400 leading-relaxed line-clamp-2">
                    {test.description}
                  </p>

                  {/* Test Specs Grid */}
                  <div className="grid grid-cols-3 gap-2 py-3 border-y border-paper-200 dark:border-darkbg-border text-center">
                    <div className="space-y-0.5">
                      <div className="flex items-center justify-center gap-1 text-ink-500 dark:text-ink-400">
                        <HelpCircle className="w-3 h-3" />
                        <span className="text-[10px] font-mono">MCQs</span>
                      </div>
                      <p className="text-xs font-bold text-ink-900 dark:text-paper-100">
                        {test.totalQuestions} Questions
                      </p>
                    </div>

                    <div className="space-y-0.5 border-x border-paper-200 dark:border-darkbg-border">
                      <div className="flex items-center justify-center gap-1 text-ink-500 dark:text-ink-400">
                        <Timer className="w-3 h-3" />
                        <span className="text-[10px] font-mono">TIME</span>
                      </div>
                      <p className="text-xs font-bold text-ink-900 dark:text-paper-100">
                        {test.durationMinutes} Mins
                      </p>
                    </div>

                    <div className="space-y-0.5">
                      <div className="flex items-center justify-center gap-1 text-ink-500 dark:text-ink-400">
                        <Award className="w-3 h-3" />
                        <span className="text-[10px] font-mono">MAX</span>
                      </div>
                      <p className="text-xs font-bold text-ink-900 dark:text-paper-100">
                        {test.maxMarks} Marks
                      </p>
                    </div>
                  </div>

                  {/* Saved Result pill if attempted */}
                  {savedResult ? (
                    <div className="flex items-center justify-between p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-700 dark:text-emerald-400 text-xs">
                      <div className="flex items-center gap-1.5">
                        <CheckCircle2 className="w-4 h-4 shrink-0" />
                        <span className="font-semibold">Last Score:</span>
                      </div>
                      <span className="font-mono font-bold">
                        {savedResult.totalScore.toFixed(2)} / {test.maxMarks} ({savedResult.accuracy}%)
                      </span>
                    </div>
                  ) : (
                    <div className="flex items-center justify-between p-2 rounded-xl bg-paper-200/40 dark:bg-darkbg-800/40 text-ink-500 dark:text-ink-400 text-xs font-mono">
                      <span>Marking: +1.0 / -0.25</span>
                      <span>Unattempted</span>
                    </div>
                  )}
                </div>

                {/* Launch Button */}
                <button
                  onClick={() => onStartExam(test)}
                  className="mt-5 w-full py-3 px-4 rounded-2xl bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 font-bold text-xs sm:text-sm tracking-wide transition-all duration-200 flex items-center justify-center gap-2 shadow-sm group-hover:shadow-md active:scale-98 cursor-pointer"
                >
                  <span>{savedResult ? 'Retake Mock Exam' : 'Start Mock Exam'}</span>
                  <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
                </button>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
