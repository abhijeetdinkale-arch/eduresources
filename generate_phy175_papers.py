import os
import subprocess

print("Writing unified master generator for all PHY175 Books...")

# Directories
DIRS = [
    "PHY175",
    "PHY175_Revision_Book",
    "PHY175_Formula_Book",
    "PHY175_Handwritten_Notes",
    "PHY175_Question_Bank",
    "PHY175_Sample_Question_Papers"
]

for d in DIRS:
    os.makedirs(f"{d}/chapters", exist_ok=True)
    os.makedirs(f"{d}/frontmatter", exist_ok=True)

# -------------------------------------------------------------
# SAMPLE QUESTION PAPERS
# -------------------------------------------------------------
papers_style = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{exam_style}[2026/09/18 v1.0 PHY175 Exam Paper Style System]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=20mm,top=22mm,bottom=22mm,headheight=20pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts,mathtools,bm}
\RequirePackage[dvipsnames]{xcolor}
\RequirePackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\RequirePackage{enumitem}
\RequirePackage{fancyhdr}
\RequirePackage{tabularx}
\RequirePackage{titlesec}
\RequirePackage{booktabs}
\RequirePackage{microtype}

\definecolor{ExamNavy}{RGB}{15, 32, 67}
\definecolor{ExamRed}{RGB}{180, 20, 20}
\definecolor{ExamBg}{RGB}{248, 249, 252}
\definecolor{SolutionBg}{RGB}{240, 253, 244}
\definecolor{SolutionBorder}{RGB}{34, 197, 94}

\RequirePackage[hidelinks,colorlinks=true,linkcolor=ExamNavy,urlcolor=ExamRed,citecolor=ExamNavy]{hyperref}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{ExamNavy}\textbf{PHY175: Modern Physics \& Electronics --- Model Examination Suite}}
\fancyhead[R]{\small\color{ExamRed}\textbf{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.5pt}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{ExamNavy}}{\chaptertitlename\ \thechapter}{10pt}{\LARGE}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{ExamNavy}}{\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{ExamRed}}{\thesubsection}{1em}{}

