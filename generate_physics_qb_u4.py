# generate_physics_qb_u4.py
# -*- coding: utf-8 -*-

def get_unit_4_content():
    unit_num = 4
    unit_title = "Quantum Mechanics"
    
    mcqs = [
        # Part I: Foundational (1-50)
        (
            r"According to the de Broglie hypothesis, the matter wavelength $\lambda$ of a particle with linear momentum $p$ is:",
            r"$\lambda = \frac{h}{p}$",
            r"$\lambda = \frac{p}{h}$",
            r"$\lambda = h p$",
            r"$\lambda = \frac{\hbar}{p^2}$",
            "(a)",
            r"The de Broglie relation states that matter wavelength is inversely proportional to momentum: $\lambda = h/p$."
        ),
        (
            r"The de Broglie wavelength of an electron accelerated from rest through an electrostatic potential difference $V$ is given by:",
            r"$\lambda = \frac{1.227}{\sqrt{V}}\text{ nm}$",
            r"$\lambda = \frac{12.27}{\sqrt{V}}\text{ nm}$",
            r"$\lambda = 1.227\sqrt{V}\text{ nm}$",
            r"$\lambda = \frac{0.1227}{V}\text{ nm}$",
            "(a)",
            r"$\lambda = \frac{h}{\sqrt{2m_e e V}} = \frac{1.227 \times 10^{-9}}{\sqrt{V}}\text{ m} = \frac{1.227}{\sqrt{V}}\text{ nm}$."
        ),
        (
            r"The wave nature of electrons was first directly validated experimentally by:",
            r"The Michelson-Morley experiment",
            r"The Davisson-Germer electron diffraction experiment",
            r"The Stern-Gerlach experiment",
            r"The Millikan oil drop experiment",
            "(b)",
            r"Davisson and Germer observed diffraction peaks of electrons scattered from a nickel crystal target in 1927."
        ),
        (
            r"In the Davisson-Germer experiment, the primary diffraction peak was observed at an accelerating potential and scattering angle of:",
            r"$54\text{ V}$ and $\phi = 50^\circ$",
            r"$100\text{ V}$ and $\phi = 90^\circ$",
            r"$25\text{ V}$ and $\phi = 30^\circ$",
            r"$500\text{ V}$ and $\phi = 45^\circ$",
            "(a)",
            r"A sharp diffraction peak occurred at $V = 54\text{ V}$ at angle $\phi = 50^\circ$, yielding $\lambda = 0.167\text{ nm}$ matching Bragg's law."
        ),
        (
            r"The phase velocity $v_p$ of a harmonic wave is defined as:",
            r"$v_p = \frac{\omega}{k}$",
            r"$v_p = \frac{d\omega}{dk}$",
            r"$v_p = \omega k$",
            r"$v_p = \frac{k}{\omega}$",
            "(a)",
            r"Phase velocity is the speed at which individual monochromatic wave crests travel: $v_p = \omega/k$."
        ),
        (
            r"The group velocity $v_g$ of a wave packet is defined as:",
            r"$v_g = \frac{d\omega}{dk}$",
            r"$v_g = \frac{\omega}{k}$",
            r"$v_g = \frac{k}{\omega}$",
            r"$v_g = \frac{d^2\omega}{dk^2}$",
            "(a)",
            r"Group velocity is the velocity of the envelope modulating the wave packet: $v_g = d\omega/dk$."
        ),
        (
            r"For a non-relativistic free particle of mass $m$ and velocity $v$, the group velocity of its de Broglie wave packet equals:",
            r"$v_g = v$ (the physical particle velocity)",
            r"$v_g = v/2$",
            r"$v_g = 2v$",
            r"$v_g = c$",
            "(a)",
            r"Using $E = \hbar\omega = \frac{\hbar^2 k^2}{2m}$, $v_g = \frac{d\omega}{dk} = \frac{\hbar k}{m} = \frac{p}{m} = v$."
        ),
        (
            r"For relativistic de Broglie matter waves, the product of phase velocity $v_p$ and group velocity $v_g$ satisfies:",
            r"$v_p \cdot v_g = c^2$",
            r"$v_p \cdot v_g = 1$",
            r"$v_p / v_g = c$",
            r"$v_p + v_g = c$",
            "(a)",
            r"Since $E = \hbar\omega = \gamma m c^2$ and $p = \hbar k = \gamma m v$, $v_p \cdot v_g = (\omega/k)(d\omega/dk) = (c^2/v)(v) = c^2$."
        ),
        (
            r"Heisenberg's Uncertainty Principle for position and linear momentum states:",
            r"$\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}$",
            r"$\Delta x \cdot \Delta p_x = 0$",
            r"$\Delta x \cdot \Delta p_x \le \hbar$",
            r"$\frac{\Delta x}{\Delta p_x} \ge \hbar$",
            "(a)",
            r"The fundamental quantum uncertainty relation is $\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}$ where $\hbar = h/(2\pi)$."
        ),
        (
            r"Heisenberg's Uncertainty Principle for energy and time is expressed as:",
            r"$\Delta E \cdot \Delta t \ge \frac{\hbar}{2}$",
            r"$\Delta E \cdot \Delta t \le \hbar$",
            r"$\Delta E = \Delta t$",
            r"$\Delta E \cdot \Delta t = 0$",
            "(a)",
            r"The conjugate energy-time uncertainty relation is $\Delta E \cdot \Delta t \ge \frac{\hbar}{2}$."
        ),
        (
            r"Why cannot electrons exist inside the atomic nucleus ($R \sim 10^{-14}\text{ m}$)?",
            r"Uncertainty in momentum would require electron kinetic energy $> 20\text{ MeV}$, which far exceeds observed $\beta$-decay energies ($\sim 2\text{--}3\text{ MeV}$)",
            r"Electrons have positive mass",
            r"Nuclear forces repel negative charges",
            r"Electrons travel at speed $2c$",
            "(a)",
            r"Confinement to $\Delta x \sim 10^{-14}\text{ m}$ gives $\Delta p \approx 5.3 \times 10^{-21}\text{ kg}\cdot\text{m/s}$, requiring $E_k > 20\text{ MeV}$, proving electrons cannot reside in nuclei."
        ),
        (
            r"Max Born's statistical interpretation of the complex quantum wavefunction $\Psi(\vec{r},t)$ states that:",
            r"$|\Psi(\vec{r},t)|^2 = \Psi^* \Psi$ represents the probability density of finding the particle at position $\vec{r}$ at time $t$",
            r"$\Psi$ represents the physical mass density of the electron",
            r"$\Psi$ is the classical electric potential",
            r"$|\Psi|^2$ is the total mechanical energy",
            "(a)",
            r"Born established that $|\Psi(\vec{r},t)|^2 dV$ is the probability of finding the quantum particle in differential volume $dV$."
        ),
        (
            r"The global normalization condition for a physically acceptable 1D wave function $\psi(x)$ is:",
            r"$\int_{-\infty}^{+\infty} |\psi(x)|^2 dx = 1$",
            r"$\int_{-\infty}^{+\infty} \psi(x) dx = 0$",
            r"$\int_{-\infty}^{+\infty} |\psi(x)|^2 dx = \infty$",
            r"$\psi(0) = 1$",
            "(a)",
            r"The total probability of finding the particle somewhere across all space must equal $100\%$ ($1.0$)."
        ),
        (
            r"Which of the following is NOT a required mathematical condition for a physically well-behaved wave function $\psi(x)$?",
            r"$\psi(x)$ must be single-valued everywhere",
            r"$\psi(x)$ must be continuous everywhere",
            r"$\frac{d\psi}{dx}$ must be continuous everywhere (for finite potentials)",
            r"$\psi(x)$ must become infinite at the boundaries",
            "(d)",
            r"A valid wavefunction must remain finite and square-integrable everywhere; it must never blow up to infinity."
        ),
        (
            r"The quantum mechanical operator for linear momentum $\hat{p}_x$ in coordinate space is:",
            r"$\hat{p}_x = -i\hbar \frac{\partial}{\partial x}$",
            r"$\hat{p}_x = i\hbar \frac{\partial}{\partial x}$",
            r"$\hat{p}_x = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}$",
            r"$\hat{p}_x = \hbar \frac{\partial}{\partial t}$",
            "(a)",
            r"In the coordinate representation, linear momentum is represented by the differential operator $\hat{p}_x = -i\hbar \frac{\partial}{\partial x}$."
        ),
        (
            r"The quantum mechanical total energy operator $\hat{E}$ is given by:",
            r"$\hat{E} = i\hbar \frac{\partial}{\partial t}$",
            r"$\hat{E} = -i\hbar \frac{\partial}{\partial t}$",
            r"$\hat{E} = \hbar \frac{\partial}{\partial x}$",
            r"$\hat{E} = -\frac{\hbar^2}{2m}$",
            "(a)",
            r"The quantum mechanical energy operator is $\hat{E} = i\hbar \frac{\partial}{\partial t}$."
        ),
        (
            r"The Hamiltonian operator $\hat{H}$ for a particle of mass $m$ in a potential $V(x)$ is:",
            r"$\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$",
            r"$\hat{H} = \frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$",
            r"$\hat{H} = -i\hbar \frac{d}{dx} + V(x)$",
            r"$\hat{H} = -\frac{\hbar^2}{2m}\nabla^2$",
            "(a)",
            r"The Hamiltonian represents total energy $\hat{H} = \hat{T} + \hat{V} = \frac{\hat{p}^2}{2m} + V(x) = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$."
        ),
        (
            r"The 1D Time-Dependent Schrödinger Equation (TDSE) is written as:",
            r"$i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V(x)\Psi$",
            r"$i\hbar \frac{\partial \Psi}{\partial x} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial t^2} + V\Psi$",
            r"$\frac{\partial^2 \Psi}{\partial t^2} = c^2 \frac{\partial^2 \Psi}{\partial x^2}$",
            r"$\hat{H}\Psi = 0$",
            "(a)",
            r"The TDSE is $i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V(x)\Psi$."
        ),
        (
            r"The 1D Time-Independent Schrödinger Equation (TISE) for stationary states of energy $E$ is:",
            r"$-\frac{\hbar^2}{2m}\frac{d^2 \psi}{dx^2} + V(x)\psi = E\psi$",
            r"$\frac{d^2\psi}{dx^2} + \frac{2m}{\hbar^2}(E - V)\psi = 0$",
            r"$\hat{H}\psi = E\psi$",
            r"All of the above are equivalent forms",
            "(d)",
            r"All three statements are mathematically equivalent representations of the eigenvalue equation $\hat{H}\psi = E\psi$."
        ),
        (
            r"For a particle of mass $m$ trapped in a 1D infinite square well of width $L$ ($0 \le x \le L$), the quantized energy eigenvalues $E_n$ are:",
            r"$E_n = \frac{n^2 h^2}{8mL^2} = \frac{n^2 \pi^2 \hbar^2}{2mL^2} \quad (n = 1, 2, 3,\dots)$",
            r"$E_n = \frac{n h}{8mL}$",
            r"$E_n = \frac{n^2 \hbar^2}{2mL}$",
            r"$E_n = \frac{(n+1/2)\hbar^2}{2mL^2}$",
            "(a)",
            r"Boundary conditions $\psi(0)=\psi(L)=0$ require $k_n = n\pi/L$, giving $E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2 h^2}{8mL^2}$."
        ),
        (
            r"Why is the quantum number $n=0$ physically impossible for a particle in an infinite potential well?",
            r"Because $n=0$ gives $\psi(x) = \sqrt{2/L}\sin(0) = 0$ everywhere, which means no particle exists (violates normalization)",
            r"Because energy would be infinite",
            r"Because momentum would be negative",
            r"Because the mass becomes zero",
            "(a)",
            r"$n=0$ yields a vanishing wavefunction $\psi(x) = 0$, representing the complete absence of a particle."
        ),
        (
            r"The zero-point energy (ground-state energy $E_1$) of a particle in an infinite square well is:",
            r"$E_1 = 0$",
            r"$E_1 = \frac{h^2}{8mL^2} > 0$",
            r"$E_1 = \infty$",
            r"$E_1 = -\frac{h^2}{8mL^2}$",
            "(b)",
            r"Zero-point energy is strictly non-zero ($E_1 = \frac{h^2}{8mL^2} > 0$), fully consistent with Heisenberg's uncertainty principle."
        ),
        (
            r"The normalized spatial wave functions $\psi_n(x)$ for a particle in a 1D infinite well of width $L$ ($0 \le x \le L$) are:",
            r"$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$",
            r"$\psi_n(x) = \sqrt{\frac{1}{L}}\cos\left(\frac{n\pi x}{L}\right)$",
            r"$\psi_n(x) = \frac{2}{L}\sin\left(\frac{n\pi x}{L}\right)$",
            r"$\psi_n(x) = \sqrt{\frac{2}{L}}e^{i n\pi x/L}$",
            "(a)",
            r"Integrating $\int_0^L A^2 \sin^2(n\pi x/L)dx = 1$ yields normalization constant $A = \sqrt{2/L}$."
        ),
        (
            r"The number of interior spatial nodes (points where $\psi(x) = 0$ inside the well) for the $n$-th energy state is:",
            r"$n$",
            r"$n - 1$",
            r"$n + 1$",
            r"$2n$",
            "(b)",
            r"The $n$-th quantum state has exactly $(n - 1)$ interior nodes (e.g., ground state $n=1$ has $0$ interior nodes)."
        ),
        (
            r"The expectation value $\langle x \rangle$ of position for any stationary state $\psi_n(x)$ in a 1D box of width $L$ ($0 \le x \le L$) is:",
            r"$\langle x \rangle = 0$",
            r"$\langle x \rangle = \frac{L}{2}$",
            r"$\langle x \rangle = \frac{L}{4}$",
            r"$\langle x \rangle = L$",
            "(b)",
            r"Because probability density $|\psi_n(x)|^2 = \frac{2}{L}\sin^2(n\pi x/L)$ is symmetric about the center, $\langle x \rangle = L/2$."
        ),
        (
            r"The expectation value of linear momentum $\langle p_x \rangle$ for any stationary state in a 1D infinite well is:",
            r"$\langle p_x \rangle = 0$",
            r"$\langle p_x \rangle = \frac{n\pi\hbar}{L}$",
            r"$\langle p_x \rangle = \frac{n h}{2L}$",
            r"$\langle p_x \rangle = \infty$",
            "(a)",
            r"The particle oscillates back and forth with equal probability of $+p$ and $-p$, making the net expectation momentum $\langle p_x \rangle = 0$."
        ),
        (
            r"The ratio of the first four energy levels ($E_1 : E_2 : E_3 : E_4$) for a particle in a 1D infinite potential well is:",
            r"$1 : 2 : 3 : 4$",
            r"$1 : 4 : 9 : 16$",
            r"$1 : 3 : 5 : 7$",
            r"$1 : 8 : 27 : 64$",
            "(b)",
            r"Because $E_n = n^2 E_1$, the energy levels scale as $1^2 : 2^2 : 3^2 : 4^2 = 1 : 4 : 9 : 16$."
        ),
        (
            r"For a particle in a 3D cubical box of side $L$, the energy eigenvalues are given by:",
            r"$E_{n_x,n_y,n_z} = \frac{h^2}{8mL^2}(n_x^2 + n_y^2 + n_z^2)$",
            r"$E = \frac{h^2}{8mL^2}(n_x + n_y + n_z)^2$",
            r"$E = \frac{3 h^2}{8mL^2} n$",
            r"$E = \frac{h^2}{8mL^2}(n_x n_y n_z)$",
            "(a)",
            r"Separation of variables in 3D yields $E = \frac{h^2}{8mL^2}(n_x^2 + n_y^2 + n_z^2)$ with quantum numbers $n_x, n_y, n_z \in \{1, 2, 3,\dots\}$."
        ),
        (
            r"In a 3D cubical box, the degree of degeneracy of the first excited energy level ($n_x^2 + n_y^2 + n_z^2 = 1^2 + 1^2 + 2^2 = 6$) is:",
            r"Non-degenerate ($1$)",
            r"$2$-fold degenerate",
            r"$3$-fold degenerate ($(2,1,1), (1,2,1), (1,1,2)$)",
            r"$6$-fold degenerate",
            "(c)",
            r"Three distinct combinations $(2,1,1), (1,2,1),$ and $(1,1,2)$ share the exact same energy $E = 6E_1$."
        ),
        (
            r"Quantum mechanical tunneling is the physical phenomenon where a particle:",
            r"Penetrates through a potential energy barrier whose height $V_0$ is greater than the particle's total energy $E$",
            r"Gains infinite velocity",
            r"Destroys the potential barrier mechanically",
            r"Absorbs an infinite number of photons",
            "(a)",
            r"Because wavefunctions decay exponentially rather than dropping abruptly to zero, there is a finite transmission probability $T > 0$ through barriers $V_0 > E$."
        ),
        (
            r"Which prominent scientific instrument operates directly on the principle of quantum mechanical electron tunneling?",
            r"Scanning Tunneling Microscope (STM)",
            r"Optical telescope",
            r"Cathode ray oscilloscope",
            r"Geiger-Muller counter",
            "(a)",
            r"Binnig and Rohrer invented the STM by measuring quantum tunneling current between an atomic tip and sample surface."
        ),
        (
            r"The transmission probability $T$ for a particle of energy $E$ tunneling through a rectangular barrier of height $V_0 > E$ and width $a$ scales as:",
            r"$T \propto e^{-2\kappa a}$ where $\kappa = \sqrt{\frac{2m(V_0 - E)}{\hbar^2}}$",
            r"$T \propto e^{+\kappa a}$",
            r"$T \propto 1/a$",
            r"$T \propto (V_0 - E)^2$",
            "(a)",
            r"The transmission coefficient decays exponentially with barrier width $a$: $T \approx 16\frac{E}{V_0}(1 - \frac{E}{V_0})e^{-2\kappa a}$."
        ),
        (
            r"The commutator bracket $[\hat{x}, \hat{p}_x] = \hat{x}\hat{p}_x - \hat{p}_x\hat{x}$ evaluates to:",
            r"$0$",
            r"$i\hbar$",
            r"$-i\hbar$",
            r"$\hbar^2$",
            "(b)",
            r"$[\hat{x}, \hat{p}_x]\psi = x(-i\hbar \psi') - (-i\hbar (x\psi)') = -i\hbar x \psi' + i\hbar \psi + i\hbar x \psi' = i\hbar \psi \implies [\hat{x}, \hat{p}_x] = i\hbar$."
        ),
        (
            r"The non-commutativity of operators $[\hat{A}, \hat{B}] \ne 0$ fundamentally implies that:",
            r"The physical observables $A$ and $B$ cannot be simultaneously measured with arbitrary precision",
            r"Both observables must equal zero",
            r"The system has zero energy",
            r"The wave function is unnormalizable",
            "(a)",
            r"Operators that do not commute do not share a common set of eigenfunctions, establishing a Robertson-Schrödinger uncertainty relation."
        ),
        (
            r"Hermitian operators in quantum mechanics are mathematically essential because:",
            r"Their eigenvalues are guaranteed to be strictly real numbers, matching physical experimental measurements",
            r"They eliminate imaginary numbers from equations",
            r"They are always diagonal matrices",
            r"They commute with all other operators",
            "(a)",
            r"Physical observables must be represented by Hermitian operators ($\hat{A}^\dagger = \hat{A}$) to ensure real observable eigenvalues."
        ),
        (
            r"Two wavefunctions $\psi_m(x)$ and $\psi_n(x)$ corresponding to distinct energy eigenvalues of a Hermitian Hamiltonian are:",
            r"Mutually orthogonal: $\int \psi_m^*(x)\psi_n(x)dx = 0 \quad (m \ne n)$",
            r"Identical",
            r"Linearly dependent",
            r"Infinite at the origin",
            "(a)",
            r"Eigenfunctions of Hermitian operators belonging to different eigenvalues are strictly orthogonal."
        ),
        (
            r"The expectation value $\langle A \rangle$ of a physical observable associated with operator $\hat{A}$ for state $\Psi$ is calculated as:",
            r"$\langle A \rangle = \int_{-\infty}^{+\infty} \Psi^* \hat{A} \Psi\,dx$",
            r"$\langle A \rangle = \int_{-\infty}^{+\infty} \hat{A} |\Psi|^2\,dx$",
            r"$\langle A \rangle = \frac{\hat{A}}{\int |\Psi|^2 dx}$",
            r"$\langle A \rangle = \Psi^* \hat{A}$",
            "(a)",
            r"The quantum expectation value is defined as the sandwich integral $\langle A \rangle = \int \Psi^* \hat{A} \Psi dx$."
        ),
        (
            r"In Compton scattering, the shift in photon wavelength $\Delta \lambda = \lambda' - \lambda$ after scattering by angle $\theta$ is:",
            r"$\Delta \lambda = \frac{h}{m_e c}(1 - \cos\theta)$",
            r"$\Delta \lambda = \frac{h}{m_e c}(1 + \cos\theta)$",
            r"$\Delta \lambda = \frac{m_e c}{h}(1 - \sin\theta)$",
            r"$\Delta \lambda = \frac{h}{2m_e c}\sin\theta$",
            "(a)",
            r"The Compton formula is $\Delta\lambda = \lambda_C(1 - \cos\theta)$ where $\lambda_C = \frac{h}{m_e c} \approx 0.02426\text{ \AA} = 2.426\text{ pm}$."
        ),
        (
            r"The Compton wavelength of an electron $\lambda_C = \frac{h}{m_e c}$ has the numerical value:",
            r"$0.0243\text{ \AA} = 2.43\text{ pm}$",
            r"$0.243\text{ nm}$",
            r"$2.43\text{ nm}$",
            r"$24.3\text{ nm}$",
            "(a)",
            r"$\lambda_C = \frac{6.626 \times 10^{-34}}{(9.109 \times 10^{-31})(3 \times 10^8)} \approx 2.426 \times 10^{-12}\text{ m} = 0.02426\text{ \AA}$."
        ),
        (
            r"The maximum possible Compton wavelength shift $\Delta \lambda_{\text{max}}$ occurs at a scattering angle of:",
            r"$\theta = 180^\circ$ (backscattering), where $\Delta\lambda = 2\lambda_C \approx 0.0485\text{ \AA}$",
            r"$\theta = 90^\circ$",
            r"$\theta = 0^\circ$",
            r"$\theta = 45^\circ$",
            "(a)",
            r"At $\theta = 180^\circ$, $(1 - \cos 180^\circ) = 1 - (-1) = 2$, maximizing the wavelength shift to $\Delta\lambda = 2\lambda_C$."
        ),
        (
            r"The photoelectric work function $\Phi$ of a metal represents:",
            r"The minimum photon energy required to liberate an electron from the metal surface at $T=0\text{ K}$",
            r"The maximum kinetic energy of photoelectrons",
            r"The energy needed to melt the metal",
            r"The total electrostatic potential of the lattice",
            "(a)",
            r"Work function $\Phi = h\nu_0$ is the minimum threshold energy required to overcome the surface barrier potential."
        ),
        (
            r"Einstein's photoelectric equation is given by:",
            r"$K_{\text{max}} = h\nu - \Phi = e V_0$",
            r"$K_{\text{max}} = h\nu + \Phi$",
            r"$K_{\text{max}} = \frac{h\nu}{\Phi}$",
            r"$K_{\text{max}} = \Phi - h\nu$",
            "(a)",
            r"Conservation of photon energy gives $K_{\text{max}} = h\nu - \Phi = e V_0$ where $V_0$ is the stopping potential."
        ),
        (
            r"The slope of the graph of stopping potential $V_0$ versus frequency $\nu$ in a photoelectric experiment is equal to:",
            r"$h/e$",
            r"$e/h$",
            r"$h$",
            r"$e$",
            "(a)",
            r"From $V_0 = \left(\frac{h}{e}\right)\nu - \frac{\Phi}{e}$, the slope is universally equal to Planck's constant divided by electron charge ($h/e$)."
        ),
        (
            r"An electron is accelerated through a potential difference $V = 100\text{ V}$. Its de Broglie wavelength is:",
            r"$0.123\text{ nm} = 1.23\text{ \AA}$",
            r"$1.23\text{ nm}$",
            r"$0.0123\text{ nm}$",
            r"$12.3\text{ nm}$",
            "(a)",
            r"$\lambda = \frac{1.227}{\sqrt{100}}\text{ nm} = \frac{1.227}{10} = 0.1227\text{ nm} \approx 1.23\text{ \AA}$."
        ),
        (
            r"A thermal neutron at temperature $T = 300\text{ K}$ has average kinetic energy $E_k = \frac{3}{2}k_B T$. Its de Broglie wavelength is approximately:",
            r"$0.145\text{ nm} = 1.45\text{ \AA}$",
            r"$1.45\text{ nm}$",
            r"$0.0145\text{ nm}$",
            r"$14.5\text{ nm}$",
            "(a)",
            r"$\lambda = \frac{h}{\sqrt{3 m_n k_B T}} = \frac{6.626 \times 10^{-34}}{\sqrt{3(1.675 \times 10^{-27})(1.38 \times 10^{-23})(300)}} \approx 1.45 \times 10^{-10}\text{ m} = 0.145\text{ nm}$."
        ),
        (
            r"An electron is confined in a 1D box of width $L = 0.1\text{ nm}$ ($1\text{ \AA}$). Its ground-state energy $E_1$ is approximately:",
            r"$37.6\text{ eV}$",
            r"$3.76\text{ eV}$",
            r"$376\text{ eV}$",
            r"$0.376\text{ eV}$",
            "(a)",
            r"$E_1 = \frac{h^2}{8 m_e L^2} = \frac{(6.626 \times 10^{-34})^2}{8(9.109 \times 10^{-31})(10^{-10})^2} \approx 6.024 \times 10^{-18}\text{ J} = \frac{6.024 \times 10^{-18}}{1.602 \times 10^{-19}} \approx 37.6\text{ eV}$."
        ),
        (
            r"For the electron in Question 46, the first excited state energy $E_2$ is:",
            r"$150.4\text{ eV}$",
            r"$75.2\text{ eV}$",
            r"$112.8\text{ eV}$",
            r"$338.4\text{ eV}$",
            "(a)",
            r"$E_2 = 2^2 E_1 = 4 \times 37.6\text{ eV} = 150.4\text{ eV}$."
        ),
        (
            r"The probability of finding a particle in the ground state of an infinite well ($0 \le x \le L$) in the middle third of the box $[L/3, 2L/3]$ is:",
            r"$\frac{1}{3} + \frac{\sqrt{3}}{2\pi} \approx 60.9\%$",
            r"$33.3\%$",
            r"$50.0\%$",
            r"$25.0\%$",
            "(a)",
            r"$P = \int_{L/3}^{2L/3}\frac{2}{L}\sin^2(\frac{\pi x}{L})dx = \left[\frac{x}{L} - \frac{\sin(2\pi x/L)}{2\pi}\right]_{L/3}^{2L/3} = \frac{1}{3} + \frac{\sqrt{3}}{2\pi} \approx 0.609$."
        ),
        (
            r"If the position of an electron is measured with an uncertainty $\Delta x = 1.0\text{ \AA} = 10^{-10}\text{ m}$, the minimum uncertainty in its velocity $\Delta v_x$ is approximately:",
            r"$5.79 \times 10^5\text{ m/s}$",
            r"$5.79 \times 10^3\text{ m/s}$",
            r"$1.16 \times 10^6\text{ m/s}$",
            r"$3.00 \times 10^8\text{ m/s}$",
            "(a)",
            r"$\Delta p_x \ge \frac{\hbar}{2\Delta x} \implies \Delta v_x \ge \frac{\hbar}{2 m_e \Delta x} = \frac{1.0545 \times 10^{-34}}{2(9.109 \times 10^{-31})(10^{-10})} \approx 5.79 \times 10^5\text{ m/s}$."
        ),
        (
            r"Ehrenfest's Theorem in quantum mechanics proves that:",
            r"Quantum mechanical expectation values follow classical Newtonian laws of motion in the correspondence limit ($\frac{d\langle x \rangle}{dt} = \frac{\langle p \rangle}{m}$ and $\frac{d\langle p \rangle}{dt} = -\langle \nabla V \rangle$)",
            r"Quantum mechanics replaces all conservation laws",
            r"Energy is never conserved in quantum systems",
            r"Electrons travel on fixed Keplerian orbits",
            "(a)",
            r"Ehrenfest's theorem bridges quantum and classical physics, demonstrating $\frac{d\langle\vec{p}\rangle}{dt} = -\langle\nabla V\rangle$."
        ),

        # Part II: Intermediate Analytical (51-80)
        (
            r"A macroscopic marble of mass $m = 10\text{ g}$ moves at $v = 10\text{ m/s}$. Its de Broglie wavelength is:",
            r"$6.63 \times 10^{-33}\text{ m}$",
            r"$6.63 \times 10^{-30}\text{ m}$",
            r"$6.63 \times 10^{-27}\text{ m}$",
            r"$1.00 \times 10^{-15}\text{ m}$",
            "(a)",
            r"$\lambda = \frac{h}{m v} = \frac{6.626 \times 10^{-34}}{(0.01\text{ kg})(10\text{ m/s})} = 6.626 \times 10^{-33}\text{ m}$ (completely unobservable at macroscopic scales)."
        ),
        (
            r"The kinetic energy of an electron whose de Broglie wavelength equals its Compton wavelength ($\lambda = \lambda_C = h/(m_e c)$) is (relativistic calculation):",
            r"$(\sqrt{2} - 1)m_e c^2 \approx 0.414 m_e c^2 \approx 212\text{ keV}$",
            r"$0.5 m_e c^2$",
            r"$1.0 m_e c^2$",
            r"$2.0 m_e c^2$",
            "(a)",
            r"$p = h/\lambda = m_e c$. Total energy $E = \sqrt{p^2 c^2 + m_e^2 c^4} = \sqrt{2}m_e c^2$. Kinetic energy $K = E - m_e c^2 = (\sqrt{2}-1)m_e c^2 \approx 212\text{ keV}$."
        ),
        (
            r"An excited atomic energy state has an average radiative lifetime $\tau = 1.0\text{ ns} = 10^{-9}\text{ s}$. The minimum natural energy linewidth $\Delta E$ of the emitted line is:",
            r"$3.29 \times 10^{-7}\text{ eV}$",
            r"$3.29 \times 10^{-5}\text{ eV}$",
            r"$6.58 \times 10^{-16}\text{ eV}$",
            r"$1.00\text{ eV}$",
            "(a)",
            r"$\Delta E \ge \frac{\hbar}{2\tau} = \frac{1.0545 \times 10^{-34}\text{ J}\cdot\text{s}}{2(10^{-9}\text{ s})} = 5.27 \times 10^{-26}\text{ J} = \frac{5.27 \times 10^{-26}}{1.602 \times 10^{-19}} \approx 3.29 \times 10^{-7}\text{ eV}$."
        ),
        (
            r"For the atomic state in Question 53 emitting at $\lambda_0 = 500\text{ nm}$ ($\nu_0 = 6 \times 10^{14}\text{ Hz}$), the fractional natural line broadening $\Delta \nu / \nu_0$ is:",
            r"$1.33 \times 10^{-7}$",
            r"$1.33 \times 10^{-5}$",
            r"$1.33 \times 10^{-9}$",
            r"$5.00 \times 10^{-3}$",
            "(a)",
            r"$\Delta\nu = \frac{\Delta E}{h} = \frac{5.27 \times 10^{-26}}{6.626 \times 10^{-34}} \approx 7.95 \times 10^7\text{ Hz} \approx 80\text{ MHz}$. $\Delta\nu/\nu_0 = \frac{7.95 \times 10^7}{6 \times 10^{14}} \approx 1.33 \times 10^{-7}$."
        ),
        (
            r"A proton and an electron have the same kinetic energy. The ratio of their de Broglie wavelengths $\lambda_p / \lambda_e$ is:",
            r"$\sqrt{\frac{m_e}{m_p}} \approx \frac{1}{\sqrt{1836}} \approx \frac{1}{42.85}$",
            r"$\sqrt{\frac{m_p}{m_e}} \approx 42.85$",
            r"$\frac{m_e}{m_p} \approx \frac{1}{1836}$",
            r"$1.0$",
            "(a)",
            r"$\lambda = \frac{h}{\sqrt{2m E_k}} \implies \frac{\lambda_p}{\lambda_e} = \sqrt{\frac{m_e}{m_p}} = \sqrt{\frac{1}{1836}} \approx \frac{1}{42.85}$."
        ),
        (
            r"A proton and an electron have the exact same momentum $p$. The ratio of their de Broglie wavelengths $\lambda_p / \lambda_e$ is:",
            r"$1.0$",
            r"$1836$",
            r"$1/1836$",
            r"$42.85$",
            "(a)",
            r"Because $\lambda = h/p$, particles with identical momenta have strictly identical de Broglie wavelengths regardless of mass."
        ),
        (
            r"For an infinite square well of width $L$, the wavelength of a photon emitted during the transition from $n=3$ to $n=1$ is:",
            r"$\lambda = \frac{hc}{8 E_1}$",
            r"$\lambda = \frac{hc}{4 E_1}$",
            r"$\lambda = \frac{hc}{9 E_1}$",
            r"$\lambda = \frac{8 E_1}{hc}$",
            "(a)",
            r"$\Delta E = E_3 - E_1 = 3^2 E_1 - 1^2 E_1 = 8 E_1$. Photon wavelength $\lambda = \frac{hc}{\Delta E} = \frac{hc}{8 E_1}$."
        ),
        (
            r"The variance in position $\sigma_x^2 = \langle x^2 \rangle - \langle x \rangle^2$ for the ground state $n=1$ in a 1D box of width $L$ is:",
            r"$L^2\left(\frac{1}{12} - \frac{1}{2\pi^2}\right) \approx 0.0326 L^2$",
            r"$\frac{L^2}{12}$",
            r"$\frac{L^2}{4}$",
            r"$0$",
            "(a)",
            r"$\langle x^2 \rangle = L^2(\frac{1}{3} - \frac{1}{2\pi^2})$ and $\langle x \rangle^2 = \frac{L^2}{4} \implies \sigma_x^2 = L^2(\frac{1}{12} - \frac{1}{2\pi^2}) \approx 0.0326 L^2$."
        ),
        (
            r"The variance in momentum $\sigma_p^2 = \langle p^2 \rangle - \langle p \rangle^2$ for the $n=1$ ground state in the box is:",
            r"$\frac{\pi^2 \hbar^2}{L^2}$",
            r"$\frac{\pi \hbar}{L}$",
            r"$0$",
            r"$\frac{h^2}{4L^2}$",
            "(a)",
            r"$\langle p^2 \rangle = 2m E_1 = \frac{\pi^2\hbar^2}{L^2}$ and $\langle p \rangle = 0 \implies \sigma_p^2 = \frac{\pi^2\hbar^2}{L^2}$."
        ),
        (
            r"The uncertainty product $\Delta x \cdot \Delta p$ for the ground state of a particle in an infinite well evaluates to:",
            r"$\hbar \sqrt{\frac{\pi^2}{12} - \frac{1}{2}} \approx 0.568 \hbar > \frac{\hbar}{2}$",
            r"$\frac{\hbar}{2}$",
            r"$0$",
            r"$\pi \hbar$",
            "(a)",
            r"$\Delta x \Delta p = \sqrt{L^2(\frac{1}{12}-\frac{1}{2\pi^2})}\left(\frac{\pi\hbar}{L}\right) = \hbar\sqrt{\frac{\pi^2}{12}-\frac{1}{2}} \approx 0.568\hbar \ge 0.5\hbar$, validating Heisenberg's principle."
        ),
        (
            r"The quantum mechanical probability current density $\vec{J}(\vec{r},t)$ is defined as:",
            r"$\vec{J} = \frac{\hbar}{2mi}\left(\Psi^* \nabla \Psi - \Psi \nabla \Psi^*\right)$",
            r"$\vec{J} = |\Psi|^2 \vec{v}$",
            r"$\vec{J} = \Psi^* \Psi$",
            r"$\vec{J} = -\frac{\hbar^2}{2m}\nabla \Psi$",
            "(a)",
            r"Probability conservation $\frac{\partial P}{\partial t} + \nabla \cdot \vec{J} = 0$ requires $\vec{J} = \frac{\hbar}{2mi}(\Psi^*\nabla\Psi - \Psi\nabla\Psi^*)$."
        ),
        (
            r"For a plane wave state $\Psi(x,t) = A e^{i(kx - \omega t)}$, the probability current density $J_x$ is:",
            r"$J_x = |A|^2 \frac{\hbar k}{m} = |A|^2 v$",
            r"$J_x = 0$",
            r"$J_x = |A|^2$",
            r"$J_x = \hbar k$",
            "(a)",
            r"$\Psi^*\frac{d\Psi}{dx} - \Psi\frac{d\Psi^*}{dx} = A^*(ik A) - A(-ik A^*) = 2ik|A|^2 \implies J = \frac{\hbar}{2mi}(2ik|A|^2) = |A|^2 \frac{\hbar k}{m} = |A|^2 v$."
        ),
        (
            r"For any real bound-state spatial eigenfunction $\psi(x) = \psi^*(x)$ (standing wave), the net probability current density $J_x$ is:",
            r"Strictly zero ($J_x = 0$ everywhere)",
            r"$1.0$",
            r"$\infty$",
            r"Proportional to $x$",
            "(a)",
            r"Since $\psi(x)$ is purely real, $\psi\frac{d\psi}{dx} - \psi\frac{d\psi}{dx} = 0$, confirming zero net probability flow in stationary bound states."
        ),
        (
            r"An electron has total energy $E = 2.0\text{ eV}$ incident on a finite potential step of height $V_0 = 5.0\text{ eV}$. In the barrier region ($x > 0$), the wave function behaves as:",
            r"A pure decaying exponential $\psi(x) = C e^{-\kappa x}$ (evanescent wave)",
            r"A purely propagating sine wave",
            r"Zero identically everywhere",
            r"An exponentially exploding wave $e^{+\kappa x}$",
            "(a)",
            r"Inside the classically forbidden barrier ($V_0 > E$), the TISE yields real exponential decay $\psi(x) \propto e^{-\kappa x}$ where $\kappa = \sqrt{2m(V_0-E)}/\hbar$."
        ),
        (
            r"For the electron in Question 64, the penetration decay constant $\kappa$ is approximately:",
            r"$8.87 \times 10^9\text{ m}^{-1} = 0.887\text{ \AA}^{-1}$",
            r"$1.00 \times 10^7\text{ m}^{-1}$",
            r"$4.50 \times 10^5\text{ m}^{-1}$",
            r"$2.20 \times 10^9\text{ m}^{-1}$",
            "(a)",
            r"$\kappa = \frac{\sqrt{2(9.109 \times 10^{-31})(3.0 \times 1.602 \times 10^{-19})}}{1.0545 \times 10^{-34}} = \frac{9.355 \times 10^{-25}}{1.0545 \times 10^{-34}} \approx 8.87 \times 10^9\text{ m}^{-1}$."
        ),
        (
            r"The characteristic penetration depth $d = 1/\kappa$ over which the electron wave amplitude drops to $1/e \approx 36.8\%$ is:",
            r"$1.13\text{ \AA} = 0.113\text{ nm}$",
            r"$1.13\text{ nm}$",
            r"$11.3\text{ nm}$",
            r"$0.011\text{ nm}$",
            "(a)",
            r"$d = \frac{1}{\kappa} = \frac{1}{8.87 \times 10^9\text{ m}^{-1}} \approx 1.127 \times 10^{-10}\text{ m} = 1.13\text{ \AA}$."
        ),
        (
            r"The reflection coefficient $R$ for the potential step in Question 64 ($E < V_0$) is:",
            r"$R = 1.0$ ($100\%$ total quantum reflection)",
            r"$R = 0.5$",
            r"$R = 0$",
            r"$R = 0.25$",
            "(a)",
            r"Because the transmitted wave is evanescent and carries zero net real current ($J_{\text{trans}} = 0$), all incident probability is reflected ($R = 1.0$)."
        ),
        (
            r"A particle in a 1D harmonic oscillator potential $V(x) = \frac{1}{2}m\omega^2 x^2$ has quantized energy levels:",
            r"$E_n = (n + 1/2)\hbar\omega \quad (n = 0, 1, 2,\dots)$",
            r"$E_n = n \hbar\omega$",
            r"$E_n = n^2 \hbar\omega$",
            r"$E_n = (n + 1)\hbar\omega$",
            "(a)",
            r"The quantum harmonic oscillator exhibits equally spaced energy levels $E_n = (n + \frac{1}{2})\hbar\omega$ with zero-point energy $E_0 = \frac{1}{2}\hbar\omega$."
        ),
        (
            r"The zero-point energy of a 1D quantum harmonic oscillator of frequency $\omega$ is:",
            r"$E_0 = \frac{1}{2}\hbar\omega$",
            r"$E_0 = 0$",
            r"$E_0 = \hbar\omega$",
            r"$E_0 = \frac{3}{2}\hbar\omega$",
            "(a)",
            r"At absolute zero ($n=0$), the ground-state zero-point energy is strictly $E_0 = \frac{1}{2}\hbar\omega$."
        ),
        (
            r"In the Bohr model of the hydrogen atom, the orbital angular momentum $L$ of the electron is quantized according to:",
            r"$L = n \hbar = \frac{n h}{2\pi} \quad (n = 1, 2, 3,\dots)$",
            r"$L = n h$",
            r"$L = \frac{\hbar}{n}$",
            r"$L = n^2 \hbar$",
            "(a)",
            r"Bohr's quantization postulate requires angular momentum to be an integer multiple of Dirac's constant: $L = n\hbar$."
        ),
        (
            r"Bohr's angular momentum quantization $m v r = n\hbar$ is physically explained by de Broglie matter waves as:",
            r"The requirement that the circumference of the electron orbit must fit an exact integer number of de Broglie wavelengths ($2\pi r = n\lambda$)",
            r"Total internal reflection inside the proton",
            r"Relativistic mass increase",
            r"Heisenberg momentum cutoff",
            "(a)",
            r"$2\pi r = n\lambda = n(h/p) = n(h/mv) \implies mvr = n(h/2\pi) = n\hbar$, forming constructive standing waves around the circular orbit."
        ),
        (
            r"The radius of the first Bohr orbit $a_0$ in hydrogen is given by:",
            r"$a_0 = \frac{4\pi \epsilon_0 \hbar^2}{m_e e^2} \approx 0.529\text{ \AA} = 0.0529\text{ nm}$",
            r"$a_0 = 0.0529\text{ \AA}$",
            r"$a_0 = 5.29\text{ nm}$",
            r"$a_0 = 1.00\text{ \AA}$",
            "(a)",
            r"Evaluating with fundamental constants: $a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_e e^2} \approx 0.529177\text{ \AA}$."
        ),
        (
            r"The ionization energy of hydrogen in its ground state ($n=1$) is:",
            r"$13.6\text{ eV}$",
            r"$3.4\text{ eV}$",
            r"$1.51\text{ eV}$",
            r"$54.4\text{ eV}$",
            "(a)",
            r"Ground-state energy is $E_1 = -13.6\text{ eV}$, so the minimum energy required to remove the electron to infinity is $+13.6\text{ eV}$."
        ),
        (
            r"The Rydberg constant $R_\infty = \frac{m_e e^4}{8 \epsilon_0^2 h^3 c}$ has the approximate value:",
            r"$1.097 \times 10^7\text{ m}^{-1}$",
            r"$1.097 \times 10^5\text{ m}^{-1}$",
            r"$3.29 \times 10^{15}\text{ Hz}$",
            r"$6.626 \times 10^{-34}\text{ J}\cdot\text{s}$",
            "(a)",
            r"The Rydberg constant for infinite nuclear mass is $R_\infty \approx 1.097373 \times 10^7\text{ m}^{-1}$."
        ),
        (
            r"The Lyman spectral series of hydrogen occurs in which region of the electromagnetic spectrum?",
            r"Ultraviolet (UV)",
            r"Visible",
            r"Infrared (IR)",
            r"Far-Infrared",
            "(a)",
            r"Transitions terminating at ground state $n=1$ ($n \to 1$) form the Lyman series in the ultraviolet ($\lambda = 91\text{--}121\text{ nm}$)."
        ),
        (
            r"The Balmer spectral series of hydrogen ($n \to 2$) is unique because:",
            r"Its principal emission lines ($H_\alpha, H_\beta, H_\gamma, H_\delta$) lie directly in the visible light spectrum ($400\text{--}700\text{ nm}$)",
            r"It emits X-rays only",
            r"It has zero transition probability",
            r"It requires nuclear fission",
            "(a)",
            r"The Balmer series ($H_\alpha = 656.3\text{ nm}, H_\beta = 486.1\text{ nm}$) spans the visible spectrum."
        ),
        (
            r"If a quantum state is a linear superposition $\Psi(x) = c_1 \psi_1(x) + c_2 \psi_2(x)$, the probability of measuring energy $E_1$ is:",
            r"$|c_1|^2$",
            r"$|c_1|$",
            r"$c_1 + c_2$",
            r"$|c_1|^2 / |c_2|^2$",
            "(a)",
            r"According to the Born probability postulate, probability of finding eigenvalue $E_1$ is given by the squared modulus $|c_1|^2$."
        ),
        (
            r"The parity of the wave function $\psi_n(x)$ in a symmetric potential $V(-x) = V(x)$ is:",
            r"Even for $n=1, 3, 5\dots$ (odd $n$) and odd for $n=2, 4, 6\dots$ (even $n$)",
            r"Always positive",
            r"Always negative",
            r"Undefined",
            "(a)",
            r"Symmetric wells yield strictly alternating parity eigenfunctions: $\psi_1(-x) = +\psi_1(x)$ (even), $\psi_2(-x) = -\psi_2(x)$ (odd)."
        ),
        (
            r"The degeneracy of the energy level $E = 14 E_1$ for a particle in a 3D cubical box ($n_x^2 + n_y^2 + n_z^2 = 14$) is:",
            r"$6$-fold degenerate",
            r"$3$-fold degenerate",
            r"$1$-fold (non-degenerate)",
            r"$12$-fold degenerate",
            "(a)",
            r"$14 = 1^2 + 2^2 + 3^2$. Six distinct permutations $(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)$ give $6$-fold degeneracy."
        ),
        (
            r"The expectation value $\langle p_x^2 \rangle$ for state $\psi_n(x)$ in a 1D box of width $L$ is:",
            r"$\frac{n^2 \pi^2 \hbar^2}{L^2}$",
            r"$0$",
            r"$\frac{n \pi \hbar}{L}$",
            r"$\frac{n^2 h^2}{4L^2}$",
            "(a)",
            r"$\langle p_x^2 \rangle = 2m E_n = 2m \left(\frac{n^2 \pi^2 \hbar^2}{2m L^2}\right) = \frac{n^2 \pi^2 \hbar^2}{L^2}$."
        ),

        # Part III: Advanced Mastery (81-100)
        (
            r"The time evolution of a non-stationary state $\Psi(x,t) = \frac{1}{\sqrt{2}}\psi_1(x)e^{-iE_1 t/\hbar} + \frac{1}{\sqrt{2}}\psi_2(x)e^{-iE_2 t/\hbar}$ produces a probability density $|\Psi(x,t)|^2$ that oscillates in time with angular frequency:",
            r"$\omega_{21} = \frac{E_2 - E_1}{\hbar}$ (Bohr transition frequency)",
            r"$\omega = \frac{E_1 + E_2}{\hbar}$",
            r"$\omega = 0$ (static)",
            r"$\omega = \frac{E_2}{\hbar}$",
            "(a)",
            r"$|\Psi(x,t)|^2 = \frac{1}{2}|\psi_1|^2 + \frac{1}{2}|\psi_2|^2 + \psi_1\psi_2\cos(\frac{E_2-E_1}{\hbar}t)$, demonstrating quantum beat oscillation."
        ),
        (
            r"In the WKB (Wentzel-Kramers-Brillouin) semiclassical approximation, the transmission probability $T$ through an arbitrary potential barrier $V(x) > E$ between turning points $x_1$ and $x_2$ is:",
            r"$T \approx \exp\left( -2\int_{x_1}^{x_2} \sqrt{\frac{2m(V(x) - E)}{\hbar^2}} dx \right)$",
            r"$T \approx \exp\left( +\int_{x_1}^{x_2} V(x) dx \right)$",
            r"$T = 0$",
            r"$T = 1 - \frac{V_0}{E}$",
            "(a)",
            r"The Gamow WKB barrier penetration formula is $T \approx \exp(-2\int_{x_1}^{x_2} \kappa(x) dx)$."
        ),
        (
            r"George Gamow applied the quantum tunneling barrier penetration formula to explain:",
            r"Alpha ($\alpha$) decay lifetimes of radioactive heavy nuclei (Geiger-Nuttall law)",
            r"Beta decay spectrum",
            r"Gamma ray emission",
            r"Cosmic ray creation",
            "(a)",
            r"Gamow proved that $\alpha$-particles tunnel through the nuclear Coulomb barrier, explaining half-lives spanning $10^{10}\text{ years}$ to $10^{-7}\text{ s}$."
        ),
        (
            r"The Dirac delta function potential $V(x) = -\alpha \delta(x)$ with $\alpha > 0$ supports:",
            r"Exactly one single bound state with energy $E = -\frac{m\alpha^2}{2\hbar^2}$",
            r"Infinite bound states",
            r"Zero bound states",
            r"Two degenerate bound states",
            "(a)",
            r"Solving the discontinuity in derivative at $x=0$ yields a single normalized bound state $\psi(x) = \sqrt{\kappa}e^{-\kappa|x|}$ with $E = -\frac{m\alpha^2}{2\hbar^2}$."
        ),
        (
            r"For a particle in a finite square well of depth $V_0$ and width $2a$, bound states require:",
            r"$\psi(x)$ to oscillate sinusoidally inside the well ($|x| < a$) and decay exponentially outside ($|x| > a$)",
            r"$\psi(x) = 0$ outside the well",
            r"$\psi(x)$ to be infinite at boundaries",
            r"Energy $E > V_0$",
            "(a)",
            r"Bound states ($E < V_0$) have sinusoidal standing waves inside the well and decaying evanescent tails outside, creating penetrating probability."
        ),
        (
            r"As the potential barrier height $V_0 \to \infty$, the energy eigenvalues of a finite square well:",
            r"Converge continuously to the eigenvalues of the infinite potential well $E_n = \frac{n^2 h^2}{8mL^2}$",
            r"Drop to zero",
            r"Become negative",
            r"Become continuous",
            "(a)",
            r"In the limit $V_0 \to \infty$, the penetration depth $d = 1/\kappa \to 0$, perfectly recovering the infinite well boundary conditions."
        ),
        (
            r"The Pauli Exclusion Principle states that:",
            r"Two identical fermions (half-integer spin particles, such as electrons) cannot occupy the exact same quantum state simultaneously",
            r"All bosons must have distinct energies",
            r"Electrons have infinite mass",
            r"Photons cannot share the same mode",
            "(a)",
            r"Total wavefunctions of identical fermions must be anti-symmetric under particle exchange: $\Psi(1,2) = -\Psi(2,1)$."
        ),
        (
            r"Particles with integer spin ($s = 0, 1, 2,\dots$) that obey Bose-Einstein statistics and can occupy the same quantum state in unlimited numbers are called:",
            r"Bosons (e.g., photons, gluons, $^4\text{He}$ atoms)",
            r"Fermions",
            r"Quarks",
            r"Leptons",
            "(a)",
            r"Bosons have symmetric wavefunctions $\Psi(1,2) = +\Psi(2,1)$ and can condense into a single ground state (Bose-Einstein Condensation)."
        ),
        (
            r"The Fermi energy $E_F(0)$ of a 3D degenerate free electron gas at $T=0\text{ K}$ with electron density $n = N/V$ is:",
            r"$E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$",
            r"$E_F = \frac{\hbar^2}{2m}(2\pi^2 n)^{1/2}$",
            r"$E_F = \frac{h^2}{8m} n$",
            r"$E_F = \frac{3}{5} n k_B T$",
            "(a)",
            r"Integrating density of states $g(E) = \frac{V}{2\pi^2}(\frac{2m}{\hbar^2})^{3/2}\sqrt{E}$ up to $E_F$ gives $E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$."
        ),
        (
            r"The average energy per electron $\langle E \rangle$ in a 3D free electron gas at $T=0\text{ K}$ in terms of Fermi energy $E_F$ is:",
            r"$\langle E \rangle = \frac{3}{5} E_F$",
            r"$\langle E \rangle = \frac{1}{2} E_F$",
            r"$\langle E \rangle = E_F$",
            r"$\langle E \rangle = \frac{5}{3} E_F$",
            "(a)",
            r"$\langle E \rangle = \frac{1}{N}\int_0^{E_F} E g(E) dE = \frac{\int_0^{E_F} E^{3/2} dE}{\int_0^{E_F} E^{1/2} dE} = \frac{\frac{2}{5}E_F^{5/2}}{\frac{2}{3}E_F^{3/2}} = \frac{3}{5}E_F$."
        ),
        (
            r"In the Kronig-Penney model of a periodic crystal lattice, energy band gaps appear because:",
            r"Destructive Bragg reflection of electron matter waves occurs at Brillouin zone boundaries ($k = \pm n\pi/a$)",
            r"Electrons collide with nuclei and stop",
            r"Lattice ions absorb all kinetic energy",
            r"The speed of light drops to zero",
            "(a)",
            r"At $k = \pm n\pi/a$, standing wave formation splits the energy into two distinct levels depending on charge distribution, creating band gaps."
        ),
        (
            r"The effective mass $m^*$ of an electron in a crystal energy band $E(k)$ is defined by:",
            r"$m^* = \hbar^2 \left( \frac{d^2 E}{dk^2} \right)^{-1}$",
            r"$m^* = \frac{1}{\hbar}\frac{dE}{dk}$",
            r"$m^* = \hbar^2 \frac{d^2 E}{dk^2}$",
            r"$m^* = \frac{E}{c^2}$",
            "(a)",
            r"Applying semi-classical acceleration $a = \frac{1}{\hbar}\frac{d v_g}{dt} = \frac{1}{\hbar^2}\frac{d^2 E}{dk^2} F \implies m^* = \frac{\hbar^2}{d^2E/dk^2}$."
        ),
        (
            r"Near the top of a valence band where the curvature $\frac{d^2 E}{dk^2} < 0$, the effective mass $m^*$ is:",
            r"Negative ($m^* < 0$), which is physically treated as a positively charged 'hole'",
            r"Infinite",
            r"Zero",
            r"Equal to free electron mass $m_0$",
            "(a)",
            r"Negative curvature implies deceleration under forward electric force; treating missing electrons as positive 'holes' restores standard equations."
        ),
        (
            r"The density of states $g(E)$ for a 1D quantum wire scales with energy $E$ as:",
            r"$g_{\text{1D}}(E) \propto E^{-1/2}$",
            r"$g_{\text{2D}}(E) = \text{constant}$",
            r"$g_{\text{3D}}(E) \propto E^{+1/2}$",
            r"All of the above statements are correct",
            "(d)",
            r"Quantum confinement dimensions scale as: 3D ($\sqrt{E}$), 2D (step constant), 1D ($E^{-1/2}$ singularity), 0D (discrete delta functions)."
        ),
        (
            r"In quantum dots (0D nanocrystals), the density of states is represented by:",
            r"A series of discrete delta functions $\sum \delta(E - E_i)$ (atomic-like sharp levels)",
            r"A smooth parabolic curve",
            r"A continuous line",
            r"Zero everywhere",
            "(a)",
            r"Confinement in all three spatial dimensions collapses energy bands into discrete atomic-like delta function energy levels."
        ),
        (
            r"A quantum well has width $L = 5.0\text{ nm}$ in GaAs ($m_e^* = 0.067 m_0$). The ground-state subband energy $E_1$ for electrons is approximately:",
            r"$22.5\text{ meV}$",
            r"$2.25\text{ eV}$",
            r"$225\text{ meV}$",
            r"$0.225\text{ meV}$",
            "(a)",
            r"$E_1 = \frac{h^2}{8 m_e^* L^2} = \frac{(6.626 \times 10^{-34})^2}{8(0.067 \times 9.109 \times 10^{-31})(5 \times 10^{-9})^2} \approx 3.60 \times 10^{-21}\text{ J} \approx 22.5\text{ meV}$."
        ),
        (
            r"The Klein-Gordon equation is a relativistic wave equation that describes:",
            r"Spin-$0$ relativistic scalar bosons (such as pions and Higgs bosons)",
            r"Spin-$1/2$ electrons",
            r"Photons exclusively",
            r"Classical fluid particles",
            "(a)",
            r"$\nabla^2\psi - \frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2} = \frac{m^2 c^2}{\hbar^2}\psi$ applies to relativistic spin-0 particles."
        ),
        (
            r"The Dirac equation in relativistic quantum mechanics successfully predicted the existence of:",
            r"Antimatter (the positron $e^+$) and electron intrinsic spin $s = 1/2$",
            r"Dark energy",
            r"Black holes",
            r"Sound waves",
            "(a)",
            r"Paul Dirac's relativistic linear equation $i\hbar\gamma^\mu\partial_\mu\psi = mc\psi$ naturally revealed electron spin and antiparticles."
        ),
        (
            r"The Aharonov-Bohm effect proves that in quantum mechanics:",
            r"The electromagnetic vector potential $\vec{A}$ has physical, gauge-invariant reality and alters electron phase even in regions where $\vec{B} = 0$",
            r"Magnetic fields do not exist",
            r"Phase cannot be measured",
            r"Electric charge is not conserved",
            "(a)",
            r"Electrons passing outside a shielded solenoid acquire a measurable phase shift $\Delta\phi = \frac{q}{\hbar}\oint \vec{A}\cdot d\vec{l} = \frac{q\Phi_B}{\hbar}$."
        ),
        (
            r"Quantum entanglement describes a multi-particle state where:",
            r"The quantum state of each particle cannot be described independently of the state of the other particles, regardless of spatial separation",
            r"Particles are physically glued together with glue",
            r"Electrons have infinite charge",
            r"Light speeds up to infinity",
            "(a)",
            r"Entangled particles exhibit non-local quantum correlations violating Bell's inequalities (Einstein-Podolsky-Rosen paradox)."
        )
    ]
    
    theory_qs = [
        (
            r"State the de Broglie hypothesis of matter waves. Derive the expression for the de Broglie wavelength of an electron accelerated from rest through a potential difference $V$. Describe the Davisson-Germer experiment and explain how it confirmed matter waves.",
            r"""\textbf{1. The de Broglie Hypothesis}:
In 1924, Louis de Broglie postulated that dual wave-particle behavior is a fundamental universal property of all matter. Any moving physical entity of linear momentum $p$ is accompanied by a matter wave of wavelength:
\begin{equation}
\mathbf{\lambda = \frac{h}{p}}
\end{equation}

\textbf{2. Derivation for Electrostatic Acceleration}:
Let an electron of rest mass $m_e$ and charge $e$ be accelerated from rest through a potential difference $V$.
The electrical work done on the electron equals its kinetic energy $E_k$:
\begin{equation}
E_k = e V = \frac{1}{2}m_e v^2 = \frac{p^2}{2m_e} \implies p = \sqrt{2 m_e e V}
\end{equation}
Substituting this into the de Broglie formula:
\begin{equation}
\lambda = \frac{h}{\sqrt{2 m_e e V}}
\end{equation}
Substituting fundamental constants ($h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$, $m_e = 9.109 \times 10^{-31}\text{ kg}$, $e = 1.602 \times 10^{-19}\text{ C}$):
\begin{equation}
\mathbf{\lambda = \frac{1.227 \times 10^{-9}\text{ m}}{\sqrt{V}} = \frac{1.227}{\sqrt{V}}\text{ nm} = \frac{12.27}{\sqrt{V}}\text{ \AA}}
\end{equation}

\textbf{3. The Davisson-Germer Experiment}:
\begin{itemize}
    \item \textbf{Setup}: A collimated beam of electrons from a heated tungsten filament was accelerated through variable voltage $V$ onto the cleaved $(111)$ face of a single nickel crystal. Scattered electrons were collected at various scattering angles $\phi$ by a movable Faraday cup detector.
    \item \textbf{Key Observation}: At $V = 54\text{ V}$, an intense, sharp diffraction peak was recorded at scattering angle $\phi = 50^\circ$.
    \item \textbf{Verification via Bragg's Law}:
    The glancing angle with crystal planes (interplanar spacing $d = 0.091\text{ nm}$) was $\theta = 90^\circ - \phi/2 = 90^\circ - 25^\circ = 65^\circ$.
    Bragg's diffraction condition for first order ($n=1$):
    \begin{equation}
    \lambda_{\text{Bragg}} = 2 d \sin\theta = 2(0.091\text{ nm})\sin(65^\circ) = 2(0.091)(0.9063) \approx \mathbf{0.165\text{ nm}}
    \end{equation}
    \item \textbf{Theoretical de Broglie Value}:
    \begin{equation}
    \lambda_{\text{theory}} = \frac{1.227}{\sqrt{54}}\text{ nm} = \frac{1.227}{7.348} \approx \mathbf{0.167\text{ nm}}
    \end{equation}
    The experimental Bragg wavelength ($0.165\text{ nm}$) matched de Broglie's prediction ($0.167\text{ nm}$) to within $1\%$, providing direct experimental proof of matter waves.
\end{itemize}"""
        ),
        (
            r"Define Phase Velocity ($v_p$) and Group Velocity ($v_g$). Derive the general relationship between group velocity and particle velocity ($v_g = v_{\text{particle}}$) for both non-relativistic and relativistic matter waves. Show that $v_p \cdot v_g = c^2$.",
            r"""\textbf{1. Definitions}:
\begin{itemize}
    \item \textbf{Phase Velocity ($v_p$)}: The speed at which individual monochromatic wave crests and troughs propagate through space:
    \begin{equation}
    \mathbf{v_p = \frac{\omega}{k}}
    \end{equation}
    \item \textbf{Group Velocity ($v_g$)}: The speed at which the overall envelope modulating a localized wave packet propagates through space (the velocity of energy and information transport):
    \begin{equation}
    \mathbf{v_g = \frac{d\omega}{dk}}
    \end{equation}
\end{itemize}

\textbf{2. Proof of $v_g = v_{\text{particle}}$ (Non-Relativistic)}:
For a free particle of mass $m$ and velocity $v$:
Total energy $E = \hbar\omega = \frac{p^2}{2m} = \frac{\hbar^2 k^2}{2m} \implies \omega(k) = \frac{\hbar k^2}{2m}$.
Differentiating with respect to $k$:
\begin{equation}
\mathbf{v_g = \frac{d\omega}{dk} = \frac{\hbar(2k)}{2m} = \frac{\hbar k}{m} = \frac{p}{m} = v_{\text{particle}}}
\end{equation}
Phase velocity is $v_p = \frac{\omega}{k} = \frac{\hbar k}{2m} = \frac{v_{\text{particle}}}{2}$.

\textbf{3. Proof of $v_g = v_{\text{particle}}$ & $v_p \cdot v_g = c^2$ (Relativistic)}:
According to special relativity:
\begin{equation}
E^2 = p^2 c^2 + m_0^2 c^4 \implies \hbar^2 \omega^2 = \hbar^2 k^2 c^2 + m_0^2 c^4
\end{equation}
Differentiating both sides with respect to $k$:
\begin{equation}
2\hbar^2 \omega \frac{d\omega}{dk} = 2\hbar^2 k c^2 \implies \frac{d\omega}{dk} = c^2 \left(\frac{k}{\omega}\right) = \frac{c^2}{v_p}
\end{equation}
Rearranging:
\begin{equation}
\mathbf{v_p \cdot v_g = c^2}
\end{equation}
Since $E = \hbar\omega = \gamma m_0 c^2$ and $p = \hbar k = \gamma m_0 v$:
\begin{align}
v_p &= \frac{\omega}{k} = \frac{\hbar\omega}{\hbar k} = \frac{\gamma m_0 c^2}{\gamma m_0 v} = \frac{c^2}{v} \\
v_g &= \frac{c^2}{v_p} = \frac{c^2}{c^2/v} = \mathbf{v_{\text{particle}}}
\end{align}
\textit{Conclusion}: The group velocity of the quantum wave packet moves at the physical particle speed $v$, while the phase velocity $v_p = c^2/v > c$ exceeds light speed without violating causality."""
        ),
        (
            r"State Heisenberg's Uncertainty Principle for position and momentum. Use it to prove analytically that electrons cannot reside inside an atomic nucleus. Estimate the ground-state energy of a hydrogen atom using the uncertainty principle.",
            r"""\textbf{1. Statement}:
Heisenberg's Uncertainty Principle states that it is physically impossible to measure simultaneously the exact position $x$ and linear momentum $p_x$ of a particle with unlimited precision:
\begin{equation}
\mathbf{\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}}
\end{equation}

\textbf{2. Proof of Non-Existence of Electrons Inside the Nucleus}:
Typical nuclear diameter is $D \sim 10^{-14}\text{ m}$. If an electron exists inside the nucleus, its position uncertainty is at most $\Delta x \approx 10^{-14}\text{ m}$.
By Heisenberg's principle:
\begin{equation}
\Delta p_x \ge \frac{\hbar}{2\Delta x} \approx \frac{1.0545 \times 10^{-34}\text{ J}\cdot\text{s}}{2(10^{-14}\text{ m})} \approx 5.27 \times 10^{-21}\text{ kg}\cdot\text{m/s}
\end{equation}
Because momentum must be at least comparable to uncertainty ($p \ge \Delta p_x$):
Calculating relativistic kinetic energy:
\begin{align*}
E &\approx p c = (5.27 \times 10^{-21}\text{ kg}\cdot\text{m/s})(3 \times 10^8\text{ m/s}) \approx 1.58 \times 10^{-12}\text{ J} \\
E &= \frac{1.58 \times 10^{-12}\text{ J}}{1.602 \times 10^{-19}\text{ J/eV}} \approx 9.87 \times 10^6\text{ eV} \approx \mathbf{10\text{--}20\text{ MeV}}
\end{align*}
However, beta-decay electrons emitted from radioactive nuclei possess energies of only $2\text{--}4\text{ MeV}$. If electrons were permanently bound inside the nucleus, their energies would have to exceed $20\text{ MeV}$. This contradiction proves that electrons cannot exist inside the nucleus.

\textbf{3. Ground-State Energy of Hydrogen Atom}:
Let the electron be confined within distance $r$ from the proton ($\Delta x \approx r$).
Then momentum uncertainty is $p \approx \Delta p \approx \frac{\hbar}{r}$.
Total energy of the hydrogen atom is:
\begin{equation}
E(r) = E_k + V = \frac{p^2}{2m} - \frac{e^2}{4\pi\epsilon_0 r} = \frac{\hbar^2}{2m r^2} - \frac{e^2}{4\pi\epsilon_0 r}
\end{equation}
To find the stable ground state, minimize $E(r)$ with respect to $r$:
\begin{equation}
\frac{dE}{dr} = -\frac{\hbar^2}{m r^3} + \frac{e^2}{4\pi\epsilon_0 r^2} = 0 \implies \mathbf{r_0 = \frac{4\pi\epsilon_0 \hbar^2}{m e^2} = a_0 \approx 0.529\text{ \AA}}
\end{equation}
Substituting $r_0$ back into $E(r)$ gives the exact ground state energy:
\begin{equation}
\mathbf{E_1 = -\frac{m e^4}{32\pi^2\epsilon_0^2\hbar^2} = -13.6\text{ eV}}
\end{equation}"""
        ),
        (
            r"Explain the physical significance of the quantum mechanical wave function $\Psi(x,t)$. Detail Max Born's probability interpretation, the normalization condition, and the four mathematical boundary conditions for physically acceptable wave functions.",
            r"""\textbf{1. Physical Interpretation of $\Psi(x,t)$}:
In quantum mechanics, the state of a physical system is completely specified by a complex wave function $\Psi(x,t)$.
While $\Psi$ itself has no direct classical counterpart and is not directly measurable, its squared magnitude carries direct physical meaning.

\textbf{2. Max Born's Statistical Postulate}:
The probability of finding a particle in an infinitesimal spatial interval $dx$ at time $t$ is proportional to the square of the modulus of the wave function:
\begin{equation}
\mathbf{dP(x,t) = |\Psi(x,t)|^2 dx = \Psi^*(x,t)\Psi(x,t) dx}
\end{equation}
where $P(x,t) = |\Psi(x,t)|^2$ is the \textbf{Probability Density}.

\textbf{3. Normalization Condition}:
Because the particle must exist somewhere along the 1D space with certainty ($100\%$ probability):
\begin{equation}
\mathbf{\int_{-\infty}^{+\infty} |\Psi(x,t)|^2 dx = 1}
\end{equation}

\textbf{4. Four Mathematical Boundary Conditions for Acceptable $\Psi(x)$}:
To ensure physical realism and conservation of probability, $\psi(x)$ must satisfy:
\begin{enumerate}
    \item \textbf{Single-Valued}: $\psi(x)$ must have only one unique value at any given spatial coordinate $x$ so that probability density $|\psi(x)|^2$ is unambiguously defined.
    \item \textbf{Continuous Everywhere}: $\psi(x)$ must be spatially continuous across all boundaries ($\lim_{\epsilon\to 0}\psi(x_0+\epsilon) = \lim_{\epsilon\to 0}\psi(x_0-\epsilon)$).
    \item \textbf{Continuous First Derivative}: $\frac{d\psi}{dx}$ must be continuous everywhere for all finite potential potentials $V(x)$, ensuring momentum is uniquely defined.
    \item \textbf{Square-Integrable (Finite Everywhere)}: $\psi(x)$ must vanish as $x \to \pm\infty$ ($\lim_{x\to\pm\infty}\psi(x) = 0$) so that the total probability integral remains finite and normalizable."""
        ),
        (
            r"Derive the 1D Time-Independent Schrödinger Equation (TISE) from the Time-Dependent Schrödinger Equation (TDSE) by the method of separation of variables. Define stationary states.",
            r"""\textbf{1. Time-Dependent Schrödinger Equation (TDSE)}:
For a particle of mass $m$ in a time-independent potential $V(x)$:
\begin{equation}
i\hbar \frac{\partial \Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi(x,t)}{\partial x^2} + V(x)\Psi(x,t)
\end{equation}

\textbf{2. Separation of Variables}:
Assume a separable product solution:
\begin{equation}
\Psi(x,t) = \psi(x) \phi(t)
\end{equation}
Compute partial derivatives:
\begin{equation}
\frac{\partial \Psi}{\partial t} = \psi(x)\frac{d\phi(t)}{dt}, \qquad \frac{\partial^2 \Psi}{\partial x^2} = \phi(t)\frac{d^2\psi(x)}{dx^2}
\end{equation}
Substitute these into the TDSE:
\begin{equation}
i\hbar \psi(x)\frac{d\phi(t)}{dt} = -\frac{\hbar^2}{2m}\phi(t)\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x)\phi(t)
\end{equation}
Divide the entire equation by $\Psi(x,t) = \psi(x)\phi(t)$:
\begin{equation}
i\hbar \frac{1}{\phi(t)}\frac{d\phi(t)}{dt} = \frac{1}{\psi(x)}\left[ -\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) \right]
\end{equation}
The left side depends solely on time $t$, while the right side depends solely on position $x$. For this to hold for all $x$ and $t$, both sides must equal a common separation constant $E$ (Total Energy):

\textbf{3. Spatial Equation (TISE)}:
\begin{equation}
\mathbf{-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x) \iff \hat{H}\psi = E\psi}
\end{equation}

\textbf{4. Temporal Equation & Stationary States}:
\begin{equation}
i\hbar \frac{d\phi(t)}{dt} = E\phi(t) \implies \frac{d\phi}{\phi} = -\frac{i E}{\hbar}dt \implies \mathbf{\phi(t) = e^{-i E t/\hbar}}
\end{equation}
The full wavefunction is $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$.
\textit{Stationary State}: The probability density is strictly static in time:
\begin{equation}
P(x,t) = |\Psi(x,t)|^2 = |\psi(x)|^2 |e^{-iEt/\hbar}|^2 = |\psi(x)|^2
\end{equation}"""
        ),
        (
            r"Solve the Time-Independent Schrödinger Equation for a particle of mass $m$ trapped in a 1D Infinite Potential Well of width $L$ ($V(x) = 0$ for $0 < x < L$ and $V(x) = \infty$ elsewhere). Derive the quantized energy eigenvalues $E_n$ and normalized eigenfunctions $\psi_n(x)$.",
            r"""\textbf{1. Model Formulation & Boundary Conditions}:
Potential profile:
\begin{equation}
V(x) = \begin{cases} 0 & 0 < x < L \\ \infty & x \le 0 \text{ or } x \ge L \end{cases}
\end{equation}
Since $V = \infty$ outside the well, the particle cannot penetrate outside: $\psi(x) = 0$ for $x \le 0$ and $x \ge L$.
Continuity of $\psi$ requires boundary conditions:
\begin{equation}
\psi(0) = 0 \quad \text{and} \quad \psi(L) = 0
\end{equation}

\textbf{2. General Solution Inside the Well ($0 < x < L$)}:
Since $V(x) = 0$, the TISE is:
\begin{equation}
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \implies \frac{d^2\psi}{dx^2} + k^2\psi = 0
\end{equation}
where $k = \frac{\sqrt{2mE}}{\hbar}$.
The general solution is:
\begin{equation}
\psi(x) = A\sin(kx) + B\cos(kx)
\end{equation}

\textbf{3. Applying Boundary Conditions}:
\begin{enumerate}
    \item At $x = 0$: $\psi(0) = A\sin(0) + B\cos(0) = B = 0 \implies B = 0$.
    \item Thus $\psi(x) = A\sin(kx)$.
    \item At $x = L$: $\psi(L) = A\sin(kL) = 0$.
    Since $A \ne 0$ (otherwise $\psi=0$ identically), we must have:
    \begin{equation}
    k L = n\pi \implies \mathbf{k_n = \frac{n\pi}{L} \quad (n = 1, 2, 3,\dots)}
    \end{equation}
\end{enumerate}

\textbf{4. Quantized Energy Eigenvalues $E_n$}:
\begin{equation}
E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{\hbar^2}{2m}\left(\frac{n\pi}{L}\right)^2 = \mathbf{\frac{n^2 \pi^2 \hbar^2}{2m L^2} = \frac{n^2 h^2}{8m L^2}} \quad (n = 1, 2, 3,\dots)
\end{equation}

\textbf{5. Normalization of Eigenfunctions}:
\begin{align*}
\int_0^L |\psi_n(x)|^2 dx = 1 &\implies A^2 \int_0^L \sin^2\left(\frac{n\pi x}{L}\right)dx = 1 \\
A^2 \int_0^L \frac{1 - \cos(2n\pi x/L)}{2}dx &= A^2 \left(\frac{L}{2}\right) = 1 \implies \mathbf{A = \sqrt{\frac{2}{L}}}
\end{align*}
The complete \textbf{Normalized Wavefunctions} are:
\begin{equation}
\mathbf{\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)}
\end{equation}"""
        ),
        (
            r"For a particle in the ground state ($n=1$) of a 1D box of width $L$, calculate the expectation values $\langle x \rangle, \langle x^2 \rangle, \langle p_x \rangle,$ and $\langle p_x^2 \rangle$. Verify that $\Delta x \cdot \Delta p_x \ge \hbar/2$.",
            r"""\textbf{1. Wavefunction}:
$\psi_1(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{\pi x}{L}\right)$ for $0 \le x \le L$.

\textbf{2. Position Expectation Values}:
\begin{itemize}
    \item $\langle x \rangle$:
    \begin{equation}
    \langle x \rangle = \int_0^L \psi_1^* x \psi_1 dx = \frac{2}{L}\int_0^L x \sin^2\left(\frac{\pi x}{L}\right)dx = \mathbf{\frac{L}{2}}
    \end{equation}
    \item $\langle x^2 \rangle$:
    Using identity $\sin^2\theta = \frac{1-\cos 2\theta}{2}$ and integrating by parts:
    \begin{equation}
    \langle x^2 \rangle = \frac{2}{L}\int_0^L x^2 \left[\frac{1 - \cos(2\pi x/L)}{2}\right]dx = \mathbf{L^2 \left( \frac{1}{3} - \frac{1}{2\pi^2} \right)} \approx 0.2827 L^2
    \end{equation}
    \item Position uncertainty $\Delta x$:
    \begin{equation}
    (\Delta x)^2 = \langle x^2 \rangle - \langle x \rangle^2 = L^2\left(\frac{1}{3} - \frac{1}{2\pi^2}\right) - \frac{L^2}{4} = L^2\left(\frac{1}{12} - \frac{1}{2\pi^2}\right) \approx \mathbf{0.03267 L^2} \implies \Delta x \approx 0.1807 L
    \end{equation}
\end{itemize}

\textbf{3. Momentum Expectation Values}:
\begin{itemize}
    \item $\langle p_x \rangle$:
    \begin{equation}
    \langle p_x \rangle = \int_0^L \psi_1^* \left(-i\hbar\frac{d}{dx}\right)\psi_1 dx = -\frac{2i\hbar\pi}{L^2}\int_0^L \sin\left(\frac{\pi x}{L}\right)\cos\left(\frac{\pi x}{L}\right)dx = \mathbf{0}
    \end{equation}
    \item $\langle p_x^2 \rangle$:
    \begin{equation}
    \langle p_x^2 \rangle = \int_0^L \psi_1^* \left(-\hbar^2\frac{d^2}{dx^2}\right)\psi_1 dx = \frac{\pi^2\hbar^2}{L^2}\int_0^L \psi_1^2 dx = \mathbf{\frac{\pi^2\hbar^2}{L^2}}
    \end{equation}
    \item Momentum uncertainty $\Delta p_x$:
    \begin{equation}
    \Delta p_x = \sqrt{\langle p_x^2 \rangle - \langle p_x \rangle^2} = \mathbf{\frac{\pi\hbar}{L}}
    \end{equation}
\end{itemize}

\textbf{4. Uncertainty Product Verification}:
\begin{equation}
\mathbf{\Delta x \cdot \Delta p_x = (0.1807 L)\left(\frac{\pi\hbar}{L}\right) = 0.1807 \pi \hbar \approx 0.568 \hbar}
\end{equation}
Since $0.568\hbar > 0.500\hbar$ ($\hbar/2$), Heisenberg's Uncertainty Principle is rigorously satisfied."""
        ),
        (
            r"Extend the Schrödinger equation to a 3D rectangular box ($a \times b \times c$) and cubical box ($L \times L \times L$). Derive the energy eigenvalues and explain the physical concept of energy degeneracy with specific examples.",
            r"""\textbf{1. 3D Potential Well & Separation of Variables}:
Potential $V(x,y,z) = 0$ inside $0 < x < a, 0 < y < b, 0 < z < c$, and $\infty$ elsewhere.
The 3D TISE is:
\begin{equation}
-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)\psi(x,y,z) = E\psi(x,y,z)
\end{equation}
Substituting $\psi(x,y,z) = X(x)Y(y)Z(z)$ and $E = E_x + E_y + E_z$:
Applying boundary conditions at each face yields:
\begin{equation}
\mathbf{\psi_{n_x,n_y,n_z}(x,y,z) = \sqrt{\frac{8}{a b c}}\sin\left(\frac{n_x\pi x}{a}\right)\sin\left(\frac{n_y\pi y}{b}\right)\sin\left(\frac{n_z\pi z}{c}\right)}
\end{equation}
where $n_x, n_y, n_z \in \{1, 2, 3,\dots\}$.

\textbf{2. Energy Eigenvalues}:
\begin{equation}
\mathbf{E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left( \frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2} \right)}
\end{equation}

\textbf{3. Cubical Box ($a = b = c = L$)}:
\begin{equation}
\mathbf{E = \frac{h^2}{8mL^2}(n_x^2 + n_y^2 + n_z^2) = E_1(n_x^2 + n_y^2 + n_z^2)}
\end{equation}
where $E_1 = \frac{h^2}{8mL^2}$.

\textbf{4. Concept of Energy Degeneracy}:
Degeneracy is the condition where two or more linearly independent quantum eigenfunctions share the exact same energy eigenvalue:
\begin{itemize}
    \item \textbf{Ground State}: $(1,1,1) \implies E = 3E_1$ (\textbf{Non-degenerate}, $g=1$).
    \item \textbf{First Excited State}: $n_x^2+n_y^2+n_z^2 = 1^2+1^2+2^2 = 6 \implies E = 6E_1$.
    Three distinct states: $(2,1,1), (1,2,1), (1,1,2)$ (\textbf{3-fold degenerate}, $g=3$).
    \item \textbf{Second Excited State}: $n_x^2+n_y^2+n_z^2 = 1^2+2^2+2^2 = 9 \implies E = 9E_1$.
    Three distinct states: $(1,2,2), (2,1,2), (2,2,1)$ (\textbf{3-fold degenerate}, $g=3$).
    \item \textbf{Third Excited State}: $n_x^2+n_y^2+n_z^2 = 1^2+1^2+3^2 = 11 \implies E = 11E_1$.
    Three states: $(3,1,1), (1,3,1), (1,1,3)$ ($g=3$).
    \item \textbf{State $E = 14E_1$}: $1^2+2^2+3^2 = 14$.
    Six states: $(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)$ (\textbf{6-fold degenerate}, $g=6$).
\end{itemize}"""
        ),
        (
            r"Explain the physical principle of Quantum Mechanical Tunneling. Set up the Schrödinger equation for a rectangular potential barrier of height $V_0$ and width $a$ for $E < V_0$. State the transmission coefficient formula and explain its application in the Scanning Tunneling Microscope (STM).",
            r"""\textbf{1. Concept of Quantum Tunneling}:
Classically, a particle of total energy $E$ encountering a potential barrier $V_0 > E$ cannot penetrate into the barrier and must undergo $100\%$ reflection.
In quantum mechanics, the wave function does not drop abruptly to zero at the barrier edge but decays exponentially: $\psi(x) \propto e^{-\kappa x}$. If the barrier is thin, $\psi(x)$ remains non-zero at the exit boundary, emerging as a transmitted travelling wave with finite probability $T > 0$.

\textbf{2. Boundary Value Formulation}:
Let a barrier of width $a$ extend from $x = 0$ to $x = a$:
\begin{align*}
\text{Region I } (x < 0, V=0): &\quad \psi_{\text{I}}(x) = e^{i k_1 x} + R e^{-i k_1 x}, \quad k_1 = \frac{\sqrt{2mE}}{\hbar} \\
\text{Region II } (0 < x < a, V=V_0): &\quad \psi_{\text{II}}(x) = A e^{-\kappa x} + B e^{+\kappa x}, \quad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar} \\
\text{Region III } (x > a, V=0): &\quad \psi_{\text{III}}(x) = T e^{i k_1 x}
\end{align*}

\textbf{3. Transmission Coefficient $T$}:
Matching $\psi$ and $\frac{d\psi}{dx}$ at $x = 0$ and $x = a$ yields:
\begin{equation}
\mathbf{T = \left[ 1 + \frac{V_0^2 \sinh^2(\kappa a)}{4E(V_0 - E)} \right]^{-1} \approx 16 \frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa a} \quad (\text{for } \kappa a \gg 1)}
\end{equation}

\textbf{4. Application: Scanning Tunneling Microscope (STM)}:
\begin{itemize}
    \item An atomically sharp metallic tip (Tungsten or Pt-Ir) is brought within sub-nanometer distance ($s \approx 0.5\text{ nm}$) of a conducting sample.
    \item Applying a small bias voltage $V$ induces a tunneling current $I_{\text{tunnel}} \propto e^{-2\kappa s}$.
    \item Because $I_{\text{tunnel}}$ changes by an order of magnitude ($10\times$) for every $0.1\text{ nm}$ change in tip-sample gap $s$, piezo-electric scanners can map individual surface atoms with sub-angstrom vertical resolution.
\end{itemize}"""
        ),
        (
            r"An electron is confined within a 1D quantum well of width $L = 0.50\text{ nm}$. Calculate: (a) the first three energy levels $E_1, E_2, E_3$ in $\text{eV}$, (b) the wavelength of light emitted when the electron transitions from $n=3$ to $n=1$, (c) the probability of finding the electron in the range $0 \le x \le L/4$ in the ground state.",
            r"""\textbf{1. Energy Levels $E_1, E_2, E_3$}:
\begin{align*}
E_1 &= \frac{h^2}{8 m_e L^2} = \frac{(6.626 \times 10^{-34}\text{ J}\cdot\text{s})^2}{8(9.109 \times 10^{-31}\text{ kg})(0.50 \times 10^{-9}\text{ m})^2} \\
&= \frac{4.3904 \times 10^{-67}}{1.8218 \times 10^{-48}} \approx 2.4099 \times 10^{-19}\text{ J} = \frac{2.4099 \times 10^{-19}}{1.602 \times 10^{-19}} \approx \mathbf{1.504\text{ eV}} \\
\mathbf{E_2} &= 2^2 E_1 = 4(1.504\text{ eV}) = \mathbf{6.016\text{ eV}} \\
\mathbf{E_3} &= 3^2 E_1 = 9(1.504\text{ eV}) = \mathbf{13.536\text{ eV}}
\end{align*}

\textbf{2. Transition Wavelength ($n=3 \to n=1$)}:
\begin{align*}
\Delta E &= E_3 - E_1 = 13.536 - 1.504 = 12.032\text{ eV} = 1.9275 \times 10^{-18}\text{ J} \\
\mathbf{\lambda} &= \frac{h c}{\Delta E} = \frac{(6.626 \times 10^{-34})(3 \times 10^8)}{1.9275 \times 10^{-18}} \approx 1.031 \times 10^{-7}\text{ m} = \mathbf{103.1\text{ nm}} \quad (\text{Far UV})
\end{align*}

\textbf{3. Probability in $0 \le x \le L/4$ (Ground State)}:
\begin{align*}
P &= \int_0^{L/4} \frac{2}{L}\sin^2\left(\frac{\pi x}{L}\right)dx = \frac{2}{L}\int_0^{L/4} \left(\frac{1 - \cos(2\pi x/L)}{2}\right)dx \\
&= \frac{1}{L}\left[ x - \frac{L}{2\pi}\sin\left(\frac{2\pi x}{L}\right) \right]_0^{L/4} = \frac{1}{L}\left[ \frac{L}{4} - \frac{L}{2\pi}\sin\left(\frac{\pi}{2}\right) \right] \\
&= \frac{1}{4} - \frac{1}{2\pi} = 0.2500 - 0.1592 = \mathbf{0.0908 = 9.08\%}
\end{align*}"""
        )
    ]
    
    return unit_num, unit_title, mcqs, theory_qs
