import os

print("Generating Physics Exam Companion (CA-1, CA-2, Mid-Term, End-Term)...")

# 1. Update exam_style.sty if needed
with open("Physics_Exam_Companion/exam_style.sty", "w") as f:
    f.write(r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{exam_style}[2026/09/16 v1.0 PHY110 Exam Companion Style]

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
\definecolor{LPUOrange}{RGB}{201, 74, 28}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{LightBg}{RGB}{246, 248, 252}
\definecolor{BorderGray}{RGB}{205, 215, 225}
\definecolor{AlertRed}{RGB}{180, 40, 40}
\definecolor{SuccessGreen}{RGB}{24, 134, 75}
\definecolor{TipBg}{RGB}{255, 250, 235}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily\color{LPUNavy}\textbf{PHY110: Engineering Physics} --- Examination Companion}
\fancyhead[R]{\small\sffamily\color{LPUOrange}\textbf{16-Paper Assessment Suite}}
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
      {\normalsize\bfseries Department of Physics | School of Chemical Engineering and Physical Sciences}\\[2mm]
      {\large\bfseries\color{LPUOrange} #1 --- #2}\\[1mm]
      {\small\bfseries Course Code: PHY110 \quad|\quad Course Title: Engineering Physics}\\[2mm]
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

\newtcolorbox{projectbox}[2][]{
    enhanced,
    breakable,
    colback=white,
    colframe=LPUNavy,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    title={Project Investigation #2 \hfill [CA-2 In-Depth Assignment / File Report]},
    boxrule=1pt,
    arc=2mm,
    top=3mm, bottom=3mm, left=3.5mm, right=3.5mm,
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

# 2. Update main.tex
with open("Physics_Exam_Companion/main.tex", "w") as f:
    f.write(r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{exam_style}

\title{PHY110: Engineering Physics --- Examination Companion \& Solved Question Papers}
\author{LPU Engineering Open Series}
\date{Academic Year 2024--2025 / 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}
\input{frontmatter/blueprint}

\tableofcontents
\newpage

\mainmatter

% ==============================================================================
% SECTION 1: CONTINUOUS ASSESSMENT 1 (CA-1) --- UNITS 1 & 2 (30 MCQs)
% ==============================================================================
\chapter{Continuous Assessment 1 (CA-1) Suite}
\label{chap:ca1}
\noindent
Continuous Assessment 1 evaluates students across \textbf{Unit 1 (Electromagnetic Theory)} and \textbf{Unit 2 (Lasers and Applications)}. Each paper contains \textbf{30 Multiple-Choice Questions (MCQs)} carrying \textbf{1 mark each} (Total = \textbf{30 Marks}, Time Allowed = \textbf{60 Minutes}). Complete answer keys and technical rationales follow each set.

\newpage
\input{ca1/set_a}
\newpage
\input{ca1/set_b}
\newpage
\input{ca1/set_c}
\newpage
\input{ca1/set_d}

% ==============================================================================
% SECTION 2: CONTINUOUS ASSESSMENT 2 (CA-2) --- IN-DEPTH PROJECT ASSIGNMENTS
% ==============================================================================
\chapter{Continuous Assessment 2 (CA-2) Suite}
\label{chap:ca2}
\noindent
Continuous Assessment 2 evaluates in-depth assignment files, theoretical derivations, and applied physics project reports across the curriculum. Four comprehensive project reports are detailed with complete mathematical models, engineering applications, and experimental verifications.

\newpage
\input{ca2/set_a}
\newpage
\input{ca2/set_b}
\newpage
\input{ca2/set_c}
\newpage
\input{ca2/set_d}

% ==============================================================================
% SECTION 3: MID-TERM EXAMINATION SUITE --- UNITS 1, 2 & 3 (30 MCQs)
% ==============================================================================
\chapter{Mid-Term Examination Suite (30 MCQs --- 30 Marks)}
\label{chap:midterm}
\noindent
The Mid-Term Examination is an objective assessment evaluating students across \textbf{Unit 1 (Electromagnetic Theory)}, \textbf{Unit 2 (Lasers)}, and \textbf{Unit 3 (Fiber Optics)}. Each paper consists of \textbf{30 Multiple-Choice Questions (MCQs) carrying 1 mark each} (10 from Unit 1, 10 from Unit 2, 10 from Unit 3) with a negative marking deduction of \textbf{0.25 marks} per incorrect answer (Total = \textbf{30 Marks}, Time Allowed = \textbf{90 Minutes}).

\newpage
\input{midterm/set_a}
\newpage
\input{midterm/set_b}
\newpage
\input{midterm/set_c}
\newpage
\input{midterm/set_d}

% ==============================================================================
% SECTION 4: END-TERM EXAMINATION SUITE --- UNITS 1 TO 6 (60 MCQs)
% ==============================================================================
\chapter{End-Term Examination Suite (60 MCQs Comprehensive)}
\label{chap:endterm}
\noindent
The End-Term Examination is the comprehensive university final examination (Total = \textbf{60 Marks}, Time Allowed = \textbf{3 Hours}):
\begin{itemize}[leftmargin=8mm]
    \item \textbf{60 Multiple-Choice Questions (MCQs)} carrying \textbf{1 mark each} (Negative marking deduction of \textbf{0.25 marks} per incorrect answer).
    \item \textbf{Curriculum Weightage:} Weighted heavily towards \textbf{Units 4, 5, and 6} (~40 MCQs from Quantum Mechanics, Semiconductors, Materials and ~20 MCQs from Units 1--3).
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
with open("Physics_Exam_Companion/frontmatter/cover.tex", "w") as f:
    f.write(r"""\begin{titlepage}
\centering
\vspace*{1.5cm}
{\Huge \textbf{\color{LPUNavy}PHY110: Engineering Physics}}\\[0.5cm]
{\LARGE \textbf{\color{LPUOrange}Examination Companion \& Solved Question Papers}}\\[0.3cm]
{\large \textit{4 CA-1 Sets + 4 CA-2 Project Reports + 4 Mid-Term Papers + 4 End-Term Papers}}\\[2cm]

\rule{\linewidth}{1.5pt}\\[0.5cm]
{\large \textbf{B.Tech / B.E. Semester 1 Curriculum | Lovely Professional University}}\\[0.5cm]
\rule{\linewidth}{1.5pt}\\[2.5cm]

\vfill
{\large \textbf{LPU Engineering Open Publishing Initiative}}\\[0.2cm]
{\small Independent Open-Source Academic Guide Series}
\end{titlepage}
\newpage
""")

with open("Physics_Exam_Companion/frontmatter/blueprint.tex", "w") as f:
    f.write(r"""\chapter*{Official Examination Blueprint \& Marking Regulations}
\addcontentsline{toc}{chapter}{Official Examination Blueprint \& Marking Regulations}

This Examination Companion provides complete mock papers and in-depth assignments strictly adhering to the official LPU examination architecture for \textbf{PHY110: Engineering Physics}:

\begin{table}[htbp]
\centering
\caption{\textbf{PHY110 Assessment Suite Architecture}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l p{3.2cm} p{2.8cm} c X}
\toprule
\textbf{Assessment} & \textbf{Syllabus Scope} & \textbf{Format} & \textbf{Marks} & \textbf{Exam Regulations} \\
\midrule
\textbf{CA-1 (4 Sets)} & Unit 1 \& Unit 2 & 30 MCQs & 30 & 15 MCQs from Unit 1, 15 MCQs from Unit 2. Time: 60 Mins. \\
\addlinespace
\textbf{CA-2 (4 Sets)} & Units 1 to 6 & In-depth Project Reports & 30 & Structured investigation report, experimental analysis, and mathematical modeling. \\
\addlinespace
\textbf{Mid-Term (4 Sets)} & Unit 1, Unit 2, Unit 3 & 30 MCQs & 30 & 10 MCQs from Unit 1, 10 from Unit 2, 10 from Unit 3. Negative marking $-0.25$ marks. Time: 90 Mins. \\
\addlinespace
\textbf{End-Term (4 Sets)} & Units 1 to 6 & 60 MCQs & 60 & Comprehensive university examination: 60 MCQs (majority from Units 4, 5, 6). Negative marking $-0.25$ marks. Time: 3 Hours. \\
\bottomrule
\end{tabularx}
\end{table}

\newpage
""")

print("Exam Companion base setup updated.")
