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
  Check,
  Maximize2,
  Minimize2,
  Keyboard,
  HelpCircle,
  AlertTriangle
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
  const [isExitConfirmOpen, setIsExitConfirmOpen] = useState(false);
  const [isShortcutsModalOpen, setIsShortcutsModalOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [fontSize, setFontSize] = useState('md'); // 'sm' | 'md' | 'lg'
  const timerRef = useRef(null);

  const currentQ = test.questions[currentIdx];
  const totalQuestions = test.questions.length;

  // Track Fullscreen status
  useEffect(() => {
    const handleFsChange = () => {
      setIsFullscreen(Boolean(document.fullscreenElement));
    };
    document.addEventListener('fullscreenchange', handleFsChange);
    return () => document.removeEventListener('fullscreenchange', handleFsChange);
  }, []);

  const toggleFullscreen = () => {
    try {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else if (document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
      }
    } catch {}
  };

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
  const handleSelectOption = useCallback((optIndex) => {
    const qId = test.questions[currentIdx].id;
    setUserAnswers((prev) => ({
      ...prev,
      [qId]: optIndex,
    }));
  }, [currentIdx, test.questions]);

  // Clear current response
  const handleClearResponse = useCallback(() => {
    const qId = test.questions[currentIdx].id;
    setUserAnswers((prev) => {
      const copy = { ...prev };
      delete copy[qId];
      return copy;
    });
  }, [currentIdx, test.questions]);

  // Toggle Mark for Review
  const handleToggleFlag = useCallback(() => {
    const qId = test.questions[currentIdx].id;
    setFlagged((prev) => {
      const next = new Set(prev);
      if (next.has(qId)) next.delete(qId);
      else next.add(qId);
      return next;
    });
  }, [currentIdx, test.questions]);

  // Next / Previous
  const handleNext = useCallback(() => {
    setCurrentIdx((prev) => Math.min(prev + 1, totalQuestions - 1));
  }, [totalQuestions]);

  const handlePrev = useCallback(() => {
    setCurrentIdx((prev) => Math.max(prev - 1, 0));
  }, []);

  // Keyboard Shortcuts Navigation Hook
  useEffect(() => {
    const handleKeyDown = (e) => {
      // Ignore if typing in text input
      if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

      // Escape key handles modals
      if (e.key === 'Escape') {
        setIsGridModalOpen(false);
        setIsSubmitModalOpen(false);
        setIsExitConfirmOpen(false);
        setIsShortcutsModalOpen(false);
        return;
      }

      // If any modal is active, pause shortcut actions
      if (isGridModalOpen || isSubmitModalOpen || isExitConfirmOpen || isShortcutsModalOpen) {
        return;
      }

      const key = e.key.toUpperCase();

      // A/B/C/D or 1/2/3/4 option selection
      if (key === 'A' || key === '1') {
        e.preventDefault();
        handleSelectOption(0);
      } else if (key === 'B' || key === '2') {
        e.preventDefault();
        handleSelectOption(1);
      } else if (key === 'C' || key === '3') {
        if (!e.ctrlKey && !e.metaKey) {
          e.preventDefault();
          handleSelectOption(2);
        }
      } else if (key === 'D' || key === '4') {
        e.preventDefault();
        handleSelectOption(3);
      } else if (e.key === 'ArrowRight' || e.key === 'Enter') {
        e.preventDefault();
        if (currentIdx < totalQuestions - 1) {
          handleNext();
        } else {
          setIsSubmitModalOpen(true);
        }
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        handlePrev();
      } else if (key === 'F' || key === 'M') {
        e.preventDefault();
        handleToggleFlag();
      } else if (key === 'X' || e.key === 'Backspace' || e.key === 'Delete') {
        e.preventDefault();
        handleClearResponse();
      } else if (key === 'G' || key === 'P') {
        e.preventDefault();
        setIsGridModalOpen(true);
      } else if (e.key === '?' || (e.shiftKey && e.key === '/')) {
        e.preventDefault();
        setIsShortcutsModalOpen(true);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [
    currentIdx,
    totalQuestions,
    isGridModalOpen,
    isSubmitModalOpen,
    isExitConfirmOpen,
    isShortcutsModalOpen,
    handleSelectOption,
    handleNext,
    handlePrev,
    handleToggleFlag,
    handleClearResponse
  ]);

  // Stats calculation
  const answeredCount = Object.keys(userAnswers).length;
  const unansweredCount = totalQuestions - answeredCount;
  const flaggedCount = flagged.size;
  const isTimeCritical = secondsRemaining < 600; // Under 10 minutes

  // Question typography classes based on user preference
  const questionTextClass = fontSize === 'lg'
    ? 'text-lg sm:text-2xl'
    : fontSize === 'sm'
    ? 'text-sm sm:text-base'
    : 'text-base sm:text-xl';

  const optionTextClass = fontSize === 'lg'
    ? 'text-sm sm:text-base'
    : fontSize === 'sm'
    ? 'text-[11px] sm:text-xs'
    : 'text-xs sm:text-sm';

  return (
    <div className="min-h-screen text-ink-900 dark:text-paper-50 flex flex-col font-sans transition-colors relative selection:bg-ochre-400 selection:text-ink-950">
      {/* 1. TOP EXAM HEADER */}
      <header className="sticky top-0 z-40 bg-paper-50/90 dark:bg-darkbg-900/90 backdrop-blur-md border-b border-paper-300 dark:border-darkbg-border px-4 sm:px-8 py-3 flex items-center justify-between shadow-xs">
        {/* Left: Test Code & Question Index */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => setIsExitConfirmOpen(true)}
            className="p-2 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 text-ink-900 dark:text-paper-50 transition cursor-pointer"
            title="Exit Exam"
          >
            <X className="w-5 h-5" />
          </button>
          <div>
            <span className="font-mono text-xs font-bold text-ink-900 dark:text-paper-50 tracking-wider">
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
              : 'bg-paper-200 dark:bg-darkbg-800 border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50 shadow-xs'
          }`}
        >
          <Timer className="w-4 h-4 text-inherit" />
          <span>{formatTime(secondsRemaining)}</span>
        </div>

        {/* Right: Quick Action Controls */}
        <div className="flex items-center gap-2 sm:gap-2.5">
          {/* Fullscreen Toggle */}
          <button
            onClick={toggleFullscreen}
            className="p-2 rounded-full bg-paper-200 hover:bg-paper-300 dark:bg-darkbg-800 dark:hover:bg-darkbg-700 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 transition cursor-pointer hidden md:flex items-center justify-center"
            title={isFullscreen ? 'Exit Fullscreen (Esc)' : 'Enter Fullscreen Exam Mode'}
          >
            {isFullscreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
          </button>

          {/* Keyboard Shortcuts Trigger */}
          <button
            onClick={() => setIsShortcutsModalOpen(true)}
            className="p-2 rounded-full bg-paper-200 hover:bg-paper-300 dark:bg-darkbg-800 dark:hover:bg-darkbg-700 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 transition cursor-pointer hidden sm:flex items-center justify-center"
            title="Keyboard Shortcuts (?)"
          >
            <Keyboard className="w-4 h-4" />
          </button>

          {/* Grid Progress Matrix */}
          <button
            onClick={() => setIsGridModalOpen(true)}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-paper-200 hover:bg-paper-300 dark:bg-darkbg-800 dark:hover:bg-darkbg-700 border border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50 text-xs font-mono font-bold transition cursor-pointer"
            title="Open Question Progress Grid (G)"
          >
            <Grid className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Progress</span>
            <span className="px-2 py-0.5 rounded-full bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 font-bold text-[10px]">
              {answeredCount}/{totalQuestions}
            </span>
          </button>

          {/* Submit Test Button */}
          <button
            onClick={() => setIsSubmitModalOpen(true)}
            className="flex items-center gap-1.5 px-4 sm:px-5 py-1.5 sm:py-2 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs font-semibold tracking-wider uppercase transition shadow-md cursor-pointer"
          >
            <Send className="w-3.5 h-3.5" />
            <span>Submit</span>
          </button>
        </div>
      </header>

      {/* Hairline Exam Progress Bar */}
      <div className="w-full h-1 bg-paper-200/80 dark:bg-darkbg-800/80 overflow-hidden sticky top-[57px] z-30">
        <div
          className="h-full bg-ink-900 dark:bg-paper-100 transition-all duration-300 ease-out"
          style={{ width: `${(answeredCount / totalQuestions) * 100}%` }}
        />
      </div>

      {/* 2. RAPID QUESTION JUMP STRIP & CONTROLS */}
      <div className="max-w-4xl w-full mx-auto px-4 sm:px-6 pt-4 pb-1 flex flex-col sm:flex-row items-center justify-between gap-3">
        {/* Horizontal Quick-Strip */}
        <div className="w-full sm:flex-1 overflow-x-auto no-scrollbar flex items-center gap-1.5 py-1">
          {test.questions.map((q, qIdx) => {
            const isAnswered = userAnswers[q.id] !== undefined;
            const isFlagged = flagged.has(q.id);
            const isCurrent = qIdx === currentIdx;

            let pillStyle = 'bg-paper-200/80 dark:bg-darkbg-850 text-ink-700 dark:text-paper-300 border-paper-300 dark:border-darkbg-border hover:bg-paper-300';
            if (isAnswered) {
              pillStyle = 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 font-bold shadow-xs border-ink-900 dark:border-paper-50';
            } else if (isFlagged) {
              pillStyle = 'bg-ochre-400 text-ink-950 font-bold border-ochre-500';
            }

            if (isCurrent) {
              pillStyle += ' ring-2 ring-ink-900 dark:ring-paper-50 scale-110 z-10 font-black';
            }

            return (
              <button
                key={q.id}
                onClick={() => setCurrentIdx(qIdx)}
                className={`w-7 h-7 sm:w-8 sm:h-8 rounded-lg shrink-0 flex items-center justify-center font-mono text-[11px] border transition cursor-pointer ${pillStyle}`}
                title={`Question ${qIdx + 1}`}
              >
                {qIdx + 1}
              </button>
            );
          })}
        </div>

        {/* Text Size Controls */}
        <div className="flex items-center gap-1.5 shrink-0 self-end sm:self-auto">
          <span className="text-[10px] font-mono text-ink-600 dark:text-ink-400 uppercase tracking-widest hidden md:inline">
            Zoom:
          </span>
          <div className="flex items-center rounded-lg border border-paper-300 dark:border-darkbg-border bg-paper-100/90 dark:bg-darkbg-850 p-0.5 text-xs font-mono">
            <button
              onClick={() => setFontSize('sm')}
              className={`px-2 py-0.5 rounded transition ${fontSize === 'sm' ? 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 font-bold' : 'text-ink-700 dark:text-paper-300 hover:text-ink-900'}`}
              title="Small text"
            >
              A-
            </button>
            <button
              onClick={() => setFontSize('md')}
              className={`px-2 py-0.5 rounded transition ${fontSize === 'md' ? 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 font-bold' : 'text-ink-700 dark:text-paper-300 hover:text-ink-900'}`}
              title="Medium standard text"
            >
              A
            </button>
            <button
              onClick={() => setFontSize('lg')}
              className={`px-2 py-0.5 rounded transition ${fontSize === 'lg' ? 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 font-bold' : 'text-ink-700 dark:text-paper-300 hover:text-ink-900'}`}
              title="Large text"
            >
              A+
            </button>
          </div>
        </div>
      </div>

      {/* 3. MAIN QUESTION CANVAS */}
      <main className="flex-1 max-w-4xl w-full mx-auto px-4 sm:px-6 py-4 sm:py-6 space-y-6">
        {/* Question Header Card */}
        <div className="bg-paper-50/95 dark:bg-darkbg-900/95 backdrop-blur-md border border-paper-300/80 dark:border-darkbg-border rounded-[32px] p-6 sm:p-10 shadow-ticket dark:shadow-ticket-dark relative overflow-hidden text-ink-900 dark:text-paper-50 transition-all">
          {/* Top Bar: Topic Badge & Bookmark */}
          <div className="flex items-center justify-between mb-6 pb-4 border-b border-paper-200 dark:border-darkbg-800">
            <div className="flex items-center gap-2.5 flex-wrap">
              <span className="px-3.5 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-100 text-xs font-mono font-bold tracking-wide">
                {currentQ.topic || 'Engineering Subject'}
              </span>
              <span className="text-[11px] font-mono text-emerald-700 dark:text-emerald-400 font-bold px-3 py-1 rounded-full border border-emerald-500/20 bg-emerald-500/10">
                +1.00 Mark
              </span>
              <span className="text-[11px] font-mono text-terracotta-600 dark:text-terracotta-400 font-bold px-3 py-1 rounded-full border border-terracotta-500/20 bg-terracotta-500/10">
                -0.25 Negative
              </span>
            </div>

            <button
              onClick={handleToggleFlag}
              className={`flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-mono border transition-all cursor-pointer font-bold ${
                flagged.has(currentQ.id)
                  ? 'bg-ochre-400 text-ink-950 border-ochre-500 shadow-xs ring-2 ring-ochre-400/30'
                  : 'bg-paper-100 hover:bg-paper-200 dark:bg-darkbg-800 dark:hover:bg-darkbg-700 text-ink-700 dark:text-paper-300 border-paper-300 dark:border-darkbg-border'
              }`}
              title="Bookmark for review later (Hotkey: F)"
            >
              {flagged.has(currentQ.id) ? (
                <>
                  <BookmarkCheck className="w-3.5 h-3.5 fill-current" />
                  <span>Flagged (F)</span>
                </>
              ) : (
                <>
                  <Bookmark className="w-3.5 h-3.5" />
                  <span>Review Later (F)</span>
                </>
              )}
            </button>
          </div>

          {/* Question Text */}
          <div className="space-y-4 pt-1">
            <div className="flex items-baseline gap-3.5">
              <span className="text-xs sm:text-sm font-mono font-bold px-3 py-1.5 rounded-xl bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 shrink-0 shadow-xs">
                Q.{currentIdx + 1}
              </span>
              <div className={`${questionTextClass} font-bold text-ink-900 dark:text-paper-50 leading-relaxed font-sans tracking-tight`}>
                <MathText text={currentQ.question} />
              </div>
            </div>
          </div>

          {/* 4. OPTION CHOICES (Enhanced Spacing, Contrast, and Hotkey Badge) */}
          <div className="grid grid-cols-1 gap-3.5 pt-8">
            {currentQ.options.map((opt, optIdx) => {
              const isSelected = userAnswers[currentQ.id] === optIdx;
              const optionLetters = ['A', 'B', 'C', 'D'];

              return (
                <button
                  key={optIdx}
                  onClick={() => handleSelectOption(optIdx)}
                  className={`group relative text-left p-4 sm:p-5 rounded-2xl border-2 transition-all duration-200 flex items-center justify-between cursor-pointer ${
                    isSelected
                      ? 'bg-ink-950 dark:bg-paper-50 text-paper-50 dark:text-ink-950 border-ink-950 dark:border-paper-50 shadow-ticket ring-2 ring-ink-900/15 dark:ring-paper-100/30 scale-[1.008]'
                      : 'bg-paper-50/90 hover:bg-paper-100 dark:bg-darkbg-850/90 dark:hover:bg-darkbg-800 border-paper-300/80 dark:border-darkbg-border hover:border-ink-400/50 dark:hover:border-paper-300/40 text-ink-900 dark:text-paper-50 shadow-xs'
                  }`}
                >
                  <div className="flex items-center gap-4 sm:gap-5 pr-4 flex-1">
                    {/* Circle Indicator with Hotkey badge */}
                    <div
                      className={`w-9 h-9 rounded-full flex items-center justify-center font-mono text-xs font-bold transition-all shrink-0 ${
                        isSelected
                          ? 'bg-paper-50 dark:bg-ink-950 text-ink-950 dark:text-paper-50 shadow-xs'
                          : 'bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200 border border-paper-300 dark:border-darkbg-border group-hover:border-ink-900 dark:group-hover:border-paper-50 group-hover:scale-105'
                      }`}
                    >
                      {optionLetters[optIdx]}
                    </div>

                    <div className={`${optionTextClass} leading-relaxed ${
                      isSelected
                        ? 'font-bold text-paper-50 dark:text-ink-950'
                        : 'font-medium text-ink-900 dark:text-paper-100'
                    }`}>
                      <MathText text={opt} />
                    </div>
                  </div>

                  {isSelected && (
                    <div className="w-6 h-6 rounded-full bg-paper-50 dark:bg-ink-950 text-ink-950 dark:text-paper-50 flex items-center justify-center shrink-0 shadow-xs">
                      <Check className="w-4 h-4 stroke-[3]" />
                    </div>
                  )}
                </button>
              );
            })}
          </div>
        </div>

        {/* Hotkey Helper Banner */}
        <div className="flex items-center justify-center gap-3 text-[11px] font-mono text-ink-600 dark:text-ink-400 py-1">
          <span>Keyboard:</span>
          <span className="px-1.5 py-0.5 rounded bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border font-bold">A-D</span>
          <span>Select</span>
          <span>•</span>
          <span className="px-1.5 py-0.5 rounded bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border font-bold">→</span>
          <span>Next</span>
          <span>•</span>
          <span className="px-1.5 py-0.5 rounded bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border font-bold">←</span>
          <span>Prev</span>
          <span>•</span>
          <span className="px-1.5 py-0.5 rounded bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border font-bold">F</span>
          <span>Flag</span>
          <button
            onClick={() => setIsShortcutsModalOpen(true)}
            className="underline underline-offset-2 ml-1 hover:text-ink-900 dark:hover:text-paper-50 cursor-pointer"
          >
            All shortcuts (?)
          </button>
        </div>
      </main>

      {/* 5. BOTTOM ACTION DOCK */}
      <footer className="sticky bottom-0 z-30 bg-paper-50/95 dark:bg-darkbg-900/95 backdrop-blur-md border-t border-paper-300 dark:border-darkbg-border px-4 sm:px-8 py-3.5 shadow-2xl text-ink-900 dark:text-paper-50">
        <div className="max-w-4xl mx-auto flex items-center justify-between gap-2 sm:gap-4">
          {/* Left: Previous & Clear */}
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrev}
              disabled={currentIdx === 0}
              className="px-4 py-2.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition flex items-center gap-1.5 cursor-pointer disabled:cursor-not-allowed border border-paper-300 dark:border-darkbg-border"
              title="Previous Question (Left Arrow)"
            >
              <ChevronLeft className="w-4 h-4" />
              <span className="hidden sm:inline">Previous</span>
            </button>

            {userAnswers[currentQ.id] !== undefined && (
              <button
                onClick={handleClearResponse}
                className="px-3.5 py-2.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition flex items-center gap-1.5 cursor-pointer border border-paper-300 dark:border-darkbg-border"
                title="Clear selected option (Backspace / X)"
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
                title="Save & Next Question (Right Arrow / Enter)"
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

      {/* 6. PROGRESS GRID MODAL */}
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

      {/* 7. EXIT CONFIRMATION MODAL */}
      {isExitConfirmOpen && (
        <div className="fixed inset-0 z-50 bg-ink-900/60 dark:bg-black/80 backdrop-blur-xs flex items-center justify-center p-4 font-sans text-ink-900 dark:text-paper-50">
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[28px] p-6 sm:p-8 max-w-md w-full shadow-ticket dark:shadow-ticket-dark space-y-6 animate-fadeIn">
            <div className="text-center space-y-2">
              <div className="w-14 h-14 rounded-full bg-terracotta-500/10 text-terracotta-500 flex items-center justify-center mx-auto border border-terracotta-500/20">
                <AlertTriangle className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold font-cinzel text-ink-900 dark:text-paper-50">
                Exit Exam Session?
              </h3>
              <p className="text-xs text-ink-600 dark:text-ink-400">
                You have answered <span className="font-bold text-ink-900 dark:text-paper-50">{answeredCount}</span> of {totalQuestions} questions. If you exit now, your current answers will be discarded.
              </p>
            </div>

            <div className="flex items-center gap-3">
              <button
                onClick={() => setIsExitConfirmOpen(false)}
                className="flex-1 py-3 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 font-bold text-xs font-mono transition border border-paper-300 dark:border-darkbg-border cursor-pointer text-ink-900 dark:text-paper-100"
              >
                Resume Exam
              </button>
              <button
                onClick={onExitExam}
                className="flex-1 py-3 rounded-full bg-terracotta-500 hover:bg-terracotta-600 text-white font-semibold text-xs font-mono tracking-wider uppercase transition shadow-md cursor-pointer"
              >
                Exit Now
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 8. KEYBOARD SHORTCUTS MODAL */}
      {isShortcutsModalOpen && (
        <div className="fixed inset-0 z-50 bg-ink-900/60 dark:bg-black/80 backdrop-blur-xs flex items-center justify-center p-4 font-sans text-ink-900 dark:text-paper-50">
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[28px] p-6 sm:p-8 max-w-md w-full shadow-ticket dark:shadow-ticket-dark space-y-6 animate-fadeIn">
            <div className="flex items-center justify-between pb-3 border-b border-paper-300 dark:border-darkbg-border">
              <div className="flex items-center gap-2">
                <Keyboard className="w-5 h-5 text-ink-900 dark:text-paper-50" />
                <h3 className="font-bold text-base">
                  Keyboard Shortcuts
                </h3>
              </div>
              <button
                onClick={() => setIsShortcutsModalOpen(false)}
                className="p-1.5 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 text-ink-600 dark:text-paper-300 cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-3 font-mono text-xs">
              <div className="flex items-center justify-between py-1.5 border-b border-paper-200 dark:border-darkbg-800">
                <span className="text-ink-600 dark:text-ink-400">Select Option</span>
                <span className="px-2 py-1 rounded bg-paper-200 dark:bg-darkbg-800 font-bold border border-paper-300 dark:border-darkbg-border">A / B / C / D or 1-4</span>
              </div>
              <div className="flex items-center justify-between py-1.5 border-b border-paper-200 dark:border-darkbg-800">
                <span className="text-ink-600 dark:text-ink-400">Save & Next</span>
                <span className="px-2 py-1 rounded bg-paper-200 dark:bg-darkbg-800 font-bold border border-paper-300 dark:border-darkbg-border">→ (Right Arrow) or Enter</span>
              </div>
              <div className="flex items-center justify-between py-1.5 border-b border-paper-200 dark:border-darkbg-800">
                <span className="text-ink-600 dark:text-ink-400">Previous Question</span>
                <span className="px-2 py-1 rounded bg-paper-200 dark:bg-darkbg-800 font-bold border border-paper-300 dark:border-darkbg-border">← (Left Arrow)</span>
              </div>
              <div className="flex items-center justify-between py-1.5 border-b border-paper-200 dark:border-darkbg-800">
                <span className="text-ink-600 dark:text-ink-400">Flag / Review Later</span>
                <span className="px-2 py-1 rounded bg-paper-200 dark:bg-darkbg-800 font-bold border border-paper-300 dark:border-darkbg-border">F or M</span>
              </div>
              <div className="flex items-center justify-between py-1.5 border-b border-paper-200 dark:border-darkbg-800">
                <span className="text-ink-600 dark:text-ink-400">Clear Answer</span>
                <span className="px-2 py-1 rounded bg-paper-200 dark:bg-darkbg-800 font-bold border border-paper-300 dark:border-darkbg-border">Backspace or X</span>
              </div>
              <div className="flex items-center justify-between py-1.5 border-b border-paper-200 dark:border-darkbg-800">
                <span className="text-ink-600 dark:text-ink-400">Open Progress Matrix</span>
                <span className="px-2 py-1 rounded bg-paper-200 dark:bg-darkbg-800 font-bold border border-paper-300 dark:border-darkbg-border">G or P</span>
              </div>
              <div className="flex items-center justify-between py-1.5">
                <span className="text-ink-600 dark:text-ink-400">Close Any Modal</span>
                <span className="px-2 py-1 rounded bg-paper-200 dark:bg-darkbg-800 font-bold border border-paper-300 dark:border-darkbg-border">Esc</span>
              </div>
            </div>

            <button
              onClick={() => setIsShortcutsModalOpen(false)}
              className="w-full py-3 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 font-semibold text-xs font-mono uppercase tracking-wider shadow-md cursor-pointer"
            >
              Got It
            </button>
          </div>
        </div>
      )}

      {/* 9. SUBMISSION CONFIRMATION MODAL */}
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
