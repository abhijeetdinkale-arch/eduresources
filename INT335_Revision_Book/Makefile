PDFLATEX ?= pdflatex
LATEXFLAGS ?= -interaction=nonstopmode -halt-on-error

.PHONY: all clean distclean

all: main.pdf

main.pdf: main.tex revision_style.sty chapters/*.tex frontmatter/*.tex
	@echo "==> Pass 1: Compiling INT335_Revision_Book/main.tex..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Pass 2: Resolving TOC and Cross-References..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Successfully compiled INT335_Revision_Book/main.pdf"

clean:
	@echo "==> Cleaning auxiliary files..."
	@rm -f *.aux *.log *.out *.toc *.synctex.gz
	@rm -f chapters/*.aux frontmatter/*.aux

distclean: clean
	@rm -f main.pdf
