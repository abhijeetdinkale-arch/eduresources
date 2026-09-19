PDFLATEX ?= pdflatex
LATEXFLAGS ?= -interaction=nonstopmode -halt-on-error

.PHONY: all clean distclean

all: main.pdf

main.pdf: main.tex style.sty chapters/*.tex
	@echo "==> Pass 1: Compiling INT335/main.tex..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Pass 2: Resolving TOC and Cross-References..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Successfully compiled INT335/main.pdf"

clean:
	@echo "==> Cleaning INT335 auxiliary build files..."
	@rm -f *.aux *.log *.out *.toc *.synctex.gz *.bcf *.run.xml *.fls *.fdb_latexmk
	@rm -f chapters/*.aux

distclean: clean
	@echo "==> Removing compiled INT335 PDF..."
	@rm -f main.pdf
