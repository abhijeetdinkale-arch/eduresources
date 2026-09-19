all: ece279

ece279:
	@echo "==> Compiling ECE279: Basic Electrical and Electronics Engineering Guide..."
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	@echo "==> ECE279 Book built successfully: main.pdf"

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk chapters/*.aux main.pdf

.PHONY: all ece279 clean
