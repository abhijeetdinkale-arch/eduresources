import os

os.makedirs("PHY175/chapters", exist_ok=True)

# ==============================================================================
# CHAPTER 1: EXPANDED SOLID STATE PHYSICS
# ==============================================================================
ch1 = r"""\chapter{Solid State Physics: Carrier Transport, Band Structure, and Energy Devices}
\label{chap:solid_state_physics}

\section{Introduction and Theoretical Foundations}
The modern era of microelectronics, solid-state computing, and optoelectronics rests entirely upon the quantum mechanical and statistical behavior of electrons within crystalline solids. Understanding how electrons move, scatter, occupy energy states, and respond to electric and magnetic fields forms the foundation for analyzing everything from diodes and transistors to photovoltaic solar cells and quantum semiconductor devices.

In this chapter, we trace the complete theoretical progression of solid-state physics:
\begin{enumerate}
    \item \textbf{Classical Drude-Lorentz Model:} Classical free electron gas dynamics, relaxation time, electrical conductivity, thermal conductivity, and the Wiedemann-Franz law.
    \item \textbf{Quantum Free Electron Theory (Sommerfeld Model):} Fermi-Dirac statistics, density of states in 3D, and the derivation of Fermi energy, Fermi velocity, and Fermi temperature.
    \item \textbf{Band Theory of Solids:} Bloch's theorem, Kronig-Penney 1D model, energy bandgap formation, and Brillouin zones.
    \item \textbf{Effective Mass and Hole Transport:} Quantum mechanical group velocity, origin of negative effective mass, and positive hole quasiparticles.
    \item \textbf{Direct vs. Indirect Bandgap Materials:} Momentum conservation, optical absorption, and radiative emission.
    \item \textbf{Semiconductor Transport and the Hall Effect:} Intrinsic and extrinsic carrier statistics, drift and diffusion currents, Einstein relation, and transverse Hall voltage characterization.
    \item \textbf{Photovoltaic Solar Cells:} P-N junction operating principles, $I$-$V$ characteristics, open-circuit voltage, short-circuit current, fill factor, efficiency, loss mechanisms, and anti-reflective coatings.
\end{enumerate}

\section{Classical Free Electron Theory: The Drude-Lorentz Model}
\subsection{Physical Postulates of the Drude Model}
Formulated by Paul Drude in 1900, the classical free electron model applies kinetic gas theory to conduction electrons in metals. The fundamental postulates are:
\begin{enumerate}
    \item \textbf{Independent and Free Electron Approximation:} Valence electrons detach from parent atoms and move freely throughout the crystal volume without inter-electronic Coulomb repulsion or positive ion lattice potential between collisions.
    \item \textbf{Collision Dynamics and Relaxation Time:} Electrons undergo instantaneous collisions with positive ion cores. The collision probability per unit time is $1/\tau$, where $\tau$ is the \textbf{mean relaxation time} (the average time between two consecutive collisions). The mean free path is $\lambda = v_{th} \tau$.
    \item \textbf{Thermal Velocity Distribution:} In the absence of an electric field, electron velocities are purely random. The average thermal velocity $\langle v_{th} \rangle$ is governed by classical Maxwell-Boltzmann equipartition:
    \begin{equation}
        \frac{1}{2} m \langle v_{th}^2 \rangle = \frac{3}{2} k_B T \implies v_{th} = \sqrt{\frac{3 k_B T}{m}}
    \end{equation}
    At room temperature ($T = 300\,\text{K}$), $v_{th} \approx 1.17 \times 10^5\,\text{m/s}$.
\end{enumerate}

\begin{derivationbox}[Derivation of Microscopic Ohm's Law and Electrical Conductivity]
Consider an electron of mass $m$ and charge $-e$ subjected to a uniform external electric field $\mathbf{E}$. The classical equation of motion incorporates an acceleration term from the electric force and a frictional damping term due to lattice collisions:
\begin{equation}
    m \frac{d\mathbf{v}_d}{dt} + \frac{m}{\tau}\mathbf{v}_d = -e \mathbf{E}
\end{equation}
Under steady-state conditions ($d\mathbf{v}_d/dt = 0$), the steady \textbf{drift velocity} $\mathbf{v}_d$ is:
\begin{equation}
    \mathbf{v}_d = -\frac{e \tau}{m} \mathbf{E} = -\mu_e \mathbf{E}
\end{equation}
where $\mu_e = \frac{e\tau}{m}$ is the electron mobility. The macroscopic current density $\mathbf{J}$ is given by the product of free electron density $n$, charge $-e$, and drift velocity $\mathbf{v}_d$:
\begin{equation}
    \mathbf{J} = n(-e)\mathbf{v}_d = n(-e)\left(-\frac{e\tau}{m}\mathbf{E}\right) = \left(\frac{n e^2 \tau}{m}\right)\mathbf{E}
\end{equation}
Comparing this directly with the microscopic form of Ohm's law, $\mathbf{J} = \sigma \mathbf{E}$, establishes the fundamental \textbf{Drude conductivity formula}:
\begin{equation}
    \sigma = \frac{n e^2 \tau}{m} = n e \mu_e
\end{equation}
The electrical resistivity is $\rho = \frac{1}{\sigma} = \frac{m}{n e^2 \tau}$.
\end{derivationbox}

\subsection{Thermal Conductivity and the Wiedemann-Franz Law}
In metals, thermal energy is primarily transported by conduction electrons. From kinetic gas theory, thermal conductivity $K$ is given by:
\begin{equation}
    K = \frac{1}{3} C_v v_{th} \lambda = \frac{1}{3} \left(\frac{3}{2} n k_B\right) v_{th} (v_{th} \tau) = \frac{1}{2} n k_B \tau v_{th}^2
\end{equation}
Substituting the classical equipartition velocity $v_{th}^2 = \frac{3 k_B T}{m}$:
\begin{equation}
    K = \frac{3 n k_B^2 T \tau}{2 m}
\end{equation}
Dividing thermal conductivity $K$ by electrical conductivity $\sigma = \frac{ne^2\tau}{m}$ produces the \textbf{Wiedemann-Franz Law}:
\begin{equation}
    \frac{K}{\sigma T} = \frac{\frac{3 n k_B^2 T \tau}{2 m}}{\left(\frac{n e^2 \tau}{m}\right) T} = \frac{3}{2} \left(\frac{k_B}{e}\right)^2 \equiv L_{\text{classical}} \approx 1.11 \times 10^{-8}\,\text{W}\,\Omega\,\text{K}^{-2}
\end{equation}
The constant $L = \frac{K}{\sigma T}$ is known as the \textbf{Lorenz number}. (In modern quantum Sommerfeld theory, $L_{\text{quantum}} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 \approx 2.44 \times 10^{-8}\,\text{W}\,\Omega\,\text{K}^{-2}$, matching experimental values with high precision).

\subsection{Successes and Critical Failures of Classical Theory}
\begin{pitfallbox}[Limitations and Failures of the Classical Drude Model]
\begin{enumerate}
    \item \textbf{Electronic Heat Capacity Anomaly:} Classical equipartition predicts each electron contributes $\frac{3}{2}k_B$ to specific heat, giving an electronic molar heat capacity $C_{v,el} = \frac{3}{2}R$. However, experimental measurements at room temperature show $C_{v,el} < 0.01 R$.
    \item \textbf{Resistivity vs. Temperature:} Classical theory predicts $\rho \propto v_{th} \propto \sqrt{T}$, whereas pure metals experimentally exhibit linear dependence $\rho \propto T$ at room temperature.
    \item \textbf{Paramagnetism:} Classical theory predicts Curie-type temperature dependence ($\chi \propto 1/T$), whereas metals exhibit temperature-independent Pauli paramagnetism.
    \item \textbf{Hall Coefficient Discrepancy:} Classical Drude theory predicts $R_H = -\frac{1}{ne}$, strictly negative for all conductors. It cannot explain the positive Hall coefficients observed in metals such as Zinc, Beryllium, and Cadmium.
\end{enumerate}
\end{pitfallbox}

\section{Quantum Free Electron Theory: The Sommerfeld Model}
\subsection{Fermi-Dirac Statistics and the Fermi Function}
Arnold Sommerfeld resolved the classical failures by applying quantum mechanics and Fermi-Dirac statistics to the electron gas. Electrons are indistinguishable fermions of spin $s = 1/2$, subject to the \textbf{Pauli Exclusion Principle} (no two electrons can occupy the same quantum state).

The probability $f(E)$ that an available quantum energy state $E$ is occupied at thermodynamic temperature $T$ is given by the \textbf{Fermi-Dirac distribution}:
\begin{equation}
    f(E) = \frac{1}{e^{(E - E_F)/k_B T} + 1}
\end{equation}
where $E_F$ is the \textbf{Fermi Energy} (chemical potential).

\begin{conceptbox}[Physical Meaning and Limiting Behavior of $f(E)$]
\begin{itemize}
    \item \textbf{At Absolute Zero ($T = 0\,\text{K}$):}
    \begin{align}
        \text{For } E < E_F(0): \quad & e^{(E-E_F)/0} = e^{-\infty} = 0 \implies f(E) = 1 \\
        \text{For } E > E_F(0): \quad & e^{(E-E_F)/0} = e^{+\infty} = \infty \implies f(E) = 0
    \end{align}
    At $T = 0\,\text{K}$, all energy levels up to $E_F(0)$ are completely filled ($100\%$ occupied), and all levels above $E_F(0)$ are completely empty.
    \item \textbf{At Finite Temperature ($T > 0\,\text{K}$):} Thermal energy ($k_B T \approx 26\,\text{meV}$ at $300\,\text{K}$) excites electrons located only within $\approx \pm k_B T$ of the Fermi surface into higher unoccupied states.
    \item \textbf{At the Fermi Level ($E = E_F$):} For any temperature $T > 0\,\text{K}$:
    \begin{equation}
        f(E_F) = \frac{1}{e^0 + 1} = \frac{1}{2} = 0.50 \quad (50\%\text{ occupancy probability})
    \end{equation}
\end{itemize}
\end{conceptbox}

\subsection{Quantum Density of States and Derivation of Fermi Energy}
\begin{derivationbox}[Rigorous Derivation of 3D Density of States and $E_F(0)$]
Consider an electron confined within a 3D cubic crystal of side $L$ and volume $V = L^3$. Solving the time-independent Schr\"{o}dinger equation $-\frac{\hbar^2}{2m}\nabla^2 \psi = E\psi$ with periodic boundary conditions yields discrete wavevector components:
\begin{equation}
    k_x = \frac{2\pi n_x}{L}, \quad k_y = \frac{2\pi n_y}{L}, \quad k_z = \frac{2\pi n_z}{L} \quad (n_x, n_y, n_z \in \mathbb{Z})
\end{equation}
The volume occupied by a single spatial quantum state in $k$-space is:
\begin{equation}
    \Delta V_k = \left(\frac{2\pi}{L}\right)^3 = \frac{8\pi^3}{V}
\end{equation}
Accounting for electron spin degeneracy ($g_s = 2$), the total number of electron states $N$ within a Fermi sphere of radius $k_F$ is:
\begin{equation}
    N = 2 \times \frac{\frac{4}{3}\pi k_F^3}{\Delta V_k} = 2 \times \frac{\frac{4}{3}\pi k_F^3}{\frac{8\pi^3}{V}} = \frac{V k_F^3}{3\pi^2}
\end{equation}
The conduction electron density is $n = \frac{N}{V} = \frac{k_F^3}{3\pi^2}$, which gives the \textbf{Fermi wavevector}:
\begin{equation}
    k_F = \left(3\pi^2 n\right)^{1/3}
\end{equation}
Substituting $k_F$ into the non-relativistic parabolic energy relation $E = \frac{\hbar^2 k^2}{2m}$ yields the \textbf{Fermi Energy at $0\,\text{K}$}:
\begin{equation}
    E_F(0) = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m}\left(3\pi^2 n\right)^{2/3}
\end{equation}
To find the \textbf{Density of States (DOS)} $g(E) = \frac{dN}{dE}$, we express $N$ as a function of energy $E$:
\begin{equation}
    N(E) = \frac{V}{3\pi^2}\left(\frac{2mE}{\hbar^2}\right)^{3/2} \implies g(E) = \frac{dN}{dE} = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \sqrt{E}
\end{equation}
The per-unit-volume density of states is $\mathcal{D}(E) = \frac{g(E)}{V} = \frac{1}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}$.
\end{derivationbox}

\subsection{Key Parameters at the Fermi Surface}
From the Fermi energy $E_F$, three fundamental quantum transport metrics are defined:
\begin{enumerate}
    \item \textbf{Fermi Velocity ($v_F$):} The speed of electrons at the Fermi surface:
    \begin{equation}
        v_F = \sqrt{\frac{2E_F}{m}} = \frac{\hbar k_F}{m} = \frac{\hbar}{m}(3\pi^2 n)^{1/3} \approx 10^6\,\text{m/s}
    \end{equation}
    \item \textbf{Fermi Temperature ($T_F$):} The characteristic degeneracy temperature:
    \begin{equation}
        T_F = \frac{E_F}{k_B} \approx 10^4 - 10^5\,\text{K}
    \end{equation}
    Because $T_{\text{room}} \ll T_F$, conduction electrons in metals form a highly degenerate Fermi gas.
    \item \textbf{Average Kinetic Energy at $0\,\text{K}$ ($\langle E \rangle$):}
    \begin{equation}
        \langle E \rangle = \frac{1}{N}\int_0^{E_F} E\, g(E)\, dE = \frac{\int_0^{E_F} E^{3/2} dE}{\int_0^{E_F} E^{1/2} dE} = \frac{\frac{2}{5}E_F^{5/2}}{\frac{2}{3}E_F^{3/2}} = \frac{3}{5}E_F
    \end{equation}
\end{enumerate}

\section{Band Theory of Solids: The Kronig-Penney Model}
\subsection{Bloch's Theorem and Crystalline Potentials}
In a perfect crystalline solid, positive ions form a regular periodic array, creating a periodic electrostatic potential satisfying:
\begin{equation}
    V(\mathbf{r} + \mathbf{R}) = V(\mathbf{r})
\end{equation}
where $\mathbf{R}$ is any lattice translation vector. According to \textbf{Bloch's Theorem}, the stationary state wavefunctions $\psi_{\mathbf{k}}(\mathbf{r})$ of electrons in a periodic potential are plane waves modulated by a periodic function $u_{\mathbf{k}}(\mathbf{r})$:
\begin{equation}
    \psi_{\mathbf{k}}(\mathbf{r}) = e^{i \mathbf{k}\cdot\mathbf{r}} u_{\mathbf{k}}(\mathbf{r}) \quad \text{where } u_{\mathbf{k}}(\mathbf{r} + \mathbf{R}) = u_{\mathbf{k}}(\mathbf{r})
\end{equation}

\subsection{The 1D Kronig-Penney Model and Energy Bandgaps}
Kronig and Penney approximated the periodic crystal potential as a 1D periodic array of rectangular potential wells (depth 0, width $a$) and barriers (height $V_0$, width $b$), with lattice period $d = a+b$.

In the limit where barriers become infinitely narrow and high ($V_0 \to \infty, b \to 0$) such that the barrier strength $P = \frac{m V_0 b a}{\hbar^2}$ remains finite, matching wavefunctions and derivatives across the boundaries yields the celebrated \textbf{Kronig-Penney Dispersion Relation}:
\begin{equation}
    P \frac{\sin \alpha a}{\alpha a} + \cos \alpha a = \cos k a \quad \text{where } \alpha = \frac{\sqrt{2mE}}{\hbar}
\end{equation}

\begin{conceptbox}[Analysis of the Kronig-Penney Equation]
Since $\cos ka$ must be real and bounded between $-1$ and $+1$:
\begin{equation}
    -1 \le P \frac{\sin \alpha a}{\alpha a} + \cos \alpha a \le +1
\end{equation}
\begin{itemize}
    \item \textbf{Allowed Energy Bands:} Energies $E$ for which the function $|f(\alpha a)| \le 1$. In these bands, electrons propagate freely through the crystal without attenuation.
    \item \textbf{Forbidden Energy Gaps ($E_g$):} Energies $E$ for which $|f(\alpha a)| > 1$. In these gaps, $k$ becomes complex, causing exponential attenuation of wavefunctions. No propagating electron states exist.
    \item \textbf{Effect of Barrier Strength $P$:}
    \begin{itemize}
        \item As $P \to 0$ (free electrons), $\cos \alpha a = \cos ka \implies \alpha = k \implies E = \frac{\hbar^2 k^2}{2m}$ (continuous parabolic energy spectrum).
        \item As $P \to \infty$ (bound electrons), $\sin \alpha a = 0 \implies \alpha a = n\pi \implies E_n = \frac{n^2\pi^2\hbar^2}{2ma^2}$ (discrete atomic energy levels).
    \end{itemize}
\end{itemize}
\end{conceptbox}

\section{Effective Mass and Positive Hole Quasiparticles}
\subsection{Mathematical Derivation of Effective Mass ($m^*$)}
When an external electric or magnetic field is applied to a crystalline solid, the electron accelerates subject to both the external force and internal lattice forces. Rather than accounting for trillions of periodic ionic forces, quantum mechanics subsumes lattice interactions into an \textbf{Effective Mass} $m^*$.

\begin{derivationbox}[Derivation of the Effective Mass Tensor]
The quantum mechanical group velocity $v_g$ of an electron wavepacket is:
\begin{equation}
    v_g = \frac{d\omega}{dk} = \frac{1}{\hbar} \frac{dE}{dk}
\end{equation}
The acceleration $a$ under an external force $F_{\text{ext}} = -eE$ is:
\begin{equation}
    a = \frac{dv_g}{dt} = \frac{1}{\hbar}\frac{d}{dt}\left(\frac{dE}{dk}\right) = \frac{1}{\hbar}\frac{d^2E}{dk^2}\frac{dk}{dt}
\end{equation}
From the semi-classical equation of motion, the crystal momentum changes according to $\hbar \frac{dk}{dt} = F_{\text{ext}} \implies \frac{dk}{dt} = \frac{F_{\text{ext}}}{\hbar}$. Substituting this into the acceleration equation:
\begin{equation}
    a = \frac{1}{\hbar^2}\frac{d^2E}{dk^2} F_{\text{ext}}
\end{equation}
Comparing directly with Newton's second law, $a = \frac{F_{\text{ext}}}{m^*}$, gives the formal definition of \textbf{Effective Mass}:
\begin{equation}
    m^* = \frac{\hbar^2}{\frac{d^2E}{dk^2}}
\end{equation}
\end{derivationbox}

\subsection{Physical Interpretation Across the Brillouin Zone}
\begin{itemize}
    \item \textbf{Near the Bottom of the Conduction Band ($k \approx 0$):} Band curvature $\frac{d^2E}{dk^2} > 0 \implies m^* > 0$. The electron accelerates in the normal direction opposite to the electric field ($a = -eE/m^*$).
    \item \textbf{At the Inflection Point ($\frac{d^2E}{dk^2} = 0$):} $m^* \to \pm \infty$. The electron experiences zero net acceleration because external acceleration is exactly countered by Bragg reflection from the lattice planes.
    \item \textbf{Near the Top of the Valence Band ($k \approx \pi/a$):} Band curvature is inverted ($\frac{d^2E}{dk^2} < 0$), yielding a \textbf{negative effective mass} ($m^* < 0$). Under an electric field, the electron accelerates in the anomalous direction because Bragg reflection exceeds the external force.
    \item \textbf{The Concept of Holes:} To avoid dealing with negative mass electrons in an almost-full valence band, solid-state physics defines an equivalent positive quasiparticle called a \textbf{hole}:
    \begin{equation}
        q_h = +e, \quad m_h^* = -m_e^* > 0, \quad \mathbf{k}_h = -\mathbf{k}_e, \quad E_h = -E_e
    \end{equation}
\end{itemize}

\section{Direct vs. Indirect Bandgap Semiconductors}
Semiconductors are classified based on the alignment of their conduction band minimum (CBM) and valence band maximum (VBM) in $E$-$k$ space.

\begin{table}[htbp]
\centering
\small
\caption{Comprehensive Comparison of Direct and Indirect Bandgap Semiconductors}
\label{tab:ch1_direct_indirect}
\begin{tabularx}{\textwidth}{p{3.2cm}XX}
\toprule
\textbf{Feature} & \textbf{Direct Bandgap Semiconductor} & \textbf{Indirect Bandgap Semiconductor} \\
\midrule
\textbf{Band Alignment} & CBM and VBM occur at the exact same wavevector $\mathbf{k} = 0$ ($\Gamma$-point). & CBM and VBM occur at different wavevectors ($\mathbf{k}_{\text{CBM}} \neq \mathbf{k}_{\text{VBM}}$). \\
\textbf{Optical Recombination} & \textbf{Direct Radiative Transition:} Electron drops vertically across $E_g$, emitting a photon of energy $h\nu \approx E_g$. & \textbf{Phonon-Assisted Transition:} Requires simultaneous interaction with a lattice \textbf{phonon} ($\hbar\Omega$) to conserve momentum. \\
\textbf{Momentum Conservation} & $\Delta k = k_{\text{photon}} \approx 0$ (automatically conserved). & $\Delta k = k_{\text{phonon}} \neq 0$ (three-body collision required). \\
\textbf{Radiative Lifetime ($\tau_r$)} & Very short ($\tau_r \approx 1-10\,\text{ns}$). High quantum efficiency ($\approx 90\%$). & Very long ($\tau_r \approx 1\,\mu\text{s}-1\,\text{ms}$). Non-radiative thermal recombination dominates. \\
\textbf{Absorption Coefficient ($\alpha$)} & Very high ($\alpha \approx 10^4-10^5\,\text{cm}^{-1}$). Thin absorption layer ($1-2\,\mu\text{m}$) needed. & Moderate ($\alpha \approx 10^2-10^3\,\text{cm}^{-1}$). Requires thick wafers ($150-300\,\mu\text{m}$) for absorption. \\
\textbf{Key Materials} & $\text{GaAs}$, $\text{InP}$, $\text{GaN}$, $\text{CdTe}$, $\text{InGaAs}$, $\text{ZnO}$. & $\text{Si}$, $\text{Ge}$, $\text{AlAs}$, $\text{GaP}$, $\text{SiC}$. \\
\textbf{Primary Applications} & Light Emitting Diodes (LEDs), Laser Diodes, High-speed optical modulators, Photodetectors. & Microprocessors (CPUs/GPUs), DRAM, Power MOSFETs, Thick silicon solar panels. \\
\bottomrule
\end{tabularx}
\end{table}

\section{Carrier Transport and the Hall Effect}
\subsection{Intrinsic and Extrinsic Semiconductor Statistics}
In thermal equilibrium, the concentrations of electrons in the conduction band ($n$) and holes in the valence band ($p$) are given by integrating the product of the density of states and the Fermi-Dirac probability:
\begin{align}
    n &= N_c e^{-(E_c - E_F)/(k_B T)} \\
    p &= N_v e^{-(E_F - E_v)/(k_B T)}
\end{align}
where $N_c = 2\left(\frac{2\pi m_e^* k_B T}{h^2}\right)^{3/2}$ and $N_v = 2\left(\frac{2\pi m_h^* k_B T}{h^2}\right)^{3/2}$ are the effective density of states in the conduction and valence bands, respectively.
\begin{itemize}
    \item \textbf{Law of Mass Action:} The product $n p$ is a constant dependent only on temperature and bandgap, independent of doping concentration:
    \begin{equation}
        n p = n_i^2 = N_c N_v e^{-E_g / (k_B T)}
    \end{equation}
    where $n_i$ is the \textbf{intrinsic carrier concentration}.
    \item \textbf{Intrinsic Fermi Level ($E_{Fi}$):} In an undoped semiconductor ($n = p = n_i$):
    \begin{equation}
        E_{Fi} = \frac{E_c + E_v}{2} + \frac{3}{4} k_B T \ln\left(\frac{m_h^*}{m_e^*}\right)
    \end{equation}
    If $m_e^* \approx m_h^*$, the intrinsic Fermi level lies exactly at the center of the bandgap.
    \item \textbf{Extrinsic Doping and Fermi Level Shift:}
    \begin{itemize}
        \item In an n-type semiconductor doped with donor density $N_d$ ($n \approx N_d$):
        \begin{equation}
            E_F - E_{Fi} = k_B T \ln\left(\frac{N_d}{n_i}\right) \quad (\text{Fermi level shifts upwards towards } E_c)
        \end{equation}
        \item In a p-type semiconductor doped with acceptor density $N_a$ ($p \approx N_a$):
        \begin{equation}
            E_{Fi} - E_F = k_B T \ln\left(\frac{N_a}{n_i}\right) \quad (\text{Fermi level shifts downwards towards } E_v)
        \end{equation}
    \end{itemize}
\end{itemize}

\subsection{Drift and Diffusion Current Components}
In semiconductors, carrier transport consists of two distinct physical mechanisms:
\begin{enumerate}
    \item \textbf{Drift Current:} Movement of carriers driven by an applied electric field $\mathbf{E}$:
    \begin{equation}
        \mathbf{J}_{\text{drift}} = q(n\mu_n + p\mu_p)\mathbf{E} = \sigma \mathbf{E}
    \end{equation}
    where $\sigma = q(n\mu_n + p\mu_p)$ is the total electrical conductivity.
    \item \textbf{Diffusion Current:} Movement of carriers driven by thermal concentration gradients:
    \begin{align}
        \mathbf{J}_{n,\text{diff}} &= q D_n \frac{dn}{dx} \quad (\text{Electrons diffuse down gradient towards lower concentration}) \\
        \mathbf{J}_{p,\text{diff}} &= -q D_p \frac{dp}{dx} \quad (\text{Holes diffuse down gradient towards lower concentration})
    \end{align}
\end{enumerate}
Carrier mobilities $\mu$ and diffusion coefficients $D$ are coupled through the \textbf{Einstein Relation}:
\begin{equation}
    \frac{D_n}{\mu_n} = \frac{D_p}{\mu_p} = \frac{k_B T}{q} = V_t \approx 25.86\,\text{mV} \quad (\text{at } T = 300\,\text{K})
\end{equation}

\subsection{The Hall Effect: Mechanism, Mathematical Derivation, and Measurement}
Discovered by Edwin Hall in 1879, the Hall effect provides the definitive experimental technique for measuring majority carrier type, carrier concentration $n$, and carrier mobility $\mu$.

\begin{derivationbox}[Derivation of Hall Voltage $V_H$ and Hall Coefficient $R_H$]
Consider a rectangular semiconductor slab of length $L$ (along $x$), width $w$ (along $y$), and thickness $t$ (along $z$).
\begin{itemize}
    \item A longitudinal electric current $I_x$ flows along the $+x$-direction, corresponding to a carrier drift velocity $\mathbf{v}_d = v_x \hat{\mathbf{x}}$.
    \item A uniform transverse magnetic field $\mathbf{B} = B_z \hat{\mathbf{z}}$ is applied along the $+z$-direction.
\end{itemize}
Carriers experience a transverse magnetic Lorentz force along the $y$-axis:
\begin{equation}
    \mathbf{F}_B = q (\mathbf{v}_d \times \mathbf{B}) = q (v_x \hat{\mathbf{x}} \times B_z \hat{\mathbf{z}}) = -q v_x B_z \hat{\mathbf{y}}
\end{equation}
This force deflects charge carriers to one side face, creating a charge separation and building up an internal transverse \textbf{Hall Electric Field} $\mathbf{E}_H = E_y \hat{\mathbf{y}}$. In steady state, the electrostatic force balances the magnetic Lorentz force:
\begin{equation}
    q E_y + (-q v_x B_z) = 0 \implies E_H = E_y = v_x B_z
\end{equation}
Expressing the drift velocity $v_x$ in terms of current $I_x$ and carrier density $n$:
\begin{equation}
    I_x = J_x \cdot A = (n q v_x)(w t) \implies v_x = \frac{I_x}{n q w t}
\end{equation}
Substituting $v_x$ into the Hall field:
\begin{equation}
    E_H = \frac{I_x B_z}{n q w t}
\end{equation}
The total measurable \textbf{Hall Voltage} $V_H$ across the slab width $w$ is:
\begin{equation}
    V_H = E_H \cdot w = \frac{I_x B_z}{n q t} = \frac{I B}{n q t}
\end{equation}
The \textbf{Hall Coefficient} $R_H$ is defined as:
\begin{equation}
    R_H \equiv \frac{E_H}{J_x B_z} = \frac{1}{n q}
\end{equation}
\begin{itemize}
    \item For electrons ($q = -e$): $R_H = -\frac{1}{ne} < 0$ (Negative Hall Voltage).
    \item For holes ($q = +e$): $R_H = +\frac{1}{pe} > 0$ (Positive Hall Voltage).
\end{itemize}
The carrier \textbf{Hall Mobility} is experimentally extracted from conductivity $\sigma = n e \mu$:
\begin{equation}
    \mu = |R_H| \sigma
\end{equation}
\end{derivationbox}

\section{P-N Junction Solar Cells and Photovoltaic Energy Conversion}
\subsection{Physical Operating Mechanism}
A photovoltaic solar cell is a specialized large-area p-n junction diode designed to convert sunlight directly into electricity:
\begin{enumerate}
    \item \textbf{Photon Absorption:} Photons with energy $h\nu \ge E_g$ generate electron-hole pairs within the depletion region and within a diffusion length of the junction.
    \item \textbf{Carrier Separation:} The built-in electric field $\mathbf{E}_{bi}$ sweeps photogenerated electrons to the n-type region and holes to the p-type region.
    \item \textbf{External Power Delivery:} Accumulation of electrons on the n-side and holes on the p-side forward-biases the junction, driving a photocurrent through an external load.
\end{enumerate}

\begin{derivationbox}[Solar Cell $I$-$V$ Equation, $V_{oc}$, $I_{sc}$, $FF$, and Efficiency]
Under illumination, the net terminal current $I(V)$ delivering power to an external load at voltage $V$ is given by the superposition of light-generated short-circuit current $I_{sc}$ and forward dark diode current:
\begin{equation}
    I(V) = I_{sc} - I_0 \left(e^{\frac{qV}{\eta k_B T}} - 1\right)
\end{equation}
where $I_0$ is the reverse saturation current, $\eta$ is the ideality factor, and $V_t = \frac{k_B T}{q} \approx 25.86\,\text{mV}$ at $300\,\text{K}$.

\begin{itemize}
    \item \textbf{Short-Circuit Current ($I_{sc}$):} Obtained at terminal voltage $V = 0$:
    \begin{equation}
        I(0) = I_{sc}
    \end{equation}
    $I_{sc}$ scales linearly with incident solar irradiance $G$ ($\text{W/m}^2$).
    \item \textbf{Open-Circuit Voltage ($V_{oc}$):} Obtained when the external load is disconnected ($I = 0$):
    \begin{equation}
        0 = I_{sc} - I_0 \left(e^{\frac{qV_{oc}}{\eta k_B T}} - 1\right) \implies V_{oc} = \frac{\eta k_B T}{q} \ln\left(\frac{I_{sc}}{I_0} + 1\right) \approx V_t \ln\left(\frac{I_{sc}}{I_0}\right)
    \end{equation}
    \item \textbf{Maximum Power Point ($P_{max}$) and Fill Factor ($FF$):}
    Electrical power delivered is $P(V) = I(V) \cdot V$. At the optimum operating point $(V_m, I_m)$, power reaches its maximum:
    \begin{equation}
        P_{max} = V_m I_m
    \end{equation}
    The \textbf{Fill Factor} ($FF$) measures the ideality and sharpness of the solar cell $I$-$V$ curve:
    \begin{equation}
        FF = \frac{P_{max}}{V_{oc} I_{sc}} = \frac{V_m I_m}{V_{oc} I_{sc}} \quad (0.70 \le FF \le 0.85 \text{ for high-quality Si})
    \end{equation}
    \item \textbf{Power Conversion Efficiency ($\eta_{eff}$):}
    For total incident optical power $P_{in} = G \cdot A_{\text{cell}}$:
    \begin{equation}
        \eta_{eff} = \frac{P_{max}}{P_{in}} \times 100\% = \frac{FF \cdot V_{oc} \cdot I_{sc}}{P_{in}} \times 100\%
    \end{equation}
\end{itemize}
\end{derivationbox}

\subsection{Loss Mechanisms and Anti-Reflective Coating (ARC)}
\begin{enumerate}
    \item \textbf{Parasitic Resistances:}
    \begin{itemize}
        \item \textbf{Series Resistance ($R_s$):} Originates from bulk semiconductor resistivity and metallic contact grid contact resistance. Reduces the Fill Factor and short-circuit current.
        \item \textbf{Shunt Resistance ($R_{sh}$):} Originates from crystal defects and edge leakage paths across the p-n junction. Reduces open-circuit voltage $V_{oc}$.
    \end{itemize}
    \item \textbf{Anti-Reflective Coating (ARC):} Bare polished silicon reflects over $30\%$ of incident sunlight due to high refractive index ($n_{Si} \approx 3.8$). Depositing a dielectric thin film (e.g., $\text{Si}_3\text{N}_4$, $n_{ARC} \approx 2.05$) of optical thickness $\lambda/4$ creates destructive interference between front and back reflected waves:
    \begin{equation}
        n_{ARC} = \sqrt{n_{\text{air}} \cdot n_{Si}} = \sqrt{1 \times 3.8} \approx 1.95, \quad d_{ARC} = \frac{\lambda_0}{4 n_{ARC}}
    \end{equation}
    For center solar wavelength $\lambda_0 = 600\,\text{nm}$, $d_{ARC} \approx \frac{600}{4(2.0)} = 75\,\text{nm}$.
\end{enumerate}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 1.1: Complete Quantum Parameters of Metallic Sodium]
\textbf{Problem:} Metallic Sodium has a BCC crystal structure with lattice constant $a = 4.29\,\text{\AA}$ and one valence electron per atom ($n = 2.65 \times 10^{28}\,\text{m}^{-3}$).
\begin{enumerate}[label=(\alph*)]
    \item Compute the Fermi wavevector $k_F$, Fermi momentum $p_F$, and Fermi energy $E_F(0)$ in eV.
    \item Calculate the Fermi velocity $v_F$, Fermi temperature $T_F$, and average electronic energy $\langle E \rangle$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Fermi Wavevector:}
    \begin{equation}
        k_F = (3\pi^2 n)^{1/3} = \left(3\pi^2 \times 2.65 \times 10^{28}\right)^{1/3} = (7.846 \times 10^{29})^{1/3} = \mathbf{9.22 \times 10^9\,\text{m}^{-1}}
    \end{equation}
    \textbf{Fermi Momentum:}
    \begin{equation}
        p_F = \hbar k_F = (1.0546 \times 10^{-34}\,\text{J}\cdot\text{s})(9.22 \times 10^9\,\text{m}^{-1}) = \mathbf{9.72 \times 10^{-25}\,\text{kg}\cdot\text{m/s}}
    \end{equation}
    \textbf{Fermi Energy:}
    \begin{align}
        E_F(0) &= \frac{\hbar^2 k_F^2}{2m} = \frac{(1.0546 \times 10^{-34})^2 (9.22 \times 10^9)^2}{2(9.109 \times 10^{-31})} = \frac{1.1122 \times 10^{-67} \times 8.50 \times 10^{19}}{1.8218 \times 10^{-30}} \\
        &= 5.19 \times 10^{-19}\,\text{J} = \frac{5.19 \times 10^{-19}}{1.602 \times 10^{-19}}\,\text{eV} = \mathbf{3.24\,\text{eV}}
    \end{align}
    \item \textbf{Fermi Velocity, Temperature, and Average Energy:}
    \begin{align}
        v_F &= \sqrt{\frac{2E_F}{m}} = \sqrt{\frac{2(5.19 \times 10^{-19})}{9.109 \times 10^{-31}}} = \sqrt{1.139 \times 10^{12}} = \mathbf{1.07 \times 10^6\,\text{m/s}} \\
        T_F &= \frac{E_F}{k_B} = \frac{5.19 \times 10^{-19}\,\text{J}}{1.3806 \times 10^{-23}\,\text{J/K}} = \mathbf{37{,}592\,\text{K}} \\
        \langle E \rangle &= \frac{3}{5}E_F = 0.6 \times 3.24\,\text{eV} = \mathbf{1.94\,\text{eV}}
    \end{align}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 1.2: Effective Mass from Energy-Wavevector Dispersion]
\textbf{Problem:} In a 1D crystal lattice with lattice constant $a = 3.0\,\text{\AA}$, the energy dispersion relation near the band edge is given by $E(k) = E_0 - 2\gamma \cos(ka)$, where $\gamma = 1.20\,\text{eV}$.
\begin{enumerate}[label=(\alph*)]
    \item Derive the expression for group velocity $v_g(k)$ and effective mass $m^*(k)$.
    \item Evaluate the effective mass at the band bottom ($k = 0$) and at the band top ($k = \pi/a$). Express results as multiples of the free electron mass $m_0 = 9.109 \times 10^{-31}\,\text{kg}$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item Differentiating $E(k)$ with respect to $k$:
    \begin{align}
        \frac{dE}{dk} &= \frac{d}{dk}[E_0 - 2\gamma \cos(ka)] = 2\gamma a \sin(ka) \implies v_g = \frac{1}{\hbar}\frac{dE}{dk} = \frac{2\gamma a}{\hbar}\sin(ka) \\
        \frac{d^2E}{dk^2} &= 2\gamma a^2 \cos(ka) \implies m^*(k) = \frac{\hbar^2}{\frac{d^2E}{dk^2}} = \frac{\hbar^2}{2\gamma a^2 \cos(ka)}
    \end{align}
    \item \textbf{At the Band Bottom ($k = 0$):}
    \begin{equation}
        \cos(0) = 1 \implies m^*(0) = \frac{\hbar^2}{2\gamma a^2}
    \end{equation}
    Converting $\gamma = 1.20\,\text{eV} = 1.20 \times 1.602 \times 10^{-19}\,\text{J} = 1.922 \times 10^{-19}\,\text{J}$, and $a = 3.0 \times 10^{-10}\,\text{m}$:
    \begin{align}
        m^*(0) &= \frac{(1.0546 \times 10^{-34})^2}{2(1.922 \times 10^{-19})(3.0 \times 10^{-10})^2} = \frac{1.1122 \times 10^{-67}}{3.460 \times 10^{-37}} = 3.214 \times 10^{-31}\,\text{kg} \\
        \frac{m^*(0)}{m_0} &= \frac{3.214 \times 10^{-31}}{9.109 \times 10^{-31}} = \mathbf{+0.353\,m_0} \quad (\text{Positive effective mass})
    \end{align}
    \textbf{At the Band Top ($k = \pi/a$):}
    \begin{equation}
        \cos(\pi) = -1 \implies m^*(\pi/a) = -\frac{\hbar^2}{2\gamma a^2} = -\mathbf{0.353\,m_0} \quad (\text{Hole mass } m_h^* = +0.353\,m_0)
    \end{equation}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 1.3: Hall Effect Analysis on p-type Germanium]
\textbf{Problem:} A p-type Germanium wafer of width $w = 3.0\,\text{mm}$ and thickness $t = 0.50\,\text{mm}$ carries a current of $I = 20.0\,\text{mA}$ in a magnetic field $B = 0.80\,\text{T}$. A positive Hall voltage of $V_H = +6.40\,\text{mV}$ is measured. The wafer's electrical conductivity is $\sigma = 320\,\Omega^{-1}\text{m}^{-1}$.
\begin{enumerate}[label=(\alph*)]
    \item Determine majority carrier type and concentration $p$.
    \item Calculate the Hall coefficient $R_H$ and hole mobility $\mu_p$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item The positive Hall voltage confirms majority carriers are \textbf{holes} ($p$-type).
    Using $V_H = \frac{I B}{p e t}$:
    \begin{align}
        p &= \frac{I B}{e t V_H} = \frac{(20.0 \times 10^{-3}\,\text{A})(0.80\,\text{T})}{(1.602 \times 10^{-19}\,\text{C})(0.50 \times 10^{-3}\,\text{m})(6.40 \times 10^{-3}\,\text{V})} \\
        &= \frac{1.60 \times 10^{-2}}{5.126 \times 10^{-25}} = \mathbf{3.12 \times 10^{22}\,\text{m}^{-3}}
    \end{align}
    \item \textbf{Hall Coefficient:}
    \begin{equation}
        R_H = +\frac{1}{p e} = \frac{1}{(3.12 \times 10^{22})(1.602 \times 10^{-19})} = +\mathbf{0.200\,\text{m}^3/\text{C}}
    \end{equation}
    \textbf{Hole Mobility:}
    \begin{equation}
        \mu_p = R_H \sigma = (0.200\,\text{m}^3/\text{C})(320\,\Omega^{-1}\text{m}^{-1}) = \mathbf{0.064\,\text{m}^2/(\text{V}\cdot\text{s})} = 640\,\text{cm}^2/(\text{V}\cdot\text{s})
    \end{equation}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 1.4: Silicon Solar Cell Efficiency and Fill Factor Analysis]
\textbf{Problem:} A silicon photovoltaic cell of active area $25.0\,\text{cm}^2$ is tested under AM1.5 standard solar irradiance ($G = 1000\,\text{W/m}^2$). The cell parameters are $I_{sc} = 850\,\text{mA}$, $I_0 = 1.50 \times 10^{-10}\,\text{A}$, ideality factor $\eta = 1.05$, and temperature $T = 300\,\text{K}$ ($V_t = 25.86\,\text{mV}$). The maximum power point is reached at $V_m = 0.530\,\text{V}$ and $I_m = 790\,\text{mA}$.
\begin{enumerate}[label=(\alph*)]
    \item Compute the open-circuit voltage $V_{oc}$.
    \item Determine the maximum electrical power $P_{max}$, fill factor $FF$, and efficiency $\eta_{eff}$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Open-Circuit Voltage:}
    \begin{align}
        V_{oc} &= \eta V_t \ln\left(\frac{I_{sc}}{I_0} + 1\right) = (1.05)(0.02586)\ln\left(\frac{0.850}{1.50 \times 10^{-10}} + 1\right) \\
        &= 0.02715 \times \ln(5.667 \times 10^9) = 0.02715 \times 22.457 = \mathbf{0.610\,\text{V}}
    \end{align}
    \item \textbf{Maximum Power, Fill Factor, and Efficiency:}
    \begin{align}
        P_{max} &= V_m I_m = (0.530\,\text{V})(0.790\,\text{A}) = \mathbf{0.4187\,\text{W}} = 418.7\,\text{mW} \\
        P_{\text{ideal}} &= V_{oc} I_{sc} = (0.610\,\text{V})(0.850\,\text{A}) = 0.5185\,\text{W} \\
        FF &= \frac{P_{max}}{V_{oc} I_{sc}} = \frac{0.4187}{0.5185} = \mathbf{0.8075} \quad (80.75\%)
    \end{align}
    Incident solar power: $P_{in} = G \cdot A = (1000\,\text{W/m}^2)(25.0 \times 10^{-4}\,\text{m}^2) = 2.50\,\text{W}$.
    \begin{equation}
        \eta_{eff} = \frac{P_{max}}{P_{in}} \times 100\% = \frac{0.4187\,\text{W}}{2.50\,\text{W}} \times 100\% = \mathbf{16.75\%}
    \end{equation}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 1.5: Carrier Concentration and Fermi Level in Doped Silicon]
\textbf{Problem:} Silicon at $T = 300\,\text{K}$ has $n_i = 1.5 \times 10^{10}\,\text{cm}^{-3}$ and is doped with Boron (acceptor) at a density of $N_a = 5.0 \times 10^{16}\,\text{cm}^{-3}$. Given $k_BT = 0.0259\,\text{eV}$:
\begin{enumerate}[label=(\alph*)]
    \item Calculate the thermal equilibrium majority hole concentration $p$ and minority electron concentration $n$.
    \item Determine the position of the Fermi level $E_F$ relative to the intrinsic Fermi level $E_{Fi}$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item At room temperature, assuming complete ionization ($p \approx N_a = \mathbf{5.0 \times 10^{16}\,\text{cm}^{-3}}$):
    Using the Law of Mass Action ($n p = n_i^2$):
    \begin{equation}
        n = \frac{n_i^2}{p} = \frac{(1.5 \times 10^{10})^2}{5.0 \times 10^{16}} = \frac{2.25 \times 10^{20}}{5.0 \times 10^{16}} = \mathbf{4.50 \times 10^3\,\text{cm}^{-3}}
    \end{equation}
    \item The shift of the Fermi level relative to $E_{Fi}$ is:
    \begin{equation}
        E_{Fi} - E_F = k_B T \ln\left(\frac{N_a}{n_i}\right) = 0.0259\,\text{eV} \times \ln\left(\frac{5.0 \times 10^{16}}{1.5 \times 10^{10}}\right) = 0.0259 \times \ln(3.333 \times 10^6) = 0.0259 \times 15.019 = \mathbf{0.389\,\text{eV}}
    \end{equation}
    The Fermi level is situated $0.389\,\text{eV}$ below the intrinsic Fermi level (towards the valence band).
\end{enumerate}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Drude Conductivity:} $\sigma = \frac{n e^2 \tau}{m}$. Classical equipartition fails drastically for electronic heat capacity ($C_{v,el} \ll \frac{3}{2}R$).
    \item \textbf{Sommerfeld Quantum Model:} Electrons obey Fermi-Dirac statistics $f(E) = \frac{1}{e^{(E-E_F)/k_BT} + 1}$. The Fermi energy at $0\,\text{K}$ is $E_F(0) = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$.
    \item \textbf{Kronig-Penney Band Theory:} Periodic crystal potentials create alternating allowed energy bands and forbidden energy bandgaps $E_g$.
    \item \textbf{Effective Mass:} $m^* = \frac{\hbar^2}{d^2E/dk^2}$. Near valence band extrema, downward curvature creates negative effective mass, giving rise to positive hole transport ($q_h = +e, m_h^* > 0$).
    \item \textbf{Direct vs. Indirect Semiconductors:} Direct bandgap semiconductors ($\text{GaAs}, \text{InP}$) emit photons efficiently without phonons, making them ideal for optoelectronics; indirect semiconductors ($\text{Si}, \text{Ge}$) require phonon participation.
    \item \textbf{Hall Effect:} $V_H = \frac{IB}{nqt}$ and $R_H = \frac{1}{nq}$. A negative $R_H$ indicates electron conduction; a positive $R_H$ indicates hole conduction.
    \item \textbf{Solar Cells:} Photovoltaic efficiency is $\eta_{eff} = \frac{FF \cdot V_{oc} I_{sc}}{P_{in}}$, where $FF = \frac{V_m I_m}{V_{oc} I_{sc}}$ and $V_{oc} = \frac{\eta k_BT}{q}\ln\left(\frac{I_{sc}}{I_0} + 1\right)$.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-01-solid-state-physics.tex", "w") as f:
    f.write(ch1)

print("Chapter 1 expanded successfully.")

# ==============================================================================
# CHAPTER 2: EXPANDED ELECTRICITY AND CIRCUIT DEVICES
# ==============================================================================
ch2 = r"""\chapter{Fundamentals of Electricity and Circuit Devices}
\label{chap:electricity_devices}

