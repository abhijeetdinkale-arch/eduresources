import React, { useState, useEffect } from 'react';
import {
  Award,
  CheckCircle2,
  XCircle,
  HelpCircle,
  RotateCcw,
  ArrowRight,
  ChevronLeft,
  ChevronRight,
  Sparkles,
  Check,
  X
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

  // Filter questions list
  const filteredQuestions = test.questions.filter((q) => {
    const userChoice = userAnswers[q.id];
    if (filterMode === 'wrong') return userChoice !== undefined && userChoice !== q.correctIndex;
    if (filterMode === 'unattempted') return userChoice === undefined;
    if (filterMode === 'correct') return userChoice === q.correctIndex;
    return true; // 'all'
  });

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
      setReviewIdx((prev) => prev + 1);
    }
  };

  const handlePrevSolution = () => {
    if (reviewIdx > 0) {
      setReviewIdx((prev) => prev - 1);
    }
  };

  const formatTimeSpent = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}m ${s < 10 ? '0' : ''}${s}s`;
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12 space-y-10 font-sans animate-fadeIn text-ink-900 dark:text-paper-50">
      {/* 1. SCORECARD HERO CARD */}
      <div className="relative rounded-[32px] p-6 sm:p-10 bg-paper-50 dark:bg-darkbg-900 text-ink-900 dark:text-paper-50 border border-paper-300 dark:border-darkbg-border shadow-ticket dark:shadow-ticket-dark overflow-hidden">
        <div className="relative z-10 space-y-6">
          {/* Header Tag */}
          <div className="flex items-center justify-between">
            <span className="text-xs font-mono font-bold px-3.5 py-1 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border uppercase tracking-wider text-ink-800 dark:text-paper-200">
              MOCK EXAMINATION SCORECARD
            </span>
            <span className="text-xs font-mono text-ink-600 dark:text-ink-400 font-semibold">
              Time Taken: {formatTimeSpent(timeSpentSeconds)}
            </span>
          </div>

          {/* Big Score Display */}
          <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-4 pb-4 border-b border-paper-300 dark:border-darkbg-border">
            <div>
              <div className="text-4xl sm:text-6xl font-cinzel font-black tracking-tight text-ink-900 dark:text-paper-50 flex items-baseline gap-2">
                <span>{totalScore.toFixed(2)}</span>
                <span className="text-xl sm:text-2xl font-mono text-ink-600 dark:text-ink-400 font-normal">
                  / {test.maxMarks}.00
                </span>
              </div>
              <p className="text-xs font-mono text-ink-600 dark:text-ink-400 mt-1">
                Marking Scheme: +1.00 Correct • -0.25 Wrong Deducted
              </p>
            </div>

            <div className="text-left sm:text-right">
              <div className="text-3xl sm:text-4xl font-bold font-mono text-ink-900 dark:text-paper-50">
                {accuracy}%
              </div>
              <div className="text-[11px] font-mono text-ink-600 dark:text-ink-400 uppercase tracking-widest font-semibold">
                Accuracy Rate
              </div>
            </div>
          </div>

          {/* Stat Pills Grid */}
          <div className="grid grid-cols-3 gap-3 text-center font-mono">
            <div className="p-3.5 rounded-2xl bg-paper-100 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border">
              <div className="text-xs font-bold uppercase text-ink-600 dark:text-ink-400">Correct</div>
              <div className="text-2xl font-black text-emerald-600 dark:text-emerald-400 mt-1">{correctCount}</div>
              <div className="text-[10px] text-ink-600 dark:text-ink-400">+{correctCount * 1} Marks</div>
            </div>

            <div className="p-3.5 rounded-2xl bg-paper-100 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border">
              <div className="text-xs font-bold uppercase text-ink-600 dark:text-ink-400">Wrong</div>
              <div className="text-2xl font-black text-terracotta-500 mt-1">{wrongCount}</div>
              <div className="text-[10px] text-ink-600 dark:text-ink-400">-{(wrongCount * 0.25).toFixed(2)} Marks</div>
            </div>

            <div className="p-3.5 rounded-2xl bg-paper-100 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border">
              <div className="text-xs font-bold uppercase text-ink-600 dark:text-ink-400">Skipped</div>
              <div className="text-2xl font-black text-ink-600 dark:text-ink-400 mt-1">{unattemptedCount}</div>
              <div className="text-[10px] text-ink-600 dark:text-ink-400">0.00 Marks</div>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="flex items-center gap-3 pt-2">
            <button
              onClick={onRetakeExam}
              className="flex-1 py-3 px-4 rounded-full bg-paper-200 hover:bg-paper-300 dark:bg-darkbg-800 dark:hover:bg-darkbg-700 text-ink-900 dark:text-paper-100 font-bold text-xs font-mono transition flex items-center justify-center gap-2 cursor-pointer border border-paper-300 dark:border-darkbg-border"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Retake Mock Exam</span>
            </button>
            <button
              onClick={onBackToHub}
              className="flex-1 py-3 px-4 rounded-full bg-ink-900 hover:bg-black dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 font-semibold text-xs tracking-wider uppercase transition flex items-center justify-center gap-2 cursor-pointer shadow-md"
            >
              <span>Practice Exams Hub</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* 2. ONE-BY-ONE STEP-BY-STEP ANIMATED SOLUTIONS */}
      <div className="space-y-5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 className="text-xl font-bold font-cinzel tracking-tight text-ink-900 dark:text-paper-50 flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-ochre-400" />
              <span>Step-by-Step Solution Walkthrough</span>
            </h2>
            <p className="text-xs text-ink-600 dark:text-ink-400 mt-0.5">
              Review answers one by one with animated steps, formulas, and derivations.
            </p>
          </div>

          {/* Filter Tabs */}
          <div className="flex items-center gap-1 bg-paper-200 dark:bg-darkbg-800 p-1 rounded-full border border-paper-300 dark:border-darkbg-border self-start">
            <button
              onClick={() => setFilterMode('wrong')}
              className={`px-3.5 py-1 rounded-full text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'wrong'
                  ? 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 shadow-xs'
                  : 'text-ink-600 hover:text-ink-900 dark:text-ink-400 dark:hover:text-paper-50'
              }`}
            >
              Wrong ({wrongCount})
            </button>
            <button
              onClick={() => setFilterMode('unattempted')}
              className={`px-3.5 py-1 rounded-full text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'unattempted'
                  ? 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 shadow-xs'
                  : 'text-ink-600 hover:text-ink-900 dark:text-ink-400 dark:hover:text-paper-50'
              }`}
            >
              Skipped ({unattemptedCount})
            </button>
            <button
              onClick={() => setFilterMode('correct')}
              className={`px-3.5 py-1 rounded-full text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'correct'
                  ? 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 shadow-xs'
                  : 'text-ink-600 hover:text-ink-900 dark:text-ink-400 dark:hover:text-paper-50'
              }`}
            >
              Correct ({correctCount})
            </button>
            <button
              onClick={() => setFilterMode('all')}
              className={`px-3.5 py-1 rounded-full text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'all'
                  ? 'bg-ink-900 text-paper-50 dark:bg-paper-50 dark:text-ink-900 shadow-xs'
                  : 'text-ink-600 hover:text-ink-900 dark:text-ink-400 dark:hover:text-paper-50'
              }`}
            >
              All ({test.questions.length})
            </button>
          </div>
        </div>

        {/* 3. QUESTION REVIEW CARD */}
        {filteredQuestions.length === 0 ? (
          <div className="p-12 text-center rounded-[28px] bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border space-y-2 text-ink-900 dark:text-paper-50 shadow-ticket">
            <Check className="w-8 h-8 mx-auto text-emerald-600 dark:text-emerald-400" />
            <p className="font-bold text-sm">
              No questions found in this filter category!
            </p>
            <button
              onClick={() => setFilterMode('all')}
              className="mt-2 text-xs font-mono text-ink-600 dark:text-ink-400 underline cursor-pointer"
            >
              View all 30 questions
            </button>
          </div>
        ) : (
          <div className="bg-paper-50 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-[28px] p-6 sm:p-8 shadow-ticket space-y-6 text-ink-900 dark:text-paper-50">
            {/* Top Navigation between solutions */}
            <div className="flex items-center justify-between pb-4 border-b border-paper-300 dark:border-darkbg-border">
              <div className="flex items-center gap-2">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-lg bg-paper-200 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 border border-paper-300 dark:border-darkbg-border">
                  Question {currentQ.id}
                </span>
                <span className="text-xs font-mono text-ink-600 dark:text-ink-400">
                  ({reviewIdx + 1} of {filteredQuestions.length})
                </span>
                {isCorrect && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>+1.00 Correct</span>
                  </span>
                )}
                {isWrong && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold text-terracotta-600 dark:text-terracotta-500 bg-terracotta-500/10 px-2 py-0.5 rounded-full">
                    <XCircle className="w-3.5 h-3.5" />
                    <span>-0.25 Deducted</span>
                  </span>
                )}
                {isSkipped && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold text-ink-600 dark:text-ink-400 bg-paper-200 dark:bg-darkbg-800 px-2 py-0.5 rounded-full">
                    <HelpCircle className="w-3.5 h-3.5" />
                    <span>Unattempted</span>
                  </span>
                )}
              </div>

              {/* Prev / Next solution arrows */}
              <div className="flex items-center gap-2">
                <button
                  onClick={handlePrevSolution}
                  disabled={reviewIdx === 0}
                  className="p-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-900 dark:text-paper-100 transition cursor-pointer disabled:cursor-not-allowed border border-paper-300 dark:border-darkbg-border"
                >
                  <ChevronLeft className="w-4 h-4" />
                </button>
                <button
                  onClick={handleNextSolution}
                  disabled={reviewIdx === filteredQuestions.length - 1}
                  className="p-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-900 dark:text-paper-100 transition cursor-pointer disabled:cursor-not-allowed border border-paper-300 dark:border-darkbg-border"
                >
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Question Text */}
            <div className="text-base sm:text-lg font-bold text-ink-900 dark:text-paper-50 leading-relaxed font-sans">
              <MathText text={currentQ.question} />
            </div>

            {/* Option Choices with Correct / Selected markers */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {currentQ.options.map((opt, optIdx) => {
                const isSelectedByUser = userChoice === optIdx;
                const isThisTheCorrectAnswer = optIdx === currentQ.correctIndex;
                const optionLetters = ['A', 'B', 'C', 'D'];

                let cardStyle = 'border-paper-300 dark:border-darkbg-border bg-paper-100 dark:bg-darkbg-800 text-ink-800 dark:text-paper-200';

                if (isThisTheCorrectAnswer) {
                  cardStyle = 'border-emerald-500 bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 font-bold';
                } else if (isSelectedByUser && !isThisTheCorrectAnswer) {
                  cardStyle = 'border-terracotta-500 bg-terracotta-500/10 text-terracotta-700 dark:text-terracotta-400 font-bold';
                }

                return (
                  <div
                    key={optIdx}
                    className={`p-3.5 rounded-xl border-2 flex items-center justify-between text-xs sm:text-sm ${cardStyle}`}
                  >
                    <div className="flex items-center gap-2.5">
                      <span className="w-6 h-6 rounded-full bg-paper-200 dark:bg-darkbg-700 text-ink-900 dark:text-paper-100 flex items-center justify-center font-mono font-bold text-[11px] shrink-0 border border-paper-300 dark:border-darkbg-border">
                        {optionLetters[optIdx]}
                      </span>
                      <MathText text={opt} />
                    </div>

                    <div>
                      {isThisTheCorrectAnswer && (
                        <span className="px-2 py-0.5 rounded-full bg-emerald-600 text-white font-mono text-[10px] font-bold">
                          CORRECT
                        </span>
                      )}
                      {isSelectedByUser && !isThisTheCorrectAnswer && (
                        <span className="px-2 py-0.5 rounded-full bg-terracotta-500 text-white font-mono text-[10px] font-bold">
                          YOUR ANSWER
                        </span>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Step-by-Step Animated Breakdown */}
            {currentQ.explanation && (
              <div className="space-y-4 pt-2">
                <div className="flex items-center gap-2 text-xs font-mono font-bold text-ink-900 dark:text-paper-50 uppercase tracking-wider">
                  <Sparkles className="w-4 h-4 text-ochre-400" />
                  <span>Step-by-Step Derivation</span>
                </div>

                <div className="space-y-2.5">
                  {currentQ.explanation.steps.map((step, sIdx) => (
                    <div
                      key={sIdx}
                      className="p-3.5 rounded-xl bg-paper-100 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-xs sm:text-sm text-ink-800 dark:text-paper-200 leading-relaxed font-sans"
                    >
                      <div className="font-mono text-[11px] font-bold text-ink-600 dark:text-ink-400 mb-1">
                        STEP {sIdx + 1}
                      </div>
                      <MathText text={step} />
                    </div>
                  ))}
                </div>

                {/* Key Concept Box */}
                {currentQ.explanation.keyConcept && (
                  <div className="p-4 rounded-xl bg-ochre-400/15 border border-ochre-400/30 text-ink-900 dark:text-paper-50 text-xs sm:text-sm leading-relaxed">
                    <span className="font-mono font-bold text-xs uppercase text-ink-900 dark:text-ochre-400 block mb-1">
                      💡 Key Examination Concept
                    </span>
                    <MathText text={currentQ.explanation.keyConcept} />
                  </div>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
