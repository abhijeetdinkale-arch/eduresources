import os
import subprocess

print("Writing PHY175 Handwritten Notes...")

os.makedirs("PHY175_Handwritten_Notes/chapters", exist_ok=True)

# Style file for Handwritten Notes
notes_style = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{style}[2026/09/18 v1.0 PHY175 Handwritten Notes Style System]

\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern}
\RequirePackage{microtype}

\RequirePackage{geometry}
\geometry{
    a4paper,
    top=22mm,
    bottom=22mm,
    left=22mm,
    right=22mm,
    headheight=14pt,
    headsep=14pt,
    footskip=12mm
}

\RequirePackage{amsmath,amssymb,amsfonts,mathtools}
\RequirePackage{bm}
\RequirePackage{siunitx}

\RequirePackage[table,dvipsnames,svgnames]{xcolor}
\definecolor{noteteal}{RGB}{13, 148, 136}
\definecolor{notedark}{RGB}{19, 78, 74}
\definecolor{notebg}{RGB}{240, 253, 250}
\definecolor{noteyellow}{RGB}{254, 240, 138}

\RequirePackage[most]{tcolorbox}
\tcbset{
    boxrule=1pt,
    arc=4pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    fonttitle=\bfseries\sffamily,
    before skip=8pt,
    after skip=8pt
}

\newtcolorbox{notebox}[1][Student Note \& Intuition]{
    enhanced, breakable, colback=notebg, colframe=noteteal,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=3mm},
    boxed title style={colback=noteteal, arc=3pt}
}

\newtcolorbox{trickbox}[1][Exam Trick / Mnemonic]{
    enhanced, breakable, colback=noteyellow!40, colframe=notedark,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=3mm},
    boxed title style={colback=notedark, arc=3pt}
}

\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{enumitem}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}

\titleformat{\chapter}[display]
{\normalfont\sffamily\LARGE\bfseries\color{notedark}}
{\flushright\fontsize{32}{36}\selectfont\color{noteteal!30}Module \thechapter}
{-15pt}
{\titlerule[1.5pt]\vspace{1ex}}
[\vspace{1ex}\titlerule]

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\sffamily\small\thepage}
\fancyhead[RE]{\sffamily\small\nouppercase{\leftmark}}
\fancyhead[LO]{\sffamily\small\nouppercase{\rightmark}}
\fancyfoot[C]{\sffamily\scriptsize LPU Engineering Open $\cdot$ PHY175 Handwritten Study Notes}
\renewcommand{\headrulewidth}{0.4pt}

\RequirePackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=notedark, citecolor=noteteal}
"""

with open("PHY175_Handwritten_Notes/style.sty", "w") as f:
    f.write(notes_style)

# Master Document
notes_main = r"""\documentclass[11pt,a4paper,twoside]{report}
\usepackage{style}

\title{\Huge\bfseries\color{notedark} PHY175: Modern Physics \& Electronics\\[0.3em]
\Large\color{noteteal} Classroom-Style Handwritten Notes, Intuition \& Diagrams}
\author{\textbf{LPU Engineering Open Series}}
\date{Academic Year 2026--2027}

\begin{document}
\maketitle
\tableofcontents

\include{chapters/notes-unit1-2}
\include{chapters/notes-unit3-4}
\include{chapters/notes-unit5-6}

\end{document}
"""

with open("PHY175_Handwritten_Notes/main.tex", "w") as f:
    f.write(notes_main)

# Unit 1 & 2 Notes
n12_tex = r"""\chapter{Solid State Physics \& Electronic Devices}

\section{Solid State Physics Intuition}
\begin{notebox}[Physical Meaning of Drude Model]
\begin{itemize}[leftmargin=*]
    \item Think of conduction electrons as a \textbf{billiard ball gas} bouncing elastically off stationary ionic bumpers.
    \item Electric field $\vec{E}$ tilts the pinball table, creating a gentle net drift velocity $\vec{v}_d = -\frac{e\tau}{m}\vec{E}$.
    \item Conductivity $\sigma = \frac{ne^2\tau}{m}$ means: more carriers ($n\uparrow$) or longer flight between hits ($\tau\uparrow$) boosts current!
\end{itemize}
\end{notebox}

