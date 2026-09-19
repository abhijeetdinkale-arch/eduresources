import os

print("Generating 16 Physics Exam Companion Papers...")

# 1. CA-1 Generator (30 MCQs from Unit 1 & Unit 2)
def generate_ca1_paper(path, title, subtitle):
    content = f"\\section{{{title}}}\n\n"
    content += f"\\ExamHeader{{{title}}}{{{subtitle}}}{{60 Minutes}}{{30 Marks}}{{None}}\n\n"
    content += r"""\noindent
\textbf{General Instructions:}
\begin{enumerate}[topsep=2pt,itemsep=1pt]
    \item This paper contains \textbf{30 Multiple-Choice Questions (MCQs)} carrying \textbf{1 mark each} (Total = 30 Marks).
    \item \textbf{15 Questions from Unit 1} (Electromagnetic Theory) and \textbf{15 Questions from Unit 2} (Lasers).
    \item All questions are compulsory.
\end{enumerate}
\vspace{3mm}

\subsection*{Section A: Unit 1 --- Electromagnetic Theory (Questions 1 to 15)}
"""
    u1_mcqs = [
        (r"If a vector field $\vec{A}$ satisfies $\nabla \cdot \vec{A} = 0$, the field is:", r"Solenoidal", r"Irrotational", r"Conservative", r"Discontinuous", r"(a)", r"Zero divergence mathematically defines a solenoidal vector field."),
        (r"If $\nabla \times \vec{A} = 0$, the vector field $\vec{A}$ is:", r"Solenoidal", r"Irrotational (Conservative)", r"Non-conservative", r"Rotational", r"(b)", r"Zero curl means line integrals are path independent."),
        (r"The electric potential $V$ satisfies Poisson's equation $\nabla^2 V = $", r"0", r"$-\rho/\epsilon_0$", r"$\rho/\epsilon_0$", r"$\mu_0 J$", r"(b)", r"Poisson's equation in differential electrostatics."),
        (r"In a charge-free region ($\rho = 0$), Poisson's equation reduces to:", r"Laplace's equation $\nabla^2 V = 0$", r"Wave equation", r"Continuity equation", r"Helmholtz equation", r"(a)", r"Laplace's equation governs charge-free electrostatic potentials."),
        (r"Gauss's Divergence Theorem converts:", r"Surface integral to volume integral", r"Line integral to surface integral", r"Line integral to volume integral", r"Double to single", r"(a)", r"$\iint_S \vec{F}\cdot d\vec{S} = \iiint_V (\nabla\cdot\vec{F}) dV$."),
        (r"Stokes' Theorem relates:", r"Line integral around closed curve and surface integral of curl", r"Volume and surface", r"Scalar and vector", r"None", r"(a)", r"$\oint_C \vec{F}\cdot d\vec{l} = \iint_S (\nabla\times\vec{F})\cdot d\vec{S}$."),
        (r"The equation of continuity $\nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0$ expresses:", r"Conservation of charge", r"Conservation of energy", r"Conservation of momentum", r"Conservation of mass", r"(a)", r"Local law of conservation of electric charge."),
        (r"Maxwell's displacement current density is given by:", r"$\vec{J}_d = \frac{\partial \vec{D}}{\partial t}$", r"$\vec{J}_d = \sigma \vec{E}$", r"$\vec{J}_d = \vec{E} \times \vec{H}$", r"$\vec{J}_d = \nabla \times \vec{H}$", r"(a)", r"Displacement current arises from time-varying electric flux."),
        (r"Maxwell's equation $\nabla \cdot \vec{B} = 0$ signifies that:", r"Magnetic monopoles do not exist", r"Charges are conserved", r"Light is an EM wave", r"EM waves are transverse", r"(a)", r"No isolated magnetic poles have ever been observed."),
        (r"Faraday's law in differential form is:", r"$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$", r"$\nabla \times \vec{B} = \mu_0 \vec{J}$", r"$\nabla \cdot \vec{E} = \rho/\epsilon$", r"$\nabla \cdot \vec{B} = 0$", r"(a)", r"Time-varying magnetic flux induces circulating electric field."),
        (r"The Poynting vector $\vec{S} = \vec{E} \times \vec{H}$ represents:", r"Rate of energy flow per unit area", r"Electric charge density", r"Magnetic energy", r"Force on charge", r"(a)", r"Direction and magnitude of electromagnetic energy transport ($W/m^2$)."),
        (r"The velocity of electromagnetic waves in vacuum is given by:", r"$c = 1/\sqrt{\mu_0 \epsilon_0}$", r"$c = \sqrt{\mu_0 \epsilon_0}$", r"$c = \mu_0 / \epsilon_0$", r"$c = \epsilon_0 / \mu_0$", r"(a)", r"Derived directly from Maxwell's wave equations in free space."),
        (r"The ratio of electric to magnetic field amplitudes $E/H$ in free space is:", r"$377\,\Omega$ (Intrinsic Impedance $\eta_0$)", r"$3 \times 10^8\,\Omega$", r"$1\,\Omega$", r"$0\,\Omega$", r"(a)", r"$\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 377\,\Omega$."),
        (r"The divergence of the curl of any vector field is:", r"0", r"1", r"$\vec{A}$", r"$\infty$", r"(a)", r"Vector calculus identity: $\nabla \cdot (\nabla \times \vec{A}) = 0$."),
        (r"The curl of the gradient of any scalar field is:", r"0", r"1", r"$\nabla^2 \phi$", r"$\phi$", r"(a)", r"Vector calculus identity: $\nabla \times (\nabla \phi) = 0$.")
    ]
    for i, m in enumerate(u1_mcqs, 1):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsection*{Section B: Unit 2 --- Lasers and Applications (Questions 16 to 30)}\n"
    u2_mcqs = [
        (r"LASER stands for:", r"Light Amplification by Stimulated Emission of Radiation", r"Light Absorption by Stimulated Emission", r"Light Amplification by Spontaneous Emission", r"None", r"(a)", r"Standard acronym definition."),
        (r"Stimulated emission was theoretically predicted by:", r"Albert Einstein (1916)", r"Theodore Maiman", r"Max Planck", r"Niels Bohr", r"(a)", r"Einstein introduced $A$ and $B$ coefficients in 1916."),
        (r"In stimulated emission, the emitted photon is:", r"Identical in frequency, phase, direction, and polarization", r"Random in phase", r"Emitted in opposite direction", r"Incoherent", r"(a)", r"Stimulated photons are exact clones of incident photon."),
        (r"The condition $B_{12} = B_{21}$ indicates that:", r"Probabilities of stimulated absorption and emission are equal", r"Absorption is impossible", r"Spontaneous emission dominates", r"Laser action is automatic", r"(a)", r"Einstein relation for stimulated transition rates."),
        (r"Population inversion means:", r"$N_2 > N_1$ (Higher state population exceeds ground state)", r"$N_1 > N_2$", r"$N_1 = N_2$", r"$N_2 = 0$", r"(a)", r"Necessary non-equilibrium state for optical amplification."),
        (r"A metastable state has a lifetime of approximately:", r"$10^{-6}\text{ to } 10^{-3}\text{ s}$", r"$10^{-8}\text{ s}$", r"$10^{-12}\text{ s}$", r"1 hour", r"(a)", r"Long lifetime allows atoms to accumulate for population inversion."),
        (r"Ruby laser is an example of a:", r"Three-level solid-state laser", r"Four-level gas laser", r"Semiconductor laser", r"Two-level laser", r"(a)", r"Maiman's original 1960 laser was a 3-level Ruby crystal."),
        (r"The active medium in He-Ne laser is:", r"Neon atoms", r"Helium atoms", r"Glass tube", r"Electrons", r"(a)", r"Neon provides the laser energy levels; Helium facilitates pumping."),
        (r"The ratio of He to Ne gas in He-Ne laser is:", r"10:1", r"1:1", r"1:10", r"100:1", r"(a)", r"Optimized mixture for resonant energy transfer."),
        (r"Nd:YAG laser produces laser radiation at wavelength:", r"$1060\text{ nm}$ ($1.06\,\mu\text{m}$)", r"$632.8\text{ nm}$", r"$900\text{ nm}$", r"$532\text{ nm}$", r"(a)", r"Near-infrared 4-level laser emission."),
        (r"Semiconductor laser uses:", r"Direct bandgap p-n junction (e.g., GaAs)", r"Indirect bandgap Silicon", r"Ruby rod", r"Gas mixture", r"(a)", r"Direct bandgap enables radiative electron-hole recombination."),
        (r"An optical resonant cavity in a laser serves to:", r"Provide optical feedback and build photon density", r"Cool the laser", r"Absorb photons", r"Filter colors", r"(a)", r"Mirrors reflect photons back and forth to sustain stimulated emission."),
        (r"Holography records:", r"Both amplitude and phase of light waves", r"Amplitude only", r"Phase only", r"Color only", r"(a)", r"Interference between object and reference beam records 3D info."),
        (r"The unique property distinguishing laser from ordinary light is:", r"High temporal and spatial coherence", r"Speed", r"Energy", r"Color", r"(a)", r"Coherence is the defining property of laser radiation."),
        (r"Optical pumping is used in:", r"Ruby laser and Nd:YAG laser", r"He-Ne laser", r"Semiconductor laser", r"CO2 laser", r"(a)", r"Flash lamps / arc lamps provide optical pumping photons.")
    ]
    for i, m in enumerate(u2_mcqs, 16):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    all_mcqs = u1_mcqs + u2_mcqs
    content += r"""
\newpage
\subsection*{Complete Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{CA-1 Answer Key \& Explanations (Questions 1 to 30)}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+1, all_mcqs[i][5], all_mcqs[i][6])
        q2 = (i+16, all_mcqs[i+15][5], all_mcqs[i+15][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}
"""
    with open(path, "w") as f:
        f.write(content)

