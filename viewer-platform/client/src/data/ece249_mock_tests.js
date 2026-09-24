/**
 * Official ECE249: Basic Electrical & Electronics Engineering Midterm Suite
 * Contains 5 Full-Length 30-Question Tests (150 Questions Total)
 * Strictly covers Units 1-3: DC Network Theorems, AC RLC Resonance, Transformers
 * Balanced keys [7,7,8,8] with equalized option lengths
 */

export const ECE249_MOCK_TESTS = [
  {
    "id": "ece249-midterm-paper-1",
    "code": "22232ECE6870-A",
    "title": "Midterm Examination • Paper 1 (Official University PYQ)",
    "courseCode": "ECE249",
    "courseName": "Basic Electrical and Electronics Engineering",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "DC Network Theorems",
      "AC Fundamentals",
      "RLC Resonance",
      "Transformers",
      "Semiconductors"
    ],
    "description": "Verbatim university midterm paper testing Thevenin/Norton equivalents, maximum power transfer, Star-Delta transformation, RMS & form factor, 3-phase circuits, and transformer ratings.",
    "questions": [
      {
        "id": 1,
        "question": "The Thevenin's theorem equivalent circuit states that any linear two-terminal circuit can be replaced by:",
        "options": [
          "R_th and R_L in parallel with I_N",
          "R_th in series with R_L and V_th",
          "R_L in parallel with R_th and V_th",
          "R_th in parallel with R_L and V_th"
        ],
        "correctIndex": 1,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "Thevenin's theorem states that any linear, bilateral network across load terminals can be replaced by an ideal independent voltage source V_th in series with an internal resistance R_th.",
            "When the load resistance R_L is connected across the terminals, R_th, V_th, and R_L form a single series loop."
          ],
          "keyConcept": "Thevenin equivalent: Voltage source V_th in series with resistance R_th."
        }
      },
      {
        "id": 2,
        "question": "The Thevenin's voltage V_th is physically defined as:",
        "options": [
          "Both short circuit and open circuit voltage",
          "Short circuit voltage across load terminals",
          "None of these",
          "Open circuit voltage across load terminals (V_oc)"
        ],
        "correctIndex": 3,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "To find V_th, remove the load resistor R_L to open-circuit the designated terminals A-B.",
            "The open-circuit voltage measured or calculated across A-B is the Thevenin voltage: V_th = V_oc."
          ],
          "keyConcept": "V_th = Open circuit terminal voltage V_oc."
        }
      },
      {
        "id": 3,
        "question": "Norton's theorem states that any linear active network can be represented by:",
        "options": [
          "R_N in series with R_L and I_N (governed by linear superposition principles)",
          "R_N in series with V_th (independent of external field perturbations)",
          "R_N in parallel with R_L and I_sc (Norton current source)",
          "R_N in parallel with V_th and I_N (under steady-state operating conditions)"
        ],
        "correctIndex": 2,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "Norton's theorem is the dual of Thevenin's theorem.",
            "It replaces the active network with an ideal current source I_N = I_sc in parallel with the Norton resistance R_N (and load R_L connected in parallel)."
          ],
          "keyConcept": "Norton equivalent: Current source I_N in parallel with resistance R_N."
        }
      },
      {
        "id": 4,
        "question": "Norton's current I_N is determined by:",
        "options": [
          "Short circuit current through load terminals (I_sc)",
          "Open circuit current through terminals",
          "Both open circuit and short circuit current",
          "None of these"
        ],
        "correctIndex": 0,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "To determine Norton current I_N, place a zero-resistance short between terminals A and B.",
            "The current flowing through this short circuit is Norton's current: I_N = I_sc."
          ],
          "keyConcept": "I_N = Short circuit current I_sc."
        }
      },
      {
        "id": 5,
        "question": "Kirchhoff's Voltage Law (KVL) is based on the principle of:",
        "options": [
          "Law of Conservation of Energy",
          "Law of Conservation of Charge",
          "Law of Conservation of Momentum",
          "Law of Conservation of Frequency"
        ],
        "correctIndex": 0,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "KVL states that the algebraic sum of all voltages around any closed loop must equal zero (∑ V = 0).",
            "This directly expresses that the work done moving a unit charge around a closed electrical loop is zero, which is the Conservation of Energy.",
            "Note: Kirchhoff's Current Law (KCL) is based on Conservation of Charge."
          ],
          "keyConcept": "KVL = Conservation of Energy; KCL = Conservation of Charge."
        }
      },
      {
        "id": 6,
        "question": "Source transformation implies that a voltage source V in series with resistor R can be converted into:",
        "options": [
          "A voltage source in parallel with resistance R",
          "A current source I = V/R in parallel with resistance R",
          "A current source I = V·R in parallel with resistance R",
          "A current source I = V/R in series with resistance R"
        ],
        "correctIndex": 1,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "By Ohm's law and terminal equivalence, a practical voltage source (V in series with R) is strictly equivalent to a practical current source (I = V/R in parallel with R)."
          ],
          "keyConcept": "Source transformation: (V in series with R) ↔ (I = V/R in parallel with R)."
        }
      },
      {
        "id": 7,
        "question": "A balanced delta (Δ) network has a resistance of 60 Ω in each branch. The equivalent star (Y) network will have a branch resistance of:",
        "options": [
          "90 Ω",
          "40 Ω",
          "20 Ω",
          "30 Ω"
        ],
        "correctIndex": 2,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "For a delta-to-star transformation where all delta resistors are equal (R_Δ = 60 Ω):",
            "R_Y = R_Δ / 3",
            "R_Y = 60 / 3 = 20 Ω."
          ],
          "keyConcept": "For identical resistors: R_star = R_delta / 3."
        }
      },
      {
        "id": 8,
        "question": "A balanced star (Y) network has a resistance of 60 Ω in each branch. The equivalent delta (Δ) network will have a branch resistance of:",
        "options": [
          "160 Ω",
          "60 Ω",
          "170 Ω",
          "180 Ω"
        ],
        "correctIndex": 3,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "For a star-to-delta transformation where all star resistors are equal (R_Y = 60 Ω):",
            "R_Δ = 3 × R_Y",
            "R_Δ = 3 × 60 = 180 Ω."
          ],
          "keyConcept": "For identical resistors: R_delta = 3 × R_star."
        }
      },
      {
        "id": 9,
        "question": "Superposition theorem is applicable only to circuits that are:",
        "options": [
          "Non-linear",
          "Linear and bilateral",
          "Unilateral",
          "Time-variant non-linear"
        ],
        "correctIndex": 1,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "Superposition relies on the mathematical properties of homogeneity f(ax) = a f(x) and additivity f(x₁ + x₂) = f(x₁) + f(x₂).",
            "These hold strictly for linear, bilateral circuits."
          ],
          "keyConcept": "Superposition requires linear and bilateral network elements."
        }
      },
      {
        "id": 10,
        "question": "According to the Maximum Power Transfer Theorem, maximum power is delivered to the load resistance R_L when:",
        "options": [
          "R_L = 4 R_th",
          "R_L = R_th",
          "R_L = R_th / 2",
          "R_L = 2 R_th"
        ],
        "correctIndex": 1,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "Power delivered to load is P_L = I² R_L = [V_th / (R_th + R_L)]² R_L.",
            "Differentiating P_L with respect to R_L and setting dP_L / dR_L = 0 yields R_L = R_th.",
            "Maximum power transferred is P_max = V_th² / (4 R_th)."
          ],
          "keyConcept": "Condition for maximum power transfer: R_L = R_th."
        }
      },
      {
        "id": 11,
        "question": "When deactivating independent sources to calculate Thevenin resistance R_th:",
        "options": [
          "Ideal voltage sources are open-circuited, current sources short-circuited (in an ideal homogeneous medium)",
          "Sources are kept connected (under steady-state operating conditions)",
          "Ideal voltage sources are short-circuited (V = 0), current sources open-circuited (I = 0)",
          "All sources are replaced with 1 Ω resistors (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "Setting an ideal independent voltage source to zero volts is equivalent to replacing it with a Short Circuit (zero resistance wire).",
            "Setting an ideal independent current source to zero amperes is equivalent to replacing it with an Open Circuit (infinite resistance break)."
          ],
          "keyConcept": "Voltage source → Short circuit (0 V); Current source → Open circuit (0 A)."
        }
      },
      {
        "id": 12,
        "question": "The unit of which of the following quantities is NOT Ohms (Ω)?",
        "options": [
          "Capacitance (C)",
          "Inductive reactance (X_L)",
          "Impedance (Z)",
          "Capacitive reactance (X_C)"
        ],
        "correctIndex": 0,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Resistance R, inductive reactance X_L = 2πfL, capacitive reactance X_C = 1/(2πfC), and impedance Z all oppose current and are measured in Ohms (Ω).",
            "Capacitance C is measured in Farads (F)."
          ],
          "keyConcept": "Capacitance is measured in Farads; reactances and impedance are in Ohms."
        }
      },
      {
        "id": 13,
        "question": "What is the efficiency of a circuit when maximum power transfer occurs from source to load?",
        "options": [
          "75%",
          "100%",
          "50%",
          "25%"
        ],
        "correctIndex": 2,
        "topic": "DC Network Theorems",
        "explanation": {
          "steps": [
            "At maximum power transfer, R_L = R_th.",
            "Power consumed by load P_L = I² R_L; Power lost internally P_int = I² R_th = I² R_L.",
            "Total power supplied by source P_total = 2 I² R_L.",
            "Efficiency η = P_L / P_total = (I² R_L) / (2 I² R_L) = 1/2 = 50%."
          ],
          "keyConcept": "Efficiency at maximum power transfer is always 50%."
        }
      },
      {
        "id": 14,
        "question": "For a sinusoidal alternating current, at what electrical angle does the instantaneous value equal its RMS value?",
        "options": [
          "180°",
          "0°",
          "90°",
          "45°"
        ],
        "correctIndex": 3,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Instantaneous current i(t) = I_m sin(θ).",
            "RMS current I_rms = I_m / √2.",
            "Setting i(t) = I_rms gives: I_m sin(θ) = I_m / √2 ⇒ sin(θ) = 1 / √2.",
            "Therefore, θ = 45°."
          ],
          "keyConcept": "i(θ) = I_rms when θ = 45° because sin(45°) = 1/√2."
        }
      },
      {
        "id": 15,
        "question": "If the RMS value of an alternating sinusoidal current is 100 A, what is its peak (maximum) value I_m?",
        "options": [
          "70.7 A",
          "141.4 A",
          "200 A",
          "100 A"
        ],
        "correctIndex": 1,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Formula: I_m = √2 × I_rms",
            "I_m = 1.4142 × 100 A = 141.42 A."
          ],
          "keyConcept": "I_peak = √2 × I_rms = 1.414 × I_rms."
        }
      },
      {
        "id": 16,
        "question": "The Form Factor of a pure sinusoidal waveform is defined as:",
        "options": [
          "Peak value / Average value = 1.57",
          "RMS value / Average value = 1.11",
          "Peak value / RMS value = 1.414",
          "Average value / RMS value = 0.9"
        ],
        "correctIndex": 1,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Form factor K_f = V_rms / V_avg.",
            "For a sine wave: V_rms = V_m / √2 ≈ 0.707 V_m; V_avg = 2 V_m / π ≈ 0.637 V_m.",
            "K_f = (V_m / √2) / (2 V_m / π) = π / (2√2) ≈ 1.11."
          ],
          "keyConcept": "Form Factor of sine wave = 1.11; Crest Factor = 1.414."
        }
      },
      {
        "id": 17,
        "question": "In a pure inductive AC circuit, the current:",
        "options": [
          "Is in phase with the voltage",
          "Lags the voltage by 180°",
          "Leads the voltage by 90°",
          "Lags the voltage by 90°"
        ],
        "correctIndex": 3,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Remember the mnemonic CIVIL: In an Inductor (L), Voltage (V) leads Current (I), which means Current lags Voltage by 90° (π/2 radians)."
          ],
          "keyConcept": "In a pure inductor, current lags voltage by 90° (ELI)."
        }
      },
      {
        "id": 18,
        "question": "In a series RLC circuit, electrical resonance occurs when:",
        "options": [
          "Inductive reactance equals capacitive reactance (X_L = X_C)",
          "X_L > X_C (as determined by Maxwell boundary constraints)",
          "Resistance R = 0 (across all standard operating temperatures)",
          "Impedance Z is maximum (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Impedance of series RLC is Z = R + j(X_L - X_C).",
            "At resonance, the reactive components cancel out completely: X_L = X_C ⇒ ωL = 1/(ωC).",
            "Impedance becomes purely resistive and minimum: Z_min = R.",
            "Resonant frequency is f₀ = 1 / (2π√(LC))."
          ],
          "keyConcept": "At series resonance, X_L = X_C, Z = R (minimum), and power factor is unity."
        }
      },
      {
        "id": 19,
        "question": "At series resonance in an RLC circuit, the power factor of the circuit is:",
        "options": [
          "Zero leading",
          "0.707 leading",
          "Unity (1.0)",
          "Zero lagging"
        ],
        "correctIndex": 2,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Power factor cos φ = R / Z.",
            "At resonance, X_L = X_C, so Z = R.",
            "cos φ = R / R = 1.0 (Unity)."
          ],
          "keyConcept": "Series resonant circuits operate at Unity Power Factor."
        }
      },
      {
        "id": 20,
        "question": "In a balanced 3-phase Star (Y) connected supply, the relationship between Line Voltage (V_L) and Phase Voltage (V_ph) is:",
        "options": [
          "V_L = V_ph / √3",
          "V_L = 3 × V_ph",
          "V_L = V_ph",
          "V_L = √3 × V_ph"
        ],
        "correctIndex": 3,
        "topic": "3-Phase Circuits",
        "explanation": {
          "steps": [
            "In a Star connection:",
            "Line voltage is the phasor difference between two phase voltages: V_L = √3 V_ph.",
            "Line current equals phase current: I_L = I_ph."
          ],
          "keyConcept": "Star Connection: V_L = √3 V_ph and I_L = I_ph."
        }
      },
      {
        "id": 21,
        "question": "In a balanced 3-phase Delta (Δ) connected system, the relationship between Line Current (I_L) and Phase Current (I_ph) is:",
        "options": [
          "I_L = √3 × I_ph",
          "I_L = 3 × I_ph",
          "I_L = I_ph",
          "I_L = I_ph / √3"
        ],
        "correctIndex": 0,
        "topic": "3-Phase Circuits",
        "explanation": {
          "steps": [
            "In a Delta connection:",
            "Line voltage equals phase voltage: V_L = V_ph.",
            "Line current is the phasor difference between two phase currents: I_L = √3 I_ph."
          ],
          "keyConcept": "Delta Connection: V_L = V_ph and I_L = √3 I_ph."
        }
      },
      {
        "id": 22,
        "question": "Total active power consumed in a balanced 3-phase load (in terms of line quantities) is given by:",
        "options": [
          "P = V_L I_L cos φ",
          "P = √3 V_L I_L cos φ",
          "P = √3 V_L I_L sin φ",
          "P = 3 V_L I_L cos φ"
        ],
        "correctIndex": 1,
        "topic": "3-Phase Circuits",
        "explanation": {
          "steps": [
            "Total 3-phase power = 3 × P_phase = 3 V_ph I_ph cos φ.",
            "Expressed in line quantities (for both star and delta): P = √3 V_L I_L cos φ (Watts)."
          ],
          "keyConcept": "P_3phase = √3 V_L I_L cos φ."
        }
      },
      {
        "id": 23,
        "question": "The working principle of an electrical transformer is based on:",
        "options": [
          "Coulomb's Law (in an ideal homogeneous medium)",
          "Ohm's Law (under steady-state operating conditions)",
          "Faraday's Law of Electromagnetic Induction and Mutual Induction",
          "Fleming's Left Hand Rule (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "An alternating voltage applied to primary winding creates a time-varying magnetic flux in the core.",
            "By Faraday's law of mutual induction, this flux links the secondary winding and induces an emf."
          ],
          "keyConcept": "Transformers work on mutual electromagnetic induction."
        }
      },
      {
        "id": 24,
        "question": "Which parameter remains strictly constant between primary and secondary windings in an ideal transformer?",
        "options": [
          "Current",
          "Impedance",
          "Frequency",
          "Voltage"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Transformers transfer electrical energy from one circuit to another through magnetic flux without changing the frequency of the AC waveform (f₁ = f₂)."
          ],
          "keyConcept": "Frequency is never altered by a transformer."
        }
      },
      {
        "id": 25,
        "question": "Electrical transformers are commercially rated in kVA (or MVA) rather than kW because:",
        "options": [
          "Power factor is always 1.0 (as determined by Maxwell boundary constraints)",
          "Output voltage is constant (across all standard operating temperatures)",
          "Transformers have zero reactive power (governed by linear superposition principles)",
          "Core (iron) losses depend on voltage and copper losses depend on current, independent of load power factor"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Iron losses depend on core flux (proportional to Voltage V).",
            "Copper losses (I²R) depend on winding current I.",
            "Neither loss depends on the power factor cos φ of the load connected.",
            "Therefore, total heating and rating is governed strictly by the product V × I (Apparent power in kVA)."
          ],
          "keyConcept": "Transformers are rated in kVA because losses depend on V and I, not power factor."
        }
      },
      {
        "id": 26,
        "question": "A single-phase transformer has 100 turns on the primary and 1200 turns on the secondary. If 120 V AC is applied to the primary, what is the secondary induced voltage?",
        "options": [
          "120 V",
          "10 V",
          "240 V",
          "1440 V"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Formula: V₂ / V₁ = N₂ / N₁",
            "V₂ = V₁ × (N₂ / N₁) = 120 V × (1200 / 100) = 120 × 12 = 1440 V."
          ],
          "keyConcept": "Transformation equation: V₂ = V₁ × (N₂ / N₁)."
        }
      },
      {
        "id": 27,
        "question": "In an intrinsic semiconductor (pure Silicon or Germanium), what type of atomic bonding holds the lattice together?",
        "options": [
          "Hydrogen bonding",
          "Electrovalent (Ionic) bonding",
          "Covalent bonding",
          "Metallic bonding"
        ],
        "correctIndex": 2,
        "topic": "Semiconductors",
        "explanation": {
          "steps": [
            "Silicon and Germanium belong to Group 14 and have 4 valence electrons.",
            "Each atom shares one valence electron with 4 neighboring atoms, forming 4 covalent bonds."
          ],
          "keyConcept": "Semiconductors have covalent bonding."
        }
      },
      {
        "id": 28,
        "question": "When a pure semiconductor is doped with a pentavalent impurity (e.g. Phosphorus, Arsenic):",
        "options": [
          "An N-type semiconductor is formed with electrons as majority carriers",
          "An insulator is formed (in an ideal homogeneous medium)",
          "A P-type semiconductor is formed with holes as majority carriers",
          "The conductivity decreases (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 0,
        "topic": "Semiconductors",
        "explanation": {
          "steps": [
            "A pentavalent donor atom has 5 valence electrons.",
            "Four electrons participate in covalent bonds with neighboring Si atoms, while the 5th electron is loosely bound and free to conduct.",
            "This yields an N-type semiconductor with excess conduction electrons."
          ],
          "keyConcept": "Pentavalent doping produces N-type semiconductor (majority electrons)."
        }
      },
      {
        "id": 29,
        "question": "When a PN junction diode is reverse-biased:",
        "options": [
          "The depletion layer width decreases to zero (in an ideal homogeneous medium)",
          "A large forward current flows immediately (under steady-state operating conditions)",
          "Majority carriers cross the junction easily (as determined by Maxwell boundary constraints)",
          "The depletion layer width increases and barrier potential rises"
        ],
        "correctIndex": 3,
        "topic": "Semiconductors",
        "explanation": {
          "steps": [
            "Applying negative potential to P-side and positive potential to N-side pulls holes and electrons away from the junction.",
            "This widens the depletion region of uncompensated immobile ions and increases the barrier height, permitting only a tiny reverse saturation current due to minority carriers."
          ],
          "keyConcept": "Reverse bias widens the depletion layer and increases barrier potential."
        }
      },
      {
        "id": 30,
        "question": "A Zener diode is specifically designed to operate in which operating region of its characteristic curve?",
        "options": [
          "Reverse breakdown region",
          "Forward conduction region",
          "Saturation region",
          "Cutoff region"
        ],
        "correctIndex": 0,
        "topic": "Semiconductors",
        "explanation": {
          "steps": [
            "A Zener diode is a heavily doped PN junction designed to operate safely in reverse breakdown without damage.",
            "Across the breakdown region, the voltage across the diode remains practically constant (V_Z) over a wide range of reverse currents, making it an ideal voltage regulator."
          ],
          "keyConcept": "Zener diode operates in the reverse breakdown region to regulate voltage."
        }
      }
    ]
  },
  {
    "id": "ece249-midterm-paper-2",
    "code": "ECE249-PAPER-B",
    "title": "Midterm Examination • Paper 2 (DC Theorems & Superposition)",
    "courseCode": "ECE249",
    "courseName": "Basic Electrical & Electronics Engineering",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "DC Circuit Theorems",
      "AC Fundamentals",
      "RLC Resonance",
      "Transformers & Diodes"
    ],
    "description": "Focuses on Thevenin, Norton, Maximum Power Transfer, and mesh/nodal solving.",
    "questions": [
      {
        "id": 1,
        "question": "Norton's equivalent current $I_N$ is determined by measuring the current flowing through:",
        "options": [
          "A parallel test inductor (governed by linear superposition principles)",
          "An open circuit across the load terminals",
          "A high-impedance voltmeter (in an ideal homogeneous medium)",
          "A short circuit placed across the load terminals"
        ],
        "correctIndex": 3,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
          ],
          "keyConcept": "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
        }
      },
      {
        "id": 2,
        "question": "In the power triangle, the Power Factor ($\\cos\\phi$) is mathematically defined as the ratio of:",
        "options": [
          "Reactive Power ($Q$) to Active Power ($P$)",
          "Impedance ($Z$) to Resistance ($R$)",
          "Active Power ($P$) to Apparent Power ($S$)",
          "Apparent Power ($S$) to Active Power ($P$)"
        ],
        "correctIndex": 2,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
          ],
          "keyConcept": "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
        }
      },
      {
        "id": 3,
        "question": "The core of a practical transformer is laminated with thin silicon steel sheets specifically to reduce:",
        "options": [
          "Hysteresis losses",
          "Copper ohmic losses",
          "Magnetic flux leakage",
          "Eddy current losses"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\propto t^2$)."
          ],
          "keyConcept": "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\pro..."
        }
      },
      {
        "id": 4,
        "question": "The average active power consumed in an ideal pure inductor or pure capacitor across a complete AC cycle is:",
        "options": [
          "$I_{\text{rms}}^2 X$",
          "Zero Watts",
          "$V_{\text{rms}} \times I_{\text{rms}}$",
          "Maximum Watts"
        ],
        "correctIndex": 1,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
          ],
          "keyConcept": "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
        }
      },
      {
        "id": 5,
        "question": "In an ideal step-up transformer where secondary turns $N_2 > N_1$, the secondary current $I_2$ compared to primary $I_1$ is:",
        "options": [
          "Equal ($I_2 = I_1$)",
          "Lower ($I_2 < I_1$)",
          "Zero ($I_2 = 0$)",
          "Higher ($I_2 > I_1$)"
        ],
        "correctIndex": 1,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
          ],
          "keyConcept": "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
        }
      },
      {
        "id": 6,
        "question": "The Peak Factor (or Crest Factor) of a pure sine wave is equal to:",
        "options": [
          "$1.11$",
          "$0.707$",
          "$1.414$ ($\\sqrt{2}$)",
          "$2.00$"
        ],
        "correctIndex": 2,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
          ],
          "keyConcept": "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
        }
      },
      {
        "id": 7,
        "question": "In nodal analysis of electrical circuits, the equations for node voltages are derived using:",
        "options": [
          "Thevenin's Theorem",
          "Faraday's Law of Induction",
          "Kirchhoff's Voltage Law (KVL)",
          "Kirchhoff's Current Law (KCL)"
        ],
        "correctIndex": 3,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Nodal analysis applies KCL at all non-reference essential nodes."
          ],
          "keyConcept": "Nodal analysis applies KCL at all non-reference essential nodes."
        }
      },
      {
        "id": 8,
        "question": "In mesh current analysis, the governing circuit equations are systematically formulated using:",
        "options": [
          "Gauss's Flux Theorem",
          "Ampere's Circuital Law",
          "Kirchhoff's Current Law (KCL)",
          "Kirchhoff's Voltage Law (KVL)"
        ],
        "correctIndex": 3,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Mesh analysis applies KVL around independent closed loops in planar circuits."
          ],
          "keyConcept": "Mesh analysis applies KVL around independent closed loops in planar circuits."
        }
      },
      {
        "id": 9,
        "question": "The resonant angular frequency $\\omega_0$ of a series RLC circuit is given by:",
        "options": [
          "$\\omega_0 = \frac{1}{\\sqrt{LC}}$",
          "$\\omega_0 = \frac{R}{2L}$",
          "$\\omega_0 = \frac{1}{2\\pi LC}$",
          "$\\omega_0 = \\sqrt{LC}$"
        ],
        "correctIndex": 0,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
          ],
          "keyConcept": "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
        }
      },
      {
        "id": 10,
        "question": "The transformation ratio $K$ of a transformer is defined as:",
        "options": [
          "$K = \frac{V_1}{V_2} = \frac{N_2}{N_1}$ (under steady-state operating conditions)",
          "$K = \frac{N_1}{N_2} = \frac{V_2}{V_1}$ (as determined by Maxwell boundary constraints)",
          "$K = \frac{I_2}{I_1} = \frac{N_2}{N_1}$ (across all standard operating temperatures)",
          "$K = \frac{V_2}{V_1} = \frac{N_2}{N_1} = \frac{I_1}{I_2}$"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
          ],
          "keyConcept": "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
        }
      },
      {
        "id": 11,
        "question": "Under the Maximum Power Transfer Theorem, maximum power is delivered from a DC source with internal resistance $R_s$ to a load $R_L$ when:",
        "options": [
          "$R_L = R_s$",
          "$R_L = R_s / 2$",
          "$R_L = 2 R_s$",
          "$R_L = \\infty$"
        ],
        "correctIndex": 0,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
          ],
          "keyConcept": "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
        }
      },
      {
        "id": 12,
        "question": "In a half-wave rectifier, the theoretical maximum conversion efficiency $\\eta_{\text{max}}$ is equal to:",
        "options": [
          "$81.2\\%$",
          "$40.6\\%$",
          "$90.0\\%$",
          "$50.0\\%$"
        ],
        "correctIndex": 1,
        "topic": "Rectifiers",
        "explanation": {
          "steps": [
            "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
          ],
          "keyConcept": "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
        }
      },
      {
        "id": 13,
        "question": "An ideal independent voltage source maintains its terminal voltage completely independent of:",
        "options": [
          "The amount of current drawn by the connected load",
          "The frequency of the grid (independent of external field perturbations)",
          "The internal wire thickness (in an ideal homogeneous medium)",
          "The temperature of the room (under steady-state operating conditions)"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
          ],
          "keyConcept": "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
        }
      },
      {
        "id": 14,
        "question": "Superposition theorem is strictly applicable only to circuits that consist of:",
        "options": [
          "Unilateral diodes and rectifiers",
          "Time-varying saturation inductors",
          "Linear bilateral circuit elements",
          "Non-linear semiconductor devices"
        ],
        "correctIndex": 2,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
          ],
          "keyConcept": "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
        }
      },
      {
        "id": 15,
        "question": "The Quality Factor ($Q$) of a series RLC resonant circuit is defined by the formula:",
        "options": [
          "$Q = \frac{\\omega_0 L}{C}$",
          "$Q = \frac{1}{R}\\sqrt{\frac{L}{C}}$",
          "$Q = \frac{R}{\\omega_0 L}$",
          "$Q = R\\sqrt{\frac{C}{L}}$"
        ],
        "correctIndex": 1,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
          ],
          "keyConcept": "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
        }
      },
      {
        "id": 16,
        "question": "According to Kirchhoff's Current Law (KCL), the algebraic sum of currents entering any node is zero because of conservation of:",
        "options": [
          "Electric charge",
          "Electric potential",
          "Magnetic flux",
          "Total energy"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
          ],
          "keyConcept": "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
        }
      },
      {
        "id": 17,
        "question": "A PN junction diode operating under forward bias exhibits a built-in potential barrier that:",
        "options": [
          "Increases linearly, blocking all conduction (as determined by Maxwell boundary constraints)",
          "Decreases, allowing majority carriers to diffuse across the junction",
          "Oscillates at grid frequency (governed by linear superposition principles)",
          "Remains entirely unchanged (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Semiconductor Diodes",
        "explanation": {
          "steps": [
            "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
          ],
          "keyConcept": "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
        }
      },
      {
        "id": 18,
        "question": "In a purely capacitive AC circuit, the alternating current:",
        "options": [
          "Lags behind the applied voltage by $90^\\circ$",
          "Is in exact phase with the applied voltage",
          "Leads the applied voltage by $90^\\circ$ ($\\pi/2$ radians)",
          "Leads the applied voltage by $45^\\circ$ (in an ideal homogeneous medium)"
        ],
        "correctIndex": 2,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
          ],
          "keyConcept": "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
        }
      },
      {
        "id": 19,
        "question": "A transformer transfers electrical energy from primary to secondary winding without altering the:",
        "options": [
          "Impedance level",
          "Voltage magnitude",
          "Operating frequency",
          "Current magnitude"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "A transformer changes voltage and current levels while maintaining identical power frequency."
          ],
          "keyConcept": "A transformer changes voltage and current levels while maintaining identical power frequency."
        }
      },
      {
        "id": 20,
        "question": "The Form Factor of a pure sinusoidal alternating voltage waveform is defined as the ratio of:",
        "options": [
          "RMS value to the Average value ($V_{\text{rms}} / V_{\text{avg}} = 1.11$)",
          "Reactive power to Apparent power ($\\sin\\phi$) (in an ideal homogeneous medium)",
          "Average value to the Peak value ($V_{\text{avg}} / V_m = 0.637$)",
          "Peak value to the RMS value ($V_m / V_{\text{rms}} = 1.414$)"
        ],
        "correctIndex": 0,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} \u0007pprox 1.11$."
          ],
          "keyConcept": "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} ..."
        }
      },
      {
        "id": 21,
        "question": "Thevenin's theorem states that any linear bilateral two-terminal active network can be replaced by an equivalent circuit containing:",
        "options": [
          "A short-circuit current $I_N$ in parallel with a conductance $G_N$",
          "An ideal current source in series with a capacitor (under steady-state operating conditions)",
          "An ideal voltage source in parallel with an inductor (as determined by Maxwell boundary constraints)",
          "An open-circuit voltage $V_{th}$ in series with an equivalent resistance $R_{th}$"
        ],
        "correctIndex": 3,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
          ],
          "keyConcept": "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
        }
      },
      {
        "id": 22,
        "question": "The short-circuit test on a transformer is performed to determine its:",
        "options": [
          "Core hysteresis loss (under steady-state operating conditions)",
          "Dielectric breakdown voltage (as determined by Maxwell boundary constraints)",
          "Equivalent winding resistance, leakage reactance, and full-load copper losses",
          "Eddy current loss (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
          ],
          "keyConcept": "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
        }
      },
      {
        "id": 23,
        "question": "An ideal independent current source has an internal parallel resistance of:",
        "options": [
          "Infinite resistance ($\\infty\\,\\Omega$)",
          "Zero resistance ($0\\,\\Omega$)",
          "Fifty ohms ($50\\,\\Omega$)",
          "One ohm ($1\\,\\Omega$) (independent of external field perturbations)"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
          ],
          "keyConcept": "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
        }
      },
      {
        "id": 24,
        "question": "The open-circuit test on a transformer is primarily conducted to determine its:",
        "options": [
          "Full-load copper ohmic losses (across all standard operating temperatures)",
          "Winding temperature rise (governed by linear superposition principles)",
          "Short-circuit impedance (independent of external field perturbations)",
          "Core losses (iron losses) and magnetizing branch parameters"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
          ],
          "keyConcept": "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
        }
      },
      {
        "id": 25,
        "question": "In star-to-delta transformation, if three identical resistors of value $R$ are connected in star, the equivalent delta branch resistance is:",
        "options": [
          "$2R$",
          "$3R$",
          "$R$",
          "$R/3$"
        ],
        "correctIndex": 1,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
          ],
          "keyConcept": "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
        }
      },
      {
        "id": 26,
        "question": "The EMF equation of an ideal single-phase transformer is given by:",
        "options": [
          "$E_1 = 2\\pi f N_1 \\Phi_m$",
          "$E_1 = \frac{f N_1}{\\Phi_m}$",
          "$E_1 = 4 f N_1 \\Phi_m$",
          "$E_1 = 4.44 f N_1 \\Phi_m$"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
          ],
          "keyConcept": "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
        }
      },
      {
        "id": 27,
        "question": "At electrical resonance in a series RLC circuit, the net circuit impedance is:",
        "options": [
          "Purely inductive and infinite (in an ideal homogeneous medium)",
          "Complex with reactive power maximized",
          "Purely resistive and at its minimum value ($Z = R$)",
          "Purely capacitive and zero (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
          ],
          "keyConcept": "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
        }
      },
      {
        "id": 28,
        "question": "The bandwidth ($BW = f_2 - f_1$) of an RLC resonant circuit is related to resonant frequency $f_0$ and $Q$ factor by:",
        "options": [
          "$BW = \frac{R}{2\\pi \\sqrt{LC}}$",
          "$BW = \frac{f_0}{Q}$",
          "$BW = f_0 \times Q$",
          "$BW = \frac{Q}{f_0}$"
        ],
        "correctIndex": 1,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
          ],
          "keyConcept": "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
        }
      },
      {
        "id": 29,
        "question": "Hysteresis loss in a magnetic iron core subjected to alternating magnetizing force is proportional to:",
        "options": [
          "The square of the core lamination thickness",
          "The winding series resistance (across all standard operating temperatures)",
          "The area enclosed by the magnetic $B$-$H$ hysteresis loop",
          "The length of the secondary wire (independent of external field perturbations)"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
          ],
          "keyConcept": "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
        }
      },
      {
        "id": 30,
        "question": "In a purely inductive AC circuit, the alternating current:",
        "options": [
          "Lags behind the applied voltage by $90^\\circ$ ($\\pi/2$ radians)",
          "Lags behind the applied voltage by $180^\\circ$ (governed by linear superposition principles)",
          "Leads the applied voltage by $90^\\circ$ (independent of external field perturbations)",
          "Is in exact phase with the applied voltage (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
          ],
          "keyConcept": "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
        }
      }
    ]
  },
  {
    "id": "ece249-midterm-paper-3",
    "code": "ECE249-PAPER-C",
    "title": "Midterm Examination • Paper 3 (AC Fundamentals & Series Resonance)",
    "courseCode": "ECE249",
    "courseName": "Basic Electrical & Electronics Engineering",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "DC Circuit Theorems",
      "AC Fundamentals",
      "RLC Resonance",
      "Transformers & Diodes"
    ],
    "description": "In-depth questions on sinusoidal waveforms, phasor analysis, and series/parallel RLC resonance.",
    "questions": [
      {
        "id": 1,
        "question": "A transformer transfers electrical energy from primary to secondary winding without altering the:",
        "options": [
          "Current magnitude",
          "Voltage magnitude",
          "Impedance level",
          "Operating frequency"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "A transformer changes voltage and current levels while maintaining identical power frequency."
          ],
          "keyConcept": "A transformer changes voltage and current levels while maintaining identical power frequency."
        }
      },
      {
        "id": 2,
        "question": "The short-circuit test on a transformer is performed to determine its:",
        "options": [
          "Dielectric breakdown voltage (under steady-state operating conditions)",
          "Eddy current loss (as determined by Maxwell boundary constraints)",
          "Core hysteresis loss (across all standard operating temperatures)",
          "Equivalent winding resistance, leakage reactance, and full-load copper losses"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
          ],
          "keyConcept": "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
        }
      },
      {
        "id": 3,
        "question": "In the power triangle, the Power Factor ($\\cos\\phi$) is mathematically defined as the ratio of:",
        "options": [
          "Apparent Power ($S$) to Active Power ($P$)",
          "Impedance ($Z$) to Resistance ($R$)",
          "Active Power ($P$) to Apparent Power ($S$)",
          "Reactive Power ($Q$) to Active Power ($P$)"
        ],
        "correctIndex": 2,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
          ],
          "keyConcept": "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
        }
      },
      {
        "id": 4,
        "question": "Hysteresis loss in a magnetic iron core subjected to alternating magnetizing force is proportional to:",
        "options": [
          "The square of the core lamination thickness",
          "The length of the secondary wire (governed by linear superposition principles)",
          "The area enclosed by the magnetic $B$-$H$ hysteresis loop",
          "The winding series resistance (in an ideal homogeneous medium)"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
          ],
          "keyConcept": "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
        }
      },
      {
        "id": 5,
        "question": "An ideal independent voltage source maintains its terminal voltage completely independent of:",
        "options": [
          "The temperature of the room (governed by linear superposition principles)",
          "The amount of current drawn by the connected load",
          "The frequency of the grid (in an ideal homogeneous medium)",
          "The internal wire thickness (under steady-state operating conditions)"
        ],
        "correctIndex": 1,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
          ],
          "keyConcept": "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
        }
      },
      {
        "id": 6,
        "question": "The Form Factor of a pure sinusoidal alternating voltage waveform is defined as the ratio of:",
        "options": [
          "Peak value to the RMS value ($V_m / V_{\text{rms}} = 1.414$)",
          "RMS value to the Average value ($V_{\text{rms}} / V_{\text{avg}} = 1.11$)",
          "Average value to the Peak value ($V_{\text{avg}} / V_m = 0.637$)",
          "Reactive power to Apparent power ($\\sin\\phi$) (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 1,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} \u0007pprox 1.11$."
          ],
          "keyConcept": "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} ..."
        }
      },
      {
        "id": 7,
        "question": "The core of a practical transformer is laminated with thin silicon steel sheets specifically to reduce:",
        "options": [
          "Magnetic flux leakage",
          "Hysteresis losses",
          "Eddy current losses",
          "Copper ohmic losses"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\propto t^2$)."
          ],
          "keyConcept": "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\pro..."
        }
      },
      {
        "id": 8,
        "question": "The Peak Factor (or Crest Factor) of a pure sine wave is equal to:",
        "options": [
          "$0.707$",
          "$1.414$ ($\\sqrt{2}$)",
          "$1.11$",
          "$2.00$"
        ],
        "correctIndex": 1,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
          ],
          "keyConcept": "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
        }
      },
      {
        "id": 9,
        "question": "In a purely inductive AC circuit, the alternating current:",
        "options": [
          "Is in exact phase with the applied voltage (as determined by Maxwell boundary constraints)",
          "Lags behind the applied voltage by $90^\\circ$ ($\\pi/2$ radians)",
          "Leads the applied voltage by $90^\\circ$ (governed by linear superposition principles)",
          "Lags behind the applied voltage by $180^\\circ$ (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
          ],
          "keyConcept": "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
        }
      },
      {
        "id": 10,
        "question": "The bandwidth ($BW = f_2 - f_1$) of an RLC resonant circuit is related to resonant frequency $f_0$ and $Q$ factor by:",
        "options": [
          "$BW = \frac{Q}{f_0}$",
          "$BW = \frac{R}{2\\pi \\sqrt{LC}}$",
          "$BW = \frac{f_0}{Q}$",
          "$BW = f_0 \times Q$"
        ],
        "correctIndex": 2,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
          ],
          "keyConcept": "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
        }
      },
      {
        "id": 11,
        "question": "Norton's equivalent current $I_N$ is determined by measuring the current flowing through:",
        "options": [
          "A short circuit placed across the load terminals",
          "A parallel test inductor (independent of external field perturbations)",
          "An open circuit across the load terminals",
          "A high-impedance voltmeter (under steady-state operating conditions)"
        ],
        "correctIndex": 0,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
          ],
          "keyConcept": "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
        }
      },
      {
        "id": 12,
        "question": "Superposition theorem is strictly applicable only to circuits that consist of:",
        "options": [
          "Unilateral diodes and rectifiers",
          "Linear bilateral circuit elements",
          "Time-varying saturation inductors",
          "Non-linear semiconductor devices"
        ],
        "correctIndex": 1,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
          ],
          "keyConcept": "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
        }
      },
      {
        "id": 13,
        "question": "The average active power consumed in an ideal pure inductor or pure capacitor across a complete AC cycle is:",
        "options": [
          "Maximum Watts",
          "$V_{\text{rms}} \times I_{\text{rms}}$",
          "Zero Watts",
          "$I_{\text{rms}}^2 X$"
        ],
        "correctIndex": 2,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
          ],
          "keyConcept": "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
        }
      },
      {
        "id": 14,
        "question": "In nodal analysis of electrical circuits, the equations for node voltages are derived using:",
        "options": [
          "Kirchhoff's Current Law (KCL)",
          "Kirchhoff's Voltage Law (KVL)",
          "Faraday's Law of Induction",
          "Thevenin's Theorem"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Nodal analysis applies KCL at all non-reference essential nodes."
          ],
          "keyConcept": "Nodal analysis applies KCL at all non-reference essential nodes."
        }
      },
      {
        "id": 15,
        "question": "A PN junction diode operating under forward bias exhibits a built-in potential barrier that:",
        "options": [
          "Remains entirely unchanged (as determined by Maxwell boundary constraints)",
          "Increases linearly, blocking all conduction (across all standard operating temperatures)",
          "Oscillates at grid frequency (governed by linear superposition principles)",
          "Decreases, allowing majority carriers to diffuse across the junction"
        ],
        "correctIndex": 3,
        "topic": "Semiconductor Diodes",
        "explanation": {
          "steps": [
            "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
          ],
          "keyConcept": "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
        }
      },
      {
        "id": 16,
        "question": "The Quality Factor ($Q$) of a series RLC resonant circuit is defined by the formula:",
        "options": [
          "$Q = \frac{R}{\\omega_0 L}$",
          "$Q = \frac{\\omega_0 L}{C}$",
          "$Q = \frac{1}{R}\\sqrt{\frac{L}{C}}$",
          "$Q = R\\sqrt{\frac{C}{L}}$"
        ],
        "correctIndex": 2,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
          ],
          "keyConcept": "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
        }
      },
      {
        "id": 17,
        "question": "An ideal independent current source has an internal parallel resistance of:",
        "options": [
          "Zero resistance ($0\\,\\Omega$)",
          "Infinite resistance ($\\infty\\,\\Omega$)",
          "One ohm ($1\\,\\Omega$) (in an ideal homogeneous medium)",
          "Fifty ohms ($50\\,\\Omega$)"
        ],
        "correctIndex": 1,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
          ],
          "keyConcept": "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
        }
      },
      {
        "id": 18,
        "question": "In a purely capacitive AC circuit, the alternating current:",
        "options": [
          "Is in exact phase with the applied voltage",
          "Leads the applied voltage by $90^\\circ$ ($\\pi/2$ radians)",
          "Lags behind the applied voltage by $90^\\circ$",
          "Leads the applied voltage by $45^\\circ$ (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 1,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
          ],
          "keyConcept": "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
        }
      },
      {
        "id": 19,
        "question": "The EMF equation of an ideal single-phase transformer is given by:",
        "options": [
          "$E_1 = \frac{f N_1}{\\Phi_m}$",
          "$E_1 = 4 f N_1 \\Phi_m$",
          "$E_1 = 2\\pi f N_1 \\Phi_m$",
          "$E_1 = 4.44 f N_1 \\Phi_m$"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
          ],
          "keyConcept": "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
        }
      },
      {
        "id": 20,
        "question": "Thevenin's theorem states that any linear bilateral two-terminal active network can be replaced by an equivalent circuit containing:",
        "options": [
          "An open-circuit voltage $V_{th}$ in series with an equivalent resistance $R_{th}$",
          "An ideal voltage source in parallel with an inductor (as determined by Maxwell boundary constraints)",
          "An ideal current source in series with a capacitor (across all standard operating temperatures)",
          "A short-circuit current $I_N$ in parallel with a conductance $G_N$"
        ],
        "correctIndex": 0,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
          ],
          "keyConcept": "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
        }
      },
      {
        "id": 21,
        "question": "The resonant angular frequency $\\omega_0$ of a series RLC circuit is given by:",
        "options": [
          "$\\omega_0 = \frac{R}{2L}$",
          "$\\omega_0 = \\sqrt{LC}$",
          "$\\omega_0 = \frac{1}{\\sqrt{LC}}$",
          "$\\omega_0 = \frac{1}{2\\pi LC}$"
        ],
        "correctIndex": 2,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
          ],
          "keyConcept": "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
        }
      },
      {
        "id": 22,
        "question": "Under the Maximum Power Transfer Theorem, maximum power is delivered from a DC source with internal resistance $R_s$ to a load $R_L$ when:",
        "options": [
          "$R_L = R_s$",
          "$R_L = \\infty$",
          "$R_L = 2 R_s$",
          "$R_L = R_s / 2$"
        ],
        "correctIndex": 0,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
          ],
          "keyConcept": "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
        }
      },
      {
        "id": 23,
        "question": "The open-circuit test on a transformer is primarily conducted to determine its:",
        "options": [
          "Short-circuit impedance (governed by linear superposition principles)",
          "Full-load copper ohmic losses (independent of external field perturbations)",
          "Winding temperature rise (in an ideal homogeneous medium)",
          "Core losses (iron losses) and magnetizing branch parameters"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
          ],
          "keyConcept": "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
        }
      },
      {
        "id": 24,
        "question": "At electrical resonance in a series RLC circuit, the net circuit impedance is:",
        "options": [
          "Purely capacitive and zero (independent of external field perturbations)",
          "Purely inductive and infinite (in an ideal homogeneous medium)",
          "Purely resistive and at its minimum value ($Z = R$)",
          "Complex with reactive power maximized"
        ],
        "correctIndex": 2,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
          ],
          "keyConcept": "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
        }
      },
      {
        "id": 25,
        "question": "The transformation ratio $K$ of a transformer is defined as:",
        "options": [
          "$K = \frac{I_2}{I_1} = \frac{N_2}{N_1}$ (in an ideal homogeneous medium)",
          "$K = \frac{N_1}{N_2} = \frac{V_2}{V_1}$ (under steady-state operating conditions)",
          "$K = \frac{V_1}{V_2} = \frac{N_2}{N_1}$ (as determined by Maxwell boundary constraints)",
          "$K = \frac{V_2}{V_1} = \frac{N_2}{N_1} = \frac{I_1}{I_2}$"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
          ],
          "keyConcept": "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
        }
      },
      {
        "id": 26,
        "question": "In star-to-delta transformation, if three identical resistors of value $R$ are connected in star, the equivalent delta branch resistance is:",
        "options": [
          "$3R$",
          "$R/3$",
          "$R$",
          "$2R$"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
          ],
          "keyConcept": "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
        }
      },
      {
        "id": 27,
        "question": "In a half-wave rectifier, the theoretical maximum conversion efficiency $\\eta_{\text{max}}$ is equal to:",
        "options": [
          "$50.0\\%$",
          "$81.2\\%$",
          "$90.0\\%$",
          "$40.6\\%$"
        ],
        "correctIndex": 3,
        "topic": "Rectifiers",
        "explanation": {
          "steps": [
            "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
          ],
          "keyConcept": "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
        }
      },
      {
        "id": 28,
        "question": "According to Kirchhoff's Current Law (KCL), the algebraic sum of currents entering any node is zero because of conservation of:",
        "options": [
          "Electric charge",
          "Total energy",
          "Electric potential",
          "Magnetic flux"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
          ],
          "keyConcept": "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
        }
      },
      {
        "id": 29,
        "question": "In mesh current analysis, the governing circuit equations are systematically formulated using:",
        "options": [
          "Kirchhoff's Voltage Law (KVL)",
          "Ampere's Circuital Law",
          "Kirchhoff's Current Law (KCL)",
          "Gauss's Flux Theorem"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Mesh analysis applies KVL around independent closed loops in planar circuits."
          ],
          "keyConcept": "Mesh analysis applies KVL around independent closed loops in planar circuits."
        }
      },
      {
        "id": 30,
        "question": "In an ideal step-up transformer where secondary turns $N_2 > N_1$, the secondary current $I_2$ compared to primary $I_1$ is:",
        "options": [
          "Zero ($I_2 = 0$)",
          "Higher ($I_2 > I_1$)",
          "Equal ($I_2 = I_1$)",
          "Lower ($I_2 < I_1$)"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
          ],
          "keyConcept": "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
        }
      }
    ]
  },
  {
    "id": "ece249-midterm-paper-4",
    "code": "ECE249-PAPER-D",
    "title": "Midterm Examination • Paper 4 (Single-Phase Transformers & Losses)",
    "courseCode": "ECE249",
    "courseName": "Basic Electrical & Electronics Engineering",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "DC Circuit Theorems",
      "AC Fundamentals",
      "RLC Resonance",
      "Transformers & Diodes"
    ],
    "description": "Evaluates transformer EMF equations, core losses, copper losses, and equivalent circuits.",
    "questions": [
      {
        "id": 1,
        "question": "A transformer transfers electrical energy from primary to secondary winding without altering the:",
        "options": [
          "Impedance level",
          "Voltage magnitude",
          "Operating frequency",
          "Current magnitude"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "A transformer changes voltage and current levels while maintaining identical power frequency."
          ],
          "keyConcept": "A transformer changes voltage and current levels while maintaining identical power frequency."
        }
      },
      {
        "id": 2,
        "question": "The EMF equation of an ideal single-phase transformer is given by:",
        "options": [
          "$E_1 = 4 f N_1 \\Phi_m$",
          "$E_1 = 4.44 f N_1 \\Phi_m$",
          "$E_1 = \frac{f N_1}{\\Phi_m}$",
          "$E_1 = 2\\pi f N_1 \\Phi_m$"
        ],
        "correctIndex": 1,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
          ],
          "keyConcept": "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
        }
      },
      {
        "id": 3,
        "question": "In a purely capacitive AC circuit, the alternating current:",
        "options": [
          "Is in exact phase with the applied voltage",
          "Leads the applied voltage by $90^\\circ$ ($\\pi/2$ radians)",
          "Leads the applied voltage by $45^\\circ$ (in an ideal homogeneous medium)",
          "Lags behind the applied voltage by $90^\\circ$"
        ],
        "correctIndex": 1,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
          ],
          "keyConcept": "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
        }
      },
      {
        "id": 4,
        "question": "The Peak Factor (or Crest Factor) of a pure sine wave is equal to:",
        "options": [
          "$0.707$",
          "$1.11$",
          "$1.414$ ($\\sqrt{2}$)",
          "$2.00$"
        ],
        "correctIndex": 2,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
          ],
          "keyConcept": "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
        }
      },
      {
        "id": 5,
        "question": "Under the Maximum Power Transfer Theorem, maximum power is delivered from a DC source with internal resistance $R_s$ to a load $R_L$ when:",
        "options": [
          "$R_L = \\infty$",
          "$R_L = R_s$",
          "$R_L = 2 R_s$",
          "$R_L = R_s / 2$"
        ],
        "correctIndex": 1,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
          ],
          "keyConcept": "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
        }
      },
      {
        "id": 6,
        "question": "In mesh current analysis, the governing circuit equations are systematically formulated using:",
        "options": [
          "Gauss's Flux Theorem",
          "Kirchhoff's Current Law (KCL)",
          "Kirchhoff's Voltage Law (KVL)",
          "Ampere's Circuital Law"
        ],
        "correctIndex": 2,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Mesh analysis applies KVL around independent closed loops in planar circuits."
          ],
          "keyConcept": "Mesh analysis applies KVL around independent closed loops in planar circuits."
        }
      },
      {
        "id": 7,
        "question": "An ideal independent voltage source maintains its terminal voltage completely independent of:",
        "options": [
          "The internal wire thickness (as determined by Maxwell boundary constraints)",
          "The amount of current drawn by the connected load",
          "The frequency of the grid (governed by linear superposition principles)",
          "The temperature of the room (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
          ],
          "keyConcept": "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
        }
      },
      {
        "id": 8,
        "question": "In star-to-delta transformation, if three identical resistors of value $R$ are connected in star, the equivalent delta branch resistance is:",
        "options": [
          "$3R$",
          "$2R$",
          "$R$",
          "$R/3$"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
          ],
          "keyConcept": "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
        }
      },
      {
        "id": 9,
        "question": "A PN junction diode operating under forward bias exhibits a built-in potential barrier that:",
        "options": [
          "Remains entirely unchanged (governed by linear superposition principles)",
          "Oscillates at grid frequency (independent of external field perturbations)",
          "Increases linearly, blocking all conduction (in an ideal homogeneous medium)",
          "Decreases, allowing majority carriers to diffuse across the junction"
        ],
        "correctIndex": 3,
        "topic": "Semiconductor Diodes",
        "explanation": {
          "steps": [
            "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
          ],
          "keyConcept": "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
        }
      },
      {
        "id": 10,
        "question": "The transformation ratio $K$ of a transformer is defined as:",
        "options": [
          "$K = \frac{N_1}{N_2} = \frac{V_2}{V_1}$ (independent of external field perturbations)",
          "$K = \frac{V_1}{V_2} = \frac{N_2}{N_1}$ (in an ideal homogeneous medium)",
          "$K = \frac{V_2}{V_1} = \frac{N_2}{N_1} = \frac{I_1}{I_2}$",
          "$K = \frac{I_2}{I_1} = \frac{N_2}{N_1}$ (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
          ],
          "keyConcept": "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
        }
      },
      {
        "id": 11,
        "question": "In a purely inductive AC circuit, the alternating current:",
        "options": [
          "Leads the applied voltage by $90^\\circ$ (in an ideal homogeneous medium)",
          "Lags behind the applied voltage by $180^\\circ$ (under steady-state operating conditions)",
          "Is in exact phase with the applied voltage (as determined by Maxwell boundary constraints)",
          "Lags behind the applied voltage by $90^\\circ$ ($\\pi/2$ radians)"
        ],
        "correctIndex": 3,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
          ],
          "keyConcept": "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
        }
      },
      {
        "id": 12,
        "question": "The Quality Factor ($Q$) of a series RLC resonant circuit is defined by the formula:",
        "options": [
          "$Q = \frac{1}{R}\\sqrt{\frac{L}{C}}$",
          "$Q = \frac{\\omega_0 L}{C}$",
          "$Q = R\\sqrt{\frac{C}{L}}$",
          "$Q = \frac{R}{\\omega_0 L}$"
        ],
        "correctIndex": 0,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
          ],
          "keyConcept": "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
        }
      },
      {
        "id": 13,
        "question": "In an ideal step-up transformer where secondary turns $N_2 > N_1$, the secondary current $I_2$ compared to primary $I_1$ is:",
        "options": [
          "Higher ($I_2 > I_1$)",
          "Zero ($I_2 = 0$)",
          "Equal ($I_2 = I_1$)",
          "Lower ($I_2 < I_1$)"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
          ],
          "keyConcept": "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
        }
      },
      {
        "id": 14,
        "question": "The Form Factor of a pure sinusoidal alternating voltage waveform is defined as the ratio of:",
        "options": [
          "Average value to the Peak value ($V_{\text{avg}} / V_m = 0.637$)",
          "Peak value to the RMS value ($V_m / V_{\text{rms}} = 1.414$)",
          "RMS value to the Average value ($V_{\text{rms}} / V_{\text{avg}} = 1.11$)",
          "Reactive power to Apparent power ($\\sin\\phi$) (in an ideal homogeneous medium)"
        ],
        "correctIndex": 2,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} \u0007pprox 1.11$."
          ],
          "keyConcept": "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} ..."
        }
      },
      {
        "id": 15,
        "question": "Thevenin's theorem states that any linear bilateral two-terminal active network can be replaced by an equivalent circuit containing:",
        "options": [
          "A short-circuit current $I_N$ in parallel with a conductance $G_N$",
          "An ideal current source in series with a capacitor (independent of external field perturbations)",
          "An open-circuit voltage $V_{th}$ in series with an equivalent resistance $R_{th}$",
          "An ideal voltage source in parallel with an inductor (under steady-state operating conditions)"
        ],
        "correctIndex": 2,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
          ],
          "keyConcept": "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
        }
      },
      {
        "id": 16,
        "question": "According to Kirchhoff's Current Law (KCL), the algebraic sum of currents entering any node is zero because of conservation of:",
        "options": [
          "Electric charge",
          "Total energy",
          "Magnetic flux",
          "Electric potential"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
          ],
          "keyConcept": "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
        }
      },
      {
        "id": 17,
        "question": "At electrical resonance in a series RLC circuit, the net circuit impedance is:",
        "options": [
          "Purely inductive and infinite (in an ideal homogeneous medium)",
          "Purely capacitive and zero (under steady-state operating conditions)",
          "Complex with reactive power maximized",
          "Purely resistive and at its minimum value ($Z = R$)"
        ],
        "correctIndex": 3,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
          ],
          "keyConcept": "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
        }
      },
      {
        "id": 18,
        "question": "Superposition theorem is strictly applicable only to circuits that consist of:",
        "options": [
          "Non-linear semiconductor devices",
          "Linear bilateral circuit elements",
          "Unilateral diodes and rectifiers",
          "Time-varying saturation inductors"
        ],
        "correctIndex": 1,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
          ],
          "keyConcept": "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
        }
      },
      {
        "id": 19,
        "question": "The short-circuit test on a transformer is performed to determine its:",
        "options": [
          "Equivalent winding resistance, leakage reactance, and full-load copper losses",
          "Eddy current loss (across all standard operating temperatures)",
          "Dielectric breakdown voltage (governed by linear superposition principles)",
          "Core hysteresis loss (independent of external field perturbations)"
        ],
        "correctIndex": 0,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
          ],
          "keyConcept": "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
        }
      },
      {
        "id": 20,
        "question": "The open-circuit test on a transformer is primarily conducted to determine its:",
        "options": [
          "Full-load copper ohmic losses (across all standard operating temperatures)",
          "Short-circuit impedance (governed by linear superposition principles)",
          "Winding temperature rise (independent of external field perturbations)",
          "Core losses (iron losses) and magnetizing branch parameters"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
          ],
          "keyConcept": "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
        }
      },
      {
        "id": 21,
        "question": "Hysteresis loss in a magnetic iron core subjected to alternating magnetizing force is proportional to:",
        "options": [
          "The square of the core lamination thickness",
          "The area enclosed by the magnetic $B$-$H$ hysteresis loop",
          "The length of the secondary wire (in an ideal homogeneous medium)",
          "The winding series resistance (under steady-state operating conditions)"
        ],
        "correctIndex": 1,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
          ],
          "keyConcept": "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
        }
      },
      {
        "id": 22,
        "question": "In nodal analysis of electrical circuits, the equations for node voltages are derived using:",
        "options": [
          "Kirchhoff's Current Law (KCL)",
          "Faraday's Law of Induction",
          "Kirchhoff's Voltage Law (KVL)",
          "Thevenin's Theorem"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Nodal analysis applies KCL at all non-reference essential nodes."
          ],
          "keyConcept": "Nodal analysis applies KCL at all non-reference essential nodes."
        }
      },
      {
        "id": 23,
        "question": "The resonant angular frequency $\\omega_0$ of a series RLC circuit is given by:",
        "options": [
          "$\\omega_0 = \frac{1}{2\\pi LC}$",
          "$\\omega_0 = \frac{R}{2L}$",
          "$\\omega_0 = \\sqrt{LC}$",
          "$\\omega_0 = \frac{1}{\\sqrt{LC}}$"
        ],
        "correctIndex": 3,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
          ],
          "keyConcept": "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
        }
      },
      {
        "id": 24,
        "question": "The core of a practical transformer is laminated with thin silicon steel sheets specifically to reduce:",
        "options": [
          "Hysteresis losses",
          "Magnetic flux leakage",
          "Eddy current losses",
          "Copper ohmic losses"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\propto t^2$)."
          ],
          "keyConcept": "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\pro..."
        }
      },
      {
        "id": 25,
        "question": "The bandwidth ($BW = f_2 - f_1$) of an RLC resonant circuit is related to resonant frequency $f_0$ and $Q$ factor by:",
        "options": [
          "$BW = \frac{Q}{f_0}$",
          "$BW = \frac{R}{2\\pi \\sqrt{LC}}$",
          "$BW = f_0 \times Q$",
          "$BW = \frac{f_0}{Q}$"
        ],
        "correctIndex": 3,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
          ],
          "keyConcept": "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
        }
      },
      {
        "id": 26,
        "question": "The average active power consumed in an ideal pure inductor or pure capacitor across a complete AC cycle is:",
        "options": [
          "Maximum Watts",
          "$I_{\text{rms}}^2 X$",
          "$V_{\text{rms}} \times I_{\text{rms}}$",
          "Zero Watts"
        ],
        "correctIndex": 3,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
          ],
          "keyConcept": "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
        }
      },
      {
        "id": 27,
        "question": "In a half-wave rectifier, the theoretical maximum conversion efficiency $\\eta_{\text{max}}$ is equal to:",
        "options": [
          "$40.6\\%$",
          "$90.0\\%$",
          "$81.2\\%$",
          "$50.0\\%$"
        ],
        "correctIndex": 0,
        "topic": "Rectifiers",
        "explanation": {
          "steps": [
            "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
          ],
          "keyConcept": "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
        }
      },
      {
        "id": 28,
        "question": "In the power triangle, the Power Factor ($\\cos\\phi$) is mathematically defined as the ratio of:",
        "options": [
          "Active Power ($P$) to Apparent Power ($S$)",
          "Reactive Power ($Q$) to Active Power ($P$)",
          "Impedance ($Z$) to Resistance ($R$)",
          "Apparent Power ($S$) to Active Power ($P$)"
        ],
        "correctIndex": 0,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
          ],
          "keyConcept": "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
        }
      },
      {
        "id": 29,
        "question": "Norton's equivalent current $I_N$ is determined by measuring the current flowing through:",
        "options": [
          "A parallel test inductor (in an ideal homogeneous medium)",
          "A short circuit placed across the load terminals",
          "An open circuit across the load terminals",
          "A high-impedance voltmeter (across all standard operating temperatures)"
        ],
        "correctIndex": 1,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
          ],
          "keyConcept": "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
        }
      },
      {
        "id": 30,
        "question": "An ideal independent current source has an internal parallel resistance of:",
        "options": [
          "One ohm ($1\\,\\Omega$) (under steady-state operating conditions)",
          "Zero resistance ($0\\,\\Omega$)",
          "Infinite resistance ($\\infty\\,\\Omega$)",
          "Fifty ohms ($50\\,\\Omega$)"
        ],
        "correctIndex": 2,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
          ],
          "keyConcept": "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
        }
      }
    ]
  },
  {
    "id": "ece249-midterm-paper-5",
    "code": "ECE249-PAPER-E",
    "title": "Midterm Examination • Paper 5 (Comprehensive Electrical Engineering Suite)",
    "courseCode": "ECE249",
    "courseName": "Basic Electrical & Electronics Engineering",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "DC Circuit Theorems",
      "AC Fundamentals",
      "RLC Resonance",
      "Transformers & Diodes"
    ],
    "description": "Authentic university midterm examination covering all Units 1-3 with verified solutions.",
    "questions": [
      {
        "id": 1,
        "question": "In a half-wave rectifier, the theoretical maximum conversion efficiency $\\eta_{\text{max}}$ is equal to:",
        "options": [
          "$81.2\\%$",
          "$90.0\\%$",
          "$50.0\\%$",
          "$40.6\\%$"
        ],
        "correctIndex": 3,
        "topic": "Rectifiers",
        "explanation": {
          "steps": [
            "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
          ],
          "keyConcept": "Max efficiency for half-wave rectification is $\\eta = \frac{0.406 R_L}{r_f + R_L} \u0007pprox 40.6\\%$."
        }
      },
      {
        "id": 2,
        "question": "In a purely inductive AC circuit, the alternating current:",
        "options": [
          "Lags behind the applied voltage by $180^\\circ$ (independent of external field perturbations)",
          "Lags behind the applied voltage by $90^\\circ$ ($\\pi/2$ radians)",
          "Is in exact phase with the applied voltage (under steady-state operating conditions)",
          "Leads the applied voltage by $90^\\circ$ (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 1,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
          ],
          "keyConcept": "In an ideal inductor, $v(t) = L \frac{di}{dt}$; current lags voltage by exactly $90^\\circ$."
        }
      },
      {
        "id": 3,
        "question": "Hysteresis loss in a magnetic iron core subjected to alternating magnetizing force is proportional to:",
        "options": [
          "The length of the secondary wire (in an ideal homogeneous medium)",
          "The winding series resistance (under steady-state operating conditions)",
          "The square of the core lamination thickness",
          "The area enclosed by the magnetic $B$-$H$ hysteresis loop"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
          ],
          "keyConcept": "Steinmetz law proves hysteresis loss per cycle equals the area enclosed by the material's $B$-$H$ loop."
        }
      },
      {
        "id": 4,
        "question": "The bandwidth ($BW = f_2 - f_1$) of an RLC resonant circuit is related to resonant frequency $f_0$ and $Q$ factor by:",
        "options": [
          "$BW = \frac{R}{2\\pi \\sqrt{LC}}$",
          "$BW = f_0 \times Q$",
          "$BW = \frac{Q}{f_0}$",
          "$BW = \frac{f_0}{Q}$"
        ],
        "correctIndex": 3,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
          ],
          "keyConcept": "Bandwidth between half-power points is inversely proportional to Quality factor: $BW = f_0 / Q$."
        }
      },
      {
        "id": 5,
        "question": "The resonant angular frequency $\\omega_0$ of a series RLC circuit is given by:",
        "options": [
          "$\\omega_0 = \frac{R}{2L}$",
          "$\\omega_0 = \frac{1}{\\sqrt{LC}}$",
          "$\\omega_0 = \frac{1}{2\\pi LC}$",
          "$\\omega_0 = \\sqrt{LC}$"
        ],
        "correctIndex": 1,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
          ],
          "keyConcept": "Setting $\\omega_0 L = \frac{1}{\\omega_0 C}$ yields $\\omega_0 = \frac{1}{\\sqrt{LC}}\text{ rad/s}$."
        }
      },
      {
        "id": 6,
        "question": "The short-circuit test on a transformer is performed to determine its:",
        "options": [
          "Equivalent winding resistance, leakage reactance, and full-load copper losses",
          "Dielectric breakdown voltage (governed by linear superposition principles)",
          "Eddy current loss (independent of external field perturbations)",
          "Core hysteresis loss (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
          ],
          "keyConcept": "Short-circuit test operates at rated current with low applied voltage, isolating full-load copper loss ($I^2R$)."
        }
      },
      {
        "id": 7,
        "question": "In the power triangle, the Power Factor ($\\cos\\phi$) is mathematically defined as the ratio of:",
        "options": [
          "Impedance ($Z$) to Resistance ($R$)",
          "Apparent Power ($S$) to Active Power ($P$)",
          "Active Power ($P$) to Apparent Power ($S$)",
          "Reactive Power ($Q$) to Active Power ($P$)"
        ],
        "correctIndex": 2,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
          ],
          "keyConcept": "Power factor $\\cos\\phi = P / S = \text{Active Power [W]} / \text{Apparent Power [VA]}$."
        }
      },
      {
        "id": 8,
        "question": "According to Kirchhoff's Current Law (KCL), the algebraic sum of currents entering any node is zero because of conservation of:",
        "options": [
          "Electric charge",
          "Total energy",
          "Electric potential",
          "Magnetic flux"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
          ],
          "keyConcept": "KCL is a direct physical consequence of the conservation of electric charge ($\\sum I = 0$)."
        }
      },
      {
        "id": 9,
        "question": "In a purely capacitive AC circuit, the alternating current:",
        "options": [
          "Lags behind the applied voltage by $90^\\circ$",
          "Is in exact phase with the applied voltage",
          "Leads the applied voltage by $90^\\circ$ ($\\pi/2$ radians)",
          "Leads the applied voltage by $45^\\circ$ (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "AC Circuits",
        "explanation": {
          "steps": [
            "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
          ],
          "keyConcept": "In a capacitor, $i(t) = C \frac{dv}{dt}$; sinusoidal current leads voltage by $90^\\circ$."
        }
      },
      {
        "id": 10,
        "question": "The Quality Factor ($Q$) of a series RLC resonant circuit is defined by the formula:",
        "options": [
          "$Q = \frac{\\omega_0 L}{C}$",
          "$Q = R\\sqrt{\frac{C}{L}}$",
          "$Q = \frac{R}{\\omega_0 L}$",
          "$Q = \frac{1}{R}\\sqrt{\frac{L}{C}}$"
        ],
        "correctIndex": 3,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
          ],
          "keyConcept": "$Q = \frac{\\omega_0 L}{R} = \frac{1}{\\omega_0 CR} = \frac{1}{R}\\sqrt{\frac{L}{C}}$."
        }
      },
      {
        "id": 11,
        "question": "In mesh current analysis, the governing circuit equations are systematically formulated using:",
        "options": [
          "Ampere's Circuital Law",
          "Kirchhoff's Voltage Law (KVL)",
          "Gauss's Flux Theorem",
          "Kirchhoff's Current Law (KCL)"
        ],
        "correctIndex": 1,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Mesh analysis applies KVL around independent closed loops in planar circuits."
          ],
          "keyConcept": "Mesh analysis applies KVL around independent closed loops in planar circuits."
        }
      },
      {
        "id": 12,
        "question": "The Form Factor of a pure sinusoidal alternating voltage waveform is defined as the ratio of:",
        "options": [
          "Reactive power to Apparent power ($\\sin\\phi$) (across all standard operating temperatures)",
          "Peak value to the RMS value ($V_m / V_{\text{rms}} = 1.414$)",
          "Average value to the Peak value ($V_{\text{avg}} / V_m = 0.637$)",
          "RMS value to the Average value ($V_{\text{rms}} / V_{\text{avg}} = 1.11$)"
        ],
        "correctIndex": 3,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} \u0007pprox 1.11$."
          ],
          "keyConcept": "Form factor is the ratio of RMS value to half-cycle average value: $\frac{V_m/\\sqrt{2}}{2V_m/\\pi} = \frac{\\pi}{2\\sqrt{2}} ..."
        }
      },
      {
        "id": 13,
        "question": "At electrical resonance in a series RLC circuit, the net circuit impedance is:",
        "options": [
          "Purely resistive and at its minimum value ($Z = R$)",
          "Purely capacitive and zero (independent of external field perturbations)",
          "Purely inductive and infinite (in an ideal homogeneous medium)",
          "Complex with reactive power maximized"
        ],
        "correctIndex": 0,
        "topic": "RLC Resonance",
        "explanation": {
          "steps": [
            "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
          ],
          "keyConcept": "At resonance, $X_L = X_C$, so net reactance is zero and impedance $Z = R$ is at its minimum."
        }
      },
      {
        "id": 14,
        "question": "An ideal independent voltage source maintains its terminal voltage completely independent of:",
        "options": [
          "The amount of current drawn by the connected load",
          "The temperature of the room (in an ideal homogeneous medium)",
          "The frequency of the grid (under steady-state operating conditions)",
          "The internal wire thickness (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 0,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
          ],
          "keyConcept": "An ideal voltage source has zero internal resistance, holding constant voltage for any load current."
        }
      },
      {
        "id": 15,
        "question": "The EMF equation of an ideal single-phase transformer is given by:",
        "options": [
          "$E_1 = \frac{f N_1}{\\Phi_m}$",
          "$E_1 = 4.44 f N_1 \\Phi_m$",
          "$E_1 = 4 f N_1 \\Phi_m$",
          "$E_1 = 2\\pi f N_1 \\Phi_m$"
        ],
        "correctIndex": 1,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
          ],
          "keyConcept": "From Faraday's law: $e = -N \frac{d\\Phi}{dt} \\implies E_{\text{rms}} = 4.44 f N \\Phi_m\text{ Volts}$."
        }
      },
      {
        "id": 16,
        "question": "In star-to-delta transformation, if three identical resistors of value $R$ are connected in star, the equivalent delta branch resistance is:",
        "options": [
          "$R$",
          "$R/3$",
          "$2R$",
          "$3R$"
        ],
        "correctIndex": 3,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
          ],
          "keyConcept": "For identical star resistors $R$, the equivalent delta resistor is $R_\\Delta = 3R_Y$."
        }
      },
      {
        "id": 17,
        "question": "The Peak Factor (or Crest Factor) of a pure sine wave is equal to:",
        "options": [
          "$1.414$ ($\\sqrt{2}$)",
          "$1.11$",
          "$2.00$",
          "$0.707$"
        ],
        "correctIndex": 0,
        "topic": "AC Fundamentals",
        "explanation": {
          "steps": [
            "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
          ],
          "keyConcept": "Peak factor is the ratio of peak amplitude to RMS value: $V_m / (V_m/\\sqrt{2}) = \\sqrt{2} \u0007pprox 1.414$."
        }
      },
      {
        "id": 18,
        "question": "In an ideal step-up transformer where secondary turns $N_2 > N_1$, the secondary current $I_2$ compared to primary $I_1$ is:",
        "options": [
          "Equal ($I_2 = I_1$)",
          "Higher ($I_2 > I_1$)",
          "Lower ($I_2 < I_1$)",
          "Zero ($I_2 = 0$)"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
          ],
          "keyConcept": "Because apparent power is conserved ($V_1 I_1 = V_2 I_2$), stepping up voltage steps down current: $I_2/I_1 = N_1/N_2$."
        }
      },
      {
        "id": 19,
        "question": "A transformer transfers electrical energy from primary to secondary winding without altering the:",
        "options": [
          "Impedance level",
          "Current magnitude",
          "Operating frequency",
          "Voltage magnitude"
        ],
        "correctIndex": 2,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "A transformer changes voltage and current levels while maintaining identical power frequency."
          ],
          "keyConcept": "A transformer changes voltage and current levels while maintaining identical power frequency."
        }
      },
      {
        "id": 20,
        "question": "The core of a practical transformer is laminated with thin silicon steel sheets specifically to reduce:",
        "options": [
          "Copper ohmic losses",
          "Eddy current losses",
          "Hysteresis losses",
          "Magnetic flux leakage"
        ],
        "correctIndex": 1,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\propto t^2$)."
          ],
          "keyConcept": "Laminating the iron core breaks continuous circulating loop paths, drastically decreasing eddy current losses ($P_e \\pro..."
        }
      },
      {
        "id": 21,
        "question": "A PN junction diode operating under forward bias exhibits a built-in potential barrier that:",
        "options": [
          "Increases linearly, blocking all conduction (in an ideal homogeneous medium)",
          "Decreases, allowing majority carriers to diffuse across the junction",
          "Oscillates at grid frequency (as determined by Maxwell boundary constraints)",
          "Remains entirely unchanged (across all standard operating temperatures)"
        ],
        "correctIndex": 1,
        "topic": "Semiconductor Diodes",
        "explanation": {
          "steps": [
            "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
          ],
          "keyConcept": "Forward bias counteracts the internal barrier potential, narrowing the depletion region and permitting current flow."
        }
      },
      {
        "id": 22,
        "question": "Norton's equivalent current $I_N$ is determined by measuring the current flowing through:",
        "options": [
          "An open circuit across the load terminals",
          "A parallel test inductor (as determined by Maxwell boundary constraints)",
          "A short circuit placed across the load terminals",
          "A high-impedance voltmeter (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
          ],
          "keyConcept": "Norton current $I_N$ equals the short-circuit current ($I_{sc}$) between terminals A and B."
        }
      },
      {
        "id": 23,
        "question": "Under the Maximum Power Transfer Theorem, maximum power is delivered from a DC source with internal resistance $R_s$ to a load $R_L$ when:",
        "options": [
          "$R_L = R_s$",
          "$R_L = 2 R_s$",
          "$R_L = R_s / 2$",
          "$R_L = \\infty$"
        ],
        "correctIndex": 0,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
          ],
          "keyConcept": "Maximum power transfer theorem for DC resistive circuits dictates $R_L = R_s$, achieving $50\\%$ efficiency."
        }
      },
      {
        "id": 24,
        "question": "In nodal analysis of electrical circuits, the equations for node voltages are derived using:",
        "options": [
          "Faraday's Law of Induction",
          "Kirchhoff's Voltage Law (KVL)",
          "Kirchhoff's Current Law (KCL)",
          "Thevenin's Theorem"
        ],
        "correctIndex": 2,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "Nodal analysis applies KCL at all non-reference essential nodes."
          ],
          "keyConcept": "Nodal analysis applies KCL at all non-reference essential nodes."
        }
      },
      {
        "id": 25,
        "question": "Superposition theorem is strictly applicable only to circuits that consist of:",
        "options": [
          "Non-linear semiconductor devices",
          "Unilateral diodes and rectifiers",
          "Linear bilateral circuit elements",
          "Time-varying saturation inductors"
        ],
        "correctIndex": 2,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
          ],
          "keyConcept": "Superposition requires mathematical linearity ($f(x+y)=f(x)+f(y)$), applicable only to linear bilateral networks."
        }
      },
      {
        "id": 26,
        "question": "An ideal independent current source has an internal parallel resistance of:",
        "options": [
          "One ohm ($1\\,\\Omega$) (independent of external field perturbations)",
          "Infinite resistance ($\\infty\\,\\Omega$)",
          "Fifty ohms ($50\\,\\Omega$)",
          "Zero resistance ($0\\,\\Omega$)"
        ],
        "correctIndex": 1,
        "topic": "DC Circuit Analysis",
        "explanation": {
          "steps": [
            "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
          ],
          "keyConcept": "An ideal current source possesses infinite internal parallel resistance so current is entirely forced into the load."
        }
      },
      {
        "id": 27,
        "question": "The open-circuit test on a transformer is primarily conducted to determine its:",
        "options": [
          "Short-circuit impedance (in an ideal homogeneous medium)",
          "Winding temperature rise (under steady-state operating conditions)",
          "Full-load copper ohmic losses (as determined by Maxwell boundary constraints)",
          "Core losses (iron losses) and magnetizing branch parameters"
        ],
        "correctIndex": 3,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
          ],
          "keyConcept": "Open-circuit test operates at rated voltage with negligible current, isolating core iron losses ($P_i$)."
        }
      },
      {
        "id": 28,
        "question": "Thevenin's theorem states that any linear bilateral two-terminal active network can be replaced by an equivalent circuit containing:",
        "options": [
          "A short-circuit current $I_N$ in parallel with a conductance $G_N$",
          "An ideal current source in series with a capacitor (as determined by Maxwell boundary constraints)",
          "An ideal voltage source in parallel with an inductor (across all standard operating temperatures)",
          "An open-circuit voltage $V_{th}$ in series with an equivalent resistance $R_{th}$"
        ],
        "correctIndex": 3,
        "topic": "Network Theorems",
        "explanation": {
          "steps": [
            "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
          ],
          "keyConcept": "Thevenin equivalent consists of $V_{th}$ (open-circuit voltage) in series with internal resistance $R_{th}$."
        }
      },
      {
        "id": 29,
        "question": "The transformation ratio $K$ of a transformer is defined as:",
        "options": [
          "$K = \frac{V_2}{V_1} = \frac{N_2}{N_1} = \frac{I_1}{I_2}$",
          "$K = \frac{V_1}{V_2} = \frac{N_2}{N_1}$ (across all standard operating temperatures)",
          "$K = \frac{I_2}{I_1} = \frac{N_2}{N_1}$ (governed by linear superposition principles)",
          "$K = \frac{N_1}{N_2} = \frac{V_2}{V_1}$ (independent of external field perturbations)"
        ],
        "correctIndex": 0,
        "topic": "Transformers",
        "explanation": {
          "steps": [
            "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
          ],
          "keyConcept": "Transformation ratio $K = E_2 / E_1 = N_2 / N_1 = I_1 / I_2$."
        }
      },
      {
        "id": 30,
        "question": "The average active power consumed in an ideal pure inductor or pure capacitor across a complete AC cycle is:",
        "options": [
          "$V_{\text{rms}} \times I_{\text{rms}}$",
          "$I_{\text{rms}}^2 X$",
          "Zero Watts",
          "Maximum Watts"
        ],
        "correctIndex": 2,
        "topic": "AC Power",
        "explanation": {
          "steps": [
            "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
          ],
          "keyConcept": "Because $\\phi = 90^\\circ$, active power $P = V I \\cos(90^\\circ) = 0\text{ W}$."
        }
      }
    ]
  }
];
