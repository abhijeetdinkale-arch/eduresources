import os
import subprocess

print("Writing PHY175 Formula Book...")

os.makedirs("PHY175_Formula_Book/chapters", exist_ok=True)

# Style file for Formula Book
form_style = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{style}[2026/09/18 v1.0 PHY175 Formula Book Style System]

\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern}
\RequirePackage{microtype}

\RequirePackage{geometry}
\geometry{
    a4paper,
    top=18mm,
    bottom=18mm,
    left=18mm,
    right=18mm,
    headheight=14pt,
    headsep=12pt,
    footskip=10mm
}

\RequirePackage{amsmath,amssymb,amsfonts,mathtools}
\RequirePackage{bm}
\RequirePackage{siunitx}
\sisetup{separate-uncertainty = true}

\RequirePackage[table,dvipsnames,svgnames]{xcolor}
\definecolor{formnavy}{RGB}{2, 48, 71}
\definecolor{formblue}{RGB}{33, 158, 188}
\definecolor{formorange}{RGB}{251, 133, 0}
\definecolor{formbg}{RGB}{240, 248, 255}

\RequirePackage[most]{tcolorbox}
\tcbset{
    boxrule=1pt,
    arc=2pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    fonttitle=\bfseries\sffamily,
    before skip=6pt,
    after skip=6pt
}

\newtcolorbox{formulabox}[1][Formula Sheet]{
    enhanced, breakable, colback=formbg, colframe=formnavy,
    coltitle=white, title={\textbf{#1}}, attach boxed title to top left={yshift=-2mm, xshift=3mm},
    boxed title style={colback=formnavy, arc=2pt}
}

\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{enumitem}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}

\titleformat{\chapter}[display]
{\normalfont\sffamily\LARGE\bfseries\color{formnavy}}
{\flushright\fontsize{32}{36}\selectfont\color{formblue!30}Unit \thechapter}
{-15pt}
{\titlerule[1.5pt]\vspace{1ex}}
[\vspace{1ex}\titlerule]

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\sffamily\small\thepage}
\fancyhead[RE]{\sffamily\small\nouppercase{\leftmark}}
\fancyhead[LO]{\sffamily\small\nouppercase{\rightmark}}
\fancyfoot[C]{\sffamily\scriptsize LPU Engineering Open $\cdot$ PHY175 Formula Handbook}
\renewcommand{\headrulewidth}{0.4pt}

\RequirePackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=formnavy, citecolor=formblue}
"""

with open("PHY175_Formula_Book/style.sty", "w") as f:
    f.write(form_style)

# Master Document
form_main = r"""\documentclass[11pt,a4paper,twoside]{report}
\usepackage{style}

\title{\Huge\bfseries\color{formnavy} PHY175: Modern Physics \& Electronics\\[0.3em]
\Large\color{formblue} Comprehensive Formula Handbook, Truth Tables \& Constants}
\author{\textbf{LPU Engineering Open Series}}
\date{Academic Year 2026--2027}

\begin{document}
\maketitle
\tableofcontents

\include{chapters/unit1-formulas}
\include{chapters/unit2-formulas}
\include{chapters/unit3-formulas}
\include{chapters/unit4-formulas}
\include{chapters/unit5-formulas}
\include{chapters/unit6-formulas}

\end{document}
"""

with open("PHY175_Formula_Book/main.tex", "w") as f:
    f.write(form_main)

# Unit 1 Formulas
u1_form = r"""\chapter{Solid State Physics Formulas}

\begin{formulabox}[Free Electron Theory \& Quantum Statistics]
\begin{align}
\text{Drude Conductivity:} \quad \sigma &= \frac{n e^2 \tau}{m} = n e \mu_e \\
\text{Electron Mobility:} \quad \mu_e &= \frac{e \tau}{m} \\
\text{Fermi-Dirac Distribution:} \quad f(E) &= \frac{1}{1 + \exp\left(\frac{E - E_F}{k_B T}\right)} \\
\text{Fermi Energy (3D Gas):} \quad E_F &= \frac{\hbar^2}{2m}\left(3\pi^2 n\right)^{2/3} \implies E_F \propto n^{2/3} \\
\text{Effective Mass Tensor:} \quad m^* &= \frac{\hbar^2}{\frac{d^2E}{dk^2}} \\
\text{Hall Coefficient (Single Carrier):} \quad R_H &= \frac{1}{n q} = \begin{cases} -\frac{1}{n e} & \text{(electrons)} \\ +\frac{1}{p e} & \text{(holes)} \end{cases} \\
\text{Hall Voltage:} \quad V_H &= \frac{R_H I B}{t} = \frac{I B}{n q t} \\
\text{Two-Carrier Hall Coefficient:} \quad R_H &= \frac{p \mu_h^2 - n \mu_e^2}{q (p \mu_h + n \mu_e)^2}
\end{align}
\end{formulabox}

