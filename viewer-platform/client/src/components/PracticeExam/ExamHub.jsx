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
  Check
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
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10 space-y-10 animate-fadeIn font-sans bg-white text-[#0A1128]">
      {/* 1. DARK NAVY BLUE HERO BANNER WITH CRISP WHITE TEXT */}
      <div className="relative rounded-[32px] p-6 sm:p-12 overflow-hidden bg-[#0A1128] text-white border-2 border-[#0A1128] shadow-2xl">
        <div className="relative z-10 max-w-3xl space-y-5">
          {/* Top Pill Badge */}
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 text-white text-xs font-mono font-bold tracking-widest uppercase">
            <span className="w-2 h-2 rounded-full bg-white animate-ping"></span>
            <span>NEW FEATURE • PRACTICE EXAMS SUITE</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-cinzel font-black tracking-tight leading-[1.12]">
            Midterm Examination <br />
            <span className="font-serif italic font-normal text-slate-300">
              Timed Mock Mastery
            </span>
          </h1>

          <p className="text-sm sm:text-base text-slate-200 leading-relaxed max-w-2xl font-sans">
            Simulate real university midterm conditions with authentic previous year papers, precise <span className="text-white font-bold underline underline-offset-4">+1.0 / -0.25 negative marking</span>, interactive 30-question progress grid, and <span className="text-white font-bold underline underline-offset-4">step-by-step animated solutions</span>.
          </p>

          {/* Navy Badges */}
          <div className="flex flex-wrap items-center gap-2 pt-2 font-mono text-[11px]">
            <span className="px-3 py-1 rounded-full bg-white/10 text-white border border-white/20">
              #LinearAlgebra
            </span>
            <span className="px-3 py-1 rounded-full bg-white/10 text-white border border-white/20">
              #Eigenvalues
            </span>
            <span className="px-3 py-1 rounded-full bg-white/10 text-white border border-white/20">
              #RolleTheorem
            </span>
            <span className="px-3 py-1 rounded-full bg-white/10 text-white border border-white/20">
              #TaylorSeries
            </span>
            <span className="px-3 py-1 rounded-full bg-white/10 text-white border border-white/20">
              #DefiniteIntegrals
            </span>
          </div>
        </div>
      </div>

      {/* 2. COURSE PICKER IN WHITE & DARK NAVY BLUE */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Layers className="w-5 h-5 text-[#0A1128]" />
            <h2 className="text-lg font-black text-[#0A1128] tracking-tight font-sans">
              Select Examination Course
            </h2>
          </div>
          <span className="text-xs font-mono font-bold text-[#0A1128]/70">
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
                    ? 'bg-[#0A1128] text-white border-[#0A1128] shadow-xl scale-[1.02]'
                    : c.active
                    ? 'bg-white border-[#0A1128]/25 text-[#0A1128] hover:border-[#0A1128]'
                    : 'bg-[#0A1128]/5 border-dashed border-[#0A1128]/20 text-[#0A1128]/40 opacity-50 cursor-not-allowed'
                }`}
              >
                <div className="flex items-start justify-between mb-3">
                  <span className={`font-mono font-black text-xs px-2.5 py-0.5 rounded-lg border ${
                    isSelected
                      ? 'bg-white/15 text-white border-transparent'
                      : 'bg-[#0A1128]/5 text-[#0A1128] border-[#0A1128]/15'
                  }`}>
                    {c.code}
                  </span>
                  {isSelected && (
                    <Check className="w-4 h-4 shrink-0" />
                  )}
                </div>

                <p className="font-bold text-xs sm:text-sm leading-snug">
                  {c.name}
                </p>

                <p className={`text-[11px] font-mono mt-2 font-medium ${isSelected ? 'text-slate-300' : 'text-[#0A1128]/60'}`}>
                  {c.tag}
                </p>
              </button>
            );
          })}
        </div>
      </div>

      {/* 3. MTH165 MIDTERM MOCK PAPERS (WHITE CARD & DARK NAVY BLUE) */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Zap className="w-5 h-5 text-[#0A1128]" />
            <h2 className="text-lg font-black text-[#0A1128] tracking-tight font-sans">
              MTH165 Midterm Mock Examination Papers
            </h2>
          </div>
          <span className="text-xs font-mono font-bold text-[#0A1128]">
            30 MCQS • 90 MINS • +1.0 / -0.25
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {MTH165_MOCK_TESTS.map((test, idx) => {
            const savedResult = getSavedResults(test.id);

            return (
              <div
                key={test.id}
                className="group relative bg-white border-2 border-[#0A1128]/20 hover:border-[#0A1128] rounded-[28px] p-6 shadow-sm hover:shadow-2xl transition-all duration-200 flex flex-col justify-between hover:-translate-y-0.5 text-[#0A1128]"
              >
                <div className="space-y-4">
                  {/* Top Badge Row */}
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] font-mono uppercase tracking-widest font-black px-3 py-1 rounded-full bg-[#0A1128] text-white">
                      MOCK TEST 0{idx + 1}
                    </span>
                    <span className="text-[11px] font-mono text-[#0A1128]/70 font-bold">
                      {test.code}
                    </span>
                  </div>

                  {/* Title & Description */}
                  <h3 className="text-base sm:text-lg font-bold text-[#0A1128] leading-snug">
                    {test.title}
                  </h3>
                  <p className="text-xs text-[#0A1128]/70 leading-relaxed line-clamp-2">
                    {test.description}
                  </p>

                  {/* Test Specs Grid in White & Dark Navy */}
                  <div className="grid grid-cols-3 gap-2 py-3 border-y-2 border-[#0A1128]/10 text-center text-[#0A1128]">
                    <div className="space-y-0.5">
                      <div className="flex items-center justify-center gap-1 text-[#0A1128]/60">
                        <HelpCircle className="w-3.5 h-3.5" />
                        <span className="text-[10px] font-mono font-bold">MCQS</span>
                      </div>
                      <p className="text-xs font-black text-[#0A1128]">
                        {test.totalQuestions}
                      </p>
                    </div>

                    <div className="space-y-0.5 border-x-2 border-[#0A1128]/10">
                      <div className="flex items-center justify-center gap-1 text-[#0A1128]/60">
                        <Timer className="w-3.5 h-3.5" />
                        <span className="text-[10px] font-mono font-bold">TIME</span>
                      </div>
                      <p className="text-xs font-black text-[#0A1128]">
                        {test.durationMinutes}m
                      </p>
                    </div>

                    <div className="space-y-0.5">
                      <div className="flex items-center justify-center gap-1 text-[#0A1128]/60">
                        <Award className="w-3.5 h-3.5" />
                        <span className="text-[10px] font-mono font-bold">MARKS</span>
                      </div>
                      <p className="text-xs font-black text-[#0A1128]">
                        {test.maxMarks}
                      </p>
                    </div>
                  </div>

                  {/* Saved Result pill if attempted */}
                  {savedResult ? (
                    <div className="flex items-center justify-between p-3 rounded-xl bg-[#0A1128]/5 border border-[#0A1128]/20 text-[#0A1128] text-xs">
                      <div className="flex items-center gap-1.5 font-bold">
                        <Check className="w-4 h-4 stroke-[3]" />
                        <span>Best Score:</span>
                      </div>
                      <span className="font-mono font-black text-sm text-[#0A1128]">
                        {savedResult.totalScore.toFixed(2)} / {test.maxMarks} ({savedResult.accuracy}%)
                      </span>
                    </div>
                  ) : (
                    <div className="flex items-center justify-between p-2.5 rounded-xl bg-[#0A1128]/5 text-[#0A1128]/70 text-xs font-mono font-bold">
                      <span>Marking: +1.0 / -0.25</span>
                      <span>Ready</span>
                    </div>
                  )}
                </div>

                {/* Launch Button in Dark Navy Blue */}
                <button
                  onClick={() => onStartExam(test)}
                  className="mt-6 w-full py-3.5 px-5 rounded-xl bg-[#0A1128] hover:bg-[#14214d] text-white font-extrabold text-xs sm:text-sm tracking-wider uppercase transition-all duration-150 flex items-center justify-center gap-2 shadow-lg active:scale-98 cursor-pointer group"
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
