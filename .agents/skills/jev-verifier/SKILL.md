---
name: jev-verifier
description: Run ultra-fast editorial, mathematical, and syllabus QA checks on LaTeX books, chapters, and question banks using TypeSafe Jev AI.
---

# Jev Book & Question Bank Verification Skill

This skill allows Antigravity to run high-speed, probabilistic quality checks on study guides, textbooks, and multiple-choice questions (MCQs) before releasing or compiling PDFs.

## When to Use This Skill
- After generating or editing a new LaTeX chapter (e.g. in `Physics/`, `INT335/`, `CSE111/`, etc.).
- When assembling a new Question Bank or Formula Sheet to ensure all MCQs have valid single-choice keys and clear explanations.
- When validating that derivations contain no skipped steps and symbols have SI units.

## How to Run Verification

### 1. Verify a LaTeX Chapter
To verify all sections of a chapter:
```bash
python pdf_verifier/verify_book_jev.py --file Physics_Question_Bank/main.tex
```

### 2. Verify a Quick Text Snippet / Derivation
```bash
python pdf_verifier/verify_book_jev.py --text "Derive the Poynting Theorem: S = E x H..."
```

## Interpreting Jev Output
- **`is_academically_sound` (`noul`)**: Must evaluate to `true`. If `false`, inspect the theory for factual physics/engineering errors.
- **`symbols_and_units_defined` (`noul`)**: Must evaluate to `true`. If `false`, add a symbol definition block with SI units (e.g., `where $\mathbf{E}$ is in $[\text{V/m}]$`).
- **`algebraic_rigor` (`score`)**: Should be rated high. If intermediate algebraic steps were omitted, expand the step-by-step math.