\begin{formulabox}[Semiconductor Physics \& Solar Cells]
\begin{align}
\text{Intrinsic Carrier Concentration:} \quad n_i &= \sqrt{N_C N_V} \exp\left(-\frac{E_g}{2 k_B T}\right) \\
\text{Mass Action Law:} \quad n \cdot p &= n_i^2 \\
\text{Intrinsic Fermi Level:} \quad E_i &= \frac{E_C + E_V}{2} + \frac{1}{2} k_B T \ln\left(\frac{N_V}{N_C}\right) = \frac{E_C + E_V}{2} + \frac{3}{4} k_B T \ln\left(\frac{m_h^*}{m_e^*}\right) \\
\text{Extrinsic Fermi Shifts:} \quad E_F - E_i &= k_B T \ln\left(\frac{N_D}{n_i}\right) \quad (\text{n-type}), \quad E_i - E_F = k_B T \ln\left(\frac{N_A}{n_i}\right) \quad (\text{p-type}) \\
\text{Einstein Relation:} \quad \frac{D_n}{\mu_n} &= \frac{D_p}{\mu_p} = \frac{k_B T}{q} = V_T \\
\text{Solar Cell Open-Circuit Voltage:} \quad V_{oc} &\approx \frac{n k_B T}{q}\ln\left(\frac{I_{sc}}{I_0}\right) \\
\text{Fill Factor \& Efficiency:} \quad FF &= \frac{V_m I_m}{V_{oc} I_{sc}}, \quad \eta = \frac{V_m I_m}{P_{in}}
\end{align}
\end{formulabox}
"""

with open("PHY175_Formula_Book/chapters/unit1-formulas.tex", "w") as f:
    f.write(u1_form)

# Unit 2 Formulas
u2_form = r"""\chapter{Electricity and Electronic Devices Formulas}

\begin{formulabox}[Circuit Laws \& Network Theorems]
\begin{align}
\text{Ohm's Law:} \quad V &= I R, \quad P = V I = I^2 R = \frac{V^2}{R} \\
\text{KCL (Node Rule):} \quad \sum I_{in} &= \sum I_{out} \\
\text{KVL (Loop Rule):} \quad \sum V_{drops} &= \sum V_{sources} \\
\text{Series Voltage Divider:} \quad V_{R2} &= V_S \frac{R_2}{R_1 + R_2} \\
\text{Parallel Current Divider:} \quad I_1 &= I_{total} \frac{R_2}{R_1 + R_2}
\end{align}
\end{formulabox}

\begin{formulabox}[Diodes, Rectifiers \& BJTs]
\begin{align}
\text{Shockley Diode Equation:} \quad I_D &= I_S \left[ \exp\left(\frac{V_D}{n V_T}\right) - 1 \right] \\
\text{Thermal Voltage:} \quad V_T &= \frac{k_B T}{q} \approx 25.9\,\text{mV at } 300\,\text{K} \\
\text{Bridge Rectifier Peak Voltage:} \quad V_{peak} &= V_m - 2 V_D \\
\text{Bridge Ripple Frequency:} \quad f_r &= 2 f_{in} = 100\,\text{Hz (for } 50\,\text{Hz AC)} \\
\text{Peak-to-Peak Ripple Voltage:} \quad V_{r(pp)} &= \frac{V_{peak}}{2 f C R_L} = \frac{I_{DC}}{2 f C} \\
\text{BJT Currents:} \quad I_E &= I_B + I_C, \quad I_C = \beta I_B = \alpha I_E, \quad \alpha = \frac{\beta}{\beta + 1} \\
\text{BJT Base Bias (Thevenin):} \quad I_B &= \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1)R_E}
\end{align}
\end{formulabox}

\begin{formulabox}[CMOS, Memory \& Architectures]
\begin{align}
\text{CMOS Dynamic Power:} \quad P_{dyn} &= \alpha C V_{DD}^2 f \\
\text{SSD Host Write Endurance:} \quad \text{Bytes} &= \frac{\text{Physical Flash Size} \times \text{P/E Cycles}}{\text{Write Amplification Factor}} \\
\text{SECDED Parity Bits:} \quad 2^k &\ge m + k + 1 \quad (+1 \text{ overall parity bit}) \\
\text{Roofline Model Bound:} \quad \text{Throughput} &= \min(\text{Peak TOPS}, \, \text{Intensity} \times \text{Bandwidth})
\end{align}
\end{formulabox}
"""

with open("PHY175_Formula_Book/chapters/unit2-formulas.tex", "w") as f:
    f.write(u2_form)

# Unit 3 Formulas
u3_form = r"""\chapter{Number Systems and Logic Gates Formulas}

