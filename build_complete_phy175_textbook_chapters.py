import os
import subprocess

print("Generating remaining chapters (2 through 6) for 60+ page PHY175 Textbook...")

# ==============================================================================
# CHAPTER 2
# ==============================================================================
ch2 = r"""\chapter{Fundamentals of Electricity and Circuit Devices}
\label{chap:electricity_devices}

\section{Introduction and Overview}
Electrical circuit theory and modern semiconductor devices form the physical backbone of all modern computing and communication systems. In this chapter, we bridge fundamental electric circuit laws (Ohm's law, KCL, KVL) with nonlinear semiconductor devices (PN diodes, bridge rectifiers, BJTs, CMOS logic), state-of-the-art memory architectures (SRAM, DRAM, SSD Flash), AI hardware acceleration models (Roofline analysis), IoT networking subnetting, and fiber-optic physical layer communications.

\section{Fundamental Circuit Laws and Network Analysis}
\subsection{Ohm's Law, KCL, and KVL}
\begin{definitionbox}[Core Circuit Laws]
\begin{enumerate}
    \item \textbf{Ohm's Law:} The current $I$ flowing through an ideal linear conductor is directly proportional to the potential difference $V$ across it at constant temperature:
    \begin{equation}
        V = I R \quad \text{or} \quad \mathbf{J} = \sigma \mathbf{E}
    \end{equation}
    \item \textbf{Kirchhoff's Current Law (KCL):} Based on the \textbf{Conservation of Electric Charge}, the algebraic sum of all currents entering and leaving any circuit node is identically zero:
    \begin{equation}
        \sum_{k=1}^N I_k = 0 \implies \sum I_{\text{entering}} = \sum I_{\text{leaving}}
    \end{equation}
    \item \textbf{Kirchhoff's Voltage Law (KVL):} Based on the \textbf{Conservation of Energy}, the algebraic sum of all electric potential differences (voltages) around any closed loop in a circuit is identically zero:
    \begin{equation}
        \sum_{k=1}^M V_k = 0 \implies \sum V_{\text{rises}} = \sum V_{\text{drops}}
    \end{equation}
\end{enumerate}
\end{definitionbox}

\subsection{Voltage and Current Division Principles}
\begin{itemize}
    \item \textbf{Voltage Division (Series Resistors):} For $N$ resistors connected in series across total voltage $V_{total}$:
    \begin{equation}
        V_k = V_{total} \left(\frac{R_k}{\sum_{i=1}^N R_i}\right)
    \end{equation}
    For two series resistors $R_1, R_2$: $V_1 = V_{total}\frac{R_1}{R_1 + R_2}$ and $V_2 = V_{total}\frac{R_2}{R_1 + R_2}$.
    \item \textbf{Current Division (Parallel Resistors):} For two parallel branches $R_1, R_2$ carrying total input current $I_{total}$:
    \begin{equation}
        I_1 = I_{total} \left(\frac{R_2}{R_1 + R_2}\right), \quad I_2 = I_{total} \left(\frac{R_1}{R_1 + R_2}\right)
    \end{equation}
\end{itemize}

\section{Semiconductor Diodes and Power Rectifier Circuits}
\subsection{The PN Junction Diode and Shockley Equation}
A PN junction consists of adjoining p-type and n-type semiconductor regions. Thermal diffusion of majority carriers creates a \textbf{depletion region} with uncompensated ionized dopants, creating a built-in potential barrier $V_{bi} \approx 0.7\,\text{V}$ (for Silicon) or $0.3\,\text{V}$ (for Germanium).

The current-voltage relationship is described by the \textbf{Shockley Ideal Diode Equation}:
\begin{equation}
    I_D = I_s \left(e^{\frac{V_D}{\eta V_t}} - 1\right)
\end{equation}
where $I_s$ is reverse saturation current, $\eta$ is ideality factor ($1 \le \eta \le 2$), and $V_t = \frac{k_BT}{q} \approx 25.86\,\text{mV}$ at $300\,\text{K}$.

\subsection{Full-Wave Bridge Rectifier with Capacitor Filter}
A full-wave bridge rectifier employs four diodes in a closed ring configuration to convert AC voltage $v_{in}(t) = V_m \sin(\omega t)$ into pulsating DC.

\begin{table}[htbp]
\centering
\small
\caption{Comparison of Rectifier Circuit Topologies}
\label{tab:rectifiers}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Parameter} & \textbf{Half-Wave Rectifier} & \textbf{Center-Tapped Full-Wave} & \textbf{Bridge Rectifier} \\
\midrule
\textbf{Number of Diodes} & 1 & 2 & 4 \\
\textbf{DC Output Voltage ($V_{dc}$)} & $\frac{V_m}{\pi} \approx 0.318 V_m$ & $\frac{2V_m}{\pi} \approx 0.636 V_m$ & $\frac{2V_m}{\pi} \approx 0.636 V_m$ \\
\textbf{RMS Output Voltage ($V_{rms}$)} & $\frac{V_m}{2} = 0.5 V_m$ & $\frac{V_m}{\sqrt{2}} \approx 0.707 V_m$ & $\frac{V_m}{\sqrt{2}} \approx 0.707 V_m$ \\
\textbf{Rectification Efficiency ($\eta$)} & $40.6\%$ & $81.2\%$ & $81.2\%$ \\
\textbf{Ripple Frequency ($f_r$)} & $f_{in}$ ($50\,\text{Hz}$) & $2 f_{in}$ ($100\,\text{Hz}$) & $2 f_{in}$ ($100\,\text{Hz}$) \\
\textbf{Ripple Factor ($\gamma$) without filter} & $1.21$ & $0.482$ & $0.482$ \\
\textbf{Peak Inverse Voltage (PIV)} & $V_m$ & $2 V_m$ & $V_m$ \\
\textbf{Transformer Utilization Factor} & $0.287$ & $0.693$ & $0.812$ \\
\bottomrule
\end{tabularx}
\end{table}

\begin{derivationbox}[Capacitor Filter Ripple Factor ($\gamma$) and Peak-to-Peak Ripple Voltage ($V_{r(pp)}$)]
Connecting a large smoothing capacitor $C$ in parallel with load resistor $R_L$:
\begin{itemize}
    \item The capacitor charges to peak voltage $V_{peak} = V_m - 2V_D$ (for bridge rectifier).
    \item During the interval between peaks ($T_r = \frac{1}{2f}$), the capacitor discharges through load $R_L$: $v(t) \approx V_{peak} e^{-t/(R_L C)} \approx V_{peak}\left(1 - \frac{t}{R_L C}\right)$.
\end{itemize}
The total charge lost during discharge time $T_r \approx \frac{1}{2f}$ is:
\begin{equation}
    \Delta Q = I_{dc} T_r = \frac{I_{dc}}{2f} = C V_{r(pp)} \implies V_{r(pp)} = \frac{I_{dc}}{2 f C} = \frac{V_{peak}}{2 f C R_L}
\end{equation}
Approximating the ripple waveform as a triangular wave of peak-to-peak amplitude $V_{r(pp)}$:
\begin{equation}
    V_{r,rms} = \frac{V_{r(pp)}}{2\sqrt{3}} = \frac{V_{peak}}{4\sqrt{3} f C R_L}
\end{equation}
The DC output voltage is $V_{dc} = V_{peak} - \frac{V_{r(pp)}}{2} \approx V_{peak}$. The \textbf{Ripple Factor} $\gamma$ is:
\begin{equation}
    \gamma \equiv \frac{V_{r,rms}}{V_{dc}} = \frac{\frac{V_{peak}}{4\sqrt{3} f C R_L}}{V_{peak}} = \frac{1}{4\sqrt{3} f C R_L}
\end{equation}
\end{derivationbox}

\section{Bipolar Junction Transistors (BJT): Operation and Biasing}
\subsection{Physical Structure and Current Relations}
A BJT consists of two back-to-back PN junctions forming three terminals: \textbf{Emitter (E)} (heavily doped), \textbf{Base (B)} (ultra-thin, lightly doped), and \textbf{Collector (C)} (moderately doped, large area for heat dissipation).

\begin{equation}
    I_E = I_B + I_C
\end{equation}
\begin{itemize}
    \item \textbf{Common Base Current Gain ($\alpha$):} $\alpha = \frac{I_C}{I_E} \approx 0.95 - 0.998$.
    \item \textbf{Common Emitter Current Gain ($\beta$):} $\beta = \frac{I_C}{I_B} \approx 50 - 500$.
    \item Mathematical relationship:
    \begin{equation}
        \beta = \frac{\alpha}{1 - \alpha}, \quad \alpha = \frac{\beta}{\beta + 1}
    \end{equation}
\end{itemize}

\subsection{BJT Operating Regions and DC Load Line Analysis}
\begin{table}[htbp]
\centering
\small
\caption{BJT Operating Modes and Junction Biasing}
\label{tab:bjt_modes}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Operating Region} & \textbf{Emitter-Base (EBJ)} & \textbf{Collector-Base (CBJ)} & \textbf{Primary Application} \\
\midrule
\textbf{Cutoff} & Reverse Biased & Reverse Biased & Digital OFF Switch ($I_C \approx 0, V_{CE} \approx V_{CC}$) \\
\textbf{Active (Forward-Active)} & Forward Biased & Reverse Biased & Linear Analog Amplifier ($I_C = \beta I_B$) \\
\textbf{Saturation} & Forward Biased & Forward Biased & Digital ON Switch ($V_{CE,\text{sat}} \approx 0.2\,\text{V}$) \\
\textbf{Reverse Active} & Reverse Biased & Forward Biased & Specialized TTL logic switches (low gain) \\
\bottomrule
\end{tabularx}
\end{table}

\begin{derivationbox}[DC Load Line and $Q$-Point Determination in Common Emitter]
In a Common Emitter circuit with supply $V_{CC}$ and collector resistor $R_C$:
Applying KVL to the collector-emitter loop:
\begin{equation}
    V_{CC} - I_C R_C - V_{CE} = 0 \implies I_C = -\frac{1}{R_C} V_{CE} + \frac{V_{CC}}{R_C}
\end{equation}
This represents a straight line with slope $-1/R_C$ on the $I_C$-$V_{CE}$ output characteristics:
\begin{itemize}
    \item \textbf{Cutoff Point ($I_C = 0$):} $V_{CE} = V_{CC}$.
    \item \textbf{Saturation Point ($V_{CE} = 0$):} $I_{C,\text{sat}} = \frac{V_{CC}}{R_C}$.
    \item \textbf{Quiescent Operating Point ($Q$-Point):} The intersection of the DC load line with the specific base current curve $I_B$:
    \begin{equation}
        Q = (V_{CEQ}, I_{CQ})
    \end{equation}
\end{itemize}
\end{derivationbox}

\section{CMOS Digital Integrated Circuits and Power Dissipation}
\subsection{CMOS Inverter Operation}
Complementary Metal-Oxide-Semiconductor (CMOS) logic integrates complementary pairs of p-channel (PMOS) and n-channel (NMOS) MOSFETs.
\begin{itemize}
    \item When input $V_{in} = \text{LOW} (0\,\text{V})$: PMOS is ON (pulls output to $V_{DD}$), NMOS is OFF. Output $V_{out} = V_{DD}$ ($\text{HIGH}$).
    \item When input $V_{in} = \text{HIGH} (V_{DD})$: PMOS is OFF, NMOS is ON (pulls output to $\text{GND}$). Output $V_{out} = 0\,\text{V}$ ($\text{LOW}$).
    \item Because one transistor is always OFF in steady-state, static current is virtually zero.
\end{itemize}

\begin{derivationbox}[CMOS Dynamic Power Dissipation Derivation]
When the CMOS inverter transitions from LOW to HIGH, energy drawn from the power supply $V_{DD}$ to charge the total output load capacitance $C_L$ is:
\begin{equation}
    E_{\text{supply}} = \int_0^\infty i(t) V_{DD} dt = V_{DD} \int_0^\infty i(t) dt = V_{DD} Q = C_L V_{DD}^2
\end{equation}
Energy stored in capacitor: $E_{\text{cap}} = \frac{1}{2} C_L V_{DD}^2$. The remaining $\frac{1}{2} C_L V_{DD}^2$ is dissipated as heat in the PMOS transistor.
During the HIGH-to-LOW transition, the capacitor discharges through NMOS to ground, dissipating the stored $\frac{1}{2} C_L V_{DD}^2$.
Total energy dissipated per full clock cycle ($0 \to 1 \to 0$) is:
\begin{equation}
    E_{\text{cycle}} = C_L V_{DD}^2
\end{equation}
For clock frequency $f$ and switching activity factor $\alpha$ ($0 \le \alpha \le 1$):
\begin{equation}
    P_{\text{dynamic}} = \alpha C_L V_{DD}^2 f
\end{equation}
Total CMOS power dissipation is the sum of dynamic and static leakage power:
\begin{equation}
    P_{\text{total}} = \alpha C_L V_{DD}^2 f + V_{DD} I_{\text{leakage}}
\end{equation}
\end{derivationbox}

\section{Semiconductor Memory Technologies and AI Hardware Accelerators}
\subsection{SRAM vs. DRAM vs. Flash SSD Memory}
\begin{table}[htbp]
\centering
\small
\caption{Comparison of Primary Semiconductor Memory Technologies}
\label{tab:memory_technologies}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Feature} & \textbf{SRAM (Static RAM)} & \textbf{DRAM (Dynamic RAM)} & \textbf{Flash SSD (NAND)} \\
\midrule
\textbf{Cell Architecture} & 6-Transistor (6T) cross-coupled CMOS latch & 1-Transistor 1-Capacitor (1T1C) cell & Floating-Gate MOSFET / 3D Charge-Trap NAND \\
\textbf{Storage Mechanism} & Bistable latch state ($Q, \bar{Q}$) & Capacitor charge ($Q = C V$) & Trapped tunneling electrons in floating gate \\
\textbf{Volatility} & Volatile (loses data on power down) & Volatile (requires periodic refresh $\sim 64\,\text{ms}$) & Non-Volatile (retains data without power) \\
\textbf{Access Latency} & Ultra-fast ($0.5 - 2\,\text{ns}$) & Fast ($10 - 20\,\text{ns}$) & Moderate/Slow ($10 - 100\,\mu\text{s}$) \\
\textbf{Integration Density} & Low (large cell area) & High ($1$ cell per bit) & Ultra-High (multi-layer 3D stacking) \\
\textbf{Cost per Bit} & Highest & Moderate & Lowest \\
\textbf{Primary Role} & CPU L1/L2/L3 On-chip Cache & Main System Memory (DDR5) & Secondary Storage, NVMe Solid State Drives \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{AI Hardware Accelerators and the Roofline Performance Model}
Modern deep learning workloads (Transformer attention, Convolutional GEMM matrix multiplications) require trillions of Multiply-Accumulate (MAC) operations.
\begin{itemize}
    \item \textbf{Systolic Arrays (Google TPU):} A 2D grid of processing elements (PEs) that stream weights and data rhythmically across adjacent registers without fetching from memory every step, dramatically lowering energy consumption.
    \item \textbf{Roofline Performance Model:} Characterizes processor operational throughput ($P$, in $\text{TFLOP/s}$) as a function of \textbf{Arithmetic Intensity} ($I$, in $\text{FLOPs/byte}$):
    \begin{equation}
        P = \min\left(P_{\text{peak}}, I \times \text{Bandwidth}_{\text{memory}}\right)
    \end{equation}
    \begin{itemize}
        \item \textbf{Memory-Bound Regime ($I < I_{\text{knee}}$):} Performance is limited by memory bandwidth ($P = I \times \text{BW}$).
        \item \textbf{Compute-Bound Regime ($I \ge I_{\text{knee}}$):} Performance saturates at hardware peak compute capacity $P_{\text{peak}}$.
    \end{itemize}
\end{itemize}

\section{IoT Sensors, IPv4 Subnetting, and Optical Fiber Communications}
\subsection{IPv4 Network Subnetting Fundamentals}
In modern IoT architectures, sensor nodes are organized into IP subnetworks. For a `/27` CIDR prefix:
\begin{itemize}
    \item \textbf{Subnet Mask:} $27$ network bits $\implies 255.255.255.224$ (Binary: $11111111.11111111.11111111.11100000$).
    \item \textbf{Host Bits:} $32 - 27 = 5$ host bits.
    \item \textbf{Total IP Addresses per Subnet:} $2^5 = 32$.
    \item \textbf{Usable Host Addresses:} $2^5 - 2 = 30$ (subtracting Network ID and Broadcast address).
\end{itemize}

\subsection{Optical Fiber Physics: Total Internal Reflection and Numerical Aperture}
Optical fibers guide light signals over long distances with minimal attenuation via \textbf{Total Internal Reflection (TIR)} at the core-cladding interface.
\begin{itemize}
    \item Refractive index condition: Core index $n_1 >$ Cladding index $n_2$.
    \item \textbf{Critical Angle ($\theta_c$):} From Snell's law ($n_1 \sin \theta_c = n_2 \sin 90^\circ$):
    \begin{equation}
        \sin \theta_c = \frac{n_2}{n_1} \implies \theta_c = \arcsin\left(\frac{n_2}{n_1}\right)
    \end{equation}
    \item \textbf{Acceptance Angle ($\theta_a$) and Numerical Aperture ($\text{NA}$):} The maximum cone of incident light accepted into the core from air ($n_0 = 1$):
    \begin{equation}
        \text{NA} = \sin \theta_a = \sqrt{n_1^2 - n_2^2}
    \end{equation}
    \item \textbf{Fractional Refractive Index Difference ($\Delta$):}
    \begin{equation}
        \Delta = \frac{n_1 - n_2}{n_1} \implies \text{NA} \approx n_1 \sqrt{2\Delta}
    \end{equation}
\end{itemize}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 2.1: Full-Wave Bridge Rectifier Design with Capacitor Filter]
\textbf{Problem:} A bridge rectifier supplied with $230\,\text{V}_{\text{rms}}, 50\,\text{Hz}$ AC uses a step-down transformer with a turns ratio of $10:1$. Silicon diodes have forward drop $V_D = 0.7\,\text{V}$. The load is $R_L = 500\,\Omega$, and a filtering capacitor $C = 1000\,\mu\text{F}$ is connected.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the secondary peak voltage $V_m$ and peak filtered DC voltage $V_{peak}$.
    \item Determine the peak-to-peak ripple voltage $V_{r(pp)}$, ripple factor $\gamma$, and DC load current $I_{dc}$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item Secondary RMS voltage: $V_{2,\text{rms}} = \frac{230}{10} = 23.0\,\text{V}_{\text{rms}}$.
    Peak secondary voltage: $V_m = \sqrt{2} \times 23.0\,\text{V} = \mathbf{32.53\,\text{V}}$.
    Accounting for two conducting diodes in bridge:
    \begin{equation}
        V_{peak} = V_m - 2 V_D = 32.53 - 2(0.7) = \mathbf{31.13\,\text{V}}
    \end{equation}
    \item \textbf{Ripple and DC Current:}
    Ripple frequency: $f_r = 2 f = 2 \times 50 = 100\,\text{Hz}$.
    \begin{align}
        V_{r(pp)} &= \frac{V_{peak}}{2 f C R_L} = \frac{31.13}{2(50)(1000 \times 10^{-6})(500)} = \frac{31.13}{50} = \mathbf{0.623\,\text{V}} \\
        V_{dc} &= V_{peak} - \frac{V_{r(pp)}}{2} = 31.13 - 0.31 = \mathbf{30.82\,\text{V}} \\
        I_{dc} &= \frac{V_{dc}}{R_L} = \frac{30.82\,\text{V}}{500\,\Omega} = \mathbf{61.64\,\text{mA}} \\
        \gamma &= \frac{V_{r(pp)}}{2\sqrt{3} V_{dc}} = \frac{0.623}{2\sqrt{3}(30.82)} = \frac{0.623}{106.76} = \mathbf{0.00583} \quad (0.583\%)
    \end{align}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 2.2: BJT Voltage Divider Bias Circuit $Q$-Point Calculation]
\textbf{Problem:} A silicon NPN transistor ($\beta = 100, V_{BE} = 0.7\,\text{V}$) is configured in a voltage divider bias circuit with $V_{CC} = 15.0\,\text{V}$, $R_1 = 39\,\text{k}\Omega$, $R_2 = 10\,\text{k}\Omega$, $R_C = 2.2\,\text{k}\Omega$, and $R_E = 1.0\,\text{k}\Omega$.
Determine the Thevenin equivalent base voltage $V_{TH}$, base resistance $R_{TH}$, base current $I_B$, collector current $I_C$, and collector-emitter voltage $V_{CE}$ at the $Q$-point.

\textbf{Solution:}
\begin{enumerate}
    \item \textbf{Thevenin Equivalent Circuit at the Base:}
    \begin{align}
        V_{TH} &= V_{CC}\left(\frac{R_2}{R_1 + R_2}\right) = 15.0\left(\frac{10}{39 + 10}\right) = 15.0\left(\frac{10}{49}\right) = \mathbf{3.061\,\text{V}} \\
        R_{TH} &= R_1 \parallel R_2 = \frac{39 \times 10}{49}\,\text{k}\Omega = \mathbf{7.959\,\text{k}\Omega}
    \end{align}
    \item \textbf{Base and Collector Currents:}
    Applying KVL around the base-emitter loop ($V_{TH} - I_B R_{TH} - V_{BE} - I_E R_E = 0$, with $I_E = (\beta+1)I_B$):
    \begin{align}
        I_B &= \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1)R_E} = \frac{3.061 - 0.70}{7959 + (101)(1000)} = \frac{2.361}{108{,}959} = \mathbf{21.67\,\mu\text{A}} \\
        I_C &= \beta I_B = 100 \times 21.67\,\mu\text{A} = \mathbf{2.167\,\text{mA}} \\
        I_E &= I_B + I_C = 2.189\,\text{mA}
    \end{align}
    \item \textbf{Collector-Emitter Voltage ($V_{CE}$):}
    Applying KVL to the collector-emitter loop:
    \begin{align}
        V_{CE} &= V_{CC} - I_C R_C - I_E R_E = 15.0 - (2.167 \times 10^{-3})(2200) - (2.189 \times 10^{-3})(1000) \\
        &= 15.0 - 4.767 - 2.189 = \mathbf{8.044\,\text{V}}
    \end{align}
    The quiescent operating point is $Q = (8.04\,\text{V}, 2.17\,\text{mA})$ in the active region ($V_{CE} > 0.2\,\text{V}$).
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 2.3: CMOS Microprocessor Dynamic Power Scaling]
\textbf{Problem:} A 64-bit multi-core CMOS processor with total switching capacitance $C_L = 25.0\,\text{nF}$ operates at clock frequency $f_1 = 3.2\,\text{GHz}$ with supply voltage $V_{DD1} = 1.20\,\text{V}$ and average activity factor $\alpha = 0.20$.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the baseline dynamic power dissipation $P_1$.
    \item To reduce heat generation, Dynamic Voltage and Frequency Scaling (DVFS) reduces $V_{DD2}$ to $0.95\,\text{V}$ and frequency to $f_2 = 2.4\,\text{GHz}$. Compute the new dynamic power $P_2$ and percentage power reduction.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Baseline Dynamic Power:}
    \begin{align}
        P_1 &= \alpha C_L V_{DD1}^2 f_1 = (0.20)(25.0 \times 10^{-9}\,\text{F})(1.20\,\text{V})^2(3.2 \times 10^9\,\text{s}^{-1}) \\
        &= (0.20)(25.0 \times 10^{-9})(1.44)(3.2 \times 10^9) = \mathbf{23.04\,\text{W}}
    \end{align}
    \item \textbf{Scaled Dynamic Power:}
    \begin{align}
        P_2 &= \alpha C_L V_{DD2}^2 f_2 = (0.20)(25.0 \times 10^{-9})(0.95)^2(2.4 \times 10^9) \\
        &= (0.20)(25.0 \times 10^{-9})(0.9025)(2.4 \times 10^9) = \mathbf{10.83\,\text{W}}
    \end{align}
    Percentage Power Reduction:
    \begin{equation}
        \Delta P\% = \frac{P_1 - P_2}{P_1} \times 100\% = \frac{23.04 - 10.83}{23.04} \times 100\% = \frac{12.21}{23.04} \times 100\% = \mathbf{53.0\%}
    \end{equation}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 2.4: Optical Fiber Numerical Aperture and Modal Propagation]
\textbf{Problem:} A step-index glass optical fiber has a core refractive index $n_1 = 1.480$ and a cladding refractive index $n_2 = 1.455$, launched from air ($n_0 = 1.0$).
\begin{enumerate}[label=(\alph*)]
    \item Calculate the critical angle $\theta_c$ at the core-cladding interface.
    \item Compute the numerical aperture $\text{NA}$ and maximum acceptance angle $\theta_a$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Critical Angle:}
    \begin{equation}
        \sin \theta_c = \frac{n_2}{n_1} = \frac{1.455}{1.480} = 0.9831 \implies \theta_c = \arcsin(0.9831) = \mathbf{79.45^\circ}
    \end{equation}
    \item \textbf{Numerical Aperture and Acceptance Angle:}
    \begin{align}
        \text{NA} &= \sqrt{n_1^2 - n_2^2} = \sqrt{(1.480)^2 - (1.455)^2} = \sqrt{2.1904 - 2.1170} = \sqrt{0.073375} = \mathbf{0.2709} \\
        \sin \theta_a &= \text{NA} = 0.2709 \implies \theta_a = \arcsin(0.2709) = \mathbf{15.72^\circ}
    \end{align}
\end{enumerate}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Circuit Theorems:} KCL is charge conservation ($\sum I = 0$); KVL is energy conservation ($\sum V = 0$).
    \item \textbf{Rectifier Systems:} Bridge rectifiers achieve $81.2\%$ efficiency with ripple frequency $2f$. A capacitor filter yields ripple $\gamma = \frac{1}{4\sqrt{3} f C R_L}$.
    \item \textbf{BJT Amplification:} In active mode ($V_{BE} \approx 0.7\,\text{V}$, CBJ reverse-biased), $I_C = \beta I_B$. The DC load line defines the $Q$-point.
    \item \textbf{CMOS Power:} Dynamic power scales quadratically with voltage: $P = \alpha C_L V_{DD}^2 f$.
    \item \textbf{Memory Cells:} SRAM (6T fast cache), DRAM (1T1C high density), Flash (non-volatile floating gate).
    \item \textbf{Roofline Model:} $P = \min(P_{\text{peak}}, I \times \text{BW})$, differentiating compute-bound and memory-bound AI workloads.
    \item \textbf{Optical Fibers:} Total internal reflection occurs when $n_1 > n_2$. Numerical aperture $\text{NA} = \sqrt{n_1^2 - n_2^2} = \sin \theta_a$.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-02-electricity-and-devices.tex", "w") as f:
    f.write(ch2)

print("Chapter 2 generated.")

# ==============================================================================
# CHAPTER 3
# ==============================================================================
ch3 = r"""\chapter{Introduction to Number Systems and Logic Gates}
\label{chap:number_systems_logic}

