import React, { useState, useEffect, useRef, useCallback, memo } from 'react';
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
  Scroll,
  FileText,
  ArrowUp,
  ArrowDown,
  Layers,
} from 'lucide-react';
import { api } from '../services/api';

pdfjsLib.GlobalWorkerOptions.workerSrc = `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version || '3.11.174'}/pdf.worker.min.js`;

/**
 * Individual Lazy-Loaded Page Component for Continuous Vertical Scroll Mode
 */
const ContinuousPageItem = memo(function ContinuousPageItem({
  pageNum,
  totalPages,
  pdfDoc,
  scale,
  defaultAspect,
  onVisible,
  user,
}) {
  const containerRef = useRef(null);
  const canvasRef = useRef(null);
  const renderTaskRef = useRef(null);
  const [inView, setInView] = useState(pageNum <= 3); // Pre-load first 3 pages immediately
  const [rendered, setRendered] = useState(false);
  const [rendering, setRendering] = useState(false);
  const [dimensions, setDimensions] = useState(null);

  // Lazy-load intersection observer
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setInView(true);
          }
        });
      },
      { rootMargin: '800px 0px 800px 0px', threshold: 0.01 }
    );

    observer.observe(el);

    // Active page observer to update current page indicator
    const activeObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && entry.intersectionRatio >= 0.4) {
            onVisible(pageNum);
          }
        });
      },
      { threshold: [0.4, 0.7] }
    );

    activeObserver.observe(el);

    return () => {
      observer.disconnect();
      activeObserver.disconnect();
    };
  }, [pageNum, onVisible]);

  // Render Page to Canvas
  useEffect(() => {
    if (!pdfDoc || !inView || !canvasRef.current) return;

    let isCurrent = true;

    async function drawPage() {
      try {
        setRendering(true);
        if (renderTaskRef.current) {
          renderTaskRef.current.cancel();
        }

        const page = await pdfDoc.getPage(pageNum);
        if (!isCurrent) return;

        const viewport = page.getViewport({ scale });
        setDimensions({ width: viewport.width, height: viewport.height });

        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
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

        if (isCurrent) {
          setRendered(true);
          setRendering(false);
        }
      } catch (err) {
        if (err?.name !== 'RenderingCancelledException') {
          console.error(`Error rendering continuous page ${pageNum}:`, err);
        }
        if (isCurrent) {
          setRendering(false);
        }
      }
    }

    drawPage();

    return () => {
      isCurrent = false;
      if (renderTaskRef.current) {
        renderTaskRef.current.cancel();
      }
    };
  }, [pdfDoc, pageNum, inView, scale]);

  const placeholderHeight = dimensions
    ? `${dimensions.height}px`
    : defaultAspect
    ? `${Math.round(defaultAspect.width * scale * (defaultAspect.height / defaultAspect.width))}px`
    : '850px';

  return (
    <div
      id={`pdf-page-${pageNum}`}
      ref={containerRef}
      className="relative flex flex-col items-center my-4 sm:my-6 transition-all"
      style={{
        minHeight: placeholderHeight,
        width: dimensions ? `${dimensions.width}px` : '100%',
        maxWidth: '100%',
      }}
    >
      {/* Page Card Frame */}
      <div className="relative shadow-2xl rounded-xl overflow-hidden border border-paper-300 dark:border-darkbg-border bg-white transition-shadow hover:shadow-2xl">
        <canvas
          ref={canvasRef}
          className="block select-none pointer-events-none max-w-full h-auto mx-auto"
        />

        {/* Loading Spinner for individual page */}
        {rendering && !rendered && (
          <div className="absolute inset-0 flex flex-col items-center justify-center bg-paper-100/60 dark:bg-darkbg-900/60 backdrop-blur-xs">
            <Loader2 className="w-6 h-6 animate-spin text-ink-700 dark:text-paper-300 mb-2" />
            <span className="text-[11px] font-mono text-ink-600 dark:text-paper-300">Rendering Page {pageNum}...</span>
          </div>
        )}

        {/* Page Corner Label */}
        <div className="absolute bottom-2 right-3 px-2 py-0.5 rounded-full bg-paper-100/80 dark:bg-darkbg-900/80 backdrop-blur-xs text-[9px] font-mono text-ink-500 dark:text-ink-400 border border-paper-300/60 dark:border-darkbg-border select-none pointer-events-none">
          Page {pageNum} of {totalPages}
        </div>
      </div>
    </div>
  );
});