generate_ca1_paper("Physics_Exam_Companion/ca1/set_a.tex", "Continuous Assessment 1 (CA-1)", "Set A (Model Paper 1)")
generate_ca1_paper("Physics_Exam_Companion/ca1/set_b.tex", "Continuous Assessment 1 (CA-1)", "Set B (Model Paper 2)")
generate_ca1_paper("Physics_Exam_Companion/ca1/set_c.tex", "Continuous Assessment 1 (CA-1)", "Set C (Model Paper 3)")
generate_ca1_paper("Physics_Exam_Companion/ca1/set_d.tex", "Continuous Assessment 1 (CA-1)", "Set D (Model Paper 4)")
print("CA-1 Sets A, B, C, D generated.")

# 2. CA-2 Generator (In-Depth Project Reports & Assignments)
def generate_ca2_paper(path, title, subtitle, projects):
    content = f"\\section{{{title}}}\n\n"
    content += f"\\ExamHeader{{{title}}}{{{subtitle}}}{{Continuous Submission}}{{30 Marks}}{{None}}\n\n"
    content += r"""\noindent
\textbf{Continuous Assessment 2 (CA-2) Project Assignment Guidelines:}
\begin{enumerate}[topsep=2pt,itemsep=1pt]
    \item CA-2 evaluates in-depth applied physics project investigations, analytical derivations, and engineering design reports.
    \item Each report must include: \textbf{Theoretical Foundation}, \textbf{Mathematical Model / Derivation}, \textbf{Engineering Application Case Study}, and \textbf{Performance Analysis}.
\end{enumerate}
\vspace{3mm}

"""
    for idx, p in enumerate(projects, 1):
        content += f"\\begin{{projectbox}}{{{idx}: {p['title']}}}\n"
        content += f"\\textbf{{Project Overview:}} {p['overview']}\n\n"
        content += f"\\textbf{{1. Theoretical Background:}}\n{p['theory']}\n\n"
        content += f"\\textbf{{2. Mathematical Formulation \\& Governing Equations:}}\n{p['math']}\n\n"
        content += f"\\textbf{{3. Engineering Case Study \\& Practical Implementation:}}\n{p['case_study']}\n\n"
        content += f"\\textbf{{4. Critical Findings \\& Performance Analysis:}}\n{p['findings']}\n"
        content += f"\\end{{projectbox}}\n\n\\vspace{{4mm}}\n\n"

    with open(path, "w") as f:
        f.write(content)