\section{Introduction and Theoretical Foundations}
Digital computation, microprocessors, and embedded systems process information exclusively in discrete binary representations. In this chapter, we develop the rigorous mathematical foundations of positional number systems, specialized binary codes (BCD, Excess-3, Gray code), radix and diminished radix complements, signed arithmetic, Boolean algebraic theorems, canonical forms, Karnaugh map (K-map) optimization, and hardware logic hazard elimination.

\section{Positional Number Systems and Radix Conversions}
\subsection{Mathematical Formulation of Base-$r$ Systems}
In a positional numeral system with radix (base) $r \in \mathbb{Z}^+$ ($r \ge 2$), any real number $N$ is represented as a polynomial sequence of digits $d_i$:
\begin{equation}
    (N)_r = \sum_{i=-m}^{n-1} d_i r^i = d_{n-1} r^{n-1} + d_{n-2} r^{n-2} + \dots + d_1 r^1 + d_0 r^0 + d_{-1} r^{-1} + \dots + d_{-m} r^{-m}
\end{equation}
where each digit $d_i \in \{0, 1, \dots, r-1\}$.
\begin{itemize}
    \item \textbf{Binary ($r = 2$):} Digits $\{0, 1\}$.
    \item \textbf{Octal ($r = 8$):} Digits $\{0, 1, 2, 3, 4, 5, 6, 7\}$ (Each octal digit maps to 3 binary bits: $2^3 = 8$).
    \item \textbf{Decimal ($r = 10$):} Digits $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.
    \item \textbf{Hexadecimal ($r = 16$):} Digits $\{0-9, \text{A}(10), \text{B}(11), \text{C}(12), \text{D}(13), \text{E}(14), \text{F}(15)\}$ (Each hex digit maps to 4 binary bits: $2^4 = 16$).
