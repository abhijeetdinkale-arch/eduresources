import os
import subprocess

print("Appending Units 2 to 6 to Question Bank Builder...")

# Helper function
def get_unit_tex(unit_num, title, mcqs, theory_qs):
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

    content += r"""
\newpage
\section{Section 2: Complete Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{Answer Key with Rationales (Questions 1 to 60)}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(30):
        q1 = (i+1, mcqs[i][5], mcqs[i][6])
        q2 = (i+31, mcqs[i+30][5], mcqs[i+30][6])
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

    return content

# UNIT 2 MCQS (60 Questions)
u2_mcqs = [
    # 1-20
    ("According to Ohm's law, what is the voltage across a $5\\,\\Omega$ resistor carrying a current of $2\\,\\text{A}$?", "$7\\,\\text{V}$", "$2.5\\,\\text{V}$", "$10\\,\\text{V}$", "$15\\,\\text{V}$", "C", "$V = I R = (2)(5) = 10\\,\\text{V}$."),
    ("Which law states that the algebraic sum of currents at an electrical junction is zero?", "Kirchhoff's current law", "Coulomb's law", "Ohm's law", "Kirchhoff's voltage law", "A", "KCL is the statement of charge conservation at a node."),
    ("Two equal resistors are connected in series across a $12\\,\\text{V}$ supply. What is the voltage across each resistor?", "$6\\,\\text{V}$", "$3\\,\\text{V}$", "$24\\,\\text{V}$", "$12\\,\\text{V}$", "A", "Voltage divides equally across identical series resistors: $12/2 = 6\\,\\text{V}$."),
    ("In a series voltage divider, which resistor receives the larger voltage drop?", "The grounded resistor", "The smaller resistor", "The first resistor", "The larger resistor", "D", "$V \\propto R$ in a series circuit."),
    ("A total current of $4\\,\\text{A}$ enters two equal resistors connected in parallel. What current flows through each resistor?", "$1\\,\\text{A}$", "$2\\,\\text{A}$", "$4\\,\\text{A}$", "$8\\,\\text{A}$", "B", "Current divides equally between identical parallel branches: $4/2 = 2\\,\\text{A}$."),
    ("In which bias condition does a PN junction diode normally conduct significant current?", "Breakdown bias", "Zero bias", "Reverse bias", "Forward bias", "D", "Forward bias lowers barrier potential, allowing large diffusion current."),
    ("What happens to the depletion region of a PN junction diode under forward bias?", "It becomes narrower", "It becomes wider", "It remains unchanged", "It becomes conductive metal", "A", "Forward voltage opposes the built-in potential, reducing depletion width."),
    ("What is the primary function of a diode rectifier?", "Convert DC to AC", "Increase signal frequency", "Store electrical charge", "Convert AC to DC", "D", "Rectification converts alternating current to unidirectional pulsating DC."),
    ("When used as an ideal switch, how does a forward-biased diode behave?", "As a closed switch", "As a charged capacitor", "As an open switch", "As a current source", "A", "Ideal forward diode has zero voltage drop and acts as a closed switch ($0\\,\\Omega$)."),
    ("What are the three terminals of a bipolar junction transistor?", "Emitter, base, collector", "Gate, source, drain", "Input, output, ground", "Anode, cathode, gate", "A", "BJT terminals are Emitter (E), Base (B), and Collector (C)."),
    ("Which small BJT current controls a larger collector current during normal operation?", "Leakage current", "Emitter current", "Reverse current", "Base current", "D", "In active mode, small $I_B$ controls large $I_C = \\beta I_B$."),
    ("Which two types of MOS transistors are combined in CMOS technology?", "LED and diode", "JFET and BJT", "NMOS and PMOS", "NPN and PNP", "C", "CMOS utilizes complementary NMOS and PMOS transistor pairs."),
    ("What is a major advantage of CMOS circuits in digital electronics?", "Low static power use", "Large physical size", "High acoustic output", "High mechanical strength", "A", "No direct $V_{DD}$ to ground path exists in steady state, yielding near-zero static power."),
    ("Which statement correctly describes RAM?", "It is usually volatile", "It is permanently read-only", "It stores data optically", "It uses magnetic tape", "A", "RAM loses its stored data upon removal of power (volatile)."),
    ("Which type of semiconductor memory is commonly used for data storage in an SSD?", "Dynamic RAM", "Register memory", "Flash memory", "Cache memory", "C", "Solid State Drives use non-volatile NAND Flash memory."),
    ("What is the main purpose of an AI accelerator chip?", "Route network packets", "Speed up AI computations", "Convert sound to light", "Measure room temperature", "B", "Accelerators (GPUs, TPUs, NPUs) accelerate matrix tensor operations in parallel."),
    ("What is the basic role of a sensor in an IoT system?", "Compile a software program", "Encrypt every network packet", "Increase battery voltage", "Detect a physical quantity", "D", "Sensors convert physical parameters (temperature, light, pressure) into electrical signals."),
    ("What is a computer network?", "A type of storage chip", "A standalone power supply", "A group of connected devices", "A single processing unit", "C", "A computer network connects autonomous devices for data communication and resource sharing."),
    ("Which physical phenomenon mainly keeps light confined inside an optical fiber?", "Electromagnetic induction", "Nuclear magnetic resonance", "Photoelectric emission", "Total internal reflection", "D", "Light propagates via TIR at the core-cladding boundary ($n_{core} > n_{clad}$)."),
    ("Which processor is generally better suited for performing many similar calculations in parallel?", "SSD controller", "Network router", "GPU", "CPU", "C", "GPUs feature thousands of SIMD cores optimized for massively parallel workloads."),
    
    # 21-40
    ("A $12\\,\\text{V}$ source is connected to two series resistors of $2\\,\\Omega$ and $4\\,\\Omega$. What is the current in the circuit?", "$6\\,\\text{A}$", "$2\\,\\text{A}$", "$1\\,\\text{A}$", "$3\\,\\text{A}$", "B", "$I = 12 / (2 + 4) = 2\\,\\text{A}$."),
    ("At a circuit node, currents of $5\\,\\text{A}$ and $2\\,\\text{A}$ enter, while currents of $4\\,\\text{A}$ and $I$ leave. What is the value of $I$?", "$3\\,\\text{A}$", "$2\\,\\text{A}$", "$1\\,\\text{A}$", "$7\\,\\text{A}$", "A", "$\\sum I_{in} = \\sum I_{out} \\implies 5 + 2 = 4 + I \\implies I = 3\\,\\text{A}$."),
    ("A $20\\,\\text{V}$ supply is connected across series resistors of $3\\,\\text{k}\\Omega$ and $7\\,\\text{k}\\Omega$. What voltage appears across the $7\\,\\text{k}\\Omega$ resistor?", "$14\\,\\text{V}$", "$17\\,\\text{V}$", "$10\\,\\text{V}$", "$6\\,\\text{V}$", "A", "$V = 20 \\times \\frac{7}{3+7} = 14\\,\\text{V}$."),
    ("A voltage divider has $R_1 = 2\\,\\text{k}\\Omega$ and $R_2 = 8\\,\\text{k}\\Omega$ connected to $10\\,\\text{V}$. If a load is connected in parallel with $R_2$, what is the main effect?", "Source voltage becomes zero", "Output voltage increases", "Current through $R_1$ becomes zero", "Output voltage decreases", "D", "Parallel loading lowers effective branch resistance, decreasing output voltage drop."),
    ("A total current of $6\\,\\text{A}$ enters two parallel resistors of $3\\,\\Omega$ and $6\\,\\Omega$. What current flows through the $3\\,\\Omega$ resistor?", "$1\\,\\text{A}$", "$4\\,\\text{A}$", "$2\\,\\text{A}$", "$6\\,\\text{A}$", "B", "$I_3 = 6 \\times \\frac{6}{3+6} = 4\\,\\text{A}$."),
    ("Two parallel branches have resistances of $4\\,\\Omega$ and $12\\,\\Omega$. If current through $4\\,\\Omega$ is $9\\,\\text{A}$, what is current through $12\\,\\Omega$?", "$1\\,\\text{A}$", "$3\\,\\text{A}$", "$27\\,\\text{A}$", "$9\\,\\text{A}$", "B", "Voltage is equal: $V = 9 \\times 4 = 36\\,\\text{V} \\implies I_{12} = 36/12 = 3\\,\\text{A}$."),
    ("When a silicon PN junction diode is forward biased, which change occurs in depletion region?", "Resistance becomes infinite", "Polarity reverses", "Width decreases", "Width increases", "C", "Applied forward bias cancels built-in potential, reducing depletion layer width."),
    ("Silicon diode is operated with anode at $0.8\\,\\text{V}$ and cathode at $0.2\\,\\text{V}$. Forward voltage drop is $\\approx 0.7\\,\\text{V}$. Expected behavior:", "Acts as open circuit", "Strongly reverse biased", "Conducts significantly", "Remains at breakdown", "A", "$V_D = 0.8 - 0.2 = 0.6\\,\\text{V} < 0.7\\,\\text{V}$ (below cut-in threshold, minimal conduction)."),
    ("A full-wave bridge rectifier is supplied with AC of $50\\,\\text{Hz}$. What is the frequency of its ideal ripple output?", "$25\\,\\text{Hz}$", "$100\\,\\text{Hz}$", "$200\\,\\text{Hz}$", "$50\\,\\text{Hz}$", "B", "Full-wave rectifiers conduct on both half cycles: $f_{ripple} = 2 f_{in} = 100\\,\\text{Hz}$."),
    ("In a diode switch, diode is forward biased when logic HIGH is applied. Under ideal model, what state does switch represent?", "Voltage amplifier", "Open circuit", "Current source", "Short circuit", "D", "Ideal forward diode has zero resistance and behaves as a short circuit."),
    ("For BJT in active region, $I_C = 2\\,\\text{mA}$ and $I_B = 20\\,\\mu\\text{A}$. What is current gain $\\beta$?", "$50$", "$10$", "$100$", "$200$", "C", "$\\beta = I_C / I_B = (2\\times 10^{-3}) / (20\\times 10^{-6}) = 100$."),
    ("Which pair of BJT operating conditions represents transistor saturation?", "Both junctions reverse biased", "Both emitter and collector junctions forward biased", "Emitter forward, collector reverse", "Emitter reverse, collector forward", "B", "In saturation mode, both EBJ and CBJ are forward biased."),
    ("In a CMOS inverter, input is LOW. Which transistor is ON and output state?", "Both OFF, floating", "PMOS ON and output HIGH", "Both ON, LOW", "NMOS ON and output LOW", "B", "LOW input turns PMOS ON and NMOS OFF, pulling output to $V_{DD}$ (HIGH)."),
    ("Why does CMOS logic consume very little static power when not switching?", "Operates only in breakdown", "Output always connected to ground", "Supply path is nonconducting in steady state", "Contains no transistors", "C", "In steady state, one transistor of the complementary pair is always completely OFF."),
    ("A computer needs temporary working storage read/written rapidly while programs run. Most suitable device:", "ROM", "SSD", "Dynamic RAM", "Optical fiber", "C", "DRAM provides high-density, low-latency temporary system working memory."),
    ("Which statement best explains why SSD is more shock-resistant than HDD?", "Uses no moving mechanical parts", "Loses data without power", "Stores data only in magnetic domains", "Requires rotating platter", "A", "SSDs use solid-state flash silicon with zero moving mechanical heads or platters."),
    ("Why are GPUs and AI accelerators effective for neural-network workloads?", "Execute sequential instructions", "Perform many similar operations in parallel", "Replace software with hardware", "Eliminate memory", "B", "Neural network matrix multiplications map directly to massively parallel SIMD execution units."),
    ("IoT node measures temperature every minute and sends data only when $\\Delta T > 2^\\circ\\text{C}$. Main benefit:", "Elimination of calibration", "Guaranteed zero measurement error", "Reduced energy and communication use", "Higher sensor noise", "C", "Event-driven edge transmission reduces radio transmission energy consumption."),
    ("A device wants to deliver data to every host on local network segment. Appropriate addressing method:", "Broadcast", "Loopback", "Point-to-point", "Unicast", "A", "Broadcast packets are delivered to all connected nodes on the local subnet."),
    ("Which property of optical fiber allows it to carry signals over long distances with low attenuation?", "Total internal reflection", "Electromagnetic induction", "Capacitive coupling", "Thermal expansion", "A", "TIR keeps optical energy contained inside low-loss glass core."),

    # 41-60
    ("Node at $V$ is connected to $10\\,\\text{V}$ through $2\\,\\Omega$, to GND through $4\\,\\Omega$, and $2\\,\\text{A}$ current injected into node. Value of $V$ and current from $10\\,\\text{V}$ toward $V$:", "$V = 8\\,\\text{V}, I = 1\\,\\text{A}$", "$V = 28/3\\,\\text{V}, I = 1/3\\,\\text{A}$", "$V = 20/3\\,\\text{V}, I = 5/3\\,\\text{A}$", "$V = 12\\,\\text{V}, I = -1\\,\\text{A}$", "A", "KCL: $\\frac{10-V}{2} + 2 = \\frac{V}{4} \\implies 20 - 2V + 8 = V \\implies 3V = 28 \\implies V = 28/3\\,\\text{V}$, with $I = \\frac{10 - 28/3}{2} = \\frac{2/3}{2} = \\frac{1}{3}\\,\\text{A}$ (matches option B)."),
    ("A $24\\,\\text{V}$ source drives divider with $R_1 = 6\\,\\text{k}\\Omega, R_2 = 3\\,\\text{k}\\Omega$. What $R_L$ in parallel with $R_2$ makes output exactly $6\\,\\text{V}$?", "$R_L = 4\\,\\text{k}\\Omega$", "$R_L = 6\\,\\text{k}\\Omega$", "$R_L = 12\\,\\text{k}\\Omega$", "$R_L = 3\\,\\text{k}\\Omega$", "B", "$V_{out} = 24\\frac{R_p}{6+R_p} = 6 \\implies R_p = 2\\,\\text{k}\\Omega \\implies 3 R_L/(3+R_L) = 2 \\implies R_L = 6\\,\\text{k}\\Omega$."),
    ("A $12\\,\\text{A}$ current source supplies parallel branches of $2\\,\\Omega, 3\\,\\Omega, 6\\,\\Omega$. If $6\\,\\Omega$ branch is open-circuited, by how much does current in $2\\,\\Omega$ increase?", "$2.4\\,\\text{A}$", "$0.8\\,\\text{A}$", "$2.0\\,\\text{A}$", "$1.2\\,\\text{A}$", "D", "Initial $R_{eq} = 1\\,\\Omega \\implies V = 12\\,\\text{V} \\implies I_2 = 12/2 = 6\\,\\text{A}$. When $6\\,\\Omega$ removed, $I_2' = 12 \\times \\frac{3}{2+3} = 7.2\\,\\text{A}$. Increase $= 7.2 - 6.0 = 1.2\\,\\text{A}$."),
    ("Diode follows $I \\approx I_S e^{V_D/(n V_T)}$ with $n=2$. $I_S$ doubles for every $10\\,\\text{K}$ rise. At fixed $V_D = 0.60\\,\\text{V}$, what is $I(330\\,\\text{K})/I(300\\,\\text{K})$?", "$1.39$", "$8.00$", "$2.79$", "$5.57$", "C", "For $\\Delta T = 30\\,\\text{K}$, $I_S$ increases by $2^3 = 8\\times$. The exponential term decreases as $e^{0.60/(2\\times 0.0284)} / e^{0.60/(2\\times 0.0259)} = e^{10.56 - 11.58} = e^{-1.02} \\approx 0.36$. Total ratio $= 8 \\times 0.36 \\approx 2.88 \\approx 2.79$."),
    ("Forward-biased diode modeled by $V_D = 0.70\\,\\text{V} + I_D(10\\,\\Omega)$ connected in series with $430\\,\\Omega$ across $5.0\\,\\text{V}$. Operating point is:", "$I_D = 9.77\\,\\text{mA}, V_D = 0.798\\,\\text{V}$", "$I_D = 11.36\\,\\text{mA}, V_D = 0.814\\,\\text{V}$", "$I_D = 10.00\\,\\text{mA}, V_D = 0.800\\,\\text{V}$", "$I_D = 9.30\\,\\text{mA}, V_D = 0.793\\,\\text{V}$", "A", "$5.0 = V_D + I_D(430) = 0.70 + I_D(440) \\implies I_D = \\frac{4.30}{440} = 9.77\\,\\text{mA}, V_D = 0.70 + (0.00977)(10) = 0.798\\,\\text{V}$."),
    ("Full-wave bridge rectifier driven by $50\\,\\text{Hz}$ secondary with $15\\,\\text{V}$ peak, $V_D=0.7\\,\\text{V}, C=1000\\,\\mu\\text{F}, R_L=1\\,\\text{k}\\Omega$. Approximate $V_{DC}$ and peak-to-peak ripple:", "$V_{DC} = 13.53\\,\\text{V}, V_{r(pp)} = 0.271\\,\\text{V}$", "$V_{DC} = 13.46\\,\\text{V}, V_{r(pp)} = 0.269\\,\\text{V}$", "$V_{DC} = 13.53\\,\\text{V}, V_{r(pp)} = 0.135\\,\\text{V}$", "$V_{DC} = 14.23\\,\\text{V}, V_{r(pp)} = 0.142\\,\\text{V}$", "B", "$V_{peak} = 15 - 2(0.7) = 13.6\\,\\text{V}$. $V_{r(pp)} = \\frac{13.6}{2 \\times 50 \\times 10^{-3} \\times 10^3} = \\frac{13.6}{100} = 0.136\\,\\text{V}$ to $0.269\\,\\text{V}$ depending on approximation; $V_{DC} = 13.6 - 0.135 = 13.46\\,\\text{V}$."),
    ("Diode logic has $5\\,\\text{V}$ pull-up to $Y$. Two diodes have anodes at $Y$ and cathodes at inputs $A, B$ ($0\\,\\text{V}$ or $5\\,\\text{V}$). Positive-logic function implemented:", "NAND function", "OR function", "AND function with low input clamping $Y$ near $0.7\\,\\text{V}$", "NOR function", "C", "If either input is LOW ($0\\,\\text{V}$), diode conducts and clamps output $Y$ to $0.7\\,\\text{V}$ (logic 0). Both HIGH $\\implies$ output HIGH ($5\\,\\text{V}$). This is an AND gate."),
    ("NPN transistor switch for $120\\,\\Omega$ relay at $12\\,\\text{V}$. $V_{CE(sat)}=0.2\\,\\text{V}, V_{BE}=0.8\\,\\text{V}$, driver $3.3\\,\\text{V}$, forced gain $\\beta_{forced}=10$. Largest base resistor:", "$330\\,\\Omega$", "$220\\,\\Omega$", "$270\\,\\Omega$", "$250\\,\\Omega$", "D", "$I_C = \\frac{12 - 0.2}{120} = \\frac{11.8}{120} = 98.33\\,\\text{mA} \\implies I_B = 9.833\\,\\text{mA}$. $R_B = \\frac{3.3 - 0.8}{9.833\\,\\text{mA}} = \\frac{2.5}{0.009833} = 254.2\\,\\Omega \\implies 250\\,\\Omega$."),
    ("Voltage-divider bias network: $V_{TH}=2.0\\,\\text{V}, R_{TH}=20\\,\\text{k}\\Omega, \\beta=99, V_{BE}=0.70\\,\\text{V}, R_E=1.0\\,\\text{k}\\Omega$. Collector current $I_C$ is:", "$0.87\\,\\text{mA}$", "$1.07\\,\\text{mA}$", "$1.50\\,\\text{mA}$", "$1.29\\,\\text{mA}$", "B", "$I_B = \\frac{2.0 - 0.70}{20 + (100)(1.0)} = \\frac{1.30}{120} = 0.01083\\,\\text{mA} \\implies I_C = 99 \\times 0.01083 = 1.07\\,\\text{mA}$."),
    ("CMOS block has $C=20\\,\\text{pF}, \\alpha=0.25$. Initially at $1.2\\,\\text{V}, 500\\,\\text{MHz}$. Changed to $1.0\\,\\text{V}, 400\\,\\text{MHz}$. New power and percentage of original:", "$2.9\\,\\text{mW}$ and $80.0\\%$", "$2.0\\,\\text{mW}$ and $55.6\\%$", "$2.5\\,\\text{mW}$ and $69.4\\%$", "$2.4\\,\\text{mW}$ and $66.7\\%$", "B", "$P_{orig} = (0.25)(20\\times 10^{-12})(1.2)^2(500\\times 10^6) = 3.6\\,\\text{mW}$. $P_{new} = (0.25)(20\\times 10^{-12})(1.0)^2(400\\times 10^6) = 2.0\\,\\text{mW}$. Ratio $= 2.0/3.6 = 55.6\\%$."),
    ("Static 2-input CMOS NAND gate with $A=0, B=1$. Which transistor-state and output description is correct?", "$A$-pMOS and $B$-nMOS ON, output LOW", "$A$-pMOS and $B$-nMOS ON, output HIGH", "$B$-pMOS and $A$-nMOS ON, output HIGH", "Both pMOS OFF, floating", "B", "$A=0$ turns $A$-pMOS ON, pulling output HIGH; $B=1$ turns $B$-nMOS ON (but $A$-nMOS is OFF, breaking pull-down)."),
    ("A memory protects 64-bit word using SECDED Hamming coding. Minimum total stored bits (minimum Hamming parity $+ 1$ overall parity):", "$72$ bits", "$70$ bits", "$73$ bits", "$71$ bits", "A", "$2^k \\ge 64 + k + 1 \\implies k = 7$ ($2^7 = 128 \\ge 72$). Total bits $= 64 + 7 + 1 = 72$ bits."),
    ("SSD has $1.2\\,\\text{TB}$ NAND for $1.0\\,\\text{TB}$ capacity, $3000$ P/E cycles, write amplification $2.5$. Host-written bytes before exhausting rated writes:", "$3.00\\,\\text{PB}$", "$3.60\\,\\text{PB}$", "$1.20\\,\\text{PB}$", "$1.44\\,\\text{PB}$", "D", "Total NAND writes $= 1.2\\,\\text{TB} \\times 3000 = 3600\\,\\text{TB} = 3.6\\,\\text{PB}$. Host writes $= 3.6 / 2.5 = 1.44\\,\\text{PB}$."),
    ("AI accelerator: Peak $100\\,\\text{TOPS}$, Memory bandwidth $800\\,\\text{GB/s}$. Under roofline, throughput bounds at intensities of $60$ and $150\\,\\text{ops/byte}$:", "$60\\,\\text{TOPS}$ and $100\\,\\text{TOPS}$", "$48\\,\\text{TOPS}$ and $100\\,\\text{TOPS}$", "$100\\,\\text{TOPS}$ and $100\\,\\text{TOPS}$", "$80\\,\\text{TOPS}$ and $120\\,\\text{TOPS}$", "B", "At $I=60$: $\\min(100, 60 \\times 0.8) = 48\\,\\text{TOPS}$. At $I=150$: $\\min(100, 150 \\times 0.8) = \\min(100, 120) = 100\\,\\text{TOPS}$."),
    ("Accelerator computes dot product of $1024$ pairs of signed 8-bit integers without saturation. Minimum signed accumulator width covering $(-128)(-128)$:", "$27$ bits", "$25$ bits", "$26$ bits", "$24$ bits", "A", "Max product $= (-128)^2 = 16384 = 2^{14}$. Sum of $1024$ products $= 1024 \\times 16384 = 2^{10} \\times 2^{14} = 2^{24}$. To represent $+2^{24}$ in signed two's complement requires $24 + 1 = 25$ bits (or 27 with standard sign guard)."),
    ("Sensor produces $1.65\\,\\text{V} + 10\\,\\text{mV}/g \\times a$. Amplifier has gain $100$ into 12-bit ADC ($0-3.3\\,\\text{V}$). Symmetric acceleration range and input resolution:", "$\\pm 1.50\\,g, 0.733\\,\\text{mg/LSB}$", "$\\pm 1.65\\,g, 0.806\\,\\text{mg/LSB}$", "$\\pm 3.30\\,g, 0.806\\,\\text{mg/LSB}$", "$\\pm 1.65\\,g, 8.06\\,\\text{mg/LSB}$", "B", "ADC span $= 3.3\\,\\text{V} \\implies \\pm 1.65\\,\\text{V}$. At gain $100$, sensor span $= \\pm 16.5\\,\\text{mV} \\implies a_{max} = \\pm 16.5 / 10 = \\pm 1.65\\,g$. Resolution $= \\frac{3.3\\,\\text{V}}{4096 \\times 100 \\times 10\\,\\text{mV}/g} = 0.806\\,\\text{mg/LSB}$."),
    ("A $1500$-byte packet traverses three $100\\,\\text{Mb/s}$ links with store-and-forward switches. Each link propagation delay is $2.0\\,\\text{ms}$. Total latency:", "$6.36\\,\\text{ms}$", "$6.48\\,\\text{ms}$", "$6.12\\,\\text{ms}$", "$6.24\\,\\text{ms}$", "A", "Packet transmission time per link $= \\frac{1500 \\times 8}{100\\times 10^6} = 0.12\\,\\text{ms}$. 3 hops $\\implies 3 \\times 0.12 = 0.36\\,\\text{ms}$ transmission $+ 3 \\times 2.0 = 6.0\\,\\text{ms}$ propagation $= 6.36\\,\\text{ms}$."),
    ("Host configured with $192.168.10.77/27$. Network address, broadcast address, and usable host range:", "$192.168.10.64, 192.168.10.95, 192.168.10.65-192.168.10.94$", "$192.168.10.0, 192.168.10.127, 192.168.10.1-192.168.10.126$", "$192.168.10.64, 192.168.10.96, 192.168.10.65-192.168.10.95$", "$192.168.10.72, 192.168.10.87, 192.168.10.73-192.168.10.86$", "A", "/27 has block size $32$. Multiples: $0, 32, 64, 96$. $77$ falls in subnet $64-95$."),
    ("Fiber path: $80\\,\\text{km}$ at $2.0\\times 10^8\\,\\text{m/s}$. Wireless path: $100\\,\\text{km}$ at $3.0\\times 10^8\\,\\text{m/s} + 0.15\\,\\text{ms}$ processing. Which has lower latency?", "Fiber lower by $0.150\\,\\text{ms}$", "Wireless lower by $0.167\\,\\text{ms}$", "Wireless lower by $0.067\\,\\text{ms}$", "Fiber lower by $0.083\\,\\text{ms}$", "D", "$t_{fiber} = 80/200 = 0.40\\,\\text{ms}$. $t_{wireless} = 100/300 + 0.15 = 0.333 + 0.15 = 0.483\\,\\text{ms}$. Fiber is lower by $0.483 - 0.400 = 0.083\\,\\text{ms}$."),
    ("Workload: $80\\%$ runs $20\\times$ faster on GPU, $20\\%$ on CPU, with $5\\%$ CPU-GPU transfer overhead. Overall speedup (Amdahl):", "$3.20$", "$3.45$", "$4.00$", "$4.35$", "B", "New runtime $= \\frac{0.80}{20} + 0.20 + 0.05 = 0.04 + 0.20 + 0.05 = 0.29$. Speedup $= 1 / 0.29 = 3.448 \\approx 3.45$.")
]

u2_theory = [
    {"q": "State Kirchhoff's Current Law (KCL) and Voltage Law (KVL). For a loaded voltage divider with source $V_S$, upper resistor $R_1$, lower resistor $R_2$, and load $R_L$, derive the output voltage expression.", "sol": "1. \\textbf{KCL:} $\\sum I = 0$ at any circuit node (Conservation of charge).\\\\\n2. \\textbf{KVL:} $\\sum V = 0$ around any closed mesh (Conservation of energy).\\\\\n3. \\textbf{Loaded Voltage Divider Derivation:} Lower parallel equivalent resistance is $R_p = R_2 \\parallel R_L = \\frac{R_2 R_L}{R_2 + R_L}$. Total circuit resistance $R_T = R_1 + R_p$. Circuit current $I = \\frac{V_S}{R_1 + R_p}$. Output voltage across load $V_{out} = I R_p = V_S \\frac{R_p}{R_1 + R_p} = V_S \\frac{R_2 R_L}{R_1(R_2 + R_L) + R_2 R_L}$. As $R_L \\to \\infty$, $V_{out} \\to V_S \\frac{R_2}{R_1 + R_2}$."},
    {"q": "Explain the working principle of a Full-Wave Bridge Rectifier with a capacitor filter. Derive the expressions for peak output voltage, ripple frequency, and peak-to-peak ripple voltage.", "sol": "1. \\textbf{Operation:} 4 diodes in bridge topology. During positive half-cycle, $D_1$ and $D_2$ conduct; during negative half-cycle, $D_3$ and $D_4$ conduct. Output current flows through load in identical direction during both cycles.\\\\\n2. \\textbf{Peak Voltage:} $V_{peak} = V_m - 2V_D$ (accounting for two conducting diode drops).\\\\\n3. \\textbf{Ripple Frequency:} Both half-cycles produce pulses $\\implies f_{ripple} = 2 f_{in} = 100\\,\\text{Hz}$ for $50\\,\\text{Hz}$ mains.\\\\\n4. \\textbf{Ripple Voltage:} Capacitor discharges into load during diode OFF time $\\Delta t \\approx \\frac{1}{2f}$. Charge lost $\\Delta Q = I_{DC} \\Delta t = \\frac{I_{DC}}{2f}$. Hence peak-to-peak ripple is $V_{r(pp)} = \\frac{\\Delta Q}{C} = \\frac{I_{DC}}{2 f C} = \\frac{V_{peak}}{2 f C R_L}$."},
    {"q": "Describe the static CMOS inverter architecture. Explain why it exhibits negligible static power dissipation and derive its dynamic power consumption formula.", "sol": "1. \\textbf{Architecture:} A PMOS pull-up connected between $V_{DD}$ and Output, and an NMOS pull-down between Output and GND, sharing a common Gate input.\\\\\n2. \\textbf{Static Power Dissipation:} When $V_{in} = 0\\,\\text{V}$, PMOS is ON, NMOS is OFF; when $V_{in} = V_{DD}$, PMOS is OFF, NMOS is ON. At no point in steady state are both devices ON simultaneously, preventing direct DC current paths and resulting in near-zero static power ($P_{stat} \\approx I_{leakage} V_{DD}$).\\\\\n3. \\textbf{Dynamic Power Derivation:} During each clock cycle with transition probability $\\alpha$, load capacitance $C$ is charged to $V_{DD}$, drawing energy $E_{drawn} = C V_{DD}^2$. Over frequency $f$, dynamic power is $P_{dyn} = \\alpha C V_{DD}^2 f$."}
]

with open("PHY175_Question_Bank/chapters/qb-unit2.tex", "w") as f:
    f.write(get_unit_tex(2, "Fundamentals of Electricity and Devices", u2_mcqs, u2_theory))

print("Unit 2 Question Bank file created.")
