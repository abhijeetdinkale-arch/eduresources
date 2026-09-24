/**
 * Official PHY110: Engineering Physics Midterm Mock Examination Suite
 * Contains 4 Full-Length 30-Question Tests (120 Questions Total)
 * Modelled on actual University Midterm Examination Papers (Codes: Paper A & Paper B)
 * Focuses strictly on Units 1-3:
 *   Unit 1: Vector Calculus & Electromagnetic Theory / Maxwell's Equations
 *   Unit 2: Lasers & Holography
 *   Unit 3: Fiber Optics
 * Authentic +1 / -0.25 marking scheme and detailed step-by-step solutions.
 */

export const PHY110_MOCK_TESTS = [
  {
    id: 'phy110-midterm-paper-1',
    code: 'PHY110-PAPER-A',
    title: 'Midterm Examination • Paper 1 (Official University PYQ)',
    courseCode: 'PHY110',
    courseName: 'Engineering Physics',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['Vector Calculus', 'Maxwell Equations', 'Lasers', 'Fiber Optics'],
    description: 'Authentic university midterm examination paper testing scalar/vector fields, divergence & Stokes theorems, laser pumping, population inversion, and optical fiber parameters.',
    questions: [
      {
        id: 1,
        question: 'The temperature at any point within or on earth\'s surface at a certain time defines a:',
        options: ['Scalar field', 'Vector field', 'Both scalar and vector field', 'None of these'],
        correctIndex: 0,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'Temperature has magnitude only and does not possess directional dependence.',
            'A physical quantity completely specified by a single real number at every point in space constitutes a scalar field T(x, y, z).'
          ],
          keyConcept: 'Temperature, electric potential, and density are classic examples of scalar fields.'
        }
      },
      {
        id: 2,
        question: 'If there exists a vector V(x, y, z) at each point (x, y, z) of a region R in space, then the field V defined in region R is called a:',
        options: ['Scalar field', 'Vector field', 'Both scalar and vector field', 'None of these'],
        correctIndex: 1,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'When every point in a region of space is associated with both a magnitude and a direction, the field is a vector field.',
            'Examples include gravitational velocity fields, electric field E, and magnetic flux density B.'
          ],
          keyConcept: 'A vector field assigns a vector V = V_x i + V_y j + V_z k to each spatial point.'
        }
      },
      {
        id: 3,
        question: 'A scalar field is defined by φ(x, y, z) = 4x³ - yz² + 7. What is the value of the field at the point (0, 0, 0)?',
        options: ['10', '4', '7', '0'],
        correctIndex: 2,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'Substitute x = 0, y = 0, z = 0 directly into the scalar function:',
            'φ(0, 0, 0) = 4(0)³ - (0)(0)² + 7 = 0 - 0 + 7 = 7.'
          ],
          keyConcept: 'Evaluating a scalar field requires direct substitution of coordinates.'
        }
      },
      {
        id: 4,
        question: 'If we define del operator ∇ = i(∂/∂x) + j(∂/∂y) + k(∂/∂z), then the Operator ∇ is a:',
        options: ['Scalar operator', 'Vector differential operator', 'Both scalar and vector operator', 'None of the above'],
        correctIndex: 1,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'The del operator ∇ contains unit vector components (i, j, k) and partial differential operators.',
            'Operating on a scalar produces a vector (gradient: ∇φ), while operating via dot product produces a scalar (divergence: ∇·A).'
          ],
          keyConcept: '∇ is formally known as the Hamilton vector differential operator (nabla).'
        }
      },
      {
        id: 5,
        question: 'A point in space having positive divergence (∇ · V > 0) is called a:',
        options: ['Sink', 'Source', 'Drain', 'None of these'],
        correctIndex: 1,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'Divergence represents net outward flux of a vector field per unit volume.',
            'If ∇·V > 0, field lines diverge away from the point, signifying a Source.',
            'If ∇·V < 0, field lines converge toward the point, signifying a Sink.'
          ],
          keyConcept: 'Positive divergence = Source; Negative divergence = Sink; Zero divergence = Solenoidal.'
        }
      },
      {
        id: 6,
        question: 'If the divergence of a vector field F vanishes everywhere (i.e., ∇ · F = 0), then F can be expressed as the curl of a vector potential A (F = ∇ × A). The vector field F in this case is called:',
        options: ['Solenoidal', 'Irrotational', 'Divergence-less', 'Both (a) and (c)'],
        correctIndex: 3,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'When ∇ · F = 0, the field has zero net divergence everywhere (divergence-less).',
            'By definition, any field with zero divergence is known as a Solenoidal field.',
            'Since div(curl A) = 0 identically, F can always be written as F = ∇ × A.'
          ],
          keyConcept: '∇·F = 0 means field F is both solenoidal and divergence-less.'
        }
      },
      {
        id: 7,
        question: 'If a vector field A is curl-less, i.e., ∇ × A = 0, the field is called:',
        options: ['Solenoidal', 'Irrotational', 'Divergence-less', 'Both (a) and (c)'],
        correctIndex: 1,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'A vector field with vanishing curl (∇ × A = 0) has zero circulation around any closed path.',
            'Such fields are called Irrotational (or Conservative).',
            'Every irrotational field can be written as the gradient of a scalar potential: A = ∇φ.'
          ],
          keyConcept: '∇ × A = 0 denotes an irrotational or conservative vector field.'
        }
      },
      {
        id: 8,
        question: 'If V is the volume bounded by a closed surface S and A is a vector function of position with continuous derivatives, then ∭_V (∇ · A) dV = ∬_S A · dS. This theorem is called:',
        options: ['Divergence theorem', 'Curl theorem', 'Gauss theorem', 'Both (a) and (c)'],
        correctIndex: 3,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'The theorem equates the volume integral of the divergence of a vector field over V to the surface integral of the vector field over the enclosing boundary S.',
            'It is universally known as the Gauss Divergence Theorem.'
          ],
          keyConcept: 'Gauss Divergence Theorem converts a volume integral into a closed surface integral.'
        }
      },
      {
        id: 9,
        question: 'If S is an open two-sided surface bounded by a closed non-intersecting curve C and A is a continuous vector function, then ∬_S (∇ × A) · dS = ∮_C A · dr. This theorem is known as:',
        options: ['Fundamental theorem of curl', 'Stokes\' theorem', 'Both (a) and (b)', 'None of the above'],
        correctIndex: 2,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'Stokes\' theorem relates the surface integral of the curl of a vector field over an open surface S to the line integral of the vector field around boundary curve C.',
            'It is also known as the fundamental theorem for curl in vector calculus.'
          ],
          keyConcept: 'Stokes\' theorem connects the surface integral of curl with line integral of circulation.'
        }
      },
      {
        id: 10,
        question: 'If V is the electric potential, ρ is the volume charge density, and ε is the permittivity of the medium, which of the following describes the correct form of Poisson\'s equation?',
        options: ['∇²V = -ρ/ε', '∇V = -ρ/ε', '∇²V = 0', '∇V = 0'],
        correctIndex: 0,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'From Gauss\'s Law: ∇ · E = ρ/ε.',
            'Since E = -∇V in electrostatics, substitution yields: ∇ · (-∇V) = ρ/ε.',
            'Therefore, ∇²V = -ρ/ε (Poisson\'s Equation). When ρ = 0, it reduces to Laplace\'s Equation ∇²V = 0.'
          ],
          keyConcept: 'Poisson\'s Equation: ∇²V = -ρ/ε.'
        }
      },
      {
        id: 11,
        question: 'LASER stands for:',
        options: [
          'Light Amplification by Spontaneous Emission of Radiation',
          'Light Amplification by Stimulated Emission of Radiation',
          'Light Amplification by Spontaneous Emission of Reaction',
          'Light Amplification by Stimulated Emission of Reaction'
        ],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'L = Light',
            'A = Amplification by',
            'S = Stimulated',
            'E = Emission of',
            'R = Radiation'
          ],
          keyConcept: 'LASER acronym: Light Amplification by Stimulated Emission of Radiation.'
        }
      },
      {
        id: 12,
        question: 'Stimulated emission of two atoms produces radiations that:',
        options: [
          'Have random phase and direction',
          'Have same phase and direction',
          'Have random phase and same direction',
          'Have same phase and random direction'
        ],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'In stimulated emission, an incident photon stimulates an excited atom to emit a identical second photon.',
            'The emitted photon possesses exactly identical frequency, phase, polarization, and direction of propagation as the incident photon.'
          ],
          keyConcept: 'Stimulated emission produces completely coherent photons (same phase and direction).'
        }
      },
      {
        id: 13,
        question: 'Spatial coherence in a laser beam refers to coherence across the:',
        options: ['Longitudinal direction', 'Transverse direction', 'Both (a) and (b)', 'None of these'],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Temporal coherence measures the correlation of wave phase along the propagation direction (longitudinal).',
            'Spatial coherence describes the constant phase relationship across different points perpendicular to the direction of propagation (transverse cross-section).'
          ],
          keyConcept: 'Spatial coherence is transverse; Temporal coherence is longitudinal.'
        }
      },
      {
        id: 14,
        question: 'Which of the following is an extraordinary, unique property of laser light compared to ordinary light?',
        options: ['Speed', 'Power', 'Wavelength', 'High Coherence'],
        correctIndex: 3,
        topic: 'Lasers',
        explanation: {
          steps: [
            'All electromagnetic waves travel at the speed of light c in vacuum.',
            'Ordinary incandescent or fluorescent sources emit incoherent light with random phases.',
            'Lasers possess exceptionally high spatial and temporal coherence, allowing extreme collimation and interference.'
          ],
          keyConcept: 'Coherence is the defining signature property of laser light.'
        }
      },
      {
        id: 15,
        question: 'In which of the following LASER systems is Optical Pumping utilized as the primary excitation mechanism?',
        options: ['Ruby and Nd:YAG laser', 'Helium-Neon laser', 'Semiconductor laser', 'Carbon Dioxide laser'],
        correctIndex: 0,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Optical pumping uses intense light from a flash lamp (e.g. Xenon lamp) or laser diode.',
            'Solid-state lasers such as Ruby laser and Nd:YAG laser rely on optical pumping.',
            'In contrast, He-Ne lasers use electric discharge, and semiconductor diode lasers use electrical injection current.'
          ],
          keyConcept: 'Nd:YAG and Ruby lasers use optical pumping.'
        }
      },
      {
        id: 16,
        question: 'The Nd:YAG laser operates as a:',
        options: ['2-Level Laser', '3-Level Laser', '4-Level Laser', 'None of these'],
        correctIndex: 2,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Nd:YAG operates between four energy levels of Nd³⁺ ions:',
            'Ground state ⁴I_9/2, pump bands ⁴F_5/2, upper laser state ⁴F_3/2, and lower laser state ⁴I_11/2.',
            'Because the lower laser level is well above the ground level and thermally depopulated, population inversion is achieved easily.'
          ],
          keyConcept: 'Nd:YAG is a four-level solid state laser emitting at 1064 nm.'
        }
      },
      {
        id: 17,
        question: 'A Gallium Arsenide (GaAs) laser is classified as a:',
        options: ['Ruby laser', 'Gas laser', 'Semiconductor diode laser', 'Dye laser'],
        correctIndex: 2,
        topic: 'Lasers',
        explanation: {
          steps: [
            'GaAs has a direct bandgap (1.42 eV).',
            'Forward-biasing a GaAs p-n junction causes electrons and holes to recombine directly across the bandgap, releasing stimulated photons in the near-infrared (~840-904 nm).'
          ],
          keyConcept: 'GaAs is an injection semiconductor laser diode.'
        }
      },
      {
        id: 18,
        question: 'A Hologram records and reconstructs:',
        options: ['Amplitude only of the object wave', 'Phase only of the object wave', 'Both amplitude and phase of the object wave', 'Neither amplitude nor phase'],
        correctIndex: 2,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Standard photography records only the intensity (amplitude squared) of light, losing depth cues.',
            'Holography utilizes an interference pattern between a reference laser beam and an object beam, capturing both amplitude and phase information.'
          ],
          keyConcept: 'Holography reproduces a true 3D image by recording both amplitude and phase.'
        }
      },
      {
        id: 19,
        question: 'A Helium-Neon (He-Ne) laser operates as a:',
        options: ['4-Level Laser', '3-Level Laser', '2-Level Laser', 'None of these'],
        correctIndex: 0,
        topic: 'Lasers',
        explanation: {
          steps: [
            'In a He-Ne laser, collision between excited He atoms and ground state Ne atoms excites Neon to 2s and 3s levels.',
            'Lasing transitions occur down to 2p levels (giving 632.8 nm red light), which subsequently decay to 1s and ground state.',
            'This constitutes a classic 4-level energy scheme.'
          ],
          keyConcept: 'He-Ne laser is a 4-level continuous-wave gas laser.'
        }
      },
      {
        id: 20,
        question: 'Which of the following is NOT true for laser light?',
        options: ['Extremely intense light', 'Perfect monochromaticity', 'Highly coherent', 'Highly divergent'],
        correctIndex: 3,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Laser beams have very low angular divergence (~1 milliradian) and travel vast distances without spreading out.',
            'Therefore, stating that laser light is "highly divergent" is false.'
          ],
          keyConcept: 'Laser beams are highly directional with minimal divergence.'
        }
      },
      {
        id: 21,
        question: 'The propagation of light through an optical fiber is governed by the principle of:',
        options: ['Refraction', 'Total Internal Reflection (TIR)', 'Diffraction', 'Interference'],
        correctIndex: 1,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'The core has refractive index n₁ and cladding has n₂, where n₁ > n₂.',
            'Light launched within the acceptance cone strikes the core-cladding boundary at an angle greater than the critical angle θ_c.',
            'Hence, it undergoes repeated total internal reflections and stays guided inside the core.'
          ],
          keyConcept: 'Total Internal Reflection is the guiding principle of optical fibers.'
        }
      },
      {
        id: 22,
        question: 'A step-index fiber has a core refractive index of 1.45 and a cladding refractive index of 1.40. Its Numerical Aperture (NA) is:',
        options: ['0.1562', '0.2441', '0.3775', '0.4863'],
        correctIndex: 2,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Formula: NA = √(n₁² - n₂²)',
            'n₁ = 1.45, n₂ = 1.40',
            'n₁² = 1.45² = 2.1025',
            'n₂² = 1.40² = 1.9600',
            'NA = √(2.1025 - 1.9600) = √(0.1425) ≈ 0.37749 ≈ 0.3775.'
          ],
          keyConcept: 'NA = √(n₁² - n₂²).'
        }
      },
      {
        id: 23,
        question: 'The necessary condition for Total Internal Reflection to occur at the core-cladding interface is:',
        options: [
          'sin θ ≥ n₂ / n₁ (where θ is angle of incidence at boundary)',
          'sin θ ≤ n₂ / n₁',
          'sin θ = n₁ / n₂',
          'sin θ ≥ n₁ / n₂'
        ],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'At the critical angle θ_c, by Snell\'s law: n₁ sin θ_c = n₂ sin 90° ⇒ sin θ_c = n₂ / n₁.',
            'For total internal reflection to occur, the incident angle θ must be greater than or equal to the critical angle: θ ≥ θ_c ⇒ sin θ ≥ sin θ_c = n₂ / n₁.'
          ],
          keyConcept: 'Critical angle condition: sin θ ≥ n₂ / n₁ with n₁ > n₂.'
        }
      },
      {
        id: 24,
        question: 'Which of the following causes optical attenuation (loss) inside a glass optical fiber?',
        options: ['Radiative loss', 'Material absorption', 'Rayleigh scattering', 'All of the above'],
        correctIndex: 3,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Optical fiber signal loss occurs due to:',
            '1. Absorption (intrinsic electronic/vibrational absorption and extrinsic impurity absorption like OH⁻ ions).',
            '2. Scattering (primarily Rayleigh scattering due to sub-microscopic density variations).',
            '3. Radiative losses (microbending and macrobending losses).'
          ],
          keyConcept: 'Total attenuation = Absorption + Scattering + Bending (Radiative) losses.'
        }
      },
      {
        id: 25,
        question: 'In an optical fiber, the refractive index of core (n₁) and cladding (n₂) must satisfy the inequality:',
        options: ['n₁ > n₂', 'n₁ < n₂', 'n₁ = n₂', 'n₁² ≤ n₂²'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Total internal reflection only occurs when light travels from an optically denser medium into an optically rarer medium.',
            'Therefore, the refractive index of the core n₁ must strictly exceed that of the cladding n₂ (n₁ > n₂).'
          ],
          keyConcept: 'Guidance requirement: n_core > n_cladding.'
        }
      },
      {
        id: 26,
        question: 'The numerical aperture (NA) of a step-index optical fiber is defined as:',
        options: ['√(n₁² - n₂²)', '(n₁ - n₂)', '√(n₁² + n₂²)', '(n₂ - n₁)'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'The acceptance angle θ₀ in air (n₀ = 1) is given by: sin θ₀ = √(n₁² - n₂²).',
            'By definition, Numerical Aperture NA = sin θ₀ = √(n₁² - n₂²).'
          ],
          keyConcept: 'NA = sin(acceptance angle) = √(n₁² - n₂²).'
        }
      },
      {
        id: 27,
        question: 'A step-index fiber has a numerical aperture of 0.26. What is the acceptance angle of the fiber in air?',
        options: ['1.47°', '15.07°', '2.18°', '24.15°'],
        correctIndex: 1,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Formula: θ₀ = sin⁻¹(NA)',
            'θ₀ = sin⁻¹(0.26)',
            'Since sin(15°) = 0.2588, sin⁻¹(0.26) ≈ 15.07°.'
          ],
          keyConcept: 'Acceptance angle θ₀ = arcsin(NA).'
        }
      },
      {
        id: 28,
        question: 'The normalized frequency parameter (V-number) for a Single-Mode step-index optical fiber must satisfy:',
        options: ['V < 2.405', 'V > 2.405', 'V = 2.405', 'None of these'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'The normalized frequency parameter is V = (2π a / λ) √(n₁² - n₂²).',
            'For a step-index fiber to support only a single fundamental mode (HE₁₁), V must remain below the first Bessel zero cutoff: V < 2.405.'
          ],
          keyConcept: 'Single mode cutoff condition: V ≤ 2.405.'
        }
      },
      {
        id: 29,
        question: 'The maximum number of guided modes (N_max) supported by a step-index multimode fiber is given approximately by:',
        options: ['V² / 2', 'V² / 4', 'V² / 3', '2 V²'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'For large V, the number of propagating spatial modes in a step-index fiber is N ≈ V² / 2.',
            'For graded-index (parabolic profile) fibers, the number of modes is N ≈ V² / 4.'
          ],
          keyConcept: 'Step-index mode capacity: N ≈ V² / 2.'
        }
      },
      {
        id: 30,
        question: 'If the V-number of a single-mode step-index fiber is 2.305, the total number of fundamental supported guided modes is:',
        options: ['1', '2', '4', '8'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Since V = 2.305 < 2.405, higher-order modes cannot propagate.',
            'Only the single fundamental HE₁₁ mode (with two orthogonal polarization states) is guided through the fiber core.'
          ],
          keyConcept: 'When V < 2.405, the fiber strictly operates in single-mode regime.'
        }
      }
    ]
  },
  {
    id: 'phy110-midterm-paper-2',
    code: 'PHY110-PAPER-B',
    title: 'Midterm Examination • Paper 2 (Official University PYQ)',
    courseCode: 'PHY110',
    courseName: 'Engineering Physics',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['Lasers', 'Fiber Optics', 'Maxwell Equations', 'Electromagnetism'],
    description: 'Verified university midterm paper B testing atomic transitions, population inversion, optical pumping wavelengths, graded-index fibers, and Maxwell\'s equations.',
    questions: [
      {
        id: 1,
        question: 'What is the fundamental physical process by which a laser amplifies light?',
        options: ['Absorption of light', 'Spontaneous emission of light', 'Stimulated emission of light', 'Refraction of light'],
        correctIndex: 2,
        topic: 'Lasers',
        explanation: {
          steps: [
            'In stimulated emission, an incoming photon triggers an excited electron to drop to a lower state, releasing an identical coherent photon.',
            'This causes optical amplification in the active medium.'
          ],
          keyConcept: 'Stimulated emission is the foundation of laser amplification.'
        }
      },
      {
        id: 2,
        question: 'Which of the following is NOT one of the essential energy level types in a typical laser system?',
        options: ['Ground state', 'Excited pump state', 'Metastable state', 'Intermediate unphysical state'],
        correctIndex: 3,
        topic: 'Lasers',
        explanation: {
          steps: [
            'A laser requires a Ground State (low energy), an Excited State (pump band), and a long-lived Metastable State (~10⁻³ s vs 10⁻⁸ s).',
            'Intermediate unphysical state is not a real physical energy level.'
          ],
          keyConcept: 'The metastable state provides the necessary storage lifetime for population inversion.'
        }
      },
      {
        id: 3,
        question: 'What happens to an atom when it absorbs a photon whose energy equals the difference between two quantum states (E₂ - E₁ = hν)?',
        options: ['It moves to a lower energy level', 'It moves to a higher energy level', 'It emits a photon of light', 'Nothing happens'],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'By the Einstein absorption postulate, absorbing energy hν lifts an electron from lower energy state E₁ to higher excited energy state E₂.'
          ],
          keyConcept: 'Optical absorption elevates an atom from ground/lower state to excited state.'
        }
      },
      {
        id: 4,
        question: 'Which type of emission occurs naturally, spontaneously, and with random phase and direction?',
        options: ['Absorption', 'Spontaneous emission', 'Stimulated emission', 'Stimulated absorption'],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Without any external triggering photon, an excited electron drops spontaneously after lifetime ~10⁻⁸ s.',
            'The emitted photon has arbitrary phase, polarization, and direction, which is Spontaneous Emission.'
          ],
          keyConcept: 'Spontaneous emission generates ordinary incoherent light.'
        }
      },
      {
        id: 5,
        question: 'Population inversion in a laser active medium occurs when:',
        options: [
          'More atoms are in the ground state than the excited state',
          'More atoms are in the excited/metastable state than the ground state',
          'There are equal numbers of atoms in both states',
          'No atoms are in the ground state'
        ],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Under thermal equilibrium (Boltzmann distribution), N₁ > N₂.',
            'Population inversion reverses this so that N₂ > N₁, making stimulated emission dominant over absorption.'
          ],
          keyConcept: 'Population inversion condition: N₂ > N₁.'
        }
      },
      {
        id: 6,
        question: 'What is the active lasing ion/medium in a Nd:YAG laser?',
        options: ['Neon', 'Neodymium (Nd³⁺ ions)', 'Aluminium', 'Silicon'],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Nd:YAG is Yttrium Aluminium Garnet (Y₃Al₅O₁₂) doped with approximately 1% Neodymium (Nd³⁺) ions.',
            'The Nd³⁺ ions serve as the active lasing centers.'
          ],
          keyConcept: 'Nd³⁺ ions are the active lasing medium in Nd:YAG.'
        }
      },
      {
        id: 7,
        question: 'What is the typical dominant emission wavelength of a red Helium-Neon (He-Ne) laser?',
        options: ['632.8 nm', '1064 nm', '1550 nm', '980 nm'],
        correctIndex: 0,
        topic: 'Lasers',
        explanation: {
          steps: [
            'The prominent red transition in a He-Ne laser is from 3s₂ to 2p₄ level of Neon, emitting at 632.8 nm.',
            '1064 nm is Nd:YAG, and 1550 nm is standard optical telecom.'
          ],
          keyConcept: 'He-Ne laser emits at λ = 632.8 nm.'
        }
      },
      {
        id: 8,
        question: 'What is the primary excitation mechanism utilized in a Nd:YAG laser?',
        options: ['Electric discharge', 'Optical pumping (flashlamp or diode)', 'Chemical reaction', 'Electron beam excitation'],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Nd:YAG lasers are optically pumped using a Krypton/Xenon arc flashlamp or semiconductor laser diode arrays.'
          ],
          keyConcept: 'Nd:YAG uses optical pumping.'
        }
      },
      {
        id: 9,
        question: 'In an optical fiber, light is guided through the core primarily by means of:',
        options: ['Diffraction', 'Interference', 'Total internal reflection', 'Polarization'],
        correctIndex: 2,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Light injected within the acceptance angle experiences total internal reflection repeatedly at the core-cladding boundary.'
          ],
          keyConcept: 'Total Internal Reflection is the waveguiding mechanism in fibers.'
        }
      },
      {
        id: 10,
        question: 'The core of an optical fiber is manufactured out of:',
        options: ['Clear high-purity silica glass or plastic', 'Aluminium', 'Copper', 'Graphite'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Optical fiber cores are made of ultra-pure fused silica (SiO₂) glass doped with Germanium (GeO₂) or transparent polymers.'
          ],
          keyConcept: 'Fiber cores are made of high-purity silica glass.'
        }
      },
      {
        id: 11,
        question: 'Total internal reflection occurs only when light travels from a:',
        options: ['Rarer to denser medium', 'Denser to rarer medium', 'Air to glass', 'Vacuum to water'],
        correctIndex: 1,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'By Snell\'s law, light bends away from the normal when moving from an optically denser medium into a rarer medium (n₁ > n₂).',
            'When angle of incidence exceeds critical angle θ_c, refracted ray cannot escape, producing total internal reflection.'
          ],
          keyConcept: 'TIR requires traveling from denser medium into rarer medium.'
        }
      },
      {
        id: 12,
        question: 'In an optical fiber, dispersion causes:',
        options: ['Pulse distortion and pulse broadening', 'Pulse narrowing', 'Pulse rise-time reduction', 'Zero propagation loss'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Different spectral components (chromatic dispersion) or different propagation modes (intermodal dispersion) travel at different group velocities.',
            'This causes light pulses to spread out temporally (pulse broadening), leading to intersymbol interference (ISI).'
          ],
          keyConcept: 'Dispersion results in pulse broadening and limits maximum data rate.'
        }
      },
      {
        id: 13,
        question: 'In a Graded-Index (GRIN) optical fiber, the refractive index of the core:',
        options: [
          'Remains constant throughout the core',
          'Is equal to the cladding index',
          'Decreases continuously and parabolically from the central axis to the cladding boundary',
          'Increases toward the cladding'
        ],
        correctIndex: 2,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'In GRIN fibers, the refractive index is highest at the center axis and decreases continuously as n(r) = n₁[1 - 2Δ(r/a)²]^(1/2).',
            'This causes light rays to bend continuously in sinusoidal curves, equalizing transit times and minimizing modal dispersion.'
          ],
          keyConcept: 'Graded-index core has a parabolic refractive index profile.'
        }
      },
      {
        id: 14,
        question: 'The condition for a vector field V to be solenoidal is:',
        options: ['∇ × V = 0', '∇ · V = 0', '∇V = 0', '∇²V = 0'],
        correctIndex: 1,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'A field with zero divergence (∇ · V = 0) has no net source or sink in the region.',
            'Such a field is called solenoidal.'
          ],
          keyConcept: 'Solenoidal field condition: ∇ · V = 0.'
        }
      },
      {
        id: 15,
        question: 'The gradient of any scalar field φ (grad φ = ∇φ) is always a:',
        options: ['Vector quantity', 'Scalar quantity', 'Tensor of rank 2', 'Dimensionless constant'],
        correctIndex: 0,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            'Grad φ = (∂φ/∂x) i + (∂φ/∂y) j + (∂φ/∂z) k.',
            'It points in the direction of the maximum rate of increase of φ and is a vector.'
          ],
          keyConcept: 'Gradient of a scalar field is a vector.'
        }
      },
      {
        id: 16,
        question: 'The divergence of any vector field A (div A = ∇ · A) is always a:',
        options: ['Vector quantity', 'Scalar quantity', 'Both vector and scalar', 'None of these'],
        correctIndex: 1,
        topic: 'Vector Calculus',
        explanation: {
          steps: [
            '∇ · A = (∂A_x/∂x) + (∂A_y/∂y) + (∂A_z/∂z).',
            'Since it is a scalar dot product of operators, the outcome is a scalar quantity.'
          ],
          keyConcept: 'Divergence of a vector is a scalar.'
        }
      },
      {
        id: 17,
        question: 'Maxwell\'s Second Equation (∇ · B = 0) represents:',
        options: [
          'Gauss\'s Law for electrostatics',
          'Gauss\'s Law for magnetostatics (non-existence of isolated magnetic monopoles)',
          'Faraday\'s Law of induction',
          'Ampere\'s Circuital Law'
        ],
        correctIndex: 1,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            '∇ · B = 0 states that total magnetic flux entering any closed surface equals total flux leaving it.',
            'This physically proves that isolated magnetic monopoles do not exist; magnetic field lines are always closed continuous loops.'
          ],
          keyConcept: '∇ · B = 0 signifies Gauss\'s law for magnetism (no isolated monopoles).'
        }
      },
      {
        id: 18,
        question: 'What is the constitutive relation connecting magnetic field intensity H, magnetic flux density B, and permeability of free space μ₀?',
        options: ['B = μ₀ H', 'H = μ₀ B', 'B = H / μ₀', 'B = μ₀ + H'],
        correctIndex: 0,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'In non-magnetic or isotropic media: B = μ H = μ_r μ₀ H.',
            'In vacuum or free space: B = μ₀ H.'
          ],
          keyConcept: 'Constitutive relation: B = μ₀ H.'
        }
      },
      {
        id: 19,
        question: 'How is the uniform electric field E related to electric potential V across a conductor of length L?',
        options: ['V = E / L', 'E = V · L', 'V = E · L', 'E = V² / L'],
        correctIndex: 2,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'Electric field is negative gradient of potential: E = -dV/dx.',
            'For a uniform field across distance L: E = V / L, which gives V = E · L.'
          ],
          keyConcept: 'Potential difference V = E · L.'
        }
      },
      {
        id: 20,
        question: 'Maxwell\'s First Equation in differential form is:',
        options: ['∇ · D = ρ', '∇ · B = 0', '∇ × E = -∂B/∂t', '∇ × H = J + ∂D/∂t'],
        correctIndex: 0,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'Maxwell\'s first equation is Gauss\'s Law for electric fields: ∇ · D = ρ (or ∇ · E = ρ/ε₀ in free space).'
          ],
          keyConcept: 'Maxwell 1st equation: ∇ · D = ρ.'
        }
      },
      {
        id: 21,
        question: 'Maxwell\'s Third Equation represents which fundamental law of electromagnetism?',
        options: ['Electrostatic Gauss law', 'Faraday\'s Law of Electromagnetic Induction', 'Ampere\'s Circuital Law', 'Coulomb\'s Law'],
        correctIndex: 1,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'Maxwell\'s third equation is ∇ × E = -∂B/∂t.',
            'This states that a time-varying magnetic field induces a circulating electric field, which is Faraday\'s Law.'
          ],
          keyConcept: 'Maxwell 3rd equation is Faraday\'s Law of Induction.'
        }
      },
      {
        id: 22,
        question: 'Maxwell\'s Fourth Equation is modified from Ampere\'s law by introducing the concept of:',
        options: ['Conduction current', 'Displacement current (∂D/∂t)', 'Eddy current', 'Leakage current'],
        correctIndex: 1,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'Ampere\'s law ∇ × H = J failed for time-varying fields because div(curl H) = 0 while div J = -∂ρ/∂t ≠ 0.',
            'Maxwell introduced displacement current density J_D = ∂D/∂t to satisfy the continuity equation.'
          ],
          keyConcept: 'Displacement current J_D = ∂D/∂t made Maxwell\'s equations consistent.'
        }
      },
      {
        id: 23,
        question: 'Which of the following is true for electromagnetic waves propagating in free space?',
        options: [
          'Electric and magnetic field vectors are parallel to each other',
          'Electric and magnetic field vectors are mutually perpendicular and perpendicular to direction of wave propagation',
          'Only electric field propagates',
          'Speed is independent of permittivity and permeability'
        ],
        correctIndex: 1,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'EM waves are transverse in nature.',
            'E ⊥ B, and both are perpendicular to the propagation vector k (E × B gives direction of wave velocity).'
          ],
          keyConcept: 'EM waves are transverse: E ⊥ B ⊥ k.'
        }
      },
      {
        id: 24,
        question: 'The velocity of an electromagnetic wave in free space is given by:',
        options: ['c = 1 / √(μ₀ ε₀)', 'c = √(μ₀ ε₀)', 'c = μ₀ / ε₀', 'c = ε₀ / μ₀'],
        correctIndex: 0,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'From wave equation derived from Maxwell\'s equations: ∇²E = μ₀ε₀ (∂²E/∂t²).',
            'Comparing with standard wave equation ∇²E = (1/v²)(∂²E/∂t²), wave velocity is c = 1 / √(μ₀ ε₀) ≈ 3 × 10⁸ m/s.'
          ],
          keyConcept: 'Speed of light c = 1 / √(μ₀ ε₀).'
        }
      },
      {
        id: 25,
        question: 'Poynting vector S represents:',
        options: [
          'Rate of energy flow per unit area in an electromagnetic field (S = E × H)',
          'Total charge stored in medium',
          'Power dissipated as heat',
          'Electrostatic force per unit charge'
        ],
        correctIndex: 0,
        topic: 'Electromagnetic Theory',
        explanation: {
          steps: [
            'The Poynting vector S = E × H (in W/m²).',
            'Its direction indicates the direction of energy transport and its magnitude represents instantaneous power flux density.'
          ],
          keyConcept: 'Poynting vector S = E × H measures directional power flow density.'
        }
      },
      {
        id: 26,
        question: 'For a medium with core index n₁ = 1.50 and cladding index n₂ = 1.48, the fractional refractive index difference Δ is:',
        options: ['0.0133', '0.0200', '0.0067', '0.0400'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'Formula: Δ = (n₁ - n₂) / n₁',
            'Δ = (1.50 - 1.48) / 1.50 = 0.02 / 1.50 = 2 / 150 ≈ 0.0133 (or 1.33%).'
          ],
          keyConcept: 'Δ = (n₁ - n₂) / n₁.'
        }
      },
      {
        id: 27,
        question: 'In an optical fiber, what does the buffer coating provide?',
        options: ['Light guidance', 'Mechanical strength and physical protection against moisture and abrasion', 'Higher refractive index', 'Optical amplification'],
        correctIndex: 1,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'The primary buffer coating is made of silicones, acrylates, or polymers.',
            'Its role is to protect the brittle silica fiber from mechanical abrasion, crushing, and environmental moisture.'
          ],
          keyConcept: 'Buffer coating provides physical and mechanical protection.'
        }
      },
      {
        id: 28,
        question: 'A laser cavity resonator consists of:',
        options: [
          'An active medium placed between two parallel optical mirrors (one 100% reflective, one partially transmissive)',
          'Two prisms',
          'A single concave lens',
          'A copper waveguide'
        ],
        correctIndex: 0,
        topic: 'Lasers',
        explanation: {
          steps: [
            'An optical resonator (Fabry-Perot cavity) consists of two aligned mirrors.',
            'Light bounces back and forth through the active medium, building up amplified stimulated emission before leaking out the partial mirror as the laser beam.'
          ],
          keyConcept: 'Optical cavity resonator provides positive optical feedback.'
        }
      },
      {
        id: 29,
        question: 'What is the role of Helium in a Helium-Neon (He-Ne) laser?',
        options: [
          'It acts as the primary lasing medium',
          'He atoms are excited by electron collision and transfer their energy to Neon atoms via resonant collision',
          'It cools the discharge tube',
          'It absorbs spontaneous emissions'
        ],
        correctIndex: 1,
        topic: 'Lasers',
        explanation: {
          steps: [
            'Helium atoms have metastable 2¹S and 2³S states with energies 20.61 eV and 19.82 eV, perfectly matching the 3s and 2s levels of Neon.',
            'Helium atoms efficiently transfer energy to Neon atoms through resonant collisions, establishing population inversion in Neon.'
          ],
          keyConcept: 'Helium enables efficient resonant excitation of Neon atoms.'
        }
      },
      {
        id: 30,
        question: 'If a step-index fiber has core diameter 50 μm, n₁ = 1.48, and n₂ = 1.46 at wavelength λ = 1.3 μm, the acceptance angle is:',
        options: ['14.07°', '21.50°', '9.82°', '18.45°'],
        correctIndex: 0,
        topic: 'Fiber Optics',
        explanation: {
          steps: [
            'NA = √(n₁² - n₂²) = √(1.48² - 1.46²) = √(2.1904 - 2.1316) = √(0.0588) ≈ 0.2425.',
            'Acceptance angle θ₀ = sin⁻¹(0.2425) ≈ 14.04° ~ 14.07°.'
          ],
          keyConcept: 'Acceptance angle θ₀ = sin⁻¹(√(n₁² - n₂²)).'
        }
      }
    ]
  }
];
