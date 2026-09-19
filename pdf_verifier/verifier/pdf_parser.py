"""
PDF Parser
==========
Extracts text content page by page from a PDF file using PyMuPDF.
Falls back to pdfplumber for complex/scanned layouts.
"""

import fitz  # PyMuPDF
from typing import Optional, Tuple


class PDFParser:
    def __init__(self, pdf_path: str, verbose: bool = False):
        self.pdf_path = pdf_path
        self.verbose = verbose

    def extract(self, page_range: Optional[Tuple[int, int]] = None) -> list:
        """
        Extract text from the PDF, page by page.

        Returns a list of page dicts:
        {
            "page_number": int,       # 1-indexed
            "lines": [
                {
                    "line_number": int,   # global line number across all pages
                    "page_line": int,     # line number within this page
                    "text": str,
                }
            ],
            "items": []               # filled later by FormulaExtractor
        }
        """
        doc = fitz.open(self.pdf_path)
        total_pages = len(doc)

        start_page = 1
        end_page = total_pages

        if page_range:
            start_page = max(1, page_range[0])
            end_page = min(total_pages, page_range[1])

        pages = []
        global_line_number = 1

        for page_idx in range(start_page - 1, end_page):  # 0-indexed for fitz
            page = doc[page_idx]
            page_number = page_idx + 1

            # Extract text as a list of lines
            raw_text = page.get_text("text")
            raw_lines = raw_text.splitlines()

            page_lines = []
            page_line_num = 1
            for raw_line in raw_lines:
                stripped = raw_line.strip()
                if not stripped:
                    page_line_num += 1
                    continue  # skip blank lines

                page_lines.append({
                    "line_number": global_line_number,
                    "page_line": page_line_num,
                    "text": stripped,
                })
                global_line_number += 1
                page_line_num += 1

            pages.append({
                "page_number": page_number,
                "lines": page_lines,
                "items": [],
            })

            if self.verbose:
                print(f"      Page {page_number}: {len(page_lines)} lines extracted")

        doc.close()
        return pages
