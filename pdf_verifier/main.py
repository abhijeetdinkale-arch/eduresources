"""
PDF Book Verifier
=================
Verifies every line, formula, and statement in a PDF book.
Outputs a detailed PDF report highlighting all errors and inconsistencies.

Usage:
    python main.py --input textbook.pdf --output report.pdf --gemini-key YOUR_KEY
    python main.py --input textbook.pdf --output report.pdf --skip-ai
    python main.py --input textbook.pdf --output report.pdf --pages 1-50 --gemini-key YOUR_KEY
"""

import argparse
import sys
import os
from typing import Optional, Tuple
from tqdm import tqdm

from verifier.pdf_parser import PDFParser
from verifier.formula_extractor import FormulaExtractor
from verifier.sympy_verifier import SympyVerifier
from verifier.ai_verifier import AIVerifier
from verifier.report_generator import ReportGenerator


def parse_page_range(page_str: str) -> Optional[Tuple[int, int]]:
    """Parse a page range string like '1-50' into (start, end) tuple (1-indexed)."""
    if not page_str:
        return None
    parts = page_str.split("-")
    if len(parts) == 2:
        return int(parts[0]), int(parts[1])
    elif len(parts) == 1:
        p = int(parts[0])
        return p, p
    raise ValueError(f"Invalid page range: {page_str}")


def main():
    parser = argparse.ArgumentParser(
        description="PDF Book Verifier — Checks every statement and formula in a PDF book."
    )
    parser.add_argument("--input", "-i", required=True, help="Path to the input PDF file")
    parser.add_argument("--output", "-o", default="verification_report.pdf",
                        help="Path for the output PDF report (default: verification_report.pdf)")
    parser.add_argument("--gemini-key", "-k", default=None,
                        help="Gemini API key for AI-based verification (or set GEMINI_API_KEY env var)")
    parser.add_argument("--skip-ai", action="store_true",
                        help="Skip AI verification (offline mode — SymPy only)")
    parser.add_argument("--pages", "-p", default=None,
                        help="Page range to verify, e.g. '1-50' (default: all pages)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show detailed progress output")
    args = parser.parse_args()

    # Validate input
    if not os.path.isfile(args.input):
        print(f"[ERROR] Input file not found: {args.input}")
        sys.exit(1)

    # Resolve Gemini API key
    gemini_key = args.gemini_key or os.environ.get("GEMINI_API_KEY")
    use_ai = not args.skip_ai
    if use_ai and not gemini_key:
        print("[WARNING] No Gemini API key provided. Falling back to SymPy-only verification.")
        print("          Set --gemini-key or GEMINI_API_KEY environment variable to enable AI checks.")
        use_ai = False

    # Parse page range
    page_range = None
    if args.pages:
        try:
            page_range = parse_page_range(args.pages)
        except ValueError as e:
            print(f"[ERROR] {e}")
            sys.exit(1)

    print("=" * 60)
    print("  PDF BOOK VERIFIER")
    print("=" * 60)
    print(f"  Input  : {args.input}")
    print(f"  Output : {args.output}")
    print(f"  AI     : {'Enabled (Gemini)' if use_ai else 'Disabled (SymPy only)'}")
    if page_range:
        print(f"  Pages  : {page_range[0]}–{page_range[1]}")
    else:
        print(f"  Pages  : All")
    print("=" * 60)

    # Step 1: Parse PDF
    print("\n[1/4] Parsing PDF...")
    pdf_parser = PDFParser(args.input, verbose=args.verbose)
    pages = pdf_parser.extract(page_range=page_range)
    print(f"      Extracted {len(pages)} page(s), {sum(len(p['lines']) for p in pages)} line(s)")

    # Step 2: Extract formulas and categorize content
    print("\n[2/4] Extracting and categorizing content...")
    extractor = FormulaExtractor(verbose=args.verbose)
    for page in tqdm(pages, desc="      Processing pages", disable=not args.verbose):
        extractor.process_page(page)
    total_items = sum(len(p["items"]) for p in pages)
    print(f"      Found {total_items} verifiable item(s)")

    # Step 3: Verify
    print("\n[3/4] Verifying content...")
    sympy_verifier = SympyVerifier(verbose=args.verbose)
    ai_verifier = AIVerifier(api_key=gemini_key, verbose=args.verbose) if use_ai else None

    all_results = []
    for page in tqdm(pages, desc="      Verifying pages"):
        page_results = []
        for item in page["items"]:
            result = {
                "page": page["page_number"],
                "line": item["line_number"],
                "type": item["type"],
                "content": item["content"],
                "sympy_result": None,
                "ai_result": None,
                "final_status": "uncertain",
                "explanation": "",
            }

            # SymPy verification for formulas/equations
            if item["type"] in ("equation", "inequality", "identity"):
                sym_res = sympy_verifier.verify(item["content"])
                result["sympy_result"] = sym_res
                result["final_status"] = sym_res["status"]
                result["explanation"] = sym_res["explanation"]

            # AI verification for all items
            if use_ai:
                ai_res = ai_verifier.verify(item)
                result["ai_result"] = ai_res
                # AI overrides uncertain SymPy results; errors from either = error
                if result["final_status"] == "uncertain":
                    result["final_status"] = ai_res["status"]
                    result["explanation"] = ai_res["explanation"]
                elif ai_res["status"] == "error":
                    result["final_status"] = "error"
                    result["explanation"] += f" | AI: {ai_res['explanation']}"

            page_results.append(result)
        all_results.append({"page_number": page["page_number"], "results": page_results})

    # Step 4: Generate report
    print("\n[4/4] Generating PDF report...")
    report = ReportGenerator(verbose=args.verbose)
    report.generate(
        results=all_results,
        source_pdf=args.input,
        output_path=args.output,
    )

    # Summary
    flat = [r for page in all_results for r in page["results"]]
    errors = sum(1 for r in flat if r["final_status"] == "error")
    correct = sum(1 for r in flat if r["final_status"] == "correct")
    uncertain = sum(1 for r in flat if r["final_status"] == "uncertain")

    print("\n" + "=" * 60)
    print("  VERIFICATION COMPLETE")
    print("=" * 60)
    print(f"  Total items checked : {len(flat)}")
    print(f"  ✅ Correct          : {correct}")
    print(f"  ❌ Errors found     : {errors}")
    print(f"  ⚠️  Uncertain        : {uncertain}")
    print(f"\n  Report saved to: {args.output}")
    print("=" * 60)


if __name__ == "__main__":
    main()