\section{Introduction and Overview}
Electrical circuit theory and modern semiconductor devices form the physical backbone of all modern computing and communication systems. In this chapter, we bridge fundamental electric circuit laws (Ohm's law, KCL, KVL) with nonlinear semiconductor devices (PN diodes, bridge rectifiers, BJTs, CMOS logic), state-of-the-art memory architectures (SRAM, DRAM, SSD Flash), AI hardware acceleration models (Roofline analysis), IoT networking subnetting, and fiber-optic physical layer communications.

\section{Fundamental Circuit Laws and Network Analysis}
\subsection{Ohm's Law, KCL, and KVL}
\begin{definitionbox}[Core Circuit Laws]
\begin{enumerate}
    \item \textbf{Ohm's Law:} The current $I$ flowing through an ideal linear conductor is directly proportional to the potential difference $V$ across it at constant temperature:
    \begin{equation}
        V = I R \quad \text{or} \quad \mathbf{J} = \sigma \mathbf{E}
    \end{equation}
    \item \textbf{Kirchhoff's Current Law (KCL):} Based on the \textbf{Conservation of Electric Charge}, the algebraic sum of all currents entering and leaving any circuit node is identically zero:
    \begin{equation}
        \sum_{k=1}^N I_k = 0 \implies \sum I_{\text{entering}} = \sum I_{\text{leaving}}
    \end{equation}
    \item \textbf{Kirchhoff's Voltage Law (KVL):} Based on the \textbf{Conservation of Energy}, the algebraic sum of all electric potential differences (voltages) around any closed loop in a circuit is identically zero:
    \begin{equation}
        \sum_{k=1}^M V_k = 0 \implies \sum V_{\text{rises}} = \sum V_{\text{drops}}
    \end{equation}
\end{enumerate}
\end{definitionbox}

\subsection{Systematic Node-Voltage and Mesh-Current Analysis}
\begin{enumerate}
    \item \textbf{Nodal Analysis:} Select a reference (ground) node ($0\,\text{V}$). Apply KCL at each non-reference node $k$:
    \begin{equation}
        \sum_{j \neq k} \frac{V_k - V_j}{R_{kj}} = I_{\text{source}, k}
    \end{equation}
    In matrix form for $n$ independent nodes:
    \begin{equation}
        \begin{bmatrix} G_{11} & G_{12} & \dots & G_{1n} \\ G_{21} & G_{22} & \dots & G_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ G_{n1} & G_{n2} & \dots & G_{nn} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_n \end{bmatrix} = \begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_n \end{bmatrix}
    \end{equation}
    where $G_{ii}$ is the sum of conductances connected to node $i$, and $G_{ij} = -1/R_{ij}$ is the mutual conductance between nodes $i$ and $j$.
    \item \textbf{Mesh Analysis:} Assign clockwise mesh currents $I_1, I_2, \dots, I_m$ to each planar loop. Apply KVL around each mesh:
    \begin{equation}
        \begin{bmatrix} R_{11} & R_{12} & \dots & R_{1m} \\ R_{21} & R_{22} & \dots & R_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ R_{m1} & R_{m2} & \dots & R_{mm} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_m \end{bmatrix} = \begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_m \end{bmatrix}
    \end{equation}
\end{enumerate}

\subsection{Voltage and Current Division Principles}
\begin{itemize}
    \item \textbf{Voltage Division (Series Resistors):} For $N$ resistors connected in series across total voltage $V_{total}$:
    \begin{equation}
        V_k = V_{total} \left(\frac{R_k}{\sum_{i=1}^N R_i}\right)
    \end{equation}
    \item \textbf{Current Division (Parallel Resistors):} For two parallel branches $R_1, R_2$ carrying total input current $I_{total}$:
    \begin{equation}
        I_1 = I_{total} \left(\frac{R_2}{R_1 + R_2}\right), \quad I_2 = I_{total} \left(\frac{R_1}{R_1 + R_2}\right)
    \end{equation}
\end{itemize}

\section{Semiconductor Diodes and Power Rectifier Circuits}
\subsection{The PN Junction Diode and Shockley Equation}
A PN junction consists of adjoining p-type and n-type semiconductor regions. Thermal diffusion of majority carriers creates a \textbf{depletion region} with uncompensated ionized dopants, creating a built-in potential barrier $V_{bi} \approx 0.7\,\text{V}$ (for Silicon) or $0.3\,\text{V}$ (for Germanium).

The current-voltage relationship is described by the \textbf{Shockley Ideal Diode Equation}:
\begin{equation}
    I_D = I_s \left(e^{\frac{V_D}{\eta V_t}} - 1\right)
\end{equation}
where $I_s$ is reverse saturation current, $\eta$ is ideality factor ($1 \le \eta \le 2$), and $V_t = \frac{k_BT}{q} \approx 25.86\,\text{mV}$ at $300\,\text{K}$.

\subsection{Full-Wave Bridge Rectifier with Capacitor Filter}
A full-wave bridge rectifier employs four diodes in a closed ring configuration to convert AC voltage $v_{in}(t) = V_m \sin(\omega t)$ into pulsating DC.

\begin{table}[htbp]
\centering
\small
\caption{Comparison of Rectifier Circuit Topologies}
\label{tab:rectifiers}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Parameter} & \textbf{Half-Wave Rectifier} & \textbf{Center-Tapped Full-Wave} & \textbf{Bridge Rectifier} \\
\midrule
\textbf{Number of Diodes} & 1 & 2 & 4 \\
\textbf{DC Output Voltage ($V_{dc}$)} & $\frac{V_m}{\pi} \approx 0.318 V_m$ & $\frac{2V_m}{\pi} \approx 0.636 V_m$ & $\frac{2V_m}{\pi} \approx 0.636 V_m$ \\
\textbf{RMS Output Voltage ($V_{rms}$)} & $\frac{V_m}{2} = 0.5 V_m$ & $\frac{V_m}{\sqrt{2}} \approx 0.707 V_m$ & $\frac{V_m}{\sqrt{2}} \approx 0.707 V_m$ \\
\textbf{Rectification Efficiency ($\eta$)} & $40.6\%$ & $81.2\%$ & $81.2\%$ \\
\textbf{Ripple Frequency ($f_r$)} & $f_{in}$ ($50\,\text{Hz}$) & $2 f_{in}$ ($100\,\text{Hz}$) & $2 f_{in}$ ($100\,\text{Hz}$) \\
\textbf{Ripple Factor ($\gamma$) without filter} & $1.21$ & $0.482$ & $0.482$ \\
\textbf{Peak Inverse Voltage (PIV)} & $V_m$ & $2 V_m$ & $V_m$ \\
\textbf{Transformer Utilization Factor} & $0.287$ & $0.693$ & $0.812$ \\
\bottomrule
\end{tabularx}
\end{table}

\begin{derivationbox}[Capacitor Filter Ripple Factor ($\gamma$) and Peak-to-Peak Ripple Voltage ($V_{r(pp)}$)]
Connecting a large smoothing capacitor $C$ in parallel with load resistor $R_L$:
\begin{itemize}
    \item The capacitor charges to peak voltage $V_{peak} = V_m - 2V_D$ (for bridge rectifier).
    \item During the interval between peaks ($T_r = \frac{1}{2f}$), the capacitor discharges through load $R_L$: $v(t) \approx V_{peak} e^{-t/(R_L C)} \approx V_{peak}\left(1 - \frac{t}{R_L C}\right)$.
\end{itemize}
The total charge lost during discharge time $T_r \approx \frac{1}{2f}$ is:
\begin{equation}
    \Delta Q = I_{dc} T_r = \frac{I_{dc}}{2f} = C V_{r(pp)} \implies V_{r(pp)} = \frac{I_{dc}}{2 f C} = \frac{V_{peak}}{2 f C R_L}
\end{equation}
Approximating the ripple waveform as a triangular wave of peak-to-peak amplitude $V_{r(pp)}$:
\begin{equation}
    V_{r,rms} = \frac{V_{r(pp)}}{2\sqrt{3}} = \frac{V_{peak}}{4\sqrt{3} f C R_L}
\end{equation}
The DC output voltage is $V_{dc} = V_{peak} - \frac{V_{r(pp)}}{2} \approx V_{peak}$. The \textbf{Ripple Factor} $\gamma$ is:
\begin{equation}
    \gamma \equiv \frac{V_{r,rms}}{V_{dc}} = \frac{\frac{V_{peak}}{4\sqrt{3} f C R_L}}{V_{peak}} = \frac{1}{4\sqrt{3} f C R_L}
\end{equation}
\end{derivationbox}

\section{Bipolar Junction Transistors (BJT): Operation, Biasing, and Stability}
\subsection{Physical Structure and Current Relations}
A BJT consists of two back-to-back PN junctions forming three terminals: \textbf{Emitter (E)} (heavily doped), \textbf{Base (B)} (ultra-thin, lightly doped), and \textbf{Collector (C)} (moderately doped, large area for heat dissipation).

\begin{equation}
    I_E = I_B + I_C
\end{equation}
\begin{itemize}
    \item \textbf{Common Base Current Gain ($\alpha$):} $\alpha = \frac{I_C}{I_E} \approx 0.95 - 0.998$.
    \item \textbf{Common Emitter Current Gain ($\beta$):} $\beta = \frac{I_C}{I_B} \approx 50 - 500$.
    \item Mathematical relationship:
    \begin{equation}
        \beta = \frac{\alpha}{1 - \alpha}, \quad \alpha = \frac{\beta}{\beta + 1}
    \end{equation}
\end{itemize}

\subsection{BJT Operating Regions and DC Load Line Analysis}
\begin{table}[htbp]
\centering
\small
\caption{BJT Operating Modes and Junction Biasing}
\label{tab:bjt_modes}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Operating Region} & \textbf{Emitter-Base (EBJ)} & \textbf{Collector-Base (CBJ)} & \textbf{Primary Application} \\
\midrule
\textbf{Cutoff} & Reverse Biased & Reverse Biased & Digital OFF Switch ($I_C \approx 0, V_{CE} \approx V_{CC}$) \\
\textbf{Active (Forward-Active)} & Forward Biased & Reverse Biased & Linear Analog Amplifier ($I_C = \beta I_B$) \\
\textbf{Saturation} & Forward Biased & Forward Biased & Digital ON Switch ($V_{CE,\text{sat}} \approx 0.2\,\text{V}$) \\
\textbf{Reverse Active} & Reverse Biased & Forward Biased & Specialized TTL logic switches (low gain) \\
\bottomrule
\end{tabularx}
\end{table}

\begin{derivationbox}[DC Load Line and $Q$-Point Determination in Common Emitter]
In a Common Emitter circuit with supply $V_{CC}$ and collector resistor $R_C$:
Applying KVL to the collector-emitter loop:
\begin{equation}
    V_{CC} - I_C R_C - V_{CE} = 0 \implies I_C = -\frac{1}{R_C} V_{CE} + \frac{V_{CC}}{R_C}
\end{equation}
This represents a straight line with slope $-1/R_C$ on the $I_C$-$V_{CE}$ output characteristics:
\begin{itemize}
    \item \textbf{Cutoff Point ($I_C = 0$):} $V_{CE} = V_{CC}$.
    \item \textbf{Saturation Point ($V_{CE} = 0$):} $I_{C,\text{sat}} = \frac{V_{CC}}{R_C}$.
    \item \textbf{Quiescent Operating Point ($Q$-Point):} The intersection of the DC load line with the specific base current curve $I_B$:
    \begin{equation}
        Q = (V_{CEQ}, I_{CQ})
    \end{equation}
\end{itemize}
\end{derivationbox}

\subsection{Bias Stabilization and Stability Factors}
To prevent thermal runaway (where temperature increase elevates $I_{CO}$, which elevates $I_C$, further heating the junction until destruction), biasing circuits are rated by the \textbf{Stability Factor} $S$:
\begin{equation}
    S \equiv \frac{\partial I_C}{\partial I_{CO}} = \frac{1 + \beta}{1 - \beta \left(\frac{\partial I_B}{\partial I_C}\right)}
\end{equation}
\begin{itemize}
    \item \textbf{Fixed Bias Circuit:} $I_B = \frac{V_{CC} - V_{BE}}{R_B} \implies \frac{\partial I_B}{\partial I_C} = 0 \implies S = 1 + \beta$ (Extremely poor thermal stability).
    \item \textbf{Voltage Divider Bias with Emitter Resistor $R_E$:}
    \begin{equation}
        S = (1 + \beta) \frac{1 + \frac{R_{TH}}{R_E}}{1 + \beta + \frac{R_{TH}}{R_E}} \approx 1 + \frac{R_{TH}}{R_E} \quad (\text{if } R_{TH} \ll \beta R_E)
    \end{equation}
    Selecting $R_{TH} \le 0.1 \beta R_E$ establishes near-perfect stability ($S \to 1$), making the $Q$-point virtually independent of transistor $\beta$ and temperature.
\end{itemize}

\section{CMOS Digital Integrated Circuits and Power Dissipation}
\subsection{CMOS Inverter Operation and Voltage Transfer Characteristics (VTC)}
Complementary Metal-Oxide-Semiconductor (CMOS) logic integrates complementary pairs of p-channel (PMOS) and n-channel (NMOS) MOSFETs.
\begin{itemize}
    \item When input $V_{in} = \text{LOW} (0\,\text{V})$: PMOS is ON (pulls output to $V_{DD}$), NMOS is OFF. Output $V_{out} = V_{DD}$ (\textbf{HIGH}).
    \item When input $V_{in} = \text{HIGH} (V_{DD})$: PMOS is OFF, NMOS is ON (pulls output to $\text{GND}$). Output $V_{out} = 0\,\text{V}$ (\textbf{LOW}).
    \item \textbf{Noise Margins:}
    \begin{align}
        NM_H &= V_{OH} - V_{IH} = V_{DD} - V_{IH} \\
        NM_L &= V_{IL} - V_{OL} = V_{IL} - 0 = V_{IL}
    \end{align}
\end{itemize}

\begin{derivationbox}[CMOS Dynamic Power Dissipation Derivation]
When the CMOS inverter transitions from LOW to HIGH, energy drawn from the power supply $V_{DD}$ to charge the total output load capacitance $C_L$ is:
\begin{equation}
    E_{\text{supply}} = \int_0^\infty i(t) V_{DD} dt = V_{DD} \int_0^\infty i(t) dt = V_{DD} Q = C_L V_{DD}^2
\end{equation}
Energy stored in capacitor: $E_{\text{cap}} = \frac{1}{2} C_L V_{DD}^2$. The remaining $\frac{1}{2} C_L V_{DD}^2$ is dissipated as heat in the PMOS transistor.
During the HIGH-to-LOW transition, the capacitor discharges through NMOS to ground, dissipating the stored $\frac{1}{2} C_L V_{DD}^2$.
Total energy dissipated per full clock cycle ($0 \to 1 \to 0$) is:
\begin{equation}
    E_{\text{cycle}} = C_L V_{DD}^2
\end{equation}
For clock frequency $f$ and switching activity factor $\alpha$ ($0 \le \alpha \le 1$):
\begin{equation}
    P_{\text{dynamic}} = \alpha C_L V_{DD}^2 f
\end{equation}
Total CMOS power dissipation is the sum of dynamic and static leakage power:
\begin{equation}
    P_{\text{total}} = \alpha C_L V_{DD}^2 f + V_{DD} I_{\text{leakage}}
\end{equation}
\end{derivationbox}

\section{Semiconductor Memory Technologies and AI Hardware Accelerators}
\subsection{SRAM vs. DRAM vs. Flash SSD Memory}
\begin{table}[htbp]
\centering
\small
\caption{Comparison of Primary Semiconductor Memory Technologies}
\label{tab:memory_technologies}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Feature} & \textbf{SRAM (Static RAM)} & \textbf{DRAM (Dynamic RAM)} & \textbf{Flash SSD (NAND)} \\
\midrule
\textbf{Cell Architecture} & 6-Transistor (6T) cross-coupled CMOS latch & 1-Transistor 1-Capacitor (1T1C) cell & Floating-Gate MOSFET / 3D Charge-Trap NAND \\
\textbf{Storage Mechanism} & Bistable latch state ($Q, \bar{Q}$) & Capacitor charge ($Q = C V$) & Trapped tunneling electrons in floating gate \\
\textbf{Volatility} & Volatile (loses data on power down) & Volatile (requires periodic refresh $\sim 64\,\text{ms}$) & Non-Volatile (retains data without power) \\
\textbf{Access Latency} & Ultra-fast ($0.5 - 2\,\text{ns}$) & Fast ($10 - 20\,\text{ns}$) & Moderate/Slow ($10 - 100\,\mu\text{s}$) \\
\textbf{Integration Density} & Low (large cell area) & High ($1$ cell per bit) & Ultra-High (multi-layer 3D stacking) \\
\textbf{Cost per Bit} & Highest & Moderate & Lowest \\
\textbf{Primary Role} & CPU L1/L2/L3 On-chip Cache & Main System Memory (DDR5) & Secondary Storage, NVMe Solid State Drives \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{AI Hardware Accelerators and the Roofline Performance Model}
Modern deep learning workloads (Transformer attention, Convolutional GEMM matrix multiplications) require trillions of Multiply-Accumulate (MAC) operations.
\begin{itemize}
    \item \textbf{Systolic Arrays (Google TPU):} A 2D grid of processing elements (PEs) that stream weights and data rhythmically across adjacent registers without fetching from memory every step, dramatically lowering energy consumption.
    \item \textbf{Roofline Performance Model:} Characterizes processor operational throughput ($P$, in $\text{TFLOP/s}$) as a function of \textbf{Arithmetic Intensity} ($I$, in $\text{FLOPs/byte}$):
    \begin{equation}
        P = \min\left(P_{\text{peak}}, I \times \text{Bandwidth}_{\text{memory}}\right)
    \end{equation}
    \begin{itemize}
        \item \textbf{Memory-Bound Regime ($I < I_{\text{knee}}$):} Performance is limited by memory bandwidth ($P = I \times \text{BW}$).
        \item \textbf{Compute-Bound Regime ($I \ge I_{\text{knee}}$):} Performance saturates at hardware peak compute capacity $P_{\text{peak}}$.
    \end{itemize}
\end{itemize}

\section{IoT Sensors, IPv4 Subnetting, and Optical Fiber Communications}
\subsection{IPv4 Network Subnetting Fundamentals}
In modern IoT architectures, sensor nodes are organized into IP subnetworks. For a `/27` CIDR prefix:
\begin{itemize}
    \item \textbf{Subnet Mask:} $27$ network bits $\implies 255.255.255.224$ (Binary: $11111111.11111111.11111111.11100000$).
    \item \textbf{Host Bits:} $32 - 27 = 5$ host bits.
    \item \textbf{Total IP Addresses per Subnet:} $2^5 = 32$.
    \item \textbf{Usable Host Addresses:} $2^5 - 2 = 30$ (subtracting Network ID and Broadcast address).
\end{itemize}

\subsection{Optical Fiber Physics: Total Internal Reflection, Dispersion, and Attenuation}
Optical fibers guide light signals over long distances with minimal attenuation via \textbf{Total Internal Reflection (TIR)} at the core-cladding interface.
\begin{itemize}
    \item Refractive index condition: Core index $n_1 >$ Cladding index $n_2$.
    \item \textbf{Critical Angle ($\theta_c$):} From Snell's law ($n_1 \sin \theta_c = n_2 \sin 90^\circ$):
    \begin{equation}
        \sin \theta_c = \frac{n_2}{n_1} \implies \theta_c = \arcsin\left(\frac{n_2}{n_1}\right)
    \end{equation}
    \item \textbf{Acceptance Angle ($\theta_a$) and Numerical Aperture ($\text{NA}$):} The maximum cone of incident light accepted into the core from air ($n_0 = 1$):
    \begin{equation}
        \text{NA} = \sin \theta_a = \sqrt{n_1^2 - n_2^2}
    \end{equation}
    \item \textbf{Intermodal Dispersion in Step-Index Fibers:} Light rays traveling along different zig-zag paths arrive at different times. The pulse broadening $\Delta t_{\text{modal}}$ over fiber length $L$ is:
    \begin{equation}
        \Delta t_{\text{modal}} = \frac{L}{c/n_1}\left(\frac{1}{\sin \theta_c} - 1\right) = \frac{L n_1}{c}\left(\frac{n_1 - n_2}{n_2}\right) \approx \frac{L n_1 \Delta}{c}
    \end{equation}
    where $\Delta = \frac{n_1 - n_2}{n_1}$ is the fractional index difference.
    \item \textbf{Fiber Attenuation Coefficient ($\alpha_{\text{dB}}$):} Signal power loss over distance $L$:
    \begin{equation}
        \alpha_{\text{dB}} = \frac{10}{L} \log_{10}\left(\frac{P_{\text{in}}}{P_{\text{out}}}\right) \quad (\text{dB/km})
    \end{equation}
\end{itemize}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 2.1: Full-Wave Bridge Rectifier Design with Capacitor Filter]
\textbf{Problem:} A bridge rectifier supplied with $230\,\text{V}_{\text{rms}}, 50\,\text{Hz}$ AC uses a step-down transformer with a turns ratio of $10:1$. Silicon diodes have forward drop $V_D = 0.7\,\text{V}$. The load is $R_L = 500\,\Omega$, and a filtering capacitor $C = 1000\,\mu\text{F}$ is connected.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the secondary peak voltage $V_m$ and peak filtered DC voltage $V_{peak}$.
    \item Determine the peak-to-peak ripple voltage $V_{r(pp)}$, ripple factor $\gamma$, and DC load current $I_{dc}$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item Secondary RMS voltage: $V_{2,\text{rms}} = \frac{230}{10} = 23.0\,\text{V}_{\text{rms}}$.
    Peak secondary voltage: $V_m = \sqrt{2} \times 23.0\,\text{V} = \mathbf{32.53\,\text{V}}$.
    Accounting for two conducting diodes in bridge:
    \begin{equation}
        V_{peak} = V_m - 2 V_D = 32.53 - 2(0.7) = \mathbf{31.13\,\text{V}}
    \end{equation}
    \item \textbf{Ripple and DC Current:}
    Ripple frequency: $f_r = 2 f = 2 \times 50 = 100\,\text{Hz}$.
    \begin{align}
        V_{r(pp)} &= \frac{V_{peak}}{2 f C R_L} = \frac{31.13}{2(50)(1000 \times 10^{-6})(500)} = \frac{31.13}{50} = \mathbf{0.623\,\text{V}} \\
        V_{dc} &= V_{peak} - \frac{V_{r(pp)}}{2} = 31.13 - 0.31 = \mathbf{30.82\,\text{V}} \\
        I_{dc} &= \frac{V_{dc}}{R_L} = \frac{30.82\,\text{V}}{500\,\Omega} = \mathbf{61.64\,\text{mA}} \\
        \gamma &= \frac{V_{r(pp)}}{2\sqrt{3} V_{dc}} = \frac{0.623}{2\sqrt{3}(30.82)} = \frac{0.623}{106.76} = \mathbf{0.00583} \quad (0.583\%)
    \end{align}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 2.2: BJT Voltage Divider Bias Circuit $Q$-Point Calculation]
