import React, { useState, useRef } from 'react';
import {
  Timer,
  BookOpen,
  ArrowRight,
  RotateCcw,
  Compass,
  Layers,
  Sparkles
} from 'lucide-react';
import { COURSES_CONFIG, getTestsForCourse } from '../../data/mock_tests_registry';

export default function ExamHub({ onStartExam, onBackToCatalog }) {
  const [selectedCourse, setSelectedCourse] = useState('MTH165');
  const [departmentFilter, setDepartmentFilter] = useState('ALL');
  const testsSectionRef = useRef(null);

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

  const handleSelectCourse = (code) => {
    setSelectedCourse(code);
    setTimeout(() => {
      testsSectionRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 50);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 space-y-8 animate-fadeIn font-sans text-ink-900 dark:text-paper-50">
      
      {/* 1. CLEAN MINIMALIST HERO (Swiss Precision) */}
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 pb-6 border-b border-paper-300 dark:border-darkbg-border">
        <div>
          <h1 className="text-3xl sm:text-5xl font-black font-display tracking-tight text-ink-950 dark:text-paper-50">
            Midterm Examination Papers
          </h1>
          <p className="text-xs sm:text-sm text-ink-600 dark:text-ink-400 mt-1.5 font-sans">
            5 full-length verified practice papers per subject with negative marking and instant animated solutions.
          </p>
        </div>

        {/* Back to Catalog if handler provided */}
        {onBackToCatalog && (
          <button
            onClick={onBackToCatalog}
            className="self-start sm:self-auto text-xs font-mono font-bold text-ink-600 dark:text-ink-400 hover:text-ink-950 dark:hover:text-paper-50 transition cursor-pointer"
          >
            ← Back to Books
          </button>
        )}
      </div>

      {/* 2. SUBJECT PICKER */}
      <div className="space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <Layers className="w-4 h-4 text-ink-900 dark:text-paper-50" />
            <h2 className="text-sm font-bold uppercase tracking-wider font-mono text-ink-800 dark:text-paper-200">
              Select Subject ({filteredCourses.length})
            </h2>
          </div>

          {/* Department Filter Pills */}
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
            {departments.map((dept) => (
              <button
                key={dept}
                onClick={() => setDepartmentFilter(dept)}
                className={`px-3 py-1 rounded-full text-xs font-mono font-bold transition-all whitespace-nowrap cursor-pointer ${
                  departmentFilter === dept
                    ? 'bg-ink-950 dark:bg-paper-50 text-paper-50 dark:text-ink-950 shadow-xs'
                    : 'bg-paper-200/80 dark:bg-darkbg-800 text-ink-700 dark:text-ink-300 hover:bg-paper-300'
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
                onClick={() => handleSelectCourse(c.code)}
                className={`group relative p-4 sm:p-5 rounded-2xl text-left border transition-all duration-200 flex flex-col justify-between h-36 cursor-pointer ${
                  isSelected
                    ? 'bg-paper-200/90 dark:bg-darkbg-800 border-ink-950 dark:border-paper-50 shadow-md ring-2 ring-ink-950/10 dark:ring-paper-50/20 scale-[1.02]'
                    : 'bg-white/80 dark:bg-darkbg-900/80 border-paper-300 dark:border-darkbg-border hover:border-ink-400 dark:hover:border-paper-400 hover:bg-white dark:hover:bg-darkbg-850'
                }`}
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span
                      className={`text-xs font-mono font-bold px-2 py-0.5 rounded-md ${
                        isSelected
                          ? 'bg-ink-950 dark:bg-paper-50 text-paper-50 dark:text-ink-950'
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

                  <h3 className="text-sm font-bold font-display text-ink-950 dark:text-paper-50 line-clamp-2 leading-tight">
                    {c.name}
                  </h3>
                </div>

                <div className="flex items-center justify-between text-[11px] font-mono font-semibold text-ink-500 dark:text-ink-400 pt-2 border-t border-paper-300/40 dark:border-darkbg-border/40">
                  <span>5 Tests Active</span>
                  <span className={`transition-transform duration-200 ${isSelected ? 'translate-x-1 font-bold text-ink-950 dark:text-paper-50' : 'group-hover:translate-x-1'}`}>
                    →
                  </span>
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* 3. ACTIVE TEST PAPERS SECTION */}
      <div ref={testsSectionRef} className="space-y-4 pt-2">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-paper-300 dark:border-darkbg-border pb-3">
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded bg-ink-950 text-white dark:bg-paper-50 dark:text-ink-950 font-mono text-xs font-bold">
              {activeCourseConfig.code}
            </span>
            <h2 className="text-lg sm:text-xl font-bold font-display text-ink-950 dark:text-paper-50">
              {activeCourseConfig.name} • 5 Midterm Papers
            </h2>
          </div>
          <span className="text-xs font-mono text-ink-600 dark:text-ink-400">
            Scope: Units 1, 2 & 3 • 90 Mins • +1.0 / -0.25 Marking
          </span>
        </div>

        {/* Test Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-5">
          {activeCourseTests.map((test, index) => {
            const savedResult = getSavedResults(test.id);

            return (
              <div
                key={test.id}
                className="group relative bg-white/80 dark:bg-darkbg-900/80 backdrop-blur-md rounded-2xl p-5 sm:p-6 border border-paper-300 dark:border-darkbg-border shadow-sm flex flex-col justify-between hover:border-ink-950 dark:hover:border-paper-100 transition-all duration-200 space-y-5"
              >
                <div className="space-y-3">
                  {/* Top Meta */}
                  <div className="flex items-center justify-between text-xs font-mono">
                    <div className="flex items-center gap-2">
                      <span className="px-2.5 py-1 rounded-md bg-ink-950 text-paper-50 dark:bg-paper-50 dark:text-ink-950 font-bold text-[11px]">
                        Paper {index + 1} of 5
                      </span>
                      <span className="px-2 py-0.5 rounded bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 font-bold border border-paper-300 dark:border-darkbg-border">
                        {test.code}
                      </span>
                    </div>

                    <span className="text-ink-600 dark:text-ink-400 font-semibold flex items-center gap-1.5 bg-paper-200/60 dark:bg-darkbg-800/60 px-2.5 py-1 rounded-full border border-paper-300/40 dark:border-darkbg-border/40">
                      <Timer className="w-3.5 h-3.5 text-ochre-500" />
                      <span>{test.durationMinutes} Mins</span>
                    </span>
                  </div>

                  {/* Title & Description */}
                  <div>
                    <h3 className="text-base sm:text-lg font-bold font-display text-ink-950 dark:text-paper-50 leading-snug">
                      {test.title}
                    </h3>
                    <p className="text-xs text-ink-600 dark:text-ink-400 mt-1 line-clamp-2 leading-relaxed font-sans">
                      {test.description}
                    </p>
                  </div>

                  {/* Syllabus Pill */}
                  <div className="flex items-center gap-2 pt-1">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border border-emerald-500/20 font-bold">
                      Units 1-3 Verified
                    </span>
                    <span className="text-[11px] font-mono text-ink-500">
                      {test.isDraftingExam ? 'CAD Challenge' : `${test.totalQuestions} Questions`}
                    </span>
                  </div>
                </div>

                {/* Bottom Action Footer */}
                <div className="pt-3 border-t border-paper-200 dark:border-darkbg-border flex items-center justify-between">
                  <div>
                    {savedResult ? (
                      <div className="space-y-0.5">
                        <span className="text-[9px] font-mono font-bold text-ink-500 uppercase tracking-widest">
                          LAST SCORE
                        </span>
                        <div className="flex items-center gap-1.5">
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
                          {test.isDraftingExam ? 'Drafting Blueprint' : '+1.0 / -0.25 Marking'}
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Start Exam Button */}
                  <button
                    onClick={() => onStartExam(test)}
                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-ink-950 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-950 font-bold text-xs tracking-wider transition-all shadow-md active:scale-95 cursor-pointer"
                  >
                    {test.isDraftingExam ? (
                      <>
                        <Compass className="w-4 h-4 text-ochre-400 dark:text-ochre-600" />
                        <span>Open Studio</span>
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
