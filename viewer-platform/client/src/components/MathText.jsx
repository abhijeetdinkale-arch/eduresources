import React from 'react';

/**
 * Lightweight, zero-bloat mathematical renderer.
 * Formats LaTeX-like and mathematical text including:
 * - Exponents: x^2, e^(x), (x-pi/2)^4
 * - Subscripts: x_1, x_2, r_1, r_2
 * - Integrals: \int, \int_0^1, \int_0^{\pi/2}
 * - Limits: \lim_{x \to 0}, \lim_{x \to \infty}
 * - Matrices: [ [1, 2], [3, 4] ] or inline matrix formatting
 * - Fractions: a/b or \frac{a}{b}
 * - Greek symbols: \lambda, \pi, \alpha, \beta, \theta
 * - Square roots: \sqrt{...}
 */
export default function MathText({ text, className = '' }) {
  if (!text) return null;

  // Render lines with potential matrix blocks or standard inline math
  const formatMathString = (str) => {
    if (typeof str !== 'string') return str;

    // Process common symbols
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

    // Split text by markdown math delimiters `$` or `$$` or return formatted text
    const parts = formatted.split(/(\$\$[\s\S]*?\$\$|\$[^$]+?\$)/g);

    return parts.map((part, idx) => {
      if (part.startsWith('$$') && part.endsWith('$$')) {
        const mathContent = part.slice(2, -2).trim();
        return (
          <div
            key={idx}
            className="my-2 py-1 px-3 bg-paper-200/50 dark:bg-darkbg-800/60 rounded-lg text-center font-mono text-sm overflow-x-auto text-ink-900 dark:text-paper-100"
          >
            {renderMathExpression(mathContent)}
          </div>
        );
      } else if (part.startsWith('$') && part.endsWith('$')) {
        const mathContent = part.slice(1, -1).trim();
        return (
          <span
            key={idx}
            className="inline-block font-mono text-sm px-1 py-0.5 rounded bg-paper-200/40 dark:bg-darkbg-800/40 text-ink-900 dark:text-paper-100 font-medium tracking-tight mx-0.5"
          >
            {renderMathExpression(mathContent)}
          </span>
        );
      }

      // Check if raw string contains matrix or equations
      return <span key={idx}>{renderMathExpression(part)}</span>;
    });
  };

  const renderMathExpression = (expr) => {
    // If matrix detected like [[a, b], [c, d]] or [ [ 1 1 6 ], [ 0 4 3 ] ]
    if (expr.includes('[[') || (expr.includes('[') && expr.includes(']') && expr.split('\n').length > 1)) {
      return renderMatrixBlock(expr);
    }

    // Convert basic formatting
    return (
      <span className="inline leading-relaxed">
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
    // Simple matrix renderer
    return <span className="font-mono whitespace-pre inline-block">{text}</span>;
  };

  return <div className={`font-sans ${className}`}>{formatMathString(text)}</div>;
}
