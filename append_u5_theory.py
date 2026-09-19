# -*- coding: utf-8 -*-

additional_tqs_u5 = [
    (
        r"Derive the temperature dependence of the Fermi level $E_F(T)$ in an n-type extrinsic semiconductor. Explain the physical behavior in the cryogenic freeze-out, extrinsic saturation, and high-temperature intrinsic regimes.",
        r"""\textbf{1. Charge Neutrality Condition}:
In an n-type semiconductor with donor concentration $N_d$ (energy level $E_d$) and no acceptors:
\begin{equation}
n = N_d^+ + p
\end{equation}
For non-degenerate electrons: $n = N_c e^{-(E_c - E_F)/k_B T}$, $p = N_v e^{-(E_F - E_v)/k_B T}$, and ionized donors $N_d^+ = \frac{N_d}{1 + 2 e^{(E_F - E_d)/k_B T}}$.

\textbf{2. Three Distinct Temperature Regimes}:
\begin{enumerate}
\item \textbf{Freeze-Out / Ionization Regime ($T \to 0\text{ K}$):}
Thermal energy is insufficient to ionize donors. Here $p \approx 0$ and $n = N_d^+$.
\begin{equation}
N_c e^{-(E_c - E_F)/k_B T} \approx N_d e^{-(E_F - E_d)/k_B T} \implies \mathbf{E_F(0) = \frac{E_c + E_d}{2}}
\end{equation}
As $T$ rises slightly, $E_F(T) = \frac{E_c + E_d}{2} + \frac{k_B T}{2}\ln\left(\frac{N_d}{2 N_c}\right)$.

\item \textbf{Extrinsic / Saturation Regime ($100\text{ K} \le T \le 450\text{ K}$):}
All donor atoms are completely ionized ($N_d^+ \approx N_d$) and minority carrier generation is negligible ($p \ll n$):
\begin{equation}
n = N_d \implies N_c e^{-(E_c - E_F)/k_B T} = N_d
\end{equation}
\begin{equation}
\mathbf{E_F(T) = E_c - k_B T \ln\left(\frac{N_c}{N_d}\right)}
\end{equation}
In this range, $n = N_d = \text{constant}$, and the Fermi level decreases linearly with temperature toward the middle of the bandgap.

\item \textbf{Intrinsic Crossover Regime ($T > 500\text{ K}$):}
Band-to-band thermal generation dominates over donor doping ($n_i(T) \gg N_d$):
\begin{equation}
n \approx p \approx n_i \implies \mathbf{E_F \to E_i = \frac{E_c + E_v}{2} + \frac{3}{4}k_B T \ln\left(\frac{m_h^*}{m_e^*}\right)}
\end{equation}
The semiconductor loses its extrinsic characteristics and behaves as an intrinsic semiconductor.
\end{enumerate}"""
    ),
    (
        r"Compare direct and indirect carrier recombination mechanisms in semiconductors. Explain Shockley-Read-Hall (SRH) recombination through deep trap levels, Auger recombination, and radiative recombination.",
        r"""\textbf{1. Direct vs Indirect Bandgap Recombination}:
\begin{itemize}
\item \textbf{Direct Recombination (e.g., GaAs, InP):} Electron at conduction band minimum drops directly into valence band maximum ($\Delta k = 0$). Momentum is conserved without phonon participation; spontaneous recombination lifetime is short ($\tau_r \sim 1\text{--}10\text{ ns}$), emitting photons efficiently.
\item \textbf{Indirect Recombination (e.g., Si, Ge):} Conduction band minimum and valence band maximum are offset in $k$-space ($\Delta k \ne 0$). Direct photon emission is forbidden by momentum conservation; transition requires simultaneous emission/absorption of a lattice phonon, leading to very long radiative lifetimes ($\tau_r \sim 1\text{ ms}$).
\end{itemize}

\textbf{2. Shockley-Read-Hall (SRH) Trap-Assisted Recombination}:
In indirect semiconductors like Silicon, non-radiative recombination occurs primarily via deep-level defect/impurity states located near the center of the bandgap ($E_t \approx E_i$):
\begin{enumerate}
\item Trap captures an electron from the conduction band.
\item Trap captures a hole from the valence band (or emits trapped electron to valence band).
\item Electron and hole annihilate, dissipating energy into the lattice as heat (phonons).
\end{enumerate}
The SRH recombination rate is:
\begin{equation}
U_{SRH} = \frac{np - n_i^2}{\tau_{p0}(n + n_1) + \tau_{n0}(p + p_1)}
\end{equation}

\textbf{3. Auger Recombination}:
A three-particle non-radiative process where the recombination energy of an electron-hole pair is transferred to a third carrier (electron or hole), which relaxes thermally.
The Auger recombination rate scales as $U_{Auger} = C_n n^2 p + C_p n p^2$, dominating at very high injection carrier densities ($n > 10^{18}\text{ cm}^{-3}$)."""
    ),
    (
        r"Explain carrier velocity saturation at high electric fields in Silicon and describe the Gunn Effect / Negative Differential Resistance (NDR) in Gallium Arsenide (GaAs) using the Ridley-Watkins-Hilsum two-valley model.",
        r"""\textbf{1. High-Field Velocity Saturation}:
At low electric fields, drift velocity increases linearly with field according to Ohm's law: $v_d = \mu E$.
At high electric fields ($E > 10^4\text{ V/cm}$), carriers gain kinetic energy faster than they can transfer it to acoustic phonons. Optical phonon emission becomes intense, scattering carriers randomly and saturating the drift velocity to a constant value:
\begin{equation}
v_{sat} \approx 1.0 \times 10^7\text{ cm/s}\quad (\text{in Silicon at }300\text{ K})
\end{equation}
The empirical drift velocity relation is:
\begin{equation}
v_d(E) = \frac{\mu_0 E}{\left[1 + \left(\frac{\mu_0 E}{v_{sat}}\right)^\beta\right]^{1/\beta}}
\end{equation}

\textbf{2. Gunn Effect and Negative Differential Resistance in GaAs}:
In GaAs, the conduction band has a two-valley structure:
\begin{itemize}
\item \textbf{Lower Valley ($\Gamma$-valley):} Located at $k=0$; low effective mass ($m_1^* = 0.067 m_0$), high electron mobility ($\mu_1 \approx 8500\text{ cm}^2/\text{V}\cdot\text{s}$).
\item \textbf{Upper Satellite Valleys ($L$-valleys):} Separated by energy offset $\Delta E \approx 0.31\text{ eV}$; high effective mass ($m_2^* = 0.22 m_0$), low mobility ($\mu_2 \approx 100\text{ cm}^2/\text{V}\cdot\text{s}$).
\end{itemize}

\textbf{3. Mechanism of Negative Differential Mobility}:
When applied electric field exceeds the threshold field $E_{th} \approx 3.2\text{ kV/cm}$:
\begin{enumerate}
\item Electrons gain sufficient kinetic energy to transfer from the high-mobility $\Gamma$-valley into the low-mobility $L$-valleys (intervalley scattering).
\item Average electron drift velocity $v_d = \frac{n_1 \mu_1 + n_2 \mu_2}{n_1 + n_2} E$ decreases as field increases above $E_{th}$.
\item This yields a negative differential mobility regime:
\begin{equation}
\mu_d = \frac{dv_d}{dE} < 0
\end{equation}
\end{enumerate}
This instability produces moving high-field charge domains (Gunn domains), generating microwave oscillations ($1\text{--}100\text{ GHz}$) in Gunn diodes."""
    ),
    (
        r"Derive the non-ideal diode I-V equation including recombination in the depletion region. Explain the physical origin of the Diode Ideality Factor $\eta$ ($\eta=1$ vs $\eta=2$) and series resistance effects.",
        r"""\textbf{1. Total Diode Current Components}:
The total forward current in a real p-n junction consists of:
\begin{equation}
I = I_{diff} + I_{rec}
\end{equation}
where $I_{diff}$ is the ideal diffusion current in quasi-neutral regions and $I_{rec}$ is the carrier recombination current within the depletion space-charge layer.

\textbf{2. Depletion Region Recombination Current}:
Inside the depletion region of width $W$, the SRH recombination rate reaches maximum when $n \approx p \approx n_i e^{qV / (2k_B T)}$.
Integrating $U_{SRH}$ across the depletion width $W$:
\begin{equation}
I_{rec} = q A \int_0^W U_{SRH}\, dx \approx \frac{q A W n_i}{2\tau_0} e^{q V / (2k_B T)} = I_{r0} e^{q V / (2k_B T)}
\end{equation}

\textbf{3. Generalized Diode Equation and Ideality Factor $\eta$}:
Combining both components yields the empirical Shockley diode equation:
\begin{equation}
\mathbf{I = I_0 \left[\exp\left(\frac{q V}{\eta k_B T}\right) - 1\right]}
\end{equation}
\begin{itemize}
\item \textbf{At Low Forward Bias ($V < 0.3\text{ V}$):} Recombination in the depletion layer dominates $\implies \mathbf{\eta \approx 2}$.
\item \textbf{At Intermediate Forward Bias ($0.3\text{ V} < V < 0.7\text{ V}$):} Diffusion of injected minority carriers in neutral regions dominates $\implies \mathbf{\eta \approx 1}$.
\item \textbf{At High Forward Bias ($V > 0.7\text{ V}$):} Bulk ohmic series resistance $R_s$ causes the external voltage to drop as $V_{internal} = V_{ext} - I R_s$, bending the $\ln(I)$ vs $V$ curve downward."""
    ),
    (
        r"Explain the photovoltaic effect in a solar cell. Derive the expressions for Short-Circuit Current $I_{sc}$, Open-Circuit Voltage $V_{oc}$, Maximum Power Output $P_{max}$, Fill Factor ($FF$), and Power Conversion Efficiency $\eta$.",
        r"""\textbf{1. Solar Cell Working Principle}:
When incident photons with $h\nu \ge E_g$ strike the p-n junction, electron-hole pairs are photogenerated. The built-in electric field $\mathbf{E}_{bi}$ in the depletion region separates these carriers, sweeping electrons to the n-side and holes to the p-side, establishing a photovoltage.

\textbf{2. Equivalent Circuit and Current Equation}:
The total current delivered to a load under illumination is:
\begin{equation}
I(V) = I_L - I_0 \left(e^{\frac{qV}{k_B T}} - 1\right)
\end{equation}
where $I_L$ is the photogenerated light current and $I_0$ is the reverse saturation current.

\textbf{3. Key Solar Cell Parameters}:
\begin{itemize}
\item \textbf{Short-Circuit Current ($I_{sc}$):} Setting $V=0$:
\begin{equation}
\mathbf{I_{sc} = I_L}
\end{equation}
\item \textbf{Open-Circuit Voltage ($V_{oc}$):} Setting $I = 0$:
\begin{equation}
0 = I_L - I_0 \left(e^{\frac{qV_{oc}}{k_B T}} - 1\right) \implies \mathbf{V_{oc} = \frac{k_B T}{q} \ln\left(\frac{I_L}{I_0} + 1\right) \approx \frac{k_B T}{q}\ln\left(\frac{I_{sc}}{I_0}\right)}
\end{equation}
\item \textbf{Maximum Power Point ($P_{max}$):} Power output $P(V) = V I(V)$ is maximized when $\frac{dP}{dV} = 0$:
\begin{equation}
P_{max} = V_{mp} I_{mp}
\end{equation}
\item \textbf{Fill Factor ($FF$):} Represents the squareness of the I-V curve:
\begin{equation}
\mathbf{FF = \frac{P_{max}}{V_{oc} I_{sc}} = \frac{V_{mp} I_{mp}}{V_{oc} I_{sc}}}\quad (\text{Typically }0.75\text{--}0.85)
\end{equation}
\item \textbf{Power Conversion Efficiency ($\eta_{cell}$):}
\begin{equation}
\mathbf{\eta = \frac{P_{max}}{P_{in}} = \frac{V_{oc} I_{sc} FF}{P_{in} \cdot A_{cell}} \times 100\%}
\end{equation}
where $P_{in}$ is the incident optical irradiance ($1000\text{ W/m}^2$ under standard AM1.5G test conditions)."""
    ),
    (
        r"Explain the physics of Light Emitting Diodes (LEDs). Derive the internal quantum efficiency $\eta_{int}$, external quantum efficiency $\eta_{ext}$, the critical extraction angle $\theta_c$, and methods used to enhance light extraction.",
        r"""\textbf{1. Principle of Operation}:
Under forward bias, minority carriers are injected across the p-n junction. Spontaneous radiative recombination of injected electrons and holes releases energy as photons of wavelength:
\begin{equation}
\lambda \approx \frac{h c}{E_g} = \frac{1.24}{E_g\text{ [eV]}}\; \mu\text{m}
\end{equation}

\textbf{2. Internal Quantum Efficiency ($\eta_{int}$)}:
Defined as the ratio of radiative recombination rate ($R_r$) to total recombination rate ($R_r + R_{nr}$):
\begin{equation}
\mathbf{\eta_{int} = \frac{R_r}{R_r + R_{nr}} = \frac{\tau_{nr}}{\tau_r + \tau_{nr}}}
\end{equation}
In direct bandgap semiconductors (InGaN, AlGaInP), $\tau_r \ll \tau_{nr}$, making $\eta_{int} > 80\%$.

\textbf{3. External Quantum Efficiency and Light Extraction Cone}:
Semiconductors have high refractive indices (e.g., $n_{GaAs} \approx 3.6$).
By Snell's law, total internal reflection traps all light striking the surface at angles greater than the critical angle $\theta_c$:
\begin{equation}
\theta_c = \sin^{-1}\left(\frac{n_{air}}{n_{semi}}\right) = \sin^{-1}\left(\frac{1}{3.6}\right) \approx 16.1^\circ
\end{equation}
The fraction of light escaping within the escape cone from an isotropic internal point source is:
\begin{equation}
\eta_{escape} \approx \frac{\Omega_{cone}}{4\pi} = \frac{2\pi(1 - \cos\theta_c)}{4\pi} \approx \frac{1 - \sqrt{1 - (1/n_s)^2}}{2} \approx \frac{1}{4 n_s^2}
\end{equation}
For GaAs ($n=3.6$), $\eta_{escape} \approx \frac{1}{4(3.6)^2} \approx 1.93\%$.

\textbf{4. Techniques to Enhance Extraction Efficiency}:
\begin{itemize}
\item Transparent hemispherical epoxy encapsulation ($n_{epoxy} \approx 1.5$) widens escape cone.
\item Surface texturing / roughening creates multiple scattering angles for trapped photons.
\item Resonant cavity and photonic crystal patterns redirect trapped waveguide modes outward."""
    ),
    (
        r"Describe the working principle of Avalanche Photodiodes (APDs). Derive the expression for optical responsivity $\mathcal{R}$, quantum efficiency $\eta_q$, and explain impact ionization and avalanche multiplication factor $M$.",
        r"""\textbf{1. Photodetector Operation and Optical Absorption}:
Incident photons with energy $h\nu \ge E_g$ generate electron-hole pairs in the high-field reverse-biased depletion region.
The primary photocurrent is:
\begin{equation}
I_{ph0} = q \eta_q \left(\frac{P_{opt}}{h\nu}\right)
\end{equation}
where $\eta_q$ is the quantum efficiency ($\eta_q = (1 - R)(1 - e^{-\alpha W})$) and $P_{opt}$ is incident optical power.

\textbf{2. Optical Responsivity ($\mathcal{R}$)}:
The responsivity in Amperes per Watt is:
\begin{equation}
\mathbf{\mathcal{R} = \frac{I_{ph}}{P_{opt}} = \frac{q \eta_q}{h\nu} M = \frac{q \eta_q \lambda}{h c} M \approx \frac{\eta_q \lambda\text{ [}\mu\text{m]}}{1.24} M\quad [\text{A/W}]}
\end{equation}
where $M$ is the avalanche multiplication factor ($M=1$ for PIN photodiodes).

\textbf{3. Impact Ionization and Avalanche Multiplication}:
In an APD, a high reverse bias ($>100\text{ V}$) produces an internal electric field exceeding $10^5\text{ V/cm}$.
\begin{enumerate}
\item Injected primary photoelectrons are accelerated to very high kinetic energies.
\item High-energy electrons collide with valence electrons in the lattice, knocking them into the conduction band to create secondary electron-hole pairs (\textit{impact ionization}).
\item The secondary carriers are also accelerated, triggering a cascade chain reaction.
\end{enumerate}

\textbf{4. Multiplication Factor $M$ (Miller's Empirical Formula)}:
\begin{equation}
\mathbf{M = \frac{1}{1 - \left(\frac{V_R}{V_B}\right)^m}}
\end{equation}
where $V_B$ is the avalanche breakdown voltage and $m \approx 3\text{--}6$.
APDs provide internal current gains of $M \sim 50\text{--}200$, significantly enhancing receiver sensitivity in optical communication links."""
    ),
    (
        r"Explain the structure and operational principles of the MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor). Draw the MOS energy band diagrams under Accumulation, Depletion, and Strong Inversion, and derive the Threshold Voltage $V_{th}$.",
        r"""\textbf{1. MOS Capacitor Structure}:
Consists of a metal/polysilicon gate, a thin dielectric oxide layer ($\text{SiO}_2$, thickness $t_{ox}$, capacitance per unit area $C_{ox} = \epsilon_{ox}/t_{ox}$), and a p-type silicon substrate.

\textbf{2. Three Operational Regimes and Energy Band Diagrams}:
\begin{itemize}
\item \textbf{Accumulation ($V_G < V_{FB}$):} Negative gate voltage attracts majority holes to the $\text{Si-SiO}_2$ interface. Valence band bends upward toward Fermi level.
\item \textbf{Depletion ($V_{FB} < V_G < V_{th}$):} Positive gate bias repels holes away from the surface, creating an uncompensated negative acceptor space charge region ($N_a^-$) of width $W_{dep} = \sqrt{\frac{2\epsilon_s \psi_s}{q N_a}}$. Bands bend downward; surface potential $0 < \psi_s < 2\phi_B$.
\item \textbf{Strong Inversion ($V_G \ge V_{th}$):} Bands bend downward such that the surface potential reaches:
\begin{equation}
\psi_s = 2\phi_B = 2\left(\frac{k_B T}{q}\ln\frac{N_a}{n_i}\right)
\end{equation}
The conduction band approaches the Fermi level, attracting a high concentration of free electrons to form an n-type conducting inversion channel between Source and Drain.
\end{itemize}

\textbf{3. Threshold Voltage Derivation}:
The gate voltage required to achieve strong inversion ($V_{th}$) equals flatband voltage plus oxide voltage drop plus surface potential:
\begin{equation}
\mathbf{V_{th} = V_{FB} + 2\phi_B + \frac{\sqrt{2\epsilon_s q N_a (2\phi_B)}}{C_{ox}}}
\end{equation}
where $V_{FB} = \Phi_{ms} - \frac{Q_{ox}}{C_{ox}}$ accounts for work function difference and oxide charges."""
    ),
    (
        r"Compare Zener Breakdown and Avalanche Breakdown in reverse-biased p-n junctions. Contrast their physical mechanisms, breakdown voltage thresholds, electric field values, and temperature coefficients.",
        r"""\textbf{1. Comprehensive Comparison Table}:
\begin{center}
\begin{tabularx}{\textwidth}{|l|X|X|}
\hline
\textbf{Parameter} & \textbf{Zener Breakdown} & \textbf{Avalanche Breakdown} \\
\hline
\textbf{Doping Concentration} & Very heavily doped ($N_a, N_d > 10^{18}\text{ cm}^{-3}$) & Lightly to moderately doped ($N_a, N_d < 10^{17}\text{ cm}^{-3}$) \\
\textbf{Depletion Width} & Extremely thin ($W < 10\text{ nm} = 100\text{ \AA}$) & Wide ($W > 1\;\mu\text{m}$) \\
\textbf{Electric Field} & Intense ($E > 10^6\text{ V/cm} = 10^8\text{ V/m}$) & Moderate ($E \sim 10^5\text{ V/cm}$) \\
\textbf{Physical Mechanism} & Quantum mechanical tunneling of valence electrons across narrow gap & Impact ionization / carrier multiplication by energetic carriers \\
\textbf{Breakdown Voltage} & Low ($V_Z < 5\text{--}6\text{ V}$) & High ($V_B > 6\text{--}8\text{ V}$) \\
\textbf{Temperature Coefficient} & \textbf{Negative} ($\frac{dV_Z}{dT} < 0$): $E_g$ decreases with $T$, making tunneling easier & \textbf{Positive} ($\frac{dV_B}{dT} > 0$): Lattice vibrations increase phonon scattering, requiring higher field \\
\textbf{I-V Knee Characteristic} & Very sharp and stable & Slightly softer knee \\
\hline
\end{tabularx}
\end{center}

\textbf{2. Practical Implication}:
Zener diodes engineered with breakdown voltage near $\sim 5.6\text{ V}$ combine Zener and Avalanche mechanisms with opposite temperature coefficients, achieving a near-zero overall temperature drift ideal for precision voltage references."""
    ),
    (
        r"A Hall effect measurement is performed on a rectangular slice of Silicon with dimensions $L = 10\text{ mm}$, width $w = 2.0\text{ mm}$, and thickness $t = 0.5\text{ mm}$. A longitudinal current $I_x = 5.0\text{ mA}$ is applied. In a magnetic field $B_z = 0.60\text{ T}$, the measured Hall voltage is $V_H = -12.5\text{ mV}$. The longitudinal voltage drop along length $L$ is $V_x = 2.0\text{ V}$. (a) Determine the majority carrier type and concentration $n$. (b) Calculate the Hall coefficient $R_H$. (c) Find the electrical conductivity $\sigma$ and electron drift mobility $\mu_n$.",
        r"""\textbf{1. Determination of Majority Carrier Type}:
The measured Hall voltage is negative ($V_H = -12.5\text{ mV}$), indicating that accumulated transverse carriers are electrons.
Therefore, the sample is an \textbf{n-type semiconductor}.

\textbf{2. Hall Coefficient ($R_H$) and Carrier Density ($n$)}:
From the Hall voltage formula:
\begin{equation}
V_H = \frac{R_H I_x B_z}{t} \implies \mathbf{R_H = \frac{V_H t}{I_x B_z}}
\end{equation}
\begin{align*}
R_H &= \frac{(-12.5 \times 10^{-3}\text{ V})(0.5 \times 10^{-3}\text{ m})}{(5.0 \times 10^{-3}\text{ A})(0.60\text{ T})} = \frac{-6.25 \times 10^{-6}}{3.0 \times 10^{-3}} = \mathbf{-2.083 \times 10^{-3}\text{ m}^3/\text{C}}
\end{align*}
Carrier concentration:
\begin{equation}
\mathbf{n} = \frac{1}{q |R_H|} = \frac{1}{(1.602 \times 10^{-19}\text{ C})(2.083 \times 10^{-3}\text{ m}^3/\text{C})} = \mathbf{3.00 \times 10^{21}\text{ m}^{-3}} = \mathbf{3.00 \times 10^{15}\text{ cm}^{-3}}
\end{equation}

\textbf{3. Electrical Conductivity ($\sigma$)}:
The sample cross-sectional area is $A = w \times t = (2.0 \times 10^{-3})(0.5 \times 10^{-3}) = 1.0 \times 10^{-6}\text{ m}^2$.
Sample resistance:
\begin{equation}
R = \frac{V_x}{I_x} = \frac{2.0\text{ V}}{5.0 \times 10^{-3}\text{ A}} = 400\text{ }\Omega
\end{equation}
Conductivity:
\begin{equation}
\mathbf{\sigma} = \frac{L}{R A} = \frac{10 \times 10^{-3}\text{ m}}{(400\text{ }\Omega)(1.0 \times 10^{-6}\text{ m}^2)} = \mathbf{25.0\text{ }\Omega^{-1}\text{m}^{-1}\text{ (or S/m)}}
\end{equation}

\textbf{4. Electron Drift Mobility ($\mu_n$)}:
\begin{equation}
\mathbf{\mu_n} = \sigma |R_H| = (25.0\text{ S/m})(2.083 \times 10^{-3}\text{ m}^3/\text{C}) = \mathbf{0.0521\text{ m}^2/(\text{V}\cdot\text{s})} = \mathbf{521\text{ cm}^2/(\text{V}\cdot\text{s})}
\end{equation}"""
    )
]