\newtcolorbox{examqbox}[2][]{
    enhanced, breakable, colback=ExamBg, colframe=ExamNavy,
    fonttitle=\bfseries\color{white}, coltitle=white,
    title={Question #2}, boxrule=1pt, arc=2mm,
    top=2mm, bottom=2mm, left=3mm, right=3mm, #1
}

\newtcolorbox{solbox}[1][Detailed Solution \& Marking Scheme]{
    enhanced, breakable, colback=SolutionBg, colframe=SolutionBorder,
    coltitle=black, title={\textbf{#1}}, boxrule=0.8pt, arc=2mm,
    top=2mm, bottom=2mm, left=3mm, right=3mm
}
"""

with open("PHY175_Sample_Question_Papers/exam_style.sty", "w") as f:
    f.write(papers_style)

# Papers Master Tex
papers_main = r"""\documentclass[11pt,a4paper,twoside,openright]{report}
\usepackage{exam_style}

\title{\Huge\bfseries\color{ExamNavy} PHY175: Modern Physics \& Electronics\\[0.5em]
\Large\color{ExamRed} Complete Model Examination Papers \& Full Solutions Manual\\[1em]
\normalsize Includes CA-1, CA-2, Mid-Term (MTE), and End-Term (ETE) Full-Length Papers}
\author{\textbf{LPU Engineering Open Series}}
\date{Academic Year 2026--2027}

\begin{document}
\maketitle

\chapter*{About the Examination Suite}
This volume contains official-pattern model examination papers modeled strictly on the LPU examination structure:
\begin{itemize}
    \item \textbf{Continuous Assessment 1 (CA-1):} Covering Units 1 and 2 (Solid State Physics \& Circuit Devices).
    \item \textbf{Continuous Assessment 2 (CA-2):} Covering Units 3 and 4 (Number Systems, Logic Gates \& Combinational Logic).
    \item \textbf{Mid-Term Examination (MTE):} Full 50-mark Mid-Term model covering Units 1, 2, and 3.
    \item \textbf{End-Term Examination (ETE):} Full 100-mark comprehensive university examination covering all 6 units with complete solutions and step-by-step marking rubrics.
\end{itemize}

\tableofcontents

\include{chapters/paper-ca1}
\include{chapters/paper-ca2}
\include{chapters/paper-midterm}
\include{chapters/paper-endterm}

\end{document}
"""

with open("PHY175_Sample_Question_Papers/main.tex", "w") as f:
    f.write(papers_main)

# CA-1 Paper
ca1_tex = r"""\chapter{Continuous Assessment 1 (CA-1) Model Paper}
\section*{Course: PHY175 $\cdot$ Max Marks: 30 $\cdot$ Time: 60 Minutes}

\subsection*{Section A: Multiple-Choice Questions (10 Marks, 1 Mark Each)}
\begin{enumerate}[leftmargin=*]
    \item According to Drude theory, electrical conductivity $\sigma$ is proportional to:
    \begin{enumerate}[label=(\alph*)]
        \item $\tau / n$ \item $n \tau$ \item $1/(n\tau)$ \item $m / (n\tau)$
    \end{enumerate}
    \item At $0\,\text{K}$, the occupation probability for states with $E > E_F$ is:
    \begin{enumerate}[label=(\alph*)]
        \item $1$ \item $0.5$ \item $0$ \item $e^{-1}$
    \end{enumerate}
    \item The Hall coefficient $R_H$ is negative for:
    \begin{enumerate}[label=(\alph*)]
        \item Holes \item Electrons \item Positive ions \item Neutrons
    \end{enumerate}
    \item A bridge rectifier supplied with $50\,\text{Hz}$ AC has a ripple frequency of:
    \begin{enumerate}[label=(\alph*)]
        \item $25\,\text{Hz}$ \item $50\,\text{Hz}$ \item $100\,\text{Hz}$ \item $200\,\text{Hz}$
    \end{enumerate}
    \item In an active-mode BJT, the base-emitter junction is:
    \begin{enumerate}[label=(\alph*)]
        \item Reverse biased \item Forward biased \item Unbiased \item Breakdown biased
    \end{enumerate}
\end{enumerate}

\subsection*{Section B: Analytical \& Numerical Problems (20 Marks)}

\begin{examqbox}{1 [5 Marks]}
A semiconductor slab of thickness $t = 0.5\,\text{mm}$ carries a current of $2.0\,\text{mA}$ in a magnetic field $B = 0.50\,\text{T}$. If the carrier density is $n = 5.0 \times 10^{22}\,\text{m}^{-3}$, compute the Hall voltage $V_H$ and state which carrier type corresponds to a negative Hall voltage.
\end{examqbox}

\begin{solbox}
\textbf{Given:} $t = 0.50 \times 10^{-3}\,\text{m}, I = 2.0 \times 10^{-3}\,\text{A}, B = 0.50\,\text{T}, n = 5.0 \times 10^{22}\,\text{m}^{-3}, e = 1.6 \times 10^{-19}\,\text{C}$.
\begin{equation}
V_H = \frac{I B}{n e t} = \frac{(2.0 \times 10^{-3})(0.50)}{(5.0 \times 10^{22})(1.6 \times 10^{-19})(0.50 \times 10^{-3})} = \frac{1.0 \times 10^{-3}}{4.0} = 0.25\,\text{mV}
\end{equation}
A negative Hall voltage indicates that electrons (negative charge carriers) are the majority carriers.
\end{solbox}

\begin{examqbox}{2 [5 Marks]}
Explain the concept of effective mass $m^*$ for electrons in a crystal lattice. Why can transport near the top of the valence band be described using positively charged holes?
\end{examqbox}

\begin{solbox}
Under crystal periodic potential, acceleration $a = \frac{1}{\hbar^2}\frac{d^2E}{dk^2} F_{ext} \implies m^* = \frac{\hbar^2}{d^2E/dk^2}$. Near the valence band maximum, band curvature is negative ($\frac{d^2E}{dk^2} < 0$), causing electrons to accelerate opposite to external forces. To avoid negative mass notation, this behavior is represented by fictitious \textbf{holes} carrying positive charge $+e$ and positive effective mass $m_h^* = -m_e^* > 0$.
\end{solbox}

\begin{examqbox}{3 [10 Marks]}
(a) Derive the dynamic power dissipation formula $P_{dyn} = \alpha C V_{DD}^2 f$ for a CMOS logic circuit.\\
(b) A CMOS processor operates at $1.2\,\text{V}$ and $500\,\text{MHz}$ with $C=20\,\text{pF}$ and $\alpha=0.25$. Calculate its initial dynamic power. If the voltage is reduced to $1.0\,\text{V}$ and frequency to $400\,\text{MHz}$, determine the new power and percentage savings.
\end{examqbox}

\begin{solbox}
\textbf{(a) Derivation:} Each clock cycle charging load capacitance $C$ to $V_{DD}$ draws energy $E_{drawn} = C V_{DD}^2$. Over frequency $f$ with activity factor $\alpha$, $P_{dyn} = \alpha C V_{DD}^2 f$.\\
\textbf{(b) Calculations:}\\
1. Initial: $P_{init} = (0.25)(20 \times 10^{-12})(1.2)^2(500 \times 10^6) = 3.60\,\text{mW}$.\\
2. New: $P_{new} = (0.25)(20 \times 10^{-12})(1.0)^2(400 \times 10^6) = 2.00\,\text{mW}$.\\
3. Percentage power reduction $= \frac{3.60 - 2.00}{3.60} \times 100\% = 44.4\%$.
\end{solbox}
"""

with open("PHY175_Sample_Question_Papers/chapters/paper-ca1.tex", "w") as f:
    f.write(ca1_tex)

# CA-2 Paper
ca2_tex = r"""\chapter{Continuous Assessment 2 (CA-2) Model Paper}
\section*{Course: PHY175 $\cdot$ Max Marks: 30 $\cdot$ Time: 60 Minutes}

\subsection*{Section A: Multiple-Choice Questions (10 Marks, 1 Mark Each)}
\begin{enumerate}[leftmargin=*]
    \item The 2's complement of 4-bit binary $0101_2$ is:
    \begin{enumerate}[label=(\alph*)]
        \item $1110_2$ \item $1011_2$ \item $1100_2$ \item $1010_2$
    \end{enumerate}
    \item Gray code for binary $1011_2$ is:
    \begin{enumerate}[label=(\alph*)]
        \item $1110$ \item $1010$ \item $1001$ \item $1101$
    \end{enumerate}
    \item The Sum output $S$ of a full adder with inputs $A, B, C_{in}$ is:
    \begin{enumerate}[label=(\alph*)]
        \item $A + B + C_{in}$ \item $A \oplus B \oplus C_{in}$ \item $AB + BC_{in}$ \item $A \odot B \odot C_{in}$
    \end{enumerate}
    \item How many select lines are required for an 8-to-1 multiplexer?
    \begin{enumerate}[label=(\alph*)]
        \item 2 \item 3 \item 4 \item 8
    \end{enumerate}
    \item A 2-to-4 decoder with active-high outputs activates how many lines for input $10_2$?
    \begin{enumerate}[label=(\alph*)]
        \item Only $Y_0$ \item Only $Y_1$ \item Only $Y_2$ \item Only $Y_3$
    \end{enumerate}
\end{enumerate}

\subsection*{Section B: Design \& Synthesis Problems (20 Marks)}

\begin{examqbox}{1 [5 Marks]}
Minimize the Boolean function $F(A,B,C,D) = \sum m(1,3,9,11,12,14) + d(0,2,8,10)$ using a 4-variable Karnaugh Map.
\end{examqbox}

\begin{solbox}
\textbf{K-Map Analysis:}\\
1. Group octet of cells $\{0, 1, 2, 3, 8, 9, 10, 11\}$ (rows $00, 10$) $\implies \bar{B}$.\\
2. Group quad of cells $\{8, 10, 12, 14\}$ (row $10, 11$ columns $00, 10$) $\implies A\bar{D}$.\\
\textbf{Minimized SOP Expression:} $F = \bar{B} + A\bar{D}$.
\end{solbox}

\begin{examqbox}{2 [5 Marks]}
Design a Full Subtractor using two Half Subtractors and an OR gate. Write the complete truth table and Boolean expressions for Difference ($D$) and Borrow-out ($B_{out}$).
\end{examqbox}

\begin{solbox}
1. First Half Subtractor: $D_1 = A \oplus B, \quad B_1 = \bar{A}B$.\\
2. Second Half Subtractor: $D = D_1 \oplus B_{in} = A \oplus B \oplus B_{in}, \quad B_2 = \bar{D}_1 B_{in} = \overline{(A \oplus B)} B_{in}$.\\
3. Final Borrow: $B_{out} = B_1 + B_2 = \bar{A}B + \bar{A}B_{in} + BB_{in}$.
\end{solbox}

\begin{examqbox}{3 [10 Marks]}
Implement the Boolean logic function $F(A,B,C) = \sum m(1,2,5,7)$ using:\\
(a) A 4-to-1 Multiplexer with select lines connected to $B$ and $C$.\\
(b) A 3-to-8 Decoder with active-high outputs.
\end{examqbox}

\begin{solbox}
\textbf{(a) 4:1 MUX Implementation ($S_1=B, S_0=C$):}\\
- $BC = 00$: $F(0,0,0)=0, F(1,0,0)=0 \implies I_0 = 0$.\\
- $BC = 01$: $F(0,0,1)=1, F(1,0,1)=1 \implies I_1 = 1$.\\
- $BC = 10$: $F(0,1,0)=1, F(1,1,0)=0 \implies I_2 = \bar{A}$.\\
- $BC = 11$: $F(0,1,1)=0, F(1,1,1)=1 \implies I_3 = A$.\\
Input vector: $(I_0, I_1, I_2, I_3) = (0, 1, \bar{A}, A)$.\\
\textbf{(b) 3-to-8 Decoder Implementation:}\\
Connect $A,B,C$ to decoder inputs. Connect outputs $Y_1, Y_2, Y_5, Y_7$ to a 4-input OR gate: $F = Y_1 + Y_2 + Y_5 + Y_7$.
\end{solbox}
"""

with open("PHY175_Sample_Question_Papers/chapters/paper-ca2.tex", "w") as f:
    f.write(ca2_tex)

# Midterm Paper
midterm_tex = r"""\chapter{Mid-Term Examination (MTE) Model Paper}
\section*{Course: PHY175 $\cdot$ Max Marks: 50 $\cdot$ Time: 120 Minutes}

\subsection*{Part A: Short Answer Questions (10 Marks, 2 Marks Each)}
\begin{enumerate}[leftmargin=*]
    \item Define Fermi energy at absolute zero.
    \item State the difference between direct and indirect band gap semiconductors.
    \item Explain the physical significance of the Hall coefficient sign.
    \item State De Morgan's laws of Boolean algebra.
    \item Write the 2's complement representation of decimal $-25$ in 8 bits.
\end{enumerate}

\subsection*{Part B: Medium Analytical Questions (20 Marks, 5 Marks Each)}

\begin{examqbox}{1 [5 Marks]}
A 3D free electron gas at $0\,\text{K}$ has electron density $n_1$. If the density is increased to $8n_1$, prove that the Fermi energy quadruples ($E_{F2} = 4E_{F1}$).
\end{examqbox}

\begin{solbox}
Density of states integration yields $E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$. Therefore, $\frac{E_{F2}}{E_{F1}} = \left(\frac{n_2}{n_1}\right)^{2/3} = (8)^{2/3} = (2^3)^{2/3} = 4$.
\end{solbox}

\begin{examqbox}{2 [5 Marks]}
In an intrinsic semiconductor, electron mobility is 3 times hole mobility ($\mu_e = 3\mu_h$). Calculate the percentage of total electrical conductivity contributed by electrons.
\end{examqbox}

\begin{solbox}
Total conductivity $\sigma = n_i e(\mu_e + \mu_h)$. Fractional electron conductivity is $\frac{\sigma_e}{\sigma} = \frac{n_i e \mu_e}{n_i e(\mu_e + \mu_h)} = \frac{3\mu_h}{3\mu_h + \mu_h} = \frac{3}{4} = 75\%$.
\end{solbox}

\begin{examqbox}{3 [5 Marks]}
A full-wave bridge rectifier is supplied with a $15\,\text{V}$ peak, $50\,\text{Hz}$ sinusoidal input. Diodes have $V_D = 0.7\,\text{V}$. A $1000\,\mu\text{F}$ capacitor filter and $1\,\text{k}\Omega$ load are connected. Compute peak DC voltage, ripple frequency, and peak-to-peak ripple voltage.
\end{examqbox}

\begin{solbox}
1. $V_{peak} = 15 - 2(0.7) = 13.6\,\text{V}$.\\
2. $f_{ripple} = 2 \times 50 = 100\,\text{Hz}$.\\
3. $V_{r(pp)} = \frac{V_{peak}}{2 f C R_L} = \frac{13.6}{2(50)(1000 \times 10^{-6})(1000)} = \frac{13.6}{100} = 0.136\,\text{V}$.
\end{solbox}

\begin{examqbox}{4 [5 Marks]}
Convert hexadecimal $(3\text{A}7.\text{C})_{16}$ into binary, octal, and decimal representations.
\end{examqbox}

\begin{solbox}
1. Binary: $0011\,1010\,0111.1100_2$.\\
2. Octal: $(1647.6)_8$.\\
3. Decimal: $3(256) + 10(16) + 7 + 12/16 = 768 + 160 + 7 + 0.75 = 935.75_{10}$.
\end{solbox}

\subsection*{Part C: Comprehensive Long Questions (20 Marks, 10 Marks Each)}

\begin{examqbox}{5 [10 Marks]}
(a) Derive the expression for the Hall voltage $V_H = \frac{IB}{nqt}$ and Hall coefficient $R_H$.\\
(b) A rectangular copper strip of thickness $t = 0.1\,\text{mm}$ carries $I = 10\,\text{A}$ in $B = 1.2\,\text{T}$. If $n = 8.5 \times 10^{28}\,\text{m}^{-3}$, find $V_H$.
\end{examqbox}

\begin{solbox}
\textbf{(a) Derivation:} Balancing magnetic Lorentz force $F_B = q v_d B$ with electrostatic Hall force $F_E = q E_H$ gives $E_H = v_d B$. With $v_d = \frac{I}{n q w t}$, $V_H = E_H w = \frac{I B}{n q t}$.\\
\textbf{(b) Calculation:} $V_H = \frac{(10)(1.2)}{(8.5 \times 10^{28})(1.6 \times 10^{-19})(0.1 \times 10^{-3})} = \frac{12}{1.36 \times 10^6} = 8.82\,\mu\text{V}$.
\end{solbox}

\begin{examqbox}{6 [10 Marks]}
(a) Minimize $F(A,B,C,D) = \sum m(0, 2, 5, 7, 8, 10, 13, 15)$ using a K-map.\\
(b) Explain static-1 hazards and write the hazard-free SOP expression.
\end{examqbox}

\begin{solbox}
\textbf{(a) K-Map Reduction:} Corner group $\{0, 2, 8, 10\} \implies \bar{B}\bar{D}$; Central group $\{5, 7, 13, 15\} \implies BD$. Minimized: $F = \bar{B}\bar{D} + BD$.\\
\textbf{(b) Hazard Analysis:} Since the groups are non-overlapping, input switching transitions between $B=0$ and $B=1$ can glitch. Adding consensus term $\bar{D}D=0$ is not needed here as variables are distinct, but for adjacent SOP terms, consensus loops eliminate hazards.
\end{solbox}
"""

with open("PHY175_Sample_Question_Papers/chapters/paper-midterm.tex", "w") as f:
    f.write(midterm_tex)

# Endterm Paper
endterm_tex = r"""\chapter{End-Term Examination (ETE) Full Syllabus Model Paper}
\section*{Course: PHY175 $\cdot$ Max Marks: 100 $\cdot$ Time: 180 Minutes}

\subsection*{Section A: 20 Objective MCQs (20 Marks)}
\begin{enumerate}[leftmargin=*]
    \item Electrical conductivity in Drude model is $\sigma = \frac{ne^2\tau}{m}$.
    \item At $T > 0\,\text{K}$, Fermi-Dirac occupancy probability at $E = E_F$ is $50\%$.
    \item Direct band gap semiconductor recombination conserves crystal momentum without phonons.
    \item CMOS dynamic power scales with $V_{DD}^2$.
    \item In a 4-to-1 MUX, the number of select lines is 2.
    \item Master-Slave JK flip-flop eliminates the race-around condition.
    \item Arduino Uno 10-bit ADC provides 1024 quantization levels.
    \item Ultrasonic HC-SR04 distance formula is $d = \frac{v \cdot t}{2}$.
    \item BCD addition requires adding $+6$ ($0110_2$) when digit sum exceeds 9.
    \item Optical fiber signal confinement relies on Total Internal Reflection (TIR).
\end{enumerate}

\subsection*{Section B: Analytical Problems (40 Marks, 8 Marks Each)}

\begin{examqbox}{1 [8 Marks]}
Derive the expression for the maximum operating clock frequency $f_{max} = \frac{1}{N \cdot t_{pd} + t_s}$ of an $N$-bit asynchronous ripple counter. If $N=4, t_{pd}=25\,\text{ns}, t_s=10\,\text{ns}$, calculate $f_{max}$.
\end{examqbox}

\begin{solbox}
In an $N$-bit ripple counter, the clock ripples through all $N$ stages serially. Total propagation delay before output stabilizes is $T_{ripple} = N \cdot t_{pd}$. Adding setup time $t_s$ for downstream logic gives minimum clock period $T_{min} = N \cdot t_{pd} + t_s$. Hence $f_{max} = \frac{1}{T_{min}} = \frac{1}{4(25\,\text{ns}) + 10\,\text{ns}} = \frac{1}{110\,\text{ns}} \approx 9.09\,\text{MHz}$.
\end{solbox}

\begin{examqbox}{2 [8 Marks]}
Convert a JK Flip-Flop into a D Flip-Flop. Show the complete conversion table, K-maps, and logic gate schematic.
\end{examqbox}

\begin{solbox}
Excitation requirements for D flip-flop ($Q_{n+1} = D$):
- When $D=0$: $Q_n=0 \to Q_{n+1}=0 \implies J=0, K=X$; $Q_n=1 \to Q_{n+1}=0 \implies J=X, K=1$.
- When $D=1$: $Q_n=0 \to Q_{n+1}=1 \implies J=1, K=X$; $Q_n=1 \to Q_{n+1}=1 \implies J=X, K=0$.
From K-maps: $J = D, \quad K = \bar{D}$. Connect $D$ to $J$ and $\bar{D}$ (via NOT gate) to $K$.
\end{solbox}

\begin{examqbox}{3 [8 Marks]}
Explain the interfacing and operating principle of an LDR sensor in an automated streetlight circuit. Explain why software hysteresis is required.
\end{examqbox}

\begin{solbox}
1. \textbf{Circuit:} LDR and fixed $10\,\text{k}\Omega$ resistor form a voltage divider connected to Arduino analog pin A0. $V_{out} = 5.0\frac{R_{fixed}}{R_{LDR} + R_{fixed}}$. As light increases, $R_{LDR}$ falls, increasing $V_{out}$.\\
2. \textbf{Hysteresis:} At twilight, slow light fluctuations and noise cause the reading to oscillate around a single threshold, causing the streetlight relay to rapidly chatter ON and OFF. Implementing two separate thresholds (e.g. Turn ON at $\text{ADC} < 300$, Turn OFF at $\text{ADC} > 450$) creates a hysteresis band that eliminates flickering.
\end{solbox}

\begin{examqbox}{4 [8 Marks]}
Design a 4-bit 2's complement adder-subtractor circuit using four Full Adders and XOR gates. Explain how the mode control line $M$ selects addition vs subtraction and how signed overflow is detected.
\end{examqbox}

\begin{solbox}
1. Connect inputs $A_i$ directly to FA inputs. Connect $B_i$ to one input of an XOR gate with mode line $M$ connected to the second input.\\
2. Mode $M=0$: XOR outputs $B_i \oplus 0 = B_i$, and $C_0 = 0 \implies$ computes $A + B$.\\
3. Mode $M=1$: XOR outputs $B_i \oplus 1 = \bar{B}_i$, and $C_0 = 1 \implies$ computes $A + \bar{B} + 1 = A - B$.\\
4. Signed Overflow Flag: $V = C_4 \oplus C_3$.
\end{solbox}

\begin{examqbox}{5 [8 Marks]}
Compare DHT11 and DHT22 temperature and humidity sensors in terms of measurement ranges, precision, sampling rate, and interface protocol.
\end{examqbox}

\begin{solbox}
\begin{itemize}
    \item \textbf{DHT11:} Range $0-50^\circ\text{C}$ ($\pm 2^\circ\text{C}$), $20-90\%\,\text{RH}$ ($\pm 5\%$), max $1\,\text{Hz}$ sampling.
    \item \textbf{DHT22:} Range $-40-80^\circ\text{C}$ ($\pm 0.5^\circ\text{C}$), $0-100\%\,\text{RH}$ ($\pm 2\%$), max $0.5\,\text{Hz}$ sampling ($2\,\text{s}$ interval).
    \item Both use a single-wire digital bus requiring an external $4.7-10\,\text{k}\Omega$ pull-up resistor.
\end{itemize}
\end{solbox}

\subsection*{Section C: Comprehensive Design Problems (40 Marks, 20 Marks Each)}

\begin{examqbox}{6 [20 Marks]}
(a) Derive the open-circuit voltage $V_{oc}$ and fill factor $FF$ of a p-n junction solar cell.\\
(b) A solar cell has $V_{oc} = 0.65\,\text{V}, I_{sc} = 40\,\text{mA}, V_m = 0.52\,\text{V}, I_m = 35\,\text{mA}$. Calculate its fill factor and maximum output power.\\
(c) If incident optical power is $200\,\text{mW}$, compute the power conversion efficiency $\eta$.
\end{examqbox}

\begin{solbox}
\textbf{(a) Derivation:} Under illumination, diode current is $I = I_{sc} - I_0(e^{qV/nkT} - 1)$. Setting $I=0$ at open-circuit gives $V_{oc} = \frac{nkT}{q}\ln\left(\frac{I_{sc}}{I_0} + 1\right)$. Fill factor is defined as $FF = \frac{P_{max}}{V_{oc} I_{sc}} = \frac{V_m I_m}{V_{oc} I_{sc}}$.\\
\textbf{(b) Calculations:}\\
- $P_{max} = V_m I_m = (0.52\,\text{V})(35 \times 10^{-3}\,\text{A}) = 18.2\,\text{mW}$.\\
- $FF = \frac{18.2\,\text{mW}}{(0.65\,\text{V})(40\,\text{mA})} = \frac{18.2}{26.0} = 0.70$ ($70\%$).\\
\textbf{(c) Efficiency:} $\eta = \frac{P_{max}}{P_{in}} \times 100\% = \frac{18.2\,\text{mW}}{200\,\text{mW}} \times 100\% = 9.1\%$.
\end{solbox}

\begin{examqbox}{7 [20 Marks]}
Design an autonomous obstacle-avoiding robotic subsystem with an Arduino Uno, HC-SR04 Ultrasonic sensor, and reflective IR sensors:\\
(a) Draw the complete hardware wiring diagram listing pin assignments.\\
(b) Write a complete, well-commented Arduino C++ program implementing obstacle detection within $20\,\text{cm}$.
\end{examqbox}

\begin{solbox}
\textbf{(a) Pin Assignments:}\\
- HC-SR04: \texttt{VCC} $\to 5\,\text{V}$, \texttt{GND} $\to \text{GND}$, \texttt{TRIG} $\to \text{Pin 9}$, \texttt{ECHO} $\to \text{Pin 10}$.\\
- Left IR Sensor: \texttt{OUT} $\to \text{Pin 2}$. Right IR Sensor: \texttt{OUT} $\to \text{Pin 3}$.\\
- Status Alert LED: \texttt{Anode} $\to \text{Pin 13}$ (through $220\,\Omega$ resistor).\\
\textbf{(b) Arduino Sketch:}
\begin{verbatim}
const int trigPin = 9;
const int echoPin = 10;
const int alertLED = 13;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(alertLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  float distanceCm = duration * 0.034 / 2.0;

  if (distanceCm < 20.0 && distanceCm > 0) {
    digitalWrite(alertLED, HIGH);
    Serial.println("Obstacle Detected!");
  } else {
    digitalWrite(alertLED, LOW);
  }
  delay(100);
}
\end{verbatim}
\end{solbox}
"""

with open("PHY175_Sample_Question_Papers/chapters/paper-endterm.tex", "w") as f:
    f.write(endterm_tex)

# Makefile
with open("PHY175_Sample_Question_Papers/Makefile", "w") as f:
    f.write("""all:
\tpdflatex -interaction=nonstopmode -halt-on-error main.tex
\tpdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
\trm -f *.aux *.log *.out *.toc *.synctex.gz
""")

print("Sample Question Papers suite generated.")
