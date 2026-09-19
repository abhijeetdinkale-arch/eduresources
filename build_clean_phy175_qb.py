import os
import subprocess

print("Writing clean Question Bank chapters for all 6 units...")

os.makedirs("PHY175_Question_Bank/chapters", exist_ok=True)

# Master tex for Question Bank
main_tex = r"""\documentclass[11pt,a4paper,twoside,openright]{report}
\usepackage{qb_style}

\title{\Huge\bfseries\color{LPUNavy} PHY175: Modern Physics \& Electronics\\[0.5em]
\Large\color{LPUOrange} Official Examination Question Bank \& Solution Manual\\[1em]
\normalsize\color{DarkSlate} Comprehensive Resource with 360 MCQs (Categorized by Difficulty) \& 90 Solved University Theory Questions}
\author{\textbf{LPU Engineering Open Series}}
\date{Academic Year 2026--2027}

\begin{document}
\maketitle

\chapter*{About the Question Bank}
This comprehensive Question Bank covers all 6 units of the \textbf{PHY175: Modern Physics and Electronics} curriculum:
\begin{itemize}
    \item \textbf{Unit 1: Solid State Physics} (Drude theory, Fermi statistics, Effective mass, Hall effect, Semiconductors, Solar cells)
    \item \textbf{Unit 2: Fundamentals of Electricity and Devices} (Circuit laws, Voltage/Current division, Diodes, BJT, CMOS, Memory, AI accelerators, Sensors, Computer Networks)
    \item \textbf{Unit 3: Introduction to Number System and Logic Gates} (Radix conversion, Gray code, Excess-3, BCD, Complements, Boolean algebra, K-Maps, Hazards)
    \item \textbf{Unit 4: Introduction to Combinational Logic Circuits} (Adders, Subtractors, CLA, Multiplexers, Decoders, Priority Encoders, Comparators)
    \item \textbf{Unit 5: Introduction to Sequential Logic Circuits} (Latches, Flip-Flops, Master-Slave JK, Flip-Flop conversions, Shift registers, Ripple counters)
    \item \textbf{Unit 6: Introduction of Arduino and Sensors} (ADC, PWM, Uno pinout, IR obstacle sensor, LDR photoresistor, Ultrasonic HC-SR04, DHT11/DHT22)
\end{itemize}

\tableofcontents

\include{chapters/qb-unit1}
\include{chapters/qb-unit2}
\include{chapters/qb-unit3}
\include{chapters/qb-unit4}
\include{chapters/qb-unit5}
\include{chapters/qb-unit6}

\end{document}
"""

with open("PHY175_Question_Bank/main.tex", "w") as f:
    f.write(main_tex)

# Style file
qb_style = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{qb_style}[2026/09/18 v1.0 PHY175 Question Bank Style System]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=20mm,top=24mm,bottom=24mm,headheight=25pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts,mathtools,bm}
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
\RequirePackage[hidelinks,colorlinks=true,linkcolor=NavyBlue,urlcolor=BrickRed,citecolor=NavyBlue]{hyperref}

\definecolor{LPUNavy}{RGB}{15, 32, 67}
\definecolor{LPUOrange}{RGB}{201, 74, 28}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{LightBg}{RGB}{246, 248, 252}
\definecolor{BorderGray}{RGB}{205, 215, 225}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{LPUNavy}\textbf{PHY175: Modern Physics \& Electronics --- Question Bank}}
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
    title={Theory Question #2 \hfill [University Exam / Analytical]},
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
    title={\textbf{\color{LPUNavy}Comprehensive Step-by-Step Solution \& Derivation:}},
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
"""

with open("PHY175_Question_Bank/qb_style.sty", "w") as f:
    f.write(qb_style)

def make_clean_unit_tex(unit_num, title, mcqs, theory_qs):
    content = f"\\chapter{{Unit {unit_num}: {title}}}\n\n"
    content += "\\section{Section 1: Chapter-Wise Multiple-Choice Questions (60 MCQs)}\n\n"
    
    content += "\\subsection*{Part I: Foundational Level (Questions 1 to 20)}\n"
    for i in range(20):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"
        
    content += "\n\\subsection*{Part II: Intermediate Analytical Level (Questions 21 to 40)}\n"
    for i in range(20, 40):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"
        
    content += "\n\\subsection*{Part III: Advanced Mastery Level (Questions 41 to 60)}\n"
    for i in range(40, 60):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    # Multi-page friendly Answer Key
    content += r"""
\newpage
\section{Section 2: Complete Answer Key \& Technical Rationales}

\subsection*{Part A: Questions 1 to 30}
\begin{table}[htbp]
\centering
\caption{\textbf{Answer Key with Rationales (Questions 1 to 30)}}
\vspace{2mm}
\small
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+1, mcqs[i][5], mcqs[i][6])
        q2 = (i+16, mcqs[i+15][5], mcqs[i+15][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}

\subsection*{Part B: Questions 31 to 60}
\begin{table}[htbp]
\centering
\caption{\textbf{Answer Key with Rationales (Questions 31 to 60)}}
\vspace{2mm}
\small
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+31, mcqs[i+30][5], mcqs[i+30][6])
        q2 = (i+46, mcqs[i+45][5], mcqs[i+45][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}

\newpage
\section{Section 3: Comprehensive Theory Questions \& Worked Solutions}
"""
    for idx, t in enumerate(theory_qs, 1):
        content += f"\\begin{{theoryq}}{{{unit_num}.{idx}}}\n{t['q']}\n\\end{{theoryq}}\n\n"
        content += f"\\begin{{theorysol}}\n{t['sol']}\n\\end{{theorysol}}\n\n\\vspace{{3mm}}\n\n"

    with open(f"PHY175_Question_Bank/chapters/qb-unit{unit_num}.tex", "w") as f:
        f.write(content)

print("Builder helper defined.")
