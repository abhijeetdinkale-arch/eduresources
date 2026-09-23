import React, { useState, useEffect, useCallback, useRef } from 'react';
import {
  Timer,
  Bookmark,
  BookmarkCheck,
  ChevronLeft,
  ChevronRight,
  Send,
  X,
  RotateCcw,
  Grid,
  AlertTriangle,
  CheckCircle2,
  HelpCircle
} from 'lucide-react';
import MathText from '../MathText';

export default function ExamScreen({ test, onFinishExam, onExitExam }) {
  const [currentIdx, setCurrentIdx] = useState(0);
  // userAnswers: { [questionId]: selectedOptionIndex (0..3) }
  const [userAnswers, setUserAnswers] = useState({});
  // flagged: Set of questionIds marked for review
  const [flagged, setFlagged] = useState(new Set());
  // Timer in seconds (90 mins * 60 = 5400)
  const [secondsRemaining, setSecondsRemaining] = useState(test.durationMinutes * 60);
  const [isSubmitModalOpen, setIsSubmitModalOpen] = useState(false);
  const [isGridModalOpen, setIsGridModalOpen] = useState(false);
  const timerRef = useRef(null);

  const currentQ = test.questions[currentIdx];
  const totalQuestions = test.questions.length;

  // Format seconds to HH:MM:SS / MM:SS
  const formatTime = (secs) => {
    const mins = Math.floor(secs / 60);
    const s = secs % 60;
    const hours = Math.floor(mins / 60);
    const m = mins % 60;

    if (hours > 0) {
      return `${hours}:${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
    }
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  };

  // Submit Handler
  const handleSubmit = useCallback(() => {
    if (timerRef.current) clearInterval(timerRef.current);
    const timeSpentSeconds = test.durationMinutes * 60 - secondsRemaining;
    onFinishExam({
      test,
      userAnswers,
      timeSpentSeconds,
    });
  }, [test, userAnswers, secondsRemaining, onFinishExam]);

  // Countdown Timer
  useEffect(() => {
    timerRef.current = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(timerRef.current);
          handleSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [handleSubmit]);

  // Option select handler
  const handleSelectOption = (optIndex) => {
    setUserAnswers((prev) => ({
      ...prev,
      [currentQ.id]: optIndex,
    }));
  };

  // Clear current response
  const handleClearResponse = () => {
    setUserAnswers((prev) => {
      const copy = { ...prev };
      delete copy[currentQ.id];
      return copy;
    });
  };

  // Toggle Mark for Review
  const handleToggleFlag = () => {
    setFlagged((prev) => {
      const next = new Set(prev);
      if (next.has(currentQ.id)) next.delete(currentQ.id);
      else next.add(currentQ.id);
      return next;
    });
  };

  // Next / Previous
  const handleNext = () => {
    if (currentIdx < totalQuestions - 1) {
      setCurrentIdx((prev) => prev + 1);
    }
  };

  const handlePrev = () => {
    if (currentIdx > 0) {
      setCurrentIdx((prev) => prev - 1);
    }
  };

  // Stats calculation
  const answeredCount = Object.keys(userAnswers).length;
  const unansweredCount = totalQuestions - answeredCount;
  const flaggedCount = flagged.size;
  const isTimeCritical = secondsRemaining < 600; // Under 10 minutes

  return (
    <div className="min-h-screen bg-[#F8F6F0] dark:bg-[#09090B] text-ink-900 dark:text-paper-100 flex flex-col font-sans transition-colors">
      {/* 1. TOP EXAM HEADER */}
      <header className="sticky top-0 z-40 bg-paper-50/95 dark:bg-darkbg-900/95 backdrop-blur-md border-b border-paper-300 dark:border-darkbg-border px-4 sm:px-8 py-3 flex items-center justify-between shadow-xs">
        {/* Left: Test Code & Question Index */}
        <div className="flex items-center gap-3">
          <button
            onClick={onExitExam}
            className="p-1.5 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 text-ink-600 dark:text-ink-300 transition"
            title="Exit Exam"
          >
            <X className="w-5 h-5" />
          </button>
          <div>
            <span className="font-mono text-xs font-bold text-ink-900 dark:text-paper-100">
              {test.courseCode} • {test.code}
            </span>
            <div className="text-[11px] font-mono text-ink-500 dark:text-ink-400">
              Question {currentIdx + 1} of {totalQuestions}
            </div>
          </div>
        </div>

        {/* Center: Live Timer Countdown (Quzi & Quizzax style) */}
        <div
          className={`flex items-center gap-2 px-4 py-1.5 rounded-full border font-mono font-bold text-xs sm:text-sm tracking-wide transition-all ${
            isTimeCritical
              ? 'bg-rose-500/15 border-rose-500 text-rose-600 dark:text-rose-400 animate-pulse ring-2 ring-rose-500/20'
              : 'bg-paper-200/80 dark:bg-darkbg-800 border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50'
          }`}
        >
          <Timer className="w-4 h-4" />
          <span>{formatTime(secondsRemaining)}</span>
        </div>

        {/* Right: Grid Palette Toggle & Submit Exam */}
        <div className="flex items-center gap-2 sm:gap-3">
          <button
            onClick={() => setIsGridModalOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border text-xs font-mono transition cursor-pointer"
            title="Open 30-Question Progress Grid"
          >
            <Grid className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Progress Grid</span>
            <span className="px-1.5 py-0.2 rounded-full bg-paper-300 dark:bg-darkbg-700 text-[10px]">
              {answeredCount}/{totalQuestions}
            </span>
          </button>

          <button
            onClick={() => setIsSubmitModalOpen(true)}
            className="flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold tracking-wide transition shadow-sm cursor-pointer"
          >
            <Send className="w-3.5 h-3.5" />
            <span>Submit</span>
          </button>
        </div>
      </header>

      {/* 2. MAIN QUESTION CANVAS */}
      <main className="flex-1 max-w-4xl w-full mx-auto px-4 sm:px-6 py-6 sm:py-8 space-y-6">
        {/* Question Header Card */}
        <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-3xl p-6 sm:p-8 shadow-ticket dark:shadow-ticket-dark relative overflow-hidden transition-colors">
          {/* Top Bar: Topic Badge & Bookmark */}
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 rounded-full bg-amber-500/15 text-amber-700 dark:text-amber-300 border border-amber-500/20 text-xs font-mono font-semibold">
                {currentQ.topic || 'General Mathematics'}
              </span>
              <span className="text-xs font-mono text-ink-400 dark:text-ink-500">
                +1.0 / -0.25 Mark
              </span>
            </div>

            <button
              onClick={handleToggleFlag}
              className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono border transition ${
                flagged.has(currentQ.id)
                  ? 'bg-amber-500 text-ink-950 border-amber-500 font-bold'
                  : 'bg-paper-200 dark:bg-darkbg-800 text-ink-600 dark:text-ink-400 border-paper-300 dark:border-darkbg-border hover:text-ink-900'
              }`}
            >
              {flagged.has(currentQ.id) ? (
                <>
                  <BookmarkCheck className="w-3.5 h-3.5 fill-current" />
                  <span>Marked for Review</span>
                </>
              ) : (
                <>
                  <Bookmark className="w-3.5 h-3.5" />
                  <span>Mark for Review</span>
                </>
              )}
            </button>
          </div>

          {/* Question Text */}
          <div className="space-y-4">
            <div className="flex items-baseline gap-2">
              <span className="text-sm font-mono font-bold text-amber-600 dark:text-amber-400">
                Q.{currentIdx + 1}
              </span>
              <div className="text-base sm:text-lg font-medium text-ink-900 dark:text-paper-50 leading-relaxed">
                <MathText text={currentQ.question} />
              </div>
            </div>
          </div>

          {/* 3. OPTION CHOICES (Quizzax & Quzi pill style) */}
          <div className="grid grid-cols-1 gap-3 pt-6">
            {currentQ.options.map((opt, optIdx) => {
              const isSelected = userAnswers[currentQ.id] === optIdx;
              const optionLetters = ['A', 'B', 'C', 'D'];

              return (
                <button
                  key={optIdx}
                  onClick={() => handleSelectOption(optIdx)}
                  className={`group relative text-left p-4 rounded-2xl border transition-all duration-150 flex items-center justify-between cursor-pointer ${
                    isSelected
                      ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 dark:border-emerald-400 text-emerald-950 dark:text-emerald-100 shadow-md ring-2 ring-emerald-500/20'
                      : 'bg-paper-100/80 dark:bg-darkbg-800/80 border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 hover:border-amber-400 dark:hover:border-darkbg-700 hover:bg-paper-200/50 dark:hover:bg-darkbg-800'
                  }`}
                >
                  <div className="flex items-center gap-3.5 pr-4 flex-1">
                    {/* Circle Indicator */}
                    <div
                      className={`w-7 h-7 rounded-full flex items-center justify-center font-mono text-xs font-bold transition-colors shrink-0 ${
                        isSelected
                          ? 'bg-emerald-600 text-white shadow-xs'
                          : 'bg-paper-200 dark:bg-darkbg-700 text-ink-700 dark:text-paper-300 group-hover:bg-amber-400 group-hover:text-ink-900'
                      }`}
                    >
                      {optionLetters[optIdx]}
                    </div>

                    <div className="text-xs sm:text-sm font-medium leading-relaxed">
                      <MathText text={opt} />
                    </div>
                  </div>

                  {isSelected && (
                    <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                  )}
                </button>
              );
            })}
          </div>
        </div>
      </main>

      {/* 4. BOTTOM ACTION DOCK */}
      <footer className="sticky bottom-0 z-30 bg-paper-50/95 dark:bg-darkbg-900/95 backdrop-blur-md border-t border-paper-300 dark:border-darkbg-border px-4 sm:px-8 py-3 shadow-2xl">
        <div className="max-w-4xl mx-auto flex items-center justify-between gap-2 sm:gap-4">
          {/* Left: Previous & Clear */}
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrev}
              disabled={currentIdx === 0}
              className="px-3 py-2 rounded-xl bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-800 dark:text-paper-200 text-xs font-mono font-semibold transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed"
            >
              <ChevronLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Previous</span>
            </button>

            {userAnswers[currentQ.id] !== undefined && (
              <button
                onClick={handleClearResponse}
                className="px-3 py-2 rounded-xl bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-600 dark:text-ink-400 text-xs font-mono transition flex items-center gap-1 cursor-pointer"
                title="Clear selected option"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Clear</span>
              </button>
            )}
          </div>

          {/* Right: Skip & Save/Next */}
          <div className="flex items-center gap-2">
            <button
              onClick={handleNext}
              disabled={currentIdx === totalQuestions - 1}
              className="px-4 py-2 rounded-xl bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-800 dark:text-paper-200 text-xs font-mono font-semibold transition cursor-pointer disabled:cursor-not-allowed"
            >
              Skip
            </button>

            {currentIdx < totalQuestions - 1 ? (
              <button
                onClick={handleNext}
                className="px-5 py-2 rounded-xl bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs sm:text-sm font-bold tracking-wide transition flex items-center gap-1.5 shadow-sm cursor-pointer"
              >
                <span>Save & Next</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            ) : (
              <button
                onClick={() => setIsSubmitModalOpen(true)}
                className="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs sm:text-sm font-bold tracking-wide transition flex items-center gap-1.5 shadow-sm cursor-pointer"
              >
                <span>Review & Submit</span>
                <Send className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        </div>
      </footer>

      {/* 5. QUIZZAX-STYLE "QUIZ PROGRESS" GRID MODAL (Inspired by Reference Screenshot 2) */}
      {isGridModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-3xl p-6 max-w-md w-full shadow-2xl space-y-5 animate-fadeIn">
            {/* Modal Header */}
            <div className="flex items-center justify-between pb-3 border-b border-paper-200 dark:border-darkbg-border">
              <div className="flex items-center gap-2">
                <Grid className="w-5 h-5 text-ink-800 dark:text-paper-200" />
                <h3 className="font-bold text-base text-ink-900 dark:text-paper-50">
                  Quiz Progress
                </h3>
              </div>
              <button
                onClick={() => setIsGridModalOpen(false)}
                className="p-1 rounded-full text-ink-500 hover:text-ink-900 dark:hover:text-paper-100"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* 30-Question Grid */}
            <div className="grid grid-cols-5 gap-2.5 max-h-[340px] overflow-y-auto p-1">
              {test.questions.map((q, qIdx) => {
                const isAnswered = userAnswers[q.id] !== undefined;
                const isFlagged = flagged.has(q.id);
                const isCurrent = qIdx === currentIdx;

                let btnClass = 'bg-paper-200/80 dark:bg-darkbg-800 text-ink-600 dark:text-ink-400 border border-paper-300 dark:border-darkbg-border';

                if (isAnswered) {
                  btnClass = 'bg-emerald-500 text-white font-bold border border-emerald-600 shadow-xs';
                } else if (isFlagged) {
                  btnClass = 'bg-amber-400 text-ink-950 font-bold border border-amber-500';
                }

                if (isCurrent) {
                  btnClass += ' ring-2 ring-ink-900 dark:ring-paper-50 scale-105';
                }

                return (
                  <button
                    key={q.id}
                    onClick={() => {
                      setCurrentIdx(qIdx);
                      setIsGridModalOpen(false);
                    }}
                    className={`h-11 rounded-xl flex items-center justify-center font-mono text-xs transition-transform active:scale-95 cursor-pointer ${btnClass}`}
                  >
                    {qIdx + 1}
                  </button>
                );
              })}
            </div>

            {/* Legend (Inspired by Quizzax screenshot) */}
            <div className="grid grid-cols-3 gap-2 pt-2 border-t border-paper-200 dark:border-darkbg-border text-[11px] font-mono">
              <div className="flex items-center gap-1.5">
                <span className="w-3 h-3 rounded-sm bg-emerald-500"></span>
                <span>Solved ({answeredCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3 h-3 rounded-sm bg-paper-300 dark:bg-darkbg-700"></span>
                <span>Unsolved ({unansweredCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3 h-3 rounded-sm bg-amber-400"></span>
                <span>Review ({flaggedCount})</span>
              </div>
            </div>

            <button
              onClick={() => setIsGridModalOpen(false)}
              className="w-full py-2.5 rounded-xl bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 font-bold text-xs"
            >
              Continue Test
            </button>
          </div>
        </div>
      )}

      {/* 6. SUBMISSION CONFIRMATION MODAL */}
      {isSubmitModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-3xl p-6 sm:p-8 max-w-md w-full shadow-2xl space-y-6 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="w-12 h-12 rounded-full bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mx-auto">
                <HelpCircle className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-ink-900 dark:text-paper-50 font-cinzel">
                Submit Examination?
              </h3>
              <p className="text-xs text-ink-600 dark:text-ink-400">
                Are you sure you want to conclude the mock examination? You will immediately see your score and step-by-step solutions.
              </p>
            </div>

            {/* Overview Summary */}
            <div className="grid grid-cols-3 gap-2 p-3 bg-paper-200/60 dark:bg-darkbg-800/60 rounded-2xl text-center font-mono">
              <div className="space-y-0.5">
                <div className="text-[10px] text-ink-500">ATTEMPTED</div>
                <div className="text-sm font-bold text-emerald-600 dark:text-emerald-400">{answeredCount}</div>
              </div>
              <div className="space-y-0.5 border-x border-paper-300 dark:border-darkbg-border">
                <div className="text-[10px] text-ink-500">UNANSWERED</div>
                <div className="text-sm font-bold text-rose-600 dark:text-rose-400">{unansweredCount}</div>
              </div>
              <div className="space-y-0.5">
                <div className="text-[10px] text-ink-500">MARKED</div>
                <div className="text-sm font-bold text-amber-600 dark:text-amber-400">{flaggedCount}</div>
              </div>
            </div>

            {/* Modal Actions */}
            <div className="flex items-center gap-3">
              <button
                onClick={() => setIsSubmitModalOpen(false)}
                className="flex-1 py-3 rounded-2xl bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-800 dark:text-paper-200 font-bold text-xs font-mono transition"
              >
                Return to Test
              </button>
              <button
                onClick={handleSubmit}
                className="flex-1 py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs tracking-wide transition shadow-sm"
              >
                Confirm Submit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
