import React, { useState, useEffect } from 'react';

export default function LogoSplash({ onComplete }) {
  const [stage, setStage] = useState('enter'); // 'enter' -> 'float' -> 'exit'

  useEffect(() => {
    // Stage 1: Float in air & expand from small to big
    const t1 = setTimeout(() => {
      setStage('float');
    }, 100);

    // Stage 2: Fade out cleanly
    const t2 = setTimeout(() => {
      setStage('exit');
    }, 1050);

    // Stage 3: Unmount
    const t3 = setTimeout(() => {
      if (onComplete) onComplete();
    }, 1300);

    const handleSkip = () => {
      setStage('exit');
      setTimeout(() => {
        if (onComplete) onComplete();
      }, 150);
    };

    window.addEventListener('keydown', handleSkip);

    return () => {
      clearTimeout(t1);
      clearTimeout(t2);
      clearTimeout(t3);
      window.removeEventListener('keydown', handleSkip);
    };
  }, [onComplete]);

  const handleDismiss = () => {
    setStage('exit');
    setTimeout(() => {
      if (onComplete) onComplete();
    }, 150);
  };

  return (
    <div
      onClick={handleDismiss}
      className={`fixed inset-0 z-[100] flex flex-col items-center justify-center cursor-pointer select-none transition-opacity duration-300 ${
        stage === 'exit' ? 'opacity-0 pointer-events-none' : 'opacity-100'
      } bg-[#09090B] text-[#F5F2EB]`}
    >
      {/* Minimalist Floating Logo (Small to Big in the Air) */}
      <div className="flex flex-col items-center">
        {/* Floating Star Circle */}
        <div
          className={`w-24 h-24 sm:w-28 sm:h-28 rounded-full bg-paper-50 flex items-center justify-center p-3 shadow-2xl transition-all duration-700 ease-out ${
            stage === 'enter'
              ? 'scale-0 opacity-0 translate-y-8'
              : 'scale-100 opacity-100 -translate-y-2'
          }`}
          style={{
            boxShadow: '0 20px 40px -10px rgba(0,0,0,0.5), 0 0 30px rgba(229,192,91,0.25)',
          }}
        >
          <img
            src="/logo.png"
            alt="Edu network star"
            className="w-full h-full object-contain filter invert-0"
          />
        </div>

        {/* Minimalist Brand Title */}
        <div
          className={`mt-6 text-center transition-all duration-500 delay-200 ${
            stage === 'enter'
              ? 'opacity-0 translate-y-3'
              : 'opacity-100 translate-y-0'
          }`}
        >
          <h1 className="text-2xl sm:text-3xl font-cinzel font-bold tracking-wide text-paper-50">
            Edu<span className="font-serif italic font-normal text-ink-400"> network</span>
          </h1>
          <p className="text-[10px] font-mono tracking-widest text-ink-500 uppercase mt-1">
            ARCHIVE 2026
          </p>
        </div>
      </div>
    </div>
  );
}
