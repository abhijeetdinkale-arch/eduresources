/**
 * Official PHY175: Physics Practice & Formulae Midterm Mock Examination Suite
 * Contains Full-Length 30-Question Tests
 * Modelled on actual University Midterm Examination Papers & Formula Companion
 * Focuses strictly on Units 1-3:
 *   Unit 1: Solid State Physics, Energy Bands, Fermi Energy & Hall Effect
 *   Unit 2: Electronic Devices, Diode Circuits, Rectifiers, Filters & BJTs
 *   Unit 3: Number Systems, Boolean Algebra, Logic Gates & K-Maps
 * Authentic +1 / -0.25 marking scheme and detailed step-by-step solutions.
 */

export const PHY175_MOCK_TESTS = [
  {
    id: 'phy175-midterm-paper-1',
    code: 'PHY175-MIDTERM-1',
    title: 'Midterm Examination • Paper 1 (Official University Model)',
    courseCode: 'PHY175',
    courseName: 'Physics Practice & Formulae',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['Solid State Physics', 'Hall Effect', 'Rectifiers & Filters', 'BJT Electronics', 'Logic Gates & Number Systems'],
    description: 'Comprehensive midterm paper testing Fermi level, Hall voltage derivations, full-wave bridge rectifier ripple factor, BJT alpha/beta relationships, and 2\'s complement binary arithmetic.',
    questions: [
      {
        id: 1,
        question: 'Fermi energy (E_F) at absolute zero temperature (0 K) represents:',
        options: [
          'The maximum kinetic energy possessed by electrons in a conduction band at 0 K',
          'The average thermal energy of lattice ions',
          'The energy required to break a covalent bond',
          'The minimum energy of the valence band'
        ],
        correctIndex: 0,
        topic: 'Solid State Physics',
        explanation: {
          steps: [
            'At T = 0 K, all electronic states up to E_F are completely filled with probability f(E) = 1.',
            'All states above E_F are completely empty with f(E) = 0.',
            'Thus, E_F at 0 K is the highest occupied energy level.'
          ],
          keyConcept: 'Fermi energy at 0 K is the maximum occupied electron energy level.'
        }
      },
      {
        id: 2,
        question: 'A 3D free electron gas at 0 K has electron concentration n₁. If the concentration is increased to 8n₁, the Fermi energy becomes:',
        options: ['2 E_F1', '4 E_F1', '8 E_F1', '16 E_F1'],
        correctIndex: 1,
        topic: 'Solid State Physics',
        explanation: {
          steps: [
            'Fermi energy formula: E_F = (ℏ² / 2m) (3π² n)^(2/3).',
            'E_F is proportional to n^(2/3).',
            'E_F2 / E_F1 = (n₂ / n₁)^(2/3) = (8)^(2/3) = (2³)^(2/3) = 2² = 4.',
            'Therefore, E_F2 = 4 E_F1.'
          ],
          keyConcept: 'E_F ∝ n^(2/3). An 8-fold density increase quadruples Fermi energy.'
        }
      },
      {
        id: 3,
        question: 'What is the primary difference between a Direct and an Indirect band gap semiconductor?',
        options: [
          'In direct band gap, the conduction band minimum and valence band maximum occur at the same crystal momentum (k = 0), allowing efficient photon emission',
          'Direct band gap semiconductors cannot emit light',
          'Indirect band gap semiconductors have higher optical emission efficiency',
          'There is no difference in momentum'
        ],
        correctIndex: 0,
        topic: 'Solid State Physics',
        explanation: {
          steps: [
            'Direct band gap (e.g. GaAs): Electron drops directly without phonon assistance (conservation of momentum). Ideal for LEDs and lasers.',
            'Indirect band gap (e.g. Si, Ge): Requires a phonon (lattice vibration) to conserve momentum, making radiative recombination inefficient.'
          ],
          keyConcept: 'Direct bandgap enables direct radiative recombination without phonons.'
        }
      },
      {
        id: 4,
        question: 'The sign of the Hall coefficient (R_H) in a semiconductor specimen is significant because it directly reveals:',
        options: [
          'The type of majority charge carriers (negative for electrons, positive for holes)',
          'The temperature of the specimen',
          'The crystal orientation only',
          'The magnitude of the applied magnetic field'
        ],
        correctIndex: 0,
        topic: 'Hall Effect',
        explanation: {
          steps: [
            'Hall coefficient: R_H = 1 / (n q).',
            'For electrons (q = -e), R_H is negative (N-type semiconductor).',
            'For holes (q = +e), R_H is positive (P-type semiconductor).'
          ],
          keyConcept: 'Sign of R_H determines N-type vs P-type carrier nature.'
        }
      },
      {
        id: 5,
        question: 'In an intrinsic semiconductor, electron mobility is 3 times hole mobility (μ_e = 3 μ_h). What percentage of total electrical conductivity is contributed by electrons?',
        options: ['25%', '50%', '75%', '100%'],
        correctIndex: 2,
        topic: 'Solid State Physics',
        explanation: {
          steps: [
            'Total conductivity σ = n_i e (μ_e + μ_h).',
            'Conductivity due to electrons σ_e = n_i e μ_e = n_i e (3 μ_h).',
            'Fraction = σ_e / σ = (3 μ_h) / (3 μ_h + μ_h) = 3/4 = 0.75 = 75%.'
          ],
          keyConcept: 'Electrons contribute 75% of total conductivity when μ_e = 3 μ_h.'
        }
      },
      {
        id: 6,
        question: 'A full-wave bridge rectifier is supplied with a 50 Hz AC mains sinusoidal input. What is the fundamental ripple frequency of the output DC voltage across the load?',
        options: ['25 Hz', '50 Hz', '100 Hz', '200 Hz'],
        correctIndex: 2,
        topic: 'Rectifiers & Filters',
        explanation: {
          steps: [
            'In a full-wave rectifier, both positive and negative half-cycles are rectified into the same polarity.',
            'Thus, output pulses appear twice per AC cycle: f_ripple = 2 × f_in = 2 × 50 Hz = 100 Hz.'
          ],
          keyConcept: 'Full-wave ripple frequency = 2 × input frequency.'
        }
      },
      {
        id: 7,
        question: 'What is the ripple factor (r) of an ideal full-wave rectifier without a filter capacitor?',
        options: ['1.21', '0.482', '0.05', '0.01'],
        correctIndex: 1,
        topic: 'Rectifiers & Filters',
        explanation: {
          steps: [
            'Ripple factor formula: r = √((V_rms / V_dc)² - 1).',
            'For half-wave: r = 1.21.',
            'For full-wave: V_rms = V_m / √2, V_dc = 2 V_m / π ⇒ r = √((π / 2√2)² - 1) = √(1.2337 - 1) ≈ 0.482.'
          ],
          keyConcept: 'Full-wave ripple factor = 0.482 (48.2%).'
        }
      },
      {
        id: 8,
        question: 'What is the 8-bit Two\'s Complement representation of decimal integer -25?',
        options: ['11100111', '00011001', '11100110', '10011001'],
        correctIndex: 0,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            '1. Decimal +25 in 8-bit binary: 00011001.',
            '2. One\'s complement (invert bits): 11100110.',
            '3. Two\'s complement (add 1): 11100110 + 1 = 11100111.'
          ],
          keyConcept: 'Two\'s complement = One\'s complement + 1.'
        }
      },
      {
        id: 9,
        question: 'According to De Morgan\'s First Law of Boolean algebra, the complement of a sum equals:',
        options: [
          'The product of the complements: (A + B)\' = A\' · B\'',
          'The sum of the complements: (A · B)\' = A\' + B\'',
          'A + B',
          'A · B'
        ],
        correctIndex: 0,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'De Morgan\'s 1st theorem: (A + B)\' = A\' · B\'. (NOR is equivalent to bubbled AND).',
            'De Morgan\'s 2nd theorem: (A · B)\' = A\' + B\'. (NAND is equivalent to bubbled OR).'
          ],
          keyConcept: 'NOR = Bubbled AND: (A + B)\' = A\' · B\'.'
        }
      },
      {
        id: 10,
        question: 'Which logic gate produces a HIGH (1) output if and only if an ODD number of its binary inputs are HIGH (1)?',
        options: ['AND Gate', 'OR Gate', 'XOR (Exclusive-OR) Gate', 'XNOR Gate'],
        correctIndex: 2,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'The XOR gate (modulo-2 adder) outputs 1 when the inputs differ (for 2 inputs: 0⊕1 = 1, 1⊕0 = 1, but 0⊕0 = 0, 1⊕1 = 0).',
            'In multi-input XOR gates, output is HIGH whenever parity is odd.'
          ],
          keyConcept: 'XOR gate is an odd parity detector.'
        }
      },
      {
        id: 11,
        question: 'Why are NAND and NOR gates designated as "Universal Logic Gates"?',
        options: [
          'Because any Boolean function and all basic gates (AND, OR, NOT) can be implemented using exclusively NAND or exclusively NOR gates',
          'Because they operate on AC voltages',
          'Because they have infinite input resistance',
          'Because they consume zero propagation delay'
        ],
        correctIndex: 0,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'Connecting both inputs of a NAND gate together creates a NOT gate.',
            'Followed by another NAND yields an AND gate.',
            'De Morgan\'s inversion creates an OR gate.',
            'Hence, NAND and NOR gates are universal.'
          ],
          keyConcept: 'Universal gates can synthesize all Boolean logic gates.'
        }
      },
      {
        id: 12,
        question: 'In a Bipolar Junction Transistor (BJT), what is the relationship between base-to-collector current gain β and emitter-to-collector current gain α?',
        options: [
          'β = α / (1 - α)',
          'β = α / (1 + α)',
          'α = β / (1 - β)',
          'α = 1 + β'
        ],
        correctIndex: 0,
        topic: 'BJT Electronics',
        explanation: {
          steps: [
            'Emitter current I_E = I_B + I_C.',
            'By definition: α = I_C / I_E and β = I_C / I_B.',
            'Dividing I_E by I_C: 1/α = (1/β) + 1 = (1 + β) / β.',
            'Inverting yields α = β / (1 + β), and solving for β gives β = α / (1 - α).'
          ],
          keyConcept: 'β = α / (1 - α) and α = β / (1 + β).'
        }
      },
      {
        id: 13,
        question: 'If a transistor has α = 0.98, what is its corresponding Common Emitter current gain β?',
        options: ['49', '50', '98', '100'],
        correctIndex: 0,
        topic: 'BJT Electronics',
        explanation: {
          steps: [
            'β = α / (1 - α) = 0.98 / (1 - 0.98) = 0.98 / 0.02 = 98 / 2 = 49.'
          ],
          keyConcept: 'When α = 0.98, β = 49.'
        }
      },
      {
        id: 14,
        question: 'In a Common Emitter (CE) BJT amplifier, what is the phase shift between the input AC base signal and the output AC collector voltage?',
        options: ['0° (In phase)', '90°', '180° (Out of phase)', '270°'],
        correctIndex: 2,
        topic: 'BJT Electronics',
        explanation: {
          steps: [
            'As input base voltage increases, base current increases, which increases collector current I_C.',
            'The voltage drop across collector load resistor (I_C R_C) increases, causing output voltage V_CE = V_CC - I_C R_C to drop.',
            'This introduces a 180° phase inversion.'
          ],
          keyConcept: 'CE amplifier provides 180° phase inversion.'
        }
      },
      {
        id: 15,
        question: 'A rectangular copper strip of thickness t = 0.1 mm carries current I = 10 A in magnetic field B = 1.2 T. If electron density n = 8.5 × 10²⁸ m⁻³, the measured Hall voltage V_H is:',
        options: ['8.82 μV', '88.2 mV', '1.24 V', '0.55 μV'],
        correctIndex: 0,
        topic: 'Hall Effect',
        explanation: {
          steps: [
            'Formula: V_H = (I B) / (n q t)',
            'Numerator = 10 A × 1.2 T = 12.',
            'Denominator = (8.5 × 10²⁸) × (1.602 × 10⁻¹⁹ C) × (0.1 × 10⁻³ m)',
            'Denominator = 1.3617 × 10⁶.',
            'V_H = 12 / (1.3617 × 10⁶) = 8.812 × 10⁻⁶ V ≈ 8.82 μV.'
          ],
          keyConcept: 'V_H = (I B) / (n q t).'
        }
      },
      {
        id: 16,
        question: 'Convert hexadecimal (3A7.C)₁₆ into decimal representation:',
        options: ['935.75', '855.25', '920.50', '1024.75'],
        correctIndex: 0,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'Integer part: 3 × 16² + A(10) × 16¹ + 7 × 16⁰',
            '= 3(256) + 10(16) + 7 = 768 + 160 + 7 = 935.',
            'Fractional part: C(12) × 16⁻¹ = 12 / 16 = 3 / 4 = 0.75.',
            'Total decimal = 935.75.'
          ],
          keyConcept: 'Hex to decimal positional evaluation.'
        }
      },
      {
        id: 17,
        question: 'The minimum number of 2-input NAND gates required to construct a 2-input XOR gate is:',
        options: ['3', '4', '5', '6'],
        correctIndex: 1,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'A XOR B = A\'B + AB\' = (A + B)(A\' + B\') = (A(AB)\')\' · (B(AB)\')\'.',
            'This standard optimal realization requires exactly 4 NAND gates.'
          ],
          keyConcept: 'Exactly 4 NAND gates construct a 2-input XOR gate.'
        }
      },
      {
        id: 18,
        question: 'In a 4-variable Karnaugh Map (K-map), grouping an isolated block of 8 adjacent 1s (an Octet) eliminates how many variables?',
        options: ['1 variable', '2 variables', '3 variables', '4 variables'],
        correctIndex: 2,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'Grouping 2^k cells eliminates k variables.',
            'Pair (2 cells) eliminates 1 variable (2¹).',
            'Quad (4 cells) eliminates 2 variables (2²).',
            'Octet (8 cells = 2³) eliminates 3 variables, leaving a single literal.'
          ],
          keyConcept: 'An octet (8 cells) eliminates 3 Boolean variables.'
        }
      },
      {
        id: 19,
        question: 'What is the Peak Inverse Voltage (PIV) rating required for each diode in a Center-Tapped full-wave rectifier delivering peak secondary voltage V_m?',
        options: ['V_m', '2 V_m', 'V_m / 2', '√2 V_m'],
        correctIndex: 1,
        topic: 'Rectifiers & Filters',
        explanation: {
          steps: [
            'In a center-tapped transformer rectifier, during the reverse half-cycle, the non-conducting diode experiences the full secondary winding voltage across both halves: PIV = 2 V_m.',
            'In contrast, a Bridge rectifier requires PIV = V_m.'
          ],
          keyConcept: 'Center-tapped rectifier PIV = 2 V_m; Bridge rectifier PIV = V_m.'
        }
      },
      {
        id: 20,
        question: 'Which capacitor filter parameter directly controls the peak-to-peak ripple voltage V_r in a full-wave power supply?',
        options: [
          'V_r = I_dc / (2 f C)',
          'V_r = 2 f C / I_dc',
          'V_r = I_dc · 2 f C',
          'V_r = f C / (2 I_dc)'
        ],
        correctIndex: 0,
        topic: 'Rectifiers & Filters',
        explanation: {
          steps: [
            'Ripple voltage V_r(pp) is given by: V_r = I_dc / (2 f C) = V_dc / (2 f R_L C).',
            'Increasing filter capacitance C or frequency f reduces ripple voltage.'
          ],
          keyConcept: 'V_r = I_dc / (2 f C).'
        }
      },
      {
        id: 21,
        question: 'In semiconductor physics, what is the relationship between the intrinsic carrier concentration n_i, electron concentration n, and hole concentration p under thermal equilibrium?',
        options: ['n · p = n_i²', 'n + p = n_i', 'n / p = n_i²', 'n · p = 2 n_i'],
        correctIndex: 0,
        topic: 'Solid State Physics',
        explanation: {
          steps: [
            'By the Mass Action Law, the product of electron and hole concentrations in a semiconductor under thermal equilibrium is constant at a given temperature: n · p = n_i².'
          ],
          keyConcept: 'Mass Action Law: n · p = n_i².'
        }
      },
      {
        id: 22,
        question: 'The Fermi-Dirac distribution function f(E) gives the probability that an electronic state at energy E is occupied. At temperature T > 0 K, when energy E = E_F:',
        options: ['f(E) = 1.0', 'f(E) = 0.5 (50%)', 'f(E) = 0', 'f(E) = 0.707'],
        correctIndex: 1,
        topic: 'Solid State Physics',
        explanation: {
          steps: [
            'f(E) = 1 / [1 + e^((E - E_F) / (k_B T))].',
            'When E = E_F, the exponent is e^0 = 1.',
            'f(E_F) = 1 / (1 + 1) = 1/2 = 0.5.'
          ],
          keyConcept: 'At E = E_F, occupation probability is exactly 50% for T > 0 K.'
        }
      },
      {
        id: 23,
        question: 'In Boolean algebra, what is the simplified result of the expression: A + A\' B?',
        options: ['A', 'B', 'A + B', 'A · B'],
        correctIndex: 2,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'By the distributive law: A + A\' B = (A + A\')(A + B).',
            'Since A + A\' = 1, this simplifies to: 1 · (A + B) = A + B.'
          ],
          keyConcept: 'Redundancy law: A + A\'B = A + B.'
        }
      },
      {
        id: 24,
        question: 'What is the binary product of binary numbers 1011₂ (11) and 101₂ (5)?',
        options: ['110111₂ (55)', '110001₂', '101101₂', '111111₂'],
        correctIndex: 0,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            '1011₂ × 101₂:',
            '  1011',
            '+ 00000',
            '+ 101100',
            '= 110111₂ (which equals 32 + 16 + 4 + 2 + 1 = 55 in decimal).'
          ],
          keyConcept: 'Binary multiplication: 11 × 5 = 55 = 110111₂.'
        }
      },
      {
        id: 25,
        question: 'Which diode breakdown mechanism occurs in heavily doped PN junctions with narrow depletion layers under reverse electric fields of ~10⁶ V/m?',
        options: ['Zener breakdown (quantum tunneling)', 'Avalanche breakdown (impact ionization)', 'Thermal runaway', 'Punch-through'],
        correctIndex: 0,
        topic: 'Electronic Devices',
        explanation: {
          steps: [
            'Heavy doping makes the depletion layer ultra-thin (< 10 nm).',
            'Strong electric fields pull valence electrons directly across the forbidden gap via quantum mechanical tunneling (Zener effect, typically < 5-6 V).'
          ],
          keyConcept: 'Zener breakdown occurs via tunneling in heavily doped junctions.'
        }
      },
      {
        id: 26,
        question: 'In a BJT operating in the active amplification region, the emitter-base junction and collector-base junction are biased respectively as:',
        options: [
          'Emitter-Base: Forward Biased; Collector-Base: Reverse Biased',
          'Emitter-Base: Reverse Biased; Collector-Base: Forward Biased',
          'Both Forward Biased',
          'Both Reverse Biased'
        ],
        correctIndex: 0,
        topic: 'BJT Electronics',
        explanation: {
          steps: [
            'Active mode: EBJ Forward biased (injects carriers from emitter into thin base), CBJ Reverse biased (sweeps carriers across into collector).'
          ],
          keyConcept: 'Active Region: Emitter-Base is Forward Biased, Collector-Base is Reverse Biased.'
        }
      },
      {
        id: 27,
        question: 'The Gray Code representation of binary number 1011₂ is:',
        options: ['1110₂', '1101₂', '1111₂', '1001₂'],
        correctIndex: 0,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'Gray code conversion algorithm:',
            'Most significant bit remains same: G₃ = B₃ = 1.',
            'G₂ = B₃ ⊕ B₂ = 1 ⊕ 0 = 1.',
            'G₁ = B₂ ⊕ B₁ = 0 ⊕ 1 = 1.',
            'G₀ = B₁ ⊕ B₀ = 1 ⊕ 1 = 0.',
            'Resulting Gray code: 1110₂.'
          ],
          keyConcept: 'Binary to Gray: G_i = B_(i+1) ⊕ B_i.'
        }
      },
      {
        id: 28,
        question: 'What is the ripple frequency of a 3-phase full-wave bridge rectifier operating on a 50 Hz power supply?',
        options: ['150 Hz', '300 Hz', '600 Hz', '100 Hz'],
        correctIndex: 1,
        topic: 'Rectifiers & Filters',
        explanation: {
          steps: [
            'A 3-phase full-wave bridge rectifier (6-pulse converter) produces 6 DC pulses per AC cycle.',
            'f_ripple = 6 × 50 Hz = 300 Hz.'
          ],
          keyConcept: '3-phase bridge rectifier ripple frequency = 6 × f_supply = 300 Hz.'
        }
      },
      {
        id: 29,
        question: 'The Hall mobility (μ_H) of charge carriers is related to the Hall coefficient (R_H) and conductivity (σ) by:',
        options: ['μ_H = R_H · σ', 'μ_H = R_H / σ', 'μ_H = σ / R_H', 'μ_H = √(R_H · σ)'],
        correctIndex: 0,
        topic: 'Hall Effect',
        explanation: {
          steps: [
            'Since R_H = 1 / (n e) and σ = n e μ, multiplying gives R_H · σ = [1 / (n e)] · (n e μ) = μ_H.'
          ],
          keyConcept: 'Hall mobility μ_H = R_H · σ.'
        }
      },
      {
        id: 30,
        question: 'In a digital system, a "Don\'t Care" condition (indicated by X) in a K-map:',
        options: [
          'Can be treated as either 0 or 1, whichever yields a larger group and simpler minimal expression',
          'Must always be set to 1',
          'Must always be set to 0',
          'Causes an invalid hardware fault'
        ],
        correctIndex: 0,
        topic: 'Logic Gates & Number Systems',
        explanation: {
          steps: [
            'Don\'t-care input combinations never occur in normal operation, so the designer can assign 1 or 0 to enlarge prime implicants and minimize gate count.'
          ],
          keyConcept: 'Don\'t cares can be grouped as 1 or ignored as 0 for maximal simplification.'
        }
      }
    ]
  }
];
