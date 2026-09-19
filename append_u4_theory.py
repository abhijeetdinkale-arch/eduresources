# -*- coding: utf-8 -*-
import generate_physics_qb_u4

additional_tqs = [
    (
        r"Describe the Davisson-Germer Experiment. Explain the experimental setup, working method, observation of diffraction peaks, and show how the calculated de Broglie wavelength matches Bragg's law.",
        r"""\textbf{1. Experimental Setup and Working Principle}:
\begin{itemize}
\item An electron gun produces a collimated beam of electrons accelerated by an adjustable potential $V$ ($40\text{--}68\text{ V}$).
\item The beam strikes the target surface of a single crystal Nickel (Ni) target.
\item Scattered electrons are collected by a movable electrostatic Faraday collector connected to a sensitive galvanometer at various scattering angles $\phi$.
\end{itemize}

\textbf{2. Experimental Observations}:
\begin{itemize}
\item At an accelerating voltage $V = 54\text{ V}$, a prominent, sharp intensity peak occurs at a scattering angle $\phi = 50^\circ$.
\item The glancing angle (Bragg angle) $\theta$ with respect to the atomic crystal planes is:
\begin{equation}
\theta = 90^\circ - \frac{\phi}{2} = 90^\circ - 25^\circ = 65^\circ
\end{equation}
\end{itemize}

\textbf{3. Verification using Bragg's Law}:
For Nickel, interplanar spacing from X-ray diffraction is $d = 0.091\text{ nm} = 0.91\text{ \AA}$.
Using first-order Bragg's diffraction condition ($n=1$):
\begin{equation}
\lambda_{Bragg} = 2d \sin\theta = 2(0.091\text{ nm}) \sin(65^\circ) = 2(0.091)(0.9063) = \mathbf{0.165\text{ nm}}
\end{equation}

\textbf{4. Theoretical de Broglie Wavelength}:
Using de Broglie's formula for an electron accelerated through $V = 54\text{ V}$:
\begin{equation}
\lambda_{dB} = \frac{h}{\sqrt{2 m_e e V}} = \frac{1.227}{\sqrt{54}}\text{ nm} = \frac{1.227}{7.348}\text{ nm} = \mathbf{0.167\text{ nm}}
\end{equation}
The near-perfect agreement between $\lambda_{Bragg}$ ($0.165\text{ nm}$) and $\lambda_{dB}$ ($0.167\text{ nm}$) provided the first conclusive experimental proof of de Broglie's wave hypothesis."""
    ),
    (
        r"Define Hermitian Operators in quantum mechanics. Prove that the eigenvalues of Hermitian operators are strictly real and that eigenfunctions corresponding to distinct eigenvalues are mutually orthogonal.",
        r"""\textbf{1. Definition of Hermitian Operator}:
An operator $\hat{A}$ is Hermitian if for any well-behaved wavefunctions $\psi$ and $\phi$:
\begin{equation}
\int \psi^* (\hat{A} \phi)\, dx = \int (\hat{A}\psi)^* \phi\, dx = \langle \psi | \hat{A} | \phi \rangle = \langle \hat{A}\psi | \phi \rangle
\end{equation}
Physical observables (position, momentum, energy) are represented by Hermitian operators because physical measurements must yield real values.

\textbf{2. Proof that Eigenvalues are Strictly Real}:
Let $\hat{A}\psi_n = a_n \psi_n$.
Taking the inner product with $\psi_n$:
\begin{equation}
\langle \psi_n | \hat{A} | \psi_n \rangle = \int \psi_n^* (\hat{A} \psi_n)\, dx = a_n \int |\psi_n|^2 dx = a_n \langle \psi_n | \psi_n \rangle
\end{equation}
Using the Hermiticity property:
\begin{equation}
\langle \psi_n | \hat{A} | \psi_n \rangle = \langle \hat{A}\psi_n | \psi_n \rangle = \int (\hat{A}\psi_n)^* \psi_n\, dx = a_n^* \int |\psi_n|^2 dx = a_n^* \langle \psi_n | \psi_n \rangle
\end{equation}
Subtracting the two relations:
\begin{equation}
(a_n - a_n^*) \langle \psi_n | \psi_n \rangle = 0
\end{equation}
Since $\langle \psi_n | \psi_n \rangle > 0$ for non-trivial states, $a_n = a_n^*$, proving all eigenvalues $a_n$ are purely real.

\textbf{3. Proof of Orthogonality of Eigenfunctions}:
Let $\hat{A}\psi_m = a_m \psi_m$ and $\hat{A}\psi_n = a_n \psi_n$ with $a_m \ne a_n$.
\begin{equation}
\langle \psi_m | \hat{A} | \psi_n \rangle = a_n \langle \psi_m | \psi_n \rangle
\end{equation}
\begin{equation}
\langle \hat{A}\psi_m | \psi_n \rangle = a_m^* \langle \psi_m | \psi_n \rangle = a_m \langle \psi_m | \psi_n \rangle
\end{equation}
Subtracting:
\begin{equation}
(a_n - a_m) \langle \psi_m | \psi_n \rangle = 0
\end{equation}
Since $a_m \ne a_n$, we must have $\langle \psi_m | \psi_n \rangle = \int \psi_m^* \psi_n dx = 0$, proving distinct eigenfunctions are orthogonal."""
    ),
    (
        r"Solve the Schrödinger equation for a 1D Quantum Harmonic Oscillator. State the quantized energy eigenvalues, explain zero-point energy $E_0 = \frac{1}{2}\hbar\omega$, and compare quantum vs classical probability distributions.",
        r"""\textbf{1. Formulation of the Oscillator Equation}:
For a particle of mass $m$ experiencing restoring force $F = -k x$, potential energy is $V(x) = \frac{1}{2}m\omega^2 x^2$.
The Time-Independent Schrödinger Equation is:
\begin{equation}
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2 x^2 \psi = E\psi
\end{equation}

\textbf{2. Dimensionless Form and Hermite Polynomials}:
Let $y = \sqrt{\frac{m\omega}{\hbar}} x$ and $\epsilon = \frac{2E}{\hbar\omega}$.
The asymptotic solution is $\psi(y) = H(y) e^{-y^2/2}$, where $H(y)$ satisfies Hermite's differential equation.
For the wavefunction to remain square-integrable as $y \to \pm\infty$, the power series must terminate into a polynomial of order $n$, yielding:
\begin{equation}
\epsilon = 2n + 1 \implies \mathbf{E_n = \left(n + \frac{1}{2}\right)\hbar\omega},\quad n = 0, 1, 2, \dots
\end{equation}
Normalized eigenfunctions are:
\begin{equation}
\psi_n(x) = \frac{1}{\sqrt{2^n n!}}\left(\frac{m\omega}{\pi\hbar}\right)^{1/4} H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right) e^{-\frac{m\omega x^2}{2\hbar}}
\end{equation}

\textbf{3. Zero-Point Energy}:
Even at absolute zero ($n=0$), ground state energy is $E_0 = \frac{1}{2}\hbar\omega > 0$.
This is a direct consequence of Heisenberg's Uncertainty Principle: if $E_0 = 0$, the particle would sit motionless at $x=0$ ($\Delta x = 0, \Delta p = 0$), violating $\Delta x \Delta p \ge \hbar/2$.

\textbf{4. Classical vs Quantum Probability}:
\begin{itemize}
\item \textit{Classical:} Maximum probability density occurs at classical turning points ($x = \pm A$) where velocity $v \to 0$.
\item \textit{Quantum Ground State ($n=0$):} Maximum probability density $|\psi_0(x)|^2$ occurs at the center ($x=0$), with exponential tunneling into classically forbidden regions $|x| > A$.
\item \textit{Correspondence Principle:} For large quantum numbers $n \gg 1$, quantum probability peaks match classical turning points."""
    ),
    (
        r"Analyze a 1D Finite Potential Well of depth $V_0$ and width $2a$. Explain the existence of bound states ($E < V_0$), boundary conditions, and show why the number of bound states is finite.",
        r"""\textbf{1. Potential Profile}:
\begin{equation}
V(x) = \begin{cases} 0, & |x| \le a \quad \text{(Region II: Well interior)} \\ V_0, & |x| > a \quad \text{(Regions I and III: Barriers)} \end{cases}
\end{equation}
For bound states ($0 < E < V_0$), let $k = \frac{\sqrt{2mE}}{\hbar}$ and $\alpha = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$.

\textbf{2. Wavefunctions by Symmetry}:
\begin{itemize}
\item \textbf{Symmetric States (Even Parity):}
\begin{equation}
\psi_{II}(x) = B \cos(kx),\quad \psi_{III}(x) = C e^{-\alpha x}\; (x > a)
\end{equation}
Matching $\psi$ and $\frac{d\psi}{dx}$ at $x = a$:
\begin{equation}
B\cos(ka) = C e^{-\alpha a},\quad -kB\sin(ka) = -\alpha C e^{-\alpha a} \implies \mathbf{k \tan(ka) = \alpha}
\end{equation}
\item \textbf{Antisymmetric States (Odd Parity):}
\begin{equation}
\psi_{II}(x) = A \sin(kx) \implies \mathbf{-k \cot(ka) = \alpha}
\end{equation}
\end{itemize}

\textbf{3. Transcendental Graphical Solution}:
Let $\xi = ka$ and $\eta = \alpha a$.
\begin{equation}
\xi^2 + \eta^2 = \frac{2m V_0 a^2}{\hbar^2} \equiv R^2
\end{equation}
The allowed energy levels correspond to intersections of the circle of radius $R = \frac{\sqrt{2mV_0}a}{\hbar}$ with curves $\eta = \xi \tan\xi$ (even) and $\eta = -\xi \cot\xi$ (odd).
\begin{itemize}
\item At least one even bound state always exists no matter how shallow or narrow the well is.
\item Total number of bound states is finite: $N = 1 + \left\lfloor \frac{R}{\pi/2} \right\rfloor$."""
    ),
    (
        r"Derive the reflection coefficient $R$ and transmission coefficient $T$ for a particle of energy $E$ incident on a potential step of height $V_0$ for both cases $E > V_0$ and $E < V_0$. Verify that $R + T = 1$.",
        r"""\textbf{1. Case I: Energy $E > V_0$}:
Let $k_1 = \frac{\sqrt{2mE}}{\hbar}$ for $x < 0$ and $k_2 = \frac{\sqrt{2m(E - V_0)}}{\hbar}$ for $x > 0$.
\begin{equation}
\psi_1(x) = A e^{j k_1 x} + B e^{-j k_1 x},\quad \psi_2(x) = C e^{j k_2 x}
\end{equation}
Applying boundary conditions at $x=0$ ($\psi_1(0)=\psi_2(0)$ and $\psi_1'(0)=\psi_2'(0)$):
\begin{equation}
A + B = C,\quad j k_1(A - B) = j k_2 C \implies k_1(A - B) = k_2(A + B)
\end{equation}
Solving for reflection amplitude $B/A$ and transmission amplitude $C/A$:
\begin{equation}
\frac{B}{A} = \frac{k_1 - k_2}{k_1 + k_2},\quad \frac{C}{A} = \frac{2k_1}{k_1 + k_2}
\end{equation}
The reflection and transmission coefficients are:
\begin{equation}
R = \left|\frac{B}{A}\right|^2 = \left(\frac{k_1 - k_2}{k_1 + k_2}\right)^2,\quad T = \frac{k_2}{k_1}\left|\frac{C}{A}\right|^2 = \frac{k_2}{k_1}\left(\frac{2k_1}{k_1 + k_2}\right)^2 = \frac{4k_1 k_2}{(k_1 + k_2)^2}
\end{equation}
\textbf{Conservation}:
\begin{equation}
R + T = \frac{(k_1 - k_2)^2 + 4k_1 k_2}{(k_1 + k_2)^2} = \frac{(k_1 + k_2)^2}{(k_1 + k_2)^2} = \mathbf{1}
\end{equation}

\textbf{2. Case II: Energy $E < V_0$}:
Here $k_2 = j\alpha$ where $\alpha = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$.
\begin{equation}
\frac{B}{A} = \frac{k_1 - j\alpha}{k_1 + j\alpha} \implies R = \left|\frac{k_1 - j\alpha}{k_1 + j\alpha}\right|^2 = \frac{k_1^2 + \alpha^2}{k_1^2 + \alpha^2} = \mathbf{1},\quad T = 0
\end{equation}
The particle is totally reflected, but exhibits an exponentially decaying evanescent wave inside the barrier ($x > 0$)."""
    ),
    (
        r"Derive the Quantum Mechanical Probability Current Density $\mathbf{J}$ and prove the Probability Conservation Law (Continuity Equation) from the Time-Dependent Schrödinger Equation.",
        r"""\textbf{1. Time-Dependent Schrödinger Equation (TDSE)}:
\begin{equation}
j\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V(\mathbf{r})\psi \implies \frac{\partial \psi}{\partial t} = \frac{j\hbar}{2m}\nabla^2\psi - \frac{j}{\hbar}V\psi
\end{equation}
Taking the complex conjugate (assuming real potential $V^* = V$):
\begin{equation}
\frac{\partial \psi^*}{\partial t} = -\frac{j\hbar}{2m}\nabla^2\psi^* + \frac{j}{\hbar}V\psi^*
\end{equation}

\textbf{2. Time Derivative of Probability Density $\rho = \psi^* \psi$}:
\begin{align*}
\frac{\partial \rho}{\partial t} &= \frac{\partial}{\partial t}(\psi^* \psi) = \psi^* \frac{\partial \psi}{\partial t} + \frac{\partial \psi^*}{\partial t}\psi \\
&= \psi^* \left(\frac{j\hbar}{2m}\nabla^2\psi - \frac{j}{\hbar}V\psi\right) + \left(-\frac{j\hbar}{2m}\nabla^2\psi^* + \frac{j}{\hbar}V\psi^*\right)\psi \\
&= \frac{j\hbar}{2m} \left[\psi^* \nabla^2\psi - (\nabla^2\psi^*)\psi\right] = \frac{j\hbar}{2m} \nabla \cdot \left[\psi^* \nabla\psi - (\nabla\psi^*)\psi\right]
\end{align*}

\textbf{3. Defining Probability Current Density $\mathbf{J}$}:
\begin{equation}
\mathbf{J} = \frac{\hbar}{2mj} \left(\psi^* \nabla\psi - \psi \nabla\psi^*\right) = \frac{\hbar}{m}\text{Im}(\psi^* \nabla\psi)
\end{equation}
Substituting back yields the fundamental continuity equation:
\begin{equation}
\mathbf{\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0}
\end{equation}
Integrating over all space reveals that total probability is strictly conserved in time:
\begin{equation}
\frac{d}{dt}\int \rho\, dV = -\oint_{S_\infty} \mathbf{J} \cdot d\mathbf{S} = 0 \implies \int_{-\infty}^\infty |\psi(\mathbf{r},t)|^2 dV = 1\quad \forall t
\end{equation}"""
    ),
    (
        r"Construct a 1D Gaussian Wave Packet. Show that it represents a minimum uncertainty state ($\Delta x \Delta p = \hbar/2$) and derive the rate of wave packet spreading in time.",
        r"""\textbf{1. Gaussian Wave Packet Formulation}:
At $t=0$, let the spatial wavefunction be:
\begin{equation}
\psi(x,0) = \left(\frac{1}{2\pi \sigma_0^2}\right)^{1/4} e^{-\frac{x^2}{4\sigma_0^2}} e^{j k_0 x}
\end{equation}
The momentum probability amplitude $\phi(p)$ is the Fourier transform:
\begin{equation}
\phi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty \psi(x,0) e^{-j px/\hbar} dx = \left(\frac{2\sigma_0^2}{\pi\hbar^2}\right)^{1/4} e^{-\frac{\sigma_0^2 (p - p_0)^2}{\hbar^2}}
\end{equation}

\textbf{2. Calculating Uncertainties $\Delta x$ and $\Delta p$}:
\begin{equation}
\langle x \rangle = 0,\quad \langle x^2 \rangle = \sigma_0^2 \implies \Delta x = \sigma_0
\end{equation}
\begin{equation}
\langle p \rangle = \hbar k_0 = p_0,\quad \langle p^2 \rangle = p_0^2 + \frac{\hbar^2}{4\sigma_0^2} \implies \Delta p = \frac{\hbar}{2\sigma_0}
\end{equation}
The uncertainty product at $t=0$ is:
\begin{equation}
\mathbf{\Delta x \Delta p = \sigma_0 \left(\frac{\hbar}{2\sigma_0}\right) = \frac{\hbar}{2}}
\end{equation}
Thus, a Gaussian wave packet achieves the theoretical minimum uncertainty limit permitted by quantum mechanics.

\textbf{3. Time Evolution and Wave Packet Spreading}:
Solving TDSE for a free particle ($V=0$):
\begin{equation}
\sigma(t) = \sigma_0 \sqrt{1 + \left(\frac{\hbar t}{2m \sigma_0^2}\right)^2}
\end{equation}
As time $t$ advances, phase velocities of component Fourier waves differ ($v_p = \hbar k/2m$), causing the wave packet width to broaden relentlessly in coordinate space."""
    ),
    (
        r"Explain the operating principle of the Scanning Tunneling Microscope (STM). Derive the exponential sensitivity of tunneling current to tip-to-sample distance $d$ and discuss constant-current vs constant-height imaging modes.",
        r"""\textbf{1. Quantum Tunneling Basis of STM}:
In classical mechanics, an electron cannot cross an insulating vacuum gap between a sharp conducting tip and a sample surface if its kinetic energy is less than the work function $\Phi$.
In quantum mechanics, the electron wavefunction penetrates the vacuum barrier of width $d$ with decay constant:
\begin{equation}
\kappa = \frac{\sqrt{2m_e \Phi}}{\hbar} \approx 0.512\sqrt{\Phi\text{ [eV]}}\; \text{\AA}^{-1}
\end{equation}

\textbf{2. Tunneling Current Dependence on Distance $d$}:
For a small bias voltage $V_b \ll \Phi$, the tunneling current $I_T$ is proportional to the barrier transmission probability $T$:
\begin{equation}
\mathbf{I_T \propto V_b e^{-2\kappa d}}
\end{equation}
For typical work functions $\Phi \approx 4.0\text{ eV}$, $\kappa \approx 1.0\text{ \AA}^{-1} = 10\text{ nm}^{-1}$:
\begin{equation}
2\kappa \approx 2.0\text{ \AA}^{-1} = 20\text{ nm}^{-1}
\end{equation}
Changing the tip-sample distance $d$ by merely $1\text{ \AA} = 0.1\text{ nm}$ alters the tunneling current by a factor of $e^{2} \approx 7.4$ (nearly an order of magnitude). This extreme sensitivity enables sub-Angstrom ($0.01\text{ nm}$) vertical resolution.

\textbf{3. Imaging Modes}:
\begin{itemize}
\item \textbf{Constant-Current Mode:} A feedback loop adjusts piezoelectric $z$-position to maintain constant $I_T$; recorded $z(x,y)$ voltage generates real-space atomic topography.
\item \textbf{Constant-Height Mode:} The tip scans at fixed $z$; rapid variations in $I_T(x,y)$ are recorded, enabling high scan speeds on atomically flat surfaces."""
    ),
    (
        r"Derive the Energy-Time Uncertainty Principle $\Delta E \Delta t \ge \hbar/2$. Explain its physical interpretation using the lifetime $\tau$ of excited atomic states and the natural spectral line broadening $\Delta \nu$.",
        r"""\textbf{1. Derivation via Generalized Uncertainty Relation}:
For any observable operator $\hat{A}$ that does not explicitly depend on time:
\begin{equation}
\frac{d\langle \hat{A}\rangle}{dt} = \frac{1}{j\hbar}\langle [\hat{A}, \hat{H}] \rangle
\end{equation}
Using the Robertson-Schrödinger uncertainty inequality $\Delta A \Delta H \ge \frac{1}{2}|\langle [\hat{A}, \hat{H}] \rangle|$:
\begin{equation}
\Delta A \Delta E \ge \frac{\hbar}{2}\left|\frac{d\langle \hat{A}\rangle}{dt}\right|
\end{equation}
Defining the characteristic time $\Delta t$ required for the expectation value of $\hat{A}$ to change by one standard deviation:
\begin{equation}
\Delta t \equiv \frac{\Delta A}{\left|\frac{d\langle \hat{A}\rangle}{dt}\right|}
\end{equation}
Substituting gives:
\begin{equation}
\mathbf{\Delta E \Delta t \ge \frac{\hbar}{2}}
\end{equation}

\textbf{2. Physical Significance in Atomic Transitions}:
If an atom is excited to a state with finite lifetime $\tau = \Delta t$, its energy cannot be strictly sharply defined. The energy uncertainty is:
\begin{equation}
\Delta E \approx \frac{\hbar}{\tau} = \frac{h}{2\pi \tau}
\end{equation}
Since $\Delta E = h \Delta\nu$, the natural spectral linewidth is:
\begin{equation}
\Delta\nu_{nat} = \frac{1}{2\pi \tau}
\end{equation}
For typical atomic optical lifetimes $\tau \sim 10\text{ ns} = 10^{-8}\text{ s}$, the unavoidable natural spectral broadening is $\Delta\nu_{nat} \approx \frac{1}{2\pi(10^{-8})} \approx 16\text{ MHz}$."""
    ),
    (
        r"An electron is trapped in an infinite potential well of width $L = 1.0\text{ nm}$. (a) Calculate the first three energy levels in eV. (b) Find the wavelength of the emitted photon when the electron falls from $n=4$ to $n=2$. (c) Calculate the expectation value $\langle x \rangle$ and $\langle x^2 \rangle$ for the ground state, and determine the spatial uncertainty $\Delta x$.",
        r"""\textbf{1. Energy Levels $E_1, E_2, E_3$}:
\begin{align*}
E_1 &= \frac{h^2}{8 m_e L^2} = \frac{(6.626 \times 10^{-34})^2}{8(9.109 \times 10^{-31})(1.0 \times 10^{-9})^2} = \frac{4.3904 \times 10^{-67}}{7.2872 \times 10^{-48}} \\
&= 6.0248 \times 10^{-20}\text{ J} = \frac{6.0248 \times 10^{-20}}{1.602 \times 10^{-19}} \approx \mathbf{0.376\text{ eV}} \\
E_2 &= 4 E_1 = 4(0.376\text{ eV}) = \mathbf{1.504\text{ eV}} \\
E_3 &= 9 E_1 = 9(0.376\text{ eV}) = \mathbf{3.384\text{ eV}} \\
E_4 &= 16 E_1 = 16(0.376\text{ eV}) = \mathbf{6.016\text{ eV}}
\end{align*}

\textbf{2. Transition Wavelength ($n=4 \to n=2$)}:
\begin{align*}
\Delta E &= E_4 - E_2 = 6.016 - 1.504 = 4.512\text{ eV} = 7.228 \times 10^{-19}\text{ J} \\
\lambda &= \frac{hc}{\Delta E} = \frac{(6.626 \times 10^{-34})(3.0 \times 10^8)}{7.228 \times 10^{-19}} = \frac{1.9878 \times 10^{-25}}{7.228 \times 10^{-19}} = 2.75 \times 10^{-7}\text{ m} = \mathbf{275\text{ nm}}\quad (\text{UV})
\end{align*}

\textbf{3. Expectation Values for Ground State ($n=1$)}:
Wavefunction $\psi_1(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{\pi x}{L}\right)$.
\begin{equation}
\mathbf{\langle x \rangle} = \int_0^L x |\psi_1(x)|^2 dx = \frac{2}{L}\int_0^L x \sin^2\left(\frac{\pi x}{L}\right)dx = \mathbf{\frac{L}{2} = 0.50\text{ nm}}
\end{equation}
\begin{equation}
\langle x^2 \rangle = \frac{2}{L}\int_0^L x^2 \sin^2\left(\frac{\pi x}{L}\right)dx = L^2\left(\frac{1}{3} - \frac{1}{2\pi^2}\right) = L^2(0.3333 - 0.05066) = \mathbf{0.2827 L^2}
\end{equation}
The spatial dispersion is:
\begin{equation}
\mathbf{\Delta x} = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \sqrt{0.2827 L^2 - 0.2500 L^2} = \sqrt{0.0327 L^2} \approx 0.1807 L = \mathbf{0.181\text{ nm}}
\end{equation}"""
    )
]

# Read original u4 content
with open('generate_physics_qb_u4.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the end of theory_qs
old_end = "return unit_num, unit_title, mcqs, theory_qs"
# Let's inspect where theory_qs ends
idx = code.rfind("theory_qs = [")
print("Found theory_qs at:", idx)

# Let's import the script, append additional_tqs to theory_qs, and rewrite cleanly
