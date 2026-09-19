import os

print("Generating MTH165 Sample Question Papers Book (16 Complete Papers)...")

# 1. paper_style.sty
with open("MTH165_Sample_Question_Papers/paper_style.sty", "w") as f:
    f.write(r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{paper_style}[2026/09/16 v1.0 MTH165 Sample Question Papers Style]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=20mm,top=24mm,bottom=24mm,headheight=16pt]{geometry}
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

% Color Palette
\definecolor{LPUNavy}{RGB}{15, 32, 67}
\definecolor{LPUOrange}{RGB}{232, 90, 16}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{LightBg}{RGB}{246, 248, 252}
\definecolor{BorderGray}{RGB}{205, 215, 225}
\definecolor{AlertRed}{RGB}{180, 40, 40}
\definecolor{SuccessGreen}{RGB}{24, 134, 75}
\definecolor{TipBg}{RGB}{255, 250, 235}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily\color{LPUNavy}\textbf{MTH165: Mathematics for Engineers} --- Sample Question Papers}
\fancyhead[R]{\small\sffamily\color{LPUOrange}\textbf{16-Paper University Exam Suite}}
\fancyfoot[C]{\small\sffamily\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.3pt}

\titleformat{\chapter}[display]
  {\normalfont\sffamily\huge\bfseries\color{LPUNavy}}
  {\Large\color{LPUOrange}\chaptertitlename\ \thechapter}{8pt}
  {\titlerule[1.5pt]\vspace{4pt}}

\titleformat{\section}
  {\normalfont\sffamily\Large\bfseries\color{LPUNavy}}
  {\thesection}{1em}{}

