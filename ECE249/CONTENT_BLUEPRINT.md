# ECE249: Digital Electronics, Electrical Fundamentals & Microcontroller Interfacing
## Master Course Analysis & Textbook Production Blueprint

---

### Course Metadata & Pedagogical Architecture
- **Course Code:** ECE249
- **Course Title:** Fundamentals of Electrical Laws, Semiconductor Devices, Digital Electronics, and Arduino Interfacing
- **Target Audience:** First- and Second-Year Undergraduate Engineering Students (ECE, CSE, IT, EE, ME, Robotics)
- **Pedagogical Philosophy:** 
  $$\text{UNDERSTAND} \longrightarrow \text{VISUALIZE} \longrightarrow \text{SOLVE} \longrightarrow \text{PRACTICE} \longrightarrow \text{EXAM}$$
- **Document Version:** 1.0 (Phase 1 Master Blueprint)
- **Authoring Initiative:** University Engineering Open Textbook Initiative

---

## 1. Complete Syllabus Hierarchy & Unit Structure

The ECE249 course is structured into **six core units**, followed by consolidated review and assessment modules:

```
ECE249 Comprehensive Structure
├── UNIT 1: Fundamentals of Electrical Laws, Semiconductor Devices and its Applications
│   ├── 1.1 DC Circuit Analysis Fundamentals (Ohm's Law, KCL, KVL, VDR, CDR)
│   ├── 1.2 Semiconductor Physics & Band Theory of Solids
│   ├── 1.3 Intrinsic & Extrinsic Semiconductors (N-Type, P-Type, Doping Mechanisms)
│   ├── 1.4 PN Junction Diode (Formation, Biasing, V-I Curves, Knee Voltage, Reverse Saturation)
│   ├── 1.5 Diode Applications (Ideal/Practical Switch, Half-Wave, Center-Tapped & Bridge Rectifiers)
│   └── 1.6 Bipolar Junction Transistor (BJT) Construction, Current Equation, Operating Modes, CE Configuration & Gain
├── UNIT 2: Introduction of Arduino, Signals, and Sensor Interfacing
│   ├── 2.1 Signal Characterization: Analog vs. Digital (Waveforms, Noise Immunity, Continuous vs. Discrete)
│   ├── 2.2 Arduino UNO Architecture & Hardware Specifications (ATmega328P, Clock, Power, Memory)
│   ├── 2.3 Comprehensive Pinout Analysis (Power, Analog Inputs A0–A5, Digital I/O 0–13, PWM, UART, SPI, Interrupts)
│   ├── 2.4 Active IR Obstacle & Line-Tracking Sensors (IR LED + Photodiode + LM393 Comparator)
│   ├── 2.5 Light Dependent Resistor (LDR / Photoresistor, CdS Photoconductivity, Voltage Divider Interfacing)
│   ├── 2.6 Ultrasonic Rangefinder HC-SR04 (Echolocation, Timing Pulse, Speed of Sound Calculation)
│   └── 2.7 Temperature & Humidity Sensors DHT11 / DHT22 (Capacitive Substrate, NTC, 1-Wire Protocol)
├── UNIT 3: Number Systems, Binary Codes, Boolean Algebra & Karnaugh Maps
│   ├── 3.1 Positional Number Systems (Binary, Octal, Decimal, Hexadecimal, Direct & Intermediate Conversions)
│   ├── 3.2 Binary Codes (BCD/8421, Excess-3 Self-Complementing Code, Gray Unit-Distance Code & Conversion)
│   ├── 3.3 Complements & Fixed-Point Binary Arithmetic (1's & 2's Complements, Subtraction via 2's Complement)
│   ├── 3.4 Logic Gates (Basic: AND/OR/NOT; Universal: NAND/NOR; Special: XOR/XNOR; Realizations)
│   ├── 3.5 Boolean Algebra Laws, Axioms, Dualities & De Morgan's Theorems
│   ├── 3.6 Standard & Canonical Forms (Minterms, Maxterms, Canonical SOP $\sum m$, Canonical POS $\prod M$)
│   └── 3.7 Karnaugh Maps (2, 3, and 4-Variable K-Maps, Gray Code Adjacency, Grouping Rules, Don't-Cares $X$)
├── UNIT 4: Combinational Logic Circuits
│   ├── 4.1 Combinational Logic Design Fundamentals (Analysis & Synthesis Flow)
│   ├── 4.2 Arithmetic Adders: Half Adder & Full Adder (Gate-Level & Two-Half-Adder Implementations)
│   ├── 4.3 Arithmetic Subtractors: Half Subtractor & Full Subtractor (Gate-Level & Two-Half-Subtractor Realizations)
│   ├── 4.4 Multiplexers (Data Selectors: 2:1, 4:1, 8:1 MUX, Expansion & Boolean Function Implementation)
│   ├── 4.5 De-Multiplexers (Data Distributors: 1:2, 1:4, 1:8 DEMUX, Decoders Comparison)
│   ├── 4.6 Binary Decoders (2-to-4, 3-to-8 with Active-High / Active-Low Enables, Logic Synthesis)
│   ├── 4.7 Binary Encoders (8-to-3 Octal Encoder, Decimal-to-BCD, Priority Encoders)
│   └── 4.8 Magnitude Comparators (1-Bit and 2-Bit Identity & Inequality Circuit Synthesis)
├── UNIT 5: Sequential Logic Fundamentals: Latches, Flip-Flops & Conversions
│   ├── 5.1 Sequential Circuit Fundamentals (Memory, Feedback, Synchronous vs. Asynchronous)
│   ├── 5.2 Bistable Latches (Cross-Coupled NOR SR Latch, Cross-Coupled NAND $\bar{S}\bar{R}$ Latch, Gated D Latch)
│   ├── 5.3 Edge-Triggered Flip-Flops (Clocked SR, JK, D, and T Flip-Flops: Truth, Characteristic & Excitation)
│   ├── 5.4 Race-Around Phenomenon in Level-Triggered JK Flip-Flops
│   ├── 5.5 Master-Slave JK Flip-Flop Architecture (Two-Stage Pulse-Triggered Operation, Glitch Elimination)
│   └── 5.6 Systematic Flip-Flop Conversion Methodology (Conversion Tables, K-Map Synthesis, Complete Verifications)
├── UNIT 6: Applications of Sequential Circuits: Registers & Counters
│   ├── 6.1 Register Architecture & Data Transfer Modes
│   ├── 6.2 Shift Registers: SISO, SIPO, PISO, PIPO Operations & Timing Waveforms
│   ├── 6.3 Asynchronous (Ripple) Counters: Up, Down, and Modulo-N Truncated Counters (Decade/BCD 7490)
│   ├── 6.4 Synchronous Counters: Up, Down, Up/Down, Modulo-N Counter Design & State Diagram Synthesis
│   └── 6.5 Shift Register Counters: Ring Counter ($N$ States) & Johnson/Twisted-Ring Counter ($2N$ States)
├── CHAPTER 7: Master Revision & Formula Sheet
├── CHAPTER 8: Comprehensive Solved Practice Problems (All Units)
└── CHAPTER 9: University-Style Mock Examinations (2 Complete Exam Papers with Detailed Solutions)
```

