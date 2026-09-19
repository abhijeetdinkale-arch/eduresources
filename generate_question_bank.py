import os

print("Generating MTH165 Question Bank...")

# 1. qb_style.sty
with open("MTH165_Question_Bank/qb_style.sty", "w") as f:
    f.write(r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{qb_style}[2026/09/16 v1.0 MTH165 Question Bank Style]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=20mm,top=24mm,bottom=24mm,headheight=22pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts,mathtools,physics,bm}
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
\RequirePackage[hidelinks,colorlinks=true,linkcolor=LPUNavy,urlcolor=LPUOrange,citecolor=LPUNavy]{hyperref}

% Palette
\definecolor{LPUNavy}{RGB}{15, 32, 67}
\definecolor{LPUOrange}{RGB}{232, 90, 16}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{LightBg}{RGB}{246, 248, 252}
\definecolor{BorderGray}{RGB}{205, 215, 225}
\definecolor{SuccessGreen}{RGB}{24, 134, 75}
\definecolor{AlertRed}{RGB}{200, 30, 30}

% Header/Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{LPUNavy}\textbf{MTH165: Mathematics for Engineers --- Question Bank}}
\fancyhead[R]{\small\color{LPUOrange}\textbf{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

% Section styling
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{LPUNavy}}{\chaptertitlename\ \thechapter}{15pt}{\Huge}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{LPUNavy}}{\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{LPUOrange}}{\thesubsection}{1em}{}

% Boxes
\newtcolorbox{subjectiveq}[2][]{
    enhanced,
    breakable,
    colback=white,
    colframe=LPUNavy,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    title={Problem #2 \hfill [Subjective --- 5/10 Marks]},
    boxrule=1pt,
    arc=3mm,
    top=3mm, bottom=3mm, left=3mm, right=3mm,
    #1
}

\newtcolorbox{solbox}[1][]{
    enhanced,
    breakable,
    colback=LightBg,
    colframe=BorderGray,
    boxrule=0.8pt,
    arc=2mm,
    top=2.5mm, bottom=2.5mm, left=3mm, right=3mm,
    title={\textbf{\color{LPUNavy}Step-by-Step Analytical Solution:}},
    #1
}

\newtcolorbox{examinertip}[1][]{
    enhanced,
    breakable,
    colback=rgb,255:red,255;green,248;blue,230,
    colframe=LPUOrange,
    fonttitle=\bfseries\color{LPUOrange},
    title={\textbf{Examiner's Guidance \& Marking Breakdown}},
    boxrule=0.8pt,
    arc=2mm,
    top=2mm, bottom=2mm, left=3mm, right=3mm,
    #1
}

\newcommand{\mcqitem}[6]{
    \noindent\textbf{Q#1. #2}
    \begin{enumerate}[label=(\alph*),topsep=2pt,itemsep=1pt,partopsep=0pt,parsep=0pt]
        \item #3
        \item #4
        \item #5
        \item #6
    \end{enumerate}
    \vspace{2mm}
}

\newenvironment{answerkeytable}[1]{
    \begin{table}[htbp]
    \centering
    \caption{\textbf{#1}}
    \vspace{2mm}
}{
    \end{table}
}
""")

# 2. main.tex
with open("MTH165_Question_Bank/main.tex", "w") as f:
    f.write(r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{qb_style}

\title{MTH165: Mathematics for Engineers --- Complete Question Bank \& PYQ Suite}
\author{LPU Engineering Open Series}
\date{Academic Year 2024--2025 / 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}
\input{frontmatter/blueprint}

\tableofcontents
\newpage

\mainmatter

\input{chapters/unit1_matrices_qb}
\input{chapters/unit2_diff_calculus_qb}
\input{chapters/unit3_integral_calculus_qb}
\input{chapters/unit4_multivariate_diff_qb}
\input{chapters/unit5_multiple_integrals_qb}
\input{chapters/unit6_fourier_series_qb}

\end{document}
""")

# 3. frontmatter/cover.tex & blueprint.tex
with open("MTH165_Question_Bank/frontmatter/cover.tex", "w") as f:
    f.write(r"""\begin{titlepage}
\centering
\vspace*{1.5cm}
{\Huge \textbf{\color{LPUNavy}MTH165: Mathematics for Engineers}}\\[0.5cm]
{\LARGE \textbf{\color{LPUOrange}Comprehensive Question Bank \& Previous Year Questions (PYQ) Book}}\\[0.3cm]
{\large \textit{120+ Fully Solved Subjective Problems \& 300+ Chapter-Wise Exam MCQs}}\\[2cm]

\rule{\linewidth}{1.5pt}\\[0.5cm]
{\large \textbf{B.Tech / B.E. Semester 1 Curriculum | Lovely Professional University}}\\[0.5cm]
\rule{\linewidth}{1.5pt}\\[2.5cm]

\vfill
{\large \textbf{LPU Engineering Open Publishing Initiative}}\\[0.2cm]
{\small Independent Open-Source Academic Guide Series}
\end{titlepage}
\newpage
""")

with open("MTH165_Question_Bank/frontmatter/blueprint.tex", "w") as f:
    f.write(r"""\chapter*{Curriculum \& Question Bank Blueprint}
\addcontentsline{toc}{chapter}{Curriculum \& Question Bank Blueprint}

This Question Bank provides complete mathematical coverage of all 6 Units of \textbf{MTH165: Mathematics for Engineers}:
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Unit 1: Matrix Methods and Linear Systems} (Elementary transformations, rank, linear independence, $Ax=b$, eigenvalues, Cayley--Hamilton).
    \item \textbf{Unit 2: Differential Calculus and Applications} (Implicit/parametric derivatives, successive derivatives, Leibniz rule, Rolle/Lagrange/Cauchy MVTs, Taylor/Maclaurin series, L'H\^opital's rule, optimization).
    \item \textbf{Unit 3: Fundamentals of Integral Calculus} (Standard antiderivatives, substitution, parts, partial fractions, definite integral properties, King's rule).
    \item \textbf{Unit 4: Multivariate Differentiation} (2D limits/continuity, partial derivatives, Euler's theorem, total differentials, Hessian discriminant, Lagrange multipliers).
    \item \textbf{Unit 5: Multivariable Integration and Applications} (Double integrals, change of order, triple integrals, Polar/Cylindrical/Spherical transformations, Jacobians, area and volume).
    \item \textbf{Unit 6: Introduction to Fourier Series} (Periodic functions, Euler formulas, Dirichlet conditions, discontinuity averages, even/odd series, half-range expansions, Parseval's identity).
\end{itemize}

Each Unit is divided into:
\begin{enumerate}
    \item \textbf{Section 1}: 20 Comprehensive Step-by-Step Solved Subjective Problems.
    \item \textbf{Section 2}: 50 Graded Solved MCQs (25 Foundational, 15 Intermediate, 10 Advanced).
    \item \textbf{Section 3}: Complete Answer Key with Mathematical Rationales.
\end{enumerate}
\newpage
""")

# 4. Makefile
with open("MTH165_Question_Bank/Makefile", "w") as f:
    f.write(r"""all:
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
""")

print("Base Question Bank files created.")
