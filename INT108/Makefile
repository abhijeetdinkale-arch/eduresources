# Makefile for INT108 Python Programming Textbook
LATEX = pdflatex
FLAGS = -interaction=nonstopmode -halt-on-error

TARGET = main.pdf
SRC = main.tex style.sty $(wildcard chapters/*.tex)

.PHONY: all clean distclean

all: $(TARGET)
	@cp main.pdf INT108.pdf
	@echo "==> Successfully compiled INT108/main.pdf & INT108/INT108.pdf"

$(TARGET): $(SRC)
	@echo "==> Pass 1/2: Generating auxiliary files..."
	$(LATEX) $(FLAGS) main.tex > /dev/null
	@echo "==> Pass 2/2: Resolving Table of Contents and Cross-References..."
	$(LATEX) $(FLAGS) main.tex

clean:
	@rm -f *.aux *.log *.out *.toc *.synctex.gz chapters/*.aux

distclean: clean
	@rm -f $(TARGET) INT108.pdf
