PDFLATEX = /Library/TeX/texbin/pdflatex
JOBNAME = MTH165_Exam_Companion

all: pdf

pdf:
	$(PDFLATEX) -interaction=nonstopmode -jobname=$(JOBNAME) main.tex
	$(PDFLATEX) -interaction=nonstopmode -jobname=$(JOBNAME) main.tex

clean:
	rm -f $(JOBNAME).aux $(JOBNAME).log $(JOBNAME).out $(JOBNAME).toc $(JOBNAME).synctex.gz
