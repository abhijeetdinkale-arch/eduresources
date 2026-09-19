# PDF Book Verifier

Verifies **every line, formula, and statement** in a PDF book and produces a colour-coded PDF report highlighting every error and inconsistency found.

## Features

- **Mathematical verification** via [SymPy](https://www.sympy.org) — algebraically checks equations, identities, and numeric claims
- **AI verification** via [Gemini API](https://ai.google.dev) — verifies factual claims, definitions, and formulas that can't be algebraically parsed
- **PDF report output** — colour-coded per-page breakdown of every verified item
- **Offline mode** — works without a Gemini API key using SymPy only
- **Page range support** — verify just a chapter at a time

## Installation

```bash
cd pdf_verifier
pip install -r requirements.txt
```

## Usage

### Full verification (AI + SymPy):
```bash
python main.py --input your_book.pdf --output report.pdf --gemini-key YOUR_GEMINI_API_KEY
```

### Offline mode (SymPy only, no API key needed):
```bash
python main.py --input your_book.pdf --output report.pdf --skip-ai
```

### Verify only specific pages:
```bash
python main.py --input your_book.pdf --output report.pdf --pages 1-50 --gemini-key YOUR_KEY
```

### Verbose mode:
```bash
python main.py --input your_book.pdf --output report.pdf --gemini-key YOUR_KEY --verbose
```

## Getting a Gemini API Key

1. Go to [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Click **Create API Key**
3. Copy the key and use it with `--gemini-key`

Or set the environment variable once:
```bash
export GEMINI_API_KEY="your_key_here"
python main.py --input book.pdf --output report.pdf
```

## Report Layout

The output PDF contains:

| Section | Description |
|---------|-------------|
| **Cover Page** | Source file, date, and summary stats (total, correct, errors, uncertain) |
| **Error Summary** | Quick index of all errors found with page/line references |
| **Per-page Detail** | Every verified item with status badge, type label, and explanation |

### Status Codes

| Badge | Meaning |
|-------|---------|
| 🟢 **CORRECT** | Verified as mathematically or factually correct |
| 🔴 **ERROR** | Verified as incorrect — explanation provided |
| 🟡 **UNCERTAIN** | Could not verify — manual review recommended |

## Project Structure

```
pdf_verifier/
├── main.py                  # CLI entry point
├── requirements.txt
├── verifier/
│   ├── pdf_parser.py        # Extracts text from PDF (PyMuPDF)
│   ├── formula_extractor.py # Classifies lines (equation, claim, definition, etc.)
│   ├── sympy_verifier.py    # Algebraic/symbolic math verification
│   ├── ai_verifier.py       # Gemini AI verification (batched)
│   └── report_generator.py  # Generates the PDF report (fpdf2)
```

## Content Types Detected

| Type | Example |
|------|---------|
| `equation` | `E = mc²`, `x² + y² = z²` |
| `inequality` | `x > 0`, `a ≤ b` |
| `identity` | `sin²θ + cos²θ = 1` |
| `numeric_claim` | `sin(30°) = 0.5`, `π ≈ 3.14159` |
| `factual_claim` | "The boiling point of water is 100°C" |
| `definition` | "Let f(x) = ...", "A matrix is ..." |
| `general_text` | All other text (sent to AI if enabled) |