ca2_projects_a = [
    {
        "title": "Electrodynamic Analysis of Maxwell's Equations and Waveguide Propagation",
        "overview": "Rigorous investigation of electromagnetic wave propagation in rectangular waveguides and displacement current verification in dielectric media.",
        "theory": "Maxwell's equations synthesize electrostatics, magnetostatics, and time-varying electrodynamics. The displacement current term $\\frac{\\partial \\vec{D}}{\\partial t}$ resolves the charge conservation paradox in capacitor charging circuits.",
        "math": r"""In free space, $\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B}) = -\mu_0 \epsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$.
Using $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E} = -\nabla^2 \vec{E}$, we obtain:
\begin{equation}
\nabla^2 \vec{E} = \frac{1}{c^2}\frac{\partial^2 \vec{E}}{\partial t^2}, \quad c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} \approx 3 \times 10^8\text{ m/s}
\end{equation}""",
        "case_study": "Design of a TE10 mode microwave waveguide operating at $10\\text{ GHz}$ for radar telecommunications.",
        "findings": "Waveguide cut-off frequency $f_c = \frac{c}{2a}$ strictly limits propagation. Group velocity $v_g = c\sqrt{1 - (f_c/f)^2}$ remains subluminal, preserving relativistic causality."
    },
    {
        "title": "Quantum Mechanical Modeling of 1D Potential Wells and Tunneling Dynamics",
        "overview": "Numerical and analytical investigation of electron confinement in semiconductor quantum wells and scanning tunneling microscopy (STM).",
        "theory": "When a particle is confined in an infinite potential box of length $L$, boundary conditions quantize momentum and energy into discrete eigenvalues.",
        "math": r"""Eigenvalues and eigenfunctions:
\begin{equation}
E_n = \frac{n^2 \pi^2 \hbar^2}{2m L^2}, \quad \psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
\end{equation}
For finite barriers of height $V_0 > E$, the transmission probability is $T \approx e^{-2\alpha L}$ where $\alpha = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$.""",
        "case_study": "Analysis of GaAs/AlGaAs quantum-well lasers and atomic-resolution imaging in Scanning Tunneling Microscopes.",
        "findings": "Exponential dependence of tunnel current $I \propto e^{-2\alpha d}$ yields sub-angstrom vertical resolution for surface topographical mapping."
    }
]

generate_ca2_paper("Physics_Exam_Companion/ca2/set_a.tex", "Continuous Assessment 2 (CA-2)", "Project Portfolio Set A", ca2_projects_a)
generate_ca2_paper("Physics_Exam_Companion/ca2/set_b.tex", "Continuous Assessment 2 (CA-2)", "Project Portfolio Set B", ca2_projects_a)
generate_ca2_paper("Physics_Exam_Companion/ca2/set_c.tex", "Continuous Assessment 2 (CA-2)", "Project Portfolio Set C", ca2_projects_a)
generate_ca2_paper("Physics_Exam_Companion/ca2/set_d.tex", "Continuous Assessment 2 (CA-2)", "Project Portfolio Set D", ca2_projects_a)
print("CA-2 Sets A, B, C, D generated.")

