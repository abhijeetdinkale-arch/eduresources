"""
Report Generator
================
Generates a detailed PDF verification report using fpdf2.

Layout:
  - Cover page: book title, date, summary stats
  - Per-page sections: each verified item with status badge
  - Final summary: error list

Color coding:
  🟢 CORRECT   — green
  🔴 ERROR     — red
  🟡 UNCERTAIN — orange/yellow
"""

import os
from datetime import datetime
from fpdf import FPDF, XPos, YPos
from fpdf.enums import XPos, YPos


# ─── Colour palette ──────────────────────────────────────────────────────────
GREEN  = (34,  139, 34)
RED    = (200, 30,  30)
ORANGE = (200, 140, 0)
GREY   = (100, 100, 100)
DARK   = (30,  30,  30)
WHITE  = (255, 255, 255)
LIGHT_BG = (245, 245, 245)
PAGE_BG  = (255, 255, 255)

STATUS_COLOR = {
    "correct":   GREEN,
    "error":     RED,
    "uncertain": ORANGE,
}
STATUS_LABEL = {
    "correct":   "CORRECT",
    "error":     "ERROR",
    "uncertain": "UNCERTAIN",
}
STATUS_SYMBOL = {
    "correct":   "[OK]",
    "error":     "[!!]",
    "uncertain": "[??]",
}


def _safe(text: str, max_len: int = 0) -> str:
    """Strip characters outside latin-1 range so Helvetica can render them."""
    # Replace common unicode math/punctuation with ASCII equivalents
    replacements = {
        "\u2212": "-",   # minus sign
        "\u00d7": "x",   # multiplication sign
        "\u00f7": "/",   # division sign
        "\u2264": "<=",  # ≤
        "\u2265": ">=",  # ≥
        "\u2260": "!=",  # ≠
        "\u221a": "sqrt",# √
        "\u03c0": "pi",  # π
        "\u221e": "inf", # ∞
        "\u03b8": "theta",
        "\u03b1": "alpha",
        "\u03b2": "beta",
        "\u03b3": "gamma",
        "\u03b4": "delta",
        "\u2202": "d",   # partial
        "\u222b": "integral",
        "\u2211": "sum",
        "\u2019": "'",   # right single quote
        "\u2018": "'",   # left single quote
        "\u201c": '"',   # left double quote
        "\u201d": '"',   # right double quote
        "\u2014": "--",  # em dash
        "\u2013": "-",   # en dash
        "\u00b2": "^2",  # superscript 2
        "\u00b3": "^3",  # superscript 3
    }
    for uni, asc in replacements.items():
        text = text.replace(uni, asc)
    # Strip any remaining non-latin-1 chars
    text = text.encode("latin-1", errors="replace").decode("latin-1")
    if max_len and len(text) > max_len:
        text = text[:max_len] + "..."
    return text


class ReportPDF(FPDF):
    """Custom FPDF subclass with header/footer."""

    def __init__(self, source_name: str):
        super().__init__()
        self.source_name = source_name
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() == 1:
            return  # no header on cover
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*GREY)
        self.cell(0, 8, f"PDF Verification Report  |  {self.source_name}", align="L",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*GREY)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(*GREY)
        self.cell(0, 5, f"Page {self.page_no()}", align="C")


