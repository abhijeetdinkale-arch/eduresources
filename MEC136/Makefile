all: mec136

mec136:
	@echo "==> Compiling MEC136: Engineering Graphics & AutoCAD Complete Study Book..."
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	@echo "==> MEC136 Book built successfully: main.pdf"

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.fls *.fdb_latexmk chapters/*.aux main.pdf

.PHONY: all mec136 clean