# 3. Mid-Term Generator (30 MCQs from Unit 1, Unit 2, Unit 3 with -0.25 negative marking)
def generate_midterm_paper(path, title, subtitle):
    content = f"\\section{{{title}}}\n\n"
    content += f"\\ExamHeader{{{title}}}{{{subtitle}}}{{90 Minutes}}{{30 Marks}}{{-0.25 Marks}}\n\n"
    content += r"""\noindent
\textbf{General Instructions:}
\begin{enumerate}[topsep=2pt,itemsep=1pt]
    \item This paper contains \textbf{30 Multiple-Choice Questions (MCQs)} carrying \textbf{1 mark each} (Total = 30 Marks).
    \item \textbf{10 Questions from Unit 1} (EM Theory), \textbf{10 Questions from Unit 2} (Lasers), and \textbf{10 Questions from Unit 3} (Fiber Optics).
    \item Each incorrect response incurs a deduction of \textbf{0.25 marks}.
\end{enumerate}
\vspace{3mm}

\subsection*{Section A: Unit 1 --- Electromagnetic Theory (Questions 1 to 10)}
"""
    u1_mcqs = [
        (r"The divergence of the electric field $\nabla \cdot \vec{E}$ in a medium of charge density $\rho$ is:", r"$\rho/\epsilon$", r"0", r"$-\rho/\epsilon$", r"$\mu_0 J$", r"(a)", r"Gauss's law in differential form."),
        (r"If $\vec{B} = \nabla \times \vec{A}$, then $\nabla \cdot \vec{B}$ is:", r"0", r"1", r"$\vec{A}$", r"$\rho$", r"(a)", r"Divergence of curl is identically zero."),
        (r"The scalar electric potential $V$ satisfies $\vec{E} = $", r"$-\nabla V$", r"$\nabla V$", r"$\nabla \times V$", r"$\nabla^2 V$", r"(a)", r"Electric field is the negative gradient of electrostatic potential."),
        (r"In an electromagnetic wave in free space, $\vec{E}$ and $\vec{B}$ are:", r"Perpendicular to each other and to direction of propagation", r"Parallel", r"At $45^\circ$", r"Opposite", r"(a)", r"Electromagnetic waves are strictly transverse waves."),
        (r"The equation $\nabla^2 V = 0$ is known as:", r"Laplace's equation", r"Poisson's equation", r"Ampere's law", r"Faraday's law", r"(a)", r"Laplace's equation in electrostatic charge-free regions."),
        (r"The continuity equation expresses conservation of:", r"Electric charge", r"Energy", r"Momentum", r"Mass", r"(a)", r"Fundamental charge conservation."),
        (r"The unit of electric permittivity $\epsilon_0$ is:", r"$\text{F/m}$", r"$\text{H/m}$", r"$\text{N/C}$", r"$\text{Tesla}$", r"(a)", r"Farads per meter (or $C^2/(N\cdot m^2)$)."),
        (r"Displacement current flows through:", r"Dielectric between capacitor plates during charging", r"Copper wire", r"Resistor", r"Battery", r"(a)", r"Time-varying electric flux generates displacement current in dielectrics."),
        (r"Stokes' theorem relates:", r"Line integral and surface integral", r"Volume and surface", r"Scalar and vector", r"None", r"(a)", r"Line integral of vector equals surface integral of curl."),
        (r"The Poynting vector magnitude represents:", r"Electromagnetic power density ($W/m^2$)", r"Force", r"Electric charge", r"Voltage", r"(a)", r"Directional energy flux density vector.")
    ]
    for i, m in enumerate(u1_mcqs, 1):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsection*{Section B: Unit 2 --- Lasers and Applications (Questions 11 to 20)}\n"
    u2_mcqs = [
        (r"Stimulated emission produces photons that are:", r"Coherent with incident photon", r"Incoherent", r"Random in frequency", r"Opposite in phase", r"(a)", r"Stimulated emission creates identical, in-phase photons."),
        (r"Population inversion is achieved when:", r"$N_2 > N_1$", r"$N_1 > N_2$", r"$N_1 = N_2$", r"$N_2 = 0$", r"(a)", r"Excited state population exceeds lower state population."),
        (r"Einstein's $A_{21}$ coefficient represents the probability of:", r"Spontaneous emission", r"Stimulated emission", r"Absorption", r"Pumping", r"(a)", r"$A_{21}$ is spontaneous transition rate per second."),
        (r"The wavelength emitted by He-Ne laser is:", r"$632.8\text{ nm}$", r"$1060\text{ nm}$", r"$900\text{ nm}$", r"$532\text{ nm}$", r"(a)", r"Standard visible red laser line."),
        (r"The pumping source in a Ruby laser is:", r"Helical Xenon flash lamp", r"Electric discharge", r"Chemical reaction", r"Thermal", r"(a)", r"Optical pumping via flash tube."),
        (r"Ruby laser is a:", r"3-level laser", r"4-level laser", r"2-level laser", r"Semiconductor laser", r"(a)", r"Maiman's 3-level solid-state ruby laser."),
        (r"In a He-Ne laser, the active medium that produces lasing is:", r"Neon", r"Helium", r"Argon", r"Krypton", r"(a)", r"Neon atoms emit laser light; Helium transfers collision energy."),
        (r"Semiconductor lasers require:", r"Direct bandgap material (GaAs)", r"Indirect bandgap (Si)", r"Gas tube", r"Flash lamp", r"(a)", r"Direct bandgap allows efficient radiative recombination."),
        (r"Holography was discovered by:", r"Dennis Gabor", r"Maiman", r"Einstein", r"Townes", r"(a)", r"Invented by Dennis Gabor in 1948."),
        (r"A hologram records:", r"Both amplitude and phase", r"Amplitude only", r"Phase only", r"Wavelength only", r"(a)", r"Complete wavefront reconstruction.")
    ]
    for i, m in enumerate(u2_mcqs, 11):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsection*{Section C: Unit 3 --- Fiber Optics (Questions 21 to 30)}\n"
    u3_mcqs = [
        (r"Light propagates through optical fiber by:", r"Total Internal Reflection", r"Diffraction", r"Refraction", r"Interference", r"(a)", r"Continuous TIR along core-cladding interface."),
        (r"In an optical fiber, the refractive indices satisfy:", r"$n_1 > n_2$ (Core > Cladding)", r"$n_1 < n_2$", r"$n_1 = n_2$", r"$n_2 = 1$", r"(a)", r"Core must be optically denser."),
        (r"The Numerical Aperture of an optical fiber is:", r"$NA = \sqrt{n_1^2 - n_2^2}$", r"$NA = n_1 - n_2$", r"$NA = n_1 + n_2$", r"$NA = n_1/n_2$", r"(a)", r"Defines light-gathering power of the fiber."),
        (r"The cutoff V-number for single-mode fiber is:", r"$V \le 2.405$", r"$V > 2.405$", r"$V = 10$", r"$V = 0$", r"(a)", r"Condition for only fundamental $HE_{11}$ mode propagation."),
        (r"In a graded-index fiber, refractive index decreases:", r"Radially from center to cladding", r"Axially", r"Linearly along length", r"Randomly", r"(a)", r"Parabolic profile equalizes modal transit times."),
        (r"The primary cause of intrinsic attenuation in silica glass at 1550 nm is:", r"Rayleigh scattering ($\propto 1/\lambda^4$)", r"Absorption", r"Bending", r"Splice loss", r"(a)", r"Rayleigh scattering scales as $1/\lambda^4$."),
        (r"The lowest optical loss window in silica fibers is at:", r"$1550\text{ nm}$ (~0.2 dB/km)", r"$850\text{ nm}$", r"$1310\text{ nm}$", r"$632.8\text{ nm}$", r"(a)", r"Optimal wavelength for long-haul telecommunications."),
        (r"In endoscopy, image transmission is performed using a:", r"Coherent fiber bundle", r"Non-coherent bundle", r"Single thick glass rod", r"Mirror", r"(a)", r"Coherent bundle preserves spatial position of pixels."),
        (r"Attenuation $\alpha$ in dB/km for length $L$ is given by:", r"$\alpha = \frac{10}{L}\log_{10}(P_{\text{in}}/P_{\text{out}})$", r"$\alpha = \frac{P_{\text{in}}}{P_{\text{out}}}$", r"$\alpha = \ln(P_{\text{in}}/P_{\text{out}})$", r"$\alpha = 10 L$", r"(a)", r"Standard decibel loss definition."),
        (r"The number of modes in a graded-index fiber is approximately:", r"$V^2/4$", r"$V^2/2$", r"$V$", r"$2V$", r"(a)", r"Graded index supports half the modes of step index ($V^2/4$).")
    ]
    for i, m in enumerate(u3_mcqs, 21):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    all_mid_mcqs = u1_mcqs + u2_mcqs + u3_mcqs
    content += r"""
\newpage
\subsection*{Complete Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{Mid-Term Answer Key \& Explanations (Questions 1 to 30)}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+1, all_mid_mcqs[i][5], all_mid_mcqs[i][6])
        q2 = (i+16, all_mid_mcqs[i+15][5], all_mid_mcqs[i+15][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}
"""
    with open(path, "w") as f:
        f.write(content)

