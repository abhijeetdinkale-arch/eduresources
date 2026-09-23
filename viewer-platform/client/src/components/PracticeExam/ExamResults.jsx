import React, { useState, useEffect } from 'react';
import {
  Award,
  CheckCircle2,
  XCircle,
  HelpCircle,
  Clock,
  RotateCcw,
  ArrowRight,
  ChevronLeft,
  ChevronRight,
  TrendingUp,
  Sparkles,
  BookOpen,
  Filter,
  Check,
  AlertCircle
} from 'lucide-react';
import MathText from '../MathText';

export default function ExamResults({ result, onRetakeExam, onBackToHub }) {
  const { test, userAnswers, timeSpentSeconds } = result;

  // Calculate scores
  let correctCount = 0;
  let wrongCount = 0;
  let unattemptedCount = 0;

  test.questions.forEach((q) => {
    const userChoice = userAnswers[q.id];
    if (userChoice === undefined) {
      unattemptedCount += 1;
    } else if (userChoice === q.correctIndex) {
      correctCount += 1;
    } else {
      wrongCount += 1;
    }
  });

  const totalScore = Math.max(0, correctCount * test.marksPerQuestion - wrongCount * test.negativeMarks);
  const accuracy = correctCount + wrongCount > 0 ? Math.round((correctCount / (correctCount + wrongCount)) * 100) : 0;

  // Save result to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(
        `edunet_exam_result_${test.id}`,
        JSON.stringify({
          testId: test.id,
          totalScore,
          accuracy,
          correctCount,
          wrongCount,
          unattemptedCount,
          completedAt: new Date().toISOString(),
        })
      );
    } catch {}
  }, [test.id, totalScore, accuracy, correctCount, wrongCount, unattemptedCount]);

  // Review mode filter: 'wrong' | 'unattempted' | 'correct' | 'all'
  const [filterMode, setFilterMode] = useState(() => (wrongCount > 0 ? 'wrong' : 'all'));
  const [reviewIdx, setReviewIdx] = useState(0);
  const [animDirection, setAnimDirection] = useState('next');

  // Filter questions list
  const filteredQuestions = test.questions.filter((q) => {
    const userChoice = userAnswers[q.id];
    if (filterMode === 'wrong') return userChoice !== undefined && userChoice !== q.correctIndex;
    if (filterMode === 'unattempted') return userChoice === undefined;
    if (filterMode === 'correct') return userChoice === q.correctIndex;
    return true; // 'all'
  });

  // Keep index in bound when filter changes
  useEffect(() => {
    setReviewIdx(0);
  }, [filterMode]);

  const currentQ = filteredQuestions[reviewIdx] || test.questions[0];
  const userChoice = currentQ ? userAnswers[currentQ.id] : undefined;
  const isCorrect = userChoice === currentQ?.correctIndex;
  const isWrong = userChoice !== undefined && !isCorrect;
  const isSkipped = userChoice === undefined;

  const handleNextSolution = () => {
    if (reviewIdx < filteredQuestions.length - 1) {
      setAnimDirection('next');
      setReviewIdx((prev) => prev + 1);
    }
  };

  const handlePrevSolution = () => {
    if (reviewIdx > 0) {
      setAnimDirection('prev');
      setReviewIdx((prev) => prev - 1);
    }
  };

  // Format time
  const formatTimeSpent = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}m ${s < 10 ? '0' : ''}${s}s`;
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12 space-y-10 font-sans animate-fadeIn">
      {/* 1. SCORECARD HERO CARD (Quizzax style) */}
      <div className="relative rounded-3xl p-6 sm:p-10 bg-gradient-to-br from-slate-900 via-zinc-900 to-black border border-paper-300/20 shadow-2xl text-white overflow-hidden">
        <div className="absolute right-0 top-0 w-72 h-72 rounded-full bg-amber-500/10 blur-3xl pointer-events-none"></div>

        <div className="relative z-10 space-y-6">
          {/* Header Tag */}
          <div className="flex items-center justify-between">
            <span className="text-xs font-mono font-bold px-3 py-1 rounded-full bg-white/10 text-amber-300 border border-white/10">
              MOCK EXAMINATION RESULT
            </span>
            <span className="text-xs font-mono text-zinc-400">
              Time: {formatTimeSpent(timeSpentSeconds)}
            </span>
          </div>

          {/* Big Score Display */}
          <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-4 pb-4 border-b border-white/10">
            <div>
              <div className="text-4xl sm:text-6xl font-cinzel font-black tracking-tight text-white flex items-baseline gap-2">
                <span>{totalScore.toFixed(2)}</span>
                <span className="text-xl sm:text-2xl font-mono text-zinc-400 font-normal">
                  / {test.maxMarks}.00
                </span>
              </div>
              <p className="text-xs font-mono text-amber-300 mt-1">
                Marking Scheme: +1.00 Correct • -0.25 Wrong Deducted
              </p>
            </div>

            <div className="flex items-center gap-4 text-left sm:text-right">
              <div>
                <div className="text-2xl sm:text-3xl font-bold font-mono text-emerald-400">
                  {accuracy}%
                </div>
                <div className="text-[11px] font-mono text-zinc-400 uppercase">
                  Accuracy
                </div>
              </div>
            </div>
          </div>

          {/* Stat Pills Grid */}
          <div className="grid grid-cols-3 gap-3 text-center">
            <div className="p-3.5 rounded-2xl bg-emerald-500/15 border border-emerald-500/30">
              <div className="flex items-center justify-center gap-1.5 text-emerald-400 text-xs font-mono font-semibold">
                <CheckCircle2 className="w-4 h-4" />
                <span>Correct</span>
              </div>
              <div className="text-xl font-bold font-mono text-emerald-300 mt-1">
                {correctCount}
              </div>
              <div className="text-[10px] font-mono text-emerald-400/80">
                +{correctCount * 1} Marks
              </div>
            </div>

            <div className="p-3.5 rounded-2xl bg-rose-500/15 border border-rose-500/30">
              <div className="flex items-center justify-center gap-1.5 text-rose-400 text-xs font-mono font-semibold">
                <XCircle className="w-4 h-4" />
                <span>Wrong</span>
              </div>
              <div className="text-xl font-bold font-mono text-rose-300 mt-1">
                {wrongCount}
              </div>
              <div className="text-[10px] font-mono text-rose-400/80">
                -{(wrongCount * 0.25).toFixed(2)} Marks
              </div>
            </div>

            <div className="p-3.5 rounded-2xl bg-zinc-800/60 border border-zinc-700/60">
              <div className="flex items-center justify-center gap-1.5 text-zinc-400 text-xs font-mono font-semibold">
                <HelpCircle className="w-4 h-4" />
                <span>Skipped</span>
              </div>
              <div className="text-xl font-bold font-mono text-zinc-300 mt-1">
                {unattemptedCount}
              </div>
              <div className="text-[10px] font-mono text-zinc-500">
                0.00 Marks
              </div>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="flex items-center gap-3 pt-2">
            <button
              onClick={onRetakeExam}
              className="flex-1 py-3 px-4 rounded-2xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs font-mono transition flex items-center justify-center gap-2 cursor-pointer"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Retake Mock Exam</span>
            </button>
            <button
              onClick={onBackToHub}
              className="flex-1 py-3 px-4 rounded-2xl bg-amber-400 hover:bg-amber-300 text-ink-950 font-bold text-xs font-mono transition flex items-center justify-center gap-2 cursor-pointer shadow-md"
            >
              <span>Practice Exams Hub</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* 2. ONE-BY-ONE SMOOTH ANIMATED SOLUTION WALKTHROUGH */}
      <div className="space-y-5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 className="text-xl font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-amber-500" />
              <span>Step-by-Step Solution Walkthrough</span>
            </h2>
            <p className="text-xs text-ink-500 dark:text-ink-400 mt-0.5">
              Review answers one by one with animated steps, formulas, and derivations.
            </p>
          </div>

          {/* Filter Tabs */}
          <div className="flex items-center gap-1.5 bg-paper-200 dark:bg-darkbg-800 p-1 rounded-2xl border border-paper-300 dark:border-darkbg-border self-start">
            <button
              onClick={() => setFilterMode('wrong')}
              className={`px-3 py-1 rounded-xl text-xs font-mono transition cursor-pointer ${
                filterMode === 'wrong'
                  ? 'bg-rose-500 text-white font-bold shadow-xs'
                  : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
              }`}
            >
              Wrong ({wrongCount})
            </button>
            <button
              onClick={() => setFilterMode('unattempted')}
              className={`px-3 py-1 rounded-xl text-xs font-mono transition cursor-pointer ${
                filterMode === 'unattempted'
                  ? 'bg-zinc-700 text-white font-bold shadow-xs'
                  : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
              }`}
            >
              Skipped ({unattemptedCount})
            </button>
            <button
              onClick={() => setFilterMode('correct')}
              className={`px-3 py-1 rounded-xl text-xs font-mono transition cursor-pointer ${
                filterMode === 'correct'
                  ? 'bg-emerald-600 text-white font-bold shadow-xs'
                  : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
              }`}
            >
              Correct ({correctCount})
            </button>
            <button
              onClick={() => setFilterMode('all')}
              className={`px-3 py-1 rounded-xl text-xs font-mono transition cursor-pointer ${
                filterMode === 'all'
                  ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 font-bold shadow-xs'
                  : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
              }`}
            >
              All ({test.questions.length})
            </button>
          </div>
        </div>

        {/* 3. CURRENT QUESTION CARD WITH SMOOTH TRANSITION */}
        {filteredQuestions.length === 0 ? (
          <div className="p-12 text-center rounded-3xl bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border space-y-2">
            <CheckCircle2 className="w-8 h-8 text-emerald-500 mx-auto" />
            <p className="font-bold text-sm text-ink-900 dark:text-paper-100">
              No questions found in this filter category!
            </p>
            <p className="text-xs text-ink-500">
              Select another filter tab above to continue reviewing.
            </p>
          </div>
        ) : (
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-3xl p-6 sm:p-8 shadow-ticket dark:shadow-ticket-dark space-y-6 transition-all duration-300 animate-fadeIn">
            {/* Top Review Header */}
            <div className="flex items-center justify-between border-b border-paper-200 dark:border-darkbg-border pb-4">
              <div className="flex items-center gap-2">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-lg bg-paper-200 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200">
                  Question {reviewIdx + 1} of {filteredQuestions.length}
                </span>

                {/* Status Badge */}
                {isCorrect && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold px-2.5 py-1 rounded-lg bg-emerald-500/15 text-emerald-700 dark:text-emerald-400 border border-emerald-500/20">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>Correct (+1.00)</span>
                  </span>
                )}
                {isWrong && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold px-2.5 py-1 rounded-lg bg-rose-500/15 text-rose-700 dark:text-rose-400 border border-rose-500/20">
                    <XCircle className="w-3.5 h-3.5" />
                    <span>Incorrect (-0.25)</span>
                  </span>
                )}
                {isSkipped && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold px-2.5 py-1 rounded-lg bg-zinc-500/15 text-zinc-600 dark:text-zinc-400 border border-zinc-500/20">
                    <HelpCircle className="w-3.5 h-3.5" />
                    <span>Skipped (0.00)</span>
                  </span>
                )}
              </div>

              {/* Prev / Next Walkthrough Buttons */}
              <div className="flex items-center gap-1">
                <button
                  onClick={handlePrevSolution}
                  disabled={reviewIdx === 0}
                  className="p-1.5 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 disabled:opacity-25 transition text-ink-800 dark:text-paper-200 cursor-pointer disabled:cursor-not-allowed"
                  title="Previous Solution"
                >
                  <ChevronLeft className="w-5 h-5" />
                </button>
                <button
                  onClick={handleNextSolution}
                  disabled={reviewIdx === filteredQuestions.length - 1}
                  className="p-1.5 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 disabled:opacity-25 transition text-ink-800 dark:text-paper-200 cursor-pointer disabled:cursor-not-allowed"
                  title="Next Solution"
                >
                  <ChevronRight className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Question Text */}
            <div className="space-y-2">
              <div className="text-xs font-mono text-amber-600 dark:text-amber-400 font-bold">
                Q.{currentQ.id} • {currentQ.topic}
              </div>
              <div className="text-base sm:text-lg font-medium text-ink-900 dark:text-paper-50 leading-relaxed">
                <MathText text={currentQ.question} />
              </div>
            </div>

            {/* Options with Visual Correct/Wrong Markers */}
            <div className="grid grid-cols-1 gap-2.5 pt-2">
              {currentQ.options.map((opt, optIdx) => {
                const isCorrectOption = optIdx === currentQ.correctIndex;
                const isUserSelection = userChoice === optIdx;
                const optionLetters = ['A', 'B', 'C', 'D'];

                let style = 'bg-paper-100/60 dark:bg-darkbg-800/60 border-paper-200 dark:border-darkbg-border text-ink-700 dark:text-paper-300';
                if (isCorrectOption) {
                  style = 'bg-emerald-500/15 border-emerald-500/60 text-emerald-950 dark:text-emerald-100 font-semibold ring-1 ring-emerald-500/30';
                } else if (isUserSelection && !isCorrectOption) {
                  style = 'bg-rose-500/15 border-rose-500/60 text-rose-950 dark:text-rose-100 font-semibold';
                }

                return (
                  <div
                    key={optIdx}
                    className={`p-3.5 rounded-2xl border flex items-center justify-between text-xs sm:text-sm ${style}`}
                  >
                    <div className="flex items-center gap-3">
                      <div
                        className={`w-6 h-6 rounded-full flex items-center justify-center font-mono text-xs font-bold ${
                          isCorrectOption
                            ? 'bg-emerald-600 text-white'
                            : isUserSelection
                            ? 'bg-rose-600 text-white'
                            : 'bg-paper-200 dark:bg-darkbg-700 text-ink-600 dark:text-paper-400'
                        }`}
                      >
                        {optionLetters[optIdx]}
                      </div>
                      <MathText text={opt} />
                    </div>

                    <div className="flex items-center gap-2 shrink-0">
                      {isUserSelection && !isCorrectOption && (
                        <span className="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-rose-500 text-white">
                          Your Choice (Wrong)
                        </span>
                      )}
                      {isCorrectOption && (
                        <span className="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-600 text-white flex items-center gap-1">
                          <Check className="w-3 h-3" />
                          <span>Correct Answer</span>
                        </span>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* 4. BASIC EXPLANATION (Step-by-step Structured Breakdown) */}
            {currentQ.explanation && (
              <div className="p-5 rounded-2xl bg-paper-200/70 dark:bg-darkbg-800/70 border border-paper-300 dark:border-darkbg-border space-y-3 mt-4">
                <div className="flex items-center gap-2 text-ink-900 dark:text-paper-50 font-bold text-xs sm:text-sm font-mono">
                  <Sparkles className="w-4 h-4 text-amber-500" />
                  <span>Basic Step-by-Step Explanation:</span>
                </div>

                <div className="space-y-2 text-xs sm:text-sm text-ink-800 dark:text-paper-200 leading-relaxed font-sans">
                  {currentQ.explanation.steps?.map((step, sIdx) => (
                    <div key={sIdx} className="flex items-start gap-2">
                      <span className="font-mono text-amber-600 dark:text-amber-400 font-bold shrink-0">
                        Step {sIdx + 1}:
                      </span>
                      <MathText text={step} />
                    </div>
                  ))}
                </div>

                {currentQ.explanation.keyConcept && (
                  <div className="pt-2 border-t border-paper-300/80 dark:border-darkbg-border/80 flex items-start gap-2 text-xs font-mono text-amber-700 dark:text-amber-300 bg-amber-500/10 p-2.5 rounded-xl border border-amber-500/20">
                    <span className="font-bold shrink-0">💡 Key Concept:</span>
                    <span>{currentQ.explanation.keyConcept}</span>
                  </div>
                )}
              </div>
            )}

            {/* Bottom Walkthrough Controls */}
            <div className="flex items-center justify-between pt-2">
              <button
                onClick={handlePrevSolution}
                disabled={reviewIdx === 0}
                className="px-4 py-2 rounded-xl bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-25 text-xs font-mono font-semibold transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Previous Question</span>
              </button>

              <button
                onClick={handleNextSolution}
                disabled={reviewIdx === filteredQuestions.length - 1}
                className="px-4 py-2 rounded-xl bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 disabled:opacity-25 text-paper-50 dark:text-ink-900 text-xs font-mono font-semibold transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed"
              >
                <span>Next Question</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
