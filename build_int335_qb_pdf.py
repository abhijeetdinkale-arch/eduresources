# -*- coding: utf-8 -*-
import os
import subprocess

os.makedirs("INT335_Question_Bank/chapters", exist_ok=True)
os.makedirs("INT335_Question_Bank/frontmatter", exist_ok=True)

# 1. qb_style.sty
qb_style = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{qb_style}[2026/09/17 v1.0 INT335 Question Bank Style]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=20mm,top=24mm,bottom=24mm,headheight=14pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts}
\RequirePackage{xcolor}
\RequirePackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\RequirePackage{enumitem}
\RequirePackage{fancyhdr}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{titlesec}
\RequirePackage{booktabs}
\RequirePackage{microtype}
\RequirePackage[hidelinks,colorlinks=true,linkcolor=BrandNavy,urlcolor=BrandOrange,citecolor=BrandNavy]{hyperref}

% Palette
\definecolor{BrandOrange}{RGB}{234, 88, 12}
\definecolor{BrandNavy}{RGB}{15, 44, 89}
\definecolor{BrandBlue}{RGB}{30, 86, 160}
\definecolor{DarkSlate}{RGB}{30, 41, 59}
\definecolor{LightBg}{RGB}{255, 247, 237}
\definecolor{BorderGray}{RGB}{226, 232, 240}
\definecolor{SuccessGreen}{RGB}{22, 163, 74}

\color{DarkSlate}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily\color{BrandNavy}\textbf{INT335: Design Thinking} --- Question Bank}
\fancyhead[R]{\small\sffamily\color{BrandOrange}\textbf{180 Chapter-Wise MCQs}}
\fancyfoot[C]{\small\sffamily\bfseries\color{BrandNavy}\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{BrandOrange}\leaders\hrule height \headrulewidth\hfill}}

\titleformat{\chapter}[display]
  {\normalfont\sffamily\raggedright}
  {\color{BrandOrange}\large\bfseries\MakeUppercase{\chaptertitlename\ \thechapter}}
  {2pt}
  {\LARGE\bfseries\color{BrandNavy}}
  [\vspace{2pt}{\color{BrandOrange}\rule{\linewidth}{1.2pt}}\vspace{6pt}]

\titlespacing*{\chapter}{0pt}{-10pt}{14pt}

\newcommand{\mcqitem}[6]{%
  \noindent
  \textbf{Q.#1}\quad #2\\[1.5mm]
  \begin{enumerate}[label=(\Alph*), itemsep=0.5mm, topsep=1mm, leftmargin=8mm]
    \item #3
    \item #4
    \item #5
    \item #6
  \end{enumerate}
  \vspace{2mm}
}

\newenvironment{answerkeytable}[1]{%
  \begin{tcolorbox}[enhanced, colback=white, colframe=BrandNavy, arc=2mm, boxrule=1pt, title={\textbf{#1}}, fonttitle=\bfseries\sffamily\color{white}, colbacktitle=BrandNavy]
  \centering
  \small\sffamily
}{%
  \end{tcolorbox}
}

\newtcolorbox{expbox}[1][Answer Key \& Explanations]{%
  enhanced,
  breakable,
  colback=LightBg,
  colframe=BrandOrange,
  arc=2mm,
  boxrule=1pt,
  title={\textbf{#1}},
  fonttitle=\bfseries\sffamily\color{white},
  colbacktitle=BrandOrange
}

\endinput
"""

with open("INT335_Question_Bank/qb_style.sty", "w", encoding="utf-8") as f:
    f.write(qb_style)

# 2. Cover
cover = r"""\begin{titlepage}
\pagenumbering{Alph}
\pagecolor{LightBg}
\begin{flushleft}
    \vspace*{1.5cm}
    {\Huge\bfseries\sffamily\color{BrandNavy} INT335: DESIGN THINKING}\\[0.4cm]
    {\LARGE\sffamily\color{BrandOrange} 180 Concept-Building MCQs \& Exam Practice Bank}\\[0.8cm]
    \noindent{\color{BrandOrange}\rule{\linewidth}{2.5pt}}\\[1.2cm]
    
    {\large\sffamily\textbf{Target Curriculum:}}\\
    {\normalsize\sffamily B.Tech Computer Science \& Engineering \textbar\ Semester 3}\\
    {\normalsize\sffamily Lovely Professional University}\\[1.5cm]
    
    \begin{tcolorbox}[enhanced, colback=white, colframe=BrandNavy, boxrule=1.5pt, arc=4pt, width=0.95\linewidth]
        \sffamily\bfseries\large Question Bank Features:
        \begin{itemize}[leftmargin=1.2em, itemsep=3pt, topsep=4pt]
            \item \textbf{Complete 6-Unit Coverage:} 30 easy, verified MCQs per Unit (180 Total).
            \item \textbf{Comprehensive Solutions:} Every question includes correct answer key and pedagogical rationale.
            \item \textbf{Aligned with Syllabus:} Covers cognitive models, user empathy, SCAMPER, wireframes, testing heuristics, and NABC pitching.
        \end{itemize}
    \end{tcolorbox}
    
    \vfill
    
    {\sffamily\small\textbf{Published by:}\\
    LPU Engineering Open Publishing Project\\
    \url{https://github.com/LPU-Engineering-Open}}
\end{flushleft}
\end{titlepage}
\nopagecolor
\pagenumbering{roman}
"""

with open("INT335_Question_Bank/frontmatter/cover.tex", "w", encoding="utf-8") as f:
    f.write(cover)

# 3. Main tex
main_qb_tex = r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{qb_style}

\title{INT335: Design Thinking --- Question Bank}
\author{LPU Engineering Open}
\date{Academic Year 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}

\tableofcontents
\newpage

\mainmatter

\input{chapters/unit1_mcqs}
\input{chapters/unit2_mcqs}
\input{chapters/unit3_mcqs}
\input{chapters/unit4_mcqs}
\input{chapters/unit5_mcqs}
\input{chapters/unit6_mcqs}

\end{document}
"""

with open("INT335_Question_Bank/main.tex", "w", encoding="utf-8") as f:
    f.write(main_qb_tex)

# 4. Makefile
qb_makefile = r"""PDFLATEX ?= pdflatex
LATEXFLAGS ?= -interaction=nonstopmode -halt-on-error

.PHONY: all clean distclean

all: main.pdf

main.pdf: main.tex qb_style.sty chapters/*.tex frontmatter/*.tex
	@echo "==> Pass 1: Compiling INT335_Question_Bank/main.tex..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Pass 2: Resolving TOC and Cross-References..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Successfully compiled INT335_Question_Bank/main.pdf"

clean:
	@echo "==> Cleaning auxiliary files..."
	@rm -f *.aux *.log *.out *.toc *.synctex.gz
	@rm -f chapters/*.aux frontmatter/*.aux

distclean: clean
	@rm -f main.pdf
"""

with open("INT335_Question_Bank/Makefile", "w", encoding="utf-8") as f:
    f.write(qb_makefile)

print("INT335 Question Bank LaTeX scaffold ready.")
