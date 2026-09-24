import React, { useState, useEffect } from 'react';
import {
  Timer,
  ChevronRight,
  Sparkles,
  X,
  FileText,
  AlertCircle
} from 'lucide-react';

export default function ExamPrepCountdown({ test, onCountdownComplete, onCancel }) {
  const [count, setCount] = useState(3);
  const [progress, setProgress] = useState(100);

  useEffect(() => {
    const startTime = Date.now();
    const duration = 3000; // 3 seconds

    const interval = setInterval(() => {
      const elapsed = Date.now() - startTime;
      const remainingTime = Math.max(0, duration - elapsed);
      const currentSeconds = Math.ceil(remainingTime / 1000);
      setCount(currentSeconds);
      setProgress((remainingTime / duration) * 100);

      if (elapsed >= duration) {
        clearInterval(interval);
        onCountdownComplete();
      }
    }, 50);

    return () => clearInterval(interval);
  }, [onCountdownComplete]);

  return (
    <div className="fixed inset-0 z-50 bg-ink-900/70 dark:bg-black/85 backdrop-blur-xs flex items-center justify-center p-4 select-none font-sans">
      <div className="relative z-10 max-w-lg w-full bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[32px] p-6 sm:p-10 shadow-ticket dark:shadow-ticket-dark text-center space-y-6 text-ink-900 dark:text-paper-50 animate-fadeIn">
        {/* Top Header Badge */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 text-xs font-mono font-bold tracking-wider uppercase">
          <span className="w-2 h-2 rounded-full bg-ochre-400 animate-ping"></span>
          <span>STARTING EXAMINATION IN 3 SECONDS</span>
        </div>

        {/* 3-2-1 Animated Progress Ring in EduNetwork Ink / Ochre */}
        <div className="relative w-28 h-28 mx-auto flex items-center justify-center">
          <svg className="w-full h-full -rotate-90" viewBox="0 0 100 100">
            <circle
              cx="50"
              cy="50"
              r="44"
              className="stroke-paper-300 dark:stroke-darkbg-border"
              strokeWidth="6"
              fill="transparent"
            />
            <circle
              cx="50"
              cy="50"
              r="44"
              className="stroke-ink-900 dark:stroke-ochre-400 transition-all duration-75"
              strokeWidth="6"
              strokeLinecap="round"
              fill="transparent"
              strokeDasharray="276.46"
              strokeDashoffset={276.46 - (276.46 * progress) / 100}
            />
          </svg>

          {/* Number Display */}
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-4xl sm:text-5xl font-black font-cinzel text-ink-900 dark:text-paper-50 scale-110 transition-transform">
              {count > 0 ? count : 'GO!'}
            </span>
            <span className="text-[9px] font-mono text-ink-600 dark:text-ink-400 font-bold uppercase tracking-widest">
              SECONDS
            </span>
          </div>
        </div>

        {/* Exam Metadata */}
        <div className="space-y-2 pt-1">
          <div className="text-xs font-mono font-bold text-ink-600 dark:text-ink-400 uppercase tracking-widest">
            {test.courseCode} • {test.courseName}
          </div>
          <h2 className="text-xl sm:text-2xl font-black font-cinzel text-ink-900 dark:text-paper-50 leading-snug">
            {test.title}
          </h2>
          <p className="text-xs text-ink-600 dark:text-ink-400 font-sans leading-relaxed">
            {test.description}
          </p>
        </div>

        {/* Exam Parameters Badges */}
        <div className="grid grid-cols-3 gap-2 py-3 px-4 bg-paper-100 dark:bg-darkbg-800 rounded-2xl border border-paper-300 dark:border-darkbg-border font-mono text-center">
          <div className="space-y-0.5">
            <div className="text-[10px] text-ink-600 dark:text-ink-400 uppercase font-bold">Questions</div>
            <div className="text-sm font-black text-ink-900 dark:text-paper-50">
              {test.isDraftingExam ? 'Part A & B (8 Qs)' : `${test.totalQuestions} MCQs`}
            </div>
          </div>
          <div className="space-y-0.5 border-x border-paper-300 dark:border-darkbg-border">
            <div className="text-[10px] text-ink-600 dark:text-ink-400 uppercase font-bold">Duration</div>
            <div className="text-sm font-black text-ink-900 dark:text-paper-50">{test.durationMinutes} Mins</div>
          </div>
          <div className="space-y-0.5">
            <div className="text-[10px] text-ink-600 dark:text-ink-400 uppercase font-bold">Marking</div>
            <div className="text-sm font-black text-ink-900 dark:text-paper-50">
              {test.isDraftingExam ? `${test.maxMarks} Marks Max` : '+1.0 / -0.25'}
            </div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="flex items-center justify-between pt-1">
          <button
            onClick={onCancel}
            className="text-xs font-mono font-bold text-ink-600 hover:text-ink-900 dark:text-ink-400 dark:hover:text-paper-50 transition cursor-pointer"
          >
            Cancel
          </button>
          <button
            onClick={onCountdownComplete}
            className="px-6 py-2.5 rounded-full bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 font-semibold text-xs tracking-wider uppercase transition shadow-md flex items-center gap-1.5 cursor-pointer"
          >
            <span>Start Now</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
}