\end{itemize}

\subsection{Systematic Base Conversion Algorithms}
\begin{enumerate}
    \item \textbf{Radix-$r$ to Decimal Conversion:} Directly evaluate the polynomial expansion $\sum d_i r^i$.
    \item \textbf{Decimal to Radix-$r$ Integer Conversion (Successive Division):} Divide the decimal integer repeatedly by base $r$. The sequence of remainders read from bottom to top (last remainder to first) forms the radix-$r$ number (MSB to LSB).
    \item \textbf{Decimal to Radix-$r$ Fraction Conversion (Successive Multiplication):} Multiply the fractional part repeatedly by base $r$. The sequence of generated integer parts read from top to bottom forms the fractional radix-$r$ digits.
    \item \textbf{Binary $\leftrightarrow$ Octal $\leftrightarrow$ Hexadecimal Conversions:} Group binary bits in sets of 3 (for octal) or 4 (for hex), starting from the radix point and moving outward (left for integer, right for fraction, zero-padding outer ends as needed).
\end{enumerate}

\section{Specialized Binary Codes}
\subsection{Binary Coded Decimal (BCD 8421)}
In BCD 8421, each decimal digit ($0-9$) is encoded as an independent 4-bit weighted binary nibble with weights $8, 4, 2, 1$.
\begin{itemize}
    \item Decimal $0$ to $9$ are represented by $0000_2$ to $1001_2$.
    \item The six 4-bit combinations $1010_2$ to $1111_2$ ($10$ to $15$) are \textbf{illegal/invalid BCD codes}.
    \item \textbf{BCD Addition Rule:} If 4-bit binary addition of two BCD digits produces a sum $\ge 10_{10}$ or generates a binary carry-out ($C=1$), the result is corrected by adding $+6$ ($0110_2$) to skip the 6 illegal states.
\end{itemize}

\subsection{Excess-3 Code (XS-3)}
Excess-3 is an unweighted binary code derived by adding decimal $3$ ($0011_2$) to each BCD digit:
\begin{equation}
    \text{XS-3}(D) = \text{BCD}(D) + 0011_2
\end{equation}
\begin{conceptbox}[Self-Complementing Property of Excess-3 Code]
Excess-3 is a \textbf{self-complementing code}: the 1's complement (bitwise inversion) of an Excess-3 codeword directly produces the 9's complement of the corresponding decimal digit:
\begin{equation}
    \overline{\text{XS-3}(D)} = \text{XS-3}(9 - D)
\end{equation}
For example, for $D=2$ ($\text{XS-3} = 0101_2$), bitwise inversion gives $1010_2$, which is $\text{XS-3}(7) = \text{XS-3}(9-2)$. This simplifies decimal subtraction in early computing hardware.
\end{conceptbox}

\subsection{Gray Code (Reflected Binary Code)}
Gray code is an unweighted, non-arithmetic code in which two consecutive numerical values differ by \textbf{only a single bit} (unit Hamming distance).

\begin{derivationbox}[Binary-to-Gray and Gray-to-Binary Conversion Algorithms]
\begin{enumerate}
    \item \textbf{Binary to Gray Conversion:}
    Given an $n$-bit binary word $B = B_{n-1} B_{n-2} \dots B_1 B_0$:
    \begin{align}
        G_{n-1} &= B_{n-1} \quad (\text{MSB remains unchanged}) \\
        G_i &= B_{i+1} \oplus B_i \quad \text{for } i = n-2, n-3, \dots, 0
    \end{align}
    \item \textbf{Gray to Binary Conversion:}
    Given an $n$-bit Gray code word $G = G_{n-1} G_{n-2} \dots G_1 G_0$:
    \begin{align}
        B_{n-1} &= G_{n-1} \quad (\text{MSB remains unchanged}) \\
        B_i &= B_{i+1} \oplus G_i \quad \text{for } i = n-2, n-3, \dots, 0
    \end{align}
\end{enumerate}
Gray codes prevent multi-bit transient glitches in optical rotary shaft encoders and asynchronous FIFO pointer synchronization across clock domains.
\end{derivationbox}

