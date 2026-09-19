# ECE279: Basic Electrical and Electronics Engineering (Practical & Viva Guide)

## Comprehensive University Laboratory & Exam Study Guide

**Author**: University Engineering Open Courseware Initiative  
**License**: CC BY-NC-SA 4.0 (Text & Educational Material) / MIT License (Build Code)  
**Target Class**: First-Year Undergraduate Engineering Students (ECE, CSE, IT, EE, Robotics)

---

### Course Practicals & Syllabus Architecture
- **Practical 1: The Electronics Expedition**  
  Component Identification (Active vs. Passive), Resistor Color Coding ($4\text{-Band}$ system), Breadboard architecture, Input sources (DC Supply, Function Generator), and Measuring Instruments (DMM, CRO/DSO).
- **Practical 2: KVL Voltage Hunt**  
  Kirchhoff's Voltage Law (KVL) verification, T-Network mesh circuit analysis, sign conventions, voltage drop calculations, and percentage error analysis.
- **Practical 3: Diode Voltage Quest**  
  PN Junction Diode (1N4007) V-I characteristics in Forward and Reverse Bias, Knee/Cut-in voltage determination ($0.7\text{V}$ Si), Static DC resistance ($R_{dc}$), and Dynamic AC resistance ($r_{ac}$) calculations.
- **Practical 4: Universal Gate Adventure**  
  Design and verification of basic logic gates (NOT, AND, OR) using IC 7400 (NAND) and IC 7402 (NOR), pinout configuration differences, and De Morgan's Law realizations.
- **Practical 5: Adder Chronicles**  
  Combinational arithmetic logic: Half Adder (XOR 7486, AND 7408) and Full Adder (two Half Adders + OR 7432), Boolean expression minterm derivations, and 8-input state verification.
- **Practical 6: Flip-Flop Warriors: NAND Edition**  
  Sequential logic: Level-triggered JK Flip-Flop using IC 7400 (cross-coupled NAND latch) and IC 7410 (triple 3-input NAND steering gates), state table analysis, and Race-Around condition evaluation.
- **Practical 7: Master Viva Voce & Exam Revision Guide**  
  Source material truncation notice & comprehensive 40+ Question Viva Voce revision bank across all practical modules.

---

### Compilation Instructions

To compile the textbook PDF using `make`:

```bash
make clean
make
```

The compiled PDF artifact will be generated at `ECE279/main.pdf`.
