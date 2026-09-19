PDFLATEX = pdflatex -interaction=nonstopmode -halt-on-error

all: main.pdf

main.pdf: main.tex style.sty $(wildcard chapters/*.tex)
	@echo "==> Pass 1/2: Generating auxiliary files..."
	$(PDFLATEX) main.tex > /dev/null
	@echo "==> Pass 2/2: Resolving cross-references and table of contents..."
	$(PDFLATEX) main.tex > /dev/null
	@cp main.pdf CSE326_TEXTBOOK.pdf
	@echo "==> Successfully compiled CSE326/main.pdf & CSE326/CSE326_TEXTBOOK.pdf"

clean:
	@rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.synctex.gz *.listing
	@rm -f chapters/*.aux

distclean: clean
	@rm -f main.pdf CSE326_TEXTBOOK.pdf

.PHONY: all clean distclean