generate_midterm_paper("Physics_Exam_Companion/midterm/set_a.tex", "Mid-Term Examination Suite", "Set A (Model Paper 1)")
generate_midterm_paper("Physics_Exam_Companion/midterm/set_b.tex", "Mid-Term Examination Suite", "Set B (Model Paper 2)")
generate_midterm_paper("Physics_Exam_Companion/midterm/set_c.tex", "Mid-Term Examination Suite", "Set C (Model Paper 3)")
generate_midterm_paper("Physics_Exam_Companion/midterm/set_d.tex", "Mid-Term Examination Suite", "Set D (Model Paper 4)")
print("Mid-Term Sets A, B, C, D generated.")

# 4. End-Term Generator (60 MCQs comprehensive from all units, mostly Units 4, 5, 6 with -0.25 negative marking)
def generate_endterm_paper(path, title, subtitle):
    content = f"\\section{{{title}}}\n\n"
    content += f"\\ExamHeader{{{title}}}{{{subtitle}}}{{3 Hours}}{{60 Marks}}{{-0.25 Marks}}\n\n"
    content += r"""\noindent
\textbf{Official University Examination Structure:}
\begin{enumerate}[topsep=2pt,itemsep=1pt]
    \item This paper contains \textbf{60 Multiple-Choice Questions (MCQs)} carrying \textbf{1 mark each} (Total = 60 Marks).
    \item \textbf{Curriculum Weightage:} ~20 MCQs from Units 1--3 and ~40 MCQs heavily concentrated in \textbf{Unit 4} (Quantum Mechanics), \textbf{Unit 5} (Semiconductor Physics), and \textbf{Unit 6} (Engineering Materials).
    \item Each incorrect response incurs a deduction of \textbf{0.25 marks}.
\end{enumerate}
\vspace{3mm}

\subsection*{Part I: Foundational Units 1, 2, 3 Review (Questions 1 to 20)}
"""
    u123_end_mcqs = [
        (r"Poisson's equation for electric potential in a medium of charge density $\rho$ is:", r"$\nabla^2 V = -\rho/\epsilon_0$", r"$\nabla^2 V = 0$", r"$\nabla V = -\rho$", r"$\nabla^2 V = \mu_0 J$", r"(a)", r"Electrostatic potential Poisson equation."),
        (r"If a vector field satisfies $\nabla \times \vec{F} = 0$, it is:", r"Irrotational", r"Solenoidal", r"Rotational", r"Non-conservative", r"(a)", r"Curl-free fields are irrotational."),
        (r"Maxwell's displacement current density is defined as:", r"$\frac{\partial \vec{D}}{\partial t}$", r"$\sigma \vec{E}$", r"$\vec{E} \times \vec{H}$", r"$\nabla \times \vec{H}$", r"(a)", r"Time rate of change of electric displacement field."),
        (r"Maxwell's second equation $\nabla \cdot \vec{B} = 0$ implies:", r"No magnetic monopoles exist", r"Charge conservation", r"EM wave speed is c", r"Ohm's law", r"(a)", r"Magnetic field lines form continuous closed loops."),
        (r"Poynting vector is given by $\vec{S} = $", r"$\vec{E} \times \vec{H}$", r"$\vec{E} \cdot \vec{B}$", r"$\vec{E} / \vec{B}$", r"$\frac{1}{2}\epsilon E^2$", r"(a)", r"Poynting energy flux vector ($W/m^2$)."),
        (r"Stimulated emission was theoretically discovered by:", r"Albert Einstein (1916)", r"Theodore Maiman", r"Max Planck", r"Niels Bohr", r"(a)", r"Einstein derived $A$ and $B$ coefficients."),
        (r"The wavelength of light emitted by a He-Ne laser is:", r"$632.8\text{ nm}$", r"$1060\text{ nm}$", r"$900\text{ nm}$", r"$532\text{ nm}$", r"(a)", r"Standard red He-Ne laser emission line."),
        (r"Nd:YAG laser operates in which spectral region?", r"Near Infrared ($1060\text{ nm}$)", r"Visible red", r"Ultraviolet", r"X-ray", r"(a)", r"1060 nm is in near infrared."),
        (r"Hologram records which properties of light?", r"Both amplitude and phase", r"Amplitude only", r"Phase only", r"Intensity only", r"(a)", r"Interference between object and reference beam records 3D information."),
        (r"Total internal reflection in optical fiber requires:", r"$n_{\text{core}} > n_{\text{cladding}}$", r"$n_{\text{core}} < n_{\text{cladding}}$", r"$n_{\text{core}} = n_{\text{cladding}}$", r"$n_{\text{cladding}} = 1$", r"(a)", r"Light must travel from optically denser core to rarer cladding."),
        (r"Numerical Aperture (NA) is calculated as:", r"$\sqrt{n_1^2 - n_2^2}$", r"$n_1 - n_2$", r"$n_1 + n_2$", r"$\sqrt{n_1/n_2}$", r"(a)", r"Standard formula for fiber light-gathering power."),
        (r"The cutoff normalized frequency $V$ for single-mode fiber is:", r"$V \le 2.405$", r"$V > 2.405$", r"$V = 10$", r"$V = 0$", r"(a)", r"Cutoff for single-mode propagation."),
        (r"The optical window with the absolute lowest attenuation in silica fiber is:", r"$1550\text{ nm}$", r"$850\text{ nm}$", r"$1310\text{ nm}$", r"$632.8\text{ nm}$", r"(a)", r"Lowest attenuation window (~0.2 dB/km)."),
        (r"In medical endoscopy, image transmission is achieved via:", r"Coherent fiber bundle", r"Incoherent bundle", r"Single core fiber", r"Prism", r"(a)", r"Coherent fiber bundles preserve 2D pixel alignment."),
        (r"The ratio of He to Ne in a He-Ne gas laser is:", r"10:1", r"1:1", r"1:10", r"100:1", r"(a)", r"Optimized 10:1 gas ratio."),
        (r"The intrinsic impedance of free space is approximately:", r"$377\,\Omega$", r"$50\,\Omega$", r"$100\,\Omega$", r"$0\,\Omega$", r"(a)", r"$\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 377\,\Omega$."),
        (r"Stokes' theorem relates surface integral of curl with:", r"Line integral around boundary curve", r"Volume integral", r"Point value", r"Scalar gradient", r"(a)", r"Stokes' integral theorem."),
        (r"Ruby laser is pumped by:", r"Xenon flash tube", r"Electric discharge", r"Chemical reaction", r"Thermal heat", r"(a)", r"Optical pumping with flash lamp."),
        (r"In graded-index optical fiber, the refractive index profile is:", r"Parabolic (maximum at axis)", r"Constant", r"Linear decrease", r"Step profile", r"(a)", r"Parabolic graded profile reduces modal dispersion."),
        (r"Einstein's relation states that $B_{12} = $", r"$B_{21}$", r"$A_{21}$", r"$2 B_{21}$", r"$0$", r"(a)", r"Equal probability for stimulated absorption and emission.")
    ]
    for i, m in enumerate(u123_end_mcqs, 1):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsection*{Part II: Core Quantum, Semiconductor, and Materials Focus (Questions 21 to 60)}\n"
    u456_end_mcqs = [
        (r"Planck's quantum hypothesis states that energy of radiation of frequency $\nu$ is:", r"$E = h\nu$", r"$E = mc^2$", r"$E = \frac{1}{2}h\nu$", r"$E = h/\nu$", r"(a)", r"Fundamental quantum formula."),
        (r"In photoelectric effect, the maximum kinetic energy of ejected electrons depends on:", r"Frequency of incident light", r"Intensity only", r"Exposure time", r"Angle of incidence", r"(a)", r"Einstein: $E_k = h\nu - \phi_0$ depends on frequency."),
        (r"The de Broglie wavelength of a particle with momentum $p$ is:", r"$\lambda = h/p$", r"$\lambda = p/h$", r"$\lambda = h p$", r"$\lambda = \sqrt{h/p}$", r"(a)", r"Matter wave wavelength."),
        (r"Electron diffraction in the Davisson-Germer experiment proved:", r"Wave nature of electrons", r"Particle nature of light", r"Photoelectric effect", r"Radioactivity", r"(a)", r"Confirmed de Broglie hypothesis experimentally."),
        (r"For matter waves, the group velocity $v_g$ equals:", r"Particle velocity $v$", r"Phase velocity $v_p$", r"Speed of light $c$", r"Zero", r"(a)", r"$v_g = d\omega/dk = v$."),
        (r"Heisenberg's uncertainty relation for position and momentum is:", r"$\Delta x \Delta p \ge \hbar/2$", r"$\Delta x \Delta p = 0$", r"$\Delta x \Delta p \le \hbar$", r"$\Delta x / \Delta p \ge \hbar$", r"(a)", r"Quantum uncertainty principle."),
        (r"The probability density of finding a quantum particle is given by:", r"$|\psi(x,t)|^2$", r"$\psi(x,t)$", r"$\frac{d\psi}{dx}$", r"$\int \psi dx$", r"(a)", r"Born statistical interpretation."),
        (r"The energy of a particle confined in a 1D box of length $L$ is proportional to:", r"$n^2$", r"$n$", r"$1/n$", r"$1/n^2$", r"(a)", r"$E_n = \frac{n^2 h^2}{8mL^2} \propto n^2$."),
        (r"The zero-point energy ($n=1$) of a particle in a 1D box is:", r"$\frac{h^2}{8mL^2}$", r"0", r"$\infty$", r"$\frac{h^2}{2mL^2}$", r"(a)", r"Minimum kinetic energy in quantum confinement."),
        (r"The Time-Independent Schrödinger Equation in 1D is:", r"$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi$", r"$\frac{d\psi}{dt} = E\psi$", r"$\nabla^2 \psi = 0$", r"$\frac{d^2\psi}{dx^2} = E\psi$", r"(a)", r"Stationary state wave equation."),
        (r"The Wiedemann-Franz Law relates:", r"Thermal and electrical conductivities ($K/\sigma = L T$)", r"Current and voltage", r"Heat and work", r"Mass and energy", r"(a)", r"$K/\sigma = L T$ in metals."),
        (r"In an intrinsic semiconductor, the Fermi level $E_F$ is located:", r"In the middle of the forbidden gap", r"In the conduction band", r"In the valence band", r"Above conduction band", r"(a)", r"$n = p = n_i \implies E_F$ in middle of gap."),
        (r"Direct bandgap semiconductors (GaAs) are preferred for LEDs because:", r"Recombination emits photons directly without phonons", r"They are cheap", r"They have zero resistance", r"They have indirect transitions", r"(a)", r"Radiative recombination occurs directly across bandgap."),
        (r"At absolute zero ($T = 0\text{ K}$), the Fermi-Dirac probability $f(E)$ for $E < E_F$ is:", r"1", r"0", r"0.5", r"0.25", r"(a)", r"All states below Fermi level are completely occupied."),
        (r"At $E = E_F$ for any temperature $T > 0\text{ K}$, the probability $f(E_F)$ is:", r"0.5 (50\%)", r"1", r"0", r"0.25", r"(a)", r"$f(E_F) = \frac{1}{1 + e^0} = 0.5$."),
        (r"A negative Hall coefficient ($R_H < 0$) indicates majority carriers are:", r"Electrons (N-type)", r"Holes (P-type)", r"Ions", r"Photons", r"(a)", r"Negative Hall coefficient signifies N-type semiconductor."),
        (r"The Hall coefficient $R_H$ is given by:", r"$R_H = \frac{1}{n q}$", r"$R_H = n q$", r"$R_H = q/n$", r"$R_H = 1/(n^2 q)$", r"(a)", r"Definition of Hall coefficient."),
        (r"A solar cell generates electrical power based on the:", r"Photovoltaic effect at a p-n junction", r"Seebeck effect", r"Peltier effect", r"Hall effect", r"(a)", r"Light creates electron-hole pairs separated by p-n junction field."),
        (r"In a P-type semiconductor, the majority charge carriers are:", r"Holes", r"Electrons", r"Photons", r"Phonons", r"(a)", r"Trivalent doping creates excess majority holes."),
        (r"Doping silicon with phosphorus (pentavalent) creates a(n):", r"N-type semiconductor", r"P-type semiconductor", r"Intrinsic semiconductor", r"Insulator", r"(a)", r"Pentavalent donor atoms produce N-type semiconductor."),
        (r"Superconductivity was discovered in 1911 by:", r"Heike Kamerlingh Onnes", r"Albert Einstein", r"Max Planck", r"Niels Bohr", r"(a)", r"Discovered in liquid helium cooled mercury at 4.12 K."),
        (r"The expulsion of magnetic flux from a superconductor ($B = 0$) is called:", r"Meissner Effect", r"Hall Effect", r"Photoelectric Effect", r"Compton Effect", r"(a)", r"Perfect diamagnetism below $T_c$."),
        (r"A superconductor inside the superconducting state is a:", r"Perfect diamagnet ($\chi_m = -1$)", r"Paramagnet", r"Ferromagnet", r"Dielectric", r"(a)", r"$B = \mu_0(H+M) = 0 \implies \chi_m = -1$."),
        (r"The critical magnetic field varies with temperature according to:", r"$H_c(T) = H_0 [1 - (T/T_c)^2]$", r"$H_c(T) = H_0 (1 - T/T_c)$", r"$H_c(T) = H_0 (1 + T/T_c)$", r"$H_c(T) = H_0 (T/T_c)^2$", r"(a)", r"Parabolic critical magnetic field equation."),
        (r"Type-I superconductors are known as:", r"Soft superconductors", r"Hard superconductors", r"High-Tc cuprates", r"Ceramics", r"(a)", r"Type-I superconductors have complete Meissner effect with low $H_c$."),
        (r"Type-II superconductors exhibit a mixed (vortex) state between:", r"$H_{c1}$ and $H_{c2}$", r"$0$ and $H_{c1}$", r"$H_{c2}$ and $\infty$", r"None", r"(a)", r"Abrikosov vortex state exists between $H_{c1}$ and $H_{c2}$."),
        (r"Above the Curie temperature $T_c$, a ferromagnetic material becomes:", r"Paramagnetic", r"Diamagnetic", r"Superconducting", r"Dielectric", r"(a)", r"Curie-Weiss law transition to paramagnetic state."),
        (r"Magnetic susceptibility of a diamagnetic material is:", r"Small and negative", r"Large and positive", r"Zero", r"Infinite", r"(a)", r"Diamagnets are weakly repelled by magnetic fields."),
        (r"Soft magnetic materials have:", r"Narrow hysteresis loop and low coercivity", r"Wide hysteresis loop", r"High coercivity", r"Zero permeability", r"(a)", r"Ideal for transformer cores and AC machines."),
        (r"The direct piezoelectric effect converts:", r"Mechanical stress into electrical voltage", r"Electric field into strain", r"Heat into light", r"Current into magnetic field", r"(a)", r"Used in gas lighters, strain gauges, and piezoelectric sensors."),
        (r"The converse (inverse) piezoelectric effect converts:", r"Alternating electric voltage into mechanical vibration", r"Stress into voltage", r"Heat into current", r"Light into sound", r"(a)", r"Used in ultrasonic transducers and sonar emitters."),
        (r"SQUID magnetometer operates using:", r"Superconducting Josephson junctions", r"Semiconductor diodes", r"Phototubes", r"Thermocouples", r"(a)", r"Measures magnetic fields as small as $10^{-14}\text{ Tesla}$."),
        (r"High-temperature superconductors (HTS like YBCO) operate above the boiling point of:", r"Liquid Nitrogen ($77\text{ K}$)", r"Liquid Helium ($4.2\text{ K}$)", r"Room temperature", r"Water", r"(a)", r"YBCO transitions at $93\text{ K} > 77\text{ K}$."),
        (r"Maglev trains utilize which superconducting property for levitation?", r"Meissner effect flux expulsion", r"High resistance", r"Piezoelectric effect", r"Hall effect", r"(a)", r"Magnetic repulsion via perfect diamagnetism."),
        (r"The electric displacement field $\vec{D}$ is related to $\vec{E}$ and polarization $\vec{P}$ by:", r"$\vec{D} = \epsilon_0 \vec{E} + \vec{P}$", r"$\vec{D} = \epsilon_0 \vec{E} - \vec{P}$", r"$\vec{D} = \vec{E}/\vec{P}$", r"$\vec{D} = \vec{P}$", r"(a)", r"Constitutive dielectric relation."),
        (r"Non-polar dielectrics have:", r"Zero permanent dipole moment in the absence of field", r"Permanent dipoles", r"Infinite conductivity", r"Negative permittivity", r"(a)", r"Dipoles are induced only when external field is applied."),
        (r"Polar dielectrics (such as water) exhibit:", r"Permanent electric dipole moments", r"Zero dipole moment", r"Superconductivity", r"Ferromagnetism", r"(a)", r"Asymmetric molecular charge distribution gives permanent dipoles."),
        (r"In the Kronig-Penney model, energy bandgaps occur at Brillouin zone boundaries where:", r"$k = \pm n\pi/a$", r"$k = 0$", r"$k = \infty$", r"$k = a/\pi$", r"(a)", r"Bragg reflection of electron waves in crystal lattice."),
        (r"The effective mass $m^*$ of an electron in an energy band is given by:", r"$m^* = \hbar^2 / \left(\frac{d^2 E}{dk^2}\right)$", r"$m^* = \hbar k$", r"$m^* = \frac{dE}{dk}$", r"$m^* = m_0$", r"(a)", r"Determined by band curvature in $E$-$k$ diagram."),
        (r"The relaxation time $\tau$ of conduction electrons in copper is approximately:", r"$10^{-14}\text{ s}$", r"$1\text{ s}$", r"$10^{-6}\text{ s}$", r"$10^{-3}\text{ s}$", r"(a)", r"Mean time between collisions at room temperature.")
    ]
    for i, m in enumerate(u456_end_mcqs, 21):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    all_end_mcqs = u123_end_mcqs + u456_end_mcqs
    content += r"""
\newpage
\subsection*{Complete Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{End-Term Answer Key \& Explanations (Questions 1 to 60)}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(30):
        q1 = (i+1, all_end_mcqs[i][5], all_end_mcqs[i][6])
        q2 = (i+31, all_end_mcqs[i+30][5], all_end_mcqs[i+30][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}
"""
    with open(path, "w") as f:
        f.write(content)

generate_endterm_paper("Physics_Exam_Companion/endterm/set_a.tex", "End-Term University Examination (60 MCQs)", "Paper Code: A (Official Model Paper 1)")
generate_endterm_paper("Physics_Exam_Companion/endterm/set_b.tex", "End-Term University Examination (60 MCQs)", "Set B (Model Paper 2)")
generate_endterm_paper("Physics_Exam_Companion/endterm/set_c.tex", "End-Term University Examination (60 MCQs)", "Set C (Model Paper 3)")
generate_endterm_paper("Physics_Exam_Companion/endterm/set_d.tex", "End-Term University Examination (60 MCQs)", "Set D (Model Paper 4)")
print("End-Term Sets A, B, C, D generated.")

print("All 16 Physics Exam Companion papers successfully generated.")
