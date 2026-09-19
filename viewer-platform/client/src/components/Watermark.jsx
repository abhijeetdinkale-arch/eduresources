import React, { useEffect, useState } from 'react';

export default function Watermark({ user }) {
  const [timestamp, setTimestamp] = useState(new Date().toLocaleString());
  const [floatPos, setFloatPos] = useState({ top: '15%', left: '20%' });

  useEffect(() => {
    const timer = setInterval(() => {
      setTimestamp(new Date().toLocaleString());
    }, 1000);

    const driftInterval = setInterval(() => {
      const top = Math.floor(10 + Math.random() * 70) + '%';
      const left = Math.floor(10 + Math.random() * 70) + '%';
      setFloatPos({ top, left });
    }, 6000);

    return () => {
      clearInterval(timer);
      clearInterval(driftInterval);
    };
  }, []);

  const watermarkText = `EDU NETWORK • ${user?.email || 'student@university.edu'} • UID: ${user?.id || 'AUTH-SECURE'} • IP: ${user?.ip || '127.0.0.1'} • ${timestamp}`;

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden select-none z-20">
      {/* 1. Tiled Archival Forensic Watermark Grid */}
      <div className="absolute -inset-[100%] w-[300%] h-[300%] flex flex-wrap content-start justify-start opacity-12 rotate-[-26deg] select-none pointer-events-none">
        {Array.from({ length: 90 }).map((_, i) => (
          <div
            key={i}
            className="p-10 font-mono text-[10px] font-bold tracking-widest text-[#18181B] whitespace-nowrap select-none"
          >
            ✦ {watermarkText}
          </div>
        ))}
      </div>

      {/* 2. Floating Archival Seal Badge */}
      <div
        className="absolute transition-all duration-1000 ease-in-out bg-ink-900/90 text-paper-50 border border-paper-300/40 text-[9px] px-3 py-1 rounded-full font-mono shadow-md backdrop-blur-xs select-none pointer-events-none flex items-center gap-1.5"
        style={{ top: floatPos.top, left: floatPos.left }}
      >
        <span className="w-1.5 h-1.5 rounded-full bg-ochre-400 animate-pulse"></span>
        <span>EDU NETWORK ARCHIVES • {user?.email}</span>
      </div>
    </div>
  );
}