---

## 2. Unit-by-Unit Detailed Topic Mapping & Learning Objectives

### UNIT 1: Fundamentals of Electrical Laws, Semiconductor Devices and its Applications
#### Learning Objectives:
1. Apply Ohm's law, KCL, and KVL to solve complex multi-loop DC resistive circuits.
2. Calculate branch currents and node voltages using Voltage Division and Current Division rules.
3. Understand energy band diagrams of conductors, insulators, and semiconductors ($E_g$ values for Si and Ge).
4. Explain carrier generation, recombination, drift, and diffusion in intrinsic and doped (N-type, P-type) semiconductors.
5. Describe the formation of the PN junction, depletion width dynamics, and barrier potential ($0.7\text{ V}$ for Si, $0.3\text{ V}$ for Ge).
6. Analyze diode V-I characteristics in forward and reverse bias, identifying knee voltage, reverse saturation current $I_0$, and breakdown mechanisms (Zener vs. Avalanche).
7. Calculate rectification parameters for Half-Wave, Center-Tapped Full-Wave, and Bridge Rectifiers ($\eta_{max}$, ripple factor $\gamma$, PIV, $V_{dc}$, $I_{rms}$).
8. Analyze BJT terminal construction, current relationships ($I_E = I_B + I_C$), operating modes (Cut-off, Active, Saturation), Common-Emitter (CE) characteristics, and current gain $\beta = \frac{\alpha}{1-\alpha}$.

#### Required Circuit Schematics & Diagrams:
- DC circuit meshes illustrating KCL at nodes and KVL around closed loops.
- Voltage divider circuit ($V_{out} = V_s \frac{R_2}{R_1+R_2}$) and Current divider circuit ($I_1 = I_s \frac{R_2}{R_1+R_2}$).
- Energy band diagrams showing valence band, conduction band, and forbidden gap $E_g$ for Insulator, Semiconductor, Conductor.
- Crystal lattice models of pure Silicon, N-type (Phosphorus donor atom + free electron), and P-type (Boron acceptor atom + hole).
- PN junction in unbiased equilibrium, forward bias (narrow depletion region), and reverse bias (widened depletion region).
- Diode V-I characteristic curve spanning Quadrants I and III with labeled Knee Voltage ($V_k$), Reverse Saturation Current ($I_0$), and Breakdown Voltage ($V_Z$).
- Half-Wave Rectifier circuit diagram with input AC, diode, load resistor, and output DC waveforms.
- Full-Wave Center-Tapped Rectifier circuit with secondary transformer center-tap and dual diodes.
- Full-Wave Bridge Rectifier circuit showing conduction paths in positive (D1, D3) and negative (D2, D4) half-cycles.
- BJT structural cross-section (NPN and PNP) with Emitter, Base, Collector doping and width comparison.
- Common Emitter (CE) NPN configuration circuit with biasing supplies $V_{BB}$, $V_{CC}$ and resistors $R_B$, $R_C$.
- CE Input Characteristics ($I_B$ vs. $V_{BE}$ for constant $V_{CE}$) and Output Characteristics ($I_C$ vs. $V_{CE}$ for constant $I_B$) with labeled Cut-off, Active, and Saturation regions.

#### Required Formulas & Equations:
- **Ohm's Law:** $V = I \cdot R$
- **KCL:** $\sum I_{in} = \sum I_{out} \iff \sum I = 0$
- **KVL:** $\sum V_{rises} = \sum V_{drops} \iff \sum V = 0$
- **Voltage Division (2 Resistors in Series):**
  $$V_1 = V_s \left(\frac{R_1}{R_1 + R_2}\right), \quad V_2 = V_s \left(\frac{R_2}{R_1 + R_2}\right)$$
- **Current Division (2 Resistors in Parallel):**
  $$I_1 = I_s \left(\frac{R_2}{R_1 + R_2}\right), \quad I_2 = I_s \left(\frac{R_1}{R_1 + R_2}\right)$$
- **Intrinsic Mass-Action Law:** $n \cdot p = n_i^2$
- **Shockley Diode Equation:** $I = I_0 \left(e^{\frac{V}{\eta V_T}} - 1\right)$
- **Half-Wave Rectifier Parameters:**
  $$V_{dc} = \frac{V_m}{\pi} \approx 0.318 V_m, \quad V_{rms} = \frac{V_m}{2}, \quad \text{Ripple Factor } \gamma = \sqrt{\left(\frac{V_{rms}}{V_{dc}}\right)^2 - 1} \approx 1.21, \quad \eta_{max} = \frac{4}{\pi^2} \frac{R_L}{r_f + R_L} \approx 40.6\%, \quad \text{PIV} = V_m$$
