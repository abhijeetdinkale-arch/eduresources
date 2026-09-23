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
    <div className="min-h-screen bg-white dark:bg-black text-black dark:text-white flex flex-col font-sans transition-colors">
      {/* 1. TOP EXAM HEADER (BLACK & WHITE) */}
      <header className="sticky top-0 z-40 bg-white/95 dark:bg-black/95 backdrop-blur-md border-b-2 border-black dark:border-white/20 px-4 sm:px-8 py-3 flex items-center justify-between shadow-xs">
        {/* Left: Test Code & Question Index */}
        <div className="flex items-center gap-3">
          <button
            onClick={onExitExam}
            className="p-1.5 rounded-full hover:bg-zinc-100 dark:hover:bg-zinc-900 transition"
            title="Exit Exam"
          >
            <X className="w-5 h-5" />
          </button>
          <div>
            <span className="font-mono text-xs font-black">
              {test.courseCode} • {test.code}
            </span>
            <div className="text-[11px] font-mono text-zinc-500 font-bold">
              Question {currentIdx + 1} of {totalQuestions}
            </div>
          </div>
        </div>

        {/* Center: Live Timer Countdown */}
        <div
          className={`flex items-center gap-2 px-4 py-1.5 rounded-full border-2 font-mono font-black text-xs sm:text-sm tracking-widest ${
            isTimeCritical
              ? 'bg-black text-white dark:bg-white dark:text-black border-black dark:border-white animate-pulse'
              : 'bg-zinc-100 dark:bg-zinc-900 border-black dark:border-white/40 text-black dark:text-white'
          }`}
        >
          <Timer className="w-4 h-4" />
          <span>{formatTime(secondsRemaining)}</span>
        </div>

        {/* Right: Grid Palette Toggle & Submit Exam */}
        <div className="flex items-center gap-2 sm:gap-3">
          <button
            onClick={() => setIsGridModalOpen(true)}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-zinc-100 dark:bg-zinc-900 hover:bg-zinc-200 dark:hover:bg-zinc-800 border-2 border-black dark:border-white/40 text-xs font-mono font-bold transition cursor-pointer"
            title="Open 30-Question Progress Grid"
          >
            <Grid className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Progress</span>
            <span className="px-2 py-0.5 rounded-full bg-black text-white dark:bg-white dark:text-black font-black text-[10px]">
              {answeredCount}/{totalQuestions}
            </span>
          </button>

          <button
            onClick={() => setIsSubmitModalOpen(true)}
            className="flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-black hover:bg-zinc-800 dark:bg-white dark:hover:bg-zinc-200 text-white dark:text-black text-xs font-black tracking-wider uppercase transition shadow-md cursor-pointer"
          >
            <Send className="w-3.5 h-3.5" />
            <span>Submit</span>
          </button>
        </div>
      </header>

      {/* 2. MAIN QUESTION CANVAS */}
      <main className="flex-1 max-w-4xl w-full mx-auto px-4 sm:px-6 py-6 sm:py-8 space-y-6">
        {/* Question Header Card */}
        <div className="bg-zinc-50 dark:bg-zinc-950 border-2 border-black dark:border-white/20 rounded-[28px] p-6 sm:p-9 shadow-ticket dark:shadow-ticket-dark relative overflow-hidden transition-colors">
          {/* Top Bar: Topic Badge & Bookmark */}
          <div className="flex items-center justify-between mb-5">
            <div className="flex items-center gap-2">
              <span className="px-3.5 py-1 rounded-full bg-black text-white dark:bg-white dark:text-black text-xs font-mono font-bold">
                {currentQ.topic || 'Mathematics'}
              </span>
              <span className="text-xs font-mono text-zinc-600 dark:text-zinc-400 font-bold px-2 py-0.5 rounded-lg border border-black/20 dark:border-white/20">
                +1.00 / -0.25 Mark
              </span>
            </div>

            <button
              onClick={handleToggleFlag}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-mono border-2 transition cursor-pointer font-bold ${
                flagged.has(currentQ.id)
                  ? 'bg-black text-white dark:bg-white dark:text-black border-black dark:border-white shadow-xs'
                  : 'bg-zinc-100 dark:bg-zinc-900 text-zinc-600 dark:text-zinc-400 border-zinc-300 dark:border-zinc-700'
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
          <div className="space-y-4">
            <div className="flex items-baseline gap-2.5">
              <span className="text-sm font-mono font-black px-2.5 py-1 rounded-lg bg-black text-white dark:bg-white dark:text-black">
                Q.{currentIdx + 1}
              </span>
              <div className="text-base sm:text-lg font-bold text-black dark:text-white leading-relaxed font-sans">
                <MathText text={currentQ.question} />
              </div>
            </div>
          </div>

          {/* 3. OPTION CHOICES (Black & White Inversion Pills) */}
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
                      ? 'bg-black text-white dark:bg-white dark:text-black border-black dark:border-white shadow-xl scale-[1.01]'
                      : 'bg-white dark:bg-zinc-900 border-zinc-300 dark:border-zinc-800 text-black dark:text-zinc-200 hover:border-black dark:hover:border-white'
                  }`}
                >
                  <div className="flex items-center gap-4 pr-4 flex-1">
                    {/* Circle Indicator */}
                    <div
                      className={`w-8 h-8 rounded-full flex items-center justify-center font-mono text-xs font-black transition-colors shrink-0 ${
                        isSelected
                          ? 'bg-white text-black dark:bg-black dark:text-white'
                          : 'bg-zinc-100 dark:bg-zinc-800 text-black dark:text-white group-hover:bg-black group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black'
                      }`}
                    >
                      {optionLetters[optIdx]}
                    </div>

                    <div className="text-xs sm:text-sm font-semibold leading-relaxed">
                      <MathText text={opt} />
                    </div>
                  </div>

                  {isSelected && (
                    <div className="w-6 h-6 rounded-full bg-white text-black dark:bg-black dark:text-white flex items-center justify-center shrink-0">
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
      <footer className="sticky bottom-0 z-30 bg-white/95 dark:bg-black/95 backdrop-blur-md border-t-2 border-black dark:border-white/20 px-4 sm:px-8 py-3.5 shadow-2xl">
        <div className="max-w-4xl mx-auto flex items-center justify-between gap-2 sm:gap-4">
          {/* Left: Previous & Clear */}
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrev}
              disabled={currentIdx === 0}
              className="px-3.5 py-2.5 rounded-xl bg-zinc-100 dark:bg-zinc-900 hover:bg-zinc-200 dark:hover:bg-zinc-800 disabled:opacity-25 text-xs font-mono font-bold transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed border border-black/20 dark:border-white/20"
            >
              <ChevronLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Previous</span>
            </button>

            {userAnswers[currentQ.id] !== undefined && (
              <button
                onClick={handleClearResponse}
                className="px-3 py-2.5 rounded-xl bg-zinc-100 dark:bg-zinc-900 hover:bg-zinc-200 dark:hover:bg-zinc-800 text-xs font-mono font-bold transition flex items-center gap-1 cursor-pointer border border-black/20 dark:border-white/20"
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
              className="px-4 py-2.5 rounded-xl bg-zinc-100 dark:bg-zinc-900 hover:bg-zinc-200 dark:hover:bg-zinc-800 disabled:opacity-25 text-xs font-mono font-bold transition cursor-pointer disabled:cursor-not-allowed border border-black/20 dark:border-white/20"
            >
              Skip
            </button>

            {currentIdx < totalQuestions - 1 ? (
              <button
                onClick={handleNext}
                className="px-6 py-2.5 rounded-xl bg-black dark:bg-white hover:bg-zinc-800 dark:hover:bg-zinc-200 text-white dark:text-black text-xs sm:text-sm font-black tracking-wider uppercase transition flex items-center gap-1.5 shadow-md active:scale-98 cursor-pointer"
              >
                <span>Save & Next</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            ) : (
              <button
                onClick={() => setIsSubmitModalOpen(true)}
                className="px-6 py-2.5 rounded-xl bg-black dark:bg-white hover:bg-zinc-800 dark:hover:bg-zinc-200 text-white dark:text-black text-xs sm:text-sm font-black tracking-wider uppercase transition flex items-center gap-1.5 shadow-md active:scale-98 cursor-pointer"
              >
                <span>Review & Submit</span>
                <Send className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        </div>
      </footer>

      {/* 5. BLACK & WHITE PROGRESS GRID MODAL */}
      {isGridModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-xs flex items-center justify-center p-4 font-sans">
          <div className="bg-white dark:bg-black border-2 border-black dark:border-white rounded-[28px] p-6 max-w-md w-full shadow-2xl space-y-5 animate-fadeIn">
            <div className="flex items-center justify-between pb-3 border-b-2 border-black/10 dark:border-white/10">
              <div className="flex items-center gap-2">
                <Grid className="w-5 h-5" />
                <h3 className="font-black text-base">
                  Quiz Progress Matrix
                </h3>
              </div>
              <button
                onClick={() => setIsGridModalOpen(false)}
                className="p-1 rounded-full text-zinc-500 hover:text-black dark:hover:text-white"
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

                let btnClass = 'bg-zinc-100 dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300 border border-zinc-300 dark:border-zinc-700';

                if (isAnswered) {
                  btnClass = 'bg-black text-white dark:bg-white dark:text-black font-black border-2 border-black dark:border-white shadow-md';
                } else if (isFlagged) {
                  btnClass = 'bg-zinc-300 dark:bg-zinc-700 text-black dark:text-white font-black border-2 border-dashed border-black dark:border-white';
                }

                if (isCurrent) {
                  btnClass += ' ring-2 ring-black dark:ring-white scale-105';
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
            <div className="grid grid-cols-3 gap-2 pt-2 border-t-2 border-black/10 dark:border-white/10 text-[11px] font-mono font-bold">
              <div className="flex items-center gap-1.5">
                <span className="w-3.5 h-3.5 rounded-sm bg-black dark:bg-white"></span>
                <span>Solved ({answeredCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3.5 h-3.5 rounded-sm bg-zinc-200 dark:bg-zinc-800"></span>
                <span>Unsolved ({unansweredCount})</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-3.5 h-3.5 rounded-sm bg-zinc-400 dark:bg-zinc-600"></span>
                <span>Review ({flaggedCount})</span>
              </div>
            </div>

            <button
              onClick={() => setIsGridModalOpen(false)}
              className="w-full py-3 rounded-xl bg-black dark:bg-white text-white dark:text-black font-black text-xs font-mono uppercase tracking-wider shadow-md"
            >
              Continue Test
            </button>
          </div>
        </div>
      )}

      {/* 6. SUBMISSION CONFIRMATION MODAL */}
      {isSubmitModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-xs flex items-center justify-center p-4 font-sans">
          <div className="bg-white dark:bg-black border-2 border-black dark:border-white rounded-[28px] p-6 sm:p-8 max-w-md w-full shadow-2xl space-y-6 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="w-14 h-14 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center mx-auto">
                <Send className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-black font-cinzel">
                Submit Examination?
              </h3>
              <p className="text-xs text-zinc-600 dark:text-zinc-400">
                Are you ready to submit? You will instantly see your score and the step-by-step animated solutions.
              </p>
            </div>

            <div className="grid grid-cols-3 gap-2 p-3 bg-zinc-100 dark:bg-zinc-900 rounded-xl text-center font-mono border border-black/10 dark:border-white/10">
              <div className="space-y-0.5">
                <div className="text-[10px] text-zinc-500 font-bold">ATTEMPTED</div>
                <div className="text-base font-black">{answeredCount}</div>
              </div>
              <div className="space-y-0.5 border-x border-black/10 dark:border-white/10">
                <div className="text-[10px] text-zinc-500 font-bold">SKIPPED</div>
                <div className="text-base font-black">{unansweredCount}</div>
              </div>
              <div className="space-y-0.5">
                <div className="text-[10px] text-zinc-500 font-bold">FLAGGED</div>
                <div className="text-base font-black">{flaggedCount}</div>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button
                onClick={() => setIsSubmitModalOpen(false)}
                className="flex-1 py-3 rounded-xl bg-zinc-100 dark:bg-zinc-900 hover:bg-zinc-200 dark:hover:bg-zinc-800 font-bold text-xs font-mono transition border border-black/20 dark:border-white/20"
              >
                Return
              </button>
              <button
                onClick={handleSubmit}
                className="flex-1 py-3 rounded-xl bg-black dark:bg-white hover:bg-zinc-800 dark:hover:bg-zinc-200 text-white dark:text-black font-black text-xs font-mono tracking-wider uppercase transition shadow-md"
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
