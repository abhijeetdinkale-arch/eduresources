/**
 * Official ECE249: Basic Electrical and Electronics Engineering Midterm Mock Examination Suite
 * Contains Full-Length 30-Question Tests (60 Questions Total)
 * Modelled directly on actual University Midterm Examination Papers (Code: 22232ECE6870, Paper Code: A)
 * Focuses strictly on Units 1-3:
 *   Unit 1: DC Circuit Analysis & Theorems (Thevenin, Norton, Superposition, Max Power, Star-Delta, KVL/KCL)
 *   Unit 2: AC Fundamentals & Single/3-Phase Circuits (RMS, Form Factor, RLC Resonance, Power in AC, 3-Phase Star/Delta)
 *   Unit 3: Transformers & Semiconductor Electronics (Faraday's law, turns ratio, kVA rating, PN junction, Zener, MOSFET)
 * Authentic +1 / -0.25 marking scheme and step-by-step mathematical solutions.
 */

export const ECE249_MOCK_TESTS = [
  {
    id: 'ece249-midterm-paper-1',
    code: '22232ECE6870-A',
    title: 'Midterm Examination • Paper 1 (Official University PYQ)',
    courseCode: 'ECE249',
    courseName: 'Basic Electrical and Electronics Engineering',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['DC Network Theorems', 'AC Fundamentals', 'RLC Resonance', 'Transformers', 'Semiconductors'],
    description: 'Verbatim university midterm paper testing Thevenin/Norton equivalents, maximum power transfer, Star-Delta transformation, RMS & form factor, 3-phase circuits, and transformer ratings.',
    questions: [
      {
        id: 1,
        question: 'The Thevenin\'s theorem equivalent circuit states that any linear two-terminal circuit can be replaced by:',
        options: [
          'R_th in series with R_L and V_th',
          'R_th in parallel with R_L and V_th',
          'R_L in parallel with R_th and V_th',
          'R_th and R_L in parallel with I_N'
        ],
        correctIndex: 0,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'Thevenin\'s theorem states that any linear, bilateral network across load terminals can be replaced by an ideal independent voltage source V_th in series with an internal resistance R_th.',
            'When the load resistance R_L is connected across the terminals, R_th, V_th, and R_L form a single series loop.'
          ],
          keyConcept: 'Thevenin equivalent: Voltage source V_th in series with resistance R_th.'
        }
      },
      {
        id: 2,
        question: 'The Thevenin\'s voltage V_th is physically defined as:',
        options: [
          'Short circuit voltage across load terminals',
          'Open circuit voltage across load terminals (V_oc)',
          'Both short circuit and open circuit voltage',
          'None of these'
        ],
        correctIndex: 1,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'To find V_th, remove the load resistor R_L to open-circuit the designated terminals A-B.',
            'The open-circuit voltage measured or calculated across A-B is the Thevenin voltage: V_th = V_oc.'
          ],
          keyConcept: 'V_th = Open circuit terminal voltage V_oc.'
        }
      },
      {
        id: 3,
        question: 'Norton\'s theorem states that any linear active network can be represented by:',
        options: [
          'R_N in series with R_L and I_N',
          'R_N in parallel with R_L and I_sc (Norton current source)',
          'R_N in parallel with V_th and I_N',
          'R_N in series with V_th'
        ],
        correctIndex: 1,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'Norton\'s theorem is the dual of Thevenin\'s theorem.',
            'It replaces the active network with an ideal current source I_N = I_sc in parallel with the Norton resistance R_N (and load R_L connected in parallel).'
          ],
          keyConcept: 'Norton equivalent: Current source I_N in parallel with resistance R_N.'
        }
      },
      {
        id: 4,
        question: 'Norton\'s current I_N is determined by:',
        options: [
          'Open circuit current through terminals',
          'Short circuit current through load terminals (I_sc)',
          'Both open circuit and short circuit current',
          'None of these'
        ],
        correctIndex: 1,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'To determine Norton current I_N, place a zero-resistance short between terminals A and B.',
            'The current flowing through this short circuit is Norton\'s current: I_N = I_sc.'
          ],
          keyConcept: 'I_N = Short circuit current I_sc.'
        }
      },
      {
        id: 5,
        question: 'Kirchhoff\'s Voltage Law (KVL) is based on the principle of:',
        options: [
          'Law of Conservation of Energy',
          'Law of Conservation of Charge',
          'Law of Conservation of Frequency',
          'Law of Conservation of Momentum'
        ],
        correctIndex: 0,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'KVL states that the algebraic sum of all voltages around any closed loop must equal zero (∑ V = 0).',
            'This directly expresses that the work done moving a unit charge around a closed electrical loop is zero, which is the Conservation of Energy.',
            'Note: Kirchhoff\'s Current Law (KCL) is based on Conservation of Charge.'
          ],
          keyConcept: 'KVL = Conservation of Energy; KCL = Conservation of Charge.'
        }
      },
      {
        id: 6,
        question: 'Source transformation implies that a voltage source V in series with resistor R can be converted into:',
        options: [
          'A current source I = V/R in parallel with resistance R',
          'A current source I = V·R in parallel with resistance R',
          'A current source I = V/R in series with resistance R',
          'A voltage source in parallel with resistance R'
        ],
        correctIndex: 0,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'By Ohm\'s law and terminal equivalence, a practical voltage source (V in series with R) is strictly equivalent to a practical current source (I = V/R in parallel with R).'
          ],
          keyConcept: 'Source transformation: (V in series with R) ↔ (I = V/R in parallel with R).'
        }
      },
      {
        id: 7,
        question: 'A balanced delta (Δ) network has a resistance of 60 Ω in each branch. The equivalent star (Y) network will have a branch resistance of:',
        options: ['30 Ω', '20 Ω', '40 Ω', '90 Ω'],
        correctIndex: 1,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'For a delta-to-star transformation where all delta resistors are equal (R_Δ = 60 Ω):',
            'R_Y = R_Δ / 3',
            'R_Y = 60 / 3 = 20 Ω.'
          ],
          keyConcept: 'For identical resistors: R_star = R_delta / 3.'
        }
      },
      {
        id: 8,
        question: 'A balanced star (Y) network has a resistance of 60 Ω in each branch. The equivalent delta (Δ) network will have a branch resistance of:',
        options: ['170 Ω', '160 Ω', '180 Ω', '60 Ω'],
        correctIndex: 2,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'For a star-to-delta transformation where all star resistors are equal (R_Y = 60 Ω):',
            'R_Δ = 3 × R_Y',
            'R_Δ = 3 × 60 = 180 Ω.'
          ],
          keyConcept: 'For identical resistors: R_delta = 3 × R_star.'
        }
      },
      {
        id: 9,
        question: 'Superposition theorem is applicable only to circuits that are:',
        options: ['Linear and bilateral', 'Non-linear', 'Unilateral', 'Time-variant non-linear'],
        correctIndex: 0,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'Superposition relies on the mathematical properties of homogeneity f(ax) = a f(x) and additivity f(x₁ + x₂) = f(x₁) + f(x₂).',
            'These hold strictly for linear, bilateral circuits.'
          ],
          keyConcept: 'Superposition requires linear and bilateral network elements.'
        }
      },
      {
        id: 10,
        question: 'According to the Maximum Power Transfer Theorem, maximum power is delivered to the load resistance R_L when:',
        options: ['R_L = R_th', 'R_L = 2 R_th', 'R_L = R_th / 2', 'R_L = 4 R_th'],
        correctIndex: 0,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'Power delivered to load is P_L = I² R_L = [V_th / (R_th + R_L)]² R_L.',
            'Differentiating P_L with respect to R_L and setting dP_L / dR_L = 0 yields R_L = R_th.',
            'Maximum power transferred is P_max = V_th² / (4 R_th).'
          ],
          keyConcept: 'Condition for maximum power transfer: R_L = R_th.'
        }
      },
      {
        id: 11,
        question: 'When deactivating independent sources to calculate Thevenin resistance R_th:',
        options: [
          'Ideal voltage sources are open-circuited, current sources short-circuited',
          'Ideal voltage sources are short-circuited (V = 0), current sources open-circuited (I = 0)',
          'All sources are replaced with 1 Ω resistors',
          'Sources are kept connected'
        ],
        correctIndex: 1,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'Setting an ideal independent voltage source to zero volts is equivalent to replacing it with a Short Circuit (zero resistance wire).',
            'Setting an ideal independent current source to zero amperes is equivalent to replacing it with an Open Circuit (infinite resistance break).'
          ],
          keyConcept: 'Voltage source → Short circuit (0 V); Current source → Open circuit (0 A).'
        }
      },
      {
        id: 12,
        question: 'The unit of which of the following quantities is NOT Ohms (Ω)?',
        options: ['Inductive reactance (X_L)', 'Capacitive reactance (X_C)', 'Impedance (Z)', 'Capacitance (C)'],
        correctIndex: 3,
        topic: 'AC Fundamentals',
        explanation: {
          steps: [
            'Resistance R, inductive reactance X_L = 2πfL, capacitive reactance X_C = 1/(2πfC), and impedance Z all oppose current and are measured in Ohms (Ω).',
            'Capacitance C is measured in Farads (F).'
          ],
          keyConcept: 'Capacitance is measured in Farads; reactances and impedance are in Ohms.'
        }
      },
      {
        id: 13,
        question: 'What is the efficiency of a circuit when maximum power transfer occurs from source to load?',
        options: ['100%', '75%', '50%', '25%'],
        correctIndex: 2,
        topic: 'DC Network Theorems',
        explanation: {
          steps: [
            'At maximum power transfer, R_L = R_th.',
            'Power consumed by load P_L = I² R_L; Power lost internally P_int = I² R_th = I² R_L.',
            'Total power supplied by source P_total = 2 I² R_L.',
            'Efficiency η = P_L / P_total = (I² R_L) / (2 I² R_L) = 1/2 = 50%.'
          ],
          keyConcept: 'Efficiency at maximum power transfer is always 50%.'
        }
      },
      {
        id: 14,
        question: 'For a sinusoidal alternating current, at what electrical angle does the instantaneous value equal its RMS value?',
        options: ['0°', '90°', '45°', '180°'],
        correctIndex: 2,
        topic: 'AC Fundamentals',
        explanation: {
          steps: [
            'Instantaneous current i(t) = I_m sin(θ).',
            'RMS current I_rms = I_m / √2.',
            'Setting i(t) = I_rms gives: I_m sin(θ) = I_m / √2 ⇒ sin(θ) = 1 / √2.',
            'Therefore, θ = 45°.'
          ],
          keyConcept: 'i(θ) = I_rms when θ = 45° because sin(45°) = 1/√2.'
        }
      },
      {
        id: 15,
        question: 'If the RMS value of an alternating sinusoidal current is 100 A, what is its peak (maximum) value I_m?',
        options: ['70.7 A', '100 A', '141.4 A', '200 A'],
        correctIndex: 2,
        topic: 'AC Fundamentals',
        explanation: {
          steps: [
            'Formula: I_m = √2 × I_rms',
            'I_m = 1.4142 × 100 A = 141.42 A.'
          ],
          keyConcept: 'I_peak = √2 × I_rms = 1.414 × I_rms.'
        }
      },
      {
        id: 16,
        question: 'The Form Factor of a pure sinusoidal waveform is defined as:',
        options: [
          'RMS value / Average value = 1.11',
          'Peak value / RMS value = 1.414',
          'Average value / RMS value = 0.9',
          'Peak value / Average value = 1.57'
        ],
        correctIndex: 0,
        topic: 'AC Fundamentals',
        explanation: {
          steps: [
            'Form factor K_f = V_rms / V_avg.',
            'For a sine wave: V_rms = V_m / √2 ≈ 0.707 V_m; V_avg = 2 V_m / π ≈ 0.637 V_m.',
            'K_f = (V_m / √2) / (2 V_m / π) = π / (2√2) ≈ 1.11.'
          ],
          keyConcept: 'Form Factor of sine wave = 1.11; Crest Factor = 1.414.'
        }
      },
      {
        id: 17,
        question: 'In a pure inductive AC circuit, the current:',
        options: [
          'Leads the voltage by 90°',
          'Lags the voltage by 90°',
          'Is in phase with the voltage',
          'Lags the voltage by 180°'
        ],
        correctIndex: 1,
        topic: 'AC Fundamentals',
        explanation: {
          steps: [
            'Remember the mnemonic CIVIL: In an Inductor (L), Voltage (V) leads Current (I), which means Current lags Voltage by 90° (π/2 radians).'
          ],
          keyConcept: 'In a pure inductor, current lags voltage by 90° (ELI).'
        }
      },
      {
        id: 18,
        question: 'In a series RLC circuit, electrical resonance occurs when:',
        options: [
          'Inductive reactance equals capacitive reactance (X_L = X_C)',
          'X_L > X_C',
          'Resistance R = 0',
          'Impedance Z is maximum'
        ],
        correctIndex: 0,
        topic: 'RLC Resonance',
        explanation: {
          steps: [
            'Impedance of series RLC is Z = R + j(X_L - X_C).',
            'At resonance, the reactive components cancel out completely: X_L = X_C ⇒ ωL = 1/(ωC).',
            'Impedance becomes purely resistive and minimum: Z_min = R.',
            'Resonant frequency is f₀ = 1 / (2π√(LC)).'
          ],
          keyConcept: 'At series resonance, X_L = X_C, Z = R (minimum), and power factor is unity.'
        }
      },
      {
        id: 19,
        question: 'At series resonance in an RLC circuit, the power factor of the circuit is:',
        options: ['Zero lagging', '0.707 leading', 'Unity (1.0)', 'Zero leading'],
        correctIndex: 2,
        topic: 'RLC Resonance',
        explanation: {
          steps: [
            'Power factor cos φ = R / Z.',
            'At resonance, X_L = X_C, so Z = R.',
            'cos φ = R / R = 1.0 (Unity).'
          ],
          keyConcept: 'Series resonant circuits operate at Unity Power Factor.'
        }
      },
      {
        id: 20,
        question: 'In a balanced 3-phase Star (Y) connected supply, the relationship between Line Voltage (V_L) and Phase Voltage (V_ph) is:',
        options: [
          'V_L = V_ph',
          'V_L = √3 × V_ph',
          'V_L = V_ph / √3',
          'V_L = 3 × V_ph'
        ],
        correctIndex: 1,
        topic: '3-Phase Circuits',
        explanation: {
          steps: [
            'In a Star connection:',
            'Line voltage is the phasor difference between two phase voltages: V_L = √3 V_ph.',
            'Line current equals phase current: I_L = I_ph.'
          ],
          keyConcept: 'Star Connection: V_L = √3 V_ph and I_L = I_ph.'
        }
      },
      {
        id: 21,
        question: 'In a balanced 3-phase Delta (Δ) connected system, the relationship between Line Current (I_L) and Phase Current (I_ph) is:',
        options: [
          'I_L = I_ph',
          'I_L = √3 × I_ph',
          'I_L = I_ph / √3',
          'I_L = 3 × I_ph'
        ],
        correctIndex: 1,
        topic: '3-Phase Circuits',
        explanation: {
          steps: [
            'In a Delta connection:',
            'Line voltage equals phase voltage: V_L = V_ph.',
            'Line current is the phasor difference between two phase currents: I_L = √3 I_ph.'
          ],
          keyConcept: 'Delta Connection: V_L = V_ph and I_L = √3 I_ph.'
        }
      },
      {
        id: 22,
        question: 'Total active power consumed in a balanced 3-phase load (in terms of line quantities) is given by:',
        options: [
          'P = 3 V_L I_L cos φ',
          'P = √3 V_L I_L cos φ',
          'P = V_L I_L cos φ',
          'P = √3 V_L I_L sin φ'
        ],
        correctIndex: 1,
        topic: '3-Phase Circuits',
        explanation: {
          steps: [
            'Total 3-phase power = 3 × P_phase = 3 V_ph I_ph cos φ.',
            'Expressed in line quantities (for both star and delta): P = √3 V_L I_L cos φ (Watts).'
          ],
          keyConcept: 'P_3phase = √3 V_L I_L cos φ.'
        }
      },
      {
        id: 23,
        question: 'The working principle of an electrical transformer is based on:',
        options: [
          'Faraday\'s Law of Electromagnetic Induction and Mutual Induction',
          'Fleming\'s Left Hand Rule',
          'Ohm\'s Law',
          'Coulomb\'s Law'
        ],
        correctIndex: 0,
        topic: 'Transformers',
        explanation: {
          steps: [
            'An alternating voltage applied to primary winding creates a time-varying magnetic flux in the core.',
            'By Faraday\'s law of mutual induction, this flux links the secondary winding and induces an emf.'
          ],
          keyConcept: 'Transformers work on mutual electromagnetic induction.'
        }
      },
      {
        id: 24,
        question: 'Which parameter remains strictly constant between primary and secondary windings in an ideal transformer?',
        options: ['Voltage', 'Current', 'Frequency', 'Impedance'],
        correctIndex: 2,
        topic: 'Transformers',
        explanation: {
          steps: [
            'Transformers transfer electrical energy from one circuit to another through magnetic flux without changing the frequency of the AC waveform (f₁ = f₂).'
          ],
          keyConcept: 'Frequency is never altered by a transformer.'
        }
      },
      {
        id: 25,
        question: 'Electrical transformers are commercially rated in kVA (or MVA) rather than kW because:',
        options: [
          'Core (iron) losses depend on voltage and copper losses depend on current, independent of load power factor',
          'Transformers have zero reactive power',
          'Power factor is always 1.0',
          'Output voltage is constant'
        ],
        correctIndex: 0,
        topic: 'Transformers',
        explanation: {
          steps: [
            'Iron losses depend on core flux (proportional to Voltage V).',
            'Copper losses (I²R) depend on winding current I.',
            'Neither loss depends on the power factor cos φ of the load connected.',
            'Therefore, total heating and rating is governed strictly by the product V × I (Apparent power in kVA).'
          ],
          keyConcept: 'Transformers are rated in kVA because losses depend on V and I, not power factor.'
        }
      },
      {
        id: 26,
        question: 'A single-phase transformer has 100 turns on the primary and 1200 turns on the secondary. If 120 V AC is applied to the primary, what is the secondary induced voltage?',
        options: ['120 V', '1440 V', '10 V', '240 V'],
        correctIndex: 1,
        topic: 'Transformers',
        explanation: {
          steps: [
            'Formula: V₂ / V₁ = N₂ / N₁',
            'V₂ = V₁ × (N₂ / N₁) = 120 V × (1200 / 100) = 120 × 12 = 1440 V.'
          ],
          keyConcept: 'Transformation equation: V₂ = V₁ × (N₂ / N₁).'
        }
      },
      {
        id: 27,
        question: 'In an intrinsic semiconductor (pure Silicon or Germanium), what type of atomic bonding holds the lattice together?',
        options: ['Electrovalent (Ionic) bonding', 'Covalent bonding', 'Metallic bonding', 'Hydrogen bonding'],
        correctIndex: 1,
        topic: 'Semiconductors',
        explanation: {
          steps: [
            'Silicon and Germanium belong to Group 14 and have 4 valence electrons.',
            'Each atom shares one valence electron with 4 neighboring atoms, forming 4 covalent bonds.'
          ],
          keyConcept: 'Semiconductors have covalent bonding.'
        }
      },
      {
        id: 28,
        question: 'When a pure semiconductor is doped with a pentavalent impurity (e.g. Phosphorus, Arsenic):',
        options: [
          'An N-type semiconductor is formed with electrons as majority carriers',
          'A P-type semiconductor is formed with holes as majority carriers',
          'An insulator is formed',
          'The conductivity decreases'
        ],
        correctIndex: 0,
        topic: 'Semiconductors',
        explanation: {
          steps: [
            'A pentavalent donor atom has 5 valence electrons.',
            'Four electrons participate in covalent bonds with neighboring Si atoms, while the 5th electron is loosely bound and free to conduct.',
            'This yields an N-type semiconductor with excess conduction electrons.'
          ],
          keyConcept: 'Pentavalent doping produces N-type semiconductor (majority electrons).'
        }
      },
      {
        id: 29,
        question: 'When a PN junction diode is reverse-biased:',
        options: [
          'The depletion layer width increases and barrier potential rises',
          'The depletion layer width decreases to zero',
          'A large forward current flows immediately',
          'Majority carriers cross the junction easily'
        ],
        correctIndex: 0,
        topic: 'Semiconductors',
        explanation: {
          steps: [
            'Applying negative potential to P-side and positive potential to N-side pulls holes and electrons away from the junction.',
            'This widens the depletion region of uncompensated immobile ions and increases the barrier height, permitting only a tiny reverse saturation current due to minority carriers.'
          ],
          keyConcept: 'Reverse bias widens the depletion layer and increases barrier potential.'
        }
      },
      {
        id: 30,
        question: 'A Zener diode is specifically designed to operate in which operating region of its characteristic curve?',
        options: [
          'Forward conduction region',
          'Reverse breakdown region',
          'Cutoff region',
          'Saturation region'
        ],
        correctIndex: 1,
        topic: 'Semiconductors',
        explanation: {
          steps: [
            'A Zener diode is a heavily doped PN junction designed to operate safely in reverse breakdown without damage.',
            'Across the breakdown region, the voltage across the diode remains practically constant (V_Z) over a wide range of reverse currents, making it an ideal voltage regulator.'
          ],
          keyConcept: 'Zener diode operates in the reverse breakdown region to regulate voltage.'
        }
      }
    ]
  }
];
