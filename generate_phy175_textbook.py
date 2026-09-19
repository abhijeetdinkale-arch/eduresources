import os
import subprocess

print("Fixing LaTeX and rebuilding PHY175 Textbook...")

os.makedirs("PHY175/chapters", exist_ok=True)
os.makedirs("PHY175/frontmatter", exist_ok=True)

# 1. Style file
style_content = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{style}[2026/09/18 v1.0 PHY175 Modern Physics & Electronics Style System]

\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern}
\RequirePackage{microtype}
\RequirePackage{textcomp}

\RequirePackage{geometry}
\geometry{
    a4paper,
    top=25mm,
    bottom=25mm,
    left=22mm,
    right=22mm,
    headheight=15pt,
    headsep=18pt,
    footskip=14mm
}

\RequirePackage{amsmath,amssymb,amsfonts,mathtools}
\RequirePackage{bm}
\RequirePackage{siunitx}
\sisetup{separate-uncertainty = true, inter-unit-product = \ensuremath{{}\cdot{}}}

\RequirePackage[table,dvipsnames,svgnames]{xcolor}
\definecolor{brandnavy}{RGB}{15, 44, 89}
\definecolor{brandblue}{RGB}{30, 86, 160}
\definecolor{brandslate}{RGB}{71, 85, 105}
\definecolor{branddark}{RGB}{15, 23, 42}
\definecolor{brandaccent}{RGB}{217, 4, 41}
\definecolor{brandgold}{RGB}{217, 119, 6}

\definecolor{boxnavyborder}{RGB}{15, 44, 89}
\definecolor{boxnavybg}{RGB}{243, 247, 254}
\definecolor{boxamberborder}{RGB}{217, 119, 6}
\definecolor{boxamberbg}{RGB}{255, 251, 235}
\definecolor{boxgreenborder}{RGB}{13, 148, 136}
\definecolor{boxgreenbg}{RGB}{240, 253, 250}
\definecolor{boxroseborder}{RGB}{225, 29, 72}
\definecolor{boxrosebg}{RGB}{255, 241, 242}
\definecolor{boxskyborder}{RGB}{2, 132, 199}
\definecolor{boxskybg}{RGB}{240, 249, 255}
\definecolor{boxpurpleborder}{RGB}{126, 34, 206}
\definecolor{boxpurplebg}{RGB}{250, 245, 255}

\RequirePackage[most]{tcolorbox}
\tcbset{
    boxrule=1pt,
    arc=3pt,
    left=10pt,
    right=10pt,
    top=8pt,
    bottom=8pt,
    fonttitle=\bfseries\sffamily,
    before skip=10pt,
    after skip=10pt
}

\newtcolorbox{definitionbox}[1][Definition]{
    enhanced, breakable, colback=boxnavybg, colframe=boxnavyborder,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=boxnavyborder, arc=2pt}
}

\newtcolorbox{conceptbox}[1][Key Concept]{
    enhanced, breakable, colback=boxskybg, colframe=boxskyborder,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=boxskyborder, arc=2pt}
}

\newtcolorbox{derivationbox}[1][Mathematical Derivation]{
    enhanced, breakable, colback=boxpurplebg, colframe=boxpurpleborder,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=boxpurpleborder, arc=2pt}
}

\newtcolorbox{examplebox}[1][Worked Example]{
    enhanced, breakable, colback=boxgreenbg, colframe=boxgreenborder,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=boxgreenborder, arc=2pt}
}

\newtcolorbox{pitfallbox}[1][Common Exam Pitfall]{
    enhanced, breakable, colback=boxrosebg, colframe=boxroseborder,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=boxroseborder, arc=2pt}
}

\newtcolorbox{takeawaybox}[1][Chapter Summary \& Key Takeaways]{
    enhanced, breakable, colback=boxamberbg, colframe=boxamberborder,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=boxamberborder, arc=2pt}
}

\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{enumitem}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{listings}