\begin{trickbox}[Fermi Level Memory Hack]
\begin{itemize}[leftmargin=*]
    \item At $T=0\,\text{K}$: $E_F$ is the \textbf{water level} of a filled glass. Below $E_F \implies 100\%$ full; above $E_F \implies 0\%$ full.
    \item At $T > 0\,\text{K}$: Thermal splashing occurs, but at exactly the water mark $E=E_F$, probability is always \textbf{exactly 50\%} ($1/2$).
    \item In 3D: $E_F \propto n^{2/3}$. Density $8\times \implies E_F$ is $4\times$.
\end{itemize}
\end{trickbox}

\begin{notebox}[Hall Effect Right-Hand Rule]
\begin{itemize}[leftmargin=*]
    \item Current along $+x$, Magnetic field along $+z$.
    \item Both electrons (moving left) and holes (moving right) experience Lorentz force pushing them toward the \textbf{$-y$ edge}!
    \item If electrons accumulate at $-y \implies V(-y)$ is negative ($R_H < 0$).
    \item If holes accumulate at $-y \implies V(-y)$ is positive ($R_H > 0$).
    \item This directly identifies whether a semiconductor is n-type or p-type!
\end{itemize}
\end{notebox}

\section{Electricity \& Circuit Devices}
\begin{trickbox}[Voltage Divider vs Current Divider]
\begin{itemize}[leftmargin=*]
    \item \textbf{Voltage Divider:} Voltage drops proportionally to its \textbf{OWN} resistance: $V_1 = V_S \frac{R_1}{R_1+R_2}$. Bigger resistor gets bigger share.
    \item \textbf{Current Divider:} Current flows preferentially through the \textbf{OPPOSITE} smaller resistance: $I_1 = I_T \frac{R_2}{R_1+R_2}$.
\end{itemize}
\end{trickbox}

\begin{notebox}[CMOS Inverter Action]
\begin{itemize}[leftmargin=*]
    \item PMOS connects to $V_{DD}$ and turns ON when gate is \textbf{LOW} ($0\,\text{V}$).
    \item NMOS connects to $\text{GND}$ and turns ON when gate is \textbf{HIGH} ($V_{DD}$).
    \item They never conduct simultaneously in DC steady state $\implies$ near-zero standby battery drain! Dynamic power only during switching: $P = \alpha C V^2 f$.
\end{itemize}
\end{notebox}
"""

with open("PHY175_Handwritten_Notes/chapters/notes-unit1-2.tex", "w") as f:
    f.write(n12_tex)

# Unit 3 & 4 Notes
n34_tex = r"""\chapter{Digital Logic: Number Systems \& Combinational Circuits}

\section{Number Systems \& Boolean Algebra}
\begin{trickbox}[Gray Code Reflection Pattern]
\begin{itemize}[leftmargin=*]
    \item 1-bit: $0, 1$.
    \item 2-bit: take $0, 1$, reflect as $1, 0$, prefix top with 0, bottom with 1: $00, 01, 11, 10$.
    \item 3-bit: reflect 2-bit list: $000, 001, 011, 010, 110, 111, 101, 100$.
    \item XOR conversion: $G_i = B_{i+1} \oplus B_i$.
\end{itemize}
\end{trickbox}

\begin{notebox}[BCD Addition Rule]
\begin{itemize}[leftmargin=*]
    \item BCD only allows $0000$ to $1001$ ($0$ to $9$).
    \item If binary addition produces a sum $> 1001_2$ (i.e. $> 9$) or an output carry: \textbf{Add $0110_2$ ($+6$)} to skip the 6 forbidden codes ($10$ to $15$).
\end{itemize}
\end{notebox}

\section{Combinational Logic Design}
\begin{notebox}[Adder vs Subtractor Expressions]
\begin{itemize}[leftmargin=*]
    \item \textbf{Half Adder:} $\text{Sum} = A \oplus B, \quad \text{Carry} = AB$.
    \item \textbf{Half Subtractor:} $\text{Diff} = A \oplus B, \quad \text{Borrow} = \bar{A}B$ (Notice the bar on $A$).
    \item \textbf{Full Adder:} $\text{Sum} = A \oplus B \oplus C_{in}, \quad \text{Carry} = AB + (A \oplus B)C_{in}$.
    \item \textbf{Full Subtractor:} $\text{Diff} = A \oplus B \oplus B_{in}, \quad \text{Borrow} = \bar{A}B + \overline{(A \oplus B)}B_{in}$.
