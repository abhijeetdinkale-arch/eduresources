import React, { useState, useEffect, useRef } from 'react';
import {
  Timer,
  ChevronRight,
  Maximize2,
  X,
  FileText
} from 'lucide-react';

export default function ExamPrepCountdown({ test, onCountdownComplete, onCancel }) {
  const [count, setCount] = useState(3);
  const [progress, setProgress] = useState(100);
  const completedRef = useRef(false);

  const startExamWithFullscreen = () => {
    if (completedRef.current) return;
    completedRef.current = true;
    try {
      if (!document.fullscreenElement && document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen().catch(() => {});
      }
    } catch {}
    onCountdownComplete();
  };

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
        startExamWithFullscreen();
      }
    }, 50);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="fixed inset-0 z-50 bg-ink-950/70 dark:bg-black/85 backdrop-blur-sm flex items-center justify-center p-4 select-none font-sans">
      <div className="relative z-10 max-w-md w-full bg-white dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[32px] p-6 sm:p-8 shadow-2xl text-center space-y-6 text-ink-900 dark:text-paper-50 animate-fadeIn">
        
        {/* Top Cancel Button */}
        <div className="flex justify-end -mt-2 -mr-2">
          <button
            onClick={onCancel}
            className="p-1.5 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 text-ink-600 dark:text-paper-300 transition cursor-pointer"
            title="Cancel"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* 3-2-1 Animated Progress Ring in Pure Swiss Style */}
        <div className="relative w-32 h-32 mx-auto flex items-center justify-center">
          <svg className="w-full h-full -rotate-90" viewBox="0 0 100 100">
            <circle
              cx="50"
              cy="50"
              r="44"
              className="stroke-paper-200 dark:stroke-darkbg-800"
              strokeWidth="6"
              fill="transparent"
            />
            <circle
              cx="50"
              cy="50"
              r="44"
              className="stroke-ink-950 dark:stroke-paper-50 transition-all duration-75"
              strokeWidth="6"
              strokeLinecap="round"
              fill="transparent"
              strokeDasharray="276.46"
              strokeDashoffset={276.46 - (276.46 * progress) / 100}
            />
          </svg>

          {/* Number Display */}
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-5xl font-black font-display text-ink-950 dark:text-paper-50 scale-110 transition-transform">
              {count > 0 ? count : 'GO!'}
            </span>
            <span className="text-[10px] font-mono text-ink-600 dark:text-ink-400 font-bold uppercase tracking-widest mt-0.5">
              SECONDS
            </span>
          </div>
        </div>

        {/* Exam Title & Code */}
        <div className="space-y-1.5 pt-1">
          <div className="text-xs font-mono font-bold text-ink-600 dark:text-ink-400 uppercase tracking-widest">
            {test.courseCode} • {test.code}
          </div>
          <h2 className="text-xl sm:text-2xl font-black font-display text-ink-950 dark:text-paper-50 leading-snug">
            {test.title}
          </h2>
          <div className="flex items-center justify-center gap-2 text-xs font-mono text-ink-600 dark:text-ink-400 pt-1">
            <span>{test.durationMinutes} Mins</span>
            <span>•</span>
            <span>{test.isDraftingExam ? 'Drafting Studio' : `${test.totalQuestions} Questions`}</span>
            <span>•</span>
            <span>Units 1-3</span>
          </div>
        </div>

        {/* Start Button (Ensures instant Fullscreen activation) */}
        <div className="pt-2">
          <button
            onClick={startExamWithFullscreen}
            className="w-full py-3.5 px-6 rounded-full bg-ink-950 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-950 font-bold text-sm tracking-wide transition-all shadow-lg flex items-center justify-center gap-2 cursor-pointer active:scale-98"
          >
            <Maximize2 className="w-4 h-4" />
            <span>Start Exam in Fullscreen</span>
            <ChevronRight className="w-4 h-4 ml-1" />
          </button>
          <div className="text-[11px] font-mono text-ink-500 dark:text-ink-400 mt-2">
            Auto-starting in {count}s or click to launch now
          </div>
        </div>

      </div>
    </div>
  );
}