\lstset{
    basicstyle=\small\ttfamily,
    keywordstyle=\color{brandnavy}\bfseries,
    commentstyle=\color{brandslate}\itshape,
    stringstyle=\color{brandaccent},
    backgroundcolor=\color{boxnavybg},
    frame=single,
    rulecolor=\color{boxnavyborder},
    breaklines=true,
    numbers=left,
    numberstyle=\tiny\color{brandslate}
}

\titleformat{\chapter}[display]
{\normalfont\sffamily\huge\bfseries\color{brandnavy}}
{\flushright\fontsize{50}{60}\selectfont\color{brandblue!30}\thechapter}
{-20pt}
{\titlerule[2pt]\vspace{1ex}}
[\vspace{1ex}\titlerule]

\titleformat{\section}
{\normalfont\sffamily\Large\bfseries\color{brandnavy}}
{\thesection}{1em}{}

\titleformat{\subsection}
{\normalfont\sffamily\large\bfseries\color{brandblue}}
{\thesubsection}{1em}{}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\sffamily\small\thepage}
\fancyhead[RE]{\sffamily\small\nouppercase{\leftmark}}
\fancyhead[LO]{\sffamily\small\nouppercase{\rightmark}}
\fancyfoot[C]{\sffamily\scriptsize LPU Engineering Open $\cdot$ PHY175: Modern Physics \& Electronics}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.3pt}

\RequirePackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=brandblue,
    citecolor=brandnavy,
    urlcolor=brandaccent,
    bookmarksnumbered=true,
    pdfstartview={FitH}
}
"""

with open("PHY175/style.sty", "w") as f:
    f.write(style_content)

# Chapter 3: Number Systems & Logic Gates
ch3_tex = r"""\chapter{Introduction to Number Systems and Logic Gates}
\label{chap:number_systems_logic}

\section{Positional Number Systems and Radix Conversions}
A positional number in radix $r$ is represented as:
\begin{equation}
(N)_r = \sum_{i=-m}^{n-1} d_i \cdot r^i
\end{equation}
Common bases in digital electronics include Binary ($r=2$), Octal ($r=8$), Decimal ($r=10$), and Hexadecimal ($r=16$).

\begin{examplebox}[Hexadecimal to Octal Conversion]
\textbf{Problem:} Convert $(3\text{A}7.\text{C})_{16}$ to its octal representation.

\textbf{Solution:}
1. Convert each hexadecimal digit into 4-bit binary:
\begin{equation}
3_{16} = 0011_2, \quad \text{A}_{16} = 1010_2, \quad 7_{16} = 0111_2, \quad \text{C}_{16} = 1100_2
\end{equation}
\begin{equation}
(3\text{A}7.\text{C})_{16} = 0011\,1010\,0111.1100_2
\end{equation}
2. Group into 3-bit clusters from radix point:
\begin{equation}
\text{Integer part:} \quad 001 \quad 110 \quad 100 \quad 111 \implies 1 \quad 6 \quad 4 \quad 7
\end{equation}
\begin{equation}
\text{Fractional part:} \quad 110 \quad 000 \implies 6 \quad 0
\end{equation}
\begin{equation}
(3\text{A}7.\text{C})_{16} = (1647.6)_8
\end{equation}
\end{examplebox}

\section{Binary Codes: Gray Code, BCD, and Excess-3}
\subsection{Reflected Gray Code}
Gray code is an unweighted, unit-distance code where adjacent numerical values differ by exactly one bit, preventing transient glitches in optical encoders and asynchronous state machines.
\begin{itemize}[leftmargin=*]
    \item \textbf{Binary to Gray:} For binary word $B_{n-1}\dots B_0$, Gray bits are:
    \begin{equation}
    G_{n-1} = B_{n-1}, \quad G_i = B_{i+1} \oplus B_i \quad (0 \le i < n-1)
    \end{equation}
    \item \textbf{Gray to Binary:}
    \begin{equation}
    B_{n-1} = G_{n-1}, \quad B_i = B_{i+1} \oplus G_i \quad (0 \le i < n-1)
    \end{equation}
\end{itemize}

