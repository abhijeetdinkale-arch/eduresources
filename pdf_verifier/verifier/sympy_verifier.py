"""
SymPy Verifier
==============
Uses SymPy (symbolic math) to algebraically verify equations and inequalities.

Attempts to:
1. Parse both sides of an equation/inequality
2. Simplify the difference and check if it equals zero (for equations)
3. Check numeric evaluations for numeric_claim types
4. Verify known identities

Returns:
    {
        "status": "correct" | "error" | "uncertain",
        "explanation": str
    }
"""

import re
from sympy import (
    sympify, simplify, expand, trigsimp, nsimplify, N, pi, E, oo,
    symbols, sqrt, sin, cos, tan, log, exp, Abs, Rational,
    SympifyError, latex,
)
from sympy import zoo  # complex infinity
from typing import Optional, Tuple


# Mapping of common text representations to SymPy equivalents
_TEXT_REPLACEMENTS = [
    # Greek letters (full names)
    (r"\bpi\b", "pi"),
    (r"\bPI\b", "pi"),
    (r"π", "pi"),
    (r"∞", "oo"),
    # Superscript digits
    (r"²", "**2"),
    (r"³", "**3"),
    (r"⁴", "**4"),
    (r"⁵", "**5"),
    (r"⁶", "**6"),
    (r"⁷", "**7"),
    (r"⁸", "**8"),
    (r"⁹", "**9"),
    (r"¹", "**1"),
    # Implicit multiplication: 2x → 2*x
    (r"(\d)([a-zA-Z(])", r"\1*\2"),
    # sqrt symbol
    (r"√\(([^)]+)\)", r"sqrt(\1)"),
    (r"√(\w+)", r"sqrt(\1)"),
    # Dot notation for multiplication
    (r"·", "*"),
    (r"×", "*"),
    # Approximation → equality for numeric checks
    (r"≈", "="),
    # Remove trailing punctuation
    (r"[.,;:]$", ""),
]


def _preprocess(expr: str) -> str:
    """Clean and normalise an expression string for SymPy parsing."""
    expr = expr.strip()
    for pattern, replacement in _TEXT_REPLACEMENTS:
        expr = re.sub(pattern, replacement, expr)
    return expr


def _split_on_equals(text: str) -> Optional[Tuple[str, str]]:
    """Split 'LHS = RHS' into (lhs, rhs). Returns None if not an equation."""
    # Handle ≠, ≤, ≥ — not equalities, skip
    if re.search(r"[≠≤≥<>]", text):
        return None
    parts = re.split(r"(?<![<>!])=(?!=)", text, maxsplit=1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return None


def _try_sympify(expr_str: str):
    """Try to parse expr_str into a SymPy expression. Returns None on failure."""
    try:
        return sympify(expr_str, evaluate=True)
    except (SympifyError, SyntaxError, TypeError, ValueError):
        return None


def verify_equation(lhs_str: str, rhs_str: str) -> dict:
    """Algebraically verify LHS = RHS."""
    lhs_proc = _preprocess(lhs_str)
    rhs_proc = _preprocess(rhs_str)

    lhs = _try_sympify(lhs_proc)
    rhs = _try_sympify(rhs_proc)

    if lhs is None or rhs is None:
        return {
            "status": "uncertain",
            "explanation": f"Could not parse expression for algebraic check: '{lhs_str} = {rhs_str}'",
        }

    try:
        diff = simplify(lhs - rhs)
        if diff == 0:
            return {"status": "correct", "explanation": "Algebraically verified: LHS − RHS = 0"}

        # Try trig simplification
        diff_trig = trigsimp(lhs - rhs)
        if diff_trig == 0:
            return {"status": "correct", "explanation": "Verified via trig simplification: LHS − RHS = 0"}

        # Try numeric evaluation at a random point
        try:
            diff_numeric = float(N(diff, subs={s: 1.23456 for s in diff.free_symbols}))
            if abs(diff_numeric) < 1e-9:
                return {
                    "status": "correct",
                    "explanation": "Numerically verified at test point (symbolic simplification inconclusive)",
                }
            else:
                return {
                    "status": "error",
                    "explanation": (
                        f"Equation appears incorrect. "
                        f"LHS − RHS evaluates to {diff_numeric:.6g} (should be 0). "
                        f"Simplified difference: {diff}"
                    ),
                }
        except Exception:
            return {
                "status": "uncertain",
                "explanation": f"Could not fully verify. Simplified difference: {diff}",
            }
    except Exception as e:
        return {
            "status": "uncertain",
            "explanation": f"Verification error: {e}",
        }


def verify_numeric_claim(text: str) -> dict:
    """Verify numeric assertions like 'sin(30) = 0.5' or 'pi = 3.14'."""
    parts = _split_on_equals(text)
    if not parts:
        return {"status": "uncertain", "explanation": "Could not split into LHS = RHS"}

    lhs_str, rhs_str = parts
    return verify_equation(lhs_str, rhs_str)


class SympyVerifier:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def verify(self, content: str) -> dict:
        """
        Verify a math string. Returns {"status": ..., "explanation": ...}.
        status is one of: "correct", "error", "uncertain"
        """
        # Try to split on '='
        parts = _split_on_equals(content)
        if parts:
            lhs, rhs = parts
            result = verify_equation(lhs, rhs)
        else:
            # Inequality or unparseable — mark uncertain for now
            result = {
                "status": "uncertain",
                "explanation": "Inequality or unparseable expression — deferred to AI verifier",
            }

        if self.verbose:
            print(f"      [SymPy] '{content[:60]}...' → {result['status']}")

        return result
