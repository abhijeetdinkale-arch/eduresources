import React, { useState, useEffect } from 'react';
import {
  Timer,
  Award,
  ChevronRight,
  Sparkles,
  X
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
    <div className="fixed inset-0 z-50 bg-[#0A1128]/80 backdrop-blur-md flex items-center justify-center p-4 select-none font-sans animate-fadeIn">
      <div className="relative z-10 max-w-lg w-full bg-white border-2 border-[#0A1128] rounded-[32px] p-6 sm:p-10 shadow-2xl text-center space-y-6 text-[#0A1128]">
        {/* Top Header Badge */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#0A1128]/10 border border-[#0A1128]/20 text-[#0A1128] text-xs font-mono font-bold tracking-wider uppercase">
          <span className="w-2 h-2 rounded-full bg-[#0A1128] animate-ping"></span>
          <span>STARTING EXAMINATION IN 3 SECONDS</span>
        </div>

        {/* 3-2-1 Animated Progress Ring in Dark Navy */}
        <div className="relative w-28 h-28 mx-auto flex items-center justify-center">
          <svg className="w-full h-full -rotate-90" viewBox="0 0 100 100">
            <circle
              cx="50"
              cy="50"
              r="44"
              className="stroke-[#0A1128]/10"
              strokeWidth="6"
              fill="transparent"
            />
            <circle
              cx="50"
              cy="50"
              r="44"
              className="stroke-[#0A1128] transition-all duration-75"
              strokeWidth="6"
              strokeLinecap="round"
              fill="transparent"
              strokeDasharray="276.46"
              strokeDashoffset={276.46 - (276.46 * progress) / 100}
            />
          </svg>

          {/* Number Display */}
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-4xl sm:text-5xl font-black font-cinzel text-[#0A1128] scale-110 transition-transform">
              {count > 0 ? count : 'GO!'}
            </span>
            <span className="text-[9px] font-mono text-[#0A1128]/70 font-bold uppercase tracking-widest">
              SECONDS
            </span>
          </div>
        </div>

        {/* Exam Metadata */}
        <div className="space-y-2 pt-1">
          <div className="text-xs font-mono font-bold text-[#0A1128]/70 uppercase tracking-widest">
            {test.courseCode} • {test.courseName}
          </div>
          <h2 className="text-xl sm:text-2xl font-black font-cinzel text-[#0A1128] leading-snug">
            {test.title}
          </h2>
          <p className="text-xs text-[#0A1128]/80 font-sans leading-relaxed">
            {test.description}
          </p>
        </div>

        {/* Exam Parameters Badges */}
        <div className="grid grid-cols-3 gap-2 py-3 px-4 bg-[#0A1128]/5 rounded-2xl border border-[#0A1128]/15 font-mono text-center">
          <div className="space-y-0.5">
            <div className="text-[10px] text-[#0A1128]/60 uppercase font-bold">Questions</div>
            <div className="text-sm font-black text-[#0A1128]">{test.totalQuestions} MCQs</div>
          </div>
          <div className="space-y-0.5 border-x border-[#0A1128]/15">
            <div className="text-[10px] text-[#0A1128]/60 uppercase font-bold">Duration</div>
            <div className="text-sm font-black text-[#0A1128]">{test.durationMinutes} Mins</div>
          </div>
          <div className="space-y-0.5">
            <div className="text-[10px] text-[#0A1128]/60 uppercase font-bold">Marking</div>
            <div className="text-sm font-black text-[#0A1128]">+1.0 / -0.25</div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="flex items-center justify-between pt-1">
          <button
            onClick={onCancel}
            className="text-xs font-mono font-bold text-[#0A1128]/60 hover:text-[#0A1128] transition cursor-pointer"
          >
            Cancel
          </button>
          <button
            onClick={onCountdownComplete}
            className="px-5 py-2.5 rounded-xl bg-[#0A1128] hover:bg-[#14214d] text-white font-extrabold text-xs font-mono tracking-wider uppercase transition shadow-lg flex items-center gap-1.5 cursor-pointer"
          >
            <span>Start Now</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
}
