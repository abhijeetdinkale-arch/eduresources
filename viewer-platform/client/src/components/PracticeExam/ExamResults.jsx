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
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12 space-y-10 font-sans animate-fadeIn text-[#0A1128] bg-white">
      {/* 1. SCORECARD HERO CARD IN DARK NAVY BLUE */}
      <div className="relative rounded-[32px] p-6 sm:p-10 bg-[#0A1128] text-white border-2 border-[#0A1128] shadow-2xl overflow-hidden">
        <div className="relative z-10 space-y-6">
          {/* Header Tag */}
          <div className="flex items-center justify-between">
            <span className="text-xs font-mono font-bold px-3 py-1 rounded-full bg-white/10 border border-white/20 uppercase tracking-wider">
              MOCK EXAMINATION SCORECARD
            </span>
            <span className="text-xs font-mono text-slate-300">
              Time: {formatTimeSpent(timeSpentSeconds)}
            </span>
          </div>

          {/* Big Score Display */}
          <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-4 pb-4 border-b border-white/20">
            <div>
              <div className="text-4xl sm:text-6xl font-cinzel font-black tracking-tight text-white flex items-baseline gap-2">
                <span>{totalScore.toFixed(2)}</span>
                <span className="text-xl sm:text-2xl font-mono text-slate-300 font-normal">
                  / {test.maxMarks}.00
                </span>
              </div>
              <p className="text-xs font-mono text-slate-200 mt-1">
                Marking Scheme: +1.00 Correct • -0.25 Wrong Deducted
              </p>
            </div>

            <div className="text-left sm:text-right">
              <div className="text-3xl sm:text-4xl font-bold font-mono text-white">
                {accuracy}%
              </div>
              <div className="text-[11px] font-mono text-slate-300 uppercase tracking-widest">
                Accuracy Rate
              </div>
            </div>
          </div>

          {/* Stat Pills Grid */}
          <div className="grid grid-cols-3 gap-3 text-center font-mono">
            <div className="p-3.5 rounded-2xl bg-white/10 border border-white/20">
              <div className="text-xs font-bold uppercase text-slate-200">Correct</div>
              <div className="text-2xl font-black text-white mt-1">{correctCount}</div>
              <div className="text-[10px] text-slate-300">+{correctCount * 1} Marks</div>
            </div>

            <div className="p-3.5 rounded-2xl bg-white/10 border border-white/20">
              <div className="text-xs font-bold uppercase text-slate-200">Wrong</div>
              <div className="text-2xl font-black text-white mt-1">{wrongCount}</div>
              <div className="text-[10px] text-slate-300">-{(wrongCount * 0.25).toFixed(2)} Marks</div>
            </div>

            <div className="p-3.5 rounded-2xl bg-white/5 border border-white/10">
              <div className="text-xs font-bold uppercase text-slate-300">Skipped</div>
              <div className="text-2xl font-black text-slate-300 mt-1">{unattemptedCount}</div>
              <div className="text-[10px] text-slate-400">0.00 Marks</div>
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
              className="flex-1 py-3 px-4 rounded-xl bg-white hover:bg-slate-100 text-[#0A1128] font-extrabold text-xs font-mono tracking-wider uppercase transition flex items-center justify-center gap-2 cursor-pointer shadow-md"
            >
              <span>Practice Exams Hub</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* 2. ONE-BY-ONE STEP-BY-STEP ANIMATED SOLUTIONS (WHITE & DARK NAVY BLUE) */}
      <div className="space-y-5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 className="text-xl font-black font-sans tracking-tight text-[#0A1128] flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-[#0A1128]" />
              <span>Step-by-Step Solution Walkthrough</span>
            </h2>
            <p className="text-xs text-[#0A1128]/70 mt-0.5">
              Review answers one by one with animated steps, formulas, and derivations.
            </p>
          </div>

          {/* Filter Tabs in White & Navy */}
          <div className="flex items-center gap-1 bg-[#0A1128]/5 p-1 rounded-2xl border-2 border-[#0A1128]/15 self-start">
            <button
              onClick={() => setFilterMode('wrong')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'wrong'
                  ? 'bg-[#0A1128] text-white shadow-xs'
                  : 'text-[#0A1128]/70 hover:text-[#0A1128]'
              }`}
            >
              Wrong ({wrongCount})
            </button>
            <button
              onClick={() => setFilterMode('unattempted')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'unattempted'
                  ? 'bg-[#0A1128] text-white shadow-xs'
                  : 'text-[#0A1128]/70 hover:text-[#0A1128]'
              }`}
            >
              Skipped ({unattemptedCount})
            </button>
            <button
              onClick={() => setFilterMode('correct')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'correct'
                  ? 'bg-[#0A1128] text-white shadow-xs'
                  : 'text-[#0A1128]/70 hover:text-[#0A1128]'
              }`}
            >
              Correct ({correctCount})
            </button>
            <button
              onClick={() => setFilterMode('all')}
              className={`px-3 py-1 rounded-xl text-xs font-mono font-bold transition cursor-pointer ${
                filterMode === 'all'
                  ? 'bg-[#0A1128] text-white shadow-xs'
                  : 'text-[#0A1128]/70 hover:text-[#0A1128]'
              }`}
            >
              All ({test.questions.length})
            </button>
          </div>
        </div>

        {/* 3. QUESTION REVIEW CARD */}
        {filteredQuestions.length === 0 ? (
          <div className="p-12 text-center rounded-[28px] bg-[#0A1128]/5 border-2 border-[#0A1128]/15 space-y-2 text-[#0A1128]">
            <Check className="w-8 h-8 mx-auto" />
            <p className="font-bold text-sm">
              No questions found in this filter category!
            </p>
            <p className="text-xs text-[#0A1128]/60">
              Select another filter tab above to continue reviewing.
            </p>
          </div>
        ) : (
          <div className="bg-white border-2 border-[#0A1128]/20 rounded-[28px] p-6 sm:p-8 shadow-lg space-y-6 transition-all duration-300 animate-fadeIn text-[#0A1128]">
            {/* Top Review Header */}
            <div className="flex items-center justify-between border-b-2 border-[#0A1128]/15 pb-4">
              <div className="flex items-center gap-2">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-lg bg-[#0A1128]/5 text-[#0A1128]">
                  Question {reviewIdx + 1} of {filteredQuestions.length}
                </span>

                {isCorrect && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-black px-2.5 py-1 rounded-lg bg-[#0A1128] text-white">
                    <Check className="w-3.5 h-3.5 stroke-[3]" />
                    <span>Correct (+1.00)</span>
                  </span>
                )}
                {isWrong && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-black px-2.5 py-1 rounded-lg border-2 border-[#0A1128] text-[#0A1128]">
                    <X className="w-3.5 h-3.5 stroke-[3]" />
                    <span>Incorrect (-0.25)</span>
                  </span>
                )}
                {isSkipped && (
                  <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold px-2.5 py-1 rounded-lg bg-[#0A1128]/10 text-[#0A1128]">
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
                  className="p-1.5 rounded-full hover:bg-[#0A1128]/10 disabled:opacity-20 transition cursor-pointer disabled:cursor-not-allowed text-[#0A1128]"
                  title="Previous Solution"
                >
                  <ChevronLeft className="w-5 h-5" />
                </button>
                <button
                  onClick={handleNextSolution}
                  disabled={reviewIdx === filteredQuestions.length - 1}
                  className="p-1.5 rounded-full hover:bg-[#0A1128]/10 disabled:opacity-20 transition cursor-pointer disabled:cursor-not-allowed text-[#0A1128]"
                  title="Next Solution"
                >
                  <ChevronRight className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Question Text */}
            <div className="space-y-2">
              <div className="text-xs font-mono font-bold text-[#0A1128]/70 uppercase tracking-widest">
                Q.{currentQ.id} • {currentQ.topic}
              </div>
              <div className="text-base sm:text-lg font-bold leading-relaxed text-[#0A1128]">
                <MathText text={currentQ.question} />
              </div>
            </div>

            {/* Options with Crisp Markers */}
            <div className="grid grid-cols-1 gap-2.5 pt-2">
              {currentQ.options.map((opt, optIdx) => {
                const isCorrectOption = optIdx === currentQ.correctIndex;
                const isUserSelection = userChoice === optIdx;
                const optionLetters = ['A', 'B', 'C', 'D'];

                let style = 'bg-white border-[#0A1128]/20 text-[#0A1128]';
                if (isCorrectOption) {
                  style = 'bg-[#0A1128] text-white border-[#0A1128] font-bold shadow-md';
                } else if (isUserSelection && !isCorrectOption) {
                  style = 'border-2 border-dashed border-[#0A1128] text-[#0A1128] font-bold bg-[#0A1128]/5';
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
                            ? 'bg-white text-[#0A1128]'
                            : isUserSelection
                            ? 'bg-[#0A1128] text-white'
                            : 'bg-[#0A1128]/10 text-[#0A1128]'
                        }`}
                      >
                        {optionLetters[optIdx]}
                      </div>
                      <MathText text={opt} />
                    </div>

                    <div className="flex items-center gap-2 shrink-0">
                      {isUserSelection && !isCorrectOption && (
                        <span className="text-[10px] font-mono font-black px-2 py-0.5 rounded border border-[#0A1128] text-[#0A1128]">
                          Your Choice (Wrong)
                        </span>
                      )}
                      {isCorrectOption && (
                        <span className="text-[10px] font-mono font-black px-2 py-0.5 rounded bg-white text-[#0A1128] flex items-center gap-1">
                          <Check className="w-3 h-3 stroke-[3]" />
                          <span>Correct Answer</span>
                        </span>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* 4. BASIC EXPLANATION IN WHITE & DARK NAVY BLUE */}
            {currentQ.explanation && (
              <div className="p-5 rounded-2xl bg-[#0A1128]/5 border-2 border-[#0A1128]/15 space-y-3 mt-4 text-[#0A1128]">
                <div className="flex items-center gap-2 font-mono font-black text-xs sm:text-sm uppercase tracking-wider text-[#0A1128]">
                  <Sparkles className="w-4 h-4" />
                  <span>Step-by-Step Explanation:</span>
                </div>

                <div className="space-y-2 text-xs sm:text-sm leading-relaxed font-sans text-[#0A1128]">
                  {currentQ.explanation.steps?.map((step, sIdx) => (
                    <div key={sIdx} className="flex items-start gap-2">
                      <span className="font-mono font-black shrink-0 text-[#0A1128]">
                        Step {sIdx + 1}:
                      </span>
                      <MathText text={step} />
                    </div>
                  ))}
                </div>

                {currentQ.explanation.keyConcept && (
                  <div className="pt-2 border-t border-[#0A1128]/15 flex items-start gap-2 text-xs font-mono bg-white p-3 rounded-xl border border-[#0A1128]/20 text-[#0A1128]">
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
                className="px-4 py-2 rounded-xl bg-[#0A1128]/5 hover:bg-[#0A1128]/10 disabled:opacity-25 text-xs font-mono font-bold transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed border border-[#0A1128]/20 text-[#0A1128]"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Previous</span>
              </button>

              <button
                onClick={handleNextSolution}
                disabled={reviewIdx === filteredQuestions.length - 1}
                className="px-5 py-2 rounded-xl bg-[#0A1128] hover:bg-[#14214d] text-white disabled:opacity-25 text-xs font-mono font-black uppercase tracking-wider transition flex items-center gap-1 cursor-pointer disabled:cursor-not-allowed shadow-md"
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
