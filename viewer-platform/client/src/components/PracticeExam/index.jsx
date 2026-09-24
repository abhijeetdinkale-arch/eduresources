import React, { useState } from 'react';
import ExamHub from './ExamHub';
import ExamPrepCountdown from './ExamPrepCountdown';
import ExamScreen from './ExamScreen';
import ExamResults from './ExamResults';
import MecDraftingExam from './MecDraftingExam';

export default function PracticeExamContainer({ onBackToCatalog, onRequireLogin, user }) {
  // view: 'hub' | 'prep' | 'exam' | 'results'
  const [examView, setExamView] = useState('hub');
  const [activeTest, setActiveTest] = useState(null);
  const [lastResult, setLastResult] = useState(null);

  const handleStartExam = (test) => {
    setActiveTest(test);
    setExamView('prep'); // Show 3-second animated prep countdown first
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleCountdownComplete = () => {
    setExamView('exam');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleFinishExam = (result) => {
    setLastResult(result);
    setExamView('results');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleRetakeExam = () => {
    if (activeTest) {
      setExamView('prep');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      setExamView('hub');
    }
  };

  const handleBackToHub = () => {
    setActiveTest(null);
    setExamView('hub');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  if (examView === 'prep' && activeTest) {
    return (
      <ExamPrepCountdown
        test={activeTest}
        onCountdownComplete={handleCountdownComplete}
        onCancel={handleBackToHub}
      />
    );
  }

  if (examView === 'exam' && activeTest) {
    // Check if test is a non-MCQ drafting / graphics exam (e.g. MEC136)
    if (activeTest.isDraftingExam) {
      return (
        <MecDraftingExam
          test={activeTest}
          onExitExam={handleBackToHub}
        />
      );
    }

    return (
      <ExamScreen
        test={activeTest}
        onFinishExam={handleFinishExam}
        onExitExam={handleBackToHub}
      />
    );
  }

  if (examView === 'results' && lastResult) {
    return (
      <ExamResults
        result={lastResult}
        onRetakeExam={handleRetakeExam}
        onBackToHub={handleBackToHub}
      />
    );
  }

  return (
    <ExamHub
      onStartExam={handleStartExam}
      onBackToCatalog={onBackToCatalog}
    />
  );
}