\newcommand{\ExamHeader}[5]{%
  \begin{tcolorbox}[
    enhanced,
    colback=white,
    colframe=LPUNavy,
    arc=2mm,
    boxrule=1.2pt,
    top=3mm, bottom=3mm, left=4mm, right=4mm
  ]
    \begin{center}
      {\large\bfseries\color{LPUNavy} LOVELY PROFESSIONAL UNIVERSITY}\\[1mm]
      {\normalsize\bfseries Department of Mathematics | School of Chemical Engineering and Physical Sciences}\\[2mm]
      {\large\bfseries\color{LPUOrange} #1 --- #2}\\[1mm]
      {\small\bfseries Course Code: MTH165 \quad|\quad Course Title: Mathematics for Engineers}\\[2mm]
      \rule{0.9\linewidth}{0.5pt}\\[1.5mm]
      {\small \textbf{Time Allowed:} #3 \hfill \textbf{Maximum Marks:} #4 \hfill \textbf{Negative Marking:} #5}
    \end{center}
  \end{tcolorbox}
  \vspace{3mm}
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
    colback=TipBg,
    colframe=LPUOrange,
    fonttitle=\bfseries\color{LPUOrange},
    title={\textbf{Examiner's Grading \& Method Tip}},
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
""")

# 2. main.tex
with open("MTH165_Sample_Question_Papers/main.tex", "w") as f:
    f.write(r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{paper_style}

\title{MTH165: Mathematics for Engineers --- Complete 16-Paper Sample Question Papers Book}
\author{LPU Engineering Open Series}
\date{Academic Year 2024--2025 / 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}
\input{frontmatter/instructions}

\tableofcontents
\newpage

\mainmatter

% ==============================================================================
% SECTION 1: CONTINUOUS ASSESSMENT 1 (CA-1) --- UNITS 1 & 2
% ==============================================================================
\chapter{Continuous Assessment 1 (CA-1) Suite}
\label{chap:ca1_suite}
\noindent
Continuous Assessment 1 evaluates students on \textbf{Unit 1 (Matrix Methods and Linear Systems)} and \textbf{Unit 2 (Differential Calculus and Applications)}. Each paper contains \textbf{6 subjective questions carrying 5 marks each (Students attempt 5 questions, Total = 30 Marks, Time Allowed = 60 Minutes)}. Complete step-by-step solutions follow each question.

\newpage
\input{ca1/set_a}
\newpage
\input{ca1/set_b}
\newpage
\input{ca1/set_c}
\newpage
\input{ca1/set_d}

% ==============================================================================
% SECTION 2: MID-TERM EXAMINATION SUITE --- UNITS 1, 2 & 3
% ==============================================================================
\chapter{Mid-Term Examination Suite (100\% MCQ Format)}
\label{chap:midterm_suite}
\noindent
The Mid-Term Examination is an objective assessment evaluating students across \textbf{Unit 1 (Matrices)}, \textbf{Unit 2 (Differential Calculus)}, and \textbf{Unit 3 (Integral Calculus)}. Each paper consists of \textbf{30 Multiple-Choice Questions (MCQs) carrying 1 mark each} (10 from Unit 1, 10 from Unit 2, 10 from Unit 3) with a negative marking deduction of \textbf{0.25 marks} per incorrect answer (Total = \textbf{30 Marks}, Time Allowed = \textbf{90 Minutes}). Complete Answer Keys and technical rationales follow each paper.

\newpage
\input{midterm/set_a}
\newpage
\input{midterm/set_b}
\newpage
\input{midterm/set_c}
\newpage
\input{midterm/set_d}

% ==============================================================================
% SECTION 3: CONTINUOUS ASSESSMENT 2 (CA-2) --- UNITS 4 & 5
% ==============================================================================
\chapter{Continuous Assessment 2 (CA-2) Suite}
\label{chap:ca2_suite}
\noindent
Continuous Assessment 2 evaluates students on \textbf{Unit 4 (Multivariate Differentiation)} and \textbf{Unit 5 (Multivariable Integration and Applications)}. Each paper contains \textbf{6 subjective questions carrying 5 marks each (Students attempt 5 questions, Total = 30 Marks, Time Allowed = 60 Minutes)}. Complete step-by-step solutions follow each question.

\newpage
\input{ca2/set_a}
\newpage
\input{ca2/set_b}
\newpage
\input{ca2/set_c}
\newpage
\input{ca2/set_d}

% ==============================================================================
% SECTION 4: END-TERM EXAMINATION SUITE --- UNITS 1 TO 6 (70 MARKS)
% ==============================================================================
\chapter{End-Term Examination Suite (70 Marks Comprehensive)}
\label{chap:endterm_suite}
\noindent
The End-Term Examination is the comprehensive university final examination (Total = \textbf{70 Marks}, Time Allowed = \textbf{3 Hours}):
\begin{itemize}[leftmargin=8mm]
    \item \textbf{Part A (Objective / MCQs --- 30 Marks):} 30 MCQs strictly testing \textbf{Unit 4, Unit 5, and Unit 6} (10 MCQs each, carrying 1 mark each, negative marking $-0.25$).
    \item \textbf{Part B (Descriptive / Subjective --- 40 Marks):} 5 comprehensive questions of 10 marks each; students attempt any 4 ($4 \times 10 = \mathbf{40\text{ Marks}}$).
    \begin{itemize}
        \item Exactly 3 questions from Units 4, 5, and 6 (one from each of Unit 4, Unit 5, Unit 6).
        \item Exactly 2 questions randomly selected across all units (Units 1 to 6).
        \item Each 10-mark question is either a comprehensive problem or a partitioned $(a)\,[5\text{ marks}] + (b)\,[5\text{ marks}]$ problem.
    \end{itemize}
\end{itemize}

\newpage
\input{endterm/set_a}
\newpage
\input{endterm/set_b}
\newpage
\input{endterm/set_c}
\newpage
\input{endterm/set_d}

\end{document}
""")

# 3. frontmatter
with open("MTH165_Sample_Question_Papers/frontmatter/cover.tex", "w") as f:
    f.write(r"""\begin{titlepage}
\centering
\vspace*{1.5cm}
{\Huge \textbf{\color{LPUNavy}MTH165: Mathematics for Engineers}}\\[0.5cm]
{\LARGE \textbf{\color{LPUOrange}16 Full Solved Sample Question Papers Book}}\\[0.3cm]
{\large \textit{4 CA-1 Papers + 4 Mid-Term Papers + 4 CA-2 Papers + 4 End-Term Papers}}\\[2cm]

\rule{\linewidth}{1.5pt}\\[0.5cm]
{\large \textbf{B.Tech / B.E. Semester 1 Curriculum | Lovely Professional University}}\\[0.5cm]
\rule{\linewidth}{1.5pt}\\[2.5cm]

\vfill
{\large \textbf{LPU Engineering Open Publishing Initiative}}\\[0.2cm]
{\small Independent Open-Source Academic Guide Series}
\end{titlepage}
\newpage
""")

with open("MTH165_Sample_Question_Papers/frontmatter/instructions.tex", "w") as f:
    f.write(r"""\chapter*{Official Examination Guidelines \& Architecture}
\addcontentsline{toc}{chapter}{Official Examination Guidelines \& Architecture}

This 16-Paper Sample Question Papers Book strictly adheres to the official evaluation architecture prescribed for \textbf{MTH165: Mathematics for Engineers}:

\begin{table}[htbp]
\centering
\caption{\textbf{MTH165 Official Assessment Suite Blueprint}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l p{3.2cm} p{2.8cm} c X}
\toprule
\textbf{Assessment} & \textbf{Syllabus Scope} & \textbf{Format} & \textbf{Marks} & \textbf{Exam Regulations} \\
\midrule
\textbf{CA-1 (4 Sets)} & Unit 1 \& Unit 2 & 6 Subjective Qs & 30 & Attempt any 5 out of 6 questions ($5 \times 6\text{M}$ or $5\text{M}$ each). Time: 60 Minutes. \\
\addlinespace
\textbf{Mid-Term (4 Sets)} & Unit 1, Unit 2, Unit 3 & 30 MCQs & 30 & 10 MCQs from Unit 1, 10 from Unit 2, 10 from Unit 3. Negative marking $-0.25$ marks for wrong answers. Time: 90 Minutes. \\
\addlinespace
\textbf{CA-2 (4 Sets)} & Unit 4 \& Unit 5 & 6 Subjective Qs & 30 & Attempt any 5 out of 6 questions ($5 \times 6\text{M}$). Time: 60 Minutes. \\
\addlinespace
\textbf{End-Term (4 Sets)} & Units 1 to 6 & \textbf{Part A}: 30 MCQs \newline \textbf{Part B}: 5 Subj Qs & 70 & \textbf{Part A}: 30 MCQs from Units 4, 5, 6 (10 each). \newline \textbf{Part B}: 5 Qs of 10M (3 from U4-6, 2 from U1-6), attempt any 4 ($4 \times 10 = 40\text{M}$). Time: 3 Hours. \\
\bottomrule
\end{tabularx}
\end{table}

\newpage
""")

# 4. Makefile
with open("MTH165_Sample_Question_Papers/Makefile", "w") as f:
    f.write(r"""all:
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
""")

print("Base setup for MTH165 Sample Question Papers created.")
