import os

os.makedirs("PHY175/chapters", exist_ok=True)

# ==============================================================================
# CHAPTER 5: SEQUENTIAL LOGIC CIRCUITS
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
Thus, the **maximum operating clock frequency** $f_{\text{max}}$ is:
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
    \begin{table}[htbp]
    \centering
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
    \end{table}
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

print("Chapter 5 successfully written.")

# ==============================================================================
# CHAPTER 6: INTRODUCTION OF ARDUINO AND SENSORS
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

print("Chapter 6 successfully written.")