\begin{formulabox}[Radix Conversion, Codes \& Complements]
\begin{align}
\text{Radix Expansion:} \quad N_r &= \sum_{i=-m}^{n-1} d_i \cdot r^i \\
\text{Binary to Gray:} \quad G_{MSB} &= B_{MSB}, \quad G_i = B_{i+1} \oplus B_i \\
\text{Gray to Binary:} \quad B_{MSB} &= G_{MSB}, \quad B_i = B_{i+1} \oplus G_i \\
\text{Excess-3 Code:} \quad \text{XS-3} &= \text{BCD} + 0011_2 \\
\text{1's Complement:} \quad (N)' &= (2^n - 1) - N \quad (\text{bitwise NOT}) \\
\text{2's Complement:} \quad (N)'' &= 2^n - N = \text{1's Comp} + 1 \\
\text{Signed Overflow Flag:} \quad V &= C_{in} \oplus C_{out} \quad \text{at MSB}
\end{align}
\end{formulabox}

\begin{formulabox}[Boolean Algebra Laws \& Theorems]
\begin{align}
\text{Identity Laws:} \quad A + 0 &= A, \quad A \cdot 1 = A \\
\text{Null / Annihilation:} \quad A + 1 &= 1, \quad A \cdot 0 = 0 \\
\text{Idempotent Laws:} \quad A + A &= A, \quad A \cdot A = A \\
\text{Complementarity:} \quad A + \bar{A} &= 1, \quad A \cdot \bar{A} = 0 \\
\text{Involution:} \quad \overline{\overline{A}} &= A \\
\text{De Morgan's Laws:} \quad \overline{A + B} &= \bar{A} \cdot \bar{B}, \quad \overline{A \cdot B} = \bar{A} + \bar{B} \\
\text{Absorption Laws:} \quad A + AB &= A, \quad A(A + B) = A \\
\text{Consensus Theorem:} \quad AB + \bar{A}C + BC &= AB + \bar{A}C
\end{align}
\end{formulabox}
"""

with open("PHY175_Formula_Book/chapters/unit3-formulas.tex", "w") as f:
    f.write(u3_form)

# Unit 4 Formulas
u4_form = r"""\chapter{Combinational Logic Circuits Formulas}

\begin{formulabox}[Adders, Subtractors \& Carry Lookahead]
\begin{align}
\text{Half Adder:} \quad S &= A \oplus B, \quad C = AB \\
\text{Full Adder:} \quad S &= A \oplus B \oplus C_{in}, \quad C_{out} = AB + BC_{in} + AC_{in} \\
\text{Half Subtractor:} \quad D &= A \oplus B, \quad B_{out} = \bar{A}B \\
\text{Full Subtractor:} \quad D &= A \oplus B \oplus B_{in}, \quad B_{out} = \bar{A}B + \bar{A}B_{in} + BB_{in} \\
\text{CLA Generate \& Propagate:} \quad G_i &= A_i B_i, \quad P_i = A_i \oplus B_i \\
\text{CLA Carry Equations:} \quad C_1 &= G_0 + P_0 C_0 \\
C_2 &= G_1 + P_1 G_0 + P_1 P_0 C_0 \\
C_3 &= G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0
\end{align}
\end{formulabox}

\begin{formulabox}[Multiplexers, Encoders \& Comparators]
\begin{align}
\text{4-to-1 MUX Output:} \quad Y &= \bar{S}_1\bar{S}_0 I_0 + \bar{S}_1 S_0 I_1 + S_1\bar{S}_0 I_2 + S_1 S_0 I_3 \\
\text{4-to-2 Priority Encoder ($D_3$ highest):} \quad Q_1 &= D_3 + D_2, \quad Q_0 = D_3 + \bar{D}_2 D_1, \quad V = \sum D_i \\
\text{2-bit Comparator Equality:} \quad (A=B) &= (A_1 \odot B_1)(A_0 \odot B_0) \\
\text{2-bit Comparator Greater:} \quad (A>B) &= A_1 \bar{B}_1 + (A_1 \odot B_1) A_0 \bar{B}_0 \\
\text{2-bit Comparator Lesser:} \quad (A<B) &= \bar{A}_1 B_1 + (A_1 \odot B_1) \bar{A}_0 B_0
\end{align}
\end{formulabox}
"""

with open("PHY175_Formula_Book/chapters/unit4-formulas.tex", "w") as f:
    f.write(u4_form)

# Unit 5 Formulas
u5_form = r"""\chapter{Sequential Logic Circuits Formulas}

\begin{formulabox}[Flip-Flop Characteristic Equations \& Excitation Tables]
\begin{align}
\text{SR Flip-Flop:} \quad Q_{n+1} &= S + \bar{R}Q_n \quad (SR=0) \\
\text{JK Flip-Flop:} \quad Q_{n+1} &= J\bar{Q}_n + \bar{K}Q_n \\
\text{D Flip-Flop:} \quad Q_{n+1} &= D \\
\text{T Flip-Flop:} \quad Q_{n+1} &= T \oplus Q_n = T\bar{Q}_n + \bar{T}Q_n
\end{align}

\begin{tabularx}{\textwidth}{c c c c c c}
\toprule
$Q_n \to Q_{n+1}$ & \textbf{SR Excitation} & \textbf{JK Excitation} & \textbf{D Excitation} & \textbf{T Excitation} \\
\midrule
$0 \to 0$ & $S=0, R=X$ & $J=0, K=X$ & $D=0$ & $T=0$ \\
$0 \to 1$ & $S=1, R=0$ & $J=1, K=X$ & $D=1$ & $T=1$ \\
$1 \to 0$ & $S=0, R=1$ & $J=X, K=1$ & $D=0$ & $T=1$ \\
$1 \to 1$ & $S=X, R=0$ & $J=X, K=0$ & $D=1$ & $T=0$ \\
\bottomrule
\end{tabularx}
\end{formulabox}

\begin{formulabox}[Shift Registers \& Counter Timing]
\begin{align}
\text{SIPO Total Load Clocks:} \quad N_{clk} &= N \\
\text{PISO Total Read Clocks:} \quad N_{clk} &= N - 1 \\
\text{Ripple Counter Min Clock Period:} \quad T_{min} &= N \cdot t_{pd} + t_s \\
\text{Max Ripple Clock Frequency:} \quad f_{max} &= \frac{1}{N \cdot t_{pd} + t_s} \\
\text{Mod-N Counter States:} \quad \text{States} &= N, \quad \text{Flip-Flops required: } 2^{k-1} < N \le 2^k
\end{align}
\end{formulabox}
"""

with open("PHY175_Formula_Book/chapters/unit5-formulas.tex", "w") as f:
    f.write(u5_form)

# Unit 6 Formulas
u6_form = r"""\chapter{Arduino and Sensor Interfacing Formulas}

\begin{formulabox}[Signals, ADC \& PWM]
\begin{align}
\text{Nyquist Sampling Criterion:} \quad f_s &\ge 2 f_{max} \\
\text{10-Bit ADC Output:} \quad \text{Count} &= \left\lfloor \frac{V_{in}}{V_{ref}} \times 1023 \right\rceil \\
\text{10-Bit ADC Voltage Step (LSB):} \quad \Delta V &= \frac{V_{ref}}{1024} = \frac{5.0\,\text{V}}{1024} \approx 4.88\,\text{mV} \\
\text{PWM Average Voltage (8-bit):} \quad V_{avg} &= \frac{\text{val}}{255} \times V_{CC}
\end{align}
\end{formulabox}

\begin{formulabox}[Sensor Interfacing Transfer Functions]
\begin{align}
\text{LDR Voltage Divider Output:} \quad V_{out} &= V_{CC} \frac{R_{fixed}}{R_{LDR} + R_{fixed}} \\
\text{Ultrasonic Sensor Distance (HC-SR04):} \quad d &= \frac{v_{sound} \cdot t_{echo}}{2} = \frac{(340\,\text{m/s}) \cdot t_{echo}}{2} \\
\text{Distance in cm ($t$ in }\mu\text{s):} \quad d_{\text{cm}} &= \frac{t\,\mu\text{s}}{58.8} \\
\text{DHT11 Sampling Minimum Interval:} \quad \Delta t &\ge 1.0\,\text{s} \quad (\text{Bandwidth } 1\,\text{Hz}) \\
\text{DHT22 Sampling Minimum Interval:} \quad \Delta t &\ge 2.0\,\text{s} \quad (\text{Bandwidth } 0.5\,\text{Hz})
\end{align}
\end{formulabox}
"""

with open("PHY175_Formula_Book/chapters/unit6-formulas.tex", "w") as f:
    f.write(u6_form)

# Makefile
makefile_content = """all:
\tpdflatex -interaction=nonstopmode -halt-on-error main.tex
\tpdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
\trm -f *.aux *.log *.out *.toc *.synctex.gz
"""

with open("PHY175_Formula_Book/Makefile", "w") as f:
    f.write(makefile_content)

print("PHY175 Formula Book created.")
