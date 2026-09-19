PDFLATEX ?= pdflatex
LATEX_FLAGS ?= -interaction=nonstopmode -halt-on-error

.PHONY: all clean

all: main.pdf

main.pdf: main.tex style.sty $(wildcard chapters/*.tex)
	@echo "==> LaTeX Pass 1/2..."
	$(PDFLATEX) $(LATEX_FLAGS) main.tex
	@echo "==> LaTeX Pass 2/2 (Cross-references & Table of Contents)..."
	$(PDFLATEX) $(LATEX_FLAGS) main.tex
	@echo "==> Successfully compiled Physics/main.pdf"

clean:
	@rm -f *.aux *.log *.out *.toc *.synctex.gz main.pdf chapters/*.aux
	@echo "==> Cleaned auxiliary and PDF files."
