/**
 * Official PHY110: Engineering Physics Midterm Mock Examination Suite
 * Contains 5 Full-Length 30-Question Tests (150 Questions Total)
 * Strictly covers Units 1-3: Vector Calculus, Lasers, Fiber Optics
 * Balanced keys [7,7,8,8] and equalized distractor lengths
 */

export const PHY110_MOCK_TESTS = [
  {
    "id": "phy110-midterm-paper-1",
    "code": "PHY110-PAPER-A",
    "title": "Midterm Examination • Paper 1 (Official University PYQ)",
    "courseCode": "PHY110",
    "courseName": "Engineering Physics",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Vector Calculus",
      "Maxwell Equations",
      "Lasers",
      "Fiber Optics"
    ],
    "description": "Authentic university midterm examination paper testing scalar/vector fields, divergence & Stokes theorems, laser pumping, population inversion, and optical fiber parameters.",
    "questions": [
      {
        "id": 1,
        "question": "The temperature at any point within or on earth's surface at a certain time defines a:",
        "options": [
          "Both scalar and vector field",
          "Scalar field",
          "Vector field",
          "None of these"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "Temperature has magnitude only and does not possess directional dependence.",
            "A physical quantity completely specified by a single real number at every point in space constitutes a scalar field T(x, y, z)."
          ],
          "keyConcept": "Temperature, electric potential, and density are classic examples of scalar fields."
        }
      },
      {
        "id": 2,
        "question": "If there exists a vector V(x, y, z) at each point (x, y, z) of a region R in space, then the field V defined in region R is called a:",
        "options": [
          "Both scalar and vector field",
          "None of these",
          "Scalar field",
          "Vector field"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "When every point in a region of space is associated with both a magnitude and a direction, the field is a vector field.",
            "Examples include gravitational velocity fields, electric field E, and magnetic flux density B."
          ],
          "keyConcept": "A vector field assigns a vector V = V_x i + V_y j + V_z k to each spatial point."
        }
      },
      {
        "id": 3,
        "question": "A scalar field is defined by φ(x, y, z) = 4x³ - yz² + 7. What is the value of the field at the point (0, 0, 0)?",
        "options": [
          "7",
          "0",
          "10",
          "4"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "Substitute x = 0, y = 0, z = 0 directly into the scalar function:",
            "φ(0, 0, 0) = 4(0)³ - (0)(0)² + 7 = 0 - 0 + 7 = 7."
          ],
          "keyConcept": "Evaluating a scalar field requires direct substitution of coordinates."
        }
      },
      {
        "id": 4,
        "question": "If we define del operator ∇ = i(∂/∂x) + j(∂/∂y) + k(∂/∂z), then the Operator ∇ is a:",
        "options": [
          "Both scalar and vector operator",
          "None of the above",
          "Vector differential operator",
          "Scalar operator"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "The del operator ∇ contains unit vector components (i, j, k) and partial differential operators.",
            "Operating on a scalar produces a vector (gradient: ∇φ), while operating via dot product produces a scalar (divergence: ∇·A)."
          ],
          "keyConcept": "∇ is formally known as the Hamilton vector differential operator (nabla)."
        }
      },
      {
        "id": 5,
        "question": "A point in space having positive divergence (∇ · V > 0) is called a:",
        "options": [
          "None of these",
          "Sink",
          "Drain",
          "Source"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "Divergence represents net outward flux of a vector field per unit volume.",
            "If ∇·V > 0, field lines diverge away from the point, signifying a Source.",
            "If ∇·V < 0, field lines converge toward the point, signifying a Sink."
          ],
          "keyConcept": "Positive divergence = Source; Negative divergence = Sink; Zero divergence = Solenoidal."
        }
      },
      {
        "id": 6,
        "question": "If the divergence of a vector field F vanishes everywhere (i.e., ∇ · F = 0), then F can be expressed as the curl of a vector potential A (F = ∇ × A). The vector field F in this case is called:",
        "options": [
          "Irrotational",
          "Solenoidal",
          "Both (a) and (c)",
          "Divergence-less"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "When ∇ · F = 0, the field has zero net divergence everywhere (divergence-less).",
            "By definition, any field with zero divergence is known as a Solenoidal field.",
            "Since div(curl A) = 0 identically, F can always be written as F = ∇ × A."
          ],
          "keyConcept": "∇·F = 0 means field F is both solenoidal and divergence-less."
        }
      },
      {
        "id": 7,
        "question": "If a vector field A is curl-less, i.e., ∇ × A = 0, the field is called:",
        "options": [
          "Both (a) and (c)",
          "Solenoidal",
          "Irrotational",
          "Divergence-less"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "A vector field with vanishing curl (∇ × A = 0) has zero circulation around any closed path.",
            "Such fields are called Irrotational (or Conservative).",
            "Every irrotational field can be written as the gradient of a scalar potential: A = ∇φ."
          ],
          "keyConcept": "∇ × A = 0 denotes an irrotational or conservative vector field."
        }
      },
      {
        "id": 8,
        "question": "If V is the volume bounded by a closed surface S and A is a vector function of position with continuous derivatives, then ∭_V (∇ · A) dV = ∬_S A · dS. This theorem is called:",
        "options": [
          "Curl theorem",
          "Both (a) and (c)",
          "Divergence theorem",
          "Gauss theorem"
        ],
        "correctIndex": 1,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "The theorem equates the volume integral of the divergence of a vector field over V to the surface integral of the vector field over the enclosing boundary S.",
            "It is universally known as the Gauss Divergence Theorem."
          ],
          "keyConcept": "Gauss Divergence Theorem converts a volume integral into a closed surface integral."
        }
      },
      {
        "id": 9,
        "question": "If S is an open two-sided surface bounded by a closed non-intersecting curve C and A is a continuous vector function, then ∬_S (∇ × A) · dS = ∮_C A · dr. This theorem is known as:",
        "options": [
          "None of the above",
          "Both (a) and (b)",
          "Stokes' theorem",
          "Fundamental theorem of curl"
        ],
        "correctIndex": 1,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "Stokes' theorem relates the surface integral of the curl of a vector field over an open surface S to the line integral of the vector field around boundary curve C.",
            "It is also known as the fundamental theorem for curl in vector calculus."
          ],
          "keyConcept": "Stokes' theorem connects the surface integral of curl with line integral of circulation."
        }
      },
      {
        "id": 10,
        "question": "If V is the electric potential, ρ is the volume charge density, and ε is the permittivity of the medium, which of the following describes the correct form of Poisson's equation?",
        "options": [
          "∇²V = -ρ/ε",
          "∇²V = 0",
          "∇V = 0",
          "∇V = -ρ/ε"
        ],
        "correctIndex": 0,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "From Gauss's Law: ∇ · E = ρ/ε.",
            "Since E = -∇V in electrostatics, substitution yields: ∇ · (-∇V) = ρ/ε.",
            "Therefore, ∇²V = -ρ/ε (Poisson's Equation). When ρ = 0, it reduces to Laplace's Equation ∇²V = 0."
          ],
          "keyConcept": "Poisson's Equation: ∇²V = -ρ/ε."
        }
      },
      {
        "id": 11,
        "question": "LASER stands for:",
        "options": [
          "Light Amplification by Stimulated Emission of Radiation",
          "Light Amplification by Spontaneous Emission of Radiation",
          "Light Amplification by Stimulated Emission of Reaction",
          "Light Amplification by Spontaneous Emission of Reaction"
        ],
        "correctIndex": 0,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "L = Light",
            "A = Amplification by",
            "S = Stimulated",
            "E = Emission of",
            "R = Radiation"
          ],
          "keyConcept": "LASER acronym: Light Amplification by Stimulated Emission of Radiation."
        }
      },
      {
        "id": 12,
        "question": "Stimulated emission of two atoms produces radiations that:",
        "options": [
          "Have random phase and direction",
          "Have same phase and random direction",
          "Have random phase and same direction",
          "Have same phase and direction"
        ],
        "correctIndex": 3,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "In stimulated emission, an incident photon stimulates an excited atom to emit a identical second photon.",
            "The emitted photon possesses exactly identical frequency, phase, polarization, and direction of propagation as the incident photon."
          ],
          "keyConcept": "Stimulated emission produces completely coherent photons (same phase and direction)."
        }
      },
      {
        "id": 13,
        "question": "Spatial coherence in a laser beam refers to coherence across the:",
        "options": [
          "Both (a) and (b)",
          "Longitudinal direction",
          "None of these",
          "Transverse direction"
        ],
        "correctIndex": 3,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Temporal coherence measures the correlation of wave phase along the propagation direction (longitudinal).",
            "Spatial coherence describes the constant phase relationship across different points perpendicular to the direction of propagation (transverse cross-section)."
          ],
          "keyConcept": "Spatial coherence is transverse; Temporal coherence is longitudinal."
        }
      },
      {
        "id": 14,
        "question": "Which of the following is an extraordinary, unique property of laser light compared to ordinary light?",
        "options": [
          "Wavelength",
          "High Coherence",
          "Power",
          "Speed"
        ],
        "correctIndex": 1,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "All electromagnetic waves travel at the speed of light c in vacuum.",
            "Ordinary incandescent or fluorescent sources emit incoherent light with random phases.",
            "Lasers possess exceptionally high spatial and temporal coherence, allowing extreme collimation and interference."
          ],
          "keyConcept": "Coherence is the defining signature property of laser light."
        }
      },
      {
        "id": 15,
        "question": "In which of the following LASER systems is Optical Pumping utilized as the primary excitation mechanism?",
        "options": [
          "Helium-Neon laser",
          "Semiconductor laser",
          "Carbon Dioxide laser",
          "Ruby and Nd:YAG laser"
        ],
        "correctIndex": 3,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Optical pumping uses intense light from a flash lamp (e.g. Xenon lamp) or laser diode.",
            "Solid-state lasers such as Ruby laser and Nd:YAG laser rely on optical pumping.",
            "In contrast, He-Ne lasers use electric discharge, and semiconductor diode lasers use electrical injection current."
          ],
          "keyConcept": "Nd:YAG and Ruby lasers use optical pumping."
        }
      },
      {
        "id": 16,
        "question": "The Nd:YAG laser operates as a:",
        "options": [
          "3-Level Laser",
          "2-Level Laser",
          "None of these",
          "4-Level Laser"
        ],
        "correctIndex": 3,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Nd:YAG operates between four energy levels of Nd³⁺ ions:",
            "Ground state ⁴I_9/2, pump bands ⁴F_5/2, upper laser state ⁴F_3/2, and lower laser state ⁴I_11/2.",
            "Because the lower laser level is well above the ground level and thermally depopulated, population inversion is achieved easily."
          ],
          "keyConcept": "Nd:YAG is a four-level solid state laser emitting at 1064 nm."
        }
      },
      {
        "id": 17,
        "question": "A Gallium Arsenide (GaAs) laser is classified as a:",
        "options": [
          "Semiconductor diode laser",
          "Dye laser (across all standard operating temperatures)",
          "Ruby laser",
          "Gas laser (independent of external field perturbations)"
        ],
        "correctIndex": 0,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "GaAs has a direct bandgap (1.42 eV).",
            "Forward-biasing a GaAs p-n junction causes electrons and holes to recombine directly across the bandgap, releasing stimulated photons in the near-infrared (~840-904 nm)."
          ],
          "keyConcept": "GaAs is an injection semiconductor laser diode."
        }
      },
      {
        "id": 18,
        "question": "A Hologram records and reconstructs:",
        "options": [
          "Neither amplitude nor phase (across all standard operating temperatures)",
          "Both amplitude and phase of the object wave",
          "Amplitude only of the object wave",
          "Phase only of the object wave"
        ],
        "correctIndex": 1,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Standard photography records only the intensity (amplitude squared) of light, losing depth cues.",
            "Holography utilizes an interference pattern between a reference laser beam and an object beam, capturing both amplitude and phase information."
          ],
          "keyConcept": "Holography reproduces a true 3D image by recording both amplitude and phase."
        }
      },
      {
        "id": 19,
        "question": "A Helium-Neon (He-Ne) laser operates as a:",
        "options": [
          "None of these",
          "3-Level Laser",
          "4-Level Laser",
          "2-Level Laser"
        ],
        "correctIndex": 2,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "In a He-Ne laser, collision between excited He atoms and ground state Ne atoms excites Neon to 2s and 3s levels.",
            "Lasing transitions occur down to 2p levels (giving 632.8 nm red light), which subsequently decay to 1s and ground state.",
            "This constitutes a classic 4-level energy scheme."
          ],
          "keyConcept": "He-Ne laser is a 4-level continuous-wave gas laser."
        }
      },
      {
        "id": 20,
        "question": "Which of the following is NOT true for laser light?",
        "options": [
          "Highly divergent",
          "Extremely intense light",
          "Perfect monochromaticity",
          "Highly coherent"
        ],
        "correctIndex": 0,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Laser beams have very low angular divergence (~1 milliradian) and travel vast distances without spreading out.",
            "Therefore, stating that laser light is \"highly divergent\" is false."
          ],
          "keyConcept": "Laser beams are highly directional with minimal divergence."
        }
      },
      {
        "id": 21,
        "question": "The propagation of light through an optical fiber is governed by the principle of:",
        "options": [
          "Interference (in an ideal homogeneous medium)",
          "Diffraction (under steady-state operating conditions)",
          "Refraction (as determined by Maxwell boundary constraints)",
          "Total Internal Reflection (TIR)"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "The core has refractive index n₁ and cladding has n₂, where n₁ > n₂.",
            "Light launched within the acceptance cone strikes the core-cladding boundary at an angle greater than the critical angle θ_c.",
            "Hence, it undergoes repeated total internal reflections and stays guided inside the core."
          ],
          "keyConcept": "Total Internal Reflection is the guiding principle of optical fibers."
        }
      },
      {
        "id": 22,
        "question": "A step-index fiber has a core refractive index of 1.45 and a cladding refractive index of 1.40. Its Numerical Aperture (NA) is:",
        "options": [
          "0.4863",
          "0.3775",
          "0.1562",
          "0.2441"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Formula: NA = √(n₁² - n₂²)",
            "n₁ = 1.45, n₂ = 1.40",
            "n₁² = 1.45² = 2.1025",
            "n₂² = 1.40² = 1.9600",
            "NA = √(2.1025 - 1.9600) = √(0.1425) ≈ 0.37749 ≈ 0.3775."
          ],
          "keyConcept": "NA = √(n₁² - n₂²)."
        }
      },
      {
        "id": 23,
        "question": "The necessary condition for Total Internal Reflection to occur at the core-cladding interface is:",
        "options": [
          "sin θ ≥ n₁ / n₂ (as determined by Maxwell boundary constraints)",
          "sin θ ≥ n₂ / n₁ (where θ is angle of incidence at boundary)",
          "sin θ = n₁ / n₂ (governed by linear superposition principles)",
          "sin θ ≤ n₂ / n₁ (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "At the critical angle θ_c, by Snell's law: n₁ sin θ_c = n₂ sin 90° ⇒ sin θ_c = n₂ / n₁.",
            "For total internal reflection to occur, the incident angle θ must be greater than or equal to the critical angle: θ ≥ θ_c ⇒ sin θ ≥ sin θ_c = n₂ / n₁."
          ],
          "keyConcept": "Critical angle condition: sin θ ≥ n₂ / n₁ with n₁ > n₂."
        }
      },
      {
        "id": 24,
        "question": "Which of the following causes optical attenuation (loss) inside a glass optical fiber?",
        "options": [
          "Material absorption",
          "Radiative loss",
          "All of the above",
          "Rayleigh scattering"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Optical fiber signal loss occurs due to:",
            "1. Absorption (intrinsic electronic/vibrational absorption and extrinsic impurity absorption like OH⁻ ions).",
            "2. Scattering (primarily Rayleigh scattering due to sub-microscopic density variations).",
            "3. Radiative losses (microbending and macrobending losses)."
          ],
          "keyConcept": "Total attenuation = Absorption + Scattering + Bending (Radiative) losses."
        }
      },
      {
        "id": 25,
        "question": "In an optical fiber, the refractive index of core (n₁) and cladding (n₂) must satisfy the inequality:",
        "options": [
          "n₁ > n₂",
          "n₁ < n₂",
          "n₁ = n₂",
          "n₁² ≤ n₂²"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Total internal reflection only occurs when light travels from an optically denser medium into an optically rarer medium.",
            "Therefore, the refractive index of the core n₁ must strictly exceed that of the cladding n₂ (n₁ > n₂)."
          ],
          "keyConcept": "Guidance requirement: n_core > n_cladding."
        }
      },
      {
        "id": 26,
        "question": "The numerical aperture (NA) of a step-index optical fiber is defined as:",
        "options": [
          "(n₂ - n₁)",
          "√(n₁² + n₂²)",
          "√(n₁² - n₂²)",
          "(n₁ - n₂)"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "The acceptance angle θ₀ in air (n₀ = 1) is given by: sin θ₀ = √(n₁² - n₂²).",
            "By definition, Numerical Aperture NA = sin θ₀ = √(n₁² - n₂²)."
          ],
          "keyConcept": "NA = sin(acceptance angle) = √(n₁² - n₂²)."
        }
      },
      {
        "id": 27,
        "question": "A step-index fiber has a numerical aperture of 0.26. What is the acceptance angle of the fiber in air?",
        "options": [
          "1.47°",
          "24.15°",
          "2.18°",
          "15.07°"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Formula: θ₀ = sin⁻¹(NA)",
            "θ₀ = sin⁻¹(0.26)",
            "Since sin(15°) = 0.2588, sin⁻¹(0.26) ≈ 15.07°."
          ],
          "keyConcept": "Acceptance angle θ₀ = arcsin(NA)."
        }
      },
      {
        "id": 28,
        "question": "The normalized frequency parameter (V-number) for a Single-Mode step-index optical fiber must satisfy:",
        "options": [
          "V < 2.405",
          "None of these",
          "V = 2.405",
          "V > 2.405"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "The normalized frequency parameter is V = (2π a / λ) √(n₁² - n₂²).",
            "For a step-index fiber to support only a single fundamental mode (HE₁₁), V must remain below the first Bessel zero cutoff: V < 2.405."
          ],
          "keyConcept": "Single mode cutoff condition: V ≤ 2.405."
        }
      },
      {
        "id": 29,
        "question": "The maximum number of guided modes (N_max) supported by a step-index multimode fiber is given approximately by:",
        "options": [
          "V² / 4",
          "V² / 3",
          "V² / 2",
          "2 V²"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "For large V, the number of propagating spatial modes in a step-index fiber is N ≈ V² / 2.",
            "For graded-index (parabolic profile) fibers, the number of modes is N ≈ V² / 4."
          ],
          "keyConcept": "Step-index mode capacity: N ≈ V² / 2."
        }
      },
      {
        "id": 30,
        "question": "If the V-number of a single-mode step-index fiber is 2.305, the total number of fundamental supported guided modes is:",
        "options": [
          "8",
          "2",
          "1",
          "4"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Since V = 2.305 < 2.405, higher-order modes cannot propagate.",
            "Only the single fundamental HE₁₁ mode (with two orthogonal polarization states) is guided through the fiber core."
          ],
          "keyConcept": "When V < 2.405, the fiber strictly operates in single-mode regime."
        }
      }
    ]
  },
  {
    "id": "phy110-midterm-paper-2",
    "code": "PHY110-PAPER-B",
    "title": "Midterm Examination • Paper 2 (Official University PYQ)",
    "courseCode": "PHY110",
    "courseName": "Engineering Physics",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Lasers",
      "Fiber Optics",
      "Maxwell Equations",
      "Electromagnetism"
    ],
    "description": "Verified university midterm paper B testing atomic transitions, population inversion, optical pumping wavelengths, graded-index fibers, and Maxwell's equations.",
    "questions": [
      {
        "id": 1,
        "question": "What is the fundamental physical process by which a laser amplifies light?",
        "options": [
          "Absorption of light",
          "Stimulated emission of light",
          "Refraction of light",
          "Spontaneous emission of light"
        ],
        "correctIndex": 1,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "In stimulated emission, an incoming photon triggers an excited electron to drop to a lower state, releasing an identical coherent photon.",
            "This causes optical amplification in the active medium."
          ],
          "keyConcept": "Stimulated emission is the foundation of laser amplification."
        }
      },
      {
        "id": 2,
        "question": "Which of the following is NOT one of the essential energy level types in a typical laser system?",
        "options": [
          "Metastable state",
          "Excited pump state",
          "Ground state (under steady-state operating conditions)",
          "Intermediate unphysical state"
        ],
        "correctIndex": 3,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "A laser requires a Ground State (low energy), an Excited State (pump band), and a long-lived Metastable State (~10⁻³ s vs 10⁻⁸ s).",
            "Intermediate unphysical state is not a real physical energy level."
          ],
          "keyConcept": "The metastable state provides the necessary storage lifetime for population inversion."
        }
      },
      {
        "id": 3,
        "question": "What happens to an atom when it absorbs a photon whose energy equals the difference between two quantum states (E₂ - E₁ = hν)?",
        "options": [
          "It moves to a higher energy level",
          "It moves to a lower energy level",
          "It emits a photon of light",
          "Nothing happens (across all standard operating temperatures)"
        ],
        "correctIndex": 0,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "By the Einstein absorption postulate, absorbing energy hν lifts an electron from lower energy state E₁ to higher excited energy state E₂."
          ],
          "keyConcept": "Optical absorption elevates an atom from ground/lower state to excited state."
        }
      },
      {
        "id": 4,
        "question": "Which type of emission occurs naturally, spontaneously, and with random phase and direction?",
        "options": [
          "Absorption",
          "Stimulated emission",
          "Spontaneous emission",
          "Stimulated absorption"
        ],
        "correctIndex": 2,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Without any external triggering photon, an excited electron drops spontaneously after lifetime ~10⁻⁸ s.",
            "The emitted photon has arbitrary phase, polarization, and direction, which is Spontaneous Emission."
          ],
          "keyConcept": "Spontaneous emission generates ordinary incoherent light."
        }
      },
      {
        "id": 5,
        "question": "Population inversion in a laser active medium occurs when:",
        "options": [
          "There are equal numbers of atoms in both states (as determined by Maxwell boundary constraints)",
          "More atoms are in the excited/metastable state than the ground state",
          "More atoms are in the ground state than the excited state",
          "No atoms are in the ground state (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Under thermal equilibrium (Boltzmann distribution), N₁ > N₂.",
            "Population inversion reverses this so that N₂ > N₁, making stimulated emission dominant over absorption."
          ],
          "keyConcept": "Population inversion condition: N₂ > N₁."
        }
      },
      {
        "id": 6,
        "question": "What is the active lasing ion/medium in a Nd:YAG laser?",
        "options": [
          "Neon (across all standard operating temperatures)",
          "Aluminium",
          "Neodymium (Nd³⁺ ions)",
          "Silicon"
        ],
        "correctIndex": 2,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Nd:YAG is Yttrium Aluminium Garnet (Y₃Al₅O₁₂) doped with approximately 1% Neodymium (Nd³⁺) ions.",
            "The Nd³⁺ ions serve as the active lasing centers."
          ],
          "keyConcept": "Nd³⁺ ions are the active lasing medium in Nd:YAG."
        }
      },
      {
        "id": 7,
        "question": "What is the typical dominant emission wavelength of a red Helium-Neon (He-Ne) laser?",
        "options": [
          "1550 nm",
          "632.8 nm",
          "1064 nm",
          "980 nm"
        ],
        "correctIndex": 1,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "The prominent red transition in a He-Ne laser is from 3s₂ to 2p₄ level of Neon, emitting at 632.8 nm.",
            "1064 nm is Nd:YAG, and 1550 nm is standard optical telecom."
          ],
          "keyConcept": "He-Ne laser emits at λ = 632.8 nm."
        }
      },
      {
        "id": 8,
        "question": "What is the primary excitation mechanism utilized in a Nd:YAG laser?",
        "options": [
          "Optical pumping (flashlamp or diode)",
          "Electric discharge (in an ideal homogeneous medium)",
          "Chemical reaction (under steady-state operating conditions)",
          "Electron beam excitation"
        ],
        "correctIndex": 0,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Nd:YAG lasers are optically pumped using a Krypton/Xenon arc flashlamp or semiconductor laser diode arrays."
          ],
          "keyConcept": "Nd:YAG uses optical pumping."
        }
      },
      {
        "id": 9,
        "question": "In an optical fiber, light is guided through the core primarily by means of:",
        "options": [
          "Polarization",
          "Interference",
          "Diffraction",
          "Total internal reflection"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Light injected within the acceptance angle experiences total internal reflection repeatedly at the core-cladding boundary."
          ],
          "keyConcept": "Total Internal Reflection is the waveguiding mechanism in fibers."
        }
      },
      {
        "id": 10,
        "question": "The core of an optical fiber is manufactured out of:",
        "options": [
          "Aluminium (under steady-state operating conditions)",
          "Copper (as determined by Maxwell boundary constraints)",
          "Clear high-purity silica glass or plastic",
          "Graphite (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Optical fiber cores are made of ultra-pure fused silica (SiO₂) glass doped with Germanium (GeO₂) or transparent polymers."
          ],
          "keyConcept": "Fiber cores are made of high-purity silica glass."
        }
      },
      {
        "id": 11,
        "question": "Total internal reflection occurs only when light travels from a:",
        "options": [
          "Vacuum to water",
          "Rarer to denser medium",
          "Denser to rarer medium",
          "Air to glass"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "By Snell's law, light bends away from the normal when moving from an optically denser medium into a rarer medium (n₁ > n₂).",
            "When angle of incidence exceeds critical angle θ_c, refracted ray cannot escape, producing total internal reflection."
          ],
          "keyConcept": "TIR requires traveling from denser medium into rarer medium."
        }
      },
      {
        "id": 12,
        "question": "In an optical fiber, dispersion causes:",
        "options": [
          "Pulse rise-time reduction",
          "Pulse distortion and pulse broadening",
          "Pulse narrowing (independent of external field perturbations)",
          "Zero propagation loss (in an ideal homogeneous medium)"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Different spectral components (chromatic dispersion) or different propagation modes (intermodal dispersion) travel at different group velocities.",
            "This causes light pulses to spread out temporally (pulse broadening), leading to intersymbol interference (ISI)."
          ],
          "keyConcept": "Dispersion results in pulse broadening and limits maximum data rate."
        }
      },
      {
        "id": 13,
        "question": "In a Graded-Index (GRIN) optical fiber, the refractive index of the core:",
        "options": [
          "Increases toward the cladding (governed by linear superposition principles)",
          "Remains constant throughout the core (independent of external field perturbations)",
          "Is equal to the cladding index (in an ideal homogeneous medium)",
          "Decreases continuously and parabolically from the central axis to the cladding boundary"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "In GRIN fibers, the refractive index is highest at the center axis and decreases continuously as n(r) = n₁[1 - 2Δ(r/a)²]^(1/2).",
            "This causes light rays to bend continuously in sinusoidal curves, equalizing transit times and minimizing modal dispersion."
          ],
          "keyConcept": "Graded-index core has a parabolic refractive index profile."
        }
      },
      {
        "id": 14,
        "question": "The condition for a vector field V to be solenoidal is:",
        "options": [
          "∇ · V = 0",
          "∇²V = 0",
          "∇ × V = 0",
          "∇V = 0"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "A field with zero divergence (∇ · V = 0) has no net source or sink in the region.",
            "Such a field is called solenoidal."
          ],
          "keyConcept": "Solenoidal field condition: ∇ · V = 0."
        }
      },
      {
        "id": 15,
        "question": "The gradient of any scalar field φ (grad φ = ∇φ) is always a:",
        "options": [
          "Tensor of rank 2",
          "Scalar quantity",
          "Dimensionless constant",
          "Vector quantity"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "Grad φ = (∂φ/∂x) i + (∂φ/∂y) j + (∂φ/∂z) k.",
            "It points in the direction of the maximum rate of increase of φ and is a vector."
          ],
          "keyConcept": "Gradient of a scalar field is a vector."
        }
      },
      {
        "id": 16,
        "question": "The divergence of any vector field A (div A = ∇ · A) is always a:",
        "options": [
          "None of these",
          "Scalar quantity",
          "Vector quantity",
          "Both vector and scalar"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus",
        "explanation": {
          "steps": [
            "∇ · A = (∂A_x/∂x) + (∂A_y/∂y) + (∂A_z/∂z).",
            "Since it is a scalar dot product of operators, the outcome is a scalar quantity."
          ],
          "keyConcept": "Divergence of a vector is a scalar."
        }
      },
      {
        "id": 17,
        "question": "Maxwell's Second Equation (∇ · B = 0) represents:",
        "options": [
          "Faraday's Law of induction (as determined by Maxwell boundary constraints)",
          "Gauss's Law for magnetostatics (non-existence of isolated magnetic monopoles)",
          "Gauss's Law for electrostatics (governed by linear superposition principles)",
          "Ampere's Circuital Law (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "∇ · B = 0 states that total magnetic flux entering any closed surface equals total flux leaving it.",
            "This physically proves that isolated magnetic monopoles do not exist; magnetic field lines are always closed continuous loops."
          ],
          "keyConcept": "∇ · B = 0 signifies Gauss's law for magnetism (no isolated monopoles)."
        }
      },
      {
        "id": 18,
        "question": "What is the constitutive relation connecting magnetic field intensity H, magnetic flux density B, and permeability of free space μ₀?",
        "options": [
          "B = μ₀ H",
          "B = H / μ₀",
          "H = μ₀ B",
          "B = μ₀ + H"
        ],
        "correctIndex": 0,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "In non-magnetic or isotropic media: B = μ H = μ_r μ₀ H.",
            "In vacuum or free space: B = μ₀ H."
          ],
          "keyConcept": "Constitutive relation: B = μ₀ H."
        }
      },
      {
        "id": 19,
        "question": "How is the uniform electric field E related to electric potential V across a conductor of length L?",
        "options": [
          "V = E · L",
          "V = E / L",
          "E = V² / L",
          "E = V · L"
        ],
        "correctIndex": 0,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "Electric field is negative gradient of potential: E = -dV/dx.",
            "For a uniform field across distance L: E = V / L, which gives V = E · L."
          ],
          "keyConcept": "Potential difference V = E · L."
        }
      },
      {
        "id": 20,
        "question": "Maxwell's First Equation in differential form is:",
        "options": [
          "∇ × H = J + ∂D/∂t",
          "∇ · B = 0",
          "∇ × E = -∂B/∂t",
          "∇ · D = ρ"
        ],
        "correctIndex": 3,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "Maxwell's first equation is Gauss's Law for electric fields: ∇ · D = ρ (or ∇ · E = ρ/ε₀ in free space)."
          ],
          "keyConcept": "Maxwell 1st equation: ∇ · D = ρ."
        }
      },
      {
        "id": 21,
        "question": "Maxwell's Third Equation represents which fundamental law of electromagnetism?",
        "options": [
          "Ampere's Circuital Law (in an ideal homogeneous medium)",
          "Electrostatic Gauss law (under steady-state operating conditions)",
          "Faraday's Law of Electromagnetic Induction",
          "Coulomb's Law (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "Maxwell's third equation is ∇ × E = -∂B/∂t.",
            "This states that a time-varying magnetic field induces a circulating electric field, which is Faraday's Law."
          ],
          "keyConcept": "Maxwell 3rd equation is Faraday's Law of Induction."
        }
      },
      {
        "id": 22,
        "question": "Maxwell's Fourth Equation is modified from Ampere's law by introducing the concept of:",
        "options": [
          "Displacement current (∂D/∂t)",
          "Leakage current",
          "Conduction current",
          "Eddy current (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "Ampere's law ∇ × H = J failed for time-varying fields because div(curl H) = 0 while div J = -∂ρ/∂t ≠ 0.",
            "Maxwell introduced displacement current density J_D = ∂D/∂t to satisfy the continuity equation."
          ],
          "keyConcept": "Displacement current J_D = ∂D/∂t made Maxwell's equations consistent."
        }
      },
      {
        "id": 23,
        "question": "Which of the following is true for electromagnetic waves propagating in free space?",
        "options": [
          "Speed is independent of permittivity and permeability (as determined by Maxwell boundary constraints)",
          "Electric and magnetic field vectors are parallel to each other (across all standard operating temperatures)",
          "Electric and magnetic field vectors are mutually perpendicular and perpendicular to direction of wave propagation",
          "Only electric field propagates (independent of external field perturbations)"
        ],
        "correctIndex": 2,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "EM waves are transverse in nature.",
            "E ⊥ B, and both are perpendicular to the propagation vector k (E × B gives direction of wave velocity)."
          ],
          "keyConcept": "EM waves are transverse: E ⊥ B ⊥ k."
        }
      },
      {
        "id": 24,
        "question": "The velocity of an electromagnetic wave in free space is given by:",
        "options": [
          "c = √(μ₀ ε₀)",
          "c = 1 / √(μ₀ ε₀)",
          "c = ε₀ / μ₀",
          "c = μ₀ / ε₀"
        ],
        "correctIndex": 1,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "From wave equation derived from Maxwell's equations: ∇²E = μ₀ε₀ (∂²E/∂t²).",
            "Comparing with standard wave equation ∇²E = (1/v²)(∂²E/∂t²), wave velocity is c = 1 / √(μ₀ ε₀) ≈ 3 × 10⁸ m/s."
          ],
          "keyConcept": "Speed of light c = 1 / √(μ₀ ε₀)."
        }
      },
      {
        "id": 25,
        "question": "Poynting vector S represents:",
        "options": [
          "Power dissipated as heat (governed by linear superposition principles)",
          "Electrostatic force per unit charge (independent of external field perturbations)",
          "Total charge stored in medium (in an ideal homogeneous medium)",
          "Rate of energy flow per unit area in an electromagnetic field (S = E × H)"
        ],
        "correctIndex": 3,
        "topic": "Electromagnetic Theory",
        "explanation": {
          "steps": [
            "The Poynting vector S = E × H (in W/m²).",
            "Its direction indicates the direction of energy transport and its magnitude represents instantaneous power flux density."
          ],
          "keyConcept": "Poynting vector S = E × H measures directional power flow density."
        }
      },
      {
        "id": 26,
        "question": "For a medium with core index n₁ = 1.50 and cladding index n₂ = 1.48, the fractional refractive index difference Δ is:",
        "options": [
          "0.0067",
          "0.0400",
          "0.0133",
          "0.0200"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Formula: Δ = (n₁ - n₂) / n₁",
            "Δ = (1.50 - 1.48) / 1.50 = 0.02 / 1.50 = 2 / 150 ≈ 0.0133 (or 1.33%)."
          ],
          "keyConcept": "Δ = (n₁ - n₂) / n₁."
        }
      },
      {
        "id": 27,
        "question": "In an optical fiber, what does the buffer coating provide?",
        "options": [
          "Optical amplification (in an ideal homogeneous medium)",
          "Light guidance (under steady-state operating conditions)",
          "Mechanical strength and physical protection against moisture and abrasion",
          "Higher refractive index (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "The primary buffer coating is made of silicones, acrylates, or polymers.",
            "Its role is to protect the brittle silica fiber from mechanical abrasion, crushing, and environmental moisture."
          ],
          "keyConcept": "Buffer coating provides physical and mechanical protection."
        }
      },
      {
        "id": 28,
        "question": "A laser cavity resonator consists of:",
        "options": [
          "An active medium placed between two parallel optical mirrors (one 100% reflective, one partially transmissive)",
          "Two prisms (as determined by Maxwell boundary constraints)",
          "A single concave lens (across all standard operating temperatures)",
          "A copper waveguide (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "An optical resonator (Fabry-Perot cavity) consists of two aligned mirrors.",
            "Light bounces back and forth through the active medium, building up amplified stimulated emission before leaking out the partial mirror as the laser beam."
          ],
          "keyConcept": "Optical cavity resonator provides positive optical feedback."
        }
      },
      {
        "id": 29,
        "question": "What is the role of Helium in a Helium-Neon (He-Ne) laser?",
        "options": [
          "It cools the discharge tube (as determined by Maxwell boundary constraints)",
          "It absorbs spontaneous emissions (across all standard operating temperatures)",
          "It acts as the primary lasing medium (governed by linear superposition principles)",
          "He atoms are excited by electron collision and transfer their energy to Neon atoms via resonant collision"
        ],
        "correctIndex": 3,
        "topic": "Lasers",
        "explanation": {
          "steps": [
            "Helium atoms have metastable 2¹S and 2³S states with energies 20.61 eV and 19.82 eV, perfectly matching the 3s and 2s levels of Neon.",
            "Helium atoms efficiently transfer energy to Neon atoms through resonant collisions, establishing population inversion in Neon."
          ],
          "keyConcept": "Helium enables efficient resonant excitation of Neon atoms."
        }
      },
      {
        "id": 30,
        "question": "If a step-index fiber has core diameter 50 μm, n₁ = 1.48, and n₂ = 1.46 at wavelength λ = 1.3 μm, the acceptance angle is:",
        "options": [
          "9.82°",
          "21.50°",
          "18.45°",
          "14.07°"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "NA = √(n₁² - n₂²) = √(1.48² - 1.46²) = √(2.1904 - 2.1316) = √(0.0588) ≈ 0.2425.",
            "Acceptance angle θ₀ = sin⁻¹(0.2425) ≈ 14.04° ~ 14.07°."
          ],
          "keyConcept": "Acceptance angle θ₀ = sin⁻¹(√(n₁² - n₂²))."
        }
      }
    ]
  },
  {
    "id": "phy110-midterm-paper-3",
    "code": "PHY110-PAPER-C",
    "title": "Midterm Examination • Paper 3 (Maxwell's Equations & Field Dynamics)",
    "courseCode": "PHY110",
    "courseName": "Engineering Physics",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Vector Calculus",
      "Maxwell Equations",
      "Lasers",
      "Fiber Optics"
    ],
    "description": "Intensive examination on Gauss & Stokes theorems, continuity equations, displacement current density, and plane wave propagation.",
    "questions": [
      {
        "id": 1,
        "question": "The total instantaneous energy density $u$ of an electromagnetic wave in a medium of permittivity $\\epsilon$ and permeability $\\mu$ is:",
        "options": [
          "$u = \\vec{E} \\times \\vec{B}$ (as determined by Maxwell boundary constraints)",
          "$u = \\frac{1}{2}\\epsilon E + \\frac{1}{2}\\mu B$",
          "$u = \\epsilon E^2$ (governed by linear superposition principles)",
          "$u = \\frac{1}{2}\\epsilon E^2 + \\frac{1}{2\\mu} B^2$"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Total energy density is the sum of electrostatic energy $\\frac{1}{2}\\epsilon E^2$ and magnetostatic energy $\\frac{1}{2\\mu} B^2$."
          ],
          "keyConcept": "Total energy density is the sum of electrostatic energy $\\frac{1}{2}\\epsilon E^2$ and magnetostatic energy $\\frac{1}{2\\m..."
        }
      },
      {
        "id": 2,
        "question": "In a plane electromagnetic wave traveling in vacuum, the ratio of electric field amplitude $E_0$ to magnetic field amplitude $B_0$ is:",
        "options": [
          "$c$",
          "$1/c$",
          "$\\sqrt{c}$",
          "$c^2$"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "In vacuum, $E_0 / B_0 = c$, where $c$ is the speed of light."
          ],
          "keyConcept": "In vacuum, $E_0 / B_0 = c$, where $c$ is the speed of light."
        }
      },
      {
        "id": 3,
        "question": "The skin depth $\\delta$ in a conducting medium represents the penetration distance at which wave field amplitude decreases to:",
        "options": [
          "$50\\%$ of its surface value",
          "Zero",
          "$1/e \\approx 36.8\\%$ of its surface value",
          "$1/e^2 \\approx 13.5\\%$ of its surface value"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Skin depth $\\delta = 1/\\alpha$ is the depth where field amplitude attenuates by a factor of $e^{-1} \\approx 0.368$."
          ],
          "keyConcept": "Skin depth $\\delta = 1/\\alpha$ is the depth where field amplitude attenuates by a factor of $e^{-1} \\approx 0.368$."
        }
      },
      {
        "id": 4,
        "question": "The mathematical formula for skin depth $\\delta$ in a good conductor of conductivity $\\sigma$ and permeability $\\mu$ at frequency $\\omega$ is:",
        "options": [
          "$\\delta = \\frac{\\omega}{\\mu \\sigma}$",
          "$\\delta = \\sqrt{\\frac{2}{\\omega \\mu \\sigma}}$",
          "$\\delta = \\sqrt{\\frac{\\omega \\mu}{2\\sigma}}$",
          "$\\delta = \\sqrt{\\frac{\\sigma}{2\\omega \\mu}}$"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Skin depth for good conductors ($\\sigma \\gg \\omega\\epsilon$) is $\\delta = \\sqrt{2/(\\omega \\mu \\sigma)}$."
          ],
          "keyConcept": "Skin depth for good conductors ($\\sigma \\gg \\omega\\epsilon$) is $\\delta = \\sqrt{2/(\\omega \\mu \\sigma)}$."
        }
      },
      {
        "id": 5,
        "question": "As the operating frequency of an electromagnetic wave in a conductor increases, the skin depth $\\delta$:",
        "options": [
          "Increases exponentially",
          "Increases linearly",
          "Remains completely unchanged",
          "Decreases as $1/\\sqrt{f}$"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Because $\\delta \\propto 1/\\sqrt{\\omega} = 1/\\sqrt{2\\pi f}$, higher frequencies result in shallower skin depths."
          ],
          "keyConcept": "Because $\\delta \\propto 1/\\sqrt{\\omega} = 1/\\sqrt{2\\pi f}$, higher frequencies result in shallower skin depths."
        }
      },
      {
        "id": 6,
        "question": "For a plane EM wave incident normally on a perfectly absorbing surface, the radiation pressure exerted is:",
        "options": [
          "$P_{\\text{rad}} = \\frac{2\\langle S \\rangle}{c}$",
          "$P_{\\text{rad}} = \\frac{\\langle S \\rangle}{c}$",
          "$P_{\\text{rad}} = \\frac{\\langle S \\rangle}{2c}$",
          "$P_{\\text{rad}} = \\langle S \\rangle c$"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "For complete absorption, momentum transferred per unit area per second is $\\langle S \\rangle / c$."
          ],
          "keyConcept": "For complete absorption, momentum transferred per unit area per second is $\\langle S \\rangle / c$."
        }
      },
      {
        "id": 7,
        "question": "For a plane EM wave incident normally on a perfectly reflecting mirror, the radiation pressure exerted is:",
        "options": [
          "$P_{\\text{rad}} = \\frac{4\\langle S \\rangle}{c}$",
          "$P_{\\text{rad}} = \\frac{\\langle S \\rangle}{c}$",
          "$P_{\\text{rad}} = 0$",
          "$P_{\\text{rad}} = \\frac{2\\langle S \\rangle}{c}$"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Reflection reverses the momentum of the photons, giving double the momentum transfer: $\\Delta p = 2U/c \\implies P = 2\\langle S \\rangle/c$."
          ],
          "keyConcept": "Reflection reverses the momentum of the photons, giving double the momentum transfer: $\\Delta p = 2U/c \\implies P = 2\\la..."
        }
      },
      {
        "id": 8,
        "question": "In a lossless dielectric medium with relative permittivity $\\epsilon_r = 4$ and relative permeability $\\mu_r = 1$, the wave velocity is:",
        "options": [
          "$0.75 \\times 10^8\\text{ m/s}$",
          "$3 \\times 10^8\\text{ m/s}$",
          "$1.5 \\times 10^8\\text{ m/s}$",
          "$6 \\times 10^8\\text{ m/s}$"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "$v = c/\\sqrt{\\epsilon_r \\mu_r} = (3 \\times 10^8)/\\sqrt{4 \\times 1} = 1.5 \\times 10^8\\text{ m/s}$."
          ],
          "keyConcept": "$v = c/\\sqrt{\\epsilon_r \\mu_r} = (3 \\times 10^8)/\\sqrt{4 \\times 1} = 1.5 \\times 10^8\\text{ m/s}$."
        }
      },
      {
        "id": 9,
        "question": "At the boundary between two lossless dielectric media with no free surface charge, the normal component of:",
        "options": [
          "Poynting vector is zero (governed by linear superposition principles)",
          "Magnetic field intensity $\\vec{H}$ is discontinuous",
          "Electric displacement $\\vec{D}$ is continuous ($D_{1n} = D_{2n}$)",
          "Electric field $\\vec{E}$ is continuous (under steady-state operating conditions)"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "From $\\nabla \\cdot \\vec{D} = \\rho_s$, when surface free charge $\\rho_s = 0$, $D_{1n} - D_{2n} = 0 \\implies D_{1n} = D_{2n}$."
          ],
          "keyConcept": "From $\\nabla \\cdot \\vec{D} = \\rho_s$, when surface free charge $\\rho_s = 0$, $D_{1n} - D_{2n} = 0 \\implies D_{1n} = D_{2..."
        }
      },
      {
        "id": 10,
        "question": "At any interface between two different media with no surface conduction current, the tangential component of:",
        "options": [
          "Electric field $\\vec{E}$ is continuous ($E_{1t} = E_{2t}$)",
          "Vector potential $\\vec{A}$ is zero (in an ideal homogeneous medium)",
          "Magnetic induction $\\vec{B}$ is continuous (under steady-state operating conditions)",
          "Electric displacement $\\vec{D}$ is continuous"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "From Faraday's boundary condition $\\oint \\vec{E}\\cdot d\\vec{l} = 0$, tangential electric field $E_t$ is always continuous across boundaries."
          ],
          "keyConcept": "From Faraday's boundary condition $\\oint \\vec{E}\\cdot d\\vec{l} = 0$, tangential electric field $E_t$ is always continuou..."
        }
      },
      {
        "id": 11,
        "question": "In a Helium-Neon (He-Ne) gas laser, the ratio of Helium to Neon gas in the tube is typically:",
        "options": [
          "$100:1$",
          "$10:1$",
          "$1:1$",
          "$1:10$"
        ],
        "correctIndex": 1,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "The gas mixture is maintained at approximately $10:1$ (or $7:1$ to $10:1$) He to Ne at low pressure ($\\sim 1\\text{ Torr}$)."
          ],
          "keyConcept": "The gas mixture is maintained at approximately $10:1$ (or $7:1$ to $10:1$) He to Ne at low pressure ($\\sim 1\\text{ Torr}..."
        }
      },
      {
        "id": 12,
        "question": "In a He-Ne laser, the primary role of Helium atoms is to:",
        "options": [
          "Absorb electrical discharge energy and transfer it to Neon atoms via resonant collision",
          "Act as optical reflectors (as determined by Maxwell boundary constraints)",
          "Cool down the discharge tube walls (across all standard operating temperatures)",
          "Directly emit the red laser light (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Helium atoms are excited to metastable states $2^1S$ and $2^3S$ by electron collision and transfer energy to Neon levels $3s$ and $2s$ by resonant collisions."
          ],
          "keyConcept": "Helium atoms are excited to metastable states $2^1S$ and $2^3S$ by electron collision and transfer energy to Neon levels..."
        }
      },
      {
        "id": 13,
        "question": "The most common visible output transition in a He-Ne laser occurs at:",
        "options": [
          "$632.8\\text{ nm}$ (bright red)",
          "$10.6\\,\\mu\\text{m}$ (infrared)",
          "$694.3\\text{ nm}$ (deep red)",
          "$532.0\\text{ nm}$ (green)"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "The $3s_2 \\to 2p_4$ transition in Neon atoms produces the famous $632.8\\text{ nm}$ red laser line."
          ],
          "keyConcept": "The $3s_2 \\to 2p_4$ transition in Neon atoms produces the famous $632.8\\text{ nm}$ red laser line."
        }
      },
      {
        "id": 14,
        "question": "The output beam of a He-Ne laser is characterized as:",
        "options": [
          "Ultraviolet polychromatic emission (across all standard operating temperatures)",
          "Pulsed with gigawatt peak powers (governed by linear superposition principles)",
          "Continuous Wave (CW) with exceptional spatial and temporal coherence",
          "Thermal white light (in an ideal homogeneous medium)"
        ],
        "correctIndex": 2,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "He-Ne lasers operate in continuous wave (CW) mode with high beam directionality and long coherence lengths."
          ],
          "keyConcept": "He-Ne lasers operate in continuous wave (CW) mode with high beam directionality and long coherence lengths."
        }
      },
      {
        "id": 15,
        "question": "The active medium in a semiconductor diode laser is:",
        "options": [
          "A neodymium crystal (governed by linear superposition principles)",
          "An indirect bandgap silicon diode",
          "A direct bandgap p-n junction (such as GaAs)",
          "A helium gas chamber (under steady-state operating conditions)"
        ],
        "correctIndex": 2,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Semiconductor lasers require direct bandgap semiconductors (e.g., GaAs, InGaAsP) where radiative electron-hole recombination is efficient without phonons."
          ],
          "keyConcept": "Semiconductor lasers require direct bandgap semiconductors (e.g., GaAs, InGaAsP) where radiative electron-hole recombina..."
        }
      },
      {
        "id": 16,
        "question": "The optical feedback in a semiconductor diode laser is achieved by:",
        "options": [
          "External curved concave dielectric mirrors (independent of external field perturbations)",
          "The naturally cleaved, polished end-facets of the semiconductor crystal",
          "A mechanical chopper wheel (under steady-state operating conditions)",
          "A quartz prism (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 1,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "The high refractive index of GaAs ($n \\approx 3.6$) provides $\\sim 32\\%$ Fresnel reflectance at each cleaved facet, serving as built-in cavity mirrors."
          ],
          "keyConcept": "The high refractive index of GaAs ($n \\approx 3.6$) provides $\\sim 32\\%$ Fresnel reflectance at each cleaved facet, serv..."
        }
      },
      {
        "id": 17,
        "question": "The laser emission wavelength $\\lambda$ of a semiconductor diode laser is determined by its bandgap $E_g$ via:",
        "options": [
          "$\\lambda = \\frac{h c}{E_g}$",
          "$\\lambda = \\sqrt{\\frac{h c}{E_g}}$",
          "$\\lambda = \\frac{E_g}{h c}$",
          "$\\lambda = \\frac{h}{E_g c}$"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Photons are emitted by direct band-to-band carrier recombination: $h\\nu = E_g \\implies \\lambda = hc/E_g$."
          ],
          "keyConcept": "Photons are emitted by direct band-to-band carrier recombination: $h\\nu = E_g \\implies \\lambda = hc/E_g$."
        }
      },
      {
        "id": 18,
        "question": "The Nd:YAG laser operates as a:",
        "options": [
          "4-level solid-state laser emitting at $1064\\text{ nm}$",
          "3-level liquid dye laser (as determined by Maxwell boundary constraints)",
          "2-level gas laser (across all standard operating temperatures)",
          "1-level chemical laser (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Nd:YAG ($\\text{Y}_3\\text{Al}_5\\text{O}_{12}:\\text{Nd}^{3+}$) is a robust 4-level solid-state laser emitting near-infrared light at $1.064\\,\\mu\\text{m}$ ($1064\\text{ nm}$)."
          ],
          "keyConcept": "Nd:YAG ($\\text{Y}_3\\text{Al}_5\\text{O}_{12}:\\text{Nd}^{3+}$) is a robust 4-level solid-state laser emitting near-infrare..."
        }
      },
      {
        "id": 19,
        "question": "The Carbon Dioxide ($\\text{CO}_2$) laser generates high-power radiation in the far-infrared region at:",
        "options": [
          "$1.06\\,\\mu\\text{m}$",
          "$0.193\\,\\mu\\text{m}$",
          "$632.8\\text{ nm}$",
          "$10.6\\,\\mu\\text{m}$"
        ],
        "correctIndex": 3,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "$\\text{CO}_2$ lasers lase between quantized molecular vibrational-rotational energy states at $\\lambda = 10.6\\,\\mu\\text{m}$."
          ],
          "keyConcept": "$\\text{CO}_2$ lasers lase between quantized molecular vibrational-rotational energy states at $\\lambda = 10.6\\,\\mu\\text{..."
        }
      },
      {
        "id": 20,
        "question": "Coherence length $L_c$ is related to coherence time $\\tau_c$ and spectral linewidth $\\Delta \\nu$ by:",
        "options": [
          "$L_c = \\frac{\\Delta \\nu}{c}$",
          "$L_c = \\frac{c}{\\tau_c} = c \\Delta \\nu$",
          "$L_c = \\tau_c / c$",
          "$L_c = c \\tau_c = \\frac{c}{\\Delta \\nu}$"
        ],
        "correctIndex": 3,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Coherence length is the spatial distance over which light maintains definite phase: $L_c = c\\tau_c = c/\\Delta\\nu$."
          ],
          "keyConcept": "Coherence length is the spatial distance over which light maintains definite phase: $L_c = c\\tau_c = c/\\Delta\\nu$."
        }
      },
      {
        "id": 21,
        "question": "The strong extrinsic absorption peak near $\\lambda = 1383\\text{ nm}$ ($1.38\\,\\mu\\text{m}$) in standard silica fibers is caused by:",
        "options": [
          "Fundamental vibrations of Silicon-Oxygen bonds (governed by linear superposition principles)",
          "Iron ($\\text{Fe}^{3+}$) metallic impurities (independent of external field perturbations)",
          "Overtone vibrational resonances of hydroxyl ($\\text{OH}^-$) water impurity ions",
          "Nitrogen contamination (under steady-state operating conditions)"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "The fundamental $\\text{OH}^-$ stretch at $2.73\\,\\mu\\text{m}$ creates a strong second overtone harmonic absorption peak at $1.383\\,\\mu\\text{m}$."
          ],
          "keyConcept": "The fundamental $\\text{OH}^-$ stretch at $2.73\\,\\mu\\text{m}$ creates a strong second overtone harmonic absorption peak a..."
        }
      },
      {
        "id": 22,
        "question": "The three standard optical telecommunication windows centered at $850\\text{ nm}$, $1310\\text{ nm}$, and $1550\\text{ nm}$ correspond to regions of:",
        "options": [
          "Maximum reflection loss (independent of external field perturbations)",
          "Total optical opacity (in an ideal homogeneous medium)",
          "Maximum dispersion (under steady-state operating conditions)",
          "Minimal combined optical attenuation and favorable dispersion characteristics"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "These spectral windows exploit valleys in the silica attenuation curve: $850\\text{ nm}$ (GaAs source), $1310\\text{ nm}$ (zero dispersion), $1550\\text{ nm}$ (lowest loss)."
          ],
          "keyConcept": "These spectral windows exploit valleys in the silica attenuation curve: $850\\text{ nm}$ (GaAs source), $1310\\text{ nm}$ ..."
        }
      },
      {
        "id": 23,
        "question": "The lowest optical attenuation in pure silica glass optical fibers occurs in the third window ($\\lambda \\approx 1550\\text{ nm}$) with a loss of approximately:",
        "options": [
          "$20\\text{ dB/km}$",
          "$0.002\\text{ dB/km}$",
          "$2.0\\text{ dB/km}$",
          "$0.2\\text{ dB/km}$"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Modern ultra-pure silica single-mode fibers achieve an absolute minimum attenuation of $\\approx 0.18\\text{--}0.20\\text{ dB/km}$ at $1550\\text{ nm}$."
          ],
          "keyConcept": "Modern ultra-pure silica single-mode fibers achieve an absolute minimum attenuation of $\\approx 0.18\\text{--}0.20\\text{ ..."
        }
      },
      {
        "id": 24,
        "question": "Intermodal (modal) dispersion occurs exclusively in:",
        "options": [
          "Single-mode fibers",
          "Free space beams",
          "Multimode fibers",
          "Planar waveguides with $V < 1$"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Intermodal dispersion results from different spatial modes traveling along different path lengths with different transit times in multimode fibers."
          ],
          "keyConcept": "Intermodal dispersion results from different spatial modes traveling along different path lengths with different transit..."
        }
      },
      {
        "id": 25,
        "question": "The intermodal pulse broadening $\\Delta \\tau_{\\text{modal}}$ over a step-index fiber of length $L$ is given by:",
        "options": [
          "$\\Delta \\tau_{\\text{modal}} \\approx \\frac{L c \\Delta}{n_1}$",
          "$\\Delta \\tau_{\\text{modal}} \\approx \\frac{L n_1 \\Delta}{c}$",
          "$\\Delta \\tau_{\\text{modal}} \\approx \\frac{L n_1 \\Delta^2}{c}$",
          "$\\Delta \\tau_{\\text{modal}} \\approx \\frac{L}{c n_1 \\Delta}$"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "$\\Delta\\tau = t_{\\text{slowest}} - t_{\\text{fastest}} = \\frac{L n_1^2}{c n_2} - \\frac{L n_1}{c} \\approx \\frac{L n_1 \\Delta}{c}$."
          ],
          "keyConcept": "$\\Delta\\tau = t_{\\text{slowest}} - t_{\\text{fastest}} = \\frac{L n_1^2}{c n_2} - \\frac{L n_1}{c} \\approx \\frac{L n_1 \\Del..."
        }
      },
      {
        "id": 26,
        "question": "Why is intermodal dispersion completely absent in Single-Mode Fibers (SMF)?",
        "options": [
          "Because light travels as a sound wave (across all standard operating temperatures)",
          "Because single-mode fibers have zero core index (governed by linear superposition principles)",
          "Because the cladding absorbs all light (independent of external field perturbations)",
          "Because only one single fundamental spatial mode ($\\text{HE}_{11}$) can propagate, eliminating mode transit time differences"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "In single-mode fibers, light propagates strictly as a solitary spatial mode, completely eliminating intermodal time delays."
          ],
          "keyConcept": "In single-mode fibers, light propagates strictly as a solitary spatial mode, completely eliminating intermodal time dela..."
        }
      },
      {
        "id": 27,
        "question": "Intramodal (chromatic) dispersion in single-mode fibers is the combined sum of:",
        "options": [
          "Material dispersion ($D_M$) and Waveguide dispersion ($D_W$)",
          "Rayleigh scattering and Bending loss (independent of external field perturbations)",
          "Intermodal dispersion and Polarization dispersion",
          "Absorption loss and Splice loss (under steady-state operating conditions)"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Total chromatic dispersion is $D_{\\text{chromatic}} = D_M + D_W$, where $D_M$ arises from wavelength-dependent refractive index $n(\\lambda)$ and $D_W$ from waveguide geometry."
          ],
          "keyConcept": "Total chromatic dispersion is $D_{\\text{chromatic}} = D_M + D_W$, where $D_M$ arises from wavelength-dependent refractiv..."
        }
      },
      {
        "id": 28,
        "question": "In standard single-mode silica fibers (ITU-T G.652), the zero-material-dispersion wavelength $\\lambda_0$ naturally occurs near:",
        "options": [
          "$2000\\text{ nm}$",
          "$1310\\text{ nm}$",
          "$850\\text{ nm}$",
          "$1550\\text{ nm}$"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "In pure fused silica, material dispersion $D_M$ crosses zero at $\\approx 1270\\text{ nm}$, yielding net chromatic dispersion zero at $\\approx 1310\\text{ nm}$."
          ],
          "keyConcept": "In pure fused silica, material dispersion $D_M$ crosses zero at $\\approx 1270\\text{ nm}$, yielding net chromatic dispers..."
        }
      },
      {
        "id": 29,
        "question": "In Dispersion-Shifted Fibers (DSF, ITU-T G.653), the zero-dispersion wavelength is shifted from $1310\\text{ nm}$ to $1550\\text{ nm}$ by:",
        "options": [
          "Operating at absolute zero (in an ideal homogeneous medium)",
          "Modifying the core refractive index profile to increase negative waveguide dispersion $D_W$",
          "Doping the fiber with copper (as determined by Maxwell boundary constraints)",
          "Increasing the fiber diameter to $1\\text{ mm}$ (across all standard operating temperatures)"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Designing a triangular or segmented index core tailors waveguide dispersion $D_W$ to cancel material dispersion $D_M$ directly at $1550\\text{ nm}$."
          ],
          "keyConcept": "Designing a triangular or segmented index core tailors waveguide dispersion $D_W$ to cancel material dispersion $D_M$ di..."
        }
      },
      {
        "id": 30,
        "question": "Macrobending loss in an optical fiber occurs when:",
        "options": [
          "The fiber is stretched longitudinally (under steady-state operating conditions)",
          "The temperature rises by $1^\\circ\\text{C}$ (as determined by Maxwell boundary constraints)",
          "The fiber is bent into a curve with a radius comparable to or smaller than a critical bend radius $R_c$",
          "Light frequency decreases by $1\\text{ Hz}$ (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "When bend radius $R \\le R_c$, the angle of incidence at the outer cladding boundary drops below the critical angle, causing light to radiate into the cladding."
          ],
          "keyConcept": "When bend radius $R \\le R_c$, the angle of incidence at the outer cladding boundary drops below the critical angle, caus..."
        }
      }
    ]
  },
  {
    "id": "phy110-midterm-paper-4",
    "code": "PHY110-PAPER-D",
    "title": "Midterm Examination • Paper 4 (Laser Systems & Resonator Optics)",
    "courseCode": "PHY110",
    "courseName": "Engineering Physics",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Vector Calculus",
      "Maxwell Equations",
      "Lasers",
      "Fiber Optics"
    ],
    "description": "Focused university test evaluating Einstein coefficients, Ruby/He-Ne population dynamics, optical cavity stability, and laser gain.",
    "questions": [
      {
        "id": 1,
        "question": "At a boundary between two media with no surface current, the normal component of magnetic induction satisfies:",
        "options": [
          "$B_{1n} = 0$",
          "$B_{1n} = B_{2n}$",
          "$B_{1n} - B_{2n} = \\mu_0$",
          "$B_{1n} = -B_{2n}$"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "From $\\nabla \\cdot \\vec{B} = 0$, the normal component of magnetic flux density $B_n$ is always continuous across any interface."
          ],
          "keyConcept": "From $\\nabla \\cdot \\vec{B} = 0$, the normal component of magnetic flux density $B_n$ is always continuous across any int..."
        }
      },
      {
        "id": 2,
        "question": "In a conducting medium, the magnetic field $\\vec{H}$ lags behind the electric field $\\vec{E}$ by a phase angle of:",
        "options": [
          "$45^\\circ$ ($\\pi/4\\text{ rad}$)",
          "$180^\\circ$ ($\\pi\\text{ rad}$)",
          "$0^\\circ$",
          "$90^\\circ$ ($\\pi/2\\text{ rad}$)"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "The complex intrinsic impedance $\\eta_c = \\sqrt{\\frac{i\\omega\\mu}{\\sigma}} = |\\eta_c| e^{i\\pi/4}$ introduces a $45^\\circ$ phase lag for $\\vec{H}$."
          ],
          "keyConcept": "The complex intrinsic impedance $\\eta_c = \\sqrt{\\frac{i\\omega\\mu}{\\sigma}} = |\\eta_c| e^{i\\pi/4}$ introduces a $45^\\circ..."
        }
      },
      {
        "id": 3,
        "question": "A medium is characterized as a 'good conductor' when the loss tangent satisfies:",
        "options": [
          "$\\frac{\\sigma}{\\omega \\epsilon} = 1$",
          "$\\frac{\\sigma}{\\omega \\epsilon} \\ll 1$",
          "$\\frac{\\sigma}{\\omega \\epsilon} \\gg 1$",
          "$\\sigma = 0$"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "When conduction current dominates displacement current ($\\sigma \\gg \\omega\\epsilon$), the medium behaves as a good conductor."
          ],
          "keyConcept": "When conduction current dominates displacement current ($\\sigma \\gg \\omega\\epsilon$), the medium behaves as a good condu..."
        }
      },
      {
        "id": 4,
        "question": "A medium is characterized as a 'good dielectric' (low loss) when:",
        "options": [
          "$\\epsilon_r = 0$",
          "$\\sigma = \\infty$",
          "$\\frac{\\sigma}{\\omega \\epsilon} \\ll 1$",
          "$\\frac{\\sigma}{\\omega \\epsilon} \\gg 1$"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "When displacement current greatly exceeds conduction current ($\\sigma/\\omega\\epsilon \\ll 1$), it behaves as a low-loss dielectric."
          ],
          "keyConcept": "When displacement current greatly exceeds conduction current ($\\sigma/\\omega\\epsilon \\ll 1$), it behaves as a low-loss d..."
        }
      },
      {
        "id": 5,
        "question": "The time-averaged Poynting vector $\\langle \\vec{S} \\rangle$ for a plane harmonic wave in lossless media is given by:",
        "options": [
          "$\\langle \\vec{S} \\rangle = \\vec{E} \\times \\vec{H}$ (in an ideal homogeneous medium)",
          "$\\langle \\vec{S} \\rangle = 2\\vec{E}_0 \\times \\vec{H}_0$ (under steady-state operating conditions)",
          "$\\langle \\vec{S} \\rangle = \\frac{E_0^2}{\\eta^2}$ (as determined by Maxwell boundary constraints)",
          "$\\langle \\vec{S} \\rangle = \\frac{1}{2}\\operatorname{Re}(\\vec{E} \\times \\vec{H}^*)$"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "The time average of the cross product of two sinusoidal vector fields is $\\langle \\vec{S} \\rangle = \\frac{1}{2}\\operatorname{Re}(\\vec{E} \\times \\vec{H}^*)$."
          ],
          "keyConcept": "The time average of the cross product of two sinusoidal vector fields is $\\langle \\vec{S} \\rangle = \\frac{1}{2}\\operator..."
        }
      },
      {
        "id": 6,
        "question": "The wave equation for electric field $\\vec{E}$ in a charge-free, non-conducting medium is:",
        "options": [
          "$\\nabla^2 \\vec{E} = \\mu \\sigma \\frac{\\partial \\vec{E}}{\\partial t}$",
          "$\\nabla \\times \\vec{E} = \\mu \\epsilon \\vec{E}$ (as determined by Maxwell boundary constraints)",
          "$\\nabla^2 \\vec{E} = \\mu \\epsilon \\frac{\\partial^2 \\vec{E}}{\\partial t^2}$",
          "$\\nabla^2 \\vec{E} = 0$ (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Combining Maxwell's curl equations in source-free lossless media yields the 3D wave equation $\\nabla^2 \\vec{E} = \\mu\\epsilon \\frac{\\partial^2\\vec{E}}{\\partial t^2}$."
          ],
          "keyConcept": "Combining Maxwell's curl equations in source-free lossless media yields the 3D wave equation $\\nabla^2 \\vec{E} = \\mu\\eps..."
        }
      },
      {
        "id": 7,
        "question": "If $\\vec{E}(z,t) = E_0 \\cos(\\omega t - kz)\\hat{i}$, the corresponding magnetic field $\\vec{H}(z,t)$ in free space is:",
        "options": [
          "$\\frac{E_0}{\\eta_0}\\cos(\\omega t - kz)\\hat{k}$",
          "$-\\frac{E_0}{\\eta_0}\\sin(\\omega t - kz)\\hat{j}$",
          "$\\frac{E_0}{\\eta_0}\\cos(\\omega t - kz)\\hat{j}$",
          "$\\eta_0 E_0 \\cos(\\omega t - kz)\\hat{j}$"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Since $\\vec{S} \\parallel \\hat{k}$, $\\hat{i} \\times \\hat{j} = \\hat{k}$, and $H_0 = E_0/\\eta_0$ with zero phase difference in lossless space."
          ],
          "keyConcept": "Since $\\vec{S} \\parallel \\hat{k}$, $\\hat{i} \\times \\hat{j} = \\hat{k}$, and $H_0 = E_0/\\eta_0$ with zero phase difference..."
        }
      },
      {
        "id": 8,
        "question": "The electric and magnetic energy densities in a free-space plane electromagnetic wave are related by:",
        "options": [
          "$u_e < u_m$ (across all standard operating temperatures)",
          "$u_e = u_m$ (Equipartition of energy)",
          "$u_e = 0$ (independent of external field perturbations)",
          "$u_e > u_m$ (in an ideal homogeneous medium)"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Because $B_0 = E_0/c$ and $c^2 = 1/(\\mu_0\\epsilon_0)$, $u_m = \\frac{B_0^2}{2\\mu_0} = \\frac{E_0^2}{2\\mu_0 c^2} = \\frac{1}{2}\\epsilon_0 E_0^2 = u_e$."
          ],
          "keyConcept": "Because $B_0 = E_0/c$ and $c^2 = 1/(\\mu_0\\epsilon_0)$, $u_m = \\frac{B_0^2}{2\\mu_0} = \\frac{E_0^2}{2\\mu_0 c^2} = \\frac{1}..."
        }
      },
      {
        "id": 9,
        "question": "Displacement current has dimensions identical to:",
        "options": [
          "Magnetic flux",
          "Electric charge density",
          "Electric current",
          "Electric field"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Displacement current $I_d = \\iint \\vec{J}_d \\cdot d\\vec{S}$ has the SI unit of Amperes ($\\text{A}$), identical to conduction current."
          ],
          "keyConcept": "Displacement current $I_d = \\iint \\vec{J}_d \\cdot d\\vec{S}$ has the SI unit of Amperes ($\\text{A}$), identical to conduc..."
        }
      },
      {
        "id": 10,
        "question": "In a circular parallel-plate capacitor of radius $R$ being charged with current $I$, the displacement current density $J_d$ is:",
        "options": [
          "$J_d = \\frac{I R^2}{\\pi}$",
          "$J_d = \\frac{I}{2\\pi R}$",
          "$J_d = 0$",
          "$J_d = \\frac{I}{\\pi R^2}$"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Uniform electric field growth produces uniform displacement current density equal to total charging current divided by area $\\pi R^2$."
          ],
          "keyConcept": "Uniform electric field growth produces uniform displacement current density equal to total charging current divided by a..."
        }
      },
      {
        "id": 11,
        "question": "The spatial divergence angle $\\theta$ of a diffraction-limited laser beam of wavelength $\\lambda$ and aperture diameter $D$ is proportional to:",
        "options": [
          "$\\theta \\propto \\lambda D$",
          "$\\theta \\propto \\frac{D}{\\lambda}$",
          "$\\theta \\propto \\frac{1}{\\lambda D}$",
          "$\\theta \\propto \\frac{\\lambda}{D}$"
        ],
        "correctIndex": 3,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "By Fraunhofer diffraction, the beam angular divergence is $\\theta \\approx 1.22 \\lambda / D$, which is extremely small for lasers."
          ],
          "keyConcept": "By Fraunhofer diffraction, the beam angular divergence is $\\theta \\approx 1.22 \\lambda / D$, which is extremely small fo..."
        }
      },
      {
        "id": 12,
        "question": "Holography was invented by Dennis Gabor and is fundamentally a technique for:",
        "options": [
          "Recording 2D intensity distributions only (under steady-state operating conditions)",
          "Measuring electrical conductivity of solids (as determined by Maxwell boundary constraints)",
          "Recording and reconstructing both the amplitude and phase of an optical wavefront (full 3D image)",
          "Thermal imaging in the dark (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Holography records the complete optical wavefront (both amplitude and phase) through interference and reconstructs it via diffraction."
          ],
          "keyConcept": "Holography records the complete optical wavefront (both amplitude and phase) through interference and reconstructs it vi..."
        }
      },
      {
        "id": 13,
        "question": "In the recording of a hologram, the photographic film records the interference pattern produced between:",
        "options": [
          "Two incoherent white light bulbs (as determined by Maxwell boundary constraints)",
          "The scattered object beam and a coherent reference beam from the same laser source",
          "The transmitted beam and a radio wave (governed by linear superposition principles)",
          "An electron beam and an X-ray beam (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Interference between the scattered light from the 3D object and an unscattered reference beam forms the microscopic holographic fringes."
          ],
          "keyConcept": "Interference between the scattered light from the 3D object and an unscattered reference beam forms the microscopic holo..."
        }
      },
      {
        "id": 14,
        "question": "When a recorded transmission hologram is illuminated by the original reference laser beam, the reconstructed wavefront forms:",
        "options": [
          "A virtual 3D image behind the plate and a real 3D image in front of the plate",
          "A single black-and-white shadow (governed by linear superposition principles)",
          "Only a 2D flat photograph (independent of external field perturbations)",
          "A rainbow spectrum of colors (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Diffraction of the reading beam creates a 3D virtual image (viewed by looking through the plate) and a conjugate real image."
          ],
          "keyConcept": "Diffraction of the reading beam creates a 3D virtual image (viewed by looking through the plate) and a conjugate real im..."
        }
      },
      {
        "id": 15,
        "question": "Which key feature fundamentally distinguishes holography from conventional photography?",
        "options": [
          "Photography uses no lenses (governed by linear superposition principles)",
          "Photography requires coherent laser light; holography requires sunlight (independent of external field perturbations)",
          "Photography records both amplitude and phase; holography records only intensity (in an ideal homogeneous medium)",
          "Photography records 2D intensity only; holography records both amplitude and phase information to preserve true 3D depth and parallax"
        ],
        "correctIndex": 3,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Conventional photos capture only 2D intensity ($I \\propto |E|^2$), discarding phase; holograms encode phase via interferometry."
          ],
          "keyConcept": "Conventional photos capture only 2D intensity ($I \\propto |E|^2$), discarding phase; holograms encode phase via interfer..."
        }
      },
      {
        "id": 16,
        "question": "The Q-switching technique in lasers is used to generate:",
        "options": [
          "Multiple laser beams of different colors (independent of external field perturbations)",
          "Low-power continuous wave light (in an ideal homogeneous medium)",
          "Ultra-short laser pulses with exceptionally high peak power (megawatts to gigawatts)",
          "Zero electromagnetic output (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 2,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Q-switching spoils the cavity quality factor $Q$ to store huge population inversion, then rapidly restores $Q$ to release a giant pulse."
          ],
          "keyConcept": "Q-switching spoils the cavity quality factor $Q$ to store huge population inversion, then rapidly restores $Q$ to releas..."
        }
      },
      {
        "id": 17,
        "question": "Mode-locking in lasers produces periodic trains of ultra-short pulses in the time domain with durations on the order of:",
        "options": [
          "Seconds to milliseconds (in an ideal homogeneous medium)",
          "Minutes (under steady-state operating conditions)",
          "Picoseconds to femtoseconds ($10^{-12}\\text{ s}$ to $10^{-15}\\text{ s}$)",
          "Microseconds (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Mode-locking locks the phases of all longitudinal cavity modes, producing femtosecond/picosecond pulse trains."
          ],
          "keyConcept": "Mode-locking locks the phases of all longitudinal cavity modes, producing femtosecond/picosecond pulse trains."
        }
      },
      {
        "id": 18,
        "question": "In eye surgery (LASIK), which type of laser is used for precision corneal reshaping due to its non-thermal photoablation in the UV spectrum?",
        "options": [
          "Excimer laser (e.g., ArF at $193\\text{ nm}$)",
          "$\\text{CO}_2$ laser (as determined by Maxwell boundary constraints)",
          "Ruby laser (across all standard operating temperatures)",
          "He-Ne laser (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Argon Fluoride (ArF) excimer lasers ($193\\text{ nm}$ UV) break molecular bonds with sub-micron precision without thermal tissue damage."
          ],
          "keyConcept": "Argon Fluoride (ArF) excimer lasers ($193\\text{ nm}$ UV) break molecular bonds with sub-micron precision without thermal..."
        }
      },
      {
        "id": 19,
        "question": "The threshold gain coefficient $g_{\\text{th}}$ for laser oscillation in a cavity of length $L$ with mirror reflectivities $R_1, R_2$ and distributed loss $\\alpha_s$ is:",
        "options": [
          "$g_{\\text{th}} = \\alpha_s + 2L\\ln(R_1 R_2)$ (as determined by Maxwell boundary constraints)",
          "$g_{\\text{th}} = \\alpha_s + \\frac{1}{2L}\\ln\\left(\\frac{1}{R_1 R_2}\\right)$",
          "$g_{\\text{th}} = \\frac{\\alpha_s}{2L}\\ln(R_1 R_2)$ (governed by linear superposition principles)",
          "$g_{\\text{th}} = \\alpha_s - \\frac{1}{L}\\ln(R_1 R_2)$ (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Round-trip loop gain condition $R_1 R_2 e^{2(g_{\\text{th}} - \\alpha_s)L} = 1 \\implies g_{\\text{th}} = \\alpha_s + \\frac{1}{2L}\\ln(1/(R_1 R_2))$."
          ],
          "keyConcept": "Round-trip loop gain condition $R_1 R_2 e^{2(g_{\\text{th}} - \\alpha_s)L} = 1 \\implies g_{\\text{th}} = \\alpha_s + \\frac{1..."
        }
      },
      {
        "id": 20,
        "question": "In a He-Ne laser, the discharge tube is often fitted with Brewster angle windows at its ends to ensure that the output beam is:",
        "options": [
          "$100\\%$ linearly polarized with zero reflection losses for p-polarized light",
          "Completely unpolarized (governed by linear superposition principles)",
          "Circularly polarized (independent of external field perturbations)",
          "Deflected by $90^\\circ$ (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Brewster angle windows transmit p-polarized light with zero reflection loss, resulting in a strictly linearly polarized laser beam."
          ],
          "keyConcept": "Brewster angle windows transmit p-polarized light with zero reflection loss, resulting in a strictly linearly polarized ..."
        }
      },
      {
        "id": 21,
        "question": "Microbending losses are caused by:",
        "options": [
          "Large loops of fiber coils (governed by linear superposition principles)",
          "Total internal reflection (independent of external field perturbations)",
          "Photodiode dark current (in an ideal homogeneous medium)",
          "Microscopic microscopic axis imperfections, localized pressure, and microscopic crinkles along the fiber core interface"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Random microscopic lateral displacements ($< 1\\,\\mu\\text{m}$) couple energy from guided core modes into lossy radiation cladding modes."
          ],
          "keyConcept": "Random microscopic lateral displacements ($< 1\\,\\mu\\text{m}$) couple energy from guided core modes into lossy radiation ..."
        }
      },
      {
        "id": 22,
        "question": "The maximum bit-rate capacity $B$ of an optical communication link limited by pulse broadening $\\Delta \\tau$ is approximately:",
        "options": [
          "$B \\approx 2\\Delta\\tau$ (independent of external field perturbations)",
          "$B \\approx \\frac{c}{\\Delta\\tau}$ (in an ideal homogeneous medium)",
          "$B \\approx \\Delta\\tau^2$ (under steady-state operating conditions)",
          "$B \\approx \\frac{1}{2\\Delta\\tau}$ (or $\\frac{1}{4\\sigma_\\tau}$)"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "To avoid inter-symbol interference (ISI) between adjacent pulses, bit period $T_b \\ge 2\\Delta\\tau \\implies B = 1/T_b \\le 1/(2\\Delta\\tau)$."
          ],
          "keyConcept": "To avoid inter-symbol interference (ISI) between adjacent pulses, bit period $T_b \\ge 2\\Delta\\tau \\implies B = 1/T_b \\le..."
        }
      },
      {
        "id": 23,
        "question": "An Erbium-Doped Fiber Amplifier (EDFA) provides direct optical amplification without electronic conversion in which telecommunication band?",
        "options": [
          "Microwave spectrum ($1\\text{--}10\\text{ GHz}$) (in an ideal homogeneous medium)",
          "C-band ($1530\\text{--}1565\\text{ nm}$) and L-band ($1565\\text{--}1625\\text{ nm}$)",
          "O-band ($1260\\text{--}1360\\text{ nm}$) (as determined by Maxwell boundary constraints)",
          "Visible spectrum ($400\\text{--}700\\text{ nm}$) (across all standard operating temperatures)"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "The $^4I_{13/2} \\to ^4I_{15/2}$ transition in $\\text{Er}^{3+}$ ions provides wide optical gain directly overlapping the $1550\\text{ nm}$ low-loss window."
          ],
          "keyConcept": "The $^4I_{13/2} \\to ^4I_{15/2}$ transition in $\\text{Er}^{3+}$ ions provides wide optical gain directly overlapping the ..."
        }
      },
      {
        "id": 24,
        "question": "Which optical source is preferred for long-haul, ultra-high-speed ($> 10\\text{ Gbps}$) fiber optic communication systems?",
        "options": [
          "Distributed Feedback (DFB) Semiconductor Laser Diode",
          "Tungsten halogen bulb (as determined by Maxwell boundary constraints)",
          "Neon indicator lamp (across all standard operating temperatures)",
          "Surface-emitting LED (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "DFB laser diodes provide single-longitudinal-mode emission with extremely narrow linewidth ($\\Delta\\lambda < 0.1\\text{ nm}$), minimizing chromatic dispersion."
          ],
          "keyConcept": "DFB laser diodes provide single-longitudinal-mode emission with extremely narrow linewidth ($\\Delta\\lambda < 0.1\\text{ n..."
        }
      },
      {
        "id": 25,
        "question": "An Avalanche Photodiode (APD) offers higher sensitivity than a PIN photodiode because:",
        "options": [
          "It has zero dark current (as determined by Maxwell boundary constraints)",
          "It exhibits internal current multiplication gain through impact ionization",
          "It generates photons rather than electrons (governed by linear superposition principles)",
          "It requires no bias voltage (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "High reverse bias accelerates photo-generated carriers to create secondary electron-hole pairs via impact ionization, providing internal gain ($M \\sim 10\\text{--}100$)."
          ],
          "keyConcept": "High reverse bias accelerates photo-generated carriers to create secondary electron-hole pairs via impact ionization, pr..."
        }
      },
      {
        "id": 26,
        "question": "In fiber optics, fusion splicing involves:",
        "options": [
          "Joining two cleaved fiber ends using an electric arc to melt and fuse the glass permanently",
          "Gluing fibers with epoxy resin (governed by linear superposition principles)",
          "Taping fibers with electrical tape (independent of external field perturbations)",
          "Twisting the glass cores together (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Fusion splicers align fiber cores with sub-micron precision and fuse them using an electric arc, achieving insertion loss $< 0.02\\text{ dB}$."
          ],
          "keyConcept": "Fusion splicers align fiber cores with sub-micron precision and fuse them using an electric arc, achieving insertion los..."
        }
      },
      {
        "id": 27,
        "question": "Fiber Bragg Grating (FBG) sensors operate on the principle of reflecting a specific narrow wavelength $\\lambda_B$ given by:",
        "options": [
          "$\\lambda_B = 2 n_{\\text{eff}} \\Lambda$",
          "$\\lambda_B = \\frac{n_{\\text{eff}}}{2\\Lambda}$",
          "$\\lambda_B = n_{\\text{eff}} \\Lambda^2$",
          "$\\lambda_B = \\frac{2\\Lambda}{n_{\\text{eff}}}$"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "The Bragg resonance condition reflects wavelength $\\lambda_B = 2 n_{\\text{eff}} \\Lambda$, where $\\Lambda$ is grating period and $n_{\\text{eff}}$ is effective index."
          ],
          "keyConcept": "The Bragg resonance condition reflects wavelength $\\lambda_B = 2 n_{\\text{eff}} \\Lambda$, where $\\Lambda$ is grating per..."
        }
      },
      {
        "id": 28,
        "question": "When an FBG sensor is subjected to mechanical strain $\\epsilon$ or temperature change $\\Delta T$, its reflected Bragg wavelength $\\lambda_B$:",
        "options": [
          "Disappears completely (independent of external field perturbations)",
          "Remains completely unchanged (in an ideal homogeneous medium)",
          "Doubles in amplitude with zero wavelength shift (under steady-state operating conditions)",
          "Shifts linearly ($\\Delta\\lambda_B / \\lambda_B = P_e \\epsilon + \\alpha_T \\Delta T$)"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Mechanical elongation changes period $\\Lambda$ and photoelastic index; temperature changes index via thermo-optic effect, shifting $\\lambda_B$."
          ],
          "keyConcept": "Mechanical elongation changes period $\\Lambda$ and photoelastic index; temperature changes index via thermo-optic effect..."
        }
      },
      {
        "id": 29,
        "question": "A typical Single-Mode Fiber (SMF-28) has a core diameter and cladding diameter of:",
        "options": [
          "$50\\,\\mu\\text{m}$ core and $125\\,\\mu\\text{m}$ cladding",
          "$62.5\\,\\mu\\text{m}$ core and $125\\,\\mu\\text{m}$ cladding",
          "$200\\,\\mu\\text{m}$ core and $500\\,\\mu\\text{m}$ cladding",
          "$9\\,\\mu\\text{m}$ core and $125\\,\\mu\\text{m}$ cladding"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Standard telecom single-mode fiber (G.652) features a nominal core diameter of $8.2\\text{--}9.0\\,\\mu\\text{m}$ and cladding diameter of $125\\,\\mu\\text{m}$."
          ],
          "keyConcept": "Standard telecom single-mode fiber (G.652) features a nominal core diameter of $8.2\\text{--}9.0\\,\\mu\\text{m}$ and claddi..."
        }
      },
      {
        "id": 30,
        "question": "A step-index fiber has core index $n_1 = 1.50$ and cladding index $n_2 = 1.45$. The critical angle $\\phi_c$ is:",
        "options": [
          "$45.0^\\circ$",
          "$75.2^\\circ$",
          "$85.0^\\circ$",
          "$60.0^\\circ$"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "$\\phi_c = \\arcsin(1.45/1.50) = \\arcsin(0.9667) \\approx 75.16^\\circ$."
          ],
          "keyConcept": "$\\phi_c = \\arcsin(1.45/1.50) = \\arcsin(0.9667) \\approx 75.16^\\circ$."
        }
      }
    ]
  },
  {
    "id": "phy110-midterm-paper-5",
    "code": "PHY110-PAPER-E",
    "title": "Midterm Examination • Paper 5 (Fiber Optics & Total Internal Reflection)",
    "courseCode": "PHY110",
    "courseName": "Engineering Physics",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Vector Calculus",
      "Maxwell Equations",
      "Lasers",
      "Fiber Optics"
    ],
    "description": "Comprehensive problem set on acceptance cone, numerical aperture, step vs graded index dispersion, and optical attenuation.",
    "questions": [
      {
        "id": 1,
        "question": "The magnetic field induced inside the capacitor plates at distance $r \\le R$ from the central axis is:",
        "options": [
          "$B(r) = \\frac{\\mu_0 I}{2\\pi r}$",
          "$B(r) = \\frac{\\mu_0 I R}{2\\pi r^2}$",
          "$B(r) = \\frac{\\mu_0 I r}{2\\pi R^2}$",
          "$B(r) = 0$"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Applying Ampere-Maxwell law to a loop of radius $r$: $B(2\\pi r) = \\mu_0 I_d(r) = \\mu_0 I (r^2/R^2) \\implies B = \\frac{\\mu_0 I r}{2\\pi R^2}$."
          ],
          "keyConcept": "Applying Ampere-Maxwell law to a loop of radius $r$: $B(2\\pi r) = \\mu_0 I_d(r) = \\mu_0 I (r^2/R^2) \\implies B = \\frac{\\m..."
        }
      },
      {
        "id": 2,
        "question": "The concept of magnetic vector potential $\\vec{A}$ arises directly from the mathematical relation:",
        "options": [
          "$\\nabla \\cdot \\vec{D} = \\rho$ (across all standard operating temperatures)",
          "$\\nabla \\cdot \\vec{B} = 0 \\implies \\vec{B} = \\nabla \\times \\vec{A}$",
          "$\\nabla \\cdot \\vec{J} = -\\partial\\rho/\\partial t$ (independent of external field perturbations)",
          "$\\nabla \\times \\vec{E} = 0 \\implies \\vec{E} = -\\nabla V$"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Because any solenoidal vector field can be expressed as the curl of another vector field, $\\nabla \\cdot \\vec{B} = 0 \\implies \\vec{B} = \\nabla \\times \\vec{A}$."
          ],
          "keyConcept": "Because any solenoidal vector field can be expressed as the curl of another vector field, $\\nabla \\cdot \\vec{B} = 0 \\imp..."
        }
      },
      {
        "id": 3,
        "question": "Under the Coulomb gauge condition, the vector potential $\\vec{A}$ satisfies:",
        "options": [
          "$\\nabla \\cdot \\vec{A} = -\\mu\\epsilon \\frac{\\partial V}{\\partial t}$",
          "$\\vec{A} = \\vec{0}$",
          "$\\nabla \\times \\vec{A} = 0$",
          "$\\nabla \\cdot \\vec{A} = 0$"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "The Coulomb gauge condition is explicitly defined by setting the divergence of vector potential to zero: $\\nabla \\cdot \\vec{A} = 0$."
          ],
          "keyConcept": "The Coulomb gauge condition is explicitly defined by setting the divergence of vector potential to zero: $\\nabla \\cdot \\..."
        }
      },
      {
        "id": 4,
        "question": "Under the Lorenz gauge condition, the potentials $\\vec{A}$ and $V$ satisfy:",
        "options": [
          "$\\nabla \\cdot \\vec{A} + \\mu\\epsilon \\frac{\\partial V}{\\partial t} = 0$",
          "$\\nabla \\times \\vec{A} + \\vec{E} = 0$ (in an ideal homogeneous medium)",
          "$\\nabla V = 0$ (under steady-state operating conditions)",
          "$\\nabla \\cdot \\vec{A} = 0$ (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "The Lorenz gauge $\\nabla \\cdot \\vec{A} + \\frac{1}{c^2}\\frac{\\partial V}{\\partial t} = 0$ decouples the wave equations for $V$ and $\\vec{A}$."
          ],
          "keyConcept": "The Lorenz gauge $\\nabla \\cdot \\vec{A} + \\frac{1}{c^2}\\frac{\\partial V}{\\partial t} = 0$ decouples the wave equations fo..."
        }
      },
      {
        "id": 5,
        "question": "The radiation resistance of an infinitesimal Hertzian dipole of length $dl \\ll \\lambda$ is proportional to:",
        "options": [
          "$(\\lambda/dl)^2$",
          "$(dl/\\lambda)^4$",
          "$(dl/\\lambda)^2$",
          "$(dl/\\lambda)$"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "The radiation resistance of a short dipole antenna is $R_{\\text{rad}} = 80\\pi^2 (dl/\\lambda)^2\\,\\Omega$."
          ],
          "keyConcept": "The radiation resistance of a short dipole antenna is $R_{\\text{rad}} = 80\\pi^2 (dl/\\lambda)^2\\,\\Omega$."
        }
      },
      {
        "id": 6,
        "question": "Which of the following Maxwell equations represents the fact that electric field lines originate and terminate on electric charges?",
        "options": [
          "$\\nabla \\cdot \\vec{D} = \\rho_v$",
          "$\\nabla \\times \\vec{H} = \\vec{J} + \\frac{\\partial \\vec{D}}{\\partial t}$",
          "$\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$",
          "$\\nabla \\cdot \\vec{B} = 0$"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Gauss's law $\\nabla \\cdot \\vec{D} = \\rho_v$ states that spatial divergence of electric displacement equals free charge density."
          ],
          "keyConcept": "Gauss's law $\\nabla \\cdot \\vec{D} = \\rho_v$ states that spatial divergence of electric displacement equals free charge d..."
        }
      },
      {
        "id": 7,
        "question": "The attenuation constant $\\alpha$ for an electromagnetic wave propagating in a good conductor is given by:",
        "options": [
          "$\\alpha = 0$",
          "$\\alpha = \\omega \\sqrt{\\mu \\epsilon}$",
          "$\\alpha = \\frac{\\sigma}{2}\\sqrt{\\frac{\\mu}{\\epsilon}}$",
          "$\\alpha = \\sqrt{\\frac{\\omega \\mu \\sigma}{2}}$"
        ],
        "correctIndex": 3,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "For a good conductor ($\\sigma \\gg \\omega\\epsilon$), the propagation constant is $\\gamma = \\sqrt{i\\omega\\mu\\sigma} = (1+i)\\sqrt{\\omega\\mu\\sigma/2}$, so $\\alpha = \\sqrt{\\omega\\mu\\sigma/2}$."
          ],
          "keyConcept": "For a good conductor ($\\sigma \\gg \\omega\\epsilon$), the propagation constant is $\\gamma = \\sqrt{i\\omega\\mu\\sigma} = (1+i..."
        }
      },
      {
        "id": 8,
        "question": "The phase velocity $v_p$ of an electromagnetic wave in a good conductor is:",
        "options": [
          "$v_p = \\sqrt{\\frac{2\\omega}{\\mu \\sigma}} = \\omega \\delta$",
          "$v_p = c$ (governed by linear superposition principles)",
          "$v_p = \\infty$ (independent of external field perturbations)",
          "$v_p = \\frac{1}{\\sqrt{\\mu\\epsilon}}$ (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "In a conductor, $v_p = \\omega/\\beta = \\omega/\\sqrt{\\omega\\mu\\sigma/2} = \\sqrt{2\\omega/(\\mu\\sigma)} = \\omega \\delta$, which is much slower than $c$."
          ],
          "keyConcept": "In a conductor, $v_p = \\omega/\\beta = \\omega/\\sqrt{\\omega\\mu\\sigma/2} = \\sqrt{2\\omega/(\\mu\\sigma)} = \\omega \\delta$, whi..."
        }
      },
      {
        "id": 9,
        "question": "The refractive index $n$ of a non-magnetic lossless medium ($\\mu_r = 1$) is related to its relative permittivity $\\epsilon_r$ by:",
        "options": [
          "$n = \\epsilon_r$",
          "$n = \\sqrt{\\epsilon_r}$",
          "$n = 1/\\sqrt{\\epsilon_r}$",
          "$n = \\epsilon_r^2$"
        ],
        "correctIndex": 1,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Maxwell's relation establishes that $n = c/v = \\sqrt{\\mu_r \\epsilon_r} = \\sqrt{\\epsilon_r}$ for non-magnetic substances."
          ],
          "keyConcept": "Maxwell's relation establishes that $n = c/v = \\sqrt{\\mu_r \\epsilon_r} = \\sqrt{\\epsilon_r}$ for non-magnetic substances."
        }
      },
      {
        "id": 10,
        "question": "When an electromagnetic wave travels from air into a dielectric medium of refractive index $n=1.5$, its wavelength $\\lambda$:",
        "options": [
          "Becomes zero",
          "Remains unchanged",
          "Decreases to $\\lambda/1.5$",
          "Increases by $1.5$ times"
        ],
        "correctIndex": 2,
        "topic": "Vector Calculus & Maxwell",
        "explanation": {
          "steps": [
            "Wave frequency $f$ remains constant across interfaces, so $\\lambda_{\\text{med}} = v/f = c/(n f) = \\lambda_0 / n$."
          ],
          "keyConcept": "Wave frequency $f$ remains constant across interfaces, so $\\lambda_{\\text{med}} = v/f = c/(n f) = \\lambda_0 / n$."
        }
      },
      {
        "id": 11,
        "question": "What type of laser transition occurs in the Semiconductor Diode Laser?",
        "options": [
          "Interband transitions of electrons from conduction band to valence band",
          "Electronic transitions between localized discrete ionic states",
          "Rotational transitions of diatomic molecules (as determined by Maxwell boundary constraints)",
          "Vibrational transitions of symmetric stretch modes (across all standard operating temperatures)"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Recombination of conduction band electrons with valence band holes across the direct bandgap produces photon emission."
          ],
          "keyConcept": "Recombination of conduction band electrons with valence band holes across the direct bandgap produces photon emission."
        }
      },
      {
        "id": 12,
        "question": "The active lasing ion in the Nd:YAG laser is:",
        "options": [
          "$\\text{Al}^{3+}$ (under steady-state operating conditions)",
          "$\\text{Y}^{3+}$ (as determined by Maxwell boundary constraints)",
          "$\\text{Nd}^{3+}$ (Neodymium ion)",
          "$\\text{Cr}^{3+}$ (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Neodymium ions ($\\text{Nd}^{3+}$) substitute for Yttrium ($\\text{Y}^{3+}$) ions in the host YAG crystal and undergo 4-level lasing transitions."
          ],
          "keyConcept": "Neodymium ions ($\\text{Nd}^{3+}$) substitute for Yttrium ($\\text{Y}^{3+}$) ions in the host YAG crystal and undergo 4-le..."
        }
      },
      {
        "id": 13,
        "question": "The beam waist $w_0$ of a Gaussian laser beam represents:",
        "options": [
          "The mirror spacing in the laser head (as determined by Maxwell boundary constraints)",
          "The distance where power drops to zero (across all standard operating temperatures)",
          "The position where beam diameter is maximum (governed by linear superposition principles)",
          "The focal region where beam radius shrinks to its absolute minimum"
        ],
        "correctIndex": 3,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Beam waist $w_0$ is the location of minimum spot size along the propagation axis of a Gaussian laser beam."
          ],
          "keyConcept": "Beam waist $w_0$ is the location of minimum spot size along the propagation axis of a Gaussian laser beam."
        }
      },
      {
        "id": 14,
        "question": "The Rayleigh range $z_R$ of a Gaussian beam with beam waist $w_0$ is given by:",
        "options": [
          "$z_R = \\frac{\\lambda}{\\pi w_0^2}$",
          "$z_R = \\frac{2\\lambda}{w_0}$",
          "$z_R = \\pi w_0 \\lambda$",
          "$z_R = \\frac{\\pi w_0^2}{\\lambda}$"
        ],
        "correctIndex": 3,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "The Rayleigh range $z_R = \\pi w_0^2/\\lambda$ is the distance over which the beam cross-sectional area doubles."
          ],
          "keyConcept": "The Rayleigh range $z_R = \\pi w_0^2/\\lambda$ is the distance over which the beam cross-sectional area doubles."
        }
      },
      {
        "id": 15,
        "question": "Which industrial process uses high-power $\\text{CO}_2$ or fiber lasers for slicing thick steel plates?",
        "options": [
          "Laser cutting and welding",
          "Laser ablation",
          "Laser annealing",
          "Photolithography"
        ],
        "correctIndex": 0,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "High-power $\\text{CO}_2$ and fiber lasers provide focused multikilowatt thermal power for precision industrial metal cutting and welding."
          ],
          "keyConcept": "High-power $\\text{CO}_2$ and fiber lasers provide focused multikilowatt thermal power for precision industrial metal cut..."
        }
      },
      {
        "id": 16,
        "question": "A Helium-Neon laser has a coherence time $\\tau_c = 10^{-8}\\text{ s}$. Its coherence length $L_c$ is:",
        "options": [
          "$300\\text{ m}$",
          "$3.0\\text{ m}$",
          "$30\\text{ m}$",
          "$0.3\\text{ m}$"
        ],
        "correctIndex": 1,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "$L_c = c \\tau_c = (3 \\times 10^8\\text{ m/s})(10^{-8}\\text{ s}) = 3.0\\text{ m}$."
          ],
          "keyConcept": "$L_c = c \\tau_c = (3 \\times 10^8\\text{ m/s})(10^{-8}\\text{ s}) = 3.0\\text{ m}$."
        }
      },
      {
        "id": 17,
        "question": "If a laser has an emission linewidth $\\Delta \\lambda = 0.002\\text{ nm}$ at central wavelength $\\lambda = 500\\text{ nm}$, its coherence length $L_c$ is:",
        "options": [
          "$12.5\\text{ m}$",
          "$1.25\\text{ cm}$",
          "$12.5\\text{ cm}$",
          "$1.25\\text{ m}$"
        ],
        "correctIndex": 2,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "$L_c \\approx \\frac{\\lambda^2}{\\Delta\\lambda} = \\frac{(500 \\times 10^{-9})^2}{0.002 \\times 10^{-9}} = \\frac{2.5 \\times 10^{-13}}{2 \\times 10^{-12}} = 0.125\\text{ m} = 12.5\\text{ cm}$."
          ],
          "keyConcept": "$L_c \\approx \\frac{\\lambda^2}{\\Delta\\lambda} = \\frac{(500 \\times 10^{-9})^2}{0.002 \\times 10^{-9}} = \\frac{2.5 \\times 10..."
        }
      },
      {
        "id": 18,
        "question": "A laser resonator has a mirror cavity length $L = 30\\text{ cm}$. The longitudinal mode spacing $\\Delta \\nu$ is:",
        "options": [
          "$1000\\text{ MHz}$ ($1\\text{ GHz}$)",
          "$1500\\text{ MHz}$",
          "$250\\text{ MHz}$",
          "$500\\text{ MHz}$"
        ],
        "correctIndex": 3,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "$\\Delta \\nu = \\frac{c}{2L} = \\frac{3 \\times 10^8}{2 \\times 0.30} = \\frac{3 \\times 10^8}{0.60} = 5 \\times 10^8\\text{ Hz} = 500\\text{ MHz}$."
          ],
          "keyConcept": "$\\Delta \\nu = \\frac{c}{2L} = \\frac{3 \\times 10^8}{2 \\times 0.30} = \\frac{3 \\times 10^8}{0.60} = 5 \\times 10^8\\text{ Hz} ..."
        }
      },
      {
        "id": 19,
        "question": "In a He-Ne laser, the transition that produces the $632.8\\text{ nm}$ red laser line occurs between which energy levels of Neon?",
        "options": [
          "$2s \\to 2p$",
          "$3s_2 \\to 2p_4$",
          "$1s \\to 2s$",
          "$3p \\to 3s$"
        ],
        "correctIndex": 1,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "The famous $632.8\\text{ nm}$ line corresponds specifically to the $3s_2 \\to 2p_4$ transition in the Paschen notation for Neon."
          ],
          "keyConcept": "The famous $632.8\\text{ nm}$ line corresponds specifically to the $3s_2 \\to 2p_4$ transition in the Paschen notation for..."
        }
      },
      {
        "id": 20,
        "question": "Why is the laser beam highly monochromatic compared to emission from a regular discharge lamp?",
        "options": [
          "Because all other colors are absorbed by the glass walls (across all standard operating temperatures)",
          "Because stimulated emission selectively amplifies only cavity-resonant frequencies within the narrow atomic gain profile",
          "Because the laser uses a color filter (independent of external field perturbations)",
          "Because atoms only possess one single quantum energy level (in an ideal homogeneous medium)"
        ],
        "correctIndex": 1,
        "topic": "Lasers & Holography",
        "explanation": {
          "steps": [
            "Repeated passes through the resonant cavity provide selective gain strictly to resonant standing-wave frequencies, narrowing the spectral linewidth."
          ],
          "keyConcept": "Repeated passes through the resonant cavity provide selective gain strictly to resonant standing-wave frequencies, narro..."
        }
      },
      {
        "id": 21,
        "question": "For the fiber in Question 40, the Numerical Aperture ($\\text{NA}$) in air is:",
        "options": [
          "$0.384$",
          "$0.150$",
          "$0.707$",
          "$0.500$"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "$\\text{NA} = \\sqrt{n_1^2 - n_2^2} = \\sqrt{(1.50)^2 - (1.45)^2} = \\sqrt{2.25 - 2.1025} = \\sqrt{0.1475} \\approx 0.384$."
          ],
          "keyConcept": "$\\text{NA} = \\sqrt{n_1^2 - n_2^2} = \\sqrt{(1.50)^2 - (1.45)^2} = \\sqrt{2.25 - 2.1025} = \\sqrt{0.1475} \\approx 0.384$."
        }
      },
      {
        "id": 22,
        "question": "For the fiber in Question 40, the Acceptance Angle $\\theta_a$ in air is:",
        "options": [
          "$12.5^\\circ$",
          "$22.6^\\circ$",
          "$30.0^\\circ$",
          "$45.0^\\circ$"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "$\\theta_a = \\arcsin(\\text{NA}) = \\arcsin(0.384) \\approx 22.58^\\circ$."
          ],
          "keyConcept": "$\\theta_a = \\arcsin(\\text{NA}) = \\arcsin(0.384) \\approx 22.58^\\circ$."
        }
      },
      {
        "id": 23,
        "question": "If the fiber in Question 40 is immersed in water ($n_0 = 1.33$), its new acceptance angle $\\theta_a'$ becomes:",
        "options": [
          "$30.2^\\circ$",
          "$8.4^\\circ$",
          "$22.6^\\circ$",
          "$16.8^\\circ$"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "$\\sin\\theta_a' = \\frac{\\text{NA}}{n_0} = \\frac{0.384}{1.33} \\approx 0.2887 \\implies \\theta_a' = \\arcsin(0.2887) \\approx 16.78^\\circ$."
          ],
          "keyConcept": "$\\sin\\theta_a' = \\frac{\\text{NA}}{n_0} = \\frac{0.384}{1.33} \\approx 0.2887 \\implies \\theta_a' = \\arcsin(0.2887) \\approx ..."
        }
      },
      {
        "id": 24,
        "question": "A $10\\text{ km}$ fiber optical link has input power $P_{\\text{in}} = 2.0\\text{ mW}$ and output power $P_{\\text{out}} = 0.2\\text{ mW}$. The attenuation coefficient $\\alpha$ is:",
        "options": [
          "$2.0\\text{ dB/km}$",
          "$0.1\\text{ dB/km}$",
          "$10\\text{ dB/km}$",
          "$1.0\\text{ dB/km}$"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "$\\alpha = \\frac{10}{L}\\log_{10}\\left(\\frac{P_{\\text{in}}}{P_{\\text{out}}}\\right) = \\frac{10}{10}\\log_{10}\\left(\\frac{2.0}{0.2}\\right) = 1.0 \\times \\log_{10}(10) = 1.0\\text{ dB/km}$."
          ],
          "keyConcept": "$\\alpha = \\frac{10}{L}\\log_{10}\\left(\\frac{P_{\\text{in}}}{P_{\\text{out}}}\\right) = \\frac{10}{10}\\log_{10}\\left(\\frac{2.0..."
        }
      },
      {
        "id": 25,
        "question": "If an optical signal of power $10\\text{ mW}$ is launched into a fiber with attenuation $0.3\\text{ dB/km}$, the power remaining after $20\\text{ km}$ is:",
        "options": [
          "$7.5\\text{ mW}$",
          "$5.0\\text{ mW}$",
          "$2.5\\text{ mW}$",
          "$1.0\\text{ mW}$"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Total loss = $0.3\\text{ dB/km} \\times 20\\text{ km} = 6\\text{ dB}$. A $6\\text{ dB}$ loss corresponds to a factor of $4$ reduction ($10^{-0.6} \\approx 0.251$): $P_{\\text{out}} = 10 \\times 0.251 \\approx 2.51\\text{ mW}$."
          ],
          "keyConcept": "Total loss = $0.3\\text{ dB/km} \\times 20\\text{ km} = 6\\text{ dB}$. A $6\\text{ dB}$ loss corresponds to a factor of $4$ r..."
        }
      },
      {
        "id": 26,
        "question": "A step-index fiber has $n_1 = 1.48$ and $\\Delta = 1\\% = 0.01$. The transit time difference per kilometer ($\\Delta\\tau/L$) due to intermodal dispersion is approximately:",
        "options": [
          "$493\\text{ ns/km}$",
          "$0.49\\text{ ns/km}$",
          "$4.93\\text{ ns/km}$",
          "$49.3\\text{ ns/km}$"
        ],
        "correctIndex": 3,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "$\\frac{\\Delta\\tau}{L} \\approx \\frac{n_1 \\Delta}{c} = \\frac{1.48 \\times 0.01}{3 \\times 10^8\\text{ m/s}} = \\frac{0.0148}{3 \\times 10^8} \\approx 4.93 \\times 10^{-11}\\text{ s/m} = 49.3\\text{ ns/km}$."
          ],
          "keyConcept": "$\\frac{\\Delta\\tau}{L} \\approx \\frac{n_1 \\Delta}{c} = \\frac{1.48 \\times 0.01}{3 \\times 10^8\\text{ m/s}} = \\frac{0.0148}{3..."
        }
      },
      {
        "id": 27,
        "question": "For the fiber in Question 46, the maximum bit rate $B$ achievable over a link of $5\\text{ km}$ without equalization is:",
        "options": [
          "$203\\text{ Mbps}$",
          "$2.03\\text{ Gbps}$",
          "$2.03\\text{ Mbps}$",
          "$20.3\\text{ Mbps}$"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Total delay $\\Delta\\tau = 49.3\\text{ ns/km} \\times 5\\text{ km} = 246.5\\text{ ns}$. $B \\approx \\frac{1}{2\\Delta\\tau} = \\frac{1}{2(246.5 \\times 10^{-9}\\text{ s})} \\approx 2.03 \\times 10^6\\text{ bps} = 2.03\\text{ Mbps}$."
          ],
          "keyConcept": "Total delay $\\Delta\\tau = 49.3\\text{ ns/km} \\times 5\\text{ km} = 246.5\\text{ ns}$. $B \\approx \\frac{1}{2\\Delta\\tau} = \\f..."
        }
      },
      {
        "id": 28,
        "question": "Why is the bandwidth of a graded-index (GRIN) fiber roughly $100\\text{ to }1000\\times$ higher than a step-index fiber of identical core size?",
        "options": [
          "Parabolic grading equalizes the group velocities of different spatial modes",
          "GRIN fibers have zero core radius (in an ideal homogeneous medium)",
          "GRIN fibers absorb all higher-order modes (under steady-state operating conditions)",
          "Light travels at twice the speed of light in GRIN cores (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 0,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Modal delay spread in parabolic GRIN fibers scales as $\\Delta^2$ rather than $\\Delta$: $\\Delta\\tau_{\\text{GRIN}} \\approx \\frac{L n_1 \\Delta^2}{2c}$, reducing modal dispersion by up to $1000\\times$."
          ],
          "keyConcept": "Modal delay spread in parabolic GRIN fibers scales as $\\Delta^2$ rather than $\\Delta$: $\\Delta\\tau_{\\text{GRIN}} \\approx..."
        }
      },
      {
        "id": 29,
        "question": "Optical fibers are completely immune to electromagnetic interference (EMI) and radio frequency interference (RFI) because:",
        "options": [
          "They are shielded with heavy lead jackets (in an ideal homogeneous medium)",
          "They are grounded at both ends (under steady-state operating conditions)",
          "They are fabricated entirely from dielectric insulator materials (silica glass) that carry light photons rather than electrical currents",
          "They operate at high DC voltages (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Silica optical fibers are all-dielectric optical channels, carrying no electrical charges and experiencing zero electromagnetic cross-talk."
          ],
          "keyConcept": "Silica optical fibers are all-dielectric optical channels, carrying no electrical charges and experiencing zero electrom..."
        }
      },
      {
        "id": 30,
        "question": "In medical endoscopy, a coherent bundle of optical fibers is used to:",
        "options": [
          "Record brain EEG signals (under steady-state operating conditions)",
          "Transmit clear spatial optical images of internal human organs with high fidelity",
          "Deliver electrical shocks to muscles (across all standard operating temperatures)",
          "Generate high-voltage X-rays (governed by linear superposition principles)"
        ],
        "correctIndex": 1,
        "topic": "Fiber Optics",
        "explanation": {
          "steps": [
            "Coherent fiber bundles maintain exact relative fiber spatial alignment at both ends, faithfully transmitting real-time 2D color images from inside body cavities."
          ],
          "keyConcept": "Coherent fiber bundles maintain exact relative fiber spatial alignment at both ends, faithfully transmitting real-time 2..."
        }
      }
    ]
  }
];
