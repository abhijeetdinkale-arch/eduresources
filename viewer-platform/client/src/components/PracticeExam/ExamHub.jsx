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
  RotateCcw,
  Compass,
  FileText,
  School,
  AlertCircle
} from 'lucide-react';
import { COURSES_CONFIG, getTestsForCourse } from '../../data/mock_tests_registry';

export default function ExamHub({ onStartExam, onBackToCatalog }) {
  const [selectedCourse, setSelectedCourse] = useState('MTH165');
  const [departmentFilter, setDepartmentFilter] = useState('ALL');

  // Load saved test results from localStorage
  const getSavedResults = (testId) => {
    try {
      const raw = localStorage.getItem(`edunet_exam_result_${testId}`);
      if (raw) return JSON.parse(raw);
    } catch {}
    return null;
  };

  const departments = ['ALL', 'Mathematics', 'Applied Sciences', 'Computer Science', 'Electronics', 'Mechanical', 'Information Tech'];

  const filteredCourses = departmentFilter === 'ALL'
    ? COURSES_CONFIG
    : COURSES_CONFIG.filter((c) => c.department === departmentFilter);

  const activeCourseConfig = COURSES_CONFIG.find((c) => c.code === selectedCourse) || COURSES_CONFIG[0];
  const activeCourseTests = getTestsForCourse(selectedCourse);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10 space-y-10 animate-fadeIn font-sans text-ink-900 dark:text-paper-50">
      {/* 1. HERO BANNER */}
      <div className="relative rounded-[36px] p-6 sm:p-12 overflow-hidden bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs border border-paper-300/80 dark:border-darkbg-border shadow-ticket dark:shadow-ticket-dark">
        <div className="relative z-10 max-w-3xl space-y-5">
          {/* Top Pill Badge */}
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 text-xs font-mono font-bold tracking-widest uppercase">
            <span className="w-2 h-2 rounded-full bg-ochre-400 animate-ping"></span>
            <span>UNIVERSITY MIDTERM EXAMINATION SUITE • UNITS 1, 2 & 3</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-cinzel font-black tracking-tight text-ink-900 dark:text-paper-50 leading-[1.12]">
            Midterm Examination <br />
            <span className="font-serif italic font-normal text-ink-600 dark:text-ink-400">
              Multi-Subject Paper Vault
            </span>
          </h1>

          <p className="text-sm sm:text-base text-ink-600 dark:text-ink-400 leading-relaxed max-w-2xl font-sans">
            Simulate real university midterm conditions across all semester courses. Features authentic previous year papers, precise <span className="text-ink-900 dark:text-paper-50 font-bold underline underline-offset-4">+1.0 / -0.25 negative marking</span>, step-by-step mathematical derivations, and a dedicated <span className="text-ink-900 dark:text-paper-50 font-bold underline underline-offset-4">Engineering Graphics Drafting Studio</span> for MEC136.
          </p>

          {/* Quick Stats Badges */}
          <div className="flex flex-wrap items-center gap-2 pt-2 font-mono text-[11px]">
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #8 Courses Active
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #MTH165 Math
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #PHY110 Physics
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #ECE249 Electrical
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #CSE111 Computing
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #INT335 DesignThinking
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #CSE326 WebDev
            </span>
            <span className="px-3 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border">
              #MEC136 DraftingStudio
            </span>
          </div>
        </div>
      </div>

      {/* 2. DEPARTMENT FILTER & COURSE PICKER */}
      <div className="space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <Layers className="w-5 h-5 text-ink-900 dark:text-paper-50" />
            <h2 className="text-lg font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
              Select Examination Subject
            </h2>
          </div>

          {/* Department Pills */}
          <div className="flex items-center gap-1.5 overflow-x-auto scrollbar-none py-1">
            {departments.map((dept) => (
              <button
                key={dept}
                onClick={() => setDepartmentFilter(dept)}
                className={`px-3 py-1 rounded-full text-xs font-mono font-bold transition-all whitespace-nowrap ${
                  departmentFilter === dept
                    ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                    : 'bg-paper-200 dark:bg-darkbg-800 text-ink-600 dark:text-ink-400 hover:bg-paper-300'
                }`}
              >
                {dept}
              </button>
            ))}
          </div>
        </div>

        {/* Course Cards Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
          {filteredCourses.map((c) => {
            const isSelected = selectedCourse === c.code;

            return (
              <button
                key={c.code}
                onClick={() => setSelectedCourse(c.code)}
                className={`group relative p-4 sm:p-5 rounded-2xl text-left border transition-all duration-300 flex flex-col justify-between h-36 ${
                  isSelected
                    ? 'bg-paper-200 dark:bg-darkbg-800 border-ink-900 dark:border-ochre-400 shadow-ticket dark:shadow-ticket-dark ring-2 ring-ink-900/10 dark:ring-ochre-400/20'
                    : 'bg-paper-100/70 dark:bg-darkbg-900/70 border-paper-300/80 dark:border-darkbg-border hover:border-ink-400 dark:hover:border-paper-400 hover:bg-paper-100 dark:hover:bg-darkbg-800'
                }`}
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span
                      className={`text-xs font-mono font-bold px-2 py-0.5 rounded-md ${
                        isSelected
                          ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                          : 'bg-paper-200 dark:bg-darkbg-800 text-ink-700 dark:text-paper-300'
                      }`}
                    >
                      {c.code}
                    </span>

                    {c.isDrafting && (
                      <span className="text-[10px] font-mono font-bold text-ochre-600 dark:text-ochre-400">
                        Drafting
                      </span>
                    )}
                  </div>

                  <h3 className="text-sm font-bold text-ink-900 dark:text-paper-50 line-clamp-2 leading-tight">
                    {c.name}
                  </h3>
                </div>

                <div className="flex items-center justify-between text-[11px] font-mono font-semibold text-ink-600 dark:text-ink-400 pt-2 border-t border-paper-300/50 dark:border-darkbg-border/50">
                  <span>{c.tag}</span>
                  <span className="text-ochre-500 font-bold">➔</span>
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* 3. SELECTED COURSE SYLLABUS HEADER */}
      <div className="p-5 sm:p-6 rounded-3xl bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border space-y-3">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-1 rounded-md bg-ochre-100 dark:bg-ochre-900/30 text-ochre-800 dark:text-ochre-300 font-mono text-xs font-bold">
                {activeCourseConfig.code}
              </span>
              <span className="text-xs font-mono text-ink-500 uppercase tracking-widest">
                {activeCourseConfig.department}
              </span>
              {activeCourseConfig.isDrafting && (
                <span className="px-2 py-0.5 rounded-md bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 text-[10px] font-bold font-mono">
                  Subjective Blueprint Studio
                </span>
              )}
            </div>
            <h2 className="text-xl sm:text-2xl font-cinzel font-bold text-ink-900 dark:text-paper-50 mt-1">
              {activeCourseConfig.name} • Midterm Papers
            </h2>
          </div>

          <div className="flex items-center gap-2 text-xs font-mono font-bold text-ink-700 dark:text-paper-300">
            <School className="w-4 h-4 text-ochre-500" />
            <span>MIDTERM SCOPE: UNITS 1, 2 & 3</span>
          </div>
        </div>

        <p className="text-xs sm:text-sm text-ink-600 dark:text-ink-400 font-sans leading-relaxed">
          {activeCourseConfig.description}
        </p>
      </div>

      {/* 4. ACTIVE TEST PAPERS LIST */}
      <div className="space-y-5">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-ink-900 dark:text-paper-50" />
            <h3 className="text-lg font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
              Available Mock Test Papers ({activeCourseTests.length})
            </h3>
          </div>
          <span className="text-xs font-mono text-ink-600 dark:text-ink-400">
            Click any test to enter 3-second animated prep
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {activeCourseTests.map((test, index) => {
            const savedResult = getSavedResults(test.id);

            return (
              <div
                key={test.id}
                className="group relative bg-paper-100/90 dark:bg-darkbg-900/90 rounded-[28px] p-6 sm:p-7 border border-paper-300/80 dark:border-darkbg-border shadow-ticket dark:shadow-ticket-dark flex flex-col justify-between hover:border-ink-900 dark:hover:border-paper-300 transition-all duration-300 space-y-6"
              >
                <div className="space-y-4">
                  {/* Top Meta Row */}
                  <div className="flex items-center justify-between text-xs font-mono">
                    <span className="px-2.5 py-1 rounded-md bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 font-bold border border-paper-300 dark:border-darkbg-border">
                      {test.code}
                    </span>

                    <span className="text-ink-600 dark:text-ink-400 font-semibold flex items-center gap-1.5">
                      <Timer className="w-3.5 h-3.5 text-ochre-500" />
                      <span>{test.durationMinutes} Minutes</span>
                    </span>
                  </div>

                  {/* Title & Description */}
                  <div>
                    <h4 className="text-lg font-bold text-ink-900 dark:text-paper-50 group-hover:text-ochre-600 dark:group-hover:text-ochre-400 transition-colors leading-snug">
                      {test.title}
                    </h4>
                    <p className="text-xs text-ink-600 dark:text-ink-400 mt-2 line-clamp-2 leading-relaxed font-sans">
                      {test.description}
                    </p>
                  </div>

                  {/* Topics Tags */}
                  <div className="flex flex-wrap gap-1.5 pt-1">
                    {test.topics.slice(0, 4).map((topic, i) => (
                      <span
                        key={i}
                        className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-paper-200 dark:bg-darkbg-800 text-ink-700 dark:text-paper-300 border border-paper-300/60 dark:border-darkbg-border/60"
                      >
                        {topic}
                      </span>
                    ))}
                    {test.topics.length > 4 && (
                      <span className="px-2 py-0.5 rounded-full text-[10px] font-mono text-ink-500">
                        +{test.topics.length - 4} more
                      </span>
                    )}
                  </div>
                </div>

                {/* Bottom Action Footer */}
                <div className="pt-4 border-t border-paper-200 dark:border-darkbg-border/60 flex items-center justify-between">
                  {/* Left: Previous Score or Specs */}
                  <div>
                    {savedResult ? (
                      <div className="space-y-0.5">
                        <span className="text-[10px] font-mono font-bold text-ink-500 uppercase tracking-widest">
                          LAST SCORE
                        </span>
                        <div className="flex items-center gap-2">
                          <span className="text-sm font-black font-mono text-emerald-600 dark:text-emerald-400">
                            {savedResult.netScore?.toFixed(2)} / {test.maxMarks}
                          </span>
                          <span className="text-xs text-ink-500 font-mono">
                            ({savedResult.percentage?.toFixed(1)}%)
                          </span>
                        </div>
                      </div>
                    ) : (
                      <div className="text-xs font-mono text-ink-600 dark:text-ink-400 space-y-0.5">
                        <div className="font-bold text-ink-800 dark:text-paper-200">
                          {test.isDraftingExam ? '40 Marks Max' : `${test.totalQuestions} Questions • 30 M`}
                        </div>
                        <div className="text-[10px] text-ink-500">
                          {test.isDraftingExam ? 'Part A (10M) + Part B (30M)' : '+1.0 / -0.25 Marking'}
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Right: Solid High-Contrast Launch Button */}
                  <button
                    onClick={() => onStartExam(test)}
                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-ink-900 hover:bg-ink-800 dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 font-bold text-xs tracking-wider transition-all shadow-md group-hover:scale-105 active:scale-95 cursor-pointer"
                  >
                    {test.isDraftingExam ? (
                      <>
                        <Compass className="w-4 h-4 text-ochre-400 dark:text-ochre-600" />
                        <span>Open Drafting Studio</span>
                      </>
                    ) : savedResult ? (
                      <>
                        <RotateCcw className="w-3.5 h-3.5" />
                        <span>Retake Paper</span>
                      </>
                    ) : (
                      <>
                        <span>Start Exam</span>
                        <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
                      </>
                    )}
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
