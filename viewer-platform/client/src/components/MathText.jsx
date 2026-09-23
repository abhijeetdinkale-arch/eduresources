import React from 'react';

/**
 * Lightweight mathematical renderer that guarantees 100% text contrast.
 * Inherits text color (text-current) so on black bg it is pure white, and on white bg it is pure black.
 */
export default function MathText({ text, className = '' }) {
  if (!text) return null;

  const formatMathString = (str) => {
    if (typeof str !== 'string') return str;

    let formatted = str
      .replace(/\\lambda/g, 'λ')
      .replace(/\\pi/g, 'π')
      .replace(/\\theta/g, 'θ')
      .replace(/\\alpha/g, 'α')
      .replace(/\\beta/g, 'β')
      .replace(/\\infty/g, '∞')
      .replace(/\\to/g, '→')
      .replace(/\\cdot/g, '·')
      .replace(/\\times/g, '×')
      .replace(/\\ne/g, '≠')
      .replace(/\\le/g, '≤')
      .replace(/\\ge/g, '≥')
      .replace(/\\pm/g, '±')
      .replace(/\\in/g, '∈')
      .replace(/\\int/g, '∫')
      .replace(/\\partial/g, '∂');

    const parts = formatted.split(/(\$\$[\s\S]*?\$\$|\$[^$]+?\$)/g);

    return parts.map((part, idx) => {
      if (part.startsWith('$$') && part.endsWith('$$')) {
        const mathContent = part.slice(2, -2).trim();
        return (
          <div
            key={idx}
            className="my-2 py-1.5 px-3 rounded-lg text-center font-mono text-sm overflow-x-auto bg-black/5 dark:bg-white/10 text-current font-bold"
          >
            {renderMathExpression(mathContent)}
          </div>
        );
      } else if (part.startsWith('$') && part.endsWith('$')) {
        const mathContent = part.slice(1, -1).trim();
        return (
          <span
            key={idx}
            className="inline-block font-mono text-sm px-1.5 py-0.5 rounded bg-black/5 dark:bg-white/10 text-current font-bold tracking-tight mx-0.5"
          >
            {renderMathExpression(mathContent)}
          </span>
        );
      }

      return <span key={idx} className="text-current">{renderMathExpression(part)}</span>;
    });
  };

  const renderMathExpression = (expr) => {
    if (expr.includes('[[') || (expr.includes('[') && expr.includes(']') && expr.split('\n').length > 1)) {
      return renderMatrixBlock(expr);
    }

    return (
      <span className="inline leading-relaxed text-current">
        {expr.split('\n').map((line, lIdx) => (
          <React.Fragment key={lIdx}>
            {lIdx > 0 && <br />}
            {line}
          </React.Fragment>
        ))}
      </span>
    );
  };

  const renderMatrixBlock = (text) => {
    return <span className="font-mono whitespace-pre inline-block text-current font-bold">{text}</span>;
  };

  return <div className={`font-sans text-current ${className}`}>{formatMathString(text)}</div>;
}
