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
  Check
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
    <div className="min-h-screen bg-paper-100 dark:bg-darkbg-950 text-ink-900 dark:text-paper-50 flex flex-col font-sans transition-colors">
      {/* 1. TOP EXAM HEADER */}
      <header className="sticky top-0 z-40 bg-paper-50/95 dark:bg-darkbg-900/95 backdrop-blur-md border-b border-paper-300 dark:border-darkbg-border px-4 sm:px-8 py-3 flex items-center justify-between shadow-xs">
        {/* Left: Test Code & Question Index */}
        <div className="flex items-center gap-3">
          <button
            onClick={onExitExam}
            className="p-2 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 text-ink-900 dark:text-paper-50 transition cursor-pointer"
            title="Exit Exam"
          >
            <X className="w-5 h-5" />
          </button>
          <div>
            <span className="font-mono text-xs font-bold text-ink-900 dark:text-paper-50">
              {test.courseCode} • {test.code}
            </span>
            <div className="text-[11px] font-mono text-ink-600 dark:text-ink-400 font-semibold">
              Question {currentIdx + 1} of {totalQuestions}
            </div>
          </div>
        </div>

        {/* Center: Live Timer Countdown */}
        <div
          className={`flex items-center gap-2 px-4 py-1.5 rounded-full border font-mono font-bold text-xs sm:text-sm tracking-widest ${
            isTimeCritical
              ? 'bg-terracotta-500 text-white border-terracotta-600 animate-pulse'
              : 'bg-paper-200 dark:bg-darkbg-800 border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50'
          }`}
        >
          <Timer className="w-4 h-4 text-inherit" />
          <span>{formatTime(secondsRemaining)}</span>
        </div>

        {/* Right: Grid Palette Toggle & Submit Exam */}
        <div className="flex items-center gap-2 sm:gap-3">
          <button
            onClick={() => setIsGridModalOpen(true)}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-paper-200 hover:bg-paper-300 dark:bg-darkbg-800 dark:hover:bg-darkbg-700 border border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50 text-xs font-mono font-bold transition cursor-pointer"
            title="Open 30-Question Progress Grid"
          >
            <Grid className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Progress</span>
            <span className="px-2 py-0.5 rounded-full bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 font-bold text-[10px]">
              {answeredCount}/{totalQuestions}
            </span>
          </button>

          <button
            onClick={() => setIsSubmitModalOpen(true)}
            className="flex items-center gap-1.5 px-5 py-2 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs font-semibold tracking-wider uppercase transition shadow-md cursor-pointer"
          >
            <Send className="w-3.5 h-3.5" />
            <span>Submit</span>
          </button>
        </div>
      </header>

      {/* 2. MAIN QUESTION CANVAS */}
      <main className="flex-1 max-w-4xl w-full mx-auto px-4 sm:px-6 py-6 sm:py-8 space-y-6">
        {/* Question Header Card */}
        <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[32px] p-6 sm:p-9 shadow-ticket dark:shadow-ticket-dark relative overflow-hidden text-ink-900 dark:text-paper-50">
          {/* Top Bar: Topic Badge & Bookmark */}
          <div className="flex items-center justify-between mb-5">
            <div className="flex items-center gap-2">
              <span className="px-3.5 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50 text-xs font-mono font-bold">
                {currentQ.topic || 'Mathematics'}
              </span>
              <span className="text-xs font-mono text-ink-800 dark:text-paper-200 font-semibold px-2.5 py-1 rounded-lg border border-paper-300 dark:border-darkbg-border bg-paper-100 dark:bg-darkbg-850">
                +1.00 / -0.25 Mark
              </span>
            </div>

            <button
              onClick={handleToggleFlag}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-mono border transition cursor-pointer font-semibold ${
                flagged.has(currentQ.id)
                  ? 'bg-ochre-400 text-ink-950 border-ochre-500 shadow-xs font-bold'
                  : 'bg-paper-100 hover:bg-paper-200 dark:bg-darkbg-800 dark:hover:bg-darkbg-700 text-ink-800 dark:text-paper-200 border-paper-300 dark:border-darkbg-border'
              }`}
            >
              {flagged.has(currentQ.id) ? (
                <>
                  <BookmarkCheck className="w-3.5 h-3.5 fill-current" />
                  <span>Marked</span>
                </>
              ) : (
                <>
                  <Bookmark className="w-3.5 h-3.5" />
                  <span>Review</span>
                </>
              )}
            </button>
          </div>

          {/* Question Text */}
          <div className="space-y-4 pt-1">
            <div className="flex items-baseline gap-3">
              <span className="text-sm font-mono font-bold px-2.5 py-1 rounded-lg bg-paper-200 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 border border-paper-300 dark:border-darkbg-border shrink-0">
                Q.{currentIdx + 1}
              </span>
              <div className="text-base sm:text-xl font-bold text-ink-900 dark:text-paper-50 leading-relaxed font-sans">
                <MathText text={currentQ.question} />
              </div>
            </div>
          </div>

          {/* 3. OPTION CHOICES (Crisp Contrast in both Light and Dark modes) */}
          <div className="grid grid-cols-1 gap-3.5 pt-6">
            {currentQ.options.map((opt, optIdx) => {
              const isSelected = userAnswers[currentQ.id] === optIdx;
              const optionLetters = ['A', 'B', 'C', 'D'];

              return (
                <button
                  key={optIdx}
                  onClick={() => handleSelectOption(optIdx)}
                  className={`group relative text-left p-4 sm:p-5 rounded-2xl border-2 transition-all duration-150 flex items-center justify-between cursor-pointer ${
                    isSelected
                      ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 border-ink-900 dark:border-paper-50 shadow-ticket scale-[1.01]'
                      : 'bg-paper-50 hover:bg-paper-100 dark:bg-darkbg-850 dark:hover:bg-darkbg-800 border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50'
                  }`}
                >
                  <div className="flex items-center gap-4 pr-4 flex-1">
                    {/* Circle Indicator */}
                    <div
                      className={`w-8 h-8 rounded-full flex items-center justify-center font-mono text-xs font-bold transition-colors shrink-0 ${
                        isSelected
                          ? 'bg-paper-50 dark:bg-ink-900 text-ink-900 dark:text-paper-50'
                          : 'bg-paper-200 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 border border-paper-300 dark:border-darkbg-border group-hover:border-ink-900 dark:group-hover:border-paper-50'
                      }`}
                    >
                      {optionLetters[optIdx]}
                    </div>

                    <div className={`text-xs sm:text-sm leading-relaxed ${
                      isSelected
                        ? 'font-bold text-paper-50 dark:text-ink-900'
                        : 'font-semibold text-ink-900 dark:text-paper-50'
                    }`}>
                      <MathText text={opt} />
                    </div>
                  </div>

                  {isSelected && (
                    <div className="w-6 h-6 rounded-full bg-paper-50 dark:bg-ink-900 text-ink-900 dark:text-paper-50 flex items-center justify-center shrink-0 shadow-xs">
                      <Check className="w-4 h-4 stroke-[3]" />
                    </div>
                  )}
                </button>
              );
            })}
          </div>
        </div>
      </main>

      {/* 4. BOTTOM ACTION DOCK */}
      <footer className="sticky bottom-0 z-30 bg-paper-50/95 dark:bg-darkbg-900/95 backdrop-blur-md border-t border-paper-300 dark:border-darkbg-border px-4 sm:px-8 py-3.5 shadow-2xl text-ink-900 dark:text-paper-50">
        <div className="max-w-4xl mx-auto flex items-center justify-between gap-2 sm:gap-4">
          {/* Left: Previous & Clear */}
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrev}
              disabled={currentIdx === 0}
              className="px-4 py-2.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition flex items-center gap-1.5 cursor-pointer disabled:cursor-not-allowed border border-paper-300 dark:border-darkbg-border"
            >
              <ChevronLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Previous</span>
            </button>

            {userAnswers[currentQ.id] !== undefined && (
              <button
                onClick={handleClearResponse}
                className="px-3.5 py-2.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition flex items-center gap-1.5 cursor-pointer border border-paper-300 dark:border-darkbg-border"
                title="Clear selected option"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Clear</span>
              </button>
            )}
          </div>

          {/* Right: Skip & Save/Next */}
          <div className="flex items-center gap-2.5">
            <button
              onClick={handleNext}
              disabled={currentIdx === totalQuestions - 1}
              className="px-5 py-2.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition cursor-pointer disabled:cursor-not-allowed border border-paper-300 dark:border-darkbg-border"
            >
              Skip
            </button>

            {currentIdx < totalQuestions - 1 ? (
              <button
                onClick={handleNext}
                className="px-6 py-2.5 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs sm:text-sm font-semibold tracking-wider uppercase transition flex items-center gap-2 shadow-md cursor-pointer"
              >
                <span>Save & Next</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            ) : (
              <button
                onClick={() => setIsSubmitModalOpen(true)}
                className="px-6 py-2.5 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs sm:text-sm font-semibold tracking-wider uppercase transition flex items-center gap-2 shadow-md cursor-pointer"
              >
                <span>Review & Submit</span>
                <Send className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        </div>
      </footer>

      {/* 5. PROGRESS GRID MODAL */}
      {isGridModalOpen && (
        <div className="fixed inset-0 z-50 bg-ink-900/60 dark:bg-black/80 backdrop-blur-xs flex items-center justify-center p-4 font-sans text-ink-900 dark:text-paper-50">
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[28px] p-6 max-w-md w-full shadow-ticket dark:shadow-ticket-dark space-y-5 animate-fadeIn">
            <div className="flex items-center justify-between pb-3 border-b border-paper-300 dark:border-darkbg-border">
              <div className="flex items-center gap-2">
                <Grid className="w-5 h-5 text-ink-900 dark:text-paper-50" />
                <h3 className="font-bold text-base">
                  Quiz Progress Matrix
                </h3>
              </div>
              <button
                onClick={() => setIsGridModalOpen(false)}
                className="p-1.5 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 text-ink-600 dark:text-paper-300 cursor-pointer"
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

                let btnClass = 'bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border hover:bg-paper-300 dark:hover:bg-darkbg-700';

                if (isAnswered) {
                  btnClass = 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 font-bold border-2 border-ink-900 dark:border-paper-50 shadow-xs';
                } else if (isFlagged) {
                  btnClass = 'bg-ochre-400 text-ink-950 font-bold border-2 border-ochre-500';
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
                    className={`h-11 rounded-xl flex items-center justify-center font-mono text-xs transition-all active:scale-95 cursor-pointer font-bold ${btnClass}`}
                  >
                    {qIdx + 1}
                  </button>
                );
              })}
            </div>

            {/* Legend */}
            <div className="grid grid-cols-3 gap-2 pt-2 border-t border-paper-300 dark:border-darkbg-border text-[11px] font-mono font-semibold text-ink-600 dark:text-paper-300">
              <div className="flex items-center gap-1.5">
                <span className="w-3.5 h-3.5 rounded-sm bg-ink-900 dark:bg-paper-50"></span>
                <span>Solved ({answeredCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3.5 h-3.5 rounded-sm bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border"></span>
                <span>Unsolved ({unansweredCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3.5 h-3.5 rounded-sm bg-ochre-400"></span>
                <span>Review ({flaggedCount})</span>
              </div>
            </div>

            <button
              onClick={() => setIsGridModalOpen(false)}
              className="w-full py-3 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 font-semibold text-xs font-mono uppercase tracking-wider shadow-md cursor-pointer"
            >
              Continue Test
            </button>
          </div>
        </div>
      )}

      {/* 6. SUBMISSION CONFIRMATION MODAL */}
      {isSubmitModalOpen && (
        <div className="fixed inset-0 z-50 bg-ink-900/60 dark:bg-black/80 backdrop-blur-xs flex items-center justify-center p-4 font-sans text-ink-900 dark:text-paper-50">
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[28px] p-6 sm:p-8 max-w-md w-full shadow-ticket dark:shadow-ticket-dark space-y-6 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="w-14 h-14 rounded-full bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 flex items-center justify-center mx-auto shadow-md">
                <Send className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold font-cinzel text-ink-900 dark:text-paper-50">
                Submit Examination?
              </h3>
              <p className="text-xs text-ink-600 dark:text-ink-400">
                Are you ready to submit? You will instantly see your score and the step-by-step animated solutions.
              </p>
            </div>

            <div className="grid grid-cols-3 gap-2 p-3 bg-paper-100 dark:bg-darkbg-800 rounded-xl text-center font-mono border border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50">
              <div className="space-y-0.5">
                <div className="text-[10px] text-ink-600 dark:text-ink-400 font-bold">ATTEMPTED</div>
                <div className="text-base font-black">{answeredCount}</div>
              </div>
              <div className="space-y-0.5 border-x border-paper-300 dark:border-darkbg-border">
                <div className="text-[10px] text-ink-600 dark:text-ink-400 font-bold">SKIPPED</div>
                <div className="text-base font-black">{unansweredCount}</div>
              </div>
              <div className="space-y-0.5">
                <div className="text-[10px] text-ink-600 dark:text-ink-400 font-bold">FLAGGED</div>
                <div className="text-base font-black">{flaggedCount}</div>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button
                onClick={() => setIsSubmitModalOpen(false)}
                className="flex-1 py-3 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 font-bold text-xs font-mono transition border border-paper-300 dark:border-darkbg-border cursor-pointer text-ink-900 dark:text-paper-100"
              >
                Return
              </button>
              <button
                onClick={handleSubmit}
                className="flex-1 py-3 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 font-semibold text-xs font-mono tracking-wider uppercase transition shadow-md cursor-pointer"
              >
                Submit Now
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
