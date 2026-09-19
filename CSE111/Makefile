PDFLATEX ?= pdflatex
LATEXFLAGS ?= -interaction=nonstopmode -halt-on-error

.PHONY: all clean distclean

all: main.pdf

main.pdf: main.tex style.sty chapters/*.tex
	@echo "==> Pass 1: Compiling CSE111/main.tex..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Pass 2: Resolving TOC and Cross-References..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Successfully compiled CSE111/main.pdf"

clean:
	@echo "==> Cleaning CSE111 auxiliary build files..."
	@rm -f *.aux *.log *.out *.toc *.synctex.gz *.bcf *.run.xml *.fls *.fdb_latexmk
	@rm -f chapters/*.aux

distclean: clean
	@echo "==> Removing compiled CSE111 PDF..."
	@rm -f main.pdf