\end{itemize}
\end{notebox}

\begin{trickbox}[Multiplexer Implementation Method]
\begin{itemize}[leftmargin=*]
    \item To implement an $n$-variable function with a $2^{n-1}$-to-1 MUX: connect $n-1$ variables to select lines ($S_{n-2}\dots S_0$).
    \item For each MUX input $I_k$, observe the truth table output: it will be $0, 1$, the remaining variable $X$, or its complement $\bar{X}$.
\end{itemize}
\end{trickbox}
"""

with open("PHY175_Handwritten_Notes/chapters/notes-unit3-4.tex", "w") as f:
    f.write(n34_tex)

# Unit 5 & 6 Notes
n56_tex = r"""\chapter{Sequential Logic \& Arduino Sensor Interfacing}

\section{Sequential Circuits \& Flip-Flops}
\begin{notebox}[Flip-Flop Behavior Summary]
\begin{itemize}[leftmargin=*]
    \item \textbf{SR Flip-Flop:} $S=1 \implies \text{Set}, R=1 \implies \text{Reset}, S=R=1 \implies \text{FORBIDDEN}$.
    \item \textbf{JK Flip-Flop:} Like SR, but $J=K=1 \implies \text{TOGGLE}$ (inverts state).
    \item \textbf{D Flip-Flop:} Data follower: $Q_{next} = D$.
    \item \textbf{T Flip-Flop:} Toggle toggle: $T=0 \implies \text{Hold}, T=1 \implies \text{Toggle}$.
\end{itemize}
\end{notebox}

\begin{trickbox}[Master-Slave Operation]
\begin{itemize}[leftmargin=*]
    \item Master takes notes while teacher talks ($\text{CLK}=1$).
    \item Slave writes exam on the board after class ends ($\text{CLK}=0$).
    \item Race-around is impossible because master and slave never listen/write at the same time!
\end{itemize}
\end{trickbox}

\section{Arduino \& Sensor Interfacing}
\begin{notebox}[Arduino Uno Essential Pinout]
\begin{itemize}[leftmargin=*]
    \item \textbf{Digital I/O:} 0 to 13 ($0=\text{RX}, 1=\text{TX}$; avoid for sensors if using USB serial).
    \item \textbf{PWM Pins:} 3, 5, 6, 9, 10, 11 (marked with $\sim$).
    \item \textbf{I2C Bus:} A4 = SDA, A5 = SCL.
    \item \textbf{SPI Bus:} 10 = SS, 11 = MOSI, 12 = MISO, 13 = SCK.
    \item \textbf{10-bit ADC:} $0-5\,\text{V} \implies 0-1023$. Voltage $= \text{analogRead}(\text{pin}) \times \frac{5.0}{1023}$.
\end{itemize}
\end{notebox}

\begin{trickbox}[Sensor Interfacing Rules]
\begin{itemize}[leftmargin=*]
    \item \textbf{LDR in Voltage Divider:} LDR on top, fixed resistor on bottom $\implies$ More light $=$ Lower LDR resistance $=$ Higher $V_{out}$.
    \item \textbf{HC-SR04 Ultrasonic:} Send $10\,\mu\text{s}$ HIGH to TRIG. Measure ECHO duration $t$. Distance $= \frac{340 \times t}{2}$. Divide by 2 because the wave goes there and back!
    \item \textbf{DHT11 / DHT22:} Single wire data line needs $10\,\text{k}\Omega$ pull-up. DHT11 wait $\ge 1\,\text{s}$ between reads; DHT22 wait $\ge 2\,\text{s}$.
\end{itemize}
\end{trickbox}
"""

with open("PHY175_Handwritten_Notes/chapters/notes-unit5-6.tex", "w") as f:
    f.write(n56_tex)

# Makefile
makefile_content = """all:
\tpdflatex -interaction=nonstopmode -halt-on-error main.tex
\tpdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
\trm -f *.aux *.log *.out *.toc *.synctex.gz
"""

with open("PHY175_Handwritten_Notes/Makefile", "w") as f:
    f.write(makefile_content)

print("PHY175 Handwritten Notes files created.")