\textbf{Problem:} A silicon NPN transistor ($\beta = 100, V_{BE} = 0.7\,\text{V}$) is configured in a voltage divider bias circuit with $V_{CC} = 15.0\,\text{V}$, $R_1 = 39\,\text{k}\Omega$, $R_2 = 10\,\text{k}\Omega$, $R_C = 2.2\,\text{k}\Omega$, and $R_E = 1.0\,\text{k}\Omega$.
Determine the Thevenin equivalent base voltage $V_{TH}$, base resistance $R_{TH}$, base current $I_B$, collector current $I_C$, and collector-emitter voltage $V_{CE}$ at the $Q$-point.

\textbf{Solution:}
\begin{enumerate}
    \item \textbf{Thevenin Equivalent Circuit at the Base:}
    \begin{align}
        V_{TH} &= V_{CC}\left(\frac{R_2}{R_1 + R_2}\right) = 15.0\left(\frac{10}{39 + 10}\right) = 15.0\left(\frac{10}{49}\right) = \mathbf{3.061\,\text{V}} \\
        R_{TH} &= R_1 \parallel R_2 = \frac{39 \times 10}{49}\,\text{k}\Omega = \mathbf{7.959\,\text{k}\Omega}
    \end{align}
    \item \textbf{Base and Collector Currents:}
    Applying KVL around the base-emitter loop ($V_{TH} - I_B R_{TH} - V_{BE} - I_E R_E = 0$, with $I_E = (\beta+1)I_B$):
    \begin{align}
        I_B &= \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1)R_E} = \frac{3.061 - 0.70}{7959 + (101)(1000)} = \frac{2.361}{108{,}959} = \mathbf{21.67\,\mu\text{A}} \\
        I_C &= \beta I_B = 100 \times 21.67\,\mu\text{A} = \mathbf{2.167\,\text{mA}} \\
        I_E &= I_B + I_C = 2.189\,\text{mA}
    \end{align}
    \item \textbf{Collector-Emitter Voltage ($V_{CE}$):}
    Applying KVL to the collector-emitter loop:
    \begin{align}
        V_{CE} &= V_{CC} - I_C R_C - I_E R_E = 15.0 - (2.167 \times 10^{-3})(2200) - (2.189 \times 10^{-3})(1000) \\
        &= 15.0 - 4.767 - 2.189 = \mathbf{8.044\,\text{V}}
    \end{align}
    The quiescent operating point is $Q = (8.04\,\text{V}, 2.17\,\text{mA})$ in the active region ($V_{CE} > 0.2\,\text{V}$).
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 2.3: CMOS Microprocessor Dynamic Power Scaling]
\textbf{Problem:} A 64-bit multi-core CMOS processor with total switching capacitance $C_L = 25.0\,\text{nF}$ operates at clock frequency $f_1 = 3.2\,\text{GHz}$ with supply voltage $V_{DD1} = 1.20\,\text{V}$ and average activity factor $\alpha = 0.20$.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the baseline dynamic power dissipation $P_1$.
    \item To reduce heat generation, Dynamic Voltage and Frequency Scaling (DVFS) reduces $V_{DD2}$ to $0.95\,\text{V}$ and frequency to $f_2 = 2.4\,\text{GHz}$. Compute the new dynamic power $P_2$ and percentage power reduction.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Baseline Dynamic Power:}
    \begin{align}
        P_1 &= \alpha C_L V_{DD1}^2 f_1 = (0.20)(25.0 \times 10^{-9}\,\text{F})(1.20\,\text{V})^2(3.2 \times 10^9\,\text{s}^{-1}) \\
        &= (0.20)(25.0 \times 10^{-9})(1.44)(3.2 \times 10^9) = \mathbf{23.04\,\text{W}}
    \end{align}
    \item \textbf{Scaled Dynamic Power:}
    \begin{align}
        P_2 &= \alpha C_L V_{DD2}^2 f_2 = (0.20)(25.0 \times 10^{-9})(0.95)^2(2.4 \times 10^9) \\
        &= (0.20)(25.0 \times 10^{-9})(0.9025)(2.4 \times 10^9) = \mathbf{10.83\,\text{W}}
    \end{align}
    Percentage Power Reduction:
    \begin{equation}
        \Delta P\% = \frac{P_1 - P_2}{P_1} \times 100\% = \frac{23.04 - 10.83}{23.04} \times 100\% = \frac{12.21}{23.04} \times 100\% = \mathbf{53.0\%}
    \end{equation}
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 2.4: Optical Fiber Dispersion and Signal Bandwidth Limit]
\textbf{Problem:} A step-index silica optical fiber has core refractive index $n_1 = 1.480$, cladding index $n_2 = 1.460$, and length $L = 5.0\,\text{km}$. Speed of light in vacuum is $c = 3.0 \times 10^8\,\text{m/s}$.
\begin{enumerate}[label=(\alph*)]
    \item Calculate the fractional refractive index difference $\Delta$, critical angle $\theta_c$, and numerical aperture $\text{NA}$.
    \item Compute the total intermodal pulse delay dispersion $\Delta t_{\text{modal}}$ and the maximum achievable optical bit rate $B \approx \frac{1}{2\Delta t}$.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Fractional Index Difference and Critical Angle:}
    \begin{align}
        \Delta &= \frac{n_1 - n_2}{n_1} = \frac{1.480 - 1.460}{1.480} = \frac{0.020}{1.480} = \mathbf{0.01351} \quad (1.351\%) \\
        \sin \theta_c &= \frac{n_2}{n_1} = \frac{1.460}{1.480} = 0.9865 \implies \theta_c = \arcsin(0.9865) = \mathbf{80.57^\circ} \\
        \text{NA} &= \sqrt{n_1^2 - n_2^2} = \sqrt{(1.480)^2 - (1.460)^2} = \sqrt{2.1904 - 2.1316} = \sqrt{0.0588} = \mathbf{0.2425}
    \end{align}
    \item \textbf{Intermodal Dispersion and Bit Rate:}
    \begin{align}
        \Delta t_{\text{modal}} &= \frac{L n_1}{c}\left(\frac{n_1 - n_2}{n_2}\right) = \frac{(5000\,\text{m})(1.480)}{3.0 \times 10^8\,\text{m/s}}\left(\frac{0.020}{1.460}\right) \\
        &= (2.467 \times 10^{-5}\,\text{s})(0.01370) = 3.379 \times 10^{-7}\,\text{s} = \mathbf{337.9\,\text{ns}} \\
        B_{\text{max}} &\approx \frac{1}{2 \Delta t_{\text{modal}}} = \frac{1}{2(337.9 \times 10^{-9}\,\text{s})} = \mathbf{1.48\,\text{Mbps}}
    \end{align}
