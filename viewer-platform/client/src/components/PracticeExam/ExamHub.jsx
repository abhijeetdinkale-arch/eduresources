import React, { useState } from 'react';
import {
  Sparkles,
  Timer,
  Award,
  BookOpen,
  ArrowRight,
  CheckCircle2,
  HelpCircle,
  Zap,
  Layers,
  Check,
  RotateCcw
} from 'lucide-react';
import { MTH165_MOCK_TESTS } from '../../data/mth165_mock_tests';

export default function ExamHub({ onStartExam, onBackToCatalog }) {
  const [selectedCourse, setSelectedCourse] = useState('MTH165');

  // Load saved test results from localStorage
  const getSavedResults = (testId) => {
    try {
      const raw = localStorage.getItem(`edunet_exam_result_${testId}`);
      if (raw) return JSON.parse(raw);
    } catch {}
    return null;
  };

  const coursesList = [
    { code: 'MTH165', name: 'Mathematics for Engineers', testsCount: 5, active: true, tag: '5 Papers Ready' },
    { code: 'PHY175', name: 'Engineering Physics & Optics', testsCount: 'Coming Soon', active: false, tag: 'Next Release' },
    { code: 'CSE111', name: 'Computing & Problem Solving', testsCount: 'Coming Soon', active: false, tag: 'Next Release' },
    { code: 'CSE326', name: 'Web Dev & Modern Frameworks', testsCount: 'Coming Soon', active: false, tag: 'Next Release' },
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10 space-y-10 animate-fadeIn font-sans text-ink-900 dark:text-paper-50">
      {/* 1. HERO BANNER */}
      <div className="relative rounded-[36px] p-6 sm:p-12 overflow-hidden bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs border border-paper-300/80 dark:border-darkbg-border shadow-ticket dark:shadow-ticket-dark">
        <div className="relative z-10 max-w-3xl space-y-5">
          {/* Top Pill Badge */}
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 text-xs font-mono font-bold tracking-widest uppercase">
            <span className="w-2 h-2 rounded-full bg-ochre-400 animate-ping"></span>
            <span>NEW FEATURE • PRACTICE EXAMS SUITE</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-cinzel font-black tracking-tight text-ink-900 dark:text-paper-50 leading-[1.12]">
            Midterm Examination <br />
            <span className="font-serif italic font-normal text-ink-600 dark:text-ink-400">
              Timed Mock Mastery
            </span>
          </h1>

          <p className="text-sm sm:text-base text-ink-600 dark:text-ink-400 leading-relaxed max-w-2xl font-sans">
            Simulate real university midterm conditions with authentic previous year papers, precise <span className="text-ink-900 dark:text-paper-50 font-bold underline underline-offset-4">+1.0 / -0.25 negative marking</span>, interactive 30-question progress grid, and <span className="text-ink-900 dark:text-paper-50 font-bold underline underline-offset-4">step-by-step animated solutions</span>.
          </p>

          {/* Topic Badges */}
          <div className="flex flex-wrap items-center gap-2 pt-2 font-mono text-[11px]">
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #LinearAlgebra
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #Eigenvalues
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #RolleTheorem
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #TaylorSeries
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #DefiniteIntegrals
            </span>
          </div>
        </div>
      </div>

      {/* 2. COURSE PICKER */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Layers className="w-5 h-5 text-ink-900 dark:text-paper-50" />
            <h2 className="text-lg font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
              Select Examination Course
            </h2>
          </div>
          <span className="text-xs font-mono font-bold text-ink-600 dark:text-ink-400">
            5 MOCK PAPERS ACTIVE
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
          {coursesList.map((c) => {
            const isSelected = selectedCourse === c.code && c.active;

            return (
              <button
                key={c.code}
                onClick={() => c.active && setSelectedCourse(c.code)}
                disabled={!c.active}
                className={`text-left p-4 sm:p-5 rounded-2xl border-2 transition-all duration-200 relative overflow-hidden cursor-pointer ${
                  isSelected
                    ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 border-ink-900 dark:border-paper-50 shadow-ticket scale-[1.02]'
                    : c.active
                    ? 'bg-paper-50 hover:bg-paper-100 dark:bg-darkbg-850 dark:hover:bg-darkbg-800 border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50'
                    : 'bg-paper-100/40 dark:bg-darkbg-900/40 border-dashed border-paper-300/50 dark:border-darkbg-border/50 text-ink-400 dark:text-ink-600 opacity-60 cursor-not-allowed'
                }`}
              >
                <div className="flex items-start justify-between mb-3">
                  <span className={`font-mono font-bold text-xs px-2.5 py-0.5 rounded-lg border ${
                    isSelected
                      ? 'bg-paper-50/20 text-paper-50 dark:bg-ink-900/20 dark:text-ink-900 border-transparent'
                      : 'bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border-paper-300 dark:border-darkbg-border'
                  }`}>
                    {c.code}
                  </span>
                  {isSelected && (
                    <Check className="w-4 h-4 shrink-0 text-ochre-400 dark:text-ochre-500" />
                  )}
                </div>

                <div className="text-xs sm:text-sm font-bold truncate">
                  {c.name}
                </div>

                <div className={`text-[11px] font-mono mt-2 ${
                  isSelected ? 'text-paper-200 dark:text-ink-600' : 'text-ink-600 dark:text-ink-400'
                }`}>
                  {typeof c.testsCount === 'number' ? `${c.testsCount} Mock Exams` : c.testsCount}
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* 3. 5 MTH165 MOCK TESTS CARDS */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-ink-900 dark:text-paper-50" />
            <h2 className="text-lg font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
              MTH165 Midterm Mock Examinations (5 Papers)
            </h2>
          </div>
          <span className="text-xs font-mono font-semibold text-ink-600 dark:text-ink-400">
            30 MCQs • 90 Mins • +1.00 / -0.25 Mark
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {MTH165_MOCK_TESTS.map((test, idx) => {
            const savedResult = getSavedResults(test.id);

            return (
              <div
                key={test.id}
                className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[28px] p-6 sm:p-7 shadow-ticket dark:shadow-ticket-dark space-y-4 hover:shadow-floating transition-all flex flex-col justify-between"
              >
                <div className="space-y-3">
                  {/* Top Row: Paper Code & Badge */}
                  <div className="flex items-center justify-between">
                    <span className="font-mono text-xs font-bold px-2.5 py-0.5 rounded-lg bg-paper-200 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 border border-paper-300 dark:border-darkbg-border">
                      {test.code}
                    </span>

                    {idx < 2 ? (
                      <span className="px-2.5 py-0.5 rounded-full bg-ochre-400 text-ink-950 font-mono text-[10px] font-bold">
                        OFFICIAL PYQ
                      </span>
                    ) : (
                      <span className="px-2.5 py-0.5 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border font-mono text-[10px] font-semibold">
                        MOCK TEST {idx + 1}
                      </span>
                    )}
                  </div>

                  {/* Title & Description */}
                  <div>
                    <h3 className="font-cinzel font-bold text-base sm:text-lg text-ink-900 dark:text-paper-50 line-clamp-2">
                      {test.title}
                    </h3>
                    <p className="text-xs text-ink-600 dark:text-ink-400 mt-1 line-clamp-2 leading-relaxed">
                      {test.description}
                    </p>
                  </div>

                  {/* Meta Pills */}
                  <div className="grid grid-cols-3 gap-2 py-2 px-3 rounded-xl bg-paper-100 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border font-mono text-center">
                    <div>
                      <div className="text-[10px] text-ink-600 dark:text-ink-400">QUESTIONS</div>
                      <div className="text-xs font-bold text-ink-900 dark:text-paper-50">{test.totalQuestions}</div>
                    </div>
                    <div className="border-x border-paper-300 dark:border-darkbg-border">
                      <div className="text-[10px] text-ink-600 dark:text-ink-400">TIME</div>
                      <div className="text-xs font-bold text-ink-900 dark:text-paper-50">{test.durationMinutes}m</div>
                    </div>
                    <div>
                      <div className="text-[10px] text-ink-600 dark:text-ink-400">MAX SCORE</div>
                      <div className="text-xs font-bold text-ink-900 dark:text-paper-50">{test.maxMarks}</div>
                    </div>
                  </div>

                  {/* Saved Result Indicator (if attempted) */}
                  {savedResult && (
                    <div className="flex items-center justify-between p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-xs font-mono">
                      <span className="text-emerald-700 dark:text-emerald-400 font-bold">
                        Best: {savedResult.totalScore.toFixed(2)}/30 ({savedResult.accuracy}%)
                      </span>
                      <span className="text-[10px] text-emerald-600 dark:text-emerald-400">
                        {savedResult.correctCount} Correct
                      </span>
                    </div>
                  )}
                </div>

                {/* Start Button */}
                <button
                  onClick={() => onStartExam(test)}
                  className="w-full py-3.5 px-4 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs font-semibold tracking-wider uppercase transition shadow-md flex items-center justify-center gap-2 cursor-pointer mt-2"
                >
                  <Sparkles className="w-4 h-4 text-ochre-400 dark:text-ochre-500" />
                  <span>{savedResult ? 'Retake Examination' : 'Start Midterm Exam'}</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
