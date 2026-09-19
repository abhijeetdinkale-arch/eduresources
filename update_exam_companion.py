import os

print("Updating MTH165 Exam Companion...")

# Update main.tex
with open("MTH165_Exam_Companion/main.tex", "w") as f:
    f.write(r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{exam_style}

\title{MTH165: Mathematics for Engineers --- Examination Companion \& Solved Question Papers}
\author{LPU Engineering Open Series}
\date{Academic Year 2024--2025 / 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}
\input{frontmatter/blueprint}
\input{frontmatter/formulas_quick_ref}

\tableofcontents
\newpage

\mainmatter

% ==============================================================================
% SECTION 1: CONTINUOUS ASSESSMENT 1 (CA-1) --- UNITS 1 & 2
% ==============================================================================
\chapter{Continuous Assessment 1 (CA-1) Suite}
\label{chap:ca1}
\noindent
Continuous Assessment 1 evaluates students on \textbf{Unit 1 (Matrix Methods and Linear Systems)} and \textbf{Unit 2 (Differential Calculus and Applications)}. Each paper contains \textbf{6 questions} carrying \textbf{5 marks each}, and students attempt \textbf{5 questions} (Total = \textbf{30 Marks}, Time Allowed = \textbf{60 Minutes}).

\newpage
\input{ca1/set_a}
\input{ca1/set_b}
\input{ca1/set_c}

% ==============================================================================
% SECTION 2: MID-TERM EXAMINATION SUITE --- UNITS 1, 2 & 3
% ==============================================================================
\chapter{Mid-Term Examination Suite (30 MCQs --- 30 Marks)}
\label{chap:midterm}
\noindent
The Mid-Term Examination is an objective assessment evaluating students across \textbf{Unit 1 (Matrices)}, \textbf{Unit 2 (Differential Calculus)}, and \textbf{Unit 3 (Integral Calculus)}. Each paper consists of \textbf{30 Multiple-Choice Questions (MCQs)} carrying \textbf{1 mark each} (10 from Unit 1, 10 from Unit 2, 10 from Unit 3) with a negative marking deduction of \textbf{0.25 marks} per incorrect answer (Total = \textbf{30 Marks}, Time Allowed = \textbf{90 Minutes}).

\newpage
\input{midterm/set_a}
\input{midterm/set_b}
\input{midterm/set_c}

% ==============================================================================
% SECTION 3: CONTINUOUS ASSESSMENT 2 (CA-2) --- UNITS 4 & 5
% ==============================================================================
\chapter{Continuous Assessment 2 (CA-2) Suite}
\label{chap:ca2}
\noindent
Continuous Assessment 2 evaluates students on \textbf{Unit 4 (Multivariate Differentiation)} and \textbf{Unit 5 (Multivariable Integration and Applications)}. Each paper contains \textbf{6 questions} carrying \textbf{5 marks each}, and students attempt \textbf{5 questions} (Total = \textbf{30 Marks}, Time Allowed = \textbf{60 Minutes}).

\newpage
\input{ca2/set_a}
\input{ca2/set_b}
\input{ca2/set_c}

% ==============================================================================
% SECTION 4: END-TERM EXAMINATION SUITE --- UNITS 1 TO 6 (70 MARKS)
% ==============================================================================
\chapter{End-Term Examination Suite (70 Marks Comprehensive)}
\label{chap:endterm}
\noindent
The End-Term Examination is the comprehensive university final examination (Total = \textbf{70 Marks}, Time Allowed = \textbf{3 Hours}):
\begin{itemize}[leftmargin=8mm]
    \item \textbf{Part A (Objective --- 30 Marks):} 30 MCQs strictly testing \textbf{Unit 4, Unit 5, and Unit 6} (10 MCQs from each unit, 1 mark each, negative marking $-0.25$).
    \item \textbf{Part B (Descriptive --- 40 Marks):} 5 comprehensive questions of 10 marks each (3 questions from Units 4, 5, 6 and 2 questions from Units 1--6). Students must \textbf{attempt any 4 questions} ($4 \times 10 = \mathbf{40\text{ Marks}}$).
\end{itemize}

\newpage
\input{endterm/set_a}
\input{endterm/set_b}
\input{endterm/set_c}

\end{document}
""")

# Blueprint in frontmatter
with open("MTH165_Exam_Companion/frontmatter/blueprint.tex", "w") as f:
    f.write(r"""\chapter*{Official Examination Architecture \& Blueprint}
\addcontentsline{toc}{chapter}{Official Examination Architecture \& Blueprint}

This Examination Companion provides verified model question papers and complete step-by-step solutions designed strictly to mirror the latest Lovely Professional University (LPU) examination structure for \textbf{MTH165: Mathematics for Engineers}:

\begin{table}[htbp]
\centering
\caption{\textbf{MTH165 Examination Structure and Marking Scheme}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l p{3.2cm} p{2.8cm} c X}
\toprule
\textbf{Assessment} & \textbf{Syllabus Scope} & \textbf{Format} & \textbf{Marks} & \textbf{Instructions \& Rules} \\
\midrule
\textbf{CA-1} & Unit 1 \& Unit 2 & 6 Subjective Qs & 30 & Attempt any 5 out of 6 questions ($5 \times 6\text{M} = 30\text{M}$ or $5 \times 5\text{M} + 5\text{M}$ step grading). Time: 60 mins. \\
\addlinespace
\textbf{Mid-Term} & Unit 1, Unit 2, Unit 3 & 30 MCQs & 30 & 10 MCQs per unit. Negative marking $-0.25$ marks for wrong answers. Time: 90 mins. \\
\addlinespace
\textbf{CA-2} & Unit 4 \& Unit 5 & 6 Subjective Qs & 30 & Attempt any 5 out of 6 questions ($5 \times 6\text{M} = 30\text{M}$). Time: 60 mins. \\
\addlinespace
\textbf{End-Term} & Units 1 to 6 & \textbf{Part A}: 30 MCQs \newline \textbf{Part B}: 5 Subj Qs & 70 & \textbf{Part A}: 30 MCQs from Units 4, 5, 6 (10 each). \newline \textbf{Part B}: 5 Qs of 10M (3 from U4-6, 2 from U1-6), attempt any 4 ($4 \times 10 = 40\text{M}$). Time: 3 Hours. \\
\bottomrule
\end{tabularx}
\end{table}

\newpage
""")

print("Exam companion main structure updated.")
