import os

print("Generating Physics Question Bank (600 MCQs + 120 Theory Questions)...")

# 1. qb_style.sty
with open("Physics_Question_Bank/qb_style.sty", "w") as f:
    f.write(r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{qb_style}[2026/09/16 v1.0 PHY110 Physics Question Bank Style]

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
\definecolor{LPUOrange}{RGB}{201, 74, 28}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{LightBg}{RGB}{246, 248, 252}
\definecolor{BorderGray}{RGB}{205, 215, 225}
\definecolor{SuccessGreen}{RGB}{24, 134, 75}
\definecolor{TipBg}{RGB}{255, 250, 235}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{LPUNavy}\textbf{PHY110: Engineering Physics --- Question Bank}}
\fancyhead[R]{\small\color{LPUOrange}\textbf{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{LPUNavy}}{\chaptertitlename\ \thechapter}{12pt}{\Huge}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{LPUNavy}}{\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{LPUOrange}}{\thesubsection}{1em}{}

\newtcolorbox{theoryq}[2][]{
    enhanced,
    breakable,
    colback=white,
    colframe=LPUNavy,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    title={Theory Question #2 \hfill [Descriptive / Derivation]},
    boxrule=1pt,
    arc=2mm,
    top=2.5mm, bottom=2.5mm, left=3mm, right=3mm,
    #1
}

\newtcolorbox{theorysol}[1][]{
    enhanced,
    breakable,
    colback=LightBg,
    colframe=BorderGray,
    boxrule=0.8pt,
    arc=2mm,
    top=2.5mm, bottom=2.5mm, left=3mm, right=3mm,
    title={\textbf{\color{LPUNavy}Comprehensive Analytical Answer \& Derivation:}},
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
""")

# 2. main.tex
with open("Physics_Question_Bank/main.tex", "w") as f:
    f.write(r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{qb_style}

\title{PHY110: Engineering Physics --- Master Question Bank (600 MCQs + 120 Theory Questions)}
\author{LPU Engineering Open Series}
\date{Academic Year 2024--2025 / 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}
\input{frontmatter/blueprint}

\tableofcontents
\newpage

\mainmatter

\input{chapters/chapter-01-electromagnetic-theory-qb}
\input{chapters/chapter-02-lasers-qb}
\input{chapters/chapter-03-fiber-optics-qb}
\input{chapters/chapter-04-quantum-mechanics-qb}
\input{chapters/chapter-05-semiconductor-physics-qb}
\input{chapters/chapter-06-engineering-materials-qb}

\end{document}
""")

# 3. frontmatter
with open("Physics_Question_Bank/frontmatter/cover.tex", "w") as f:
    f.write(r"""\begin{titlepage}
\centering
\vspace*{1.5cm}
{\Huge \textbf{\color{LPUNavy}PHY110: Engineering Physics}}\\[0.5cm]
{\LARGE \textbf{\color{LPUOrange}Master Question Bank \& Previous Year Questions}}\\[0.3cm]
{\large \textit{600 Chapter-Wise Graded MCQs + 120 Comprehensive Theory Solutions}}\\[2cm]

\rule{\linewidth}{1.5pt}\\[0.5cm]
{\large \textbf{B.Tech / B.E. Semester 1 Curriculum | Lovely Professional University}}\\[0.5cm]
\rule{\linewidth}{1.5pt}\\[2.5cm]

\vfill
{\large \textbf{LPU Engineering Open Publishing Initiative}}\\[0.2cm]
{\small Independent Open-Source Academic Guide Series}
\end{titlepage}
\newpage
""")

with open("Physics_Question_Bank/frontmatter/blueprint.tex", "w") as f:
    f.write(r"""\chapter*{Curriculum \& Question Bank Architecture}
\addcontentsline{toc}{chapter}{Curriculum \& Question Bank Architecture}

This Master Question Bank provides complete mathematical and conceptual coverage across all 6 Units of \textbf{PHY110: Engineering Physics}:
\begin{enumerate}
    \item \textbf{Unit 1: Electromagnetic Theory} (Vector calculus, divergence, curl, Poisson/Laplace, continuity, Ampere law, Maxwell's 4 equations, Poynting vector).
    \item \textbf{Unit 2: Lasers and Applications} (Einstein coefficients, population inversion, metastable states, Ruby, He-Ne, Nd:YAG, Semiconductor lasers, holography).
    \item \textbf{Unit 3: Fiber Optics} (TIR, critical angle, numerical aperture, V-number, modal dispersion, attenuation windows, endoscopy).
    \item \textbf{Unit 4: Quantum Mechanics} (Photoelectric effect, de Broglie matter waves, Davisson-Germer, group/phase velocity, Heisenberg uncertainty, Schrödinger equation, particle in a box).
    \item \textbf{Unit 5: Semiconductor Physics \& Solid State} (Drude free electron model, Wiedemann-Franz law, band theory, intrinsic/extrinsic semiconductors, direct/indirect bandgap, Fermi-Dirac, Hall effect, solar cells).
    \item \textbf{Unit 6: Engineering Materials} (Dielectrics, polarization, magnetic materials, hysteresis, piezoelectrics, superconductivity, Meissner effect, Type I/II superconductors).
\end{enumerate}

Each chapter contains:
\begin{itemize}
    \item \textbf{Section 1}: 100 Graded MCQs (50 Foundational, 30 Intermediate, 20 Advanced).
    \item \textbf{Section 2}: Complete Answer Key \& Technical Explanations.
    \item \textbf{Section 3}: 20 Comprehensive Theory Questions with step-by-step analytical derivations.
\end{itemize}
\newpage
""")

# 4. Makefile
with open("Physics_Question_Bank/Makefile", "w") as f:
    f.write(r"""all:
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
""")

print("Question Bank base setup completed.")
