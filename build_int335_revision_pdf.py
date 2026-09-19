# -*- coding: utf-8 -*-
import os

os.makedirs("INT335_Revision_Book/chapters", exist_ok=True)
os.makedirs("INT335_Revision_Book/frontmatter", exist_ok=True)

# 1. revision_style.sty
rev_style = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{revision_style}[2026/09/17 v1.0 INT335 Revision Book Style]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=18mm,top=22mm,bottom=22mm,headheight=16pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts,mathtools}
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
\definecolor{GoldBg}{RGB}{254, 243, 199}
\definecolor{GoldBorder}{RGB}{217, 119, 6}

\color{DarkSlate}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily\color{BrandNavy}\textbf{INT335: Design Thinking} --- High-Yield Revision Guide}
\fancyhead[R]{\small\sffamily\color{BrandOrange}\textbf{\leftmark}}
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

\titleformat{\section}
  {\normalfont\Large\bfseries\sffamily\color{BrandNavy}}
  {\thesection}{1em}{}
  [\vspace{2pt}{\color{BrandOrange!40}\rule{\linewidth}{0.5pt}}]

\titlespacing*{\section}{0pt}{12pt}{4pt}

\titleformat{\subsection}
  {\normalfont\large\bfseries\sffamily\color{BrandBlue}}
  {\thesubsection}{0.8em}{}
\titlespacing*{\subsection}{0pt}{8pt}{3pt}

% High-Yield Card Box
\newtcolorbox{revbox}[1][Key Concept Summary]{%
  enhanced,
  breakable,
  colback=LightBg,
  colframe=BrandOrange,
  arc=2mm,
  boxrule=1.2pt,
  leftrule=4pt,
  title={\textbf{#1}},
  fonttitle=\bfseries\sffamily\color{white},
  colbacktitle=BrandOrange
}

% Formula / Law Box
\newtcolorbox{formulabox}[1][Core Framework / Equation]{%
  enhanced,
  breakable,
  colback=GoldBg,
  colframe=GoldBorder,
  arc=2mm,
  boxrule=1.2pt,
  leftrule=4pt,
  title={\textbf{#1}},
  fonttitle=\bfseries\sffamily\color{white},
  colbacktitle=GoldBorder
}

% Case Takeaway Box
\newtcolorbox{casebox}[1][Case Study Takeaway]{%
  enhanced,
  breakable,
  colback=white,
  colframe=BrandNavy,
  arc=2mm,
  boxrule=1.2pt,
  leftrule=4pt,
  title={\textbf{#1}},
  fonttitle=\bfseries\sffamily\color{white},
  colbacktitle=BrandNavy
}

\endinput
"""

with open("INT335_Revision_Book/revision_style.sty", "w", encoding="utf-8") as f:
    f.write(rev_style)

# 2. Cover
rev_cover = r"""\begin{titlepage}
\pagenumbering{Alph}
\pagecolor{LightBg}
\begin{flushleft}
    \vspace*{1.5cm}
    {\Huge\bfseries\sffamily\color{BrandNavy} INT335: DESIGN THINKING}\\[0.4cm]
    {\LARGE\sffamily\color{BrandOrange} High-Yield Exam Revision Handbook}\\[0.8cm]
    \noindent{\color{BrandOrange}\rule{\linewidth}{2.5pt}}\\[1.2cm]
    
    {\large\sffamily\textbf{Target Curriculum:}}\\
    {\normalsize\sffamily B.Tech Computer Science \& Engineering \textbar\ Semester 3}\\
    {\normalsize\sffamily Lovely Professional University}\\[1.5cm]
    
    \begin{tcolorbox}[enhanced, colback=white, colframe=BrandNavy, boxrule=1.5pt, arc=4pt, width=0.95\linewidth]
        \sffamily\bfseries\large Revision Handbook Highlights:
        \begin{itemize}[leftmargin=1.2em, itemsep=3pt, topsep=4pt]
            \item \textbf{High-Yield Concept Cards:} Core theoretical models, psychological axioms, and cognitive biases.
            \item \textbf{Comparison Matrices:} Qualitative vs. Quantitative, Lo-Fi vs. Hi-Fi, Usability vs. CX, Refactoring vs. Re-design.
            \item \textbf{Formulas \& Metrics:} Screening matrix scoring, priority formula $P = F \times S \times C$, WCAG contrast ratios.
            \item \textbf{Landmark Case Studies:} OXO Good Grips, M-Pesa, Jaipur Foot, Juicero, Google Glass, and Ford Edsel.
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

with open("INT335_Revision_Book/frontmatter/cover.tex", "w", encoding="utf-8") as f:
    f.write(rev_cover)

# 3. Main tex
main_rev_tex = r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{revision_style}

\title{INT335: Design Thinking --- Quick Revision Handbook}
\author{LPU Engineering Open}
\date{Academic Year 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}

\tableofcontents
\newpage

\mainmatter

\input{chapters/chapter1_revision}
\input{chapters/chapter2_revision}
\input{chapters/chapter3_revision}
\input{chapters/chapter4_revision}
\input{chapters/chapter5_revision}
\input{chapters/chapter6_revision}

\end{document}
"""

with open("INT335_Revision_Book/main.tex", "w", encoding="utf-8") as f:
    f.write(main_rev_tex)

# 4. Makefile
rev_makefile = r"""PDFLATEX ?= pdflatex
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
"""

with open("INT335_Revision_Book/Makefile", "w", encoding="utf-8") as f:
    f.write(rev_makefile)

print("Revision book LaTeX structure initialized.")
