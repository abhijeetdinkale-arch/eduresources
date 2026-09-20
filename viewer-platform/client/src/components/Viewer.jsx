import React, { useState, useEffect, useRef, useCallback } from 'react';
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
  StretchHorizontal,
  Maximize,
  SlidersHorizontal,
  X,
} from 'lucide-react';
import { api } from '../services/api';

pdfjsLib.GlobalWorkerOptions.workerSrc = `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version || '3.11.174'}/pdf.worker.min.js`;

export default function Viewer({ material, user, onBack }) {
  const [pdfDoc, setPdfDoc] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);
  const [scale, setScale] = useState(1.0);
  const [fitMode, setFitMode] = useState(() => (window.innerWidth < 768 ? 'fit-width' : 'fit-page'));
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [renderingPage, setRenderingPage] = useState(false);

  const canvasRef = useRef(null);
  const viewerContainerRef = useRef(null);
  const mainContainerRef = useRef(null);
  const renderTaskRef = useRef(null);
  const rawPageViewportRef = useRef(null);

  // Sync fullscreen state with native document fullscreen
  useEffect(() => {
    const handleFullscreenChange = () => {
      setIsFullscreen(Boolean(document.fullscreenElement));
    };

    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);

    return () => {
      document.removeEventListener('fullscreenchange', handleFullscreenChange);
      document.removeEventListener('webkitfullscreenchange', handleFullscreenChange);
    };
  }, []);

  // Load PDF Document
  useEffect(() => {
    let isMounted = true;

    async function loadDocument() {
      try {
        let doc;
        try {
          const tokenData = await api.getDocumentStreamToken(material.id);
          const streamUrl = api.getDocumentStreamUrl(tokenData.token, material);

          const loadingTask = pdfjsLib.getDocument({
            url: streamUrl,
            withCredentials: true,
            disableAutoFetch: false,
            disableStream: false,
          });
          doc = await loadingTask.promise;
        } catch (streamErr) {
          // Cloud/Serverless Edge fallback: load directly from pre-cached static book asset
          try {
            const fallbackUrl = `/books/${material.id}.dat`;
            const fallbackTask = pdfjsLib.getDocument({
              url: fallbackUrl,
              withCredentials: true,
            });
            doc = await fallbackTask.promise;
          } catch (fallbackErr) {
            throw streamErr || fallbackErr;
          }
        }
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

  // Compute adaptive scale according to device and fitMode
  const calculateScale = useCallback(
    (pageViewport, mode) => {
      if (!mainContainerRef.current || !pageViewport) return scale;

      const container = mainContainerRef.current;
      const isMobile = window.innerWidth < 640;
      const padX = isMobile ? 16 : 48;
      const padY = isMobile ? 16 : 48;

      const availWidth = Math.max(280, container.clientWidth - padX);
      const availHeight = Math.max(280, container.clientHeight - padY);

      if (mode === 'fit-width') {
        const computed = availWidth / pageViewport.width;
        return Math.min(3.0, Math.max(0.35, +computed.toFixed(2)));
      } else if (mode === 'fit-page') {
        const scaleX = availWidth / pageViewport.width;
        const scaleY = availHeight / pageViewport.height;
        const computed = Math.min(scaleX, scaleY);
        return Math.min(3.0, Math.max(0.35, +computed.toFixed(2)));
      }

      return scale;
    },
    [scale]
  );

  // Render Page onto Canvas
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

        const unscaledViewport = page.getViewport({ scale: 1.0 });
        rawPageViewportRef.current = unscaledViewport;

        // Auto calculate scale if in fit mode
        let activeScale = scale;
        if (fitMode === 'fit-width' || fitMode === 'fit-page') {
          activeScale = calculateScale(unscaledViewport, fitMode);
          if (activeScale !== scale) {
            setScale(activeScale);
          }
        }

        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');

        const viewport = page.getViewport({ scale: activeScale });
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
  }, [pdfDoc, currentPage, scale, fitMode, calculateScale, user]);

  // Window resize handler to maintain adaptive sizing
  useEffect(() => {
    let resizeTimer = null;
    const handleResize = () => {
      if (resizeTimer) clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        if (fitMode === 'fit-width' || fitMode === 'fit-page') {
          if (rawPageViewportRef.current) {
            const newScale = calculateScale(rawPageViewportRef.current, fitMode);
            setScale(newScale);
          }
        }
      }, 150);
    };

    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
      if (resizeTimer) clearTimeout(resizeTimer);
    };
  }, [fitMode, calculateScale]);

  // Page navigation handlers
  const handlePrevPage = useCallback(() => {
    setCurrentPage((prev) => Math.max(1, prev - 1));
  }, []);

  const handleNextPage = useCallback(() => {
    setCurrentPage((prev) => (totalPages > 0 ? Math.min(totalPages, prev + 1) : prev + 1));
  }, [totalPages]);

  const toggleFullscreen = useCallback(() => {
    if (!document.fullscreenElement) {
      viewerContainerRef.current?.requestFullscreen?.().catch(() => {});
      setIsFullscreen(true);
    } else {
      document.exitFullscreen?.().catch(() => {});
      setIsFullscreen(false);
    }
  }, []);

  const handleBackToArchives = useCallback(() => {
    if (document.fullscreenElement) {
      document.exitFullscreen?.().catch(() => {});
    }
    if (onBack) onBack();
  }, [onBack]);

  // Keyboard navigation for Laptop / Hardware keys
  useEffect(() => {
    const handleKeyDown = (e) => {
      // Don't intercept if user is typing in an input
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) {
        return;
      }

      // Next page keys: ArrowRight, ArrowDown, PageDown, Spacebar, Enter, N
      if (
        e.key === 'ArrowRight' ||
        e.key === 'ArrowDown' ||
        e.key === 'PageDown' ||
        (e.key === ' ' && !e.shiftKey) ||
        e.key === 'n' ||
        e.key === 'N'
      ) {
        e.preventDefault();
        handleNextPage();
      }
      // Previous page keys: ArrowLeft, ArrowUp, PageUp, Shift+Space, Backspace, P
      else if (
        e.key === 'ArrowLeft' ||
        e.key === 'ArrowUp' ||
        e.key === 'PageUp' ||
        (e.key === ' ' && e.shiftKey) ||
        e.key === 'p' ||
        e.key === 'P'
      ) {
        e.preventDefault();
        handlePrevPage();
      }
      // First page / Last page
      else if (e.key === 'Home') {
        e.preventDefault();
        setCurrentPage(1);
      } else if (e.key === 'End') {
        e.preventDefault();
        if (totalPages > 0) setCurrentPage(totalPages);
      }
      // Zoom in: + or =
      else if (e.key === '+' || e.key === '=') {
        e.preventDefault();
        setFitMode('custom');
        setScale((s) => Math.min(3.0, +(s + 0.15).toFixed(2)));
      }
      // Zoom out: - or _
      else if (e.key === '-' || e.key === '_') {
        e.preventDefault();
        setFitMode('custom');
        setScale((s) => Math.max(0.4, +(s - 0.15).toFixed(2)));
      }
      // Reset fit / 100%: 0
      else if (e.key === '0') {
        e.preventDefault();
        setFitMode('fit-width');
      }
      // Fullscreen: F
      else if (e.key === 'f' || e.key === 'F') {
        if (!e.ctrlKey && !e.metaKey) {
          e.preventDefault();
          toggleFullscreen();
        }
      }
      // Escape: Go back if not in native fullscreen
      else if (e.key === 'Escape') {
        if (!document.fullscreenElement && onBack) {
          onBack();
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleNextPage, handlePrevPage, totalPages, toggleFullscreen, onBack]);

  const handleZoomIn = () => {
    setFitMode('custom');
    setScale((s) => Math.min(3.0, +(s + 0.2).toFixed(2)));
  };

  const handleZoomOut = () => {
    setFitMode('custom');
    setScale((s) => Math.max(0.4, +(s - 0.2).toFixed(2)));
  };

  const handleSetFitWidth = () => {
    setFitMode('fit-width');
    if (rawPageViewportRef.current) {
      setScale(calculateScale(rawPageViewportRef.current, 'fit-width'));
    }
  };

  const handleSetFitPage = () => {
    setFitMode('fit-page');
    if (rawPageViewportRef.current) {
      setScale(calculateScale(rawPageViewportRef.current, 'fit-page'));
    }
  };

  return (
    <div
      ref={viewerContainerRef}
      className="flex flex-col h-screen bg-[#EFECE4] dark:bg-darkbg-950 text-ink-900 dark:text-paper-100 select-none overflow-hidden transition-colors relative"
    >
      {/* Top Header Toolbar */}
      <header className="h-16 bg-paper-50/95 dark:bg-darkbg-900/95 border-b border-paper-300 dark:border-darkbg-border px-3 sm:px-6 flex items-center justify-between z-30 shrink-0 backdrop-blur-md gap-2">
        {/* Left: Back + Book Title */}
        <div className="flex items-center gap-2 sm:gap-3 min-w-0">
          <button
            onClick={handleBackToArchives}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-800 dark:text-paper-100 transition text-xs font-mono font-semibold border border-paper-300/80 dark:border-darkbg-border shadow-xs shrink-0"
            title="Return to Subject Dossier"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">ARCHIVES</span>
          </button>

          <div className="h-5 w-px bg-paper-300 dark:bg-darkbg-border hidden md:block"></div>

          {/* Star Logo + Title */}
          <div className="flex items-center gap-2 min-w-0">
            <div className="w-6 h-6 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center p-1 shrink-0">
              <img src="/logo.png" alt="Star" className="w-full h-full object-contain filter invert dark:invert-0" />
            </div>
            <div className="flex flex-col min-w-0">
              <h2 className="text-xs sm:text-sm font-bold font-sans text-ink-900 dark:text-paper-50 truncate max-w-[130px] sm:max-w-[220px] md:max-w-md">
                {material.title}
              </h2>
              <span className="text-[10px] font-mono text-ink-400 dark:text-ink-400 truncate">
                {material.courseCode} • {material.category}
              </span>
            </div>
          </div>
        </div>

        {/* Center Page Navigator */}
        <div className="flex items-center gap-1 bg-paper-200/90 dark:bg-darkbg-800 px-2 py-1 rounded-full border border-paper-300 dark:border-darkbg-border shadow-xs shrink-0">
          <button
            onClick={handlePrevPage}
            disabled={currentPage <= 1 || loading}
            className="p-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 transition"
            title="Previous Page (← / PageUp)"
          >
            <ChevronLeft className="w-4 h-4 text-ink-800 dark:text-paper-100" />
          </button>

          <div className="flex items-center gap-1 font-mono text-[11px] font-bold text-ink-900 dark:text-paper-50 px-1.5 sm:px-2">
            <span>{currentPage}</span>
            <span className="text-paper-400 dark:text-ink-600">/</span>
            <span>{totalPages || '--'}</span>
          </div>

          <button
            onClick={handleNextPage}
            disabled={currentPage >= totalPages || loading}
            className="p-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 transition"
            title="Next Page (→ / PageDown / Space)"
          >
            <ChevronRight className="w-4 h-4 text-ink-800 dark:text-paper-100" />
          </button>
        </div>

        {/* Right Controls: Fit Width / Fit Page + Zoom + Fullscreen / Exit Cross */}
        <div className="flex items-center gap-1 sm:gap-2 shrink-0">
          {/* Keyboard prompt badge on desktop */}
          <div className="hidden xl:flex items-center gap-1 bg-paper-200/60 dark:bg-darkbg-800/60 px-2.5 py-1 rounded-full border border-paper-300/80 dark:border-darkbg-border text-[9px] font-mono text-ink-500 dark:text-ink-400">
            <span>⌨ Laptop Keys: [← / → / Space]</span>
          </div>

          {/* Adaptive Fit Modes */}
          <div className="hidden md:flex items-center gap-1 bg-paper-200/90 dark:bg-darkbg-800 rounded-full p-1 border border-paper-300 dark:border-darkbg-border">
            <button
              onClick={handleSetFitWidth}
              className={`px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold transition flex items-center gap-1 ${
                fitMode === 'fit-width'
                  ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                  : 'text-ink-700 dark:text-paper-300 hover:bg-paper-300 dark:hover:bg-darkbg-700'
              }`}
              title="Fit to Width (0 key)"
            >
              <StretchHorizontal className="w-3 h-3" />
              <span>Fit Width</span>
            </button>
            <button
              onClick={handleSetFitPage}
              className={`px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold transition flex items-center gap-1 ${
                fitMode === 'fit-page'
                  ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                  : 'text-ink-700 dark:text-paper-300 hover:bg-paper-300 dark:hover:bg-darkbg-700'
              }`}
              title="Fit to Whole Page"
            >
              <Maximize className="w-3 h-3" />
              <span>Fit Page</span>
            </button>
          </div>

          {/* Zoom controls */}
          <div className="flex items-center gap-0.5 sm:gap-1 bg-paper-200/90 dark:bg-darkbg-800 rounded-full p-1 border border-paper-300 dark:border-darkbg-border">
            <button
              onClick={handleZoomOut}
              className="p-1 hover:bg-paper-300 dark:hover:bg-darkbg-700 rounded-full text-ink-700 dark:text-paper-200 transition"
              title="Zoom Out (- key)"
            >
              <ZoomOut className="w-3.5 h-3.5" />
            </button>
            <span className="text-[10px] font-mono px-1 sm:px-1.5 text-ink-600 dark:text-paper-300 font-bold min-w-[36px] text-center">
              {Math.round(scale * 100)}%
            </span>
            <button
              onClick={handleZoomIn}
              className="p-1 hover:bg-paper-300 dark:hover:bg-darkbg-700 rounded-full text-ink-700 dark:text-paper-200 transition"
              title="Zoom In (+ key)"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>
            <button
              onClick={handleSetFitWidth}
              className="hidden sm:block p-1 hover:bg-paper-300 dark:hover:bg-darkbg-700 rounded-full text-ink-700 dark:text-paper-200 transition"
              title="Reset Zoom to Fit Width (0 key)"
            >
              <RotateCcw className="w-3 h-3" />
            </button>
          </div>

          {/* Fullscreen / Exit Fullscreen Cross Button */}
          <button
            onClick={toggleFullscreen}
            className={`p-2 rounded-full transition border shadow-xs flex items-center gap-1.5 text-xs font-mono font-bold ${
              isFullscreen
                ? 'bg-terracotta-500/15 border-terracotta-500/40 text-terracotta-600 dark:text-terracotta-400 hover:bg-terracotta-500/25 px-3'
                : 'bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-800 dark:text-paper-100 border-paper-300 dark:border-darkbg-border'
            }`}
            title={isFullscreen ? 'Exit Fullscreen (✕ / Esc / F)' : 'Toggle Fullscreen (F key)'}
          >
            {isFullscreen ? (
              <>
                <X className="w-4 h-4 text-terracotta-600 dark:text-terracotta-400 shrink-0" />
                <span className="hidden sm:inline">EXIT (✕)</span>
              </>
            ) : (
              <Maximize2 className="w-3.5 h-3.5" />
            )}
          </button>
        </div>
      </header>

      {/* Floating Exit / Back Controls (Visible when in Fullscreen) */}
      {isFullscreen && (
        <div className="fixed top-20 right-4 sm:right-8 z-50 flex items-center gap-2 bg-paper-50/95 dark:bg-darkbg-850/95 backdrop-blur-md p-1.5 rounded-full border border-paper-300 dark:border-darkbg-border shadow-floating animate-in fade-in zoom-in duration-200">
          <button
            onClick={handleBackToArchives}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-750 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-900 dark:text-paper-100 text-xs font-mono font-semibold transition shadow-xs"
            title="Return to Archives"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span>Archives</span>
          </button>
          <button
            onClick={toggleFullscreen}
            className="flex items-center gap-1 px-3.5 py-1.5 rounded-full bg-terracotta-500/15 hover:bg-terracotta-500/25 text-terracotta-600 dark:text-terracotta-400 text-xs font-mono font-bold transition border border-terracotta-500/30 shadow-xs"
            title="Exit Fullscreen Mode (✕ / Esc)"
          >
            <X className="w-4 h-4" />
            <span>Exit Fullscreen</span>
          </button>
        </div>
      )}

      {/* Main Canvas Document Area (Adaptive Responsive Fitting) */}
      <main
        ref={mainContainerRef}
        className="flex-1 overflow-auto relative flex items-center justify-center p-2 sm:p-6 md:p-8 bg-[#E5E1D5] dark:bg-darkbg-900 scroll-smooth"
      >
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
              onClick={handleBackToArchives}
              className="px-5 py-2.5 bg-ink-900 dark:bg-paper-100 text-paper-50 dark:text-ink-900 rounded-full text-xs font-semibold uppercase tracking-wider transition"
            >
              Return to Archives
            </button>
          </div>
        )}

        {!loading && !error && (
          <div className="relative shadow-2xl rounded-xl overflow-hidden border border-paper-300 dark:border-darkbg-border bg-white my-auto max-w-full">
            <canvas
              ref={canvasRef}
              className="block select-none pointer-events-none transition-transform max-w-full h-auto mx-auto"
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
      <footer className="h-8 bg-paper-50 dark:bg-darkbg-900 border-t border-paper-300 dark:border-darkbg-border px-4 sm:px-6 flex items-center justify-between text-[10px] text-ink-500 dark:text-ink-400 font-mono shrink-0">
        <div className="flex items-center gap-2 sm:gap-3 truncate">
          <span className="font-bold text-ink-800 dark:text-paper-200 truncate">EDU NETWORK ARCHIVES</span>
          <span>•</span>
          <span className="truncate">ACCOUNT: {user?.email}</span>
        </div>
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          <span className="hidden sm:inline">NO DOWNLOAD PERMITTED</span>
          <span className="hidden sm:inline">•</span>
          <span className="barcode text-[10px]">|||| ||| |||||</span>
        </div>
      </footer>
    </div>
  );
}
