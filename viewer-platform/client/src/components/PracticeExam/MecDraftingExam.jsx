import React, { useState, useRef, useEffect } from 'react';
import {
  Ruler,
  Compass,
  Layers,
  Eye,
  CheckCircle2,
  Clock,
  ArrowLeft,
  Download,
  RotateCcw,
  Sparkles,
  Info,
  Maximize2,
  PenTool,
  Eraser,
  HelpCircle,
  FileText,
  ChevronRight,
  Award
} from 'lucide-react';

export default function MecDraftingExam({ test, onExitExam }) {
  const [activeTab, setActiveTab] = useState('partB-p4'); // 'partA' | 'partB-p2' | 'partB-p3' | 'partB-p4' | 'rubric'
  const [secondsRemaining, setSecondsRemaining] = useState((test.durationMinutes || 90) * 60);
  const [showExitDialog, setShowExitDialog] = useState(false);
  const [showSolutionOverlay, setShowSolutionOverlay] = useState(false);
  const [activeViewMode, setActiveViewMode] = useState('all'); // 'all' | 'isometric' | 'front' | 'top' | 'side'
  const [currentStep, setCurrentStep] = useState(1);
  const [revealedAnswers, setRevealedAnswers] = useState({});
  const [rubricScores, setRubricScores] = useState({});

  // Canvas drawing state
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [drawTool, setDrawTool] = useState('pen'); // 'pen' | 'eraser'
  const [showGrid, setShowGrid] = useState(true);

  // Timer countdown
  useEffect(() => {
    const timer = setInterval(() => {
      setSecondsRemaining((prev) => (prev > 0 ? prev - 1 : 0));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // Toggle Part A question solution
  const toggleAnswer = (qId) => {
    setRevealedAnswers((prev) => ({ ...prev, [qId]: !prev[qId] }));
  };

  // Canvas handling
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    // Clear and draw grid
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (showGrid) {
      ctx.strokeStyle = '#E2E8F0';
      ctx.lineWidth = 0.5;
      const gridSize = 20;
      for (let x = 0; x < canvas.width; x += gridSize) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
      }
      for (let y = 0; y < canvas.height; y += gridSize) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
      }
    }
  }, [showGrid, activeTab]);

  const startDrawing = (e) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
    setIsDrawing(true);
  };

  const draw = (e) => {
    if (!isDrawing) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const ctx = canvas.getContext('2d');
    ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
    ctx.strokeStyle = drawTool === 'eraser' ? '#FFFFFF' : '#1E293B';
    ctx.lineWidth = drawTool === 'eraser' ? 16 : 2;
    ctx.lineCap = 'round';
    ctx.stroke();
  };

  const stopDrawing = () => {
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (showGrid) {
      ctx.strokeStyle = '#E2E8F0';
      ctx.lineWidth = 0.5;
      const gridSize = 20;
      for (let x = 0; x < canvas.width; x += gridSize) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
      }
      for (let y = 0; y < canvas.height; y += gridSize) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
      }
    }
  };

  const totalEvaluatedScore = Object.values(rubricScores).reduce((a, b) => a + b, 0);

  return (
    <div className="min-h-screen bg-[#F8F6F0] dark:bg-[#0F1117] text-ink-900 dark:text-paper-50 font-sans pb-16">
      {/* 1. TOP DRAFTING STUDIO HEADER */}
      <header className="sticky top-0 z-40 bg-paper-50/95 dark:bg-[#181822]/95 backdrop-blur-md border-b border-paper-300 dark:border-darkbg-border shadow-xs">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex items-center justify-between">
          {/* Left: Back & Exam Title */}
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowExitDialog(true)}
              className="p-2 rounded-full hover:bg-paper-200 dark:hover:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-700 dark:text-paper-200 transition-colors"
              title="Exit Drafting Exam"
            >
              <ArrowLeft className="w-5 h-5" />
            </button>

            <div>
              <div className="flex items-center gap-2">
                <span className="px-2 py-0.5 rounded-md bg-paper-200 dark:bg-darkbg-800 text-[10px] font-mono font-bold tracking-wider text-ink-700 dark:text-paper-200 uppercase">
                  {test.code}
                </span>
                <span className="hidden sm:inline-block text-xs font-semibold text-ochre-600 dark:text-ochre-400">
                  Engineering Graphics Studio (Subjective)
                </span>
              </div>
              <h1 className="text-sm sm:text-base font-bold text-ink-900 dark:text-paper-50 tracking-tight font-sans">
                {test.courseName} • Midterm Exam
              </h1>
            </div>
          </div>

          {/* Right: Timer & Scorecard */}
          <div className="flex items-center gap-3">
            {/* Timer Capsule */}
            <div className={`flex items-center gap-2 px-3.5 py-1.5 rounded-full border font-mono text-xs font-bold ${
              secondsRemaining < 300
                ? 'bg-red-500/10 border-red-500 text-red-600 animate-pulse'
                : 'bg-paper-100 dark:bg-darkbg-900 border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200'
            }`}>
              <Clock className="w-4 h-4 text-ochre-500" />
              <span>{formatTime(secondsRemaining)}</span>
            </div>

            {/* Score Tracker */}
            <div className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-xs font-mono font-bold">
              <Award className="w-3.5 h-3.5 text-ochre-500" />
              <span>{totalEvaluatedScore} / 40 M</span>
            </div>

            {/* Finish Review Button */}
            <button
              onClick={() => setActiveTab('rubric')}
              className="px-4 py-1.5 rounded-full bg-ink-900 hover:bg-ink-800 dark:bg-paper-50 dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs font-bold tracking-wide transition-all shadow-xs"
            >
              Self-Assess Rubric
            </button>
          </div>
        </div>

        {/* Navigation Tabs Bar */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center gap-1 overflow-x-auto py-1 scrollbar-none border-t border-paper-200 dark:border-darkbg-border text-xs font-semibold">
          <button
            onClick={() => setActiveTab('partB-p4')}
            className={`px-3.5 py-2 rounded-lg transition-all whitespace-nowrap flex items-center gap-1.5 ${
              activeTab === 'partB-p4'
                ? 'bg-paper-300/80 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 font-bold border-b-2 border-ochre-500'
                : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
            }`}
          >
            <Compass className="w-3.5 h-3.5 text-ochre-500" />
            <span>Problem 4: 3D Orthographic Views (10M)</span>
          </button>

          <button
            onClick={() => setActiveTab('partB-p2')}
            className={`px-3.5 py-2 rounded-lg transition-all whitespace-nowrap flex items-center gap-1.5 ${
              activeTab === 'partB-p2'
                ? 'bg-paper-300/80 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 font-bold border-b-2 border-ochre-500'
                : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
            }`}
          >
            <Ruler className="w-3.5 h-3.5 text-blue-500" />
            <span>Problem 2: Diagonal Scale (10M)</span>
          </button>

          <button
            onClick={() => setActiveTab('partB-p3')}
            className={`px-3.5 py-2 rounded-lg transition-all whitespace-nowrap flex items-center gap-1.5 ${
              activeTab === 'partB-p3'
                ? 'bg-paper-300/80 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 font-bold border-b-2 border-ochre-500'
                : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
            }`}
          >
            <PenTool className="w-3.5 h-3.5 text-emerald-500" />
            <span>Problem 3: Line Projections & Traces (10M)</span>
          </button>

          <button
            onClick={() => setActiveTab('partA')}
            className={`px-3.5 py-2 rounded-lg transition-all whitespace-nowrap flex items-center gap-1.5 ${
              activeTab === 'partA'
                ? 'bg-paper-300/80 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 font-bold border-b-2 border-ochre-500'
                : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
            }`}
          >
            <FileText className="w-3.5 h-3.5 text-purple-500" />
            <span>Part-A: 5 Technical Concepts (10M)</span>
          </button>

          <button
            onClick={() => setActiveTab('rubric')}
            className={`px-3.5 py-2 rounded-lg transition-all whitespace-nowrap flex items-center gap-1.5 ${
              activeTab === 'rubric'
                ? 'bg-paper-300/80 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 font-bold border-b-2 border-ochre-500'
                : 'text-ink-600 dark:text-ink-400 hover:text-ink-900'
            }`}
          >
            <Award className="w-3.5 h-3.5 text-amber-500" />
            <span>Marking Scheme & Rubric</span>
          </button>
        </div>
      </header>

      {/* 2. MAIN WORKSPACE */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
        {/* =========================================================================
            TAB 1: PROBLEM 4 - 3D ISOMETRIC TO ORTHOGRAPHIC MULTI-VIEW
            ========================================================================= */}
        {activeTab === 'partB-p4' && (
          <div className="space-y-6">
            {/* Problem Statement Card */}
            <div className="bg-white dark:bg-[#181822] rounded-3xl p-6 border border-paper-300 dark:border-darkbg-border shadow-sm space-y-4">
              <div className="flex items-center justify-between">
                <span className="px-3 py-1 rounded-full bg-ochre-100 dark:bg-ochre-900/30 text-ochre-800 dark:text-ochre-300 text-xs font-mono font-bold">
                  PART-B • QUESTION 4 [10 MARKS]
                </span>
                <span className="text-xs text-ink-600 dark:text-ink-400 font-mono">
                  First Angle Projection System
                </span>
              </div>

              <h2 className="text-lg sm:text-xl font-bold text-ink-900 dark:text-paper-50 leading-snug">
                Orthographic Multi-View Drafting from 3D Isometric View
              </h2>

              <p className="text-sm text-ink-700 dark:text-paper-200 leading-relaxed">
                Given the 3D isometric component shown below (Base: <span className="font-mono font-bold">60 mm × 35 mm</span>, step height: <span className="font-mono font-bold">10 mm</span>, elevated right block: <span className="font-mono font-bold">35 mm × 35 mm × 35 mm</span>, total height: <span className="font-mono font-bold">45 mm</span>).
                Draw the following orthographic views in First Angle Projection:
                <br />
                <span className="font-bold">1. Front View (Elevation)</span> looking in the direction of Arrow X.
                <br />
                <span className="font-bold">2. Top View (Plan)</span> looking directly from above.
                <br />
                <span className="font-bold">3. Left Side View (Profile)</span> projected to the right of the Front View.
              </p>

              {/* View Switcher Controls */}
              <div className="flex flex-wrap items-center gap-2 pt-2">
                <span className="text-xs font-bold text-ink-600 dark:text-ink-400 mr-2">Display View:</span>
                {[
                  { id: 'all', label: 'All 3 Views (First Angle Blueprint)' },
                  { id: 'isometric', label: '3D Isometric Model' },
                  { id: 'front', label: 'Front View (Elevation)' },
                  { id: 'top', label: 'Top View (Plan)' },
                  { id: 'side', label: 'Side View' },
                ].map((v) => (
                  <button
                    key={v.id}
                    onClick={() => setActiveViewMode(v.id)}
                    className={`px-3 py-1.5 rounded-full text-xs font-bold transition-all ${
                      activeViewMode === v.id
                        ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 shadow-xs'
                        : 'bg-paper-200 dark:bg-darkbg-800 text-ink-700 dark:text-paper-200 hover:bg-paper-300'
                    }`}
                  >
                    {v.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Blueprint Visualization Studio */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
              {/* Left Column: Interactive Blueprint Render */}
              <div className="lg:col-span-7 bg-white dark:bg-[#181822] rounded-3xl p-6 border border-paper-300 dark:border-darkbg-border shadow-sm flex flex-col items-center justify-center min-h-[420px]">
                <div className="w-full flex items-center justify-between mb-4">
                  <span className="text-xs font-mono font-bold text-ink-500 uppercase tracking-widest flex items-center gap-1.5">
                    <Compass className="w-4 h-4 text-ochre-500" />
                    CAD Specification Blueprint
                  </span>
                  <button
                    onClick={() => setShowSolutionOverlay(!showSolutionOverlay)}
                    className="text-xs font-bold text-ochre-600 dark:text-ochre-400 hover:underline flex items-center gap-1"
                  >
                    <Eye className="w-3.5 h-3.5" />
                    <span>{showSolutionOverlay ? 'Hide Construction Lines' : 'Show Construction Lines'}</span>
                  </button>
                </div>

                {/* SVG High-Precision Blueprint Render */}
                <div className="w-full max-w-lg aspect-4/3 flex items-center justify-center bg-[#FBF9F5] dark:bg-[#12131C] rounded-2xl p-4 border border-dashed border-paper-300 dark:border-darkbg-border overflow-hidden">
                  <svg viewBox="0 0 500 400" className="w-full h-full drop-shadow-md">
                    {/* Definitions */}
                    <defs>
                      <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 0 L 10 5 L 0 10 z" fill="#EA580C" />
                      </marker>
                      <pattern id="hatch" width="10" height="10" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
                        <line x1="0" y1="0" x2="0" y2="10" stroke="#94A3B8" strokeWidth="1" />
                      </pattern>
                    </defs>

                    {/* Reference Line XY */}
                    <line x1="30" y1="210" x2="470" y2="210" stroke="#64748B" strokeWidth="1.5" strokeDasharray="6 3" />
                    <text x="35" y="202" fill="#64748B" fontSize="12" fontFamily="monospace" fontWeight="bold">X</text>
                    <text x="455" y="202" fill="#64748B" fontSize="12" fontFamily="monospace" fontWeight="bold">Y</text>
                    <text x="40" y="225" fill="#94A3B8" fontSize="10" fontFamily="sans-serif">VP (Front View Above XY)</text>
                    <text x="40" y="380" fill="#94A3B8" fontSize="10" fontFamily="sans-serif">HP (Top View Below XY)</text>

                    {/* FRONT VIEW (Elevation - Above XY) */}
                    {(activeViewMode === 'all' || activeViewMode === 'front') && (
                      <g className="transition-opacity duration-300">
                        {/* Base Ledge: 60mm wide, 10mm high; Right step rises to 45mm total */}
                        <path
                          d="M 120 200 L 120 180 L 170 180 L 170 110 L 240 110 L 240 200 Z"
                          fill="#E2E8F0"
                          stroke="#0F172A"
                          strokeWidth="2.5"
                          className="dark:fill-[#27273A] dark:stroke-paper-50"
                        />
                        {/* Labels */}
                        <text x="145" y="195" fill="#475569" fontSize="11" fontWeight="bold" textAnchor="middle">10 mm</text>
                        <text x="205" y="155" fill="#475569" fontSize="11" fontWeight="bold" textAnchor="middle">45 mm</text>
                        <text x="180" y="90" fill="#0F172A" fontSize="12" fontWeight="bold" textAnchor="middle" className="dark:fill-paper-50">FRONT VIEW (FV)</text>
                      </g>
                    )}

                    {/* TOP VIEW (Plan - Below XY) */}
                    {(activeViewMode === 'all' || activeViewMode === 'top') && (
                      <g className="transition-opacity duration-300">
                        {/* Outer rectangle 60mm × 35mm (scaled to 120 × 70) */}
                        <rect
                          x="120"
                          y="230"
                          width="120"
                          height="70"
                          fill="#E2E8F0"
                          stroke="#0F172A"
                          strokeWidth="2.5"
                          className="dark:fill-[#27273A] dark:stroke-paper-50"
                        />
                        {/* Step boundary line */}
                        <line x1="170" y1="230" x2="170" y2="300" stroke="#0F172A" strokeWidth="2" strokeDasharray="none" className="dark:stroke-paper-50" />
                        <text x="145" y="270" fill="#475569" fontSize="11" textAnchor="middle">25 mm</text>
                        <text x="205" y="270" fill="#475569" fontSize="11" fontWeight="bold" textAnchor="middle">35 mm</text>
                        <text x="180" y="325" fill="#0F172A" fontSize="12" fontWeight="bold" textAnchor="middle" className="dark:fill-paper-50">TOP VIEW (TV)</text>
                      </g>
                    )}

                    {/* SIDE VIEW (Profile - Left side view on Right of FV) */}
                    {(activeViewMode === 'all' || activeViewMode === 'side') && (
                      <g className="transition-opacity duration-300">
                        {/* Left view of stepped block: Width 35mm, Height 45mm, base line at 10mm */}
                        <rect
                          x="320"
                          y="110"
                          width="70"
                          height="90"
                          fill="#E2E8F0"
                          stroke="#0F172A"
                          strokeWidth="2.5"
                          className="dark:fill-[#27273A] dark:stroke-paper-50"
                        />
                        {/* Visible step level at 10mm from bottom (y=180) */}
                        <line x1="320" y1="180" x2="390" y2="180" stroke="#0F172A" strokeWidth="2" className="dark:stroke-paper-50" />
                        <text x="355" y="90" fill="#0F172A" fontSize="12" fontWeight="bold" textAnchor="middle" className="dark:fill-paper-50">LEFT SIDE VIEW</text>
                      </g>
                    )}

                    {/* Construction / Projection Lines (Toggleable) */}
                    {showSolutionOverlay && (
                      <g stroke="#EF4444" strokeWidth="1" strokeDasharray="3 3" opacity="0.75">
                        <line x1="120" y1="200" x2="120" y2="230" />
                        <line x1="170" y1="200" x2="170" y2="230" />
                        <line x1="240" y1="200" x2="240" y2="230" />
                        {/* Horizontal projectors to Side View */}
                        <line x1="240" y1="110" x2="320" y2="110" />
                        <line x1="240" y1="180" x2="320" y2="180" />
                        <line x1="240" y1="200" x2="320" y2="200" />
                      </g>
                    )}
                  </svg>
                </div>
              </div>

              {/* Right Column: Drafting Canvas & Step-by-Step Procedure */}
              <div className="lg:col-span-5 space-y-4">
                {/* Interactive Drawing Pad */}
                <div className="bg-white dark:bg-[#181822] rounded-3xl p-5 border border-paper-300 dark:border-darkbg-border shadow-sm space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold font-mono text-ink-700 dark:text-paper-200 flex items-center gap-1.5">
                      <PenTool className="w-3.5 h-3.5 text-ochre-500" />
                      Drafting Sheet Canvas
                    </span>
                    <div className="flex items-center gap-1.5">
                      <button
                        onClick={() => setDrawTool('pen')}
                        className={`p-1.5 rounded-lg border text-xs font-bold transition-all ${
                          drawTool === 'pen' ? 'bg-ink-900 text-white' : 'bg-paper-200 dark:bg-darkbg-800'
                        }`}
                        title="Pencil"
                      >
                        <PenTool className="w-3.5 h-3.5" />
                      </button>
                      <button
                        onClick={() => setDrawTool('eraser')}
                        className={`p-1.5 rounded-lg border text-xs font-bold transition-all ${
                          drawTool === 'eraser' ? 'bg-ink-900 text-white' : 'bg-paper-200 dark:bg-darkbg-800'
                        }`}
                        title="Eraser"
                      >
                        <Eraser className="w-3.5 h-3.5" />
                      </button>
                      <button
                        onClick={clearCanvas}
                        className="p-1.5 rounded-lg border bg-paper-200 dark:bg-darkbg-800 text-xs font-bold hover:bg-paper-300"
                        title="Clear Sketch"
                      >
                        <RotateCcw className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </div>

                  {/* HTML5 Canvas */}
                  <div className="border border-paper-300 dark:border-darkbg-border rounded-2xl overflow-hidden bg-white cursor-crosshair">
                    <canvas
                      ref={canvasRef}
                      width={380}
                      height={240}
                      onMouseDown={startDrawing}
                      onMouseMove={draw}
                      onMouseUp={stopDrawing}
                      onMouseLeave={stopDrawing}
                      className="w-full h-[220px]"
                    />
                  </div>
                  <p className="text-[11px] text-ink-500 font-mono">
                    Tip: Sketch your projected views or construction rays directly on the grid above.
                  </p>
                </div>

                {/* Step-by-Step Construction Guide */}
                <div className="bg-white dark:bg-[#181822] rounded-3xl p-5 border border-paper-300 dark:border-darkbg-border shadow-sm space-y-3">
                  <h3 className="text-sm font-bold text-ink-900 dark:text-paper-50 flex items-center gap-2">
                    <Info className="w-4 h-4 text-ochre-500" />
                    Step-by-Step Drafting Procedure
                  </h3>

                  <div className="space-y-2.5 text-xs text-ink-700 dark:text-paper-200">
                    <div className="p-3 rounded-xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border space-y-1">
                      <span className="font-bold text-ochre-600 dark:text-ochre-400">Step 1: Reference Line XY</span>
                      <p>Draw a horizontal reference line XY. In First Angle Projection, Elevation (FV) sits above XY, and Plan (TV) sits directly below XY.</p>
                    </div>
                    <div className="p-3 rounded-xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border space-y-1">
                      <span className="font-bold text-ochre-600 dark:text-ochre-400">Step 2: Draw Front View</span>
                      <p>Looking along Arrow X, draw the stepped contour: base length 60 mm, base height 10 mm, right elevated block 35 mm high (total 45 mm).</p>
                    </div>
                    <div className="p-3 rounded-xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border space-y-1">
                      <span className="font-bold text-ochre-600 dark:text-ochre-400">Step 3: Project Top View (TV)</span>
                      <p>Drop vertical projector lines down from FV. Draw the 60 mm × 35 mm enclosing boundary with a dividing line at 25 mm for the lower step.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* =========================================================================
            TAB 2: PROBLEM 2 - DIAGONAL SCALE CONSTRUCTION
            ========================================================================= */}
        {activeTab === 'partB-p2' && (
          <div className="bg-white dark:bg-[#181822] rounded-3xl p-6 sm:p-8 border border-paper-300 dark:border-darkbg-border shadow-sm space-y-6">
            <div className="flex items-center justify-between">
              <span className="px-3 py-1 rounded-full bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300 text-xs font-mono font-bold">
                PART-B • QUESTION 2 [10 MARKS]
              </span>
              <span className="text-xs font-mono text-ink-500">Representative Fraction = 1/50</span>
            </div>

            <div>
              <h2 className="text-lg sm:text-2xl font-bold text-ink-900 dark:text-paper-50">
                Construction of Diagonal Scale to Read 4.75 Metres
              </h2>
              <p className="text-sm text-ink-600 dark:text-ink-400 mt-1">
                "Construct a diagonal scale, having R.F. = 1/50, showing metres, decimetres and centimetres, to measure up to 5 metres. Mark a distance of 4.75 m on it."
              </p>
            </div>

            {/* Calculations Box */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div className="p-4 rounded-2xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border">
                <span className="text-[11px] font-mono text-ink-500 uppercase">1. Length of Scale (LOS)</span>
                <p className="text-base font-bold text-ink-900 dark:text-paper-50 mt-1">10 cm</p>
                <p className="text-xs text-ink-600 dark:text-ink-400 font-mono mt-0.5">LOS = (1/50) × 500 cm</p>
              </div>
              <div className="p-4 rounded-2xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border">
                <span className="text-[11px] font-mono text-ink-500 uppercase">2. Units Represented</span>
                <p className="text-base font-bold text-ink-900 dark:text-paper-50 mt-1">m, dm, cm</p>
                <p className="text-xs text-ink-600 dark:text-ink-400 font-mono mt-0.5">3 Consecutive Units</p>
              </div>
              <div className="p-4 rounded-2xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border">
                <span className="text-[11px] font-mono text-ink-500 uppercase">3. Target Measurement</span>
                <p className="text-base font-bold text-ink-900 dark:text-paper-50 mt-1">4.75 Metres</p>
                <p className="text-xs text-ink-600 dark:text-ink-400 font-mono mt-0.5">4 m + 7 dm + 5 cm</p>
              </div>
            </div>

            {/* Interactive Diagonal Scale Visualizer */}
            <div className="bg-[#FBF9F5] dark:bg-[#12131C] rounded-2xl p-6 border border-paper-300 dark:border-darkbg-border flex flex-col items-center">
              <span className="text-xs font-mono font-bold text-ink-600 dark:text-paper-300 mb-4">
                CONSTRUCTED DIAGONAL SCALE (LOS = 10 CM, RF = 1/50)
              </span>

              <svg viewBox="0 0 600 240" className="w-full max-w-2xl">
                {/* Main scale rectangle: 500px wide (represents 10 cm), 100px high (represents 5 cm) */}
                <rect x="50" y="80" width="500" height="100" fill="#FFFFFF" stroke="#0F172A" strokeWidth="2" className="dark:fill-[#1E1E2A] dark:stroke-paper-50" />

                {/* 5 Main 1-metre blocks (each 100px) */}
                {[0, 1, 2, 3, 4, 5].map((i) => (
                  <g key={i}>
                    <line x1={50 + i * 100} y1="80" x2={50 + i * 100} y2="180" stroke="#0F172A" strokeWidth={i === 1 ? 2.5 : 1.5} className="dark:stroke-paper-50" />
                    {i > 0 && (
                      <text x={50 + i * 100} y="198" fill="#475569" fontSize="12" fontWeight="bold" textAnchor="middle" className="dark:fill-paper-200">
                        {i - 1} m
                      </text>
                    )}
                  </g>
                ))}

                {/* Subdivisions of first block (left of 0, from 150 back to 50): 10 decimetre divisions (each 10px) */}
                {Array.from({ length: 11 }).map((_, d) => (
                  <line key={d} x1={150 - d * 10} y1="175" x2={150 - d * 10} y2="180" stroke="#64748B" strokeWidth="1" />
                ))}
                <text x="150" y="198" fill="#0F172A" fontSize="12" fontWeight="bold" textAnchor="middle" className="dark:fill-paper-50">0</text>
                <text x="50" y="198" fill="#475569" fontSize="11" fontWeight="bold" textAnchor="middle" className="dark:fill-paper-200">10 dm</text>

                {/* 10 Horizontal Centimetre lines (each 10px high) */}
                {Array.from({ length: 11 }).map((_, c) => (
                  <line key={c} x1="50" y1={80 + c * 10} x2="550" y2={80 + c * 10} stroke="#CBD5E1" strokeWidth="0.8" className="dark:stroke-[#333344]" />
                ))}

                {/* Diagonal lines in first block (from 150-10*d at y=180 to 150-10*(d+1) at y=80) */}
                {Array.from({ length: 10 }).map((_, d) => (
                  <line
                    key={d}
                    x1={150 - d * 10}
                    y1="180"
                    x2={150 - (d + 1) * 10}
                    y2="80"
                    stroke="#3B82F6"
                    strokeWidth="1.2"
                    strokeDasharray="none"
                  />
                ))}

                {/* Marked Distance: 4.75 m (From 4m main right mark x=450 to 7th decimetre diagonal at 5th cm line y=130, x=75) */}
                <g>
                  {/* Dimension line at y=40 */}
                  <line x1="75" y1="40" x2="450" y2="40" stroke="#DC2626" strokeWidth="2" markerEnd="url(#arrow)" markerStart="url(#arrow)" />
                  {/* Extension lines */}
                  <line x1="75" y1="35" x2="75" y2="130" stroke="#DC2626" strokeWidth="1" strokeDasharray="3 3" />
                  <line x1="450" y1="35" x2="450" y2="180" stroke="#DC2626" strokeWidth="1" strokeDasharray="3 3" />
                  {/* Intersection dot at 4.75m */}
                  <circle cx="75" cy="130" r="4" fill="#DC2626" />
                  <text x="262" y="32" fill="#DC2626" fontSize="13" fontWeight="bold" textAnchor="middle">
                    DIST = 4.75 METRES
                  </text>
                </g>
              </svg>
            </div>
          </div>
        )}

        {/* =========================================================================
            TAB 3: PROBLEM 3 - LINE PROJECTIONS & TRACES
            ========================================================================= */}
        {activeTab === 'partB-p3' && (
          <div className="bg-white dark:bg-[#181822] rounded-3xl p-6 sm:p-8 border border-paper-300 dark:border-darkbg-border shadow-sm space-y-6">
            <div className="flex items-center justify-between">
              <span className="px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-900/30 text-emerald-800 dark:text-emerald-300 text-xs font-mono font-bold">
                PART-B • QUESTION 3 [10 MARKS]
              </span>
              <span className="text-xs font-mono text-ink-500">True Length = 60 mm, θ = 45°</span>
            </div>

            <div>
              <h2 className="text-lg sm:text-2xl font-bold text-ink-900 dark:text-paper-50">
                Projections of Straight Line AB Inclined to HP and Parallel to VP
              </h2>
              <p className="text-sm text-ink-600 dark:text-ink-400 mt-1">
                "Represent the projection of line AB 60 mm long inclined to HP at 45° and parallel to VP. The nearest end A is 20 mm above HP and 25 mm in front of VP. Also show the trace of line."
              </p>
            </div>

            {/* Calculations & Properties */}
            <div className="grid grid-cols-1 sm:grid-cols-4 gap-3 text-xs">
              <div className="p-3.5 rounded-xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border">
                <span className="text-ink-500 font-mono">True Length (TL)</span>
                <p className="text-sm font-bold text-ink-900 dark:text-paper-50 mt-1">60 mm</p>
              </div>
              <div className="p-3.5 rounded-xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border">
                <span className="text-ink-500 font-mono">Front View (a'b')</span>
                <p className="text-sm font-bold text-emerald-600 dark:text-emerald-400 mt-1">60 mm at 45° (TL)</p>
              </div>
              <div className="p-3.5 rounded-xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border">
                <span className="text-ink-500 font-mono">Top View Plan (ab)</span>
                <p className="text-sm font-bold text-blue-600 dark:text-blue-400 mt-1">42.43 mm (Horizontal)</p>
              </div>
              <div className="p-3.5 rounded-xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border">
                <span className="text-ink-500 font-mono">Horizontal Trace (HT)</span>
                <p className="text-sm font-bold text-red-600 dark:text-red-400 mt-1">25 mm below XY</p>
              </div>
            </div>

            {/* SVG Line Projection Model */}
            <div className="bg-[#FBF9F5] dark:bg-[#12131C] rounded-2xl p-6 border border-paper-300 dark:border-darkbg-border flex flex-col items-center">
              <svg viewBox="0 0 500 300" className="w-full max-w-xl">
                {/* Reference line XY */}
                <line x1="50" y1="150" x2="450" y2="150" stroke="#0F172A" strokeWidth="2" className="dark:stroke-paper-50" />
                <text x="55" y="142" fill="#64748B" fontSize="12" fontWeight="bold">X</text>
                <text x="440" y="142" fill="#64748B" fontSize="12" fontWeight="bold">Y</text>

                {/* Point A vertical projector */}
                <line x1="180" y1="70" x2="180" y2="230" stroke="#94A3B8" strokeWidth="1" strokeDasharray="3 3" />
                {/* a' at 20mm above XY (y = 150 - 40 = 110) */}
                <circle cx="180" cy="110" r="3.5" fill="#0F172A" className="dark:fill-paper-50" />
                <text x="165" y="115" fill="#0F172A" fontSize="12" fontWeight="bold" className="dark:fill-paper-50">a'</text>

                {/* a at 25mm below XY (y = 150 + 50 = 200) */}
                <circle cx="180" cy="200" r="3.5" fill="#0F172A" className="dark:fill-paper-50" />
                <text x="168" y="205" fill="#0F172A" fontSize="12" fontWeight="bold" className="dark:fill-paper-50">a</text>

                {/* Front view line a'b' = 60mm at 45 deg */}
                <line x1="180" y1="110" x2="265" y2="25" stroke="#059669" strokeWidth="3" />
                <circle cx="265" cy="25" r="3.5" fill="#059669" />
                <text x="272" y="25" fill="#059669" fontSize="12" fontWeight="bold">b' (TL = 60)</text>

                {/* Angle 45 deg arc */}
                <line x1="180" y1="110" x2="230" y2="110" stroke="#CBD5E1" strokeWidth="1" strokeDasharray="2 2" />
                <text x="210" y="105" fill="#059669" fontSize="10" fontWeight="bold">45°</text>

                {/* Projector from b' down to Top view line */}
                <line x1="265" y1="25" x2="265" y2="200" stroke="#94A3B8" strokeWidth="1" strokeDasharray="3 3" />

                {/* Top view line ab (horizontal parallel to XY) */}
                <line x1="180" y1="200" x2="265" y2="200" stroke="#2563EB" strokeWidth="3" />
                <circle cx="265" cy="200" r="3.5" fill="#2563EB" />
                <text x="272" y="205" fill="#2563EB" fontSize="12" fontWeight="bold">b (Apparent = 42.4)</text>

                {/* Trace HT: extend b'a' back to XY at h' */}
                <line x1="180" y1="110" x2="140" y2="150" stroke="#EF4444" strokeWidth="1.5" strokeDasharray="2 2" />
                <circle cx="140" cy="150" r="3" fill="#EF4444" />
                <text x="135" y="142" fill="#EF4444" fontSize="11" fontWeight="bold">h'</text>

                {/* Project down to meet line ba extended at HT */}
                <line x1="140" y1="150" x2="140" y2="200" stroke="#EF4444" strokeWidth="1.5" strokeDasharray="2 2" />
                <line x1="180" y1="200" x2="140" y2="200" stroke="#EF4444" strokeWidth="1.5" strokeDasharray="2 2" />
                <circle cx="140" cy="200" r="4" fill="#DC2626" />
                <text x="120" y="218" fill="#DC2626" fontSize="11" fontWeight="bold">HT (25mm)</text>
              </svg>
            </div>
          </div>
        )}

        {/* =========================================================================
            TAB 4: PART-A CONCEPTUAL QUESTIONS
            ========================================================================= */}
        {activeTab === 'partA' && (
          <div className="bg-white dark:bg-[#181822] rounded-3xl p-6 sm:p-8 border border-paper-300 dark:border-darkbg-border shadow-sm space-y-6">
            <div className="flex items-center justify-between">
              <span className="px-3 py-1 rounded-full bg-purple-100 dark:bg-purple-900/30 text-purple-800 dark:text-purple-300 text-xs font-mono font-bold">
                PART-A • 5 COMPULSORY QUESTIONS [10 MARKS TOTAL]
              </span>
              <span className="text-xs font-mono text-ink-500">2 Marks Each</span>
            </div>

            <div className="space-y-4">
              {test.partA.questions.map((q) => {
                const isRevealed = revealedAnswers[q.id];

                return (
                  <div
                    key={q.id}
                    className="p-5 rounded-2xl bg-paper-100/70 dark:bg-darkbg-900/70 border border-paper-200 dark:border-darkbg-border space-y-3 transition-all"
                  >
                    <div className="flex items-start justify-between gap-4">
                      <div>
                        <span className="text-xs font-mono font-bold text-ochre-600 dark:text-ochre-400">
                          {q.questionNumber} • {q.topic} [2 Marks]
                        </span>
                        <h3 className="text-sm sm:text-base font-bold text-ink-900 dark:text-paper-50 mt-1">
                          {q.prompt}
                        </h3>
                      </div>

                      <button
                        onClick={() => toggleAnswer(q.id)}
                        className="px-3 py-1 rounded-full text-xs font-bold bg-white dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 hover:bg-paper-200 transition-colors whitespace-nowrap"
                      >
                        {isRevealed ? 'Hide Solution' : 'Reveal Solution'}
                      </button>
                    </div>

                    {isRevealed && (
                      <div className="pt-3 border-t border-paper-200 dark:border-darkbg-border space-y-2 text-xs text-ink-700 dark:text-paper-200 animate-fadeIn">
                        <p className="font-bold text-ink-900 dark:text-paper-50">{q.modelAnswer.summary}</p>
                        <ul className="list-disc list-inside space-y-1 text-ink-600 dark:text-ink-400">
                          {q.modelAnswer.points.map((pt, i) => (
                            <li key={i}>{pt}</li>
                          ))}
                        </ul>
                        {q.modelAnswer.keyFormula && (
                          <div className="p-2.5 rounded-lg bg-ochre-50 dark:bg-ochre-900/20 text-ochre-800 dark:text-ochre-300 font-mono text-[11px] font-bold">
                            {q.modelAnswer.keyFormula}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* =========================================================================
            TAB 5: SCORING RUBRIC & SELF-EVALUATION
            ========================================================================= */}
        {activeTab === 'rubric' && (
          <div className="bg-white dark:bg-[#181822] rounded-3xl p-6 sm:p-8 border border-paper-300 dark:border-darkbg-border shadow-sm space-y-6">
            <div className="flex items-center justify-between">
              <span className="px-3 py-1 rounded-full bg-amber-100 dark:bg-amber-900/30 text-amber-800 dark:text-amber-300 text-xs font-mono font-bold">
                UNIVERSITY EVALUATION RUBRIC [MAX: 40 MARKS]
              </span>
              <span className="text-sm font-mono font-bold text-ochre-600 dark:text-ochre-400">
                Your Assessed Score: {totalEvaluatedScore} / 40
              </span>
            </div>

            <p className="text-xs text-ink-600 dark:text-ink-400">
              Grade your manual drawing sheets using the official university criteria below. Check the boxes or assign points to track your midterm readiness.
            </p>

            {/* Rubric Breakdown */}
            <div className="space-y-4">
              <div className="p-4 rounded-2xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border space-y-3">
                <h3 className="text-sm font-bold text-ink-900 dark:text-paper-50 flex items-center justify-between">
                  <span>Part-A: Technical Concepts (Q1a to Q1e)</span>
                  <span className="font-mono text-xs text-ochre-500">10 Marks Max</span>
                </h3>
                <div className="grid grid-cols-2 sm:grid-cols-5 gap-2 text-xs">
                  {['Q1(a)', 'Q1(b)', 'Q1(c)', 'Q1(d)', 'Q1(e)'].map((label, idx) => {
                    const key = `partA_${idx}`;
                    const curr = rubricScores[key] || 0;
                    return (
                      <div key={key} className="p-2.5 rounded-xl bg-white dark:bg-darkbg-800 border flex items-center justify-between">
                        <span className="font-bold">{label}</span>
                        <div className="flex items-center gap-1">
                          {[0, 1, 2].map((pts) => (
                            <button
                              key={pts}
                              onClick={() => setRubricScores({ ...rubricScores, [key]: pts })}
                              className={`w-6 h-6 rounded-md font-mono text-[10px] font-bold ${
                                curr === pts ? 'bg-ink-900 text-white dark:bg-paper-50 dark:text-ink-900' : 'bg-paper-200 dark:bg-darkbg-700'
                              }`}
                            >
                              {pts}
                            </button>
                          ))}
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Part B Rubrics */}
              {test.partB.problems.map((prob) => (
                <div key={prob.id} className="p-4 rounded-2xl bg-paper-100 dark:bg-darkbg-900 border border-paper-200 dark:border-darkbg-border space-y-3">
                  <h3 className="text-sm font-bold text-ink-900 dark:text-paper-50 flex items-center justify-between">
                    <span>{prob.questionNumber}: {prob.title}</span>
                    <span className="font-mono text-xs text-ochre-500">10 Marks Max</span>
                  </h3>
                  <div className="space-y-2">
                    {prob.scoringRubric.map((crit, cIdx) => {
                      const key = `${prob.id}_${cIdx}`;
                      const isAwarded = rubricScores[key] === crit.marks;
                      return (
                        <div key={key} className="flex items-center justify-between text-xs p-2 rounded-lg bg-white dark:bg-darkbg-800 border border-paper-200 dark:border-darkbg-border">
                          <span>{crit.criterion}</span>
                          <button
                            onClick={() => setRubricScores({
                              ...rubricScores,
                              [key]: isAwarded ? 0 : crit.marks
                            })}
                            className={`px-3 py-1 rounded-md font-mono font-bold transition-all ${
                              isAwarded ? 'bg-emerald-600 text-white' : 'bg-paper-200 dark:bg-darkbg-700 text-ink-700 dark:text-paper-200'
                            }`}
                          >
                            {isAwarded ? `+${crit.marks} M` : `0 / ${crit.marks}`}
                          </button>
                        </div>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      {/* Exit Confirmation Modal */}
      {showExitDialog && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-ink-950/60 backdrop-blur-sm animate-fadeIn">
          <div className="bg-white dark:bg-[#181822] rounded-3xl max-w-sm w-full p-6 border border-paper-300 dark:border-darkbg-border shadow-2xl space-y-4">
            <h3 className="text-base font-bold text-ink-900 dark:text-paper-50">
              Leave Drafting Studio?
            </h3>
            <p className="text-xs text-ink-600 dark:text-ink-400">
              Are you sure you want to return to the Exam Hub? Your draft sketches and self-assessment scores will be saved.
            </p>
            <div className="flex items-center justify-end gap-2 pt-2">
              <button
                onClick={() => setShowExitDialog(false)}
                className="px-4 py-2 rounded-xl text-xs font-bold text-ink-700 dark:text-paper-200 hover:bg-paper-200"
              >
                Continue Drafting
              </button>
              <button
                onClick={onExitExam}
                className="px-4 py-2 rounded-xl text-xs font-bold bg-red-600 text-white hover:bg-red-700"
              >
                Exit to Hub
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