class ReportGenerator:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def generate(
        self,
        results: list[dict],
        source_pdf: str,
        output_path: str,
    ) -> None:
        source_name = os.path.basename(source_pdf)
        pdf = ReportPDF(source_name)

        # ── Flatten results for stats ─────────────────────────────────────────
        flat = [r for page in results for r in page["results"]]
        total   = len(flat)
        correct  = sum(1 for r in flat if r["final_status"] == "correct")
        errors   = sum(1 for r in flat if r["final_status"] == "error")
        uncertain = sum(1 for r in flat if r["final_status"] == "uncertain")
        error_items = [r for r in flat if r["final_status"] == "error"]

        # ── Cover page ────────────────────────────────────────────────────────
        pdf.add_page()
        pdf.set_fill_color(*DARK)
        pdf.rect(0, 0, 210, 297, "F")

        pdf.set_y(60)
        pdf.set_font("Helvetica", "B", 28)
        pdf.set_text_color(*WHITE)
        pdf.cell(0, 12, "PDF BOOK VERIFIER", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.set_font("Helvetica", "", 14)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, "Verification Report", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.ln(10)
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(*WHITE)
        pdf.cell(0, 8, f"Source: {source_name}", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", align="C",
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Stats boxes
        pdf.ln(20)
        box_y = pdf.get_y()
        box_w = 40
        box_h = 30
        cols = [
            (total,     "TOTAL",     (80,  80,  80)),
            (correct,   "CORRECT",   GREEN),
            (errors,    "ERRORS",    RED),
            (uncertain, "UNCERTAIN", ORANGE),
        ]
        start_x = (210 - (box_w * 4 + 9 * 3)) / 2
        for i, (val, label, color) in enumerate(cols):
            bx = start_x + i * (box_w + 9)
            pdf.set_fill_color(*color)
            pdf.rect(bx, box_y, box_w, box_h, "F")
            pdf.set_xy(bx, box_y + 4)
            pdf.set_font("Helvetica", "B", 18)
            pdf.set_text_color(*WHITE)
            pdf.cell(box_w, 12, str(val), align="C", new_x=XPos.RIGHT, new_y=YPos.TOP)
            pdf.set_xy(bx, box_y + 17)
            pdf.set_font("Helvetica", "", 7)
            pdf.cell(box_w, 8, label, align="C")

        # Accuracy bar
        pdf.set_y(box_y + box_h + 15)
        acc = (correct / total * 100) if total else 0
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(*WHITE)
        pdf.cell(0, 8, f"Accuracy: {acc:.1f}%  |  {errors} issue(s) found", align="C",
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # ── Summary / Error Index page ────────────────────────────────────────
        if error_items:
            pdf.add_page()
            pdf.set_text_color(*DARK)
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_fill_color(*RED)
            pdf.set_text_color(*WHITE)
            pdf.cell(0, 10, f"  Error Summary ({len(error_items)} issues)", align="L",
                     fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(4)

            pdf.set_font("Helvetica", "", 9)
            for i, r in enumerate(error_items, 1):
                if pdf.get_y() > 260:
                    pdf.add_page()
                pdf.set_text_color(*DARK)
                pdf.set_fill_color(*LIGHT_BG)
                pdf.cell(0, 6,
                         _safe(f"{i}. [Page {r['page']} | Line {r['line']}]  {r['content'][:90]}"),
                         fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                if r["explanation"]:
                    pdf.set_text_color(*RED)
                    pdf.set_x(20)
                    pdf.multi_cell(0, 5, _safe(f"   -> {r['explanation']}"))
                    pdf.set_text_color(*DARK)
                pdf.ln(1)

        # ── Per-page detail sections ──────────────────────────────────────────
        for page_data in results:
            page_num = page_data["page_number"]
            page_results = page_data["results"]
            if not page_results:
                continue

            pdf.add_page()
            # Page header banner
            pdf.set_fill_color(50, 50, 100)
            pdf.set_text_color(*WHITE)
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 9, f"  Page {page_num}", fill=True,
                     new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(3)

            for r in page_results:
                if pdf.get_y() > 265:
                    pdf.add_page()
                    pdf.set_fill_color(50, 50, 100)
                    pdf.set_text_color(*WHITE)
                    pdf.set_font("Helvetica", "B", 10)
                    pdf.cell(0, 7, f"  Page {page_num} (continued)", fill=True,
                             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    pdf.ln(2)

                status = r["final_status"]
                color = STATUS_COLOR.get(status, GREY)
                label = STATUS_LABEL.get(status, "UNCERTAIN")

                # Status badge
                pdf.set_font("Helvetica", "B", 7)
                pdf.set_fill_color(*color)
                pdf.set_text_color(*WHITE)
                pdf.cell(22, 5, f" {label}", fill=True)

                # Type badge
                pdf.set_fill_color(200, 200, 220)
                pdf.set_text_color(*DARK)
                pdf.set_font("Helvetica", "", 7)
                pdf.cell(22, 5, f" {r['type'][:14]}", fill=True)

                # Line reference
                pdf.set_text_color(*GREY)
                pdf.cell(22, 5, f"  Ln {r['line']}")

                # Content (rest of line)
                pdf.set_text_color(*DARK)
                content_preview = _safe(r["content"], max_len=80)
                pdf.cell(0, 5, content_preview, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

                if r["explanation"]:
                    pdf.set_text_color(*color)
                    pdf.set_x(25)
                    pdf.set_font("Helvetica", "I", 7)
                    explanation = _safe(r["explanation"], max_len=200)
                    pdf.multi_cell(0, 4, f"   -> {explanation}")
                    pdf.set_text_color(*DARK)

                pdf.ln(1)

        # ── Save ──────────────────────────────────────────────────────────────
        pdf.output(output_path)
        if self.verbose:
            print(f"      Report written to: {output_path}")