\subsection{Binary Coded Decimal (BCD) and Excess-3}
\begin{itemize}[leftmargin=*]
    \item \textbf{BCD (8421):} Each decimal digit ($0$ to $9$) is encoded into a 4-bit binary nibble ($0000$ to $1001$). Combinations $1010_2$ to $1111_2$ are invalid. In BCD addition, if the sum exceeds $9$ or produces an output carry, add $6$ ($0110_2$) to correct.
    \item \textbf{Excess-3 Code:} An unweighted self-complementing code formed by adding $3$ ($0011_2$) to the BCD value of each decimal digit. 9's complement of an Excess-3 number is obtained by bitwise inversion.
\end{itemize}

\section{Complements and Signed Arithmetic}
In digital computers, subtraction $A - B$ is evaluated via addition using 2's complement representation:
\begin{equation}
A - B = A + (\bar{B} + 1)
\end{equation}

\begin{conceptbox}[Signed Two's Complement Overflow]
When two numbers of the same sign are added and produce a result of opposite sign, \textbf{signed overflow} occurs. For an $n$-bit adder with carry-in $C_{n-1}$ and carry-out $C_n$ at the MSB stage:
\begin{equation}
V = C_n \oplus C_{n-1}
\end{equation}
If $V = 1$, the result exceeds the representable range $[-2^{n-1}, +2^{n-1}-1]$.
\end{conceptbox}

\section{Boolean Algebra and Logic Gates}
\begin{table}[htbp]
\centering
\caption{\textbf{Fundamental Logic Gates and Boolean Operations}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l l l X}
\toprule
\textbf{Gate} & \textbf{Symbol} & \textbf{Boolean Function} & \textbf{Characteristic Output} \\
\midrule
\textbf{AND} & $Y = A \cdot B$ & Product & $1$ only when all inputs are $1$. \\
\textbf{OR} & $Y = A + B$ & Sum & $1$ when at least one input is $1$. \\
\textbf{NOT} & $Y = \bar{A}$ & Inversion & Inverts logic level ($0 \to 1, 1 \to 0$). \\
\textbf{NAND} & $Y = \overline{A \cdot B}$ & Universal & $0$ only when all inputs are $1$. \\
\textbf{NOR} & $Y = \overline{A + B}$ & Universal & $1$ only when all inputs are $0$. \\
\textbf{XOR} & $Y = A \oplus B = \bar{A}B + A\bar{B}$ & Inequality & $1$ when inputs differ. \\
\textbf{XNOR} & $Y = A \odot B = AB + \bar{A}\bar{B}$ & Equivalence & $1$ when inputs are identical. \\
\bottomrule
\end{tabularx}
\end{table}

\section{Karnaugh Map (K-Map) Simplification and Hazards}
K-Maps provide a systematic graphical technique for minimizing Boolean expressions up to 4 variables.
\begin{itemize}[leftmargin=*]
    \item \textbf{Gray Code Cell Ordering:} Rows and columns follow $00, 01, 11, 10$.
    \item \textbf{Adjacency \& Grouping:} Groups must contain $2^k$ cells ($1, 2, 4, 8, 16$).
    \item \textbf{Don't Care Conditions ($d$):} Used to enlarge groups where output conditions are irrelevant.
    \item \textbf{Static-1 Hazard Elimination:} A static-1 hazard occurs when adjacent 1s in a K-map belong to different prime implicants without an overlapping consensus term. Including the redundant consensus product term prevents transient zero glitches.
\end{itemize}

\begin{takeawaybox}
\begin{itemize}[leftmargin=*]
    \item Gray code differs by 1 bit between adjacent values (unit distance).
    \item BCD arithmetic requires adding $0110_2$ (+6) when digit sum exceeds 9.
    \item Signed overflow flag $V = C_{in} \oplus C_{out}$ at MSB stage.
    \item NAND and NOR are universal gates capable of implementing any Boolean function.
    \item Static-1 hazards are eliminated by adding redundant consensus groups in K-maps.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-03-number-systems-and-logic.tex", "w") as f:
    f.write(ch3_tex)

print("Updated Chapter 3 successfully.")