\section{Complements and Signed Binary Arithmetic}
\subsection{Radix and Diminished Radix Complements}
For an $n$-digit base-$r$ integer $N$:
\begin{enumerate}
    \item \textbf{Diminished Radix Complement ($(r-1)$'s Complement):}
    \begin{equation}
        (r-1)\text{'s Complement} = (r^n - 1) - N
    \end{equation}
    In binary ($r=2$), the 1's complement is obtained by inverting every bit ($0 \leftrightarrow 1$).
    \item \textbf{Radix Complement ($r$'s Complement):}
    \begin{equation}
        r\text{'s Complement} = r^n - N = [(r^n - 1) - N] + 1 = (r-1)\text{'s Complement} + 1
    \end{equation}
    In binary ($r=2$), the 2's complement is obtained by inverting all bits and adding $1$ to the LSB:
    \begin{equation}
        \text{2's Complement}(N) = \bar{N} + 1
    \end{equation}
\end{enumerate}

\subsection{Signed Binary Number Representations}
For an $n$-bit signed binary word:
\begin{table}[htbp]
\centering
\small
\caption{Comparison of $n$-bit Signed Number Systems}
\label{tab:signed_systems}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Representation} & \textbf{Dynamic Number Range} & \textbf{Zero Representations} & \textbf{Arithmetic Complexity} \\
\midrule
\textbf{Signed Magnitude} & $-(2^{n-1}-1) \text{ to } +(2^{n-1}-1)$ & Two ($+0 = 00\dots0, -0 = 10\dots0$) & High (requires sign comparison) \\
\textbf{1's Complement} & $-(2^{n-1}-1) \text{ to } +(2^{n-1}-1)$ & Two ($+0 = 00\dots0, -0 = 11\dots1$) & Requires end-around carry \\
\textbf{2's Complement} & $-2^{n-1} \text{ to } +(2^{n-1}-1)$ & \textbf{Unique} ($0000\dots0$) & Standard unified adder/subtractor \\
\bottomrule
\end{tabularx}
\end{table}

\begin{derivationbox}[2's Complement Subtraction and Overflow Detection]
To compute subtraction $A - B$ using an $n$-bit adder:
\begin{equation}
    A - B = A + (\bar{B} + 1)
\end{equation}
\begin{itemize}
    \item If a final carry-out occurs ($C_n = 1$), it is discarded, and the result is positive.
    \item If no carry-out occurs ($C_n = 0$), the result is negative and in 2's complement form.
    \item \textbf{Signed Overflow Detection ($V$):}
    When adding two numbers of the same sign, an overflow occurs if the result has the opposite sign:
    \begin{equation}
        V = C_n \oplus C_{n-1}
    \end{equation}
    where $C_n$ is the carry out of the MSB (sign bit) and $C_{n-1}$ is the carry into the MSB. An overflow ($V = 1$) indicates that the true arithmetic result exceeds the representable range $[-2^{n-1}, +2^{n-1}-1]$.
\end{itemize}
\end{derivationbox}

\section{Logic Gates, Universal Gates, and Boolean Algebra}
\subsection{Primary and Special Logic Gates}
\begin{itemize}
    \item \textbf{Primary Gates:}
    \begin{itemize}
        \item \textbf{AND Gate:} $Y = A \cdot B$ (Output is 1 if and only if all inputs are 1).
        \item \textbf{OR Gate:} $Y = A + B$ (Output is 1 if any input is 1).
        \item \textbf{NOT Gate (Inverter):} $Y = \bar{A}$ (Output is the logical inversion of the input).
    \end{itemize}
    \item \textbf{Universal Gates:}
    \begin{itemize}
        \item \textbf{NAND Gate:} $Y = \overline{A \cdot B}$.
        \item \textbf{NOR Gate:} $Y = \overline{A + B}$.
        Any arbitrary Boolean function can be synthesized using exclusively NAND or exclusively NOR gates.
    \end{itemize}
    \item \textbf{Special Exclusive Gates:}
    \begin{itemize}
        \item \textbf{XOR Gate (Odd Parity Detector):} $Y = A \oplus B = \bar{A}B + A\bar{B}$. Output is 1 when inputs differ.
        \item \textbf{XNOR Gate (Equivalence Gate):} $Y = A \odot B = \overline{A \oplus B} = AB + \bar{A}\bar{B}$. Output is 1 when inputs are identical.
    \end{itemize}
\end{itemize}

\subsection{Fundamental Postulates and Theorems of Boolean Algebra}
\begin{table}[htbp]
\centering
\small
\caption{Key Theorems and Axioms of Boolean Algebra}
\label{tab:boolean_theorems}
\begin{tabularx}{\textwidth}{lXX}
\toprule
\textbf{Theorem Name} & \textbf{AND Form} & \textbf{OR Form} \\
\midrule
\textbf{Identity Law} & $A \cdot 1 = A$ & $A + 0 = A$ \\
\textbf{Null / Annihilation Law} & $A \cdot 0 = 0$ & $A + 1 = 1$ \\
\textbf{Idempotent Law} & $A \cdot A = A$ & $A + A = A$ \\
\textbf{Complementarity Law} & $A \cdot \bar{A} = 0$ & $A + \bar{A} = 1$ \\
\textbf{Involution Law} & $\overline{\overline{A}} = A$ & --- \\
\textbf{Commutative Law} & $A \cdot B = B \cdot A$ & $A + B = B + A$ \\
\textbf{Associative Law} & $A(BC) = (AB)C$ & $A + (B + C) = (A + B) + C$ \\
\textbf{Distributive Law} & $A + BC = (A+B)(A+C)$ & $A(B+C) = AB + AC$ \\
\textbf{Absorption Law} & $A(A + B) = A$ & $A + AB = A$ \\
\textbf{Elimination Law} & $A(\bar{A} + B) = AB$ & $A + \bar{A}B = A + B$ \\
\textbf{Consensus Theorem} & $(A+B)(\bar{A}+C)(B+C) = (A+B)(\bar{A}+C)$ & $AB + \bar{A}C + BC = AB + \bar{A}C$ \\
\textbf{De Morgan's Laws} & $\overline{A \cdot B} = \bar{A} + \bar{B}$ & $\overline{A + B} = \bar{A} \cdot \bar{B}$ \\
\bottomrule
\end{tabularx}
\end{table}

\section{Canonical Forms and Karnaugh Map (K-Map) Optimization}
\subsection{Canonical Minterms and Maxterms}
For an $n$-variable Boolean function $F(x_1, x_2, \dots, x_n)$:
\begin{itemize}
    \item \textbf{Minterm ($m_i$):} A product term containing all $n$ literals in either true or complemented form that equals 1 for exactly one row of the truth table.
    \item \textbf{Maxterm ($M_i$):} A sum term containing all $n$ literals in either true or complemented form that equals 0 for exactly one row of the truth table.
    \item Relationship: $M_i = \overline{m_i}$.
    \item \textbf{Canonical Sum-of-Products (SOP):} $F = \sum m(\text{indices where } F=1)$.
    \item \textbf{Canonical Product-of-Sums (POS):} $F = \prod M(\text{indices where } F=0)$.
\end{itemize}

\subsection{Karnaugh Map Minimization Principles}
A Karnaugh Map is a 2D graphical representation of a truth table arranged in \textbf{Gray code order} ($00, 01, 11, 10$) so that adjacent cells differ by exactly one binary variable.

\begin{conceptbox}[Rules for K-Map Grouping]
\begin{enumerate}
    \item Group size must be an integer power of 2 ($1, 2, 4, 8, 16$).
    \item Groups must be rectangular or square; diagonal grouping is strictly invalid.
    \item Groups wrap around edges and corners (toroidal adjacency).
    \item Groups should be made as large as possible to eliminate the maximum number of literals ($2^k$ cells eliminate $k$ variables).
    \item Every 1-cell must be included in at least one group.
    \item \textbf{Prime Implicant (PI):} A rectangular group of $2^k$ 1-cells that cannot be merged into a larger valid group.
    \item \textbf{Essential Prime Implicant (EPI):} A Prime Implicant that contains at least one 1-cell not covered by any other prime implicant. All EPIs must appear in the minimal SOP expression.
    \item \textbf{Don't Care Conditions ($d$):} Input combinations that cannot occur or whose outputs are irrelevant may be treated as 1s (to enlarge groups) or 0s (to avoid creating extra groups).
\end{enumerate}
\end{conceptbox}

\section{Logic Hazards and Glitch Elimination}
\subsection{Static-1 and Static-0 Hazards}
In physical logic gates, propagation delays through complementary signal paths are not instantaneous.
\begin{itemize}
    \item \textbf{Static-1 Hazard:} A condition where an output is expected to remain steadily at 1 during an input variable transition, but momentarily glitches to 0 due to asymmetric gate delays.
    \item \textbf{Static-0 Hazard:} A condition where an output is expected to remain steadily at 0, but momentarily glitches to 1.
\end{itemize}

\begin{derivationbox}[Hazard Detection and Elimination via Consensus Terms]
Consider the minimal SOP expression:
\begin{equation}
    F = A B + \bar{A} C
\end{equation}
When inputs change from $A=1, B=1, C=1$ to $A=0, B=1, C=1$:
\begin{itemize}
    \item Term $AB$ transitions from $1 \to 0$.
    \item Term $\bar{A}C$ transitions from $0 \to 1$.
    \item If the inverter producing $\bar{A}$ introduces propagation delay $t_{pd}$, there exists a transient duration where both $A=0$ and $\bar{A}=0$, causing $F = 0 + 0 = 0$ (a static-1 glitch).
\end{itemize}
\textbf{Elimination Method:} On the K-map, static hazards occur between adjacent 1-cells covered by different prime implicant groups. Adding the \textbf{consensus prime implicant} $BC$ covers the transition:
\begin{equation}
    F_{\text{hazard-free}} = A B + \bar{A} C + B C
\end{equation}
When $B=1$ and $C=1$, the consensus term $BC=1$ holds the output HIGH regardless of fluctuations in $A$ or $\bar{A}$.
\end{derivationbox}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 3.1: Complete Radix Conversions and Arithmetic]
\textbf{Problem:}
\begin{enumerate}[label=(\alph*)]
    \item Convert decimal $(427.6875)_{10}$ into binary, octal, and hexadecimal representations.
    \item Perform binary subtraction $(01100100)_2 - (00111100)_2$ ($100_{10} - 60_{10}$) using 8-bit 2's complement arithmetic and verify the overflow flag.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Integer Part ($427_{10}$):}
    \begin{align*}
        427 / 2 &= 213 \text{ rem } 1 \quad (\text{LSB}) \\
        213 / 2 &= 106 \text{ rem } 1 \\
        106 / 2 &= 53 \text{ rem } 0 \\
        53 / 2 &= 26 \text{ rem } 1 \\
        26 / 2 &= 13 \text{ rem } 0 \\
        13 / 2 &= 6 \text{ rem } 1 \\
        6 / 2 &= 3 \text{ rem } 0 \\
        3 / 2 &= 1 \text{ rem } 1 \\
        1 / 2 &= 0 \text{ rem } 1 \quad (\text{MSB}) \implies (427)_{10} = (110101011)_2
    \end{align*}
    \textbf{Fractional Part ($0.6875_{10}$):}
    \begin{align*}
        0.6875 \times 2 &= 1.3750 \implies \text{int } 1 \\
        0.3750 \times 2 &= 0.7500 \implies \text{int } 0 \\
        0.7500 \times 2 &= 1.5000 \implies \text{int } 1 \\
        0.5000 \times 2 &= 1.0000 \implies \text{int } 1 \implies (0.6875)_{10} = (0.1011)_2
    \end{align*}
    Combined Binary: $(427.6875)_{10} = \mathbf{(110101011.1011)_2}$.
    \begin{itemize}
        \item \textbf{Octal:} Grouping in 3s: $(110\,101\,011.101\,100)_2 = \mathbf{(653.54)_8}$.
        \item \textbf{Hexadecimal:} Grouping in 4s: $(0001\,1010\,1011.1011)_2 = \mathbf{(1\text{AB}.\text{B})_{16}}$.
    \end{itemize}
    \item \textbf{8-Bit 2's Complement Subtraction:}
    $A = 01100100_2$, $B = 00111100_2$.
    1's complement of $B$: $\bar{B} = 11000011_2$.
    2's complement of $B$: $\bar{B} + 1 = 11000100_2$.
    \begin{align*}
        A + (\bar{B} + 1) &= 01100100_2 + 11000100_2 \\
        &= (1)\,00101000_2
    \end{align*}
    Discarding the end-around carry $C_8 = 1$, the result is $00101000_2 = 32 + 8 = \mathbf{40_{10}}$.
    Carry into MSB ($C_7$) is $1$, carry out of MSB ($C_8$) is $1$.
    Overflow flag: $V = C_8 \oplus C_7 = 1 \oplus 1 = \mathbf{0}$ (No overflow, result is valid).
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 3.2: 4-Variable K-Map Minimization with Don't Cares]
\textbf{Problem:} Minimize the following 4-variable Boolean function into minimal Sum-of-Products (SOP) and Product-of-Sums (POS) forms:
\begin{equation}
    F(A,B,C,D) = \sum m(1, 3, 7, 11, 15) + d(0, 2, 5)
\end{equation}

\textbf{Solution:}
Plotting the 1s and don't cares ($d$) on the $4 \times 4$ K-map ($AB \times CD$):
\begin{itemize}
    \item Row $00$: $m(0)=d, m(1)=1, m(3)=1, m(2)=d$.
    \item Row $01$: $m(4)=0, m(5)=d, m(7)=1, m(6)=0$.
    \item Row $11$: $m(12)=0, m(13)=0, m(15)=1, m(14)=0$.
    \item Row $10$: $m(8)=0, m(9)=0, m(11)=1, m(10)=0$.
\end{itemize}
\textbf{SOP Grouping:}
\begin{enumerate}
    \item Octet formed by Row $00$ combined with column $11$ ($m_0, m_1, m_2, m_3$ with $m_7, m_{15}, m_{11}$ and $m_5=d$):
    \begin{itemize}
        \item Group 1 (Quad of column $CD=11$): cells $\{3, 7, 15, 11\} \implies \mathbf{CD}$.
        \item Group 2 (Quad of row $AB=00$): cells $\{0, 1, 3, 2\} \implies \mathbf{\bar{A}\bar{B}}$.
    \end{itemize}
\end{enumerate}
\textbf{Minimal SOP Expression:}
\begin{equation}
    F_{\text{min, SOP}} = \bar{A}\bar{B} + C D
\end{equation}
\textbf{Minimal POS Expression:}
\begin{equation}
    F_{\text{min, POS}} = (\bar{A} + C)(\bar{B} + D)(\bar{A} + D)
\end{equation}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Number Systems:} Positional polynomial $\sum d_i r^i$. Successive division for integers, multiplication for fractions.
    \item \textbf{Codes:} BCD adds $+6$ on correction ($>9$); Excess-3 is self-complementing; Gray code has unit Hamming distance ($G_i = B_{i+1} \oplus B_i$).
    \item \textbf{Complements:} 2's complement $\bar{N}+1$. Subtraction $A-B = A + (\bar{B}+1)$. Overflow occurs when $V = C_n \oplus C_{n-1} = 1$.
    \item \textbf{Universal Gates:} Both NAND and NOR can synthesize NOT, AND, OR, XOR, and XNOR gates.
    \item \textbf{K-Map Minimization:} Groups must be powers of 2. Essential Prime Implicants contain unique 1s.
    \item \textbf{Static Hazards:} Prevented by adding redundant consensus prime implicants to cover adjacent group boundaries.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-03-number-systems-and-logic.tex", "w") as f:
    f.write(ch3)

print("Chapter 3 generated.")

# ==============================================================================
# CHAPTER 4
# ==============================================================================
ch4 = r"""\chapter{Combinational Logic Circuits: Arithmetic, Routing, and Decoding}
\label{chap:combinational_logic}

\section{Introduction and Characteristics of Combinational Logic}
Combinational logic circuits are memoryless digital networks whose output at any instant depends strictly on the current combination of input signals. In this chapter, we explore arithmetic modules (adders, subtractors, Carry Lookahead Adders), data routing multiplexers/demultiplexers, decoding/encoding structures (priority encoders, BCD-to-7-segment decoders), and digital magnitude comparators.

\section{Arithmetic Combinational Circuits}
\subsection{Half Adder and Full Adder Modules}
\begin{enumerate}
    \item \textbf{Half Adder (HA):} Adds two 1-bit binary operands $A$ and $B$, generating a Sum ($S$) and Carry-out ($C_{out}$):
    \begin{align}
        S &= A \oplus B = \bar{A}B + A\bar{B} \\
        C_{out} &= A \cdot B
    \end{align}
    A Half Adder cannot accept an incoming carry from a preceding less-significant stage.
    \item \textbf{Full Adder (FA):} Adds three 1-bit binary inputs: two data bits $A, B$ and a Carry-in $C_{in}$:
    \begin{align}
        S &= A \oplus B \oplus C_{in} \\
        C_{out} &= A B + B C_{in} + A C_{in} = A B + C_{in}(A \oplus B)
    \end{align}
    A Full Adder can be constructed using two Half Adders and an OR gate.
\end{enumerate}

\subsection{Ripple Carry Adder (RCA) and Timing Bottleneck}
An $n$-bit parallel Ripple Carry Adder cascades $n$ Full Adders such that the carry output $C_i$ of each stage ripples to the carry input $C_{in}$ of the next higher stage.
\begin{itemize}
    \item \textbf{Propagation Delay Bottleneck:} The MSB sum $S_{n-1}$ and final carry $C_n$ cannot stabilize until the carry ripples through all preceding $n$ stages.
    \item Total worst-case propagation delay for an $n$-bit RCA:
    \begin{equation}
        T_{\text{RCA}} = (n - 1) t_{\text{carry}} + t_{\text{sum}}
    \end{equation}
    where $t_{\text{carry}}$ is the carry propagation delay per stage and $t_{\text{sum}}$ is the sum generation delay.
\end{itemize}

\subsection{Carry Lookahead Adder (CLA): High-Speed Addition}
To eliminate the linear ripple delay $O(n)$, the Carry Lookahead Adder (CLA) computes all carry signals in parallel using two auxiliary functions for each bit position $i$:
\begin{align}
    \text{\textbf{Carry Generate:}} \quad G_i &= A_i \cdot B_i \quad (\text{Generates a carry regardless of } C_i) \\
    \text{\textbf{Carry Propagate:}} \quad P_i &= A_i \oplus B_i \quad (\text{Propagates an incoming carry } C_i)
\end{align}

\begin{derivationbox}[Carry Lookahead Recursive Carry Expansions]
The sum and stage carry expressions are:
\begin{align}
    S_i &= P_i \oplus C_i \\
    C_{i+1} &= G_i + P_i C_i
\end{align}
Expanding recursively for a 4-bit CLA:
\begin{align}
    C_1 &= G_0 + P_0 C_0 \\
    C_2 &= G_1 + P_1 C_1 = G_1 + P_1(G_0 + P_0 C_0) = G_1 + P_1 G_0 + P_1 P_0 C_0 \\
    C_3 &= G_2 + P_2 C_2 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0 \\
    C_4 &= G_3 + P_3 C_3 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0
\end{align}
Every carry bit $C_{i+1}$ is expressed as a direct two-level SOP function of initial carry $C_0$ and input operands ($G_k, P_k$).
Thus, all carries are computed simultaneously in constant time $O(1)$ (typically 2 to 3 gate delays), independent of word width $n$.
\end{derivationbox}

\subsection{4-Bit Parallel Adder-Subtractor with Overflow Detection}
A versatile arithmetic module capable of computing both addition ($A + B$) and subtraction ($A - B$) uses four Full Adders and four controlled XOR inverters driven by a Mode line $M$:
\begin{itemize}
    \item Connect operand $A_i$ directly to FA input $A_i$. Connect operand $B_i$ to one XOR input, with Mode line $M$ to the other XOR input. Connect Mode line $M$ directly to initial carry-in $C_0$.
    \item \textbf{When $M = 0$ (Addition Mode):}
    \begin{equation}
        B_i \oplus 0 = B_i, \quad C_0 = 0 \implies \text{Computes } A + B + 0 = A + B
    \end{equation}
    \item \textbf{When $M = 1$ (Subtraction Mode):}
    \begin{equation}
        B_i \oplus 1 = \bar{B}_i, \quad C_0 = 1 \implies \text{Computes } A + \bar{B} + 1 = A - B
    \end{equation}
    \item \textbf{Signed Overflow Flag ($V$):}
    \begin{equation}
        V = C_4 \oplus C_3
    \end{equation}
\end{itemize}

\section{Multiplexers (Data Selectors) and Boolean Synthesis}
\subsection{Multiplexer Architecture}
A Multiplexer (MUX) is a digital selector with $2^n$ data inputs ($I_0, I_1, \dots, I_{2^n-1}$), $n$ select control lines ($S_{n-1}, \dots, S_0$), and a single output $Y$:
\begin{itemize}
    \item \textbf{4-to-1 MUX ($n=2$ select lines $S_1, S_0$):}
    \begin{equation}
        Y = \bar{S}_1 \bar{S}_0 I_0 + \bar{S}_1 S_0 I_1 + S_1 \bar{S}_0 I_2 + S_1 S_0 I_3
    \end{equation}
    \item \textbf{8-to-1 MUX ($n=3$ select lines $S_2, S_1, S_0$):}
    \begin{equation}
        Y = \sum_{k=0}^7 m_k(S_2, S_1, S_0) \cdot I_k
    \end{equation}
\end{itemize}

\subsection{Universal Boolean Function Synthesis Using Multiplexers}
Any $n$-variable Boolean function $F(x_1, x_2, \dots, x_n)$ can be synthesized using a single $2^{n-1}$-to-1 MUX:
\begin{enumerate}
    \item Connect $(n-1)$ variables to select lines $S_{n-2}, \dots, S_0$.
    \item The remaining variable $x_n$ provides data inputs ($I_k \in \{0, 1, x_n, \bar{x}_n\}$).
    \item Construct an implementation table comparing minterms where the function is 1 against $x_n = 0$ and $x_n = 1$.
\end{enumerate}

\section{Demultiplexers, Decoders, and Display Drivers}
\subsection{Decoders and Demultiplexers}
\begin{itemize}
    \item \textbf{Demultiplexer (DEMUX):} Directs a single data input $D_{in}$ to one of $2^n$ output lines based on $n$ select lines.
    \item \textbf{Binary Decoder:} Converts an $n$-bit binary code into $2^n$ unique active outputs.
    \item \textbf{3-to-8 Active-Low Decoder (74138):} Uses three enable pins ($G_1, \bar{G}_{2A}, \bar{G}_{2B}$) to decode inputs $A, B, C$ into active-low outputs $\bar{Y}_0$ to $\bar{Y}_7$:
    \begin{equation}
        \bar{Y}_k = \overline{m_k(A, B, C)}
    \end{equation}
    \item \textbf{Synthesizing Multi-Output Logic with Decoders:} Since each decoder output corresponds to a minterm, connecting selected active-low outputs to a multi-input NAND gate realizes any arbitrary SOP function:
    \begin{equation}
        F = \sum m(1, 2, 5, 7) \implies F = \overline{\bar{Y}_1 \cdot \bar{Y}_2 \cdot \bar{Y}_5 \cdot \bar{Y}_7}
    \end{equation}
\end{itemize}

\subsection{BCD-to-7-Segment Decoder/Driver}
Drives 7 LED segments ($a, b, c, d, e, f, g$) to render decimal numbers $0-9$:
\begin{itemize}
    \item \textbf{Common Anode Display:} All LED anodes connect to $V_{CC}$; driven by active-low segment outputs ($\text{LOW} = \text{ON}$).
    \item \textbf{Common Cathode Display:} All LED cathodes connect to ground; driven by active-high segment outputs ($\text{HIGH} = \text{ON}$).
\end{itemize}

\section{Encoders and Priority Encoders}
\subsection{Standard Encoders vs. Priority Encoders}
A standard $2^n$-to-$n$ encoder performs the reverse operation of a decoder. However, standard encoders fail if multiple input lines are active simultaneously or if all inputs are zero.

\begin{derivationbox}[Priority Encoder (74148) Architecture and Truth Table]
A 4-input Priority Encoder accepts four inputs ($D_0, D_1, D_2, D_3$), where $D_3$ has the highest priority and $D_0$ has the lowest priority. It generates a 2-bit binary output ($Y_1, Y_0$) and a \textbf{Valid Bit} ($V$) indicating if any input is active.

\begin{center}
\small
\begin{tabular}{cccc|ccc}
\toprule
\multicolumn{4}{c|}{\textbf{Inputs}} & \multicolumn{3}{c}{\textbf{Outputs}} \\
$D_3$ & $D_2$ & $D_1$ & $D_0$ & $Y_1$ & $Y_0$ & $V$ (Valid) \\
\midrule
0 & 0 & 0 & 0 & X & X & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & X & 0 & 1 & 1 \\
0 & 1 & X & X & 1 & 0 & 1 \\
1 & X & X & X & 1 & 1 & 1 \\
\bottomrule
\end{tabular}
\end{center}

From the truth table, the minimized output equations are:
\begin{align}
    Y_1 &= D_3 + D_2 \\
    Y_0 &= D_3 + \bar{D}_2 D_1 \\
    V &= D_3 + D_2 + D_1 + D_0
\end{align}
\end{derivationbox}

\section{Magnitude Comparators}
A magnitude comparator inspects two $n$-bit binary words $A$ and $B$ and determines their relative magnitude: $A > B$, $A = B$, or $A < B$.
\begin{itemize}
    \item \textbf{1-Bit Comparator:} For inputs $A, B$:
    \begin{align}
        (A = B) &= A \odot B = A B + \bar{A}\bar{B} \\
        (A > B) &= A \bar{B} \\
        (A < B) &= \bar{A} B
    \end{align}
    \item \textbf{4-Bit Magnitude Comparator (7485):} Compares $A_3 A_2 A_1 A_0$ with $B_3 B_2 B_1 B_0$. Equality occurs when all corresponding bits match:
    \begin{equation}
        (A = B) = (A_3 \odot B_3)(A_2 \odot B_2)(A_1 \odot B_1)(A_0 \odot B_0)
    \end{equation}
    Cascading input pins ($I_{A>B}, I_{A=B}, I_{A<B}$) permit connecting multiple 4-bit comparators to form 8-bit, 12-bit, or 16-bit comparators.
\end{itemize}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 4.1: Boolean Function Implementation using 4-to-1 Multiplexer]
\textbf{Problem:} Implement the 3-variable Boolean function $F(A,B,C) = \sum m(1, 2, 6, 7)$ using a single 4-to-1 Multiplexer with $A$ and $B$ connected to select lines $S_1$ and $S_0$.

\textbf{Solution:}
\begin{enumerate}
    \item Assign select lines: $S_1 = A, S_0 = B$. The remaining input variable is $C$.
    \item Construct the MUX implementation table:
    \begin{center}
    \small
    \begin{tabular}{c|cccc}
    \toprule
    \textbf{Input Variable $C$} & $I_0 (AB=00)$ & $I_1 (AB=01)$ & $I_2 (AB=10)$ & $I_3 (AB=11)$ \\
    \midrule
    $C = 0$ & $m_0$ & $m_2$ (1) & $m_4$ & $m_6$ (1) \\
    $C = 1$ & $m_1$ (1) & $m_3$ & $m_5$ & $m_7$ (1) \\
    \midrule
    \textbf{Derived Data Input $I_k$} & $I_0 = C$ & $I_1 = \bar{C}$ & $I_2 = 0$ & $I_3 = 1$ \\
    \bottomrule
    \end{tabular}
    \end{center}
    \item \textbf{Input Vector:} $(I_0, I_1, I_2, I_3) = (C, \bar{C}, 0, 1)$. Connect $C$ to $I_0$, an inverted $\bar{C}$ to $I_1$, logic 0 (GND) to $I_2$, and logic 1 ($V_{CC}$) to $I_3$.
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 4.2: Full Subtractor Design Using 3-to-8 Decoder]
\textbf{Problem:} Design a Full Subtractor (Difference $D$ and Borrow-out $B_{out}$) for inputs $A, B, B_{in}$ using a 3-to-8 Decoder (74138) with active-high outputs and minimal OR gates.

\textbf{Solution:}
\begin{enumerate}
    \item The truth table for Full Subtractor yields minterms:
    \begin{align}
        D(A, B, B_{in}) &= \sum m(1, 2, 4, 7) \\
        B_{out}(A, B, B_{in}) &= \sum m(1, 2, 3, 7)
    \end{align}
    \item Connect inputs $A \to A_2, B \to A_1, B_{in} \to A_0$ on the 3-to-8 decoder.
    \item Connect decoder outputs $Y_1, Y_2, Y_4, Y_7$ to a 4-input OR gate to produce Difference $D$.
    \item Connect decoder outputs $Y_1, Y_2, Y_3, Y_7$ to a 4-input OR gate to produce Borrow $B_{out}$.
\end{enumerate}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Adders:} Full Adder $S = A \oplus B \oplus C_{in}$, $C_{out} = AB + C_{in}(A \oplus B)$.
    \item \textbf{Carry Lookahead:} Eliminates ripple delay by computing carries in parallel using $G_i = A_i B_i$ and $P_i = A_i \oplus B_i$ in constant $O(1)$ time.
    \item \textbf{Adder-Subtractor:} Controlled with XOR gates and mode line $M$; signed overflow detected via $V = C_n \oplus C_{n-1}$.
    \item \textbf{Multiplexers:} Universal logic elements; an $n$-variable Boolean function can be realized using a single $2^{n-1}:1$ MUX.
    \item \textbf{Priority Encoders:} Resolve simultaneous active inputs by selecting the highest-order input line, generating a binary code and Valid flag.
    \item \textbf{Comparators:} Evaluate $A > B$, $A = B$, $A < B$; expandable across multiple stages using cascade inputs.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-04-combinational-logic.tex", "w") as f:
    f.write(ch4)

print("Chapter 4 generated.")

# ==============================================================================
# CHAPTER 5
# ==============================================================================
ch5 = r"""\chapter{Sequential Logic Circuits: Flip-Flops, Registers, and Counters}
\label{chap:sequential_logic}

\section{Introduction and Characteristics of Sequential Logic}
Unlike combinational logic, sequential logic circuits possess internal memory elements. The output of a sequential circuit at any given instant is a function of both its current inputs and its past history (\textbf{present state}). In this chapter, we develop the theory of bistable latches, clocked flip-flops, Master-Slave race-around resolution, flip-flop conversion algorithms, multi-mode shift registers, and ripple/synchronous counters.

\section{Latches vs. Flip-Flops: Bistable Storage Elements}
\subsection{SR Latch Implementations}
\begin{enumerate}
    \item \textbf{NOR-Based SR Latch:} Uses two cross-coupled NOR gates:
    \begin{align}
        Q &= \overline{R + \bar{Q}} \\
        \bar{Q} &= \overline{S + Q}
    \end{align}
    \begin{itemize}
        \item $S = 0, R = 0$: Memory State ($Q_{n+1} = Q_n$).
        \item $S = 1, R = 0$: Set State ($Q_{n+1} = 1$).
        \item $S = 0, R = 1$: Reset State ($Q_{n+1} = 0$).
        \item $S = 1, R = 1$: \textbf{Prohibited / Invalid State} (forces $Q = \bar{Q} = 0$; if inputs return to 00 simultaneously, circuit enters an unpredictable race condition).
    \end{itemize}
    \item \textbf{NAND-Based $\bar{S}\bar{R}$ Latch:} Uses cross-coupled NAND gates with active-low inputs ($\bar{S}, \bar{R}$):
    \begin{itemize}
        \item $\bar{S}=1, \bar{R}=1$: Memory State.
        \item $\bar{S}=0, \bar{R}=1$: Set State ($Q = 1$).
        \item $\bar{S}=1, \bar{R}=0$: Reset State ($Q = 0$).
        \item $\bar{S}=0, \bar{R}=0$: \textbf{Prohibited State} (forces $Q = \bar{Q} = 1$).
    \end{itemize}
\end{enumerate}

\subsection{Level-Triggered Latches vs. Edge-Triggered Flip-Flops}
\begin{itemize}
    \item \textbf{Latch (Level-Sensitive):} Changes state continuously whenever the enable (clock) input is at logic HIGH (transparent mode). Vulnerable to unwanted glitches during the clock pulse.
    \item \textbf{Flip-Flop (Edge-Triggered):} Changes state \textbf{only at discrete transitions} (either rising positive edge $\uparrow$ or falling negative edge $\downarrow$) of the clock pulse.
\end{itemize}

\section{Flip-Flop Types, Characteristic Equations, and Excitation Tables}
\subsection{Core Flip-Flop Families}
\begin{table}[htbp]
\centering
\small
\caption{Comprehensive Comparison of Flip-Flop Types}
\label{tab:flip_flops}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Flip-Flop Type} & \textbf{Inputs} & \textbf{Characteristic Equation} & \textbf{Key Functional Feature} \\
\midrule
\textbf{SR Flip-Flop} & $S, R, \text{CLK}$ & $Q_{n+1} = S + \bar{R}Q_n \quad (SR=0)$ & Set/Reset memory; invalid when $S=R=1$. \\
\textbf{D Flip-Flop} & $D, \text{CLK}$ & $Q_{n+1} = D$ & Data/Delay buffer; eliminates invalid state. \\
\textbf{JK Flip-Flop} & $J, K, \text{CLK}$ & $Q_{n+1} = J\bar{Q}_n + \bar{K}Q_n$ & Universal flip-flop; toggles when $J=K=1$. \\
\textbf{T Flip-Flop} & $T, \text{CLK}$ & $Q_{n+1} = T \oplus Q_n$ & Toggle flip-flop; divides frequency by 2. \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Excitation Tables for Sequential Circuit Synthesis}
The excitation table dictates the required input conditions to achieve a desired state transition from present state $Q_n$ to next state $Q_{n+1}$.

\begin{table}[htbp]
\centering
\small
\caption{Excitation Tables for All Primary Flip-Flops}
\label{tab:excitation_tables}
\begin{tabularx}{0.8\textwidth}{cc|cccc}
\toprule
\textbf{Present State} & \textbf{Next State} & \multicolumn{4}{c}{\textbf{Required Flip-Flop Inputs}} \\
$Q_n$ & $Q_{n+1}$ & $S \quad R$ & $D$ & $J \quad K$ & $T$ \\
\midrule
0 & 0 & $0 \quad \text{X}$ & 0 & $0 \quad \text{X}$ & 0 \\
0 & 1 & $1 \quad 0$ & 1 & $1 \quad \text{X}$ & 1 \\
1 & 0 & $0 \quad 1$ & 0 & $\text{X} \quad 1$ & 1 \\
1 & 1 & $\text{X} \quad 0$ & 1 & $\text{X} \quad 0$ & 0 \\
\bottomrule
\end{tabularx}
\end{table}

\section{The Race-Around Condition and Master-Slave Architecture}
\subsection{Origin of the Race-Around Condition}
In a level-triggered JK flip-flop, when $J = 1$ and $K = 1$:
\begin{itemize}
    \item The output is instructed to toggle: $Q_{n+1} = \bar{Q}_n$.
    \item If the clock pulse width $t_p$ is greater than the internal propagation delay $t_{pd(FF)}$ of the flip-flop ($t_p > t_{pd(FF)}$), the newly toggled output feeds back to the input gates while the clock is still HIGH.
    \item This causes the output to toggle repeatedly ($0 \to 1 \to 0 \to 1 \dots$) within a single clock pulse, leaving the final output unpredictable at the clock's falling edge. This instability is the \textbf{Race-Around Condition}.
\end{itemize}

\subsection{Master-Slave JK Flip-Flop Resolution}
The Master-Slave JK flip-flop eliminates race-around by cascading two separate latches controlled by complementary clock phases:
\begin{enumerate}
    \item \textbf{Master Latch (Active on $\text{CLK} = 1$):} Receives external $J, K$ inputs and updates its intermediate state ($Q_M, \bar{Q}_M$), while the Slave latch is disabled by an inverter ($\overline{\text{CLK}} = 0$).
    \item \textbf{Slave Latch (Active on $\text{CLK} = 0$):} When the clock transitions to LOW, the Master is isolated from external inputs, and the Slave transfers the stored Master state ($Q_M$) to the final outputs ($Q, \bar{Q}$).
    \item Because the output $Q$ never feeds back to the active input during the same clock phase, race-around is completely prevented.
\end{enumerate}

\section{Shift Registers}
A shift register is a cascaded sequence of flip-flops sharing a common clock, designed for temporary data storage and serial/parallel format conversions.
\begin{enumerate}
    \item \textbf{Serial-In Serial-Out (SISO):} Requires $n$ clock pulses to load an $n$-bit word and $n$ clock pulses to retrieve it.
    \item \textbf{Serial-In Parallel-Out (SIPO):} Requires $n$ clock pulses to load data serially, but all $n$ bits are read simultaneously in 1 clock pulse.
    \item \textbf{Parallel-In Serial-Out (PISO):} Loads all $n$ bits in 1 clock pulse using parallel load gates, then shifts out serially in $(n-1)$ clock pulses.
    \item \textbf{Parallel-In Parallel-Out (PIPO):} Loads and retrieves data in 1 clock pulse (pure parallel register).
    \item \textbf{4-Bit Universal Shift Register (74194):} Controlled by two mode select lines ($S_1, S_0$):
    \begin{itemize}
        \item $S_1 S_0 = 00$: Hold (No change).
        \item $S_1 S_0 = 01$: Shift Right (Serial input $D_{SR}$).
        \item $S_1 S_0 = 10$: Shift Left (Serial input $D_{SL}$).
        \item $S_1 S_0 = 11$: Parallel Load ($D_3 D_2 D_1 D_0$).
    \end{itemize}
    \item \textbf{Ring Counter:} An $n$-bit shift register with serial output connected back to serial input. An initial single '1' circulates through $n$ distinct states.
    \item \textbf{Johnson (Twisted-Ring) Counter:} Inverted output $\bar{Q}_n$ is fed back to the input. An $n$-bit register produces $2n$ distinct decoded states without extra logic.
\end{enumerate}

\section{Asynchronous and Synchronous Counters}
\subsection{Asynchronous (Ripple) Counters and Maximum Operating Frequency}
In an Asynchronous (Ripple) counter, the external clock pulse is applied only to the LSB flip-flop; each subsequent stage is clocked by the output of the preceding stage.

\begin{derivationbox}[Derivation of Maximum Clock Frequency in an $n$-Bit Ripple Counter]
Consider an $n$-bit ripple counter composed of flip-flops each with propagation delay $t_{pd}$.
The total time required for a transition to ripple from the LSB to the MSB is:
\begin{equation}
    T_{\text{ripple}} = n \cdot t_{pd}
\end{equation}
To ensure that all outputs stabilize and satisfy downstream setup time $t_s$ before the next clock pulse arrives:
\begin{equation}
    T_{\text{clk, min}} \ge n \cdot t_{pd} + t_s
\end{equation}
Thus, the \textbf{maximum operating clock frequency} $f_{\text{max}}$ is:
\begin{equation}
    f_{\text{max}} = \frac{1}{T_{\text{clk, min}}} = \frac{1}{n \cdot t_{pd} + t_s}
\end{equation}
\end{derivationbox}

\subsection{Synchronous Counters and Mod-N Design}
In a Synchronous Counter, the common clock is connected directly to the clock inputs of all flip-flops simultaneously, eliminating accumulated ripple delays.
\begin{itemize}
    \item \textbf{Design Procedure:}
    \begin{enumerate}
        \item Determine the number of flip-flops: $2^{n-1} < N \le 2^n$ (for Mod-$N$).
        \item Write the state transition table ($Q_n \to Q_{n+1}$).
        \item Extract required flip-flop inputs using the Excitation Table.
        \item Minimize input Boolean expressions using K-maps.
        \item Implement the logic circuit and verify self-correction from unused states.
    \end{enumerate}
\end{itemize}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 5.1: Conversion of JK Flip-Flop to D Flip-Flop]
\textbf{Problem:} Convert a standard JK Flip-Flop into a D Flip-Flop. Provide the complete conversion table, K-maps, and final logic gate implementation.

\textbf{Solution:}
\begin{enumerate}
    \item \textbf{Conversion Table:}
    \begin{center}
    \small
    \begin{tabular}{cc|c|cc}
    \toprule
    \textbf{Target Input $D$} & \textbf{Present State $Q_n$} & \textbf{Next State $Q_{n+1}$} & \multicolumn{2}{c}{\textbf{Required JK Inputs}} \\
    $D$ & $Q_n$ & $Q_{n+1}$ & $J$ & $K$ \\
    \midrule
    0 & 0 & 0 & 0 & X \\
    0 & 1 & 0 & X & 1 \\
    1 & 0 & 1 & 1 & X \\
    1 & 1 & 1 & X & 0 \\
    \bottomrule
    \end{tabular}
    \end{center}
    \item \textbf{K-Map Minimization:}
    \begin{itemize}
        \item For $J(D, Q_n)$: Cell $(0,0)=0, (0,1)=X, (1,0)=1, (1,1)=X \implies \mathbf{J = D}$.
        \item For $K(D, Q_n)$: Cell $(0,0)=X, (0,1)=1, (1,0)=X, (1,1)=0 \implies \mathbf{K = \bar{D}}$.
    \end{itemize}
    \item \textbf{Implementation:} Connect input $D$ directly to the $J$ terminal, and connect an inverted $\bar{D}$ (via a NOT gate) to the $K$ terminal.
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 5.2: Maximum Clock Frequency of a 4-Bit Ripple Counter]
\textbf{Problem:} A 4-bit asynchronous binary ripple counter is constructed using four negative-edge triggered JK flip-flops. Each flip-flop has a propagation delay $t_{pd} = 15\,\text{ns}$ and setup time $t_s = 5\,\text{ns}$.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the maximum operating clock frequency $f_{\text{max}}$.
    \item If the counter is operated with an input clock of $10\,\text{MHz}$, what is the output frequency at the MSB stage ($Q_3$)?
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Maximum Operating Clock Frequency:}
    \begin{align}
        T_{\text{clk, min}} &= n \cdot t_{pd} + t_s = (4)(15\,\text{ns}) + 5\,\text{ns} = 60\,\text{ns} + 5\,\text{ns} = 65\,\text{ns} \\
        f_{\text{max}} &= \frac{1}{T_{\text{clk, min}}} = \frac{1}{65 \times 10^{-9}\,\text{s}} = \mathbf{15.38\,\text{MHz}}
    \end{align}
    \item \textbf{MSB Output Frequency:}
    A 4-bit binary counter divides the input clock frequency by $2^4 = 16$:
    \begin{equation}
        f_{Q3} = \frac{f_{\text{in}}}{2^4} = \frac{10\,\text{MHz}}{16} = \mathbf{625\,\text{kHz}}
    \end{equation}
\end{enumerate}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Latches vs Flip-Flops:} Latches are level-sensitive; Flip-flops are edge-triggered.
    \item \textbf{Race-Around Condition:} Occurs in level-triggered JK flip-flops when $J=K=1$ and $t_p > t_{pd(FF)}$; solved by Master-Slave two-phase clocking.
    \item \textbf{Excitation Tables:} Direct tool for synthesizing sequential state machines ($Q_n \to Q_{n+1}$).
    \item \textbf{Universal Shift Register (74194):} Supports Hold, Shift-Right, Shift-Left, and Parallel Load via mode control lines $S_1 S_0$.
    \item \textbf{Ripple Counter Speed:} Limited by cumulative delay: $f_{\text{max}} = \frac{1}{n \cdot t_{pd} + t_s}$.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-05-sequential-logic.tex", "w") as f:
    f.write(ch5)

print("Chapter 5 generated.")

# ==============================================================================
# CHAPTER 6
# ==============================================================================
ch6 = r"""\chapter{Introduction to Arduino Microcontrollers and Sensor Interfacing}
\label{chap:arduino_sensors}

\section{Introduction and Embedded Systems Architecture}
Modern engineering applications—from autonomous robotics and Internet-of-Things (IoT) smart cities to industrial automation—require bridging the analog physical world with digital computational controllers. In this chapter, we explore the physical architecture of microcontroller systems (specifically the Arduino Uno R3 / ATmega328P platform), analog-to-digital quantization, Pulse Width Modulation (PWM), and the operational physics, circuit interfacing, and firmware implementation of reflective optical, LDR, ultrasonic, and environmental sensors.

\section{Analog vs. Digital Signals and Arduino Uno Hardware Architecture}
\subsection{Analog vs. Digital Domain Representations}
\begin{itemize}
    \item \textbf{Analog Signals:} Continuous physical variables (temperature, light intensity, sound pressure, acoustic echo delay) that vary smoothly over time and can take any value within a continuous voltage spectrum (e.g., $0.0\,\text{V}$ to $5.0\,\text{V}$).
    \item \textbf{Digital Signals:} Discrete, quantized representations restricted to binary logic levels ($\text{LOW} = 0\,\text{V}$, $\text{HIGH} = 5.0\,\text{V}$), offering superior noise immunity and error-free digital processing.
\end{itemize}

\subsection{Arduino Uno R3 (ATmega328P) Hardware Specifications}
\begin{table}[htbp]
\centering
\small
\caption{Arduino Uno R3 Microcontroller Specifications}
\label{tab:arduino_specs}
\begin{tabularx}{\textwidth}{lXX}
\toprule
\textbf{Hardware Component} & \textbf{Specification / Value} & \textbf{Engineering Function} \\
\midrule
\textbf{Microcontroller Core} & ATmega328P (8-bit AVR RISC) & Executes instructions at 16 MIPS. \\
\textbf{Operating Voltage} & $5.0\,\text{V}$ (Nominal) & Standard TTL logic level. \\
\textbf{Input Supply Voltage} & $7.0\,\text{V} - 12.0\,\text{V}$ (via VIN / DC Jack) & Regulated down to $5\,\text{V}$ on-board. \\
\textbf{Clock Frequency} & $16.0\,\text{MHz}$ Quartz Crystal & Provides master system timing ($62.5\,\text{ns}$ cycle). \\
\textbf{Flash Memory} & $32\,\text{KB}$ ($0.5\,\text{KB}$ used by Bootloader) & Non-volatile storage for compiled program code. \\
\textbf{SRAM} & $2.0\,\text{KB}$ & Volatile working memory for active variables. \\
\textbf{EEPROM} & $1.0\,\text{KB}$ & Non-volatile byte-addressable parameter storage. \\
\textbf{Digital I/O Pins} & 14 pins (Pins 0 to 13) & Reconfigurable as digital inputs or outputs. \\
\textbf{Hardware PWM Pins} & 6 pins (Pins 3, 5, 6, 9, 10, 11) & Hardware timer-driven PWM outputs. \\
\textbf{Analog Input Pins} & 6 channels (Pins A0 to A5) & Multiplexed into 10-bit Successive Approximation ADC. \\
\textbf{DC Current per I/O Pin} & $20\,\text{mA}$ (Recommended), $40\,\text{mA}$ (Absolute Max) & Direct drive limit for LEDs and transistors. \\
\bottomrule
\end{tabularx}
\end{table}

\section{Analog-to-Digital Conversion (ADC) and Pulse Width Modulation (PWM)}
\subsection{10-Bit Successive Approximation ADC}
The ATmega328P features an on-chip 10-bit Successive Approximation Register (SAR) ADC.

\begin{derivationbox}[ADC Quantization, Step Resolution, and Voltage Mapping]
A 10-bit ADC quantizes an analog input voltage $V_{\text{in}}$ into $2^{10} = 1024$ discrete integer digital levels ($0$ to $1023$).
For a reference voltage $V_{\text{ref}} = 5.0\,\text{V}$:
\begin{itemize}
    \item \textbf{Quantization Step Resolution ($\Delta V$):}
    \begin{equation}
        \Delta V = \frac{V_{\text{ref}}}{2^n - 1} = \frac{5.0\,\text{V}}{1023} \approx 4.8876\,\text{mV/step}
    \end{equation}
    \item \textbf{Digital Output Calculation:}
    \begin{equation}
        \text{ADC Value} = \text{round}\left(\frac{V_{\text{in}}}{V_{\text{ref}}} \times 1023\right)
    \end{equation}
    \item \textbf{Analog Voltage Reconstruction:} In Arduino firmware:
    \begin{equation}
        V_{\text{in}} = \text{ADC Value} \times \left(\frac{5.0}{1023.0}\right)
    \end{equation}
\end{itemize}
\end{derivationbox}

\subsection{Pulse Width Modulation (PWM)}
Pulse Width Modulation generates an analog-like average voltage by rapidly switching a digital output pin between HIGH ($5\,\text{V}$) and LOW ($0\,\text{V}$) at a fixed frequency ($490\,\text{Hz}$ or $980\,\text{Hz}$).

\begin{derivationbox}[PWM Duty Cycle and Average Output Voltage]
For a square wave of period $T$ and ON-time $t_{\text{on}}$:
\begin{itemize}
    \item \textbf{Duty Cycle ($D$):}
    \begin{equation}
        D = \frac{t_{\text{on}}}{T} \times 100\%
    \end{equation}
    \item \textbf{Average DC Voltage ($V_{\text{avg}}$):}
    \begin{equation}
        V_{\text{avg}} = \frac{1}{T}\int_0^T v(t)\, dt = \frac{V_{CC} \cdot t_{\text{on}}}{T} = D \times V_{CC}
    \end{equation}
    \item \textbf{Arduino 8-Bit PWM Mapping:} `analogWrite(pin, value)` maps an 8-bit integer parameter ($0$ to $255$):
    \begin{equation}
        D = \frac{\text{value}}{255}, \quad V_{\text{avg}} = \left(\frac{\text{value}}{255.0}\right) \times 5.0\,\text{V}
    \end{equation}
\end{itemize}
\end{derivationbox}

\section{Optical and Environmental Sensors: Physics and Interfacing}
\subsection{Reflective Optical Infrared (IR) Sensor}
\begin{itemize}
    \item \textbf{Operating Physics:} Consists of an Infrared Emitting Diode (emitting at $\lambda \approx 940\,\text{nm}$) and an NPN phototransistor/photodiode receiver.
    \item \textbf{Reflectance Differentiation:} Highly reflective surfaces (white line) reflect IR photons back to the photodiode, driving it into conduction (LOW output). Non-reflective surfaces (black line) absorb IR, keeping the photodiode in cutoff (HIGH output).
    \item \textbf{On-Board LM393 Comparator:} Compares the photodiode analog voltage against a reference set by a multi-turn potentiometer, outputting a clean digital logic level on pin `OUT`.
\end{itemize}

\subsection{Light Dependent Resistor (LDR) and Software Hysteresis}
An LDR (Cadmium Sulfide, CdS) is a photoresistor whose resistance decreases exponentially with increasing incident light intensity (photoconductivity):
\begin{equation}
    R_{\text{LDR}} \approx R_0 \left(\frac{L_0}{L}\right)^\gamma
\end{equation}
\begin{itemize}
    \item \textbf{Voltage Divider Interface:} Connected in series with a fixed $R_{\text{fixed}} = 10\,\text{k}\Omega$ pull-down resistor across $5.0\,\text{V}$:
    \begin{equation}
        V_{\text{out}} = 5.0\,\text{V} \times \left(\frac{R_{\text{fixed}}}{R_{\text{LDR}} + R_{\text{fixed}}}\right)
    \end{equation}
    In darkness ($R_{\text{LDR}} \sim 1\,\text{M}\Omega$), $V_{\text{out}} \approx 0.05\,\text{V}$ ($\text{ADC} \approx 10$). In bright light ($R_{\text{LDR}} \sim 1\,\text{k}\Omega$), $V_{\text{out}} \approx 4.54\,\text{V}$ ($\text{ADC} \approx 930$).
    \item \textbf{Software Hysteresis:} In automated lighting systems, ambient light fluctuates slowly around a single threshold at twilight. Hysteresis establishes two separate switching thresholds:
    \begin{equation}
        \text{Turn ON Light when } \text{ADC} < 300; \quad \text{Turn OFF Light when } \text{ADC} > 450
    \end{equation}
    The deadband ($\Delta = 150$ counts) prevents rapid relay chatter and flickering.
\end{itemize}

\subsection{HC-SR04 Ultrasonic Distance Sensor}
\begin{derivationbox}[Ultrasonic Time-of-Flight Derivation]
The HC-SR04 sensor operates by emitting high-frequency acoustic waves and timing the reflected echo:
\begin{enumerate}
    \item Microcontroller issues a $10\,\mu\text{s}$ HIGH pulse on the \texttt{TRIG} pin.
    \item Transmitter emits an 8-cycle burst of ultrasound at $40\,\text{kHz}$.
    \item The \texttt{ECHO} pin goes HIGH and stays HIGH until the reflected sound wave strikes the receiver transducer.
    \item The HIGH duration of the Echo pulse represents the total round-trip transit time $t$.
\end{enumerate}
Speed of sound in dry air at $20^\circ\text{C}$ is $v = 340\,\text{m/s} = 0.034\,\text{cm}/\mu\text{s}$.
The total distance travelled is $2d = v \cdot t$:
\begin{equation}
    d = \frac{v \cdot t}{2} = \frac{0.034\,\text{cm}/\mu\text{s} \times t}{2} = \frac{t}{58.82}\,\text{cm}
\end{equation}
\end{derivationbox}

\subsection{DHT11 vs. DHT22 Digital Temperature and Humidity Sensors}
\begin{table}[htbp]
\centering
\small
\caption{Comparison Between DHT11 and DHT22 Environmental Sensors}
\label{tab:dht_comparison}
\begin{tabularx}{\textwidth}{lXX}
\toprule
\textbf{Specification} & \textbf{DHT11 (Basic Sensor)} & \textbf{DHT22 / AM2302 (Precision Sensor)} \\
\midrule
\textbf{Temperature Range} & $0^\circ\text{C}$ to $50^\circ\text{C}$ & $-40^\circ\text{C}$ to $+80^\circ\text{C}$ \\
\textbf{Temperature Accuracy} & $\pm 2.0^\circ\text{C}$ & $\pm 0.5^\circ\text{C}$ \\
\textbf{Temperature Resolution} & $1^\circ\text{C}$ (8-bit integer) & $0.1^\circ\text{C}$ (16-bit float) \\
\textbf{Humidity Range} & $20\%$ to $90\%\,\text{RH}$ & $0\%$ to $100\%\,\text{RH}$ \\
\textbf{Humidity Accuracy} & $\pm 5\%\,\text{RH}$ & $\pm 2\%\,\text{RH}$ \\
\textbf{Sampling Period} & $1.0\,\text{s}$ ($1\,\text{Hz}$ max) & $2.0\,\text{s}$ ($0.5\,\text{Hz}$ max) \\
\textbf{Communication Protocol} & Single-wire bidirectional custom bus & Single-wire bidirectional custom bus \\
\textbf{External Pull-Up} & $4.7\,\text{k}\Omega - 10\,\text{k}\Omega$ to $5\,\text{V}$ & $4.7\,\text{k}\Omega - 10\,\text{k}\Omega$ to $5\,\text{V}$ \\
\bottomrule
\end{tabularx}
\end{table}

\section{Practical Arduino C++ Firmware Implementations}

\begin{lstlisting}[language=C++, caption={Complete Obstacle Avoidance and Distance Ranging Firmware}]
// Hardware Pin Declarations
const int trigPin = 9;
const int echoPin = 10;
const int ldrPin = A0;
const int alertLED = 13;
const int pwmMotorPin = 6;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(alertLED, OUTPUT);
  pinMode(pwmMotorPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // 1. Trigger Ultrasonic Sensor Burst
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // 2. Measure Echo Pulse Width in Microseconds
  long duration = pulseIn(echoPin, HIGH, 30000); // 30ms timeout
  float distanceCm = (duration * 0.034) / 2.0;

  // 3. Read Analog LDR Value
  int ldrVal = analogRead(ldrPin);

  // 4. Decision Logic with Hysteresis
  if (distanceCm > 0 && distanceCm < 20.0) {
    digitalWrite(alertLED, HIGH);
    analogWrite(pwmMotorPin, 0); // Stop motor
    Serial.println("ALERT: Obstacle Detected!");
  } else {
    digitalWrite(alertLED, LOW);
    analogWrite(pwmMotorPin, 180); // Cruise speed
  }

  delay(100);
}
\end{lstlisting}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 6.1: Precision ADC Quantization Error and Voltage Mapping]
\textbf{Problem:} An Arduino Uno operates with $V_{\text{ref}} = 5.00\,\text{V}$.
\begin{enumerate}[label=(\alph*)]
    \item What digital ADC integer value is returned for an analog input of $V_{\text{in}} = 3.30\,\text{V}$?
    \item If the ADC reads a raw value of $614$, what is the calculated input voltage and maximum possible quantization uncertainty?
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item Digital ADC output:
    \begin{equation}
        \text{ADC Value} = \text{round}\left(\frac{3.30\,\text{V}}{5.00\,\text{V}} \times 1023\right) = \text{round}(675.18) = \mathbf{675}
    \end{equation}
    \item Reconstructed voltage:
    \begin{equation}
        V_{\text{in}} = 614 \times \left(\frac{5.00\,\text{V}}{1023}\right) = \mathbf{3.001\,\text{V}}
    \end{equation}
    The step resolution is $\Delta V = \frac{5.00\,\text{V}}{1023} = 4.888\,\text{mV}$. The maximum quantization uncertainty is $\pm \frac{1}{2}\Delta V = \pm \mathbf{2.444\,\text{mV}}$.
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 6.2: Ultrasonic Ranging Echo Pulse Timing]
\textbf{Problem:} An HC-SR04 ultrasonic sensor placed on an autonomous vehicle measures an echo pulse duration of $t = 1176\,\mu\text{s}$. If ambient temperature is $20^\circ\text{C}$ ($v = 340\,\text{m/s}$), calculate the obstacle distance in centimeters.

\textbf{Solution:}
\begin{equation}
    d = \frac{v \cdot t}{2} = \frac{0.034\,\text{cm}/\mu\text{s} \times 1176\,\mu\text{s}}{2} = \frac{39.984\,\text{cm}}{2} = \mathbf{19.99\,\text{cm}} \approx \mathbf{20.0\,\text{cm}}
\end{equation}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Arduino Uno (ATmega328P):} 16 MHz clock, 32 KB Flash, 2 KB SRAM, 14 digital I/O pins, 6 analog inputs.
    \item \textbf{10-Bit ADC:} 1024 quantization steps; resolution $\Delta V = \frac{5.0\,\text{V}}{1023} \approx 4.89\,\text{mV}$.
    \item \textbf{PWM Output:} `analogWrite(pin, val)` outputs average voltage $V_{\text{avg}} = \frac{\text{val}}{255} \times 5\,\text{V}$.
    \item \textbf{LDR & Hysteresis:} Voltage divider translates resistance variation into analog voltage; dual thresholds eliminate relay chatter.
    \item \textbf{Ultrasonic HC-SR04:} Emits $40\,\text{kHz}$ burst; distance $d = \frac{t}{58.82}\,\text{cm}$.
    \item \textbf{DHT11 vs DHT22:} DHT22 provides wider range ($-40$ to $80^\circ\text{C}$) and higher precision ($\pm 0.5^\circ\text{C}$) over single-wire digital bus.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-06-arduino-and-sensors.tex", "w") as f:
    f.write(ch6)

print("Chapter 6 generated.")
