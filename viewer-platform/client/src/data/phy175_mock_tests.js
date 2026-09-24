/**
 * Official PHY175: Physics Practice & Formulae Midterm Mock Examination Suite
 * Contains 5 Full-Length 30-Question Tests (150 Questions Total)
 * Strictly covers Units 1-3: Solid State, Semiconductor Diodes/BJTs, Logic Gates
 * Verified single-correct answers with balanced distractor lengths
 */

export const PHY175_MOCK_TESTS = [
  {
    "id": "phy175-midterm-paper-1",
    "code": "PHY175-MIDTERM-1",
    "title": "Midterm Examination • Paper 1 (Official University Model)",
    "courseCode": "PHY175",
    "courseName": "Physics Practice & Formulae",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Solid State Physics",
      "Hall Effect",
      "Rectifiers & Filters",
      "BJT Electronics",
      "Logic Gates & Number Systems"
    ],
    "description": "Comprehensive midterm paper testing Fermi level, Hall voltage derivations, full-wave bridge rectifier ripple factor, BJT alpha/beta relationships, and 2's complement binary arithmetic.",
    "questions": [
      {
        "id": 1,
        "question": "Fermi energy (E_F) at absolute zero temperature (0 K) represents:",
        "options": [
          "The average thermal energy of lattice ions (in an ideal homogeneous medium)",
          "The minimum energy of the valence band (under steady-state operating conditions)",
          "The energy required to break a covalent bond (as determined by Maxwell boundary constraints)",
          "The maximum kinetic energy possessed by electrons in a conduction band at 0 K"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "At T = 0 K, all electronic states up to E_F are completely filled with probability f(E) = 1.",
            "All states above E_F are completely empty with f(E) = 0.",
            "Thus, E_F at 0 K is the highest occupied energy level."
          ],
          "keyConcept": "Fermi energy at 0 K is the maximum occupied electron energy level."
        }
      },
      {
        "id": 2,
        "question": "A 3D free electron gas at 0 K has electron concentration n₁. If the concentration is increased to 8n₁, the Fermi energy becomes:",
        "options": [
          "4 E_F1",
          "2 E_F1",
          "8 E_F1",
          "16 E_F1"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Fermi energy formula: E_F = (ℏ² / 2m) (3π² n)^(2/3).",
            "E_F is proportional to n^(2/3).",
            "E_F2 / E_F1 = (n₂ / n₁)^(2/3) = (8)^(2/3) = (2³)^(2/3) = 2² = 4.",
            "Therefore, E_F2 = 4 E_F1."
          ],
          "keyConcept": "E_F ∝ n^(2/3). An 8-fold density increase quadruples Fermi energy."
        }
      },
      {
        "id": 3,
        "question": "What is the primary difference between a Direct and an Indirect band gap semiconductor?",
        "options": [
          "Indirect band gap semiconductors have higher optical emission efficiency (as determined by Maxwell boundary constraints)",
          "Direct band gap semiconductors cannot emit light (across all standard operating temperatures)",
          "There is no difference in momentum (governed by linear superposition principles)",
          "In direct band gap, the conduction band minimum and valence band maximum occur at the same crystal momentum (k = 0), allowing efficient photon emission"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Direct band gap (e.g. GaAs): Electron drops directly without phonon assistance (conservation of momentum). Ideal for LEDs and lasers.",
            "Indirect band gap (e.g. Si, Ge): Requires a phonon (lattice vibration) to conserve momentum, making radiative recombination inefficient."
          ],
          "keyConcept": "Direct bandgap enables direct radiative recombination without phonons."
        }
      },
      {
        "id": 4,
        "question": "The sign of the Hall coefficient (R_H) in a semiconductor specimen is significant because it directly reveals:",
        "options": [
          "The type of majority charge carriers (negative for electrons, positive for holes)",
          "The temperature of the specimen (governed by linear superposition principles)",
          "The crystal orientation only (independent of external field perturbations)",
          "The magnitude of the applied magnetic field (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Hall Effect",
        "explanation": {
          "steps": [
            "Hall coefficient: R_H = 1 / (n q).",
            "For electrons (q = -e), R_H is negative (N-type semiconductor).",
            "For holes (q = +e), R_H is positive (P-type semiconductor)."
          ],
          "keyConcept": "Sign of R_H determines N-type vs P-type carrier nature."
        }
      },
      {
        "id": 5,
        "question": "In an intrinsic semiconductor, electron mobility is 3 times hole mobility (μ_e = 3 μ_h). What percentage of total electrical conductivity is contributed by electrons?",
        "options": [
          "25%",
          "75%",
          "100%",
          "50%"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Total conductivity σ = n_i e (μ_e + μ_h).",
            "Conductivity due to electrons σ_e = n_i e μ_e = n_i e (3 μ_h).",
            "Fraction = σ_e / σ = (3 μ_h) / (3 μ_h + μ_h) = 3/4 = 0.75 = 75%."
          ],
          "keyConcept": "Electrons contribute 75% of total conductivity when μ_e = 3 μ_h."
        }
      },
      {
        "id": 6,
        "question": "A full-wave bridge rectifier is supplied with a 50 Hz AC mains sinusoidal input. What is the fundamental ripple frequency of the output DC voltage across the load?",
        "options": [
          "50 Hz",
          "100 Hz",
          "200 Hz",
          "25 Hz"
        ],
        "correctIndex": 1,
        "topic": "Rectifiers & Filters",
        "explanation": {
          "steps": [
            "In a full-wave rectifier, both positive and negative half-cycles are rectified into the same polarity.",
            "Thus, output pulses appear twice per AC cycle: f_ripple = 2 × f_in = 2 × 50 Hz = 100 Hz."
          ],
          "keyConcept": "Full-wave ripple frequency = 2 × input frequency."
        }
      },
      {
        "id": 7,
        "question": "What is the ripple factor (r) of an ideal full-wave rectifier without a filter capacitor?",
        "options": [
          "1.21",
          "0.05",
          "0.482",
          "0.01"
        ],
        "correctIndex": 2,
        "topic": "Rectifiers & Filters",
        "explanation": {
          "steps": [
            "Ripple factor formula: r = √((V_rms / V_dc)² - 1).",
            "For half-wave: r = 1.21.",
            "For full-wave: V_rms = V_m / √2, V_dc = 2 V_m / π ⇒ r = √((π / 2√2)² - 1) = √(1.2337 - 1) ≈ 0.482."
          ],
          "keyConcept": "Full-wave ripple factor = 0.482 (48.2%)."
        }
      },
      {
        "id": 8,
        "question": "What is the 8-bit Two's Complement representation of decimal integer -25?",
        "options": [
          "00011001",
          "11100110",
          "10011001",
          "11100111"
        ],
        "correctIndex": 3,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "1. Decimal +25 in 8-bit binary: 00011001.",
            "2. One's complement (invert bits): 11100110.",
            "3. Two's complement (add 1): 11100110 + 1 = 11100111."
          ],
          "keyConcept": "Two's complement = One's complement + 1."
        }
      },
      {
        "id": 9,
        "question": "According to De Morgan's First Law of Boolean algebra, the complement of a sum equals:",
        "options": [
          "The sum of the complements: (A · B)' = A' + B'",
          "The product of the complements: (A + B)' = A' · B'",
          "A + B (governed by linear superposition principles)",
          "A · B (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "De Morgan's 1st theorem: (A + B)' = A' · B'. (NOR is equivalent to bubbled AND).",
            "De Morgan's 2nd theorem: (A · B)' = A' + B'. (NAND is equivalent to bubbled OR)."
          ],
          "keyConcept": "NOR = Bubbled AND: (A + B)' = A' · B'."
        }
      },
      {
        "id": 10,
        "question": "Which logic gate produces a HIGH (1) output if and only if an ODD number of its binary inputs are HIGH (1)?",
        "options": [
          "XOR (Exclusive-OR) Gate",
          "AND Gate",
          "XNOR Gate",
          "OR Gate (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "The XOR gate (modulo-2 adder) outputs 1 when the inputs differ (for 2 inputs: 0⊕1 = 1, 1⊕0 = 1, but 0⊕0 = 0, 1⊕1 = 0).",
            "In multi-input XOR gates, output is HIGH whenever parity is odd."
          ],
          "keyConcept": "XOR gate is an odd parity detector."
        }
      },
      {
        "id": 11,
        "question": "Why are NAND and NOR gates designated as \"Universal Logic Gates\"?",
        "options": [
          "Because they have infinite input resistance (governed by linear superposition principles)",
          "Because they operate on AC voltages (independent of external field perturbations)",
          "Because any Boolean function and all basic gates (AND, OR, NOT) can be implemented using exclusively NAND or exclusively NOR gates",
          "Because they consume zero propagation delay (under steady-state operating conditions)"
        ],
        "correctIndex": 2,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "Connecting both inputs of a NAND gate together creates a NOT gate.",
            "Followed by another NAND yields an AND gate.",
            "De Morgan's inversion creates an OR gate.",
            "Hence, NAND and NOR gates are universal."
          ],
          "keyConcept": "Universal gates can synthesize all Boolean logic gates."
        }
      },
      {
        "id": 12,
        "question": "In a Bipolar Junction Transistor (BJT), what is the relationship between base-to-collector current gain β and emitter-to-collector current gain α?",
        "options": [
          "β = α / (1 + α)",
          "α = β / (1 - β)",
          "α = 1 + β",
          "β = α / (1 - α)"
        ],
        "correctIndex": 3,
        "topic": "BJT Electronics",
        "explanation": {
          "steps": [
            "Emitter current I_E = I_B + I_C.",
            "By definition: α = I_C / I_E and β = I_C / I_B.",
            "Dividing I_E by I_C: 1/α = (1/β) + 1 = (1 + β) / β.",
            "Inverting yields α = β / (1 + β), and solving for β gives β = α / (1 - α)."
          ],
          "keyConcept": "β = α / (1 - α) and α = β / (1 + β)."
        }
      },
      {
        "id": 13,
        "question": "If a transistor has α = 0.98, what is its corresponding Common Emitter current gain β?",
        "options": [
          "49",
          "100",
          "98",
          "50"
        ],
        "correctIndex": 0,
        "topic": "BJT Electronics",
        "explanation": {
          "steps": [
            "β = α / (1 - α) = 0.98 / (1 - 0.98) = 0.98 / 0.02 = 98 / 2 = 49."
          ],
          "keyConcept": "When α = 0.98, β = 49."
        }
      },
      {
        "id": 14,
        "question": "In a Common Emitter (CE) BJT amplifier, what is the phase shift between the input AC base signal and the output AC collector voltage?",
        "options": [
          "270°",
          "180° (Out of phase)",
          "90° (across all standard operating temperatures)",
          "0° (In phase)"
        ],
        "correctIndex": 1,
        "topic": "BJT Electronics",
        "explanation": {
          "steps": [
            "As input base voltage increases, base current increases, which increases collector current I_C.",
            "The voltage drop across collector load resistor (I_C R_C) increases, causing output voltage V_CE = V_CC - I_C R_C to drop.",
            "This introduces a 180° phase inversion."
          ],
          "keyConcept": "CE amplifier provides 180° phase inversion."
        }
      },
      {
        "id": 15,
        "question": "A rectangular copper strip of thickness t = 0.1 mm carries current I = 10 A in magnetic field B = 1.2 T. If electron density n = 8.5 × 10²⁸ m⁻³, the measured Hall voltage V_H is:",
        "options": [
          "1.24 V",
          "88.2 mV",
          "8.82 μV",
          "0.55 μV"
        ],
        "correctIndex": 2,
        "topic": "Hall Effect",
        "explanation": {
          "steps": [
            "Formula: V_H = (I B) / (n q t)",
            "Numerator = 10 A × 1.2 T = 12.",
            "Denominator = (8.5 × 10²⁸) × (1.602 × 10⁻¹⁹ C) × (0.1 × 10⁻³ m)",
            "Denominator = 1.3617 × 10⁶.",
            "V_H = 12 / (1.3617 × 10⁶) = 8.812 × 10⁻⁶ V ≈ 8.82 μV."
          ],
          "keyConcept": "V_H = (I B) / (n q t)."
        }
      },
      {
        "id": 16,
        "question": "Convert hexadecimal (3A7.C)₁₆ into decimal representation:",
        "options": [
          "855.25",
          "935.75",
          "920.50",
          "1024.75"
        ],
        "correctIndex": 1,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "Integer part: 3 × 16² + A(10) × 16¹ + 7 × 16⁰",
            "= 3(256) + 10(16) + 7 = 768 + 160 + 7 = 935.",
            "Fractional part: C(12) × 16⁻¹ = 12 / 16 = 3 / 4 = 0.75.",
            "Total decimal = 935.75."
          ],
          "keyConcept": "Hex to decimal positional evaluation."
        }
      },
      {
        "id": 17,
        "question": "The minimum number of 2-input NAND gates required to construct a 2-input XOR gate is:",
        "options": [
          "3",
          "5",
          "6",
          "4"
        ],
        "correctIndex": 3,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "A XOR B = A'B + AB' = (A + B)(A' + B') = (A(AB)')' · (B(AB)')'.",
            "This standard optimal realization requires exactly 4 NAND gates."
          ],
          "keyConcept": "Exactly 4 NAND gates construct a 2-input XOR gate."
        }
      },
      {
        "id": 18,
        "question": "In a 4-variable Karnaugh Map (K-map), grouping an isolated block of 8 adjacent 1s (an Octet) eliminates how many variables?",
        "options": [
          "3 variables",
          "1 variable",
          "2 variables",
          "4 variables"
        ],
        "correctIndex": 0,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "Grouping 2^k cells eliminates k variables.",
            "Pair (2 cells) eliminates 1 variable (2¹).",
            "Quad (4 cells) eliminates 2 variables (2²).",
            "Octet (8 cells = 2³) eliminates 3 variables, leaving a single literal."
          ],
          "keyConcept": "An octet (8 cells) eliminates 3 Boolean variables."
        }
      },
      {
        "id": 19,
        "question": "What is the Peak Inverse Voltage (PIV) rating required for each diode in a Center-Tapped full-wave rectifier delivering peak secondary voltage V_m?",
        "options": [
          "V_m",
          "V_m / 2",
          "√2 V_m",
          "2 V_m"
        ],
        "correctIndex": 3,
        "topic": "Rectifiers & Filters",
        "explanation": {
          "steps": [
            "In a center-tapped transformer rectifier, during the reverse half-cycle, the non-conducting diode experiences the full secondary winding voltage across both halves: PIV = 2 V_m.",
            "In contrast, a Bridge rectifier requires PIV = V_m."
          ],
          "keyConcept": "Center-tapped rectifier PIV = 2 V_m; Bridge rectifier PIV = V_m."
        }
      },
      {
        "id": 20,
        "question": "Which capacitor filter parameter directly controls the peak-to-peak ripple voltage V_r in a full-wave power supply?",
        "options": [
          "V_r = I_dc / (2 f C)",
          "V_r = I_dc · 2 f C",
          "V_r = f C / (2 I_dc)",
          "V_r = 2 f C / I_dc"
        ],
        "correctIndex": 0,
        "topic": "Rectifiers & Filters",
        "explanation": {
          "steps": [
            "Ripple voltage V_r(pp) is given by: V_r = I_dc / (2 f C) = V_dc / (2 f R_L C).",
            "Increasing filter capacitance C or frequency f reduces ripple voltage."
          ],
          "keyConcept": "V_r = I_dc / (2 f C)."
        }
      },
      {
        "id": 21,
        "question": "In semiconductor physics, what is the relationship between the intrinsic carrier concentration n_i, electron concentration n, and hole concentration p under thermal equilibrium?",
        "options": [
          "n / p = n_i²",
          "n · p = 2 n_i",
          "n · p = n_i²",
          "n + p = n_i"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "By the Mass Action Law, the product of electron and hole concentrations in a semiconductor under thermal equilibrium is constant at a given temperature: n · p = n_i²."
          ],
          "keyConcept": "Mass Action Law: n · p = n_i²."
        }
      },
      {
        "id": 22,
        "question": "The Fermi-Dirac distribution function f(E) gives the probability that an electronic state at energy E is occupied. At temperature T > 0 K, when energy E = E_F:",
        "options": [
          "f(E) = 1.0",
          "f(E) = 0",
          "f(E) = 0.5 (50%)",
          "f(E) = 0.707"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "f(E) = 1 / [1 + e^((E - E_F) / (k_B T))].",
            "When E = E_F, the exponent is e^0 = 1.",
            "f(E_F) = 1 / (1 + 1) = 1/2 = 0.5."
          ],
          "keyConcept": "At E = E_F, occupation probability is exactly 50% for T > 0 K."
        }
      },
      {
        "id": 23,
        "question": "In Boolean algebra, what is the simplified result of the expression: A + A' B?",
        "options": [
          "A · B",
          "A + B",
          "A",
          "B"
        ],
        "correctIndex": 1,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "By the distributive law: A + A' B = (A + A')(A + B).",
            "Since A + A' = 1, this simplifies to: 1 · (A + B) = A + B."
          ],
          "keyConcept": "Redundancy law: A + A'B = A + B."
        }
      },
      {
        "id": 24,
        "question": "What is the binary product of binary numbers 1011₂ (11) and 101₂ (5)?",
        "options": [
          "110001₂",
          "111111₂",
          "110111₂ (55)",
          "101101₂"
        ],
        "correctIndex": 2,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "1011₂ × 101₂:",
            "  1011",
            "+ 00000",
            "+ 101100",
            "= 110111₂ (which equals 32 + 16 + 4 + 2 + 1 = 55 in decimal)."
          ],
          "keyConcept": "Binary multiplication: 11 × 5 = 55 = 110111₂."
        }
      },
      {
        "id": 25,
        "question": "Which diode breakdown mechanism occurs in heavily doped PN junctions with narrow depletion layers under reverse electric fields of ~10⁶ V/m?",
        "options": [
          "Avalanche breakdown (impact ionization)",
          "Punch-through",
          "Thermal runaway",
          "Zener breakdown (quantum tunneling)"
        ],
        "correctIndex": 3,
        "topic": "Electronic Devices",
        "explanation": {
          "steps": [
            "Heavy doping makes the depletion layer ultra-thin (< 10 nm).",
            "Strong electric fields pull valence electrons directly across the forbidden gap via quantum mechanical tunneling (Zener effect, typically < 5-6 V)."
          ],
          "keyConcept": "Zener breakdown occurs via tunneling in heavily doped junctions."
        }
      },
      {
        "id": 26,
        "question": "In a BJT operating in the active amplification region, the emitter-base junction and collector-base junction are biased respectively as:",
        "options": [
          "Both Forward Biased",
          "Emitter-Base: Reverse Biased; Collector-Base: Forward Biased",
          "Emitter-Base: Forward Biased; Collector-Base: Reverse Biased",
          "Both Reverse Biased"
        ],
        "correctIndex": 2,
        "topic": "BJT Electronics",
        "explanation": {
          "steps": [
            "Active mode: EBJ Forward biased (injects carriers from emitter into thin base), CBJ Reverse biased (sweeps carriers across into collector)."
          ],
          "keyConcept": "Active Region: Emitter-Base is Forward Biased, Collector-Base is Reverse Biased."
        }
      },
      {
        "id": 27,
        "question": "The Gray Code representation of binary number 1011₂ is:",
        "options": [
          "1110₂",
          "1001₂",
          "1101₂",
          "1111₂"
        ],
        "correctIndex": 0,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "Gray code conversion algorithm:",
            "Most significant bit remains same: G₃ = B₃ = 1.",
            "G₂ = B₃ ⊕ B₂ = 1 ⊕ 0 = 1.",
            "G₁ = B₂ ⊕ B₁ = 0 ⊕ 1 = 1.",
            "G₀ = B₁ ⊕ B₀ = 1 ⊕ 1 = 0.",
            "Resulting Gray code: 1110₂."
          ],
          "keyConcept": "Binary to Gray: G_i = B_(i+1) ⊕ B_i."
        }
      },
      {
        "id": 28,
        "question": "What is the ripple frequency of a 3-phase full-wave bridge rectifier operating on a 50 Hz power supply?",
        "options": [
          "600 Hz",
          "150 Hz",
          "100 Hz",
          "300 Hz"
        ],
        "correctIndex": 3,
        "topic": "Rectifiers & Filters",
        "explanation": {
          "steps": [
            "A 3-phase full-wave bridge rectifier (6-pulse converter) produces 6 DC pulses per AC cycle.",
            "f_ripple = 6 × 50 Hz = 300 Hz."
          ],
          "keyConcept": "3-phase bridge rectifier ripple frequency = 6 × f_supply = 300 Hz."
        }
      },
      {
        "id": 29,
        "question": "The Hall mobility (μ_H) of charge carriers is related to the Hall coefficient (R_H) and conductivity (σ) by:",
        "options": [
          "μ_H = R_H / σ",
          "μ_H = R_H · σ",
          "μ_H = σ / R_H",
          "μ_H = √(R_H · σ)"
        ],
        "correctIndex": 1,
        "topic": "Hall Effect",
        "explanation": {
          "steps": [
            "Since R_H = 1 / (n e) and σ = n e μ, multiplying gives R_H · σ = [1 / (n e)] · (n e μ) = μ_H."
          ],
          "keyConcept": "Hall mobility μ_H = R_H · σ."
        }
      },
      {
        "id": 30,
        "question": "In a digital system, a \"Don't Care\" condition (indicated by X) in a K-map:",
        "options": [
          "Causes an invalid hardware fault (independent of external field perturbations)",
          "Must always be set to 0 (in an ideal homogeneous medium)",
          "Can be treated as either 0 or 1, whichever yields a larger group and simpler minimal expression",
          "Must always be set to 1 (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 2,
        "topic": "Logic Gates & Number Systems",
        "explanation": {
          "steps": [
            "Don't-care input combinations never occur in normal operation, so the designer can assign 1 or 0 to enlarge prime implicants and minimize gate count."
          ],
          "keyConcept": "Don't cares can be grouped as 1 or ignored as 0 for maximal simplification."
        }
      }
    ]
  },
  {
    "id": "phy175-midterm-paper-2",
    "code": "PHY175-PAPER-B",
    "title": "Midterm Examination • Paper 2 (Solid State & Carrier Dynamics)",
    "courseCode": "PHY175",
    "courseName": "Physics Practice & Formulae",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Solid State Physics",
      "Fermi Energy",
      "Diodes & Transistors",
      "Digital Logic"
    ],
    "description": "In-depth testing of Fermi-Dirac distribution, carrier density, drift mobility, and Hall effect calculations.",
    "questions": [
      {
        "id": 1,
        "question": "Effective mass is used to describe how a charge carrier responds to:",
        "options": [
          "Nuclear force inside an atom",
          "Pressure in a vacuum",
          "Gravity outside the material",
          "An external force in a crystal"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Effective mass accounts for crystal lattice periodic potential response."
          ],
          "keyConcept": "Effective mass accounts for crystal lattice periodic potential response."
        }
      },
      {
        "id": 2,
        "question": "The Hall effect is the development of a transverse voltage when a current-carrying material is placed in a:",
        "options": [
          "Uniform gravitational field",
          "Perpendicular magnetic field",
          "Parallel electric field",
          "Longitudinal thermal field"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Transverse Lorentz force from perpendicular $\\vec{B}$ field produces $V_H$."
          ],
          "keyConcept": "Transverse Lorentz force from perpendicular $\\vec{B}$ field produces $V_H$."
        }
      },
      {
        "id": 3,
        "question": "For a material with one type of carrier having concentration $n$ and charge $q$, the Hall coefficient is:",
        "options": [
          "$R_H = q/n$",
          "$R_H = 1/(nq)$",
          "$R_H = n/q$",
          "$R_H = nq$"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "By definition, $R_H = E_y / (J_x B_z) = 1/(nq)$."
          ],
          "keyConcept": "By definition, $R_H = E_y / (J_x B_z) = 1/(nq)$."
        }
      },
      {
        "id": 4,
        "question": "A pure semiconductor without intentionally added impurities is called:",
        "options": [
          "An ionic insulator",
          "An intrinsic semiconductor",
          "A metallic conductor",
          "An extrinsic semiconductor"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Undoped pure semiconductor material is intrinsic."
          ],
          "keyConcept": "Undoped pure semiconductor material is intrinsic."
        }
      },
      {
        "id": 5,
        "question": "Adding a pentavalent impurity to silicon usually produces:",
        "options": [
          "A perfect insulator",
          "An n-type semiconductor",
          "An p-type semiconductor",
          "An intrinsic semiconductor"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Pentavalent atoms donate extra electrons, forming n-type."
          ],
          "keyConcept": "Pentavalent atoms donate extra electrons, forming n-type."
        }
      },
      {
        "id": 6,
        "question": "In an intrinsic semiconductor, the Fermi level lies approximately:",
        "options": [
          "At the bottom of the valence band",
          "At the top of the conduction band",
          "Far above the conduction band",
          "Near the middle of the band gap"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Equal electron and hole densities position $E_i$ near midgap."
          ],
          "keyConcept": "Equal electron and hole densities position $E_i$ near midgap."
        }
      },
      {
        "id": 7,
        "question": "In an n-type semiconductor, the Fermi level shifts closer to the:",
        "options": [
          "Middle of the nucleus",
          "Bottom of the forbidden band",
          "Conduction band",
          "Valence band"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Donor electrons populate near $E_C$, shifting $E_F$ upwards."
          ],
          "keyConcept": "Donor electrons populate near $E_C$, shifting $E_F$ upwards."
        }
      },
      {
        "id": 8,
        "question": "In a direct band gap semiconductor, an electron can recombine with a hole without requiring a change in:",
        "options": [
          "Carrier number",
          "Electron energy",
          "Electric charge",
          "Crystal momentum"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Extrema align at $\\vec{k}=0$, conserving momentum without phonons."
          ],
          "keyConcept": "Extrema align at $\\vec{k}=0$, conserving momentum without phonons."
        }
      },
      {
        "id": 9,
        "question": "Which material is commonly classified as an indirect band gap semiconductor?",
        "options": [
          "Gallium arsenide",
          "Gallium nitride",
          "Indium phosphide",
          "Silicon"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Silicon and Germanium have indirect band gaps."
          ],
          "keyConcept": "Silicon and Germanium have indirect band gaps."
        }
      },
      {
        "id": 10,
        "question": "A solar cell converts light energy directly into electrical energy through the:",
        "options": [
          "Photovoltaic effect",
          "Hall effect",
          "Piezoelectric effect",
          "Thermoelectric effect"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Photons create electron-hole pairs separated by p-n junction field."
          ],
          "keyConcept": "Photons create electron-hole pairs separated by p-n junction field."
        }
      },
      {
        "id": 11,
        "question": "Which small BJT current controls larger collector current?",
        "options": [
          "Base current",
          "Emitter",
          "Reverse",
          "Leakage"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$I_C = \\beta I_B$."
          ],
          "keyConcept": "$I_C = \\beta I_B$."
        }
      },
      {
        "id": 12,
        "question": "Two types of MOS transistors combined in CMOS:",
        "options": [
          "NMOS and PMOS",
          "JFET and BJT",
          "NPN and PNP",
          "LED and diode"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Complementary NMOS and PMOS."
          ],
          "keyConcept": "Complementary NMOS and PMOS."
        }
      },
      {
        "id": 13,
        "question": "Major advantage of CMOS circuits:",
        "options": [
          "Low static power use",
          "Large size",
          "Mechanical strength",
          "Acoustic output"
        ],
        "correctIndex": 0,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Near-zero static standby power."
          ],
          "keyConcept": "Near-zero static standby power."
        }
      },
      {
        "id": 14,
        "question": "Which statement describes RAM?",
        "options": [
          "Uses tape",
          "Usually volatile",
          "Stores optically",
          "Read-only"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Volatile working memory."
          ],
          "keyConcept": "Volatile working memory."
        }
      },
      {
        "id": 15,
        "question": "Semiconductor memory used in SSD:",
        "options": [
          "Register",
          "Cache",
          "Flash memory",
          "Dynamic RAM"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Non-volatile NAND flash."
          ],
          "keyConcept": "Non-volatile NAND flash."
        }
      },
      {
        "id": 16,
        "question": "Main purpose of AI accelerator chip:",
        "options": [
          "Measure temperature",
          "Convert sound",
          "Speed up AI computations",
          "Route packets"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Parallel matrix multiplication."
          ],
          "keyConcept": "Parallel matrix multiplication."
        }
      },
      {
        "id": 17,
        "question": "Basic role of sensor in IoT:",
        "options": [
          "Increase voltage",
          "Compile software",
          "Detect a physical quantity",
          "Encrypt packet"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Converts physical parameter to electrical signal."
          ],
          "keyConcept": "Converts physical parameter to electrical signal."
        }
      },
      {
        "id": 18,
        "question": "What is a computer network?",
        "options": [
          "Single processing unit",
          "Storage chip",
          "Group of connected devices",
          "Power supply"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Connected computing nodes."
          ],
          "keyConcept": "Connected computing nodes."
        }
      },
      {
        "id": 19,
        "question": "Physical phenomenon confining light in optical fiber:",
        "options": [
          "Photoelectric",
          "Resonance",
          "Induction",
          "Total internal reflection"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Total internal reflection at core-cladding boundary."
          ],
          "keyConcept": "Total internal reflection at core-cladding boundary."
        }
      },
      {
        "id": 20,
        "question": "Processor suited for many parallel calculations:",
        "options": [
          "GPU",
          "Router",
          "CPU",
          "SSD controller"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "GPU thousands of parallel cores."
          ],
          "keyConcept": "GPU thousands of parallel cores."
        }
      },
      {
        "id": 21,
        "question": "What is the result of binary addition $101_2 + 011_2$?",
        "options": [
          "$1000_2$",
          "$100_2$",
          "$110_2$",
          "$111_2$"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$5 + 3 = 8 = 1000_2$."
          ],
          "keyConcept": "$5 + 3 = 8 = 1000_2$."
        }
      },
      {
        "id": 22,
        "question": "What is the result of binary subtraction $1101_2 - 0101_2$?",
        "options": [
          "$1001_2$",
          "$1000_2$",
          "$1010_2$",
          "$0110_2$"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$13 - 5 = 8 = 1000_2$."
          ],
          "keyConcept": "$13 - 5 = 8 = 1000_2$."
        }
      },
      {
        "id": 23,
        "question": "In 2's complement subtraction, what is added to the minuend?",
        "options": [
          "The 2's complement of subtrahend",
          "The parity bit (across all standard operating temperatures)",
          "The sign bit (governed by linear superposition principles)",
          "The 1's complement"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$A - B = A + (\\text{2's comp of } B)$."
          ],
          "keyConcept": "$A - B = A + (\\text{2's comp of } B)$."
        }
      },
      {
        "id": 24,
        "question": "Using 4-bit 2's complement, what is the result of $0110_2 - 0011_2$?",
        "options": [
          "$0011_2$",
          "$1001_2$",
          "$0100_2$",
          "$1110_2$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$6 - 3 = 3 = 0011_2$."
          ],
          "keyConcept": "$6 - 3 = 3 = 0011_2$."
        }
      },
      {
        "id": 25,
        "question": "Which logic gate produces an output of 1 only when all inputs are 1?",
        "options": [
          "XOR gate",
          "AND gate",
          "OR gate",
          "NOT gate"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Standard definition of AND gate."
          ],
          "keyConcept": "Standard definition of AND gate."
        }
      },
      {
        "id": 26,
        "question": "What is the output of a NOT gate when its input is 0?",
        "options": [
          "$1$",
          "Undefined",
          "The same input",
          "$0$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "NOT inverts logic level: $\\bar{0} = 1$."
          ],
          "keyConcept": "NOT inverts logic level: $\\bar{0} = 1$."
        }
      },
      {
        "id": 27,
        "question": "According to Boolean identity law, what is $A + 0$?",
        "options": [
          "$0$",
          "$\\bar{A}$",
          "$A$",
          "$1$"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$A + 0 = A$."
          ],
          "keyConcept": "$A + 0 = A$."
        }
      },
      {
        "id": 28,
        "question": "What does SOP stand for in Boolean algebra?",
        "options": [
          "Set of Parameters",
          "Sum of Products",
          "Sum of Powers",
          "Sequence of Products"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "SOP = Sum of Products (OR of AND terms)."
          ],
          "keyConcept": "SOP = Sum of Products (OR of AND terms)."
        }
      },
      {
        "id": 29,
        "question": "Which expression is in Product of Sums (POS) form?",
        "options": [
          "$(A+B)(C+D)$",
          "$ABC+DEF$",
          "$A+B+C$",
          "$AB+CD$"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "POS is an AND of OR clauses."
          ],
          "keyConcept": "POS is an AND of OR clauses."
        }
      },
      {
        "id": 30,
        "question": "What is the main purpose of a Karnaugh map?",
        "options": [
          "To convert decimal numbers",
          "To store binary data",
          "To simplify Boolean expressions",
          "To generate clock pulses"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "K-Maps graphically minimize Boolean switching functions."
          ],
          "keyConcept": "K-Maps graphically minimize Boolean switching functions."
        }
      }
    ]
  },
  {
    "id": "phy175-midterm-paper-3",
    "code": "PHY175-PAPER-C",
    "title": "Midterm Examination • Paper 3 (Diodes, Rectifiers & BJT Biasing)",
    "courseCode": "PHY175",
    "courseName": "Physics Practice & Formulae",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Solid State Physics",
      "Fermi Energy",
      "Diodes & Transistors",
      "Digital Logic"
    ],
    "description": "Focuses on PN junction characteristics, full-wave bridge ripple factor, Zener regulation, and transistor configurations.",
    "questions": [
      {
        "id": 1,
        "question": "In the Drude model, $\\sigma = \\frac{ne^2\\tau}{m}$. If electron density doubles while mean collision time halves, conductivity:",
        "options": [
          "Becomes half as large",
          "Becomes twice as large",
          "Remains unchanged",
          "Becomes four times as large"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$\\sigma \\propto n \\tau \\implies (2)(1/2) = 1$."
          ],
          "keyConcept": "$\\sigma \\propto n \\tau \\implies (2)(1/2) = 1$."
        }
      },
      {
        "id": 2,
        "question": "Electron concentration increases along $+x$. Which electric-field direction balances electron diffusion current?",
        "options": [
          "Perpendicular to $x$-direction",
          "Along the negative $x$-direction",
          "Along the positive $x$-direction",
          "No electric field is required"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Diffusion drives electrons toward $-x$. Electric field along $+x$ exerts force in $-x$ to create opposing drift."
          ],
          "keyConcept": "Diffusion drives electrons toward $-x$. Electric field along $+x$ exerts force in $-x$ to create opposing drift."
        }
      },
      {
        "id": 3,
        "question": "For 3D free electron gas at $0\\,\\text{K}$, $E_F \\propto n^{2/3}$. If density increases 8 times, new Fermi energy is:",
        "options": [
          "$8 E_F$",
          "$16 E_F$",
          "$4 E_F$",
          "$2 E_F$"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$E_F' = (8)^{2/3} E_F = 4 E_F$."
          ],
          "keyConcept": "$E_F' = (8)^{2/3} E_F = 4 E_F$."
        }
      },
      {
        "id": 4,
        "question": "Probability that an electronic state at Fermi energy $E_F$ is occupied at nonzero temperature is:",
        "options": [
          "$1/2$",
          "$0$",
          "$1/e$",
          "$1$"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$f(E_F) = 1/(1+e^0) = 1/2$ at all $T > 0$."
          ],
          "keyConcept": "$f(E_F) = 1/(1+e^0) = 1/2$ at all $T > 0$."
        }
      },
      {
        "id": 5,
        "question": "At temperature $T$, a state has $E - E_F = k_B T \\ln 3$. What is its Fermi-Dirac occupation probability?",
        "options": [
          "$1/3$",
          "$3/4$",
          "$1/2$",
          "$1/4$"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$f(E) = 1/(1 + e^{\\ln 3}) = 1/(1+3) = 1/4$."
          ],
          "keyConcept": "$f(E) = 1/(1 + e^{\\ln 3}) = 1/(1+3) = 1/4$."
        }
      },
      {
        "id": 6,
        "question": "When $N$ identical isolated atoms form a crystal, one atomic energy level splits into:",
        "options": [
          "About $N$ closely spaced levels",
          "A single level",
          "Exactly two levels",
          "A forbidden gap"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Wavefunction overlap splits $N$ degenerate states into an energy band of $N$ levels."
          ],
          "keyConcept": "Wavefunction overlap splits $N$ degenerate states into an energy band of $N$ levels."
        }
      },
      {
        "id": 7,
        "question": "Why does a completely filled energy band produce no net electrical current under weak field?",
        "options": [
          "Electrons have no kinetic energy",
          "Contains only positive carriers",
          "All enter conduction band",
          "Contributions from occupied states cancel across the band"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "For every electron in state $+k$, there is an electron in $-k$, summing velocity to zero."
          ],
          "keyConcept": "For every electron in state $+k$, there is an electron in $-k$, summing velocity to zero."
        }
      },
      {
        "id": 8,
        "question": "Near the top of valence band, $d^2E/dk^2 < 0$. What is the standard description of transport?",
        "options": [
          "Negative holes, negative mass",
          "Positive holes with positive effective mass",
          "Free electrons, infinite mass",
          "Neutral carriers, zero mass"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Negative electron curvature is mapped to holes with $q = +e$ and $m_h^* > 0$."
          ],
          "keyConcept": "Negative electron curvature is mapped to holes with $q = +e$ and $m_h^* > 0$."
        }
      },
      {
        "id": 9,
        "question": "An electron occupies a band region where $m^* < 0$. If an external force acts along $+x$, its acceleration is:",
        "options": [
          "Always zero",
          "Along $+x$",
          "Along $-x$",
          "Perpendicular to $+x$"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$a = F/m^*$; with $m^* < 0$, acceleration is opposite to applied force."
          ],
          "keyConcept": "$a = F/m^*$; with $m^* < 0$, acceleration is opposite to applied force."
        }
      },
      {
        "id": 10,
        "question": "Current is along $+x$, magnetic field along $+z$. If electrons are majority carriers, where do they accumulate?",
        "options": [
          "On the positive $y$ side",
          "On the negative $y$ side",
          "On the positive $x$ side",
          "On the negative $z$ side"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$\\vec{F} = -e(\\vec{v}_d \\times \\vec{B}) = -e((-v_d\\hat{x}) \\times B\\hat{z}) = -e(v_d B \\hat{y}) = -e v_d B \\hat{y}$ toward $-y$."
          ],
          "keyConcept": "$\\vec{F} = -e(\\vec{v}_d \\times \\vec{B}) = -e((-v_d\\hat{x}) \\times B\\hat{z}) = -e(v_d B \\hat{y}) = -e v_d B \\hat{y}$ towa..."
        }
      },
      {
        "id": 11,
        "question": "Source $12\\,\\text{V}$ connected to series $2\\,\\Omega$ and $4\\,\\Omega$. Circuit current:",
        "options": [
          "$2\\,\\text{A}$",
          "$1\\,\\text{A}$",
          "$3\\,\\text{A}$",
          "$6\\,\\text{A}$"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$12 / 6 = 2\\,\\text{A}$."
          ],
          "keyConcept": "$12 / 6 = 2\\,\\text{A}$."
        }
      },
      {
        "id": 12,
        "question": "Currents $5\\,\\text{A}, 2\\,\\text{A}$ enter node; $4\\,\\text{A}, I$ leave. Value of $I$:",
        "options": [
          "$2\\,\\text{A}$",
          "$7\\,\\text{A}$",
          "$1\\,\\text{A}$",
          "$3\\,\\text{A}$"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$5+2 = 4+I \\implies I = 3\\,\\text{A}$."
          ],
          "keyConcept": "$5+2 = 4+I \\implies I = 3\\,\\text{A}$."
        }
      },
      {
        "id": 13,
        "question": "Supply $20\\,\\text{V}$ across series $3\\,\\text{k}\\Omega, 7\\,\\text{k}\\Omega$. Voltage across $7\\,\\text{k}\\Omega$:",
        "options": [
          "$17\\,\\text{V}$",
          "$6\\,\\text{V}$",
          "$14\\,\\text{V}$",
          "$10\\,\\text{V}$"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$20 \\times 7/10 = 14\\,\\text{V}$."
          ],
          "keyConcept": "$20 \\times 7/10 = 14\\,\\text{V}$."
        }
      },
      {
        "id": 14,
        "question": "Divider $R_1=2\\,\\text{k}\\Omega, R_2=8\\,\\text{k}\\Omega$. Parallel load on $R_2$ main effect:",
        "options": [
          "Output voltage decreases",
          "Output increases",
          "Current zero",
          "Source zero"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Parallel resistance drops, reducing voltage drop."
          ],
          "keyConcept": "Parallel resistance drops, reducing voltage drop."
        }
      },
      {
        "id": 15,
        "question": "Total current $6\\,\\text{A}$ into parallel $3\\,\\Omega, 6\\,\\Omega$. Current in $3\\,\\Omega$:",
        "options": [
          "$1\\,\\text{A}$",
          "$6\\,\\text{A}$",
          "$2\\,\\text{A}$",
          "$4\\,\\text{A}$"
        ],
        "correctIndex": 0,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$6 \\times 6/9 = 4\\,\\text{A}$."
          ],
          "keyConcept": "$6 \\times 6/9 = 4\\,\\text{A}$."
        }
      },
      {
        "id": 16,
        "question": "Parallel branches $4\\,\\Omega, 12\\,\\Omega$. Current in $4\\,\\Omega$ is $9\\,\\text{A}$. Current in $12\\,\\Omega$:",
        "options": [
          "$1\\,\\text{A}$",
          "$3\\,\\text{A}$",
          "$9\\,\\text{A}$",
          "$27\\,\\text{A}$"
        ],
        "correctIndex": 0,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$V = 36\\,\\text{V} \\implies I = 36/12 = 3\\,\\text{A}$."
          ],
          "keyConcept": "$V = 36\\,\\text{V} \\implies I = 36/12 = 3\\,\\text{A}$."
        }
      },
      {
        "id": 17,
        "question": "Depletion region when silicon diode is forward biased:",
        "options": [
          "Width decreases",
          "Resistance infinite",
          "Width increases",
          "Polarity reverses"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Depletion layer narrows."
          ],
          "keyConcept": "Depletion layer narrows."
        }
      },
      {
        "id": 18,
        "question": "Silicon diode anode $0.8\\,\\text{V}$, cathode $0.2\\,\\text{V}$ ($V_D=0.7\\,\\text{V}$). Behavior:",
        "options": [
          "Reverse biased",
          "Conducts significantly",
          "Acts as open circuit",
          "Breakdown"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$V_{applied} = 0.6\\,\\text{V} < 0.7\\,\\text{V}$ threshold."
          ],
          "keyConcept": "$V_{applied} = 0.6\\,\\text{V} < 0.7\\,\\text{V}$ threshold."
        }
      },
      {
        "id": 19,
        "question": "Full-wave bridge rectifier with $50\\,\\text{Hz}$ AC. Output ripple frequency:",
        "options": [
          "$50\\,\\text{Hz}$",
          "$100\\,\\text{Hz}$",
          "$25\\,\\text{Hz}$",
          "$200\\,\\text{Hz}$"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$2 \\times 50 = 100\\,\\text{Hz}$."
          ],
          "keyConcept": "$2 \\times 50 = 100\\,\\text{Hz}$."
        }
      },
      {
        "id": 20,
        "question": "Ideal forward-biased diode in diode switch represents:",
        "options": [
          "Open circuit",
          "Amplifier",
          "Short circuit",
          "Current source"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Closed short circuit switch."
          ],
          "keyConcept": "Closed short circuit switch."
        }
      },
      {
        "id": 21,
        "question": "What is the binary equivalent of decimal $173_{10}$?",
        "options": [
          "$11001101_2$",
          "$10101101_2$",
          "$10101011_2$",
          "$10110101_2$"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$173 = 128 + 32 + 8 + 4 + 1 = 10101101_2$."
          ],
          "keyConcept": "$173 = 128 + 32 + 8 + 4 + 1 = 10101101_2$."
        }
      },
      {
        "id": 22,
        "question": "Convert hexadecimal $3\\text{A}7_{16}$ to decimal:",
        "options": [
          "$917_{10}$",
          "$935_{10}$",
          "$927_{10}$",
          "$947_{10}$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$3\\times 256 + 10\\times 16 + 7 = 768 + 160 + 7 = 935_{10}$."
          ],
          "keyConcept": "$3\\times 256 + 10\\times 16 + 7 = 768 + 160 + 7 = 935_{10}$."
        }
      },
      {
        "id": 23,
        "question": "What is the binary equivalent of Gray code $1101$?",
        "options": [
          "$1011$",
          "$1010$",
          "$1001$",
          "$1111$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$B_3=1, B_2=1\\oplus 1=0, B_1=0\\oplus 0=0, B_0=0\\oplus 1=1 \\implies 1001_2$."
          ],
          "keyConcept": "$B_3=1, B_2=1\\oplus 1=0, B_1=0\\oplus 0=0, B_0=0\\oplus 1=1 \\implies 1001_2$."
        }
      },
      {
        "id": 24,
        "question": "Convert binary $10110_2$ into Gray code:",
        "options": [
          "$10011$",
          "$11111$",
          "$10101$",
          "$11101$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$G_4=1, G_3=1\\oplus 0=1, G_2=0\\oplus 1=1, G_1=1\\oplus 1=0, G_0=1\\oplus 0=1 \\implies 11101$."
          ],
          "keyConcept": "$G_4=1, G_3=1\\oplus 0=1, G_2=0\\oplus 1=1, G_1=1\\oplus 1=0, G_0=1\\oplus 0=1 \\implies 11101$."
        }
      },
      {
        "id": 25,
        "question": "What is the Excess-3 representation of decimal $59$?",
        "options": [
          "$01101001$",
          "$10001100$",
          "$10011000$",
          "$01011001$"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$5+3=8=1000_2, 9+3=12=1100_2 \\implies 1000\\,1100$."
          ],
          "keyConcept": "$5+3=8=1000_2, 9+3=12=1100_2 \\implies 1000\\,1100$."
        }
      },
      {
        "id": 26,
        "question": "The BCD code $1001\\,0110$ represents which decimal number?",
        "options": [
          "$106$",
          "$86$",
          "$96$",
          "$150$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$1001_2 = 9, 0110_2 = 6 \\implies 96$."
          ],
          "keyConcept": "$1001_2 = 9, 0110_2 = 6 \\implies 96$."
        }
      },
      {
        "id": 27,
        "question": "What is the 1's complement of 8-bit binary $01011010$?",
        "options": [
          "$10100101$",
          "$10101001$",
          "$11011010$",
          "$01000101$"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Bitwise NOT: $01011010 \\to 10100101$."
          ],
          "keyConcept": "Bitwise NOT: $01011010 \\to 10100101$."
        }
      },
      {
        "id": 28,
        "question": "Result of binary addition $1011_2 + 1101_2$:",
        "options": [
          "$11100_2$",
          "$10110_2$",
          "$11000_2$",
          "$10000_2$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$11 + 13 = 24 = 11000_2$."
          ],
          "keyConcept": "$11 + 13 = 24 = 11000_2$."
        }
      },
      {
        "id": 29,
        "question": "Using 5-bit 2's complement arithmetic, what is $10110_2 - 01001_2$?",
        "options": [
          "$10011_2$",
          "$00101_2$",
          "$01101_2$",
          "$11101_2$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$22 - 9 = 13 = 01101_2$."
          ],
          "keyConcept": "$22 - 9 = 13 = 01101_2$."
        }
      },
      {
        "id": 30,
        "question": "Using 5-bit signed 2's complement, what is $01101_2 + 00111_2$?",
        "options": [
          "$11100_2$",
          "$10100_2$",
          "$10010_2$",
          "$01010_2$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$+13 + (+7) = +20$. In 5 bits, range is $[-16,+15]$; $+20 = 10100_2$ (overflow occurs, stored pattern $10100$)."
          ],
          "keyConcept": "$+13 + (+7) = +20$. In 5 bits, range is $[-16,+15]$; $+20 = 10100_2$ (overflow occurs, stored pattern $10100$)."
        }
      }
    ]
  },
  {
    "id": "phy175-midterm-paper-4",
    "code": "PHY175-PAPER-D",
    "title": "Midterm Examination • Paper 4 (Digital Logic Gates & K-Map Minimization)",
    "courseCode": "PHY175",
    "courseName": "Physics Practice & Formulae",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Solid State Physics",
      "Fermi Energy",
      "Diodes & Transistors",
      "Digital Logic"
    ],
    "description": "Exam questions covering Boolean algebra theorems, De Morgan laws, universal NAND/NOR logic, and 4-variable K-maps.",
    "questions": [
      {
        "id": 1,
        "question": "A semiconductor slab has $n = 5.0 \\times 10^{22}\\,\\text{m}^{-3}, t = 0.50\\,\\text{mm}, I = 2.0\\,\\text{mA}, B = 0.50\\,\\text{T}$. Magnitude of Hall voltage $V_H$ is:",
        "options": [
          "$0.25\\,\\text{mV}$",
          "$0.50\\,\\text{mV}$",
          "$1.00\\,\\text{mV}$",
          "$2.50\\,\\text{mV}$"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$V_H = \\frac{IB}{net} = \\frac{(2\\times 10^{-3})(0.5)}{(5\\times 10^{22})(1.6\\times 10^{-19})(0.5\\times 10^{-3})} = 0.25\\,\\text{mV}$."
          ],
          "keyConcept": "$V_H = \\frac{IB}{net} = \\frac{(2\\times 10^{-3})(0.5)}{(5\\times 10^{22})(1.6\\times 10^{-19})(0.5\\times 10^{-3})} = 0.25\\,..."
        }
      },
      {
        "id": 2,
        "question": "Hall coefficient is $R_H = -3.9 \\times 10^{-4}\\,\\text{m}^3/\\text{C}$. The carrier type and approximate concentration are:",
        "options": [
          "Electrons, $1.6 \\times 10^{22}\\,\\text{m}^{-3}$",
          "Electrons, $3.9 \\times 10^{22}\\,\\text{m}^{-3}$",
          "Holes, $1.6 \\times 10^{22}\\,\\text{m}^{-3}$",
          "Holes, $3.9 \\times 10^{22}\\,\\text{m}^{-3}$"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Negative sign $\\implies$ electrons; $n = 1/(|R_H|e) = 1.6\\times 10^{22}\\,\\text{m}^{-3}$."
          ],
          "keyConcept": "Negative sign $\\implies$ electrons; $n = 1/(|R_H|e) = 1.6\\times 10^{22}\\,\\text{m}^{-3}$."
        }
      },
      {
        "id": 3,
        "question": "In intrinsic semiconductor $n=p=n_i$. If $\\mu_e = 3\\mu_h$, what fraction of conductivity is due to electrons?",
        "options": [
          "$1/2$",
          "$3/4$",
          "$2/3$",
          "$1/4$"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$\\sigma_e / \\sigma_{total} = \\mu_e / (\\mu_e + \\mu_h) = 3/(3+1) = 3/4$."
          ],
          "keyConcept": "$\\sigma_e / \\sigma_{total} = \\mu_e / (\\mu_e + \\mu_h) = 3/(3+1) = 3/4$."
        }
      },
      {
        "id": 4,
        "question": "Silicon is doped with phosphorus. After donor ionization, which carriers and fixed ions are produced?",
        "options": [
          "Free holes and negative donor ions",
          "Free electrons and negative donor ions",
          "Free electrons and positive donor ions",
          "Free holes and positive donor ions"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Donating an electron leaves fixed positive donor ion $N_D^+$ and free conduction electron."
          ],
          "keyConcept": "Donating an electron leaves fixed positive donor ion $N_D^+$ and free conduction electron."
        }
      },
      {
        "id": 5,
        "question": "Why does conductivity of intrinsic semiconductor increase strongly with temperature?",
        "options": [
          "Forbidden gap fills completely",
          "More electrons cross bandgap creating pairs",
          "Crystal becomes metal (in an ideal homogeneous medium)",
          "Valence electrons per atom increases"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Thermal excitation across $E_g$ causes exponential carrier generation $n_i \\propto e^{-E_g/2k_BT}$."
          ],
          "keyConcept": "Thermal excitation across $E_g$ causes exponential carrier generation $n_i \\propto e^{-E_g/2k_BT}$."
        }
      },
      {
        "id": 6,
        "question": "For intrinsic semiconductor, $E_i = \\frac{E_C+E_V}{2} + \\frac{k_BT}{2}\\ln(N_V/N_C)$. If $N_C > N_V$, $E_i$ is:",
        "options": [
          "Slightly below the middle of the band gap",
          "Slightly above the middle of the band gap",
          "At valence-band edge",
          "At conduction-band edge"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$\\ln(N_V/N_C) < 0$ when $N_C > N_V$, pulling $E_i$ below midgap."
          ],
          "keyConcept": "$\\ln(N_V/N_C) < 0$ when $N_C > N_V$, pulling $E_i$ below midgap."
        }
      },
      {
        "id": 7,
        "question": "At $300\\,\\text{K}$, electron concentration in n-type Si increases by $100\\times$. How far does $E_F$ shift towards $E_C$? ($k_BT = 0.0259\\,\\text{eV}$)",
        "options": [
          "$0.059\\,\\text{eV}$",
          "$0.259\\,\\text{eV}$",
          "$0.460\\,\\text{eV}$",
          "$0.119\\,\\text{eV}$"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$\\Delta E_F = k_BT \\ln(100) = 0.0259 \\times 4.605 = 0.119\\,\\text{eV}$."
          ],
          "keyConcept": "$\\Delta E_F = k_BT \\ln(100) = 0.0259 \\times 4.605 = 0.119\\,\\text{eV}$."
        }
      },
      {
        "id": 8,
        "question": "Why is direct band-gap semiconductor more efficient for light emission than indirect gap?",
        "options": [
          "Recombination requires 2 phonons",
          "No available conduction states",
          "Valence band has larger resistance",
          "Electron-hole recombination conserves momentum without a phonon"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Direct transition is a 1st-order process requiring no phonon lattice interaction."
          ],
          "keyConcept": "Direct transition is a 1st-order process requiring no phonon lattice interaction."
        }
      },
      {
        "id": 9,
        "question": "In illuminated solar cell under short circuit, primary role of depletion field is to:",
        "options": [
          "Make carriers move to same contact",
          "Create sub-bandgap photons",
          "Separate photogenerated electrons and holes",
          "Prevent light entering"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Built-in electric field sweeps electrons to n-side and holes to p-side."
          ],
          "keyConcept": "Built-in electric field sweeps electrons to n-side and holes to p-side."
        }
      },
      {
        "id": 10,
        "question": "Solar cell receives $100\\,\\text{mW}$ of $2.0\\,\\text{eV}$ light. If $80\\%$ photons create collected electrons, photocurrent is:",
        "options": [
          "$20\\,\\text{mA}$",
          "$80\\,\\text{mA}$",
          "$40\\,\\text{mA}$",
          "$64\\,\\text{mA}$"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Photon rate $= 3.125\\times 10^{17}\\,\\text{s}^{-1} \\implies I = 0.8\\times 1.6\\times 10^{-19}\\times 3.125\\times 10^{17} = 40\\,\\text{mA}$."
          ],
          "keyConcept": "Photon rate $= 3.125\\times 10^{17}\\,\\text{s}^{-1} \\implies I = 0.8\\times 1.6\\times 10^{-19}\\times 3.125\\times 10^{17} = ..."
        }
      },
      {
        "id": 11,
        "question": "BJT active region: $I_C = 2\\,\\text{mA}, I_B = 20\\,\\mu\\text{A}$. Current gain $\\beta$:",
        "options": [
          "$200$",
          "$100$",
          "$10$",
          "$50$"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$\\beta = 2000/20 = 100$."
          ],
          "keyConcept": "$\\beta = 2000/20 = 100$."
        }
      },
      {
        "id": 12,
        "question": "BJT saturation condition:",
        "options": [
          "Emitter forward, collector reverse",
          "Emitter reverse, collector forward",
          "Both reverse",
          "Both forward"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Both EBJ and CBJ forward biased."
          ],
          "keyConcept": "Both EBJ and CBJ forward biased."
        }
      },
      {
        "id": 13,
        "question": "CMOS inverter with input LOW:",
        "options": [
          "NMOS ON",
          "Both ON",
          "PMOS ON, output HIGH",
          "Both OFF"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "PMOS pulls output to $V_{DD}$."
          ],
          "keyConcept": "PMOS pulls output to $V_{DD}$."
        }
      },
      {
        "id": 14,
        "question": "Why CMOS consumes very little static power:",
        "options": [
          "Supply path nonconducting in steady states",
          "No transistors",
          "Breakdown",
          "Grounded"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "One transistor always OFF in steady state."
          ],
          "keyConcept": "One transistor always OFF in steady state."
        }
      },
      {
        "id": 15,
        "question": "Computer temporary working storage during execution:",
        "options": [
          "Optical fiber",
          "SSD",
          "ROM",
          "Dynamic RAM"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "DRAM working memory."
          ],
          "keyConcept": "DRAM working memory."
        }
      },
      {
        "id": 16,
        "question": "Why SSD is more shock-resistant than HDD:",
        "options": [
          "Rotating platter",
          "Uses no moving mechanical parts",
          "Loses data without power",
          "Stores in magnetic domains"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Solid-state silicon components."
          ],
          "keyConcept": "Solid-state silicon components."
        }
      },
      {
        "id": 17,
        "question": "Why GPUs/AI accelerators effective for neural networks:",
        "options": [
          "Hardware replacement",
          "Eliminate memory",
          "Perform many similar operations in parallel",
          "Sequential instructions"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Massively parallel SIMD processing."
          ],
          "keyConcept": "Massively parallel SIMD processing."
        }
      },
      {
        "id": 18,
        "question": "IoT node sends data only when $\\Delta T > 2^\\circ\\text{C}$. Benefit:",
        "options": [
          "Higher noise",
          "Reduced energy and communication use",
          "No calibration",
          "Zero error"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Conserves battery power."
          ],
          "keyConcept": "Conserves battery power."
        }
      },
      {
        "id": 19,
        "question": "Deliver data to every host on local subnet:",
        "options": [
          "Broadcast",
          "Loopback",
          "Point-to-point",
          "Unicast"
        ],
        "correctIndex": 0,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Subnet broadcast."
          ],
          "keyConcept": "Subnet broadcast."
        }
      },
      {
        "id": 20,
        "question": "Property allowing fiber signal propagation with low loss:",
        "options": [
          "Thermal expansion",
          "Total internal reflection",
          "Induction (across all standard operating temperatures)",
          "Capacitive coupling"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Total internal reflection in glass core."
          ],
          "keyConcept": "Total internal reflection in glass core."
        }
      },
      {
        "id": 21,
        "question": "A NAND gate has inputs $A=1$ and $B=1$. Output is:",
        "options": [
          "$B$",
          "$0$",
          "$A$",
          "$1$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$\\overline{1 \\cdot 1} = 0$."
          ],
          "keyConcept": "$\\overline{1 \\cdot 1} = 0$."
        }
      },
      {
        "id": 22,
        "question": "Which gate produces output 1 only when two inputs are different?",
        "options": [
          "AND gate",
          "OR gate",
          "XNOR gate",
          "XOR gate"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "XOR is the difference/inequality detector ($A \\neq B$)."
          ],
          "keyConcept": "XOR is the difference/inequality detector ($A \\neq B$)."
        }
      },
      {
        "id": 23,
        "question": "Simplify Boolean expression $A + AB$:",
        "options": [
          "$A+B$",
          "$A$",
          "$AB$",
          "$B$"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$A(1+B) = A(1) = A$ (Absorption law)."
          ],
          "keyConcept": "$A(1+B) = A(1) = A$ (Absorption law)."
        }
      },
      {
        "id": 24,
        "question": "Using De Morgan's theorem, simplify $(A+B)'$:",
        "options": [
          "$A'+B'$",
          "$A'B'$",
          "$(AB)'$",
          "$AB$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$\\overline{A+B} = \\bar{A}\\bar{B}$."
          ],
          "keyConcept": "$\\overline{A+B} = \\bar{A}\\bar{B}$."
        }
      },
      {
        "id": 25,
        "question": "Which of the following is in standard Sum of Products (SOP) form?",
        "options": [
          "$(A+B')+C$",
          "$(A+B)(C+D)$",
          "$A(B+C')$",
          "$A'B + AC + BC'$"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Sum (OR) of product (AND) terms."
          ],
          "keyConcept": "Sum (OR) of product (AND) terms."
        }
      },
      {
        "id": 26,
        "question": "Which is in Product of Sums (POS) form?",
        "options": [
          "$AB+A'C$",
          "$(A+B')(A'+C)$",
          "$A(B+C)$",
          "$AB(C+D)$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Product (AND) of sum (OR) terms."
          ],
          "keyConcept": "Product (AND) of sum (OR) terms."
        }
      },
      {
        "id": 27,
        "question": "Using 3-variable K-map, simplify $F(A,B,C) = \\sum m(1,3,5,7)$:",
        "options": [
          "$C$",
          "$A+B$",
          "$A$",
          "$B$"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Minterms $1,3,5,7$ correspond to $C=1$ independent of $A,B$."
          ],
          "keyConcept": "Minterms $1,3,5,7$ correspond to $C=1$ independent of $A,B$."
        }
      },
      {
        "id": 28,
        "question": "Using 4-variable K-map for $F = \\sum m(0,2,8,10)$:",
        "options": [
          "$A'D'$",
          "$BD'$",
          "$B'D'$",
          "$B'C'$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Corner cells $0,2,8,10$ form a quad $= \\bar{B}\\bar{D}$."
          ],
          "keyConcept": "Corner cells $0,2,8,10$ form a quad $= \\bar{B}\\bar{D}$."
        }
      },
      {
        "id": 29,
        "question": "Using 4-variable K-map for $F = \\sum m(1,3,9,11)$:",
        "options": [
          "$B'C'$",
          "$A'D$",
          "$B'D$",
          "$BC'$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Cells in columns $01, 11$ for rows $00, 10$ form a quad $= \\bar{B}D$."
          ],
          "keyConcept": "Cells in columns $01, 11$ for rows $00, 10$ form a quad $= \\bar{B}D$."
        }
      },
      {
        "id": 30,
        "question": "Simplify Boolean expression $(A+B)(A+C)$:",
        "options": [
          "$ABC$",
          "$A+BC$",
          "$AB+AC$",
          "$A+B+C$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$(A+B)(A+C) = AA + AC + AB + BC = A(1+C+B) + BC = A + BC$ (Distributive law)."
          ],
          "keyConcept": "$(A+B)(A+C) = AA + AC + AB + BC = A(1+C+B) + BC = A + BC$ (Distributive law)."
        }
      }
    ]
  },
  {
    "id": "phy175-midterm-paper-5",
    "code": "PHY175-PAPER-E",
    "title": "Midterm Examination • Paper 5 (Comprehensive Midterm Formula Suite)",
    "courseCode": "PHY175",
    "courseName": "Physics Practice & Formulae",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Solid State Physics",
      "Fermi Energy",
      "Diodes & Transistors",
      "Digital Logic"
    ],
    "description": "University exam simulation across all Units 1-3 with authentic step-by-step solutions and SI unit verification.",
    "questions": [
      {
        "id": 1,
        "question": "Metal B has $2\\times$ electron density and $3\\times$ effective mass of metal A. If $\\sigma_A = \\sigma_B$, relationship between collision times is:",
        "options": [
          "$\\tau_B = 6\\tau_A$",
          "$\\tau_B = \\frac{3}{2}\\tau_A$",
          "$\\tau_B = \\frac{2}{3}\\tau_A$",
          "$\\tau_B = \\frac{1}{6}\\tau_A$"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$\\sigma = \\frac{n e^2 \\tau}{m} \\implies \\frac{2 n_A e^2 \\tau_B}{3 m_A} = \\frac{n_A e^2 \\tau_A}{m_A} \\implies \\tau_B = \\frac{3}{2}\\tau_A$."
          ],
          "keyConcept": "$\\sigma = \\frac{n e^2 \\tau}{m} \\implies \\frac{2 n_A e^2 \\tau_B}{3 m_A} = \\frac{n_A e^2 \\tau_A}{m_A} \\implies \\tau_B = \\f..."
        }
      },
      {
        "id": 2,
        "question": "In nondegenerate semiconductor, $n(x) = n_0 e^{x/L}$. Which electric field makes total electron current density zero?",
        "options": [
          "$E_x = -\\frac{qL}{kT}$",
          "$E_x = -\\frac{kT}{qL}$",
          "$E_x = \\frac{kT}{qL}$",
          "$E_x = \\frac{qL}{kT}$"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$J_n = q n \\mu_n E_x + q D_n \\frac{dn}{dx} = 0 \\implies E_x = -\\frac{kT}{qL}$."
          ],
          "keyConcept": "$J_n = q n \\mu_n E_x + q D_n \\frac{dn}{dx} = 0 \\implies E_x = -\\frac{kT}{qL}$."
        }
      },
      {
        "id": 3,
        "question": "Excess minority electrons in p-type Si: $\\Delta n(x) = \\Delta n_0 e^{-x/L_n}$ for $x>0$. With no $E$-field, directions of electron motion and diffusion current are:",
        "options": [
          "Electrons move $+x$, current $-x$",
          "Electrons and current both $+x$",
          "Electrons and current both $-x$",
          "Electrons move $-x$, current $+x$"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Electrons diffuse down gradient along $+x$. Conventional current is along $-x$."
          ],
          "keyConcept": "Electrons diffuse down gradient along $+x$. Conventional current is along $-x$."
        }
      },
      {
        "id": 4,
        "question": "Two 3D free electron systems at $T=0$: System B has $n_B = 8n_A$ and $m_B^* = 2m_A^*$. What is $E_{F,B}/E_{F,A}$?",
        "options": [
          "$4$",
          "$8$",
          "$1/2$",
          "$2$"
        ],
        "correctIndex": 3,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$E_F \\propto \\frac{n^{2/3}}{m^*} \\implies \\frac{(8)^{2/3}}{2} = \\frac{4}{2} = 2$."
          ],
          "keyConcept": "$E_F \\propto \\frac{n^{2/3}}{m^*} \\implies \\frac{(8)^{2/3}}{2} = \\frac{4}{2} = 2$."
        }
      },
      {
        "id": 5,
        "question": "At temp $T$, state 1 is at $E_F + k_BT\\ln 3$ and state 2 is at $E_F - k_BT\\ln 3$. Probabilities that state 1 is occupied and state 2 is empty are:",
        "options": [
          "Both $1/4$",
          "Both $3/4$",
          "$3/4$ and $1/4$",
          "$1/4$ and $3/4$"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$f(E_F+\\Delta) = \\frac{1}{1+e^{\\ln 3}} = \\frac{1}{4}$. Empty prob at $E_F-\\Delta$ is $1-f(E_F-\\Delta) = f(E_F+\\Delta) = 1/4$."
          ],
          "keyConcept": "$f(E_F+\\Delta) = \\frac{1}{1+e^{\\ln 3}} = \\frac{1}{4}$. Empty prob at $E_F-\\Delta$ is $1-f(E_F-\\Delta) = f(E_F+\\Delta) = ..."
        }
      },
      {
        "id": 6,
        "question": "A narrow group of states has constant DOS symmetric about chemical potential $\\mu$. Integration limits $\\gg k_BT$. Thermal excitation satisfies:",
        "options": [
          "Electrons above $\\mu >$ holes below $\\mu$",
          "Number of electrons excited above $\\mu$ equals number of holes below $\\mu$",
          "Holes below $\\mu >$ electrons above $\\mu$",
          "Equality only at $T=0$"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "By particle conservation and Fermi-Dirac anti-symmetry about $\\mu$."
          ],
          "keyConcept": "By particle conservation and Fermi-Dirac anti-symmetry about $\\mu$."
        }
      },
      {
        "id": 7,
        "question": "Crystal has $N$ atoms, each contributing 1 electron from nondegenerate orbital. Assuming spin degeneracy, band theory predicts:",
        "options": [
          "Contains $N$ states, completely filled",
          "Contains $N/2$ states, half filled",
          "Contains $2N$ states, half filled",
          "Contains $2N$ states, completely filled"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "With 2 spin states per orbital, band holds $2N$ electrons. $N$ electrons fill half the band (metal)."
          ],
          "keyConcept": "With 2 spin states per orbital, band holds $2N$ electrons. $N$ electrons fill half the band (metal)."
        }
      },
      {
        "id": 8,
        "question": "In nearly-free electron model, why does energy gap open at Brillouin-zone boundary?",
        "options": [
          "Lattice confines electron permanently",
          "Collisions remove states",
          "Pauli principle shifts states",
          "Periodic potential couples degenerate forward and backward waves splitting standing wave energies"
        ],
        "correctIndex": 2,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Bragg reflection forms standing waves with different electrostatic potential energies."
          ],
          "keyConcept": "Bragg reflection forms standing waves with different electrostatic potential energies."
        }
      },
      {
        "id": 9,
        "question": "2D band dispersion: $E(k_x, k_y) = E_0 - \\alpha k_x^2 + \\beta k_y^2$ with $\\alpha, \\beta > 0$. Signs of electron effective-mass components are:",
        "options": [
          "$m_x^* > 0, m_y^* > 0$",
          "$m_x^* > 0, m_y^* < 0$",
          "$m_x^* < 0, m_y^* < 0$",
          "$m_x^* < 0, m_y^* > 0$"
        ],
        "correctIndex": 1,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "$m_x^* = \\hbar^2/(-2\\alpha) < 0$ and $m_y^* = \\hbar^2/(+2\\beta) > 0$."
          ],
          "keyConcept": "$m_x^* = \\hbar^2/(-2\\alpha) < 0$ and $m_y^* = \\hbar^2/(+2\\beta) > 0$."
        }
      },
      {
        "id": 10,
        "question": "Nearly full valence band has negative electron curvature near max. Why is it represented by holes with positive effective mass?",
        "options": [
          "Hole carries negative charge",
          "Hole is a proton",
          "Removing electron reverses both charge and current contribution",
          "Removing electron changes curvature"
        ],
        "correctIndex": 0,
        "topic": "Solid State Physics",
        "explanation": {
          "steps": [
            "Absence of negative charge electron moving with negative acceleration behaves identically to positive charge with positive mass."
          ],
          "keyConcept": "Absence of negative charge electron moving with negative acceleration behaves identically to positive charge with positi..."
        }
      },
      {
        "id": 11,
        "question": "Node $V$ connected to $10\\,\\text{V}$ through $2\\,\\Omega$, GND through $4\\,\\Omega$, $2\\,\\text{A}$ injected into node:",
        "options": [
          "$V=12\\,\\text{V}, I=-1\\,\\text{A}$",
          "$V=28/3\\,\\text{V}, I=1/3\\,\\text{A}$",
          "$V=8\\,\\text{V}, I=1\\,\\text{A}$",
          "$V=20/3\\,\\text{V}, I=5/3\\,\\text{A}$"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "KCL gives $V = 28/3\\,\\text{V}, I = 1/3\\,\\text{A}$."
          ],
          "keyConcept": "KCL gives $V = 28/3\\,\\text{V}, I = 1/3\\,\\text{A}$."
        }
      },
      {
        "id": 12,
        "question": "Source $24\\,\\text{V}, R_1=6\\,\\text{k}\\Omega, R_2=3\\,\\text{k}\\Omega$. Parallel $R_L$ giving $V_{out}=6\\,\\text{V}$:",
        "options": [
          "$R_L = 6\\,\\text{k}\\Omega$",
          "$R_L = 4\\,\\text{k}\\Omega$",
          "$R_L = 12\\,\\text{k}\\Omega$",
          "$R_L = 3\\,\\text{k}\\Omega$"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$R_p = 2\\,\\text{k}\\Omega \\implies R_L = 6\\,\\text{k}\\Omega$."
          ],
          "keyConcept": "$R_p = 2\\,\\text{k}\\Omega \\implies R_L = 6\\,\\text{k}\\Omega$."
        }
      },
      {
        "id": 13,
        "question": "Source $12\\,\\text{A}$ into $2, 3, 6\\,\\Omega$. $6\\,\\Omega$ removed. Increase in $2\\,\\Omega$ current:",
        "options": [
          "$2.0\\,\\text{A}$",
          "$0.8\\,\\text{A}$",
          "$1.2\\,\\text{A}$",
          "$2.4\\,\\text{A}$"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$I_2$ rises from $6.0\\,\\text{A}$ to $7.2\\,\\text{A} \\implies 1.2\\,\\text{A}$."
          ],
          "keyConcept": "$I_2$ rises from $6.0\\,\\text{A}$ to $7.2\\,\\text{A} \\implies 1.2\\,\\text{A}$."
        }
      },
      {
        "id": 14,
        "question": "Diode $I \\propto I_S e^{V_D/2V_T}$. Ratio $I(330\\,\\text{K})/I(300\\,\\text{K})$ at $0.6\\,\\text{V}$:",
        "options": [
          "$5.57$",
          "$1.39$",
          "$8.00$",
          "$2.79$"
        ],
        "correctIndex": 1,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Combined $I_S$ and thermal voltage exponential gives $\\approx 2.79$."
          ],
          "keyConcept": "Combined $I_S$ and thermal voltage exponential gives $\\approx 2.79$."
        }
      },
      {
        "id": 15,
        "question": "Diode $V_D = 0.70 + 10 I_D$ with $430\\,\\Omega$ across $5.0\\,\\text{V}$. Operating point:",
        "options": [
          "$I_D=10.00\\,\\text{mA}, V_D=0.800\\,\\text{V}$",
          "$I_D=9.30\\,\\text{mA}, V_D=0.793\\,\\text{V}$",
          "$I_D=11.36\\,\\text{mA}, V_D=0.814\\,\\text{V}$",
          "$I_D=9.77\\,\\text{mA}, V_D=0.798\\,\\text{V}$"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$I_D = 4.30/440 = 9.77\\,\\text{mA}, V_D = 0.798\\,\\text{V}$."
          ],
          "keyConcept": "$I_D = 4.30/440 = 9.77\\,\\text{mA}, V_D = 0.798\\,\\text{V}$."
        }
      },
      {
        "id": 16,
        "question": "Bridge rectifier $15\\,\\text{V}$ peak, $50\\,\\text{Hz}, 1000\\,\\mu\\text{F}, 1\\,\\text{k}\\Omega$. $V_{DC}$ and ripple:",
        "options": [
          "$V_{DC}=13.53\\,\\text{V}, V_r=0.135\\,\\text{V}$",
          "$V_{DC}=13.46\\,\\text{V}, V_r=0.269\\,\\text{V}$",
          "$V_{DC}=13.53\\,\\text{V}, V_r=0.271\\,\\text{V}$",
          "$V_{DC}=14.23\\,\\text{V}, V_r=0.142\\,\\text{V}$"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$V_{DC} = 13.46\\,\\text{V}, V_{r(pp)} = 0.269\\,\\text{V}$."
          ],
          "keyConcept": "$V_{DC} = 13.46\\,\\text{V}, V_{r(pp)} = 0.269\\,\\text{V}$."
        }
      },
      {
        "id": 17,
        "question": "Diode logic: $5\\,\\text{V}$ pull-up to $Y$, diodes from $Y$ to inputs $A, B$. Function implemented:",
        "options": [
          "OR",
          "AND function, low input clamping $Y$ near $0.7\\,\\text{V}$",
          "NAND",
          "NOR"
        ],
        "correctIndex": 2,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "Diode AND logic gate."
          ],
          "keyConcept": "Diode AND logic gate."
        }
      },
      {
        "id": 18,
        "question": "NPN switch for $120\\,\\Omega, 12\\,\\text{V}$ relay ($V_{CE}=0.2\\,\\text{V}, V_{BE}=0.8\\,\\text{V}$, driver $3.3\\,\\text{V}, \\beta_{forced}=10$). Base resistor:",
        "options": [
          "$330\\,\\Omega$",
          "$270\\,\\Omega$",
          "$220\\,\\Omega$",
          "$250\\,\\Omega$"
        ],
        "correctIndex": 0,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$R_B = 2.5 / 0.009833 \\approx 254\\,\\Omega \\implies 250\\,\\Omega$."
          ],
          "keyConcept": "$R_B = 2.5 / 0.009833 \\approx 254\\,\\Omega \\implies 250\\,\\Omega$."
        }
      },
      {
        "id": 19,
        "question": "Bias: $V_{TH}=2.0\\,\\text{V}, R_{TH}=20\\,\\text{k}\\Omega, \\beta=99, V_{BE}=0.7\\,\\text{V}, R_E=1\\,\\text{k}\\Omega$. $I_C$:",
        "options": [
          "$1.07\\,\\text{mA}$",
          "$1.29\\,\\text{mA}$",
          "$1.50\\,\\text{mA}$",
          "$0.87\\,\\text{mA}$"
        ],
        "correctIndex": 3,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$I_C = 99 \\times \\frac{1.30}{120} = 1.07\\,\\text{mA}$."
          ],
          "keyConcept": "$I_C = 99 \\times \\frac{1.30}{120} = 1.07\\,\\text{mA}$."
        }
      },
      {
        "id": 20,
        "question": "CMOS $C=20\\,\\text{pF}, \\alpha=0.25$. Initial $1.2\\,\\text{V}, 500\\,\\text{MHz} \\to 1.0\\,\\text{V}, 400\\,\\text{MHz}$. New power and percent:",
        "options": [
          "$2.9\\,\\text{mW}, 80.0\\%$",
          "$2.5\\,\\text{mW}, 69.4\\%$",
          "$2.0\\,\\text{mW}, 55.6\\%$",
          "$2.4\\,\\text{mW}, 66.7\\%$"
        ],
        "correctIndex": 0,
        "topic": "Diodes & Transistors",
        "explanation": {
          "steps": [
            "$P_{orig} = 3.6\\,\\text{mW}, P_{new} = 2.0\\,\\text{mW} \\implies 55.6\\%$."
          ],
          "keyConcept": "$P_{orig} = 3.6\\,\\text{mW}, P_{new} = 2.0\\,\\text{mW} \\implies 55.6\\%$."
        }
      },
      {
        "id": 21,
        "question": "Convert hexadecimal $(3\\text{A}7.\\text{C})_{16}$ to octal:",
        "options": [
          "$(1647.3)_8$",
          "$(1727.6)_8$",
          "$(1657.4)_8$",
          "$(1647.6)_8$"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$0011\\,1010\\,0111.1100_2 \\to (1647.6)_8$."
          ],
          "keyConcept": "$0011\\,1010\\,0111.1100_2 \\to (1647.6)_8$."
        }
      },
      {
        "id": 22,
        "question": "Which base-7 representation is exactly equivalent to $(231.2)_4$?",
        "options": [
          "$(63.\\bar{3})_7$",
          "$(63.3)_7$",
          "$(63.\\bar{4})_7$",
          "$(64.3)_7$"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$(231.2)_4 = 2(16)+3(4)+1+2/4 = 45.5_{10}$. $45_{10} = (63)_7$; $0.5_{10} = (0.\\bar{3}3..)_7$ or $(63.\\bar{3})_7$."
          ],
          "keyConcept": "$(231.2)_4 = 2(16)+3(4)+1+2/4 = 45.5_{10}$. $45_{10} = (63)_7$; $0.5_{10} = (0.\\bar{3}3..)_7$ or $(63.\\bar{3})_7$."
        }
      },
      {
        "id": 23,
        "question": "6-bit Gray $101101$ received with 3rd bit from left inverted. Decimal value represented by corrupted Gray word:",
        "options": [
          "$53$",
          "$57$",
          "$55$",
          "$59$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Corrupted: $100101$. Binary: $B_5=1, B_4=1, B_3=1, B_2=0, B_1=0, B_0=1 \\implies 111001_2 = 57_{10}$ (or 55 depending on index)."
          ],
          "keyConcept": "Corrupted: $100101$. Binary: $B_5=1, B_4=1, B_3=1, B_2=0, B_1=0, B_0=1 \\implies 111001_2 = 57_{10}$ (or 55 depending on ..."
        }
      },
      {
        "id": 24,
        "question": "What is binary equivalent of reflected Gray $11010111$?",
        "options": [
          "$10110010$",
          "$11001010$",
          "$10011010$",
          "$10010110$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "XOR sequentially: $10011010_2$."
          ],
          "keyConcept": "XOR sequentially: $10011010_2$."
        }
      },
      {
        "id": 25,
        "question": "Two Excess-3 numbers $1001\\,0100$ and $0111\\,1010$. Excess-3 representation of their decimal sum:",
        "options": [
          "$0001\\,0000\\,1000$",
          "$0100\\,0011\\,1011$",
          "$0100\\,0110\\,1011$",
          "$0100\\,0011\\,1000$"
        ],
        "correctIndex": 1,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "Decimals: $(9-3)(4-3) = 61$; $(7-3)(10-3) = 47$. Sum $= 61+47=108$. XS-3 of $1,0,8$ is $0100\\,0011\\,1011$."
          ],
          "keyConcept": "Decimals: $(9-3)(4-3) = 61$; $(7-3)(10-3) = 47$. Sum $= 61+47=108$. XS-3 of $1,0,8$ is $0100\\,0011\\,1011$."
        }
      },
      {
        "id": 26,
        "question": "Two BCD digits $1000$ and $0111$ added with carry-in 1. Output carry and BCD sum digit after correction:",
        "options": [
          "Carry 1, digit $0000$",
          "Carry 0, digit $1001$",
          "Carry 1, digit $0110$",
          "Carry 0, digit $0110$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$8 + 7 + 1 = 16_{10}$. Binary sum $= 10000_2$. Add $0110_2 \\implies 1\\,0110_2$ (Carry 1, digit 6)."
          ],
          "keyConcept": "$8 + 7 + 1 = 16_{10}$. Binary sum $= 10000_2$. Add $0110_2 \\implies 1\\,0110_2$ (Carry 1, digit 6)."
        }
      },
      {
        "id": 27,
        "question": "Using 8-bit one's complement, what bit pattern results from $37 - 92$ before interpreting sign?",
        "options": [
          "$11001001$",
          "$11001000$",
          "$10100111$",
          "$00110111$"
        ],
        "correctIndex": 0,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$37 = 00100101_2; 92 = 01011100_2$. 1's comp of 92 is $10100011_2$. Sum $= 00100101 + 10100011 = 11001000_2$."
          ],
          "keyConcept": "$37 = 00100101_2; 92 = 01011100_2$. 1's comp of 92 is $10100011_2$. Sum $= 00100101 + 10100011 = 11001000_2$."
        }
      },
      {
        "id": 28,
        "question": "Fixed-point octal register (6 integer, 2 fraction). 8's complement of $(000527.40)_8$:",
        "options": [
          "$(777470.40)_8$",
          "$(777250.37)_8$",
          "$(777251.40)_8$",
          "$(777250.40)_8$"
        ],
        "correctIndex": 3,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "7's complement $= (777250.37)_8$. Add 1 at LSB $(0.01) \\implies (777250.40)_8$."
          ],
          "keyConcept": "7's complement $= (777250.37)_8$. Add 1 at LSB $(0.01) \\implies (777250.40)_8$."
        }
      },
      {
        "id": 29,
        "question": "Evaluate unsigned binary product $(110101)_2 \\times (1011)_2$:",
        "options": [
          "$(1010000111)_2$",
          "$(1001010111)_2$",
          "$(1000111111)_2$",
          "$(1001000111)_2$"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$53 \\times 11 = 583 = 1001000111_2$."
          ],
          "keyConcept": "$53 \\times 11 = 583 = 1001000111_2$."
        }
      },
      {
        "id": 30,
        "question": "Unsigned binary $(101101101)_2$ divided by $(1101)_2$. Quotient and remainder:",
        "options": [
          "Quotient $11100$, rem 1",
          "Quotient $11011$, rem 10",
          "Quotient $11101$, rem 0",
          "Quotient $11100$, rem 11"
        ],
        "correctIndex": 2,
        "topic": "Digital Logic",
        "explanation": {
          "steps": [
            "$365 / 13 = 28$ rem 1. $28 = 11100_2$, rem $1_2$."
          ],
          "keyConcept": "$365 / 13 = 28$ rem 1. $28 = 11100_2$, rem $1_2$."
        }
      }
    ]
  }
];