export default function Viewer({ material, user, onBack }) {
  const [pdfDoc, setPdfDoc] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [jumpPageInput, setJumpPageInput] = useState('1');
  const [totalPages, setTotalPages] = useState(0);
  const [scale, setScale] = useState(1.0);
  const [fitMode, setFitMode] = useState(() => (window.innerWidth < 768 ? 'fit-width' : 'fit-page'));
  const [scrollMode, setScrollMode] = useState('continuous'); // 'continuous' (Vertical PDF scroll) | 'single'
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [renderingSinglePage, setRenderingSinglePage] = useState(false);
  const [defaultAspect, setDefaultAspect] = useState(null);

  const singleCanvasRef = useRef(null);
  const viewerContainerRef = useRef(null);
  const scrollContainerRef = useRef(null);
  const singleRenderTaskRef = useRef(null);
  const rawPageViewportRef = useRef(null);

  // Sync fullscreen state
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

  // Sync jump input with current page
  useEffect(() => {
    setJumpPageInput(String(currentPage));
  }, [currentPage]);

  // Load PDF Document
  useEffect(() => {
    let isMounted = true;

    async function loadDocument() {
      try {
        setLoading(true);
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
          // Cloud fallback: load from pre-cached static book asset
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

          // Get first page dimensions to compute default aspect ratio and initial scale
          const page1 = await doc.getPage(1);
          const viewport1 = page1.getViewport({ scale: 1.0 });
          rawPageViewportRef.current = viewport1;
          setDefaultAspect({ width: viewport1.width, height: viewport1.height });

          // Auto calculate initial adaptive scale
          const computedScale = calculateScale(viewport1, fitMode);
          setScale(computedScale);

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

  // Adaptive scale calculator
  const calculateScale = useCallback(
    (pageViewport, mode) => {
      if (!scrollContainerRef.current || !pageViewport) return scale;

      const container = scrollContainerRef.current;
      const isMobile = window.innerWidth < 640;
      const padX = isMobile ? 24 : 64;
      const padY = isMobile ? 24 : 64;

      const availWidth = Math.max(280, container.clientWidth - padX);
      const availHeight = Math.max(280, container.clientHeight - padY);

      if (mode === 'fit-width') {
        const computed = availWidth / pageViewport.width;
        return Math.min(2.5, Math.max(0.35, +computed.toFixed(2)));
      } else if (mode === 'fit-page') {
        const scaleX = availWidth / pageViewport.width;
        const scaleY = availHeight / pageViewport.height;
        const computed = Math.min(scaleX, scaleY);
        return Math.min(2.5, Math.max(0.35, +computed.toFixed(2)));
      }

      return scale;
    },
    [scale]
  );

  // Single Page Render effect (when scrollMode === 'single')
  useEffect(() => {
    if (!pdfDoc || scrollMode !== 'single' || !singleCanvasRef.current) return;

    let isCurrentRender = true;

    async function renderSingle() {
      try {
        setRenderingSinglePage(true);

        if (singleRenderTaskRef.current) {
          singleRenderTaskRef.current.cancel();
        }

        const page = await pdfDoc.getPage(currentPage);
        if (!isCurrentRender) return;

        const unscaledViewport = page.getViewport({ scale: 1.0 });
        rawPageViewportRef.current = unscaledViewport;

        let activeScale = scale;
        if (fitMode === 'fit-width' || fitMode === 'fit-page') {
          activeScale = calculateScale(unscaledViewport, fitMode);
          if (activeScale !== scale) {
            setScale(activeScale);
          }
        }

        const canvas = singleCanvasRef.current;
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
        singleRenderTaskRef.current = renderTask;

        await renderTask.promise;

        if (isCurrentRender) {
          setRenderingSinglePage(false);
        }
      } catch (err) {
        if (err?.name !== 'RenderingCancelledException') {
          console.error('Single page render error:', err);
        }
        if (isCurrentRender) {
          setRenderingSinglePage(false);
        }
      }
    }

    renderSingle();

    return () => {
      isCurrentRender = false;
      if (singleRenderTaskRef.current) {
        singleRenderTaskRef.current.cancel();
      }
    };
  }, [pdfDoc, currentPage, scale, fitMode, scrollMode, calculateScale]);

  // Window resize handler
  useEffect(() => {
    let resizeTimer = null;
    const handleResize = () => {
      if (resizeTimer) clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        if ((fitMode === 'fit-width' || fitMode === 'fit-page') && rawPageViewportRef.current) {
          const newScale = calculateScale(rawPageViewportRef.current, fitMode);
          setScale(newScale);
        }
      }, 150);
    };

    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
      if (resizeTimer) clearTimeout(resizeTimer);
    };
  }, [fitMode, calculateScale]);

  // Scroll to a specific page smoothly in continuous mode
  const scrollToPage = useCallback(
    (targetPage) => {
      const pageIndex = Math.max(1, Math.min(totalPages || 1, targetPage));
      setCurrentPage(pageIndex);

      if (scrollMode === 'continuous') {
        const el = document.getElementById(`pdf-page-${pageIndex}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    },
    [totalPages, scrollMode]
  );

  // Previous and Next page handlers
  const handlePrevPage = useCallback(() => {
    const target = Math.max(1, currentPage - 1);
    scrollToPage(target);
  }, [currentPage, scrollToPage]);

  const handleNextPage = useCallback(() => {
    const target = totalPages > 0 ? Math.min(totalPages, currentPage + 1) : currentPage + 1;
    scrollToPage(target);
  }, [currentPage, totalPages, scrollToPage]);

  // Direct Page Jump Form Submission
  const handleJumpSubmit = (e) => {
    e.preventDefault();
    const parsed = parseInt(jumpPageInput, 10);
    if (!isNaN(parsed) && parsed >= 1 && parsed <= totalPages) {
      scrollToPage(parsed);
    } else {
      setJumpPageInput(String(currentPage));
    }
  };

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

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) {
        return;
      }

      // Next page keys
      if (
        e.key === 'ArrowRight' ||
        e.key === 'PageDown' ||
        (e.key === ' ' && !e.shiftKey) ||
        e.key === 'n' ||
        e.key === 'N'
      ) {
        e.preventDefault();
        handleNextPage();
      }
      // Previous page keys
      else if (
        e.key === 'ArrowLeft' ||
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
        scrollToPage(1);
      } else if (e.key === 'End') {
        e.preventDefault();
        if (totalPages > 0) scrollToPage(totalPages);
      }
      // Zoom
      else if (e.key === '+' || e.key === '=') {
        e.preventDefault();
        setFitMode('custom');
        setScale((s) => Math.min(2.5, +(s + 0.15).toFixed(2)));
      } else if (e.key === '-' || e.key === '_') {
        e.preventDefault();
        setFitMode('custom');
        setScale((s) => Math.max(0.4, +(s - 0.15).toFixed(2)));
      } else if (e.key === '0') {
        e.preventDefault();
        setFitMode('fit-width');
        if (rawPageViewportRef.current) {
          setScale(calculateScale(rawPageViewportRef.current, 'fit-width'));
        }
      }
      // Fullscreen
      else if (e.key === 'f' || e.key === 'F') {
        if (!e.ctrlKey && !e.metaKey) {
          e.preventDefault();
          toggleFullscreen();
        }
      }
      // Escape
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
  }, [handleNextPage, handlePrevPage, scrollToPage, totalPages, toggleFullscreen, onBack, calculateScale]);

  const handleZoomIn = () => {
    setFitMode('custom');
    setScale((s) => Math.min(2.5, +(s + 0.15).toFixed(2)));
  };

  const handleZoomOut = () => {
    setFitMode('custom');
    setScale((s) => Math.max(0.4, +(s - 0.15).toFixed(2)));
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

  const handlePageVisibleCallback = useCallback((pageNum) => {
    setCurrentPage(pageNum);
  }, []);

  return (
    <div
      ref={viewerContainerRef}
      className="flex flex-col h-screen bg-[#EFECE4] dark:bg-darkbg-950 text-ink-900 dark:text-paper-100 select-none overflow-hidden transition-colors relative"
    >
      {/* 1. TOP HEADER TOOLBAR */}
      <header className="h-16 bg-paper-50/95 dark:bg-darkbg-900/95 border-b border-paper-300 dark:border-darkbg-border px-3 sm:px-6 flex items-center justify-between z-30 shrink-0 backdrop-blur-md gap-2">
        {/* Left: Back to Archives + Book Title */}
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
              <h2 className="text-xs sm:text-sm font-bold font-sans text-ink-900 dark:text-paper-50 truncate max-w-[120px] sm:max-w-[200px] md:max-w-md">
                {material.title}
              </h2>
              <span className="text-[10px] font-mono text-ink-400 dark:text-ink-400 truncate">
                {material.courseCode} • {material.category}
              </span>
            </div>
          </div>
        </div>

        {/* Center: Back / Forth Navigation Buttons & Page Jumper */}
        <div className="flex items-center gap-1 sm:gap-1.5 bg-paper-200/90 dark:bg-darkbg-800 px-2 py-1 rounded-full border border-paper-300 dark:border-darkbg-border shadow-xs shrink-0">
          <button
            onClick={handlePrevPage}
            disabled={currentPage <= 1 || loading}
            className="p-1 sm:px-2 sm:py-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 transition flex items-center gap-1 text-xs font-mono font-bold text-ink-800 dark:text-paper-100"
            title="Previous Page (← / PageUp)"
          >
            <ChevronLeft className="w-4 h-4" />
            <span className="hidden md:inline text-[11px]">Prev</span>
          </button>

          {/* Page Jumper Input */}
          <form onSubmit={handleJumpSubmit} className="flex items-center gap-1 font-mono text-xs font-bold px-1">
            <input
              type="text"
              value={jumpPageInput}
              onChange={(e) => setJumpPageInput(e.target.value)}
              onBlur={() => setJumpPageInput(String(currentPage))}
              className="w-8 sm:w-10 text-center py-0.5 px-1 bg-white dark:bg-darkbg-900 rounded border border-paper-300 dark:border-darkbg-border text-ink-900 dark:text-paper-50 text-[11px] font-mono focus:outline-none focus:ring-1 focus:ring-ink-900 dark:focus:ring-paper-50"
              title="Type page number and press Enter to jump"
            />
            <span className="text-paper-400 dark:text-ink-500 font-normal">/</span>
            <span className="text-ink-800 dark:text-paper-200 text-[11px]">{totalPages || '--'}</span>
          </form>

          <button
            onClick={handleNextPage}
            disabled={currentPage >= totalPages || loading}
            className="p-1 sm:px-2 sm:py-1 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 transition flex items-center gap-1 text-xs font-mono font-bold text-ink-800 dark:text-paper-100"
            title="Next Page (→ / PageDown / Space)"
          >
            <span className="hidden md:inline text-[11px]">Next</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>

        {/* Right Controls: Scroll Mode Switcher + Fit + Zoom + Fullscreen */}
        <div className="flex items-center gap-1 sm:gap-2 shrink-0">
          {/* Continuous Scroll vs Single Page Mode Toggle */}
          <div className="flex items-center bg-paper-200/90 dark:bg-darkbg-800 rounded-full p-0.5 border border-paper-300 dark:border-darkbg-border">
            <button
              onClick={() => setScrollMode('continuous')}
              className={`px-2.5 py-1 rounded-full text-[10px] font-mono font-semibold transition flex items-center gap-1 ${
                scrollMode === 'continuous'
                  ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 shadow-xs'
                  : 'text-ink-700 dark:text-paper-300 hover:bg-paper-300 dark:hover:bg-darkbg-700'
              }`}
              title="Continuous Vertical Scrolling (Standard PDF Mode)"
            >
              <Scroll className="w-3 h-3" />
              <span className="hidden lg:inline">Scroll Mode</span>
            </button>
            <button
              onClick={() => setScrollMode('single')}
              className={`px-2.5 py-1 rounded-full text-[10px] font-mono font-semibold transition flex items-center gap-1 ${
                scrollMode === 'single'
                  ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 shadow-xs'
                  : 'text-ink-700 dark:text-paper-300 hover:bg-paper-300 dark:hover:bg-darkbg-700'
              }`}
              title="Single Page Mode"
            >
              <FileText className="w-3 h-3" />
              <span className="hidden lg:inline">Page Mode</span>
            </button>
          </div>

          {/* Adaptive Fit Modes */}
          <div className="hidden md:flex items-center gap-0.5 bg-paper-200/90 dark:bg-darkbg-800 rounded-full p-0.5 border border-paper-300 dark:border-darkbg-border">
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
              <span>Width</span>
            </button>
            <button
              onClick={handleSetFitPage}
              className={`px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold transition flex items-center gap-1 ${
                fitMode === 'fit-page'
                  ? 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                  : 'text-ink-700 dark:text-paper-300 hover:bg-paper-300 dark:hover:bg-darkbg-700'
              }`}
              title="Fit Page"
            >
              <Maximize className="w-3 h-3" />
              <span>Page</span>
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
            <span className="text-[10px] font-mono px-1 sm:px-1.5 text-ink-600 dark:text-paper-300 font-bold min-w-[34px] text-center">
              {Math.round(scale * 100)}%
            </span>
            <button
              onClick={handleZoomIn}
              className="p-1 hover:bg-paper-300 dark:hover:bg-darkbg-700 rounded-full text-ink-700 dark:text-paper-200 transition"
              title="Zoom In (+ key)"
            >
              <ZoomIn className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Fullscreen button */}
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
                <span className="hidden sm:inline">EXIT</span>
              </>
            ) : (
              <Maximize2 className="w-3.5 h-3.5" />
            )}
          </button>
        </div>
      </header>

      {/* Floating Exit Button (Visible in Fullscreen) */}
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
            title="Exit Fullscreen Mode"
          >
            <X className="w-4 h-4" />
            <span>Exit Fullscreen</span>
          </button>
        </div>
      )}

      {/* 2. MAIN READING DOCUMENT AREA */}
      <main
        ref={scrollContainerRef}
        className="flex-1 overflow-y-auto overflow-x-auto relative p-2 sm:p-6 md:p-8 bg-[#E5E1D5] dark:bg-darkbg-900 scroll-smooth"
      >
        {loading && (
          <div className="h-full flex flex-col items-center justify-center gap-3 text-ink-600 dark:text-ink-400 min-h-[400px]">
            <Loader2 className="w-8 h-8 animate-spin text-ink-900 dark:text-paper-100" />
            <p className="text-xs font-mono tracking-widest uppercase">Opening Archival Volume...</p>
          </div>
        )}

        {error && (
          <div className="h-full flex items-center justify-center min-h-[400px]">
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
          </div>
        )}

        {!loading && !error && (
          <>
            {/* CONTINUOUS VERTICAL SCROLL MODE (Like PDF Viewer) */}
            {scrollMode === 'continuous' && (
              <div className="flex flex-col items-center min-w-full pb-28">
                {Array.from({ length: totalPages }, (_, i) => i + 1).map((pageNum) => (
                  <ContinuousPageItem
                    key={pageNum}
                    pageNum={pageNum}
                    totalPages={totalPages}
                    pdfDoc={pdfDoc}
                    scale={scale}
                    defaultAspect={defaultAspect}
                    onVisible={handlePageVisibleCallback}
                    user={user}
                  />
                ))}
              </div>
            )}

            {/* SINGLE PAGE VIEW MODE */}
            {scrollMode === 'single' && (
              <div className="flex items-center justify-center min-h-full pb-20">
                <div className="relative shadow-2xl rounded-xl overflow-hidden border border-paper-300 dark:border-darkbg-border bg-white my-auto max-w-full">
                  <canvas
                    ref={singleCanvasRef}
                    className="block select-none pointer-events-none transition-transform max-w-full h-auto mx-auto"
                  />

                  {renderingSinglePage && (
                    <div className="absolute top-3 right-3 bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-md px-3 py-1 rounded-full text-[10px] font-mono text-ink-700 dark:text-paper-200 flex items-center gap-1.5 border border-paper-300 dark:border-darkbg-border shadow-xs">
                      <Loader2 className="w-3 h-3 animate-spin text-ink-900 dark:text-paper-100" />
                      <span>Syncing Page...</span>
                    </div>
                  )}

                  <div className="absolute bottom-2 right-3 px-2 py-0.5 rounded-full bg-paper-100/80 dark:bg-darkbg-900/80 backdrop-blur-xs text-[9px] font-mono text-ink-500 dark:text-ink-400 border border-paper-300/60 dark:border-darkbg-border select-none pointer-events-none">
                    Page {currentPage} of {totalPages}
                  </div>
                </div>
              </div>
            )}
          </>
        )}
      </main>

      {/* 3. FLOATING SMART DOCK (Back & Forth Navigation Buttons) */}
      {!loading && !error && (
        <div className="fixed bottom-12 left-1/2 -translate-x-1/2 z-40 flex items-center gap-1.5 sm:gap-2 bg-paper-50/95 dark:bg-darkbg-850/95 backdrop-blur-md px-3 py-2 rounded-full border border-paper-300 dark:border-darkbg-border shadow-floating animate-in fade-in slide-in-from-bottom-4 duration-300">
          {/* Scroll to Top */}
          <button
            onClick={() => scrollToPage(1)}
            disabled={currentPage <= 1}
            className="p-1.5 hover:bg-paper-200 dark:hover:bg-darkbg-700 disabled:opacity-25 rounded-full text-ink-700 dark:text-paper-300 transition"
            title="Jump to Beginning (Home key)"
          >
            <ArrowUp className="w-3.5 h-3.5" />
          </button>

          <div className="h-4 w-px bg-paper-300 dark:bg-darkbg-border"></div>

          {/* Previous Page Button */}
          <button
            onClick={handlePrevPage}
            disabled={currentPage <= 1}
            className="flex items-center gap-1 px-3 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-750 hover:bg-paper-300 dark:hover:bg-darkbg-700 disabled:opacity-30 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition shadow-xs"
            title="Previous Page (←)"
          >
            <ChevronLeft className="w-4 h-4" />
            <span className="hidden sm:inline">Back</span>
          </button>

          {/* Page Pill Indicator */}
          <div className="flex items-center gap-1 px-2.5 py-1 bg-white dark:bg-darkbg-900 rounded-full border border-paper-300 dark:border-darkbg-border text-xs font-mono font-bold text-ink-900 dark:text-paper-50">
            <span>{currentPage}</span>
            <span className="text-paper-400 dark:text-ink-500 font-normal">/</span>
            <span>{totalPages || '--'}</span>
          </div>

          {/* Next Page Button */}
          <button
            onClick={handleNextPage}
            disabled={currentPage >= totalPages}
            className="flex items-center gap-1 px-3 py-1.5 rounded-full bg-ink-900 dark:bg-paper-100 text-paper-50 dark:text-ink-900 hover:bg-ink-800 dark:hover:bg-paper-200 disabled:opacity-30 text-xs font-mono font-bold transition shadow-xs"
            title="Next Page (→ / Space)"
          >
            <span className="hidden sm:inline">Next</span>
            <ChevronRight className="w-4 h-4" />
          </button>

          <div className="h-4 w-px bg-paper-300 dark:bg-darkbg-border"></div>

          {/* Scroll to Bottom */}
          <button
            onClick={() => scrollToPage(totalPages)}
            disabled={currentPage >= totalPages}
            className="p-1.5 hover:bg-paper-200 dark:hover:bg-darkbg-700 disabled:opacity-25 rounded-full text-ink-700 dark:text-paper-300 transition"
            title="Jump to End (End key)"
          >
            <ArrowDown className="w-3.5 h-3.5" />
          </button>
        </div>
      )}

      {/* 4. PERFORATED ARCHIVAL FOOTER */}
      <footer className="h-8 bg-paper-50 dark:bg-darkbg-900 border-t border-paper-300 dark:border-darkbg-border px-4 sm:px-6 flex items-center justify-between text-[10px] text-ink-500 dark:text-ink-400 font-mono shrink-0 z-20">
        <div className="flex items-center gap-2 sm:gap-3 truncate">
          <span className="font-bold text-ink-800 dark:text-paper-200 truncate">EDU NETWORK ARCHIVES</span>
          <span>•</span>
          <span className="truncate">ACCOUNT: {user?.email}</span>
        </div>
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          <span className="hidden sm:inline">CONTINUOUS PDF SCROLL ENABLED</span>
          <span className="hidden sm:inline">•</span>
          <span className="barcode text-[10px]">|||| ||| |||||</span>
        </div>
      </footer>
    </div>
  );
}