\end{enumerate}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Circuit Theorems:} KCL is charge conservation ($\sum I = 0$); KVL is energy conservation ($\sum V = 0$).
    \item \textbf{Rectifier Systems:} Bridge rectifiers achieve $81.2\%$ efficiency with ripple frequency $2f$. A capacitor filter yields ripple $\gamma = \frac{1}{4\sqrt{3} f C R_L}$.
    \item \textbf{BJT Amplification:} In active mode ($V_{BE} \approx 0.7\,\text{V}$, CBJ reverse-biased), $I_C = \beta I_B$. Voltage divider bias provides robust $Q$-point thermal stability ($S \to 1$).
    \item \textbf{CMOS Power:} Dynamic power scales quadratically with voltage: $P = \alpha C_L V_{DD}^2 f$.
    \item \textbf{Memory Cells:} SRAM (6T fast cache), DRAM (1T1C high density), Flash (non-volatile floating gate).
    \item \textbf{Roofline Model:} $P = \min(P_{\text{peak}}, I \times \text{BW})$, differentiating compute-bound and memory-bound AI workloads.
    \item \textbf{Optical Fibers:} Total internal reflection occurs when $n_1 > n_2$. Numerical aperture $\text{NA} = \sqrt{n_1^2 - n_2^2} = \sin \theta_a$. Intermodal dispersion is $\Delta t \approx \frac{L n_1 \Delta}{c}$.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-02-electricity-and-devices.tex", "w") as f:
    f.write(ch2)

print("Chapter 2 expanded successfully.")

