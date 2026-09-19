# ECE249: Digital Electronics, Electrical Fundamentals & Microcontroller Interfacing
## Comprehensive University Study & Practice Guide

**Author**: University Engineering Open Courseware Initiative  
**License**: CC BY-NC-SA 4.0 (Text & Educational Material) / MIT License (Build Code)  
**Target Class**: Undergraduate Engineering Students (ECE, CSE, IT, EE, Robotics)

---

### Course Modules & Syllabus Architecture
- **Unit 1: Fundamentals of Electrical Laws, Semiconductor Devices and its Applications**
  - DC Circuit Analysis (Ohm's Law, KCL, KVL, Voltage & Current Division Rules)
  - Semiconductor Physics & Band Theory ($E_g$, Intrinsic vs. Extrinsic N/P Doping)
  - PN Junction Diodes (Biasing, V-I Characteristics, Zener/Avalanche Breakdown)
  - Diode Rectification (Half-Wave, Full-Wave Center-Tapped, Bridge Rectifiers)
  - BJT Fundamentals (Construction, Modes of Operation, CE Characteristics, Gain $\alpha$ and $\beta$)
- **Unit 2: Introduction of Arduino, Signals, and Sensor Interfacing**
  - Analog vs. Digital Signals (Continuity, Noise Immunity, ADC & PWM Concepts)
  - Arduino UNO Board Architecture (ATmega328P, Power, Pinout Subsystems)
  - Sensors & Transducers (Active IR Module, CdS LDR Photoresistor, Ultrasonic Rangefinder HC-SR04, DHT11/22 Temperature & Humidity Sensors)
- **Unit 3: Number Systems, Binary Codes, Logic Gates & Karnaugh Maps**
  - Positional Number Systems (Binary, Octal, Decimal, Hexadecimal Base Conversions)
  - Binary Codes (BCD 8421, Excess-3 Self-Complementing Code, Gray Unit-Distance Code)
  - Complements & Binary Arithmetic (1's & 2's Complements, Subtraction via 2's Complement)
  - Logic Gates (Basic, Universal NAND/NOR Realizations, Special XOR/XNOR Gates)
  - Boolean Algebra Postulates, Absorption Laws, De Morgan's Theorems
  - Canonical SOP ($\sum m$) & POS ($\prod M$) Forms
  - Karnaugh Maps (2, 3, 4-Variable K-Maps, Gray Code Cell Indexing, Don't-Care Optimization)
- **Unit 4: Combinational Logic Circuits**
  - Arithmetic Adders & Subtractors (Half/Full Adders, Half/Full Subtractors, Two-Half-Adder Implementations)
  - Multiplexers (2:1, 4:1, 8:1 MUX, Function Synthesis)
  - De-multiplexers (1:2, 1:4, 1:8 DEMUX)
  - Binary Decoders (2-to-4, 3-to-8 with Active-Low/Active-High Enables)
  - Binary Encoders & Priority Encoders
  - Digital Magnitude Comparators (1-Bit and 2-Bit Identity & Inequality Circuits)
- **Unit 5: Introduction to Sequential Logic Circuits**
  - Sequential vs. Combinational Fundamentals (Memory, Feedback, State Variables)
  - Bistable Latches (NOR SR Latch, NAND $\bar{S}\bar{R}$ Latch, Gated D Latch)
  - Edge-Triggered Flip-Flops (SR, JK, D, T: Truth Tables, Characteristic & Excitation Tables)
  - Race-Around Condition in Level-Triggered JK Flip-Flops
  - Master-Slave JK Flip-Flop Architecture (Glitch Elimination)
  - Systematic 5-Step Flip-Flop Conversion Methodology
- **Unit 6: Applications of Sequential Circuits**
  - Shift Registers (SISO, SIPO, PISO, PIPO Topologies & Timing Diagrams)
  - Asynchronous (Ripple) Counters (UP, DOWN, Modulo-$N$ Truncated Reset Counters)
  - Synchronous Counters (Parallel Clocking, UP/DOWN/Mod-$N$ State Machine Synthesis)
  - Shift Register Counters (Ring Counter, Johnson Twisted-Ring Counter)
- **Chapter 7: Master Revision Sheet & Formula Reference**
- **Chapter 8: Comprehensive Solved Practice Problems (All Units)**
- **Chapter 9: University-Style Mock Examinations (Two 100-Mark Papers with Full Solutions)**

---

### Compilation Instructions

To compile the textbook PDF using `make`:

```bash
make clean
make
```
