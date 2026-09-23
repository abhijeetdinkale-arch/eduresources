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
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12 space-y-10 font-sans animate-fadeIn text-black dark:text-white">
      {/* 1. SCORECARD HERO CARD (BLACK & WHITE) */}
      <div className="relative rounded-[32px] p-6 sm:p-10 bg-black text-white border-2 border-zinc-800 dark:border-white/20 shadow-2xl overflow-hidden">
        <div className="relative z-10 space-y-6">
          {/* Header Tag */}
          <div className="flex items-center justify-between">
            <span className="text-xs font-mono font-bold px-3 py-1 rounded-full bg-white/10 border border-white/20 uppercase tracking-wider">
              MOCK EXAMINATION SCORECARD
            </span>
            <span className="text-xs font-mono text-zinc-400">
              Time: {formatTimeSpent(timeSpentSeconds)}
            </span>
          </div>

          {/* Big Score Display */}
          <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-4 pb-4 border-b border-white/20">
            <div>
              <div className="text-4xl sm:text-6xl font-cinzel font-black tracking-tight text-white flex items-baseline gap-2">
                <span>{totalScore.toFixed(2)}</span>
                <span className="text-xl sm:text-2xl font-mono text-zinc-400 font-normal">
                  / {test.maxMarks}.00
                </span>
              </div>
              <p className="text-xs font-mono text-zinc-300 mt-1">
                Marking Scheme: +1.00 Correct • -0.25 Wrong Deducted
              </p>
            </div>

            <div className="text-left sm:text-right">
              <div className="text-3xl sm:text-4xl font-bold font-mono text-white">
                {accuracy}%
              </div>
              <div className="text-[11px] font-mono text-zinc-400 uppercase tracking-widest">
                Accuracy Rate
              </div>
            </div>
          </div>

          {/* Stat Pills Grid in Black & White */}
          <div className="grid grid-cols-3 gap-3 text-center font-mono">
            <div className="p-3.5 rounded-2xl bg-white/10 border border-white/20">
              <div className="text-xs font-bold uppercase text-zinc-200">Correct</div>
              <div className="text-2xl font-black text-white mt-1">{correctCount}</div>
              <div className="text-[10px] text-zinc-400">+{correctCount * 1} Marks</div>
            </div>

            <div className="p-3.5 rounded-2xl bg-white/10 border border-white/20">
              <div className="text-xs font-bold uppercase text-zinc-200">Wrong</div>
              <div className="text-2xl font-black text-white mt-1">{wrongCount}</div>
              <div className="text-[10px] text-zinc-400">-{(wrongCount * 0.25).toFixed(2)} Marks</div>
            </div>

            <div className="p-3.5 rounded-2xl bg-white/5 border border-white/10">
              <div className="text-xs font-bold uppercase text-zinc-400">Skipped</div>
              <div className="text-2xl font-black text-zinc-300 mt-1">{unattemptedCount}</div>
              <div className="text-[10px] text-zinc-500">0.00 Marks</div>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="flex items-center gap-3 pt-2">
            <button
              onClick={onRetakeExam}
              className="flex-1 py-3 px-4 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs font-mono transition flex items-center justify-center gap-2 cursor-pointer border border-white/20"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Retake Mock Exam</span>
            </button>
            <button
              onClick={onBackToHub}
              className="flex-1 py-3 px-4 rounded-xl bg-white hover:bg-zinc-200 text-black font-extrabold text-xs font-mono tracking-wider uppercase transition flex items-center justify-center gap-2 cursor-pointer shadow-md"
            >
              <span>Practice Exams Hub</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* 2. ONE-BY-ONE STEP-BY-STEP ANIMATED SOLUTIONS (BLACK & WHITE) */}
      <div className="space-y-5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 className="text-xl font-bold font-sans tracking-tight flex items-center gap-2">
              <Sparkles className="w-5 h-5" />
              <span>Step-by-Step Solution Walkthrough</span>
            </h2>
            <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-0.5">
              Review answers one by one with animated steps, formulas, and derivations.
            </p>
          </div>

          {/* Filter Tabs in Black & White */}
          <div className="flex items-center gap-1 bg-zinc-100 dark:bg-zinc-900 p-1 rounded-2xl border-2 border-black/10 dark:border-white/10 self-start">
            <button
              onClick={() => setFilterMode('wrong')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'wrong'
                  ? 'bg-black text-white dark:bg-white dark:text-black shadow-xs'
                  : 'text-zinc-600 dark:text-zinc-400 hover:text-black dark:hover:text-white'
              }`}
            >
              Wrong ({wrongCount})
            </button>
            <button
              onClick={() => setFilterMode('unattempted')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'unattempted'
                  ? 'bg-black text-white dark:bg-white dark:text-black shadow-xs'
                  : 'text-zinc-600 dark:text-zinc-400 hover:text-black dark:hover:text-white'
              }`}
            >
              Skipped ({unattemptedCount})
            </button>
            <button
              onClick={() => setFilterMode('correct')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'correct'
                  ? 'bg-black text-white dark:bg-white dark:text-black shadow-xs'
                  : 'text-zinc-600 dark:text-zinc-400 hover:text-black dark:hover:text-white'
              }`}
            >
              Correct ({correctCount})
            </button>
            <button
              onClick={() => setFilterMode('all')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'all'
                  ? 'bg-black text-white dark:bg-white dark:text-black shadow-xs'
                  : 'text-zinc-600 dark:text-zinc-400 hover:text-black dark:hover:text-white'
              }`}
            >
              All ({test.questions.length})
            </button>
          </div>
        </div>

        {/* 3. QUESTION REVIEW CARD */}
        {filteredQuestions.length === 0 ? (
          <div className="p-12 text-center rounded-[28px] bg-zinc-50 dark:bg-zinc-950 border-2 border-black/10 dark:border-white/10 space-y-2">
            <Check className="w-8 h-8 mx-auto" />
            <p className="font-bold text-sm">
              No questions found in this filter category!
            </p>
            <p className="text-xs text-zinc-500">
              Select another filter tab above to continue reviewing.
            </p>
          </div>
        ) : (
          <div className="bg-white dark:bg-zinc-950 border-2 border-black dark:border-white/20 rounded-[28px] p-6 sm:p-8 shadow-ticket dark:shadow-ticket-dark space-y-6 transition-all duration-300 animate-fadeIn">
            {/* Top Review Header */}
            <div className="flex items-center justify-between border-b-2 border-black/10 dark:border-white/10 pb-4">
              <div className="flex items-center gap-2">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-lg bg-zinc-100 dark:bg-zinc-900">
                  Question {reviewIdx + 1} of {filteredQuestions.length}
                </span>

                {isCorrect && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-black px-2.5 py-1 rounded-lg bg-black text-white dark:bg-white dark:text-black">
                    <Check className="w-3.5 h-3.5 stroke-[3]" />
                    <span>Correct (+1.00)</span>
                  </span>
                )}
                {isWrong && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-black px-2.5 py-1 rounded-lg border-2 border-black dark:border-white">
                    <X className="w-3.5 h-3.5 stroke-[3]" />
                    <span>Incorrect (-0.25)</span>
                  </span>
                )}
                {isSkipped && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold px-2.5 py-1 rounded-lg bg-zinc-200 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-200">
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
                  className="p-1.5 rounded-full hover:bg-zinc-100 dark:hover:bg-zinc-900 disabled:opacity-20 transition cursor-pointer disabled:cursor-not-allowed"
                  title="Previous Solution"
                >
                  <ChevronLeft className="w-5 h-5" />
                </button>
                <button
                  onClick={handleNextSolution}
                  disabled={reviewIdx === filteredQuestions.length - 1}
                  className="p-1.5 rounded-full hover:bg-zinc-100 dark:hover:bg-zinc-900 disabled:opacity-20 transition cursor-pointer disabled:cursor-not-allowed"
                  title="Next Solution"
                >
                  <ChevronRight className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Question Text */}
            <div className="space-y-2">
              <div className="text-xs font-mono font-bold text-zinc-500 uppercase tracking-widest">
                Q.{currentQ.id} • {currentQ.topic}
              </div>
              <div className="text-base sm:text-lg font-bold leading-relaxed">
                <MathText text={currentQ.question} />
              </div>
            </div>

            {/* Options with Crisp Monochrome Visual Markers */}
            <div className="grid grid-cols-1 gap-2.5 pt-2">
              {currentQ.options.map((opt, optIdx) => {
                const isCorrectOption = optIdx === currentQ.correctIndex;
                const isUserSelection = userChoice === optIdx;
                const optionLetters = ['A', 'B', 'C', 'D'];

                let style = 'bg-zinc-50 dark:bg-zinc-900/60 border-zinc-200 dark:border-zinc-800 text-zinc-800 dark:text-zinc-200';
                if (isCorrectOption) {
                  style = 'bg-black text-white dark:bg-white dark:text-black border-black dark:border-white font-bold shadow-md';
                } else if (isUserSelection && !isCorrectOption) {
                  style = 'border-2 border-dashed border-black dark:border-white text-black dark:text-white font-bold';
                }

                return (
                  <div
                    key={optIdx}
                    className={`p-3.5 rounded-2xl border-2 flex items-center justify-between text-xs sm:text-sm ${style}`}
                  >
                    <div className="flex items-center gap-3">
                      <div
                        className={`w-6 h-6 rounded-full flex items-center justify-center font-mono text-xs font-bold ${
                          isCorrectOption
                            ? 'bg-white text-black dark:bg-black dark:text-white'
                            : isUserSelection
                            ? 'bg-black text-white dark:bg-white dark:text-black'
                            : 'bg-zinc-200 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300'
                        }`}
                      >
                        {optionLetters[optIdx]}
                      </div>
                      <MathText text={opt} />
                    </div>

                    <div className="flex items-center gap-2 shrink-0">
                      {isUserSelection && !isCorrectOption && (
                        <span className="text-[10px] font-mono font-black px-2 py-0.5 rounded border border-black dark:border-white">
                          Your Choice (Wrong)
                        </span>
                      )}
                      {isCorrectOption && (
                        <span className="text-[10px] font-mono font-black px-2 py-0.5 rounded bg-white text-black dark:bg-black dark:text-white flex items-center gap-1">
                          <Check className="w-3 h-3 stroke-[3]" />
                          <span>Correct Answer</span>
                        </span>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* 4. BASIC EXPLANATION IN BLACK & WHITE */}
            {currentQ.explanation && (
              <div className="p-5 rounded-2xl bg-zinc-100 dark:bg-zinc-900 border-2 border-black/10 dark:border-white/10 space-y-3 mt-4">
                <div className="flex items-center gap-2 font-mono font-black text-xs sm:text-sm uppercase tracking-wider">
                  <Sparkles className="w-4 h-4" />
                  <span>Step-by-Step Explanation:</span>
                </div>

                <div className="space-y-2 text-xs sm:text-sm leading-relaxed font-sans">
                  {currentQ.explanation.steps?.map((step, sIdx) => (
                    <div key={sIdx} className="flex items-start gap-2">
                      <span className="font-mono font-black shrink-0">
                        Step {sIdx + 1}:
                      </span>
                      <MathText text={step} />
                    </div>
                  ))}
                </div>

                {currentQ.explanation.keyConcept && (
                  <div className="pt-2 border-t border-black/10 dark:border-white/10 flex items-start gap-2 text-xs font-mono bg-white dark:bg-black p-3 rounded-xl border border-black/20 dark:border-white/20">
                    <span className="font-black shrink-0">💡 Note:</span>
                    <span>{currentQ.explanation.keyConcept}</span>
                  </div>
                )}
              </div>
            )}

            {/* Bottom Controls */}
            <div className="flex items-center justify-between pt-2">
              <button
                onClick={handlePrevSolution}
                disabled={reviewIdx === 0}
                className="px-4 py-2 rounded-xl bg-zinc-100 dark:bg-zinc-900 hover:bg-zinc-200 dark:hover:bg-zinc-800 disabled:opacity-25 text-xs font-mono font-bold transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed border border-black/20 dark:border-white/20"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Previous</span>
              </button>

              <button
                onClick={handleNextSolution}
                disabled={reviewIdx === filteredQuestions.length - 1}
                className="px-5 py-2 rounded-xl bg-black dark:bg-white hover:bg-zinc-800 dark:hover:bg-zinc-200 text-white dark:text-black disabled:opacity-25 text-xs font-mono font-black uppercase tracking-wider transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed shadow-md"
              >
                <span>Next</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
