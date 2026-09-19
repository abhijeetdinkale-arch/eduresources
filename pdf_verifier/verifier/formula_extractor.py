"""
Formula Extractor
=================
Analyses each line of extracted text and categorizes it as:
- equation       : e.g.  E = mc²,  x² + y² = z²
- inequality     : e.g.  x > 0,  a ≤ b
- identity       : known mathematical identities
- numeric_claim  : e.g.  "sin(30°) = 0.5",  "π ≈ 3.14159"
- factual_claim  : text statements that assert facts
- definition     : "A vector is ...",  "Let f(x) = ..."
- general_text   : everything else

Items are added to the page's "items" list.
"""

import re
from typing import Optional


# Regex patterns for detecting math content
EQUATION_PATTERN = re.compile(
    r"""
    (?:
        [a-zA-Zα-ωΑ-Ω₀-₉⁰-⁹]+   # variable or Greek letter
        \s*[\^_]?\s*               # optional superscript/subscript
    )?
    [\w\s\(\)\[\]{}^_,.]*         # expression parts
    \s*[=≡≈≠≤≥<>∝∞±∓√∫∑∏]\s*    # operator
    [\w\s\(\)\[\]{}^_,.+\-*/\\°]+  # right-hand side
    """,
    re.VERBOSE | re.UNICODE,
)

# Simpler pattern: line contains an '=' with math-like content on both sides
SIMPLE_EQ_PATTERN = re.compile(
    r"[\w\d\(\)\[\]\.]+\s*=\s*[\w\d\(\)\[\]\.\+\-\*/\^]+"
)

# Inequality markers
INEQUALITY_MARKERS = re.compile(r"[≤≥<>≠]|!=|<=|>=")

# Numeric assertion: something = number
NUMERIC_CLAIM_PATTERN = re.compile(
    r"[\w\(\)]+\s*[=≈]\s*[-+]?\d+[\.,]?\d*"
)

# Known math function names for scoring
MATH_KEYWORDS = {
    "sin", "cos", "tan", "log", "ln", "exp", "sqrt", "lim",
    "derivative", "integral", "sum", "product", "matrix", "vector",
    "eigenvalue", "determinant", "divergence", "gradient", "curl",
    "dx", "dy", "dz", "dt", "partial",
}

# Factual claim cue words
FACTUAL_CUES = re.compile(
    r"\b(is|are|was|were|equals|equal to|defined as|known as|called|"
    r"represents?|denotes?|means?|equivalent to|given by|expressed as)\b",
    re.IGNORECASE,
)

# Definition cue words
DEFINITION_CUES = re.compile(
    r"\b(let|define|definition|denote|suppose|assume|given|consider|"
    r"where|such that|we say|we call|notation)\b",
    re.IGNORECASE,
)


def _math_score(text: str) -> int:
    """Score how 'mathy' a line is (higher = more mathematical)."""
    score = 0
    lower = text.lower()
    # Special characters
    for ch in "=∫∑∏√±∓≤≥≠≈≡∞∝∂∇∆":
        score += text.count(ch) * 3
    # Superscripts / subscripts
    score += len(re.findall(r"[\^_]\d", text)) * 2
    # LaTeX markers
    score += text.count("\\") * 2
    # Parentheses (common in math)
    score += (text.count("(") + text.count(")"))
    # Known math keywords
    for kw in MATH_KEYWORDS:
        if kw in lower:
            score += 2
    return score


def _classify_line(text: str) -> Optional[str]:
    """Classify a text line into a content type. Returns None if not verifiable."""
    if len(text) < 3:
        return None

    score = _math_score(text)

    # Check for explicit equation
    if SIMPLE_EQ_PATTERN.search(text) and score >= 3:
        if INEQUALITY_MARKERS.search(text):
            return "inequality"
        return "equation"

    # Inequality without '='
    if INEQUALITY_MARKERS.search(text) and score >= 2:
        return "inequality"

    # Numeric claim
    if NUMERIC_CLAIM_PATTERN.search(text):
        return "numeric_claim"

    # Definition
    if DEFINITION_CUES.search(text):
        return "definition"

    # Factual claim (sentence with assertion)
    if FACTUAL_CUES.search(text) and len(text.split()) >= 4:
        return "factual_claim"

    # Mathy lines that didn't fit above
    if score >= 5:
        return "equation"

    return "general_text"


class FormulaExtractor:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def process_page(self, page: dict) -> None:
        """
        Processes all lines in a page dict, classifying and building the items list.
        Modifies page in-place.
        """
        items = []
        for line in page["lines"]:
            text = line["text"]
            content_type = _classify_line(text)
            if content_type is None:
                continue

            items.append({
                "line_number": line["line_number"],
                "page_line": line["page_line"],
                "content": text,
                "type": content_type,
            })

        page["items"] = items

        if self.verbose:
            print(f"      Page {page['page_number']}: {len(items)} verifiable items")