- **Full-Wave Bridge Rectifier Parameters:**
  $$V_{dc} = \frac{2V_m}{\pi} \approx 0.636 V_m, \quad V_{rms} = \frac{V_m}{\sqrt{2}}, \quad \text{Ripple Factor } \gamma = \sqrt{\left(\frac{V_{rms}}{V_{dc}}\right)^2 - 1} \approx 0.48, \quad \eta_{max} = \frac{8}{\pi^2} \approx 81.2\%, \quad \text{PIV} = V_m \text{ (Bridge)}, \; 2V_m \text{ (Center-Tap)}$$
- **BJT Current Equations:**
  $$I_E = I_B + I_C$$
  $$I_C = \beta I_B + I_{CEO} = \alpha I_E + I_{CBO}$$
  $$\beta = \frac{\alpha}{1 - \alpha}, \quad \alpha = \frac{\beta}{1 + \beta}$$

---

### UNIT 2: Introduction of Arduino and Sensors
#### Learning Objectives:
1. Distinguish between continuous analog signals and discrete digital signals in time, amplitude, noise tolerance, and transmission.
2. Master the hardware architecture of Arduino UNO (ATmega328P microcontroller, 16 MHz crystal, 32 KB Flash, 2 KB SRAM, 1 KB EEPROM).
3. Comprehend pin functional assignments: Power (Vin, 5V, 3.3V, GND, IOREF), 6 Analog inputs A0–A5 with 10-bit ADC, 14 Digital I/O (0–13), PWM outputs (~3, ~5, ~6, ~9, ~10, ~11), Serial UART (0 RX, 1 TX), External Interrupts (2, 3), and SPI (10–13).
4. Analyze the working mechanism of active IR obstacle and line-tracking sensors (IR transmitter LED, photodiode, LM393 operational amplifier comparator, threshold potentiometer).
5. Understand the photoconductivity of Light Dependent Resistors (CdS semiconductor band structure, inverse resistance-illuminance relationship) and calculate voltage divider outputs.
6. Derive distance from time-of-flight measurements using Ultrasonic Sensor HC-SR04 (10 $\mu\text{s}$ trigger pulse, 40 kHz burst, echo pulse width, acoustic velocity $v = 340\text{ m/s}$).
7. Evaluate capacitive humidity and NTC thermistor temperature sensing in DHT11 and DHT22 modules, analyzing digital single-bus serial packet timing.

#### Required Diagrams & Schematics:
- Waveform comparison: Continuous sinusoidal analog signal vs. discrete square-wave digital signal.
- Arduino UNO complete board layout with callouts for ATmega328P, USB port, DC power barrel jack, voltage regulators, reset button, pin headers, and status LEDs (TX, RX, L, ON).
- Analog-to-Digital Converter (ADC) transfer curve showing 10-bit mapping ($0\text{ V} \rightarrow 0$, $5\text{ V} \rightarrow 1023$, $\text{Step size} = \frac{5\text{ V}}{1024} \approx 4.88\text{ mV}$).
- Pulse Width Modulation (PWM) waveforms showing $0\%$, $25\%$, $50\%$, $75\%$, and $100\%$ duty cycles and equivalent DC voltage values.
- Active IR Sensor Module schematic showing IR emitter LED, reverse-biased photodiode, LM393 comparator, potentiometer, and D0 digital output.
- Line follower surface reflection behavior: IR reflection on high-albedo white surface vs. absorption on black matte surface.
- LDR Voltage Divider interfacing circuit with Arduino Analog Pin A0 (Pull-down and Pull-up configurations).
- Ultrasonic Sensor HC-SR04 timing diagram: $10\,\mu\text{s}$ Trig input $\rightarrow$ 8-cycle 40 kHz acoustic burst $\rightarrow$ Echo pulse width ($t$) proportional to round-trip distance.
- DHT11 / DHT22 internal block diagram showing capacitive moisture substrate, NTC thermistor, 8-bit MCU, and 40-bit serial single-bus communication frame.

#### Required Formulas & Calculations:
- **ADC Voltage Conversion:**
  $$V_{analog} = \text{ADC\_Value} \times \left(\frac{V_{ref}}{1023}\right) = \text{ADC\_Value} \times \left(\frac{5.0\text{ V}}{1023}\right)$$
- **PWM Output Average Voltage:**
  $$V_{avg} = V_{CC} \times \left(\frac{\text{Duty Cycle}}{100}\right) = 5.0\text{ V} \times \left(\frac{\text{analogWrite Value}}{255}\right)$$
- **LDR Voltage Divider:**
  $$V_{out} = V_{CC} \times \left(\frac{R_{fixed}}{R_{LDR} + R_{fixed}}\right) \quad (\text{LDR on top})$$
- **Ultrasonic Distance Calculation:**
  $$\text{Distance (cm)} = \frac{\text{Echo Pulse Width } (\mu\text{s}) \times 0.0343\text{ cm/}\mu\text{s}}{2} = \frac{\text{Echo Time } (\mu\text{s})}{58.3}$$
  $$\text{Distance (inches)} = \frac{\text{Echo Time } (\mu\text{s})}{148}$$

---

### UNIT 3: Number Systems, Logic Gates, Boolean Algebra & Karnaugh Maps
#### Learning Objectives:
1. Perform multi-base conversions across Binary, Octal, Decimal, and Hexadecimal systems for both integer and fractional components.
2. Differentiate weighted codes (Binary, Octal, Hex, BCD 8421) from non-weighted codes (Excess-3, Gray code).
3. Execute Binary $\leftrightarrow$ Gray code conversions using bitwise XOR logic.
4. Calculate $(r-1)$'s and $r$'s complements (1's, 2's, 9's, 10's complements) and execute subtraction using 2's complement with overflow/carry analysis.
5. Analyze truth tables, logic symbols, and Boolean expressions for all 7 standard logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR).
6. Prove the functional universality of NAND and NOR gates by synthesizing all basic operations.
7. Simplify complex Boolean expressions using algebraic identities, absorption laws, and De Morgan's theorems.
8. Expand Boolean expressions into Canonical Sum of Products (Minterms $\sum m$) and Canonical Product of Sums (Maxterms $\prod M$).
9. Formulate, plot, and minimize 2-variable, 3-variable, and 4-variable Karnaugh Maps (K-Maps) using Gray code cell ordering, prime implicant grouping (pairs, quads, octets), roll-over/wrap-around boundaries, and Don't Care conditions ($X$).

