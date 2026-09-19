import React, { useState, useEffect, useRef } from 'react';
import * as pdfjsLib from 'pdfjs-dist';
import {
  ChevronLeft,
  ChevronRight,
  ZoomIn,
  ZoomOut,
  Maximize2,
  Minimize2,
  ArrowLeft,
  ShieldCheck,
  RotateCcw,
  Loader2,
  Lock,
} from 'lucide-react';
import { api } from '../services/api';

pdfjsLib.GlobalWorkerOptions.workerSrc = `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version || '3.11.174'}/pdf.worker.min.js`;

export default function Viewer({ material, user, onBack }) {
  const [pdfDoc, setPdfDoc] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);
  const [scale, setScale] = useState(1.2);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [renderingPage, setRenderingPage] = useState(false);

  const canvasRef = useRef(null);
  const viewerContainerRef = useRef(null);
  const renderTaskRef = useRef(null);

  useEffect(() => {
    let isMounted = true;

    async function loadDocument() {
      try {
        setLoading(true);
        setError(null);

        const tokenData = await api.getDocumentStreamToken(material.id);
        const streamUrl = api.getDocumentStreamUrl(tokenData.token, material);

        const loadingTask = pdfjsLib.getDocument({
          url: streamUrl,
          withCredentials: true,
          disableAutoFetch: false,
          disableStream: false,
        });

        const doc = await loadingTask.promise;
        if (isMounted) {
          setPdfDoc(doc);
          setTotalPages(doc.numPages);
          setCurrentPage(1);
          setLoading(false);
        }
      } catch (err) {
        console.error('Error loading secure document:', err);
        if (isMounted) {
          setError(err.message || 'Failed to load document. Please verify your login.');
          setLoading(false);
        }
      }
    }

    if (material && material.id) {
      loadDocument();
    }

    return () => {
      isMounted = false;
    };
  }, [material]);

  useEffect(() => {
    if (!pdfDoc || !canvasRef.current) return;

    let isCurrentRender = true;

    async function renderPage() {
      try {
        setRenderingPage(true);

        if (renderTaskRef.current) {
          renderTaskRef.current.cancel();
        }

        const page = await pdfDoc.getPage(currentPage);
        if (!isCurrentRender) return;

        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');

        const viewport = page.getViewport({ scale });
        const outputScale = window.devicePixelRatio || 1;

        canvas.width = Math.floor(viewport.width * outputScale);
        canvas.height = Math.floor(viewport.height * outputScale);
        canvas.style.width = Math.floor(viewport.width) + 'px';
        canvas.style.height = Math.floor(viewport.height) + 'px';

        const transform = outputScale !== 1 ? [outputScale, 0, 0, outputScale, 0, 0] : null;

        const renderContext = {
          canvasContext: ctx,
          transform: transform,
          viewport: viewport,
        };

        const renderTask = page.render(renderContext);
        renderTaskRef.current = renderTask;

        await renderTask.promise;

        if (isCurrentRender) {
          setRenderingPage(false);
        }
      } catch (err) {
        if (err.name !== 'RenderingCancelledException') {
          console.error('Page render error:', err);
        }
        if (isCurrentRender) {
          setRenderingPage(false);
        }
      }
    }

    renderPage();

    return () => {
      isCurrentRender = false;
      if (renderTaskRef.current) {
        renderTaskRef.current.cancel();
      }
    };
  }, [pdfDoc, currentPage, scale, user]);

  const handlePrevPage = () => {
    if (currentPage > 1) setCurrentPage((prev) => prev - 1);
  };

  const handleNextPage = () => {
    if (currentPage < totalPages) setCurrentPage((prev) => prev + 1);
  };

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      viewerContainerRef.current?.requestFullscreen?.();
      setIsFullscreen(true);
    } else {
      document.exitFullscreen?.();
      setIsFullscreen(false);
    }
  };

  return (
    <div
      ref={viewerContainerRef}
      className="flex flex-col h-screen bg-[#EFECE4] dark:bg-darkbg-950 text-ink-900 dark:text-paper-100 select-none overflow-hidden transition-colors"
    >
      {/* Top Header Toolbar */}
      <header className="h-16 bg-paper-50/90 dark:bg-darkbg-900/90 border-b border-paper-300 dark:border-darkbg-border px-4 sm:px-6 flex items-center justify-between z-30 shrink-0 backdrop-blur-md">
        <div className="flex items-center gap-3">
          <button
            onClick={onBack}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-800 dark:text-paper-100 transition text-xs font-mono font-semibold border border-paper-300/80 dark:border-darkbg-border shadow-xs"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">ARCHIVES</span>
          </button>

          <div className="h-5 w-px bg-paper-300 dark:bg-darkbg-border hidden sm:block"></div>

          {/* Star Logo + Title */}
          <div className="flex items-center gap-2.5 min-w-0">
            <div className="w-6 h-6 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center p-1 shrink-0">
              <img src="/logo.png" alt="Star" className="w-full h-full object-contain filter invert dark:invert-0" />
            </div>
            <div className="flex flex-col min-w-0">
              <h2 className="text-xs sm:text-sm font-bold font-sans text-ink-900 dark:text-paper-50 truncate max-w-[180px] sm:max-w-md">
                {material.title}
              </h2>
              <span className="text-[10px] font-mono text-ink-400 dark:text-ink-400 truncate">
                {material.courseCode} • {material.category}
              </span>
            </div>
          </div>
        </div>

        {/* Center Page Navigator */}
        <div className="flex items-center gap-1.5 bg-paper-200/90 dark:bg-darkbg-800 px-2 py-1 rounded-full border border-paper-300 dark:border-darkbg-border shadow-xs">
          <button
            onClick={handlePrevPage}
            disabled={currentPage <= 1 || loading}
            className="p-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 transition"
          >
            <ChevronLeft className="w-4 h-4 text-ink-800 dark:text-paper-100" />
          </button>

          <div className="flex items-center gap-1 font-mono text-[11px] font-bold text-ink-900 dark:text-paper-50 px-2">
            <span>{currentPage}</span>
            <span className="text-paper-400 dark:text-ink-600">/</span>
            <span>{totalPages || '--'}</span>
          </div>

          <button
            onClick={handleNextPage}
            disabled={currentPage >= totalPages || loading}
            className="p-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 transition"
          >
            <ChevronRight className="w-4 h-4 text-ink-800 dark:text-paper-100" />
          </button>
        </div>

        {/* Right Controls */}
        <div className="flex items-center gap-2">
          <div className="hidden md:flex items-center gap-1.5 bg-paper-200 dark:bg-darkbg-800 px-3 py-1 rounded-full border border-paper-300 dark:border-darkbg-border text-[10px] font-mono text-emerald-800 dark:text-emerald-400 font-semibold">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
            <span>PROTECTED PASS</span>
          </div>

          <div className="flex items-center gap-1 bg-paper-200/90 dark:bg-darkbg-800 rounded-full p-1 border border-paper-300 dark:border-darkbg-border">
            <button
              onClick={() => setScale((s) => Math.max(0.6, s - 0.2))}
              className="p-1 hover:bg-paper-300 dark:hover:bg-darkbg-700 rounded-full text-ink-700 dark:text-paper-200 transition"
              title="Zoom Out"
            >
              <ZoomOut className="w-3.5 h-3.5" />
            </button>
            <span className="text-[10px] font-mono px-1.5 text-ink-600 dark:text-paper-300 font-bold">
              {Math.round(scale * 100)}%
            </span>
            <button
              onClick={() => setScale((s) => Math.min(2.5, s + 0.2))}
              className="p-1 hover:bg-paper-300 dark:hover:bg-darkbg-700 rounded-full text-ink-700 dark:text-paper-200 transition"
              title="Zoom In"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={() => setScale(1.2)}
              className="p-1 hover:bg-paper-300 dark:hover:bg-darkbg-700 rounded-full text-ink-700 dark:text-paper-200 transition"
              title="Reset Zoom"
            >
              <RotateCcw className="w-3 h-3" />
            </button>
          </div>

          <button
            onClick={toggleFullscreen}
            className="p-2 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-800 dark:text-paper-100 transition border border-paper-300 dark:border-darkbg-border"
            title="Toggle Fullscreen"
          >
            {isFullscreen ? <Minimize2 className="w-3.5 h-3.5" /> : <Maximize2 className="w-3.5 h-3.5" />}
          </button>
        </div>
      </header>

      {/* Main Canvas Document Area (Completely Clean without Watermarks) */}
      <main className="flex-1 overflow-auto relative flex items-center justify-center p-4 sm:p-8 bg-[#E5E1D5] dark:bg-darkbg-900">
        {loading && (
          <div className="flex flex-col items-center gap-3 text-ink-600 dark:text-ink-400">
            <Loader2 className="w-8 h-8 animate-spin text-ink-900 dark:text-paper-100" />
            <p className="text-xs font-mono tracking-widest uppercase">Opening Archival Volume...</p>
          </div>
        )}

        {error && (
          <div className="max-w-md p-8 bg-paper-50 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border rounded-[32px] text-center shadow-floating">
            <Lock className="w-10 h-10 text-terracotta-600 mx-auto mb-3" />
            <h3 className="text-base font-cinzel font-bold text-ink-900 dark:text-paper-50 mb-1">Pass Required</h3>
            <p className="text-xs text-ink-600 dark:text-ink-400 mb-4">{error}</p>
            <button
              onClick={onBack}
              className="px-5 py-2.5 bg-ink-900 dark:bg-paper-100 text-paper-50 dark:text-ink-900 rounded-full text-xs font-semibold uppercase tracking-wider transition"
            >
              Return to Archives
            </button>
          </div>
        )}

        {!loading && !error && (
          <div className="relative shadow-2xl rounded-xl overflow-hidden border border-paper-300 dark:border-darkbg-border bg-white">
            <canvas
              ref={canvasRef}
              className="block select-none pointer-events-none transition-transform"
            />

            {renderingPage && (
              <div className="absolute top-3 right-3 bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-md px-3 py-1 rounded-full text-[10px] font-mono text-ink-700 dark:text-paper-200 flex items-center gap-1.5 border border-paper-300 dark:border-darkbg-border shadow-xs">
                <Loader2 className="w-3 h-3 animate-spin text-ink-900 dark:text-paper-100" />
                <span>Syncing Page...</span>
              </div>
            )}
          </div>
        )}
      </main>

      {/* Perforated Archival Footer */}
      <footer className="h-8 bg-paper-50 dark:bg-darkbg-900 border-t border-paper-300 dark:border-darkbg-border px-6 flex items-center justify-between text-[10px] text-ink-500 dark:text-ink-400 font-mono shrink-0">
        <div className="flex items-center gap-3">
          <span className="font-bold text-ink-800 dark:text-paper-200">EDU NETWORK ARCHIVES</span>
          <span>•</span>
          <span className="truncate">ACCOUNT: {user?.email}</span>
        </div>
        <div className="hidden sm:flex items-center gap-3">
          <span>NO DOWNLOAD PERMITTED</span>
          <span>•</span>
          <span className="barcode text-[10px]">|||| ||| |||||</span>
        </div>
      </footer>
    </div>
  );
}