#### Required Truth Tables, Conversion Tables & K-Map Grids:
- Master Number Representation Table: Decimal 0 to 15 mapped to Binary (4-bit), Octal, Hexadecimal, BCD (8421), Excess-3, and Gray Code.
- Logic Gate Summary Table: Gate name, IEEE standard symbol, algebraic equation, truth table, and switch equivalent.
- Universal Gate Implementation Matrix: Schematics for building NOT, AND, OR, XOR, XNOR using ONLY NAND gates, and ONLY NOR gates.
- Boolean Algebra Postulates and Laws Table (Identity, Domination, Idempotence, Involution, Complementarity, Commutative, Associative, Distributive, Absorption, De Morgan's).
- Canonical Minterm ($m$) and Maxterm ($M$) Designation Table for 3-variable and 4-variable spaces.
- K-Map Layouts:
  - 2-Variable K-Map ($2 \times 2 = 4$ cells: $m_0, m_1, m_2, m_3$)
  - 3-Variable K-Map ($2 \times 4 = 8$ cells: $m_0$ to $m_7$ with $00, 01, 11, 10$ column ordering)
  - 4-Variable K-Map ($4 \times 4 = 16$ cells: $m_0$ to $m_{15}$ with Gray code row and column ordering)
- Annotated K-Map grouping examples showing:
  - Single cell (no reduction)
  - 2-cell Pair (eliminates 1 variable)
  - 4-cell Quad (eliminates 2 variables)
  - 8-cell Octet (eliminates 3 variables)
  - 16-cell full group (reduces to logic 1)
  - Corner Quad ($m_0, m_2, m_8, m_{10} \implies \bar{B}\bar{D}$)
  - Don't-Care optimal grouping ($d$ / $X$).

#### Required Algorithms & Conversion Rules:
- **Decimal to Base-$r$:** Successive division by $r$ (record remainders bottom-to-top) + Successive multiplication by $r$ (record integer parts top-to-bottom).
- **Binary to Gray Code:**
  $$G_{MSB} = B_{MSB}, \quad G_i = B_{i+1} \oplus B_i$$
- **Gray Code to Binary:**
  $$B_{MSB} = G_{MSB}, \quad B_i = B_{i+1} \oplus G_i$$
- **2's Complement Subtraction ($A - B$):**
  1. Compute $2\text{'s complement of } B = \overline{B} + 1$.
  2. Compute $Sum = A + (2\text{'s complement of } B)$.
  3. If End-Around Carry = 1: Discard carry $\implies$ Result is Positive and in true binary.
  4. If End-Around Carry = 0: Result is Negative $\implies$ Magnitude is $2\text{'s complement of } Sum$.
- **De Morgan's Theorems:**
  $$\overline{A \cdot B} = \overline{A} + \overline{B}, \quad \overline{A + B} = \overline{A} \cdot \overline{B}$$
  $$\overline{A_1 \cdot A_2 \cdots A_n} = \overline{A_1} + \overline{A_2} + \cdots + \overline{A_n}, \quad \overline{A_1 + A_2 + \cdots + A_n} = \overline{A_1} \cdot \overline{A_2} \cdots \overline{A_n}$$

---

### UNIT 4: Introduction to Combinational Logic Circuits
#### Learning Objectives:
1. Understand the formal design process for combinational logic: Specification $\rightarrow$ Truth Table $\rightarrow$ K-Map Simplification $\rightarrow$ Logic Circuit Diagram.
2. Design, analyze, and synthesize Half Adders and Full Adders using basic gates and XOR-AND networks; implement a Full Adder using two Half Adders and an OR gate.
3. Design, analyze, and synthesize Half Subtractors and Full Subtractors; implement a Full Subtractor using two Half Subtractors and an OR gate.
4. Master Multiplexers (MUX) as data selectors: Design 2:1, 4:1, and 8:1 MUX circuits using AND-OR structures, and implement arbitrary Boolean functions using MUXes.
5. Master De-multiplexers (DEMUX) as data distributors: Synthesize 1:2, 1:4, and 1:8 DEMUX circuits and explain their relationship to decoders.
6. Design binary decoders (2-to-4 line, 3-to-8 line) with Active-High and Active-Low Enable inputs; implement higher-order decoders (e.g., 3-to-8 using 2-to-4).
7. Synthesize binary encoders (8-to-3 Octal-to-Binary, Decimal-to-BCD) and Priority Encoders (resolving simultaneous multi-input active states).
8. Design 1-bit and 2-bit Digital Magnitude Comparators generating $A > B$, $A = B$, and $A < B$ outputs.

#### Required Circuit Schematics & Truth Tables:
- Half Adder: Block diagram, Truth Table, and Logic Diagram ($S = A \oplus B$, $C = A \cdot B$).
- Full Adder: Block diagram, 3-input Truth Table, K-Maps for $S$ and $C_{out}$, Gate-level Logic Schematic, and Two-Half-Adder composite block.
- Half Subtractor: Block diagram, Truth Table, Logic Diagram ($D = A \oplus B$, $B_{out} = \bar{A}B$).
- Full Subtractor: Block diagram, 3-input Truth Table, K-Maps for $D$ and $B_{out}$, Gate-level Logic Schematic, and Two-Half-Subtractor composite diagram.
- 4:1 Multiplexer: Block diagram, Functional Truth Table, Gate-level circuit (4 AND gates, 1 OR gate, 2 NOT gates), and Boolean equation.
- 8:1 Multiplexer implementation of 3-variable and 4-variable logic functions without external gates.
- 1:4 De-multiplexer: Block diagram, Truth Table, Logic Diagram (4 AND gates, 2 NOT gates).
- 2-to-4 Line Decoder: Block diagram with Enable ($E$), Truth Table, Gate schematic.
- 3-to-8 Line Decoder (74138 style) with Active-Low outputs.
- 8-to-3 Octal-to-Binary Encoder logic diagram using 3 OR gates.
- 4-Input Priority Encoder Truth Table (with Don't Care inputs and Valid flag $V$) and Logic Schematic.
- 1-Bit Magnitude Comparator circuit ($A=B \implies \overline{A \oplus B}$, $A>B \implies A\bar{B}$, $A<B \implies \bar{A}B$).
- 2-Bit Magnitude Comparator complete logic circuit with inputs $A_1A_0, B_1B_0$.

#### Required Formulas & Equations:
- **Full Adder:**
  $$S = A \oplus B \oplus C_{in}, \quad C_{out} = AB + BC_{in} + AC_{in} = AB + C_{in}(A \oplus B)$$
- **Full Subtractor:**
  $$D = A \oplus B \oplus B_{in}, \quad B_{out} = \overline{A}B + \overline{A}B_{in} + BB_{in} = \overline{A}B + B_{in}\overline{(A \oplus B)}$$
- **4:1 MUX Output:**
  $$Y = \overline{S_1}\,\overline{S_0}I_0 + \overline{S_1}S_0I_1 + S_1\overline{S_0}I_2 + S_1S_0I_3$$
- **1:4 DEMUX Outputs:**
  $$Y_0 = \overline{S_1}\,\overline{S_0}D_{in}, \quad Y_1 = \overline{S_1}S_0D_{in}, \quad Y_2 = S_1\overline{S_0}D_{in}, \quad Y_3 = S_1S_0D_{in}$$
- **2-Bit Comparator Equations:**
  $$\text{Let } x_1 = \overline{A_1 \oplus B_1} = A_1B_1 + \overline{A_1}\,\overline{B_1}, \quad x_0 = \overline{A_0 \oplus B_0} = A_0B_0 + \overline{A_0}\,\overline{B_0}$$
  $$(A = B) = x_1 \cdot x_0$$
  $$(A > B) = A_1\overline{B_1} + x_1 A_0\overline{B_0}$$
  $$(A < B) = \overline{A_1}B_1 + x_1 \overline{A_0}B_0$$

---

### UNIT 5: Introduction to Sequential Logic Circuits
#### Learning Objectives:
1. Explain the fundamental difference between combinational logic and sequential logic, highlighting the role of memory, clocking, and feedback.
2. Differentiate between asynchronous latches (level-sensitive) and synchronous flip-flops (edge-triggered).
3. Analyze the cross-coupled NOR SR latch and cross-coupled NAND $\bar{S}\bar{R}$ latch, demonstrating state derivation and the cause of invalid/metastable states ($S=R=1$ in NOR, $\bar{S}=\bar{R}=0$ in NAND).
4. Evaluate the Gated D Latch (Transparent Latch), explaining how it eliminates invalid states.
5. Master the four foundational Flip-Flops: SR, JK, D, and T Flip-Flops. For each flip-flop, construct its Logic Symbol, Gate-Level Circuit, Truth Table, Characteristic Table, Characteristic Equation (via K-Map), and Excitation Table.
6. Detail the **Race-Around Condition** in level-triggered JK flip-flops ($J=K=1$, clock pulse duration $t_p > t_{pd}$ propagation delay).
7. Construct and analyze the **Master-Slave JK Flip-Flop** (Master active on clock high, Slave active on clock low/inverted clock) to eliminate race-around.
8. Master the universal 5-step **Flip-Flop Conversion Methodology** to convert any source flip-flop into any target flip-flop (SR to JK, JK to D, SR to D, JK to T, D to T, T to D).

#### Required Tables, Schematics & State Diagrams:
- Cross-Coupled NOR SR Latch circuit and operational Truth Table.
- Cross-Coupled NAND $\bar{S}\bar{R}$ Latch circuit and operational Truth Table.
- Gated D Latch circuit diagram and timing waveform showing transparency.
- Clocked SR Flip-Flop: Symbol, Gate schematic (4 NANDs), Truth Table, Characteristic Table, Excitation Table.
- Clocked JK Flip-Flop: Symbol, Gate schematic with output feedback, Truth Table, Characteristic Table, Excitation Table.
- Clocked D Flip-Flop: Symbol, Circuit, Characteristic Table, Excitation Table.
- Clocked T Flip-Flop: Symbol, Circuit, Characteristic Table, Excitation Table.
- Timing diagram illustrating the **Race-Around Phenomenon** in level-triggered JK Flip-Flop when $J=K=1$.
- Master-Slave JK Flip-Flop circuit schematic showing Master stage, Slave stage, clock inverter, and feedback loops.
- Master-Slave timing waveforms showing Master state capture on rising edge and Slave output update on falling edge.
- Complete Flip-Flop Conversion Diagrams with auxiliary combinational logic for:
  - SR $\rightarrow$ JK Flip-Flop ($S = J\bar{Q}, R = KQ$)
  - JK $\rightarrow$ D Flip-Flop ($J = D, K = \bar{D}$)
  - SR $\rightarrow$ D Flip-Flop ($S = D, R = \bar{D}$)
  - JK $\rightarrow$ T Flip-Flop ($J = T, K = T$)
  - D $\rightarrow$ T Flip-Flop ($D = T \oplus Q$)

#### Master Flip-Flop Summary Equations:
- **SR Flip-Flop:** $Q_{n+1} = S + \overline{R}Q_n \quad (\text{Constraint: } SR = 0)$
- **JK Flip-Flop:** $Q_{n+1} = J\overline{Q}_n + \overline{K}Q_n$
- **D Flip-Flop:** $Q_{n+1} = D$
- **T Flip-Flop:** $Q_{n+1} = T \oplus Q_n = T\overline{Q}_n + \overline{T}Q_n$

#### Master Flip-Flop Excitation Reference Table:
$$\begin{array}{|c|c|c|c|c|c|c|c|}
\hline
Q_n & Q_{n+1} & S & R & J & K & D & T \\
\hline
0 & 0 & 0 & X & 0 & X & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & X & 1 & 1 \\
1 & 0 & 0 & 1 & X & 1 & 0 & 1 \\
1 & 1 & X & 0 & X & 0 & 1 & 0 \\
\hline
\end{array}$$

---

### UNIT 6: Applications of Sequential Circuits
#### Learning Objectives:
1. Define register operation, bit storage capacity, parallel loading, and serial shifting.
2. Analyze the four fundamental shift register architectures:
   - **SISO (Serial In - Serial Out):** Data loading, shifting, propagation delay, and retrieval time ($N$ clock cycles to load, $N-1$ to shift out).
   - **SIPO (Serial In - Parallel Out):** Serial reception, conversion to spatial bus representation, $N$ clock cycles to load, instantaneous read.
   - **PISO (Parallel In - Serial Out):** Shift/$\overline{\text{Load}}$ control logic, parallel data entry, serial transmission.
   - **PIPO (Parallel In - Parallel Out):** High-speed buffer register, single-clock parallel write and read.
3. Classify binary counters based on clocking mechanisms (Asynchronous Ripple vs. Synchronous Parallel).
4. Analyze Asynchronous (Ripple) UP, DOWN, and UP/DOWN counters using negative-edge-triggered and positive-edge-triggered flip-flops.
5. Design Asynchronous Modulo-$N$ (Truncated) Counters using feedback NAND/AND gates to trigger asynchronous Clear inputs (e.g., Mod-10 Decade/BCD counter).
6. Calculate maximum operating frequency of ripple counters based on cumulative propagation delay ($f_{max} = \frac{1}{N \cdot t_{pd}}$).
7. Formulate and synthesize Synchronous Counters (UP, DOWN, Modulo-$N$) using the complete state machine design flow: State Diagram $\rightarrow$ State Table $\rightarrow$ Flip-Flop Excitation Mapping $\rightarrow$ K-Map Optimization $\rightarrow$ Circuit Synthesis.
8. Design and compare Shift Register Counters:
   - **Ring Counter:** Circular shift ($Q_{last} \rightarrow D_{first}$), self-decoding, $N$ states for $N$ flip-flops.
   - **Johnson (Twisted Ring / Moebius) Counter:** Inverted feedback ($\bar{Q}_{last} \rightarrow D_{first}$), $2N$ states for $N$ flip-flops, 2-input AND decoding.

#### Required Diagrams, State Graphs & Waveforms:
- 4-Bit SISO Shift Register schematic with D Flip-Flops and shifting timing waveforms.
- 4-Bit SIPO Shift Register schematic showing serial input and parallel output lines $Q_0, Q_1, Q_2, Q_3$.
- 4-Bit PISO Shift Register schematic with Shift/$\overline{\text{Load}}$ combinational gating network.
- 4-Bit PIPO Shift Register schematic with common clock and independent parallel inputs/outputs.
- 3-Bit Asynchronous Ripple UP Counter schematic (JK flip-flops in toggle mode, negative-edge clocking from $Q$).
- 3-Bit Ripple UP Counter complete timing diagram showing cumulative propagation delay ripples and glitches.
- 3-Bit Asynchronous Ripple DOWN Counter schematic (clocked from $\bar{Q}$).
- Mod-10 (Decade / BCD) Asynchronous Counter schematic with NAND gate detecting $Q_3Q_1 = 1010_2$ and driving active-low CLR pins.
- 3-Bit Synchronous UP Counter schematic showing parallel clock distribution and carry-forward AND gates.
- Complete State Transition Graph and State Table for 3-bit Synchronous UP/DOWN Counter with mode control $M$.
- 4-Bit Ring Counter schematic, state sequence cycle ($1000 \rightarrow 0100 \rightarrow 0010 \rightarrow 0001 \rightarrow 1000$), and non-overlapping output waveforms.
- 4-Bit Johnson Counter schematic, state sequence cycle (8 states: $0000 \rightarrow 1000 \rightarrow 1100 \rightarrow 1110 \rightarrow 1111 \rightarrow 0111 \rightarrow 0011 \rightarrow 0001 \rightarrow 0000$), and 2-input AND decoding network.

#### Required Summary Comparison Table:
| Parameter | Asynchronous (Ripple) Counter | Synchronous Counter | Ring Counter | Johnson Counter |
| :--- | :--- | :--- | :--- | :--- |
| **Clocking** | Staggered (Output of prev FF drives next) | Simultaneous (Common clock to all FFs) | Simultaneous (Shift register clock) | Simultaneous (Shift register clock) |
| **Operating Speed** | Low ($f_{max} = \frac{1}{N \cdot t_{pd}}$) | High ($f_{max} = \frac{1}{t_{pd} + t_{gate}}$) | Very High | Very High |
| **Number of States ($N$ FFs)** | $2^N$ (Standard) or $< 2^N$ (Mod-$N$) | $2^N$ (Standard) or $< 2^N$ (Mod-$N$) | $N$ States | $2N$ States |
| **Decoding Complexity** | Complex ($N$-input AND gates) | Moderate | None (Outputs inherently decoded) | Simple (2-input AND gates) |
| **Hardware Overhead** | Minimal (Flip-flops only) | High (Requires look-ahead AND gates) | Moderate (Requires preset logic) | Low |
| **Glitches / Hazards** | Present during ripple transitions | Negligible | None | None |

---

## 3. Pedagogical Standard & Worked Example Protocols

To ensure university-level pedagogical excellence, every topic in Chapters 1–6 and Practice/Exam sections must adhere to strict structured protocols:

### A. Protocol for Circuit Analysis & Numerical Problems
$$\begin{aligned}
\textbf{Step 1: Given} &\longrightarrow \text{List all circuit components, voltages, currents, resistances, and boundary conditions.} \\
\textbf{Step 2: Required} &\longrightarrow \text{Explicitly state what quantity or waveform needs to be determined.} \\
\textbf{Step 3: Principle / Formula} &\longrightarrow \text{State the governing law (Ohm's Law, KCL, KVL, Shockley equation, Rectifier formula).} \\
\textbf{Step 4: Substitution} &\longrightarrow \text{Substitute numerical values with explicit SI units into the formula.} \\
\textbf{Step 5: Step-by-Step Calculation} &\longrightarrow \text{Show algebraic manipulation and intermediate arithmetic clearly.} \\
\textbf{Step 6: Final Answer} &\longrightarrow \text{Highlight final numerical value with correct physical units in a box or bold.}
\end{aligned}$$

### B. Protocol for Logic Gate & Combinational Logic Design
$$\begin{aligned}
\textbf{Step 1: Functional Definition} &\longrightarrow \text{State system requirements, input variables, and output variables.} \\
\textbf{Step 2: Truth Table} &\longrightarrow \text{Construct exhaustive table for all } 2^n \text{ combinations.} \\
\textbf{Step 3: Minterm / Maxterm Expression} &\longrightarrow \text{Extract canonical SOP } (\sum m) \text{ or POS } (\prod M) \text{ forms.} \\
\textbf{Step 4: K-Map Simplification} &\longrightarrow \text{Plot onto K-Map, identify prime implicants, and show grouping loops.} \\
\textbf{Step 5: Minimal Boolean Equation} &\longrightarrow \text{Write simplified algebraic expression.} \\
\textbf{Step 6: Logic Circuit Schematic} &\longrightarrow \text{Draw clean gate-level schematic (standard or universal gate implementation).}
\end{aligned}$$

### C. Protocol for Sequential Counter & State Machine Design
$$\begin{aligned}
\textbf{Step 1: State Diagram} &\longrightarrow \text{Draw directed graph of all counting states and reset transitions.} \\
\textbf{Step 2: State Table} &\longrightarrow \text{Tabulate Present State } (Q_n) \text{ vs. Next State } (Q_{n+1}). \\
\textbf{Step 3: Flip-Flop Selection \& Excitation} &\longrightarrow \text{Map required inputs using the chosen Flip-Flop Excitation Table.} \\
\textbf{Step 4: K-Map Minimization} &\longrightarrow \text{Solve K-Maps for each flip-flop control input } (J, K, D, \text{ or } T). \\
\textbf{Step 5: Logic Circuit Diagram} &\longrightarrow \text{Draw complete schematic with clock distribution and combinational gating.} \\
\textbf{Step 6: Self-Correction Verification} &\longrightarrow \text{Verify lock-out behavior for unused states to guarantee self-starting.}
\end{aligned}$$

---

## 4. Chapters 7, 8, and 9 Specifications

### Chapter 7 — Master Revision Sheet
A high-yield, compact reference section summarizing all critical course data:
- **Electrical & Semiconductor Formulas Table:** Complete summary of Ohm's law, Kirchhoff's laws, VDR, CDR, Shockley equation, Rectifier parameters ($\eta, \gamma, \text{PIV}$), BJT current relations ($\alpha, \beta, I_E, I_B, I_C$).
- **Arduino UNO Quick-Reference Guide:** Full pin map, ADC conversion formulas, PWM pins and duty cycle calculation, timer clocks, and electrical ratings.
- **Sensor Comparative Specs Table:** IR, LDR, Ultrasonic HC-SR04, DHT11, DHT22 with operating voltage, sensing range, resolution, output protocol, and typical circuit interface.
- **Number Systems & Binary Codes Reference Sheet:** Base conversion algorithms, 1's/2's complement subtraction rules, BCD, Excess-3 self-complementing property, and Gray code XOR conversion rules.
- **Logic Gates & Boolean Algebra Reference Card:** Complete 7-gate symbol, truth table, and equation summary, Boolean postulates, absorption laws, and De Morgan's theorems.
- **Combinational Block Summary Table:** Adders, subtractors, MUX, DEMUX, decoders, encoders, comparators (Input, Output, Selection/Enable equations).
- **Master Flip-Flop & Counter Reference Sheet:** Latches vs. Flip-flops, Characteristic and Excitation tables for SR, JK, D, T, conversion equations, and Counter taxonomy (Ripple vs. Synchronous vs. Ring vs. Johnson).

### Chapter 8 — Comprehensive Practice Problems with Step-by-Step Solutions
Substantial, multi-tiered practice sets spanning all 6 units:
- **Unit 1 Set:** Multi-loop DC resistor circuit analysis with KVL/KCL, diode circuit operating point calculations, Half-Wave/Bridge rectifier parameter calculations, BJT DC load-line analysis.
- **Unit 2 Set:** Arduino ADC integer-to-voltage conversions, PWM analogWrite duty-cycle output calculations, ultrasonic distance time-of-flight problems, LDR voltage divider calculations.
- **Unit 3 Set:** Fractional number system conversions, 2's complement subtraction with carry analysis, Boolean algebra simplifications, 3-variable and 4-variable K-Map minimizations with Don't Care conditions.
- **Unit 4 Set:** Full Adder/Subtractor synthesis, 8:1 MUX boolean function implementations, priority encoder truth-table problem, 2-bit magnitude comparator synthesis.
- **Unit 5 Set:** Latch race conditions, characteristic equation derivations, master-slave timing problem, complete flip-flop conversions (SR $\rightarrow$ JK, JK $\rightarrow$ D, T $\rightarrow$ D).
- **Unit 6 Set:** Shift register bit-pattern tracing across clock cycles, 3-bit asynchronous down-counter waveform analysis, Mod-12 synchronous counter synthesis with JK flip-flops, Ring vs. Johnson state trace.
- **Complete Solutions:** 100% worked-out solutions with explicit step-by-step arithmetic, K-map tables, circuit schematics, and verification steps.

### Chapter 9 — University-Style Mock Examinations
Two comprehensive, authentic university exam papers structured for a 100-mark final assessment:
- **Mock Examination 1:**
  - **Section A (20 Marks):** 10 Short conceptual questions (2 marks each) testing definitions, basic formulas, gate representations, and pinout facts.
  - **Section B (30 Marks):** 6 Numerical and analytical problems (5 marks each) testing KCL/KVL, 2's complement, K-map simplification, MUX design, and Flip-Flop excitation.
  - **Section C (50 Marks):** 5 Long-form comprehensive questions (10 marks each) testing full rectifier analysis, synchronous counter design, BJT CE characteristics, Arduino ultrasonic interfacing, and flip-flop conversion.
  - **Complete Solution Key:** Fully worked solutions with step-by-step marking rubrics.
- **Mock Examination 2:**
  - **Section A (20 Marks):** 10 High-yield conceptual questions (2 marks each).
  - **Section B (30 Marks):** 6 Analytical and design problems (5 marks each).
  - **Section C (50 Marks):** 5 Comprehensive circuit and sequential design problems (10 marks each).
  - **Complete Solution Key:** Step-by-step answers, circuit diagrams, K-maps, and marking schemes.

---

## 5. Technical Ambiguities & Quality Control Standards

| Area of Potential Ambiguity | Standardized ECE249 Textbook Resolution |
| :--- | :--- |
| **KCL Sign Convention** | Standardize on **Currents entering a node = Positive (+)**, **Currents leaving = Negative (-)**. $\sum I_{in} = \sum I_{out}$. |
| **KVL Sign Convention** | Moving from $-$ to $+$ across a source/element is a **Voltage Rise ($+V$)**; moving from $+$ to $-$ is a **Voltage Drop ($-V$)**. |
| **Silicon vs. Germanium Diode Knee Voltage** | Silicon barrier potential $V_k = 0.7\text{ V}$; Germanium barrier potential $V_k = 0.3\text{ V}$. Default to Silicon unless Germanium is explicitly specified. |
| **Rectifier Diode Model** | State whether ideal diode ($V_{on} = 0\text{ V}$) or practical silicon diode ($V_{on} = 0.7\text{ V}$) is used in calculations. Peak load voltage $V_{L,peak} = V_m - 2V_D$ for bridge rectifier with practical diodes. |
| **Arduino ADC Quantization** | Arduino uses a 10-bit successive approximation ADC with $2^{10} = 1024$ quantization levels ($0$ to $1023$). Voltage per step $= \frac{5.0\text{ V}}{1024} = 4.8828\text{ mV}$. Total range mapped is 0 to 1023. |
| **PWM Frequency on Arduino UNO** | Pins 5 and 6 run at $\approx 980\text{ Hz}$ (Timer 0); Pins 3, 9, 10, 11 run at $\approx 490\text{ Hz}$ (Timers 1 and 2). 8-bit resolution ($0\text{--}255$). |
| **Speed of Sound in Air** | Standard acoustic velocity at room temperature ($20^\circ\text{C}$) is $v = 343\text{ m/s} = 0.0343\text{ cm/}\mu\text{s}$. |
| **2's Complement Zero Representation** | 2's complement has a single representation for zero ($0000_2$), unlike 1's complement which has $+0$ ($0000_2$) and $-0$ ($1111_2$). Range for $n$ bits is $-2^{n-1}$ to $+2^{n-1}-1$. |
| **K-Map Cell Numbering** | Use standard Gray code cell indexing. For 4-variable $AB \setminus CD$, row order is $00, 01, 11, 10$ ($0, 1, 3, 2$) and column order is $00, 01, 11, 10$ ($0, 1, 3, 2$). Row 3 corresponds to $m_{12}, m_{13}, m_{15}, m_{14}$, and Row 4 corresponds to $m_8, m_9, m_{11}, m_{10}$. |
| **Encoder Priority Assignment** | In Priority Encoders, higher index input (e.g., $D_7$ or $D_3$) has highest priority unless explicitly specified otherwise. Include Valid flag $V$. |
| **Flip-Flop Clock Triggering** | Asynchronous ripple counters: explicitly note whether flip-flops are negative-edge triggered ($\downarrow$) or positive-edge triggered ($\uparrow$) to avoid inverted counting directions. |
| **Race-Around Condition Criteria** | Clearly state the double condition: $J=K=1$, clock pulse width $t_p > t_{pd}$ (propagation delay of the flip-flop). Master-Slave eliminates this because data transfer occurs on the falling edge without feedback during clock low. |
| **Ring vs. Johnson Modulus** | $N$ flip-flops in a Ring Counter yield Mod-$N$ ($N$ states). $N$ flip-flops in a Johnson (Twisted Ring) Counter yield Mod-$2N$ ($2N$ states). |

---

## 6. Phase 2 Production & File Structure Roadmap

```
ECE249/
├── CONTENT_BLUEPRINT.md                                 # [Completed Phase 1 Master Blueprint]
├── README.md                                           # Project documentation and build guide
├── Makefile                                            # Compilation pipeline for pdflatex/latexmk
├── style.sty                                           # Complete LaTeX package (TikZ, Circuitikz, tcolorbox, colors)
├── main.tex                                            # Master LaTeX document
├── chapters/
│   ├── chapter-01-electrical-laws-semiconductors.tex   # Unit 1 Full Textbook Chapter
│   ├── chapter-02-arduino-sensors.tex                  # Unit 2 Full Textbook Chapter
│   ├── chapter-03-number-systems-logic-gates.tex       # Unit 3 Full Textbook Chapter
│   ├── chapter-04-combinational-logic.tex              # Unit 4 Full Textbook Chapter
│   ├── chapter-05-sequential-logic.tex                 # Unit 5 Full Textbook Chapter
│   ├── chapter-06-sequential-applications.tex          # Unit 6 Full Textbook Chapter
│   ├── chapter-07-master-revision-sheet.tex            # Chapter 7 High-Yield Master Revision Sheet
│   ├── chapter-08-practice-problems.tex                # Chapter 8 Extensive Practice Problems & Solutions
│   └── chapter-09-mock-examinations.tex                # Chapter 9 Two Complete Mock Exams & Rubrics
├── figures/                                            # Directory for standalone TikZ/schematics
├── tables/                                             # Directory for standalone tables
└── examples/                                           # Directory for standalone worked problems
```

---
*End of Phase 1 Content Blueprint. Ready for immediate Phase 2 Textbook Production and Compilation.*
