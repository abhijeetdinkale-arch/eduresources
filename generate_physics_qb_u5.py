# generate_physics_qb_u5.py
# -*- coding: utf-8 -*-

def get_unit_5_content():
    unit_num = 5
    unit_title = "Semiconductor Physics and Solid State"
    
    mcqs = [
        # Part I: Foundational (1-50)
        (
            r"The Wiedemann-Franz Law states that the ratio of thermal conductivity $K$ to electrical conductivity $\sigma$ for metals is:",
            r"Directly proportional to absolute temperature $T$ ($K/\sigma = L T$)",
            r"Inversely proportional to temperature $T$",
            r"Independent of temperature",
            r"Zero at all temperatures",
            "(a)",
            r"The Wiedemann-Franz Law establishes that $K/\sigma = L T$, where Lorenz number $L = \frac{\pi^2 k_B^2}{3e^2} \approx 2.44 \times 10^{-8}\text{ W}\cdot\Omega/\text{K}^2$."
        ),
        (
            r"The classical Drude electrical conductivity $\sigma$ of a free electron gas with density $n$, relaxation time $\tau$, and electron mass $m$ is:",
            r"$\sigma = \frac{n e^2 \tau}{m}$",
            r"$\sigma = \frac{n e \tau}{m^2}$",
            r"$\sigma = \frac{m}{n e^2 \tau}$",
            r"$\sigma = n e \tau$",
            "(a)",
            r"Drude free electron theory gives $\sigma = n e^2\tau / m$."
        ),
        (
            r"At absolute zero temperature ($T = 0\text{ K}$), the Fermi-Dirac distribution function $f(E)$ for $E < E_F$ is:",
            r"$1.0$ (completely occupied)",
            r"$0.5$",
            r"$0$",
            r"$\infty$",
            "(a)",
            r"At $T = 0\text{ K}$, all energy states below the Fermi level $E_F$ are $100\%$ occupied ($f(E) = 1$)."
        ),
        (
            r"At absolute zero temperature ($T = 0\text{ K}$), the Fermi-Dirac distribution function $f(E)$ for $E > E_F$ is:",
            r"$0$ (completely empty)",
            r"$1.0$",
            r"$0.5$",
            r"$-1.0$",
            "(a)",
            r"At $T = 0\text{ K}$, all energy states above $E_F$ are completely unoccupied ($f(E) = 0$)."
        ),
        (
            r"At any finite temperature $T > 0\text{ K}$, the probability of occupancy of an energy state precisely at the Fermi level $E = E_F$ is:",
            r"$0.5$ ($50\%$)",
            r"$1.0$",
            r"$0$",
            r"$0.25$",
            "(a)",
            r"$f(E_F) = \frac{1}{1 + e^{(E_F - E_F)/k_BT}} = \frac{1}{1 + e^0} = \frac{1}{1 + 1} = 0.5$."
        ),
        (
            r"In an intrinsic (pure) semiconductor, the Fermi level $E_{Fi}$ lies:",
            r"Essentially in the middle of the forbidden energy bandgap ($E_g/2$)",
            r"Inside the conduction band",
            r"Inside the valence band",
            r"At the vacuum level",
            "(a)",
            r"For equal effective masses, $E_{Fi} = \frac{E_c + E_v}{2}$, located precisely at the bandgap midpoint."
        ),
        (
            r"The Kronig-Penney model explains the origin of energy bands in solids by analyzing electron motion in a:",
            r"1D periodic square-well lattice potential representing crystalline atomic ion cores",
            r"Completely uniform constant potential",
            r"Coulomb potential of a single isolated atom",
            r"Random chaotic potential",
            "(a)",
            r"The Kronig-Penney model applies Bloch's theorem to a periodic array of potential barriers, generating allowed energy bands and forbidden gaps."
        ),
        (
            r"In a direct bandgap semiconductor (such as GaAs or InP):",
            r"The conduction band minimum and valence band maximum occur at the exact same crystal wavevector ($k = 0$)",
            r"The band extrema occur at different $k$-values",
            r"The bandgap is zero",
            r"Photons cannot be emitted",
            "(a)",
            r"Direct band alignment permits rapid radiative electron-hole recombination with direct photon emission without phonon participation."
        ),
        (
            r"In an indirect bandgap semiconductor (such as Silicon or Germanium):",
            r"Electron-hole recombination requires both a photon and a lattice phonon to conserve energy and crystal momentum simultaneously",
            r"Photons can never be absorbed",
            r"Effective mass is zero",
            r"Energy bands do not exist",
            "(a)",
            r"Because conduction minimum and valence maximum are displaced in $k$-space, radiative transitions require a phonon to satisfy $\Delta k \ne 0$."
        ),
        (
            r"Why is Gallium Arsenide (GaAs) used for LEDs and semiconductor lasers, whereas Silicon (Si) is not?",
            r"GaAs is a direct bandgap semiconductor with high radiative efficiency, while Si is an indirect bandgap material where non-radiative phonon relaxation dominates",
            r"Silicon is an insulator",
            r"GaAs has zero electrical resistance",
            r"Silicon cannot be doped",
            "(a)",
            r"Direct bandgap GaAs produces efficient light emission, whereas indirect bandgap Silicon releases recombination energy as thermal lattice heat."
        ),
        (
            r"The Law of Mass Action in non-degenerate semiconductors states that under thermal equilibrium:",
            r"$n \cdot p = n_i^2$",
            r"$n + p = n_i$",
            r"$n / p = n_i$",
            r"$n \cdot p = N_D N_A$",
            "(a)",
            r"The product of electron concentration $n$ and hole concentration $p$ is a constant dependent only on temperature: $n p = n_i^2(T)$."
        ),
        (
            r"An n-type semiconductor is created by doping pure Silicon (tetravalent, Group IV) with:",
            r"Pentavalent donor impurity atoms from Group V (e.g., Phosphorus, Arsenic, Antimony)",
            r"Trivalent acceptor impurity atoms from Group III (e.g., Boron, Gallium)",
            r"Noble gas atoms",
            r"Gold atoms only",
            "(a)",
            r"Group V donor atoms donate extra conduction electrons, creating majority carrier electron concentration $n \approx N_D$."
        ),
        (
            r"A p-type semiconductor is created by doping pure Silicon with:",
            r"Trivalent acceptor impurity atoms from Group III (e.g., Boron, Aluminum, Gallium, Indium)",
            r"Pentavalent donor atoms",
            r"Iron atoms",
            r"Oxygen molecules",
            "(a)",
            r"Group III acceptor atoms accept electrons from the valence band, creating majority carrier hole concentration $p \approx N_A$."
        ),
        (
            r"In an n-type semiconductor, the donor energy level $E_d$ lies:",
            r"Just below the bottom of the conduction band $E_c$ ($\Delta E \approx 0.01\text{--}0.05\text{ eV}$)",
            r"Just above the top of the valence band $E_v$",
            r"In the exact middle of the bandgap",
            r"Deep inside the valence band",
            "(a)",
            r"Donor levels lie only tens of $\text{meV}$ below $E_c$, allowing room-temperature thermal energy ($k_BT \approx 26\text{ meV}$) to ionize nearly all donors."
        ),
        (
            r"In a p-type semiconductor, the acceptor energy level $E_a$ lies:",
            r"Just above the top of the valence band $E_v$ ($\Delta E \approx 0.01\text{--}0.05\text{ eV}$)",
            r"Just below the conduction band",
            r"At the center of the bandgap",
            r"Inside the conduction band",
            "(a)",
            r"Acceptor levels lie slightly above $E_v$, so valence electrons easily jump into $E_a$, leaving behind free mobile holes in the valence band."
        ),
        (
            r"As the temperature of an extrinsic n-type semiconductor increases to very high levels ($T > 500\text{ K}$), the semiconductor behaves as:",
            r"An intrinsic semiconductor (intrinsic carrier generation $n_i(T)$ overwhelms doping $N_D$)",
            r"A superconductor",
            r"A perfect dielectric",
            r"A ferromagnetic metal",
            "(a)",
            r"At high temperatures, thermal band-to-band excitation causes $n_i(T) \gg N_D$, causing the material to transition into the intrinsic regime."
        ),
        (
            r"The effective mass $m^*$ of an electron in a crystal band with energy dispersion relation $E(k)$ is given by:",
            r"$m^* = \frac{\hbar^2}{\frac{d^2 E}{dk^2}}$",
            r"$m^* = \hbar^2 \frac{d^2 E}{dk^2}$",
            r"$m^* = \frac{1}{\hbar}\frac{dE}{dk}$",
            r"$m^* = \frac{\hbar k}{E}$",
            "(a)",
            r"Effective mass reflects lattice force interactions: $m^* = \hbar^2 / (d^2E/dk^2)$."
        ),
        (
            r"Drift velocity $v_d$ of charge carriers in an applied electric field $E$ is related to mobility $\mu$ by:",
            r"$v_d = \mu E$",
            r"$v_d = \mu / E$",
            r"$v_d = \mu E^2$",
            r"$v_d = E / \mu$",
            "(a)",
            r"Drift velocity is directly proportional to applied electric field: $v_d = \mu E$."
        ),
        (
            r"The total electrical conductivity $\sigma$ of a semiconductor with electron mobility $\mu_n$ and hole mobility $\mu_p$ is:",
            r"$\sigma = q (n \mu_n + p \mu_p)$",
            r"$\sigma = q (n \mu_n - p \mu_p)$",
            r"$\sigma = \frac{q}{n \mu_n + p \mu_p}$",
            r"$\sigma = q n p (\mu_n + \mu_p)$",
            "(a)",
            r"Total conductivity is the sum of electron and hole drift conductivities: $\sigma = q(n\mu_n + p\mu_p)$."
        ),
        (
            r"Why is the electron mobility $\mu_n$ always greater than the hole mobility $\mu_p$ in Silicon ($\mu_n \approx 1350\text{ cm}^2/\text{V}\cdot\text{s}$ vs $\mu_p \approx 480\text{ cm}^2/\text{V}\cdot\text{s}$)?",
            r"Electrons move in the conduction band with a smaller effective mass ($m_e^* < m_h^*$) compared to holes moving in the valence band",
            r"Holes have negative charge",
            r"Electrons are not affected by phonons",
            r"Silicon contains no holes",
            "(a)",
            r"Conduction band curvature is sharper than valence band curvature, giving electrons smaller effective mass and higher mobility."
        ),
        (
            r"The Einstein relation connecting diffusion coefficient $D$ and carrier mobility $\mu$ at temperature $T$ is:",
            r"$\frac{D_n}{\mu_n} = \frac{D_p}{\mu_p} = \frac{k_B T}{q} = V_T$",
            r"$\frac{D}{\mu} = \frac{q}{k_B T}$",
            r"$D \cdot \mu = \frac{k_B T}{q}$",
            r"$\frac{D}{\mu} = k_B T q$",
            "(a)",
            r"The Einstein relation establishes $\frac{D}{\mu} = \frac{k_BT}{q} = V_T \approx 25.9\text{ mV}$ at room temperature ($300\text{ K}$)."
        ),
        (
            r"The thermal voltage $V_T = \frac{k_B T}{q}$ at room temperature ($T = 300\text{ K}$) is approximately equal to:",
            r"$25.9\text{ mV} \approx 26\text{ mV}$",
            r"$1.0\text{ V}$",
            r"$0.7\text{ V}$",
            r"$120\text{ mV}$",
            "(a)",
            r"$V_T = \frac{(1.38 \times 10^{-23}\text{ J/K})(300\text{ K})}{1.602 \times 10^{-19}\text{ C}} \approx 0.02585\text{ V} \approx 25.9\text{ mV}$."
        ),
        (
            r"The Hall Effect occurs when a current-carrying semiconductor sample is placed in a transverse magnetic field, generating a transverse electric field due to the:",
            r"Magnetic Lorentz force $\vec{F} = q(\vec{v}_d \times \vec{B})$ deflecting charge carriers to the lateral faces",
            r"Coulomb repulsion between ions",
            r"Thermal expansion of the semiconductor",
            r"Photoelectric effect",
            "(a)",
            r"Moving carriers experience transverse Lorentz force $q(\vec{v}_d \times \vec{B})$, accumulating on side faces to produce the Hall voltage."
        ),
        (
            r"The Hall coefficient $R_H$ for an n-type semiconductor where electrons dominate is given by:",
            r"$R_H = -\frac{1}{n q}$",
            r"$R_H = +\frac{1}{n q}$",
            r"$R_H = -n q$",
            r"$R_H = 0$",
            "(a)",
            r"For n-type material, majority carriers are electrons ($q = -e$), giving negative Hall coefficient $R_H = -1/(ne)$."
        ),
        (
            r"A positive Hall coefficient ($R_H > 0$) experimentally confirms that the semiconductor sample is:",
            r"p-type (majority charge carriers are positive holes)",
            r"n-type",
            r"A perfect insulator",
            r"A superconductor",
            "(a)",
            r"A positive sign for $R_H = +1/(pq)$ proves that holes are the majority mobile charge carriers."
        ),
        (
            r"The Hall Voltage $V_H$ developed across a semiconductor slab of thickness $w$ carrying current $I$ in magnetic field $B$ is:",
            r"$V_H = \frac{R_H I B}{w}$",
            r"$V_H = R_H I B w$",
            r"$V_H = \frac{I B}{R_H w}$",
            r"$V_H = \frac{R_H w}{I B}$",
            "(a)",
            r"Balancing electric and magnetic forces gives $V_H = E_H d = \frac{R_H J B}{\dots} \implies V_H = \frac{R_H I B}{w}$."
        ),
        (
            r"Hall mobility $\mu_H$ is related to Hall coefficient $R_H$ and electrical conductivity $\sigma$ by:",
            r"$\mu_H = |R_H| \sigma$",
            r"$\mu_H = \frac{|R_H|}{\sigma}$",
            r"$\mu_H = \frac{\sigma}{|R_H|}$",
            r"$\mu_H = |R_H| \sigma^2$",
            "(a)",
            r"Combining $R_H = 1/(nq)$ and $\sigma = nq\mu$ yields the Hall mobility formula $\mu_H = |R_H|\sigma$."
        ),
        (
            r"In a p-n junction under thermal equilibrium (zero external bias), the net electric current across the junction is:",
            r"Strictly zero ($I_{\text{drift}} + I_{\text{diffusion}} = 0$)",
            r"Infinite",
            r"Positive forward current",
            r"Equal to saturation current $I_0$",
            "(a)",
            r"At equilibrium, hole diffusion current is exactly balanced by hole drift current, and electron diffusion balances electron drift, giving zero net current."
        ),
        (
            r"The built-in potential barrier $V_{bi}$ across a step-graded p-n junction at temperature $T$ is given by:",
            r"$V_{bi} = \frac{k_B T}{q}\ln\left(\frac{N_A N_D}{n_i^2}\right)$",
            r"$V_{bi} = \frac{k_B T}{q}\ln\left(\frac{n_i^2}{N_A N_D}\right)$",
            r"$V_{bi} = \frac{q}{k_B T}\ln\left(\frac{N_A N_D}{n_i^2}\right)$",
            r"$V_{bi} = \frac{k_B T}{q}\left(\frac{N_A + N_D}{n_i}\right)$",
            "(a)",
            r"Integrating Poisson's equation across the depletion region yields $V_{bi} = V_T \ln(N_A N_D / n_i^2)$."
        ),
        (
            r"The depletion region (space-charge layer) of a p-n junction consists of:",
            r"Immobile ionized donor ions ($N_D^+$) on the n-side and immobile ionized acceptor ions ($N_A^-$) on the p-side, devoid of free mobile carriers",
            r"High concentrations of free electrons and holes",
            r"Pure neutral silicon atoms only",
            r"Liquid electrolyte",
            "(a)",
            r"Carrier diffusion leaves behind exposed uncompensated fixed donor ($N_D^+$) and acceptor ($N_A^-$) ionic space charge."
        ),
        (
            r"When a p-n junction is Forward Biased (positive terminal connected to p-side):",
            r"The potential barrier height decreases ($V_{bi} - V_a$) and depletion layer width narrows, allowing large diffusion current",
            r"The depletion layer widens",
            r"The built-in potential increases",
            r"Current drops to zero",
            "(a)",
            r"Forward bias opposes the built-in field, reducing the barrier height and allowing majority carriers to diffuse readily across the junction."
        ),
        (
            r"When a p-n junction is Reverse Biased (positive terminal connected to n-side):",
            r"The potential barrier increases ($V_{bi} + V_R$) and depletion width widens, allowing only tiny minority carrier reverse saturation current $I_0$",
            r"A massive forward current flows",
            r"The barrier height drops to zero",
            r"The bandgap vanishes",
            "(a)",
            r"Reverse bias reinforces the built-in electric field, widening the space-charge width $W \propto \sqrt{V_{bi} + V_R}$."
        ),
        (
            r"The Shockley ideal diode equation relating current $I$ to applied voltage $V$ is:",
            r"$I = I_0 \left(e^{qV/\eta k_BT} - 1\right)$",
            r"$I = I_0 e^{qV/\eta k_BT}$",
            r"$I = I_0 \left(e^{-qV/k_BT} + 1\right)$",
            r"$I = \frac{V}{R_0}$",
            "(a)",
            r"The ideal diode current-voltage relationship is $I = I_0 (e^{qV/\eta k_BT} - 1)$, where $\eta$ is the ideality factor."
        ),
        (
            r"The photovoltaic effect in a Solar Cell generates electricity through:",
            r"Photogeneration of electron-hole pairs by incident photons ($h\nu \ge E_g$) and separation of carriers by the built-in electric field of a p-n junction",
            r"Heating of the silicon wafer to boil water",
            r"Chemical oxidation of metal electrodes",
            r"Piezoelectric crystal deformation",
            "(a)",
            r"Photons create electron-hole pairs in the depletion region; the built-in field sweeps electrons to the n-side and holes to the p-side, producing photovoltage."
        ),
        (
            r"The Fill Factor ($FF$) of a solar cell with open-circuit voltage $V_{oc}$, short-circuit current $I_{sc}$, and maximum power point $(V_m, I_m)$ is:",
            r"$FF = \frac{V_m I_m}{V_{oc} I_{sc}} = \frac{P_{\text{max}}}{V_{oc} I_{sc}}$",
            r"$FF = \frac{V_{oc} I_{sc}}{V_m I_m}$",
            r"$FF = \frac{V_m}{V_{oc}} + \frac{I_m}{I_{sc}}$",
            r"$FF = V_{oc} I_{sc}$",
            "(a)",
            r"Fill Factor measures squareness of the $I$-$V$ curve: $FF = P_{\text{max}} / (V_{oc} I_{sc}) < 1.0$ (typically $0.7\text{--}0.85$)."
        ),
        (
            r"The power conversion efficiency $\eta$ of a solar cell illuminated by optical input power $P_{\text{in}}$ is:",
            r"$\eta = \frac{P_{\text{max}}}{P_{\text{in}}} = \frac{V_{oc} I_{sc} FF}{P_{\text{in}}}$",
            r"$\eta = \frac{P_{\text{in}}}{P_{\text{max}}}$",
            r"$\eta = \frac{V_{oc}}{I_{sc} P_{\text{in}}}$",
            r"$\eta = FF \times P_{\text{in}}$",
            "(a)",
            r"Solar cell efficiency is the ratio of maximum electrical power output to total incident optical irradiance power: $\eta = (V_{oc} I_{sc} FF)/P_{\text{in}}$."
        ),
        (
            r"A Photodiode is operated in which electrical bias regime to achieve high speed and linearity?",
            r"Reverse Bias",
            r"Forward Bias",
            r"Zero Bias (open circuit)",
            r"High AC Voltage",
            "(a)",
            r"Reverse bias widens the depletion region, minimizes junction capacitance ($C_j \propto 1/W$), and accelerates carrier transit time."
        ),
        (
            r"A Light Emitting Diode (LED) emits spontaneous light when operated in:",
            r"Forward Bias",
            r"Reverse Bias",
            r"Breakdown regime",
            r"Zero Bias",
            "(a)",
            r"Forward bias injects majority carriers across the junction, resulting in radiative electron-hole recombination."
        ),
        (
            r"The depletion width $W$ of a step-graded p-n junction with doping $N_A, N_D$ under applied voltage $V_a$ is proportional to:",
            r"$W \propto \sqrt{V_{bi} - V_a}$",
            r"$W \propto (V_{bi} - V_a)^2$",
            r"$W \propto \frac{1}{V_{bi} - V_a}$",
            r"$W \propto (V_{bi} - V_a)$",
            "(a)",
            r"From Poisson's equation, depletion width scales as $W = \sqrt{\frac{2\epsilon_s}{q}\left(\frac{1}{N_A} + \frac{1}{N_D}\right)(V_{bi} - V_a)}$."
        ),
        (
            r"In an asymmetric one-sided step junction ($p^+$-$n$ where $N_A \gg N_D$):",
            r"The depletion region extends almost entirely into the lightly doped n-side ($W \approx x_n$)",
            r"The depletion region extends equally into both sides",
            r"The depletion region lies exclusively on the $p^+$ side",
            r"No depletion region exists",
            "(a)",
            r"Charge neutrality requires $q N_A x_p = q N_D x_n$. Since $N_A \gg N_D$, $x_p \ll x_n$, so depletion penetrates into the lightly doped region."
        ),
        (
            r"In intrinsic Silicon at $T = 300\text{ K}$, intrinsic carrier concentration is $n_i \approx 1.5 \times 10^{10}\text{ cm}^{-3}$. If Silicon is doped with $N_D = 10^{16}\text{ cm}^{-3}$ Arsenic atoms, the minority hole concentration $p$ is:",
            r"$2.25 \times 10^4\text{ cm}^{-3}$",
            r"$1.5 \times 10^6\text{ cm}^{-3}$",
            r"$10^{16}\text{ cm}^{-3}$",
            r"$2.25 \times 10^{10}\text{ cm}^{-3}$",
            "(a)",
            r"By Mass Action: $p = \frac{n_i^2}{n} \approx \frac{(1.5 \times 10^{10})^2}{10^{16}} = \frac{2.25 \times 10^{20}}{10^{16}} = 2.25 \times 10^4\text{ cm}^{-3}$."
        ),
        (
            r"For the doped Silicon sample in Question 41, the shift of the Fermi level $(E_F - E_{Fi})$ above the intrinsic level is ($k_BT = 0.0259\text{ eV}$):",
            r"$0.347\text{ eV}$",
            r"$0.026\text{ eV}$",
            r"$0.550\text{ eV}$",
            r"$1.120\text{ eV}$",
            "(a)",
            r"$E_F - E_{Fi} = k_BT \ln\left(\frac{N_D}{n_i}\right) = 0.0259 \ln\left(\frac{10^{16}}{1.5 \times 10^{10}}\right) = 0.0259 \ln(6.67 \times 10^5) = 0.0259(13.41) \approx 0.347\text{ eV}$."
        ),
        (
            r"A semiconductor sample of thickness $w = 0.5\text{ mm}$ carrying current $I = 10\text{ mA}$ in magnetic field $B = 0.5\text{ T}$ produces a Hall voltage $V_H = 5.0\text{ mV}$. The Hall coefficient $R_H$ is:",
            r"$5.0 \times 10^{-4}\text{ m}^3/\text{C}$",
            r"$5.0 \times 10^{-3}\text{ m}^3/\text{C}$",
            r"$2.5 \times 10^{-2}\text{ m}^3/\text{C}$",
            r"$1.0 \times 10^{-5}\text{ m}^3/\text{C}$",
            "(a)",
            r"$R_H = \frac{V_H w}{I B} = \frac{(5 \times 10^{-3}\text{ V})(0.5 \times 10^{-3}\text{ m})}{(10 \times 10^{-3}\text{ A})(0.5\text{ T})} = \frac{2.5 \times 10^{-6}}{5 \times 10^{-3}} = 5.0 \times 10^{-4}\text{ m}^3/\text{C}$."
        ),
        (
            r"For the sample in Question 43, the majority carrier concentration $n$ is:",
            r"$1.25 \times 10^{22}\text{ m}^{-3} = 1.25 \times 10^{16}\text{ cm}^{-3}$",
            r"$6.25 \times 10^{18}\text{ m}^{-3}$",
            r"$1.25 \times 10^{14}\text{ cm}^{-3}$",
            r"$3.00 \times 10^{15}\text{ cm}^{-3}$",
            "(a)",
            r"$n = \frac{1}{|R_H| q} = \frac{1}{(5.0 \times 10^{-4})(1.602 \times 10^{-19})} \approx 1.248 \times 10^{22}\text{ m}^{-3} = 1.25 \times 10^{16}\text{ cm}^{-3}$."
        ),
        (
            r"If the electrical conductivity of the sample in Question 43 is $\sigma = 270\text{ S/m}$, the Hall mobility $\mu_H$ is:",
            r"$0.135\text{ m}^2/\text{V}\cdot\text{s} = 1350\text{ cm}^2/\text{V}\cdot\text{s}$",
            r"$2700\text{ cm}^2/\text{V}\cdot\text{s}$",
            r"$480\text{ cm}^2/\text{V}\cdot\text{s}$",
            r"$500\text{ cm}^2/\text{V}\cdot\text{s}$",
            "(a)",
            r"$\mu_H = |R_H|\sigma = (5.0 \times 10^{-4}\text{ m}^3/\text{C})(270\text{ S/m}) = 0.135\text{ m}^2/\text{V}\cdot\text{s} = 1350\text{ cm}^2/\text{V}\cdot\text{s}$."
        ),
        (
            r"In a Silicon p-n junction with $N_A = 10^{17}\text{ cm}^{-3}$ and $N_D = 10^{16}\text{ cm}^{-3}$ ($n_i = 1.5 \times 10^{10}\text{ cm}^{-3}$), the built-in potential $V_{bi}$ at $300\text{ K}$ is:",
            r"$0.754\text{ V}$",
            r"$0.550\text{ V}$",
            r"$1.120\text{ V}$",
            r"$0.350\text{ V}$",
            "(a)",
            r"$V_{bi} = 0.0259 \ln\left(\frac{10^{17} \times 10^{16}}{(1.5 \times 10^{10})^2}\right) = 0.0259 \ln\left(\frac{10^{33}}{2.25 \times 10^{20}}\right) = 0.0259 \ln(4.44 \times 10^{12}) = 0.0259(29.12) \approx 0.754\text{ V}$."
        ),
        (
            r"A silicon solar cell has $V_{oc} = 0.60\text{ V}$, $I_{sc} = 3.0\text{ A}$, and $FF = 0.78$. The maximum electrical power output $P_{\text{max}}$ is:",
            r"$1.404\text{ W}$",
            r"$1.800\text{ W}$",
            r"$2.340\text{ W}$",
            r"$0.780\text{ W}$",
            "(a)",
            r"$P_{\text{max}} = V_{oc} \cdot I_{sc} \cdot FF = (0.60\text{ V})(3.0\text{ A})(0.78) = 1.404\text{ W}$."
        ),
        (
            r"If the solar cell in Question 47 has an active area $A = 100\text{ cm}^2 = 0.01\text{ m}^2$ under standard $1\text{ Sun}$ illumination ($P_{\text{opt}} = 1000\text{ W/m}^2$), its efficiency $\eta$ is:",
            r"$14.04\%$",
            r"$18.00\%$",
            r"$7.80\%$",
            r"$23.40\%$",
            "(a)",
            r"$P_{\text{in}} = 1000\text{ W/m}^2 \times 0.01\text{ m}^2 = 10\text{ W}$. $\eta = \frac{P_{\text{max}}}{P_{\text{in}}} = \frac{1.404\text{ W}}{10\text{ W}} = 0.1404 = 14.04\%$."
        ),
        (
            r"The temperature dependence of carrier mobility due to acoustic phonon (lattice) scattering follows:",
            r"$\mu_{\text{lattice}} \propto T^{-3/2}$",
            r"$\mu_{\text{lattice}} \propto T^{+3/2}$",
            r"$\mu_{\text{lattice}} \propto T^0$",
            r"$\mu_{\text{lattice}} \propto T^{-1}$",
            "(a)",
            r"As temperature increases, thermal lattice vibrations increase, causing electron-phonon collision rates to rise as $\mu \propto T^{-3/2}$."
        ),
        (
            r"The temperature dependence of carrier mobility due to ionized impurity scattering follows:",
            r"$\mu_{\text{impurity}} \propto T^{+3/2}$",
            r"$\mu_{\text{impurity}} \propto T^{-3/2}$",
            r"$\mu_{\text{impurity}} \propto 1/T$",
            r"$\mu_{\text{impurity}} \propto e^{-T}$",
            "(a)",
            r"Faster-moving thermal carriers spend less time near ionized dopant ions, reducing Coulomb deflection and increasing mobility as $\mu \propto T^{3/2}$."
        ),

        # Part II: Intermediate Analytical (51-80)
        (
            r"According to Matthiessen's Rule, the total carrier mobility $\mu$ combining lattice scattering ($\mu_L$) and impurity scattering ($\mu_I$) is:",
            r"$\frac{1}{\mu} = \frac{1}{\mu_L} + \frac{1}{\mu_I}$",
            r"$\mu = \mu_L + \mu_I$",
            r"$\mu = \sqrt{\mu_L \mu_I}$",
            r"$\mu = \mu_L - \mu_I$",
            "(a)",
            r"Scattering rates sum linearly: $\frac{1}{\tau_{\text{total}}} = \frac{1}{\tau_L} + \frac{1}{\tau_I} \implies \frac{1}{\mu} = \frac{1}{\mu_L} + \frac{1}{\mu_I}$."
        ),
        (
            r"The intrinsic carrier concentration $n_i$ of Silicon as a function of temperature $T$ scales predominantly as:",
            r"$n_i(T) \propto T^{3/2} \exp\left(-\frac{E_g}{2 k_B T}\right)$",
            r"$n_i(T) \propto \exp\left(-\frac{E_g}{k_B T}\right)$",
            r"$n_i(T) \propto T^3$",
            r"$n_i(T) \propto \frac{1}{T}$",
            "(a)",
            r"$n_i = \sqrt{N_c N_v}e^{-E_g/2k_BT}$, and since $N_c, N_v \propto T^{3/2}$, $n_i \propto T^{3/2} e^{-E_g/(2k_BT)}$."
        ),
        (
            r"If the energy bandgap of Silicon is $E_g = 1.12\text{ eV}$ and Germanium is $E_g = 0.67\text{ eV}$, at room temperature Germanium has:",
            r"A much higher intrinsic carrier concentration $n_i$ and lower resistivity than Silicon",
            r"Lower carrier concentration than Silicon",
            r"Zero intrinsic carriers",
            r"Identical resistivity to Silicon",
            "(a)",
            r"Because $E_g(\text{Ge}) < E_g(\text{Si})$, $e^{-E_g/2k_BT}$ is orders of magnitude larger for Ge ($n_i \approx 2.4 \times 10^{13}\text{ cm}^{-3}$ vs $1.5 \times 10^{10}\text{ cm}^{-3}$ in Si)."
        ),
        (
            r"The position of the intrinsic Fermi level $E_{Fi}$ relative to the bandgap midpoint $\frac{E_c + E_v}{2}$ is given by:",
            r"$E_{Fi} = \frac{E_c + E_v}{2} + \frac{3}{4}k_B T \ln\left(\frac{m_h^*}{m_e^*}\right)$",
            r"$E_{Fi} = \frac{E_c + E_v}{2} - \frac{3}{4}k_B T \ln\left(\frac{m_h^*}{m_e^*}\right)$",
            r"$E_{Fi} = \frac{E_c - E_v}{2}$",
            r"$E_{Fi} = E_c - k_B T$",
            "(a)",
            r"Setting $n = p \implies N_c e^{-(E_c-E_F)/k_BT} = N_v e^{-(E_F-E_v)/k_BT}$ gives $E_{Fi} = \frac{E_c+E_v}{2} + \frac{3}{4}k_BT\ln(m_h^*/m_e^*)$."
        ),
        (
            r"If hole effective mass $m_h^*$ exceeds electron effective mass $m_e^*$ ($m_h^* > m_e^*$), as temperature $T$ increases the intrinsic Fermi level $E_{Fi}$:",
            r"Shifts upward toward the conduction band",
            r"Shifts downward toward the valence band",
            r"Remains exactly static at absolute center",
            r"Enters the core band",
            "(a)",
            r"Because $\ln(m_h^*/m_e^*) > 0$, the positive term $\frac{3}{4}k_BT\ln(m_h^*/m_e^*)$ increases linearly with $T$, shifting $E_{Fi}$ upward."
        ),
        (
            r"In degenerate semiconductors (very heavily doped, $N_D > 10^{19}\text{ cm}^{-3}$):",
            r"The Fermi level $E_F$ is driven inside the conduction band ($E_F > E_c$) and the material exhibits metallic conduction",
            r"The bandgap becomes infinite",
            r"Current stops flowing",
            r"The material becomes an insulator",
            "(a)",
            r"Extreme donor doping forces $E_F$ above the conduction band edge $E_c$, causing the semiconductor to behave degenerately like a metal."
        ),
        (
            r"The Zener breakdown in a p-n junction is caused by:",
            r"Direct quantum mechanical tunneling of valence electrons on the p-side into the empty conduction band on the n-side under intense electric field ($> 10^6\text{ V/cm}$)",
            r"Impact ionization by accelerated carriers",
            r"Melting of the wire leads",
            r"Thermal runaway",
            "(a)",
            r"Zener breakdown occurs in heavily doped thin junctions ($V_Z < 5\text{ V}$) via direct quantum band-to-band tunneling."
        ),
        (
            r"The Avalanche breakdown in a p-n junction is caused by:",
            r"Impact ionization where accelerated carriers gain enough kinetic energy to knock valence electrons into the conduction band, initiating an electron avalanche",
            r"Direct quantum tunneling",
            r"Laser excitation",
            r"Chemical decomposition",
            "(a)",
            r"In lightly doped wide junctions ($V_{\text{BR}} > 6\text{ V}$), carriers trigger avalanche multiplication through high-energy impact ionization."
        ),
        (
            r"The temperature coefficient of breakdown voltage is:",
            r"Negative for Zener breakdown and positive for Avalanche breakdown",
            r"Positive for Zener and negative for Avalanche",
            r"Positive for both",
            r"Negative for both",
            "(a)",
            r"Zener tunneling increases with temperature (bandgap narrows $\implies$ negative tempco); avalanche breakdown decreases with temperature (more phonon scattering $\implies$ positive tempco)."
        ),
        (
            r"The junction capacitance $C_j$ of a reverse-biased step p-n junction varies with reverse voltage $V_R$ as:",
            r"$C_j \propto \frac{1}{\sqrt{V_{bi} + V_R}}$",
            r"$C_j \propto \sqrt{V_{bi} + V_R}$",
            r"$C_j \propto (V_{bi} + V_R)^2$",
            r"$C_j = \text{constant}$",
            "(a)",
            r"Because $C_j = \frac{\epsilon_s A}{W}$ and depletion width $W \propto \sqrt{V_{bi} + V_R}$, capacitance scales as $C_j \propto 1/\sqrt{V_{bi} + V_R}$."
        ),
        (
            r"A Varactor Diode utilizes which electrical property of a p-n junction for RF voltage-controlled tuning?",
            r"Voltage-dependent reverse junction capacitance $C_j(V_R)$",
            r"Forward diffusion conductance",
            r"Optical emission",
            r"Zener resistance",
            "(a)",
            r"Varactors operate as voltage-variable capacitors in reverse bias for RF frequency synthesizers and voltage-controlled oscillators (VCOs)."
        ),
        (
            r"The diffusion capacitance $C_d$ of a p-n junction under Forward Bias is caused by:",
            r"The storage of minority carrier excess charge distribution injected across the junction",
            r"Immobile space charge ions",
            r"The dielectric thickness of the casing",
            r"Magnetic induction of the leads",
            "(a)",
            r"Forward bias injects minority carriers whose stored charge $Q = I\tau$ varies with voltage, creating diffusion capacitance $C_d = \frac{q I \tau}{k_BT}$."
        ),
        (
            r"In Silicon, the electron diffusion length $L_n$ is related to electron diffusion coefficient $D_n$ and minority carrier lifetime $\tau_n$ by:",
            r"$L_n = \sqrt{D_n \tau_n}$",
            r"$L_n = D_n \tau_n$",
            r"$L_n = \frac{D_n}{\tau_n}$",
            r"$L_n = \sqrt{\frac{D_n}{\tau_n}}$",
            "(a)",
            r"Solving the steady-state continuity equation $\frac{d^2(\Delta n)}{dx^2} = \frac{\Delta n}{D_n\tau_n}$ defines diffusion length $L_n = \sqrt{D_n\tau_n}$."
        ),
        (
            r"Given $D_n = 35\text{ cm}^2/\text{s}$ and lifetime $\tau_n = 10\,\mu\text{s} = 10^{-5}\text{ s}$, the electron diffusion length $L_n$ is:",
            r"$1.87 \times 10^{-2}\text{ cm} = 187\,\mu\text{m}$",
            r"$350\,\mu\text{m}$",
            r"$18.7\,\mu\text{m}$",
            r"$1.87\text{ mm}$",
            "(a)",
            r"$L_n = \sqrt{D_n \tau_n} = \sqrt{35 \times 10^{-5}} = \sqrt{3.5 \times 10^{-4}} \approx 0.0187\text{ cm} = 187\,\mu\text{m}$."
        ),
        (
            r"The Haynes-Shockley experiment is an important semiconductor characterization technique that directly measures:",
            r"Minority carrier drift mobility $\mu$ and diffusion coefficient $D$",
            r"The energy bandgap $E_g$",
            r"The mass of the silicon atom",
            r"The crystal lattice constant",
            "(a)",
            r"The Haynes-Shockley experiment injects a minority pulse and tracks its drift time and dispersion to measure $\mu$ and $D$ directly."
        ),
        (
            r"In the Hall effect, the Hall angle $\theta_H$ between total current density $\vec{J}$ and total electric field $\vec{E}$ is given by:",
            r"$\tan \theta_H = \mu_H B$",
            r"$\tan \theta_H = \frac{\mu_H}{B}$",
            r"$\sin \theta_H = \mu_H B^2$",
            r"$\cos \theta_H = \mu_H B$",
            "(a)",
            r"$\tan\theta_H = E_H / E_x = (R_H J B)/ (J/\sigma) = R_H \sigma B = \mu_H B$."
        ),
        (
            r"For an intrinsic semiconductor where electrons and holes both contribute to the Hall effect, the Hall coefficient $R_H$ is:",
            r"$R_H = \frac{1}{q}\frac{p \mu_p^2 - n \mu_n^2}{(p \mu_p + n \mu_n)^2}$",
            r"$R_H = \frac{1}{q(n+p)}$",
            r"$R_H = 0$",
            r"$R_H = \frac{\mu_n - \mu_p}{q}$",
            "(a)",
            r"Two-carrier transport gives $R_H = \frac{1}{q}\frac{p\mu_p^2 - n\mu_n^2}{(p\mu_p + n\mu_n)^2}$. Since $\mu_n > \mu_p$, intrinsic Si has a slightly negative $R_H$."
        ),
        (
            r"The Quantum Hall Effect observed in 2D electron gases at cryogenic temperatures and high magnetic fields yields quantized Hall resistance:",
            r"$R_H = \frac{h}{\nu e^2} \quad (\nu = 1, 2, 3,\dots)$",
            r"$R_H = \frac{\nu h}{e}$",
            r"$R_H = \frac{h^2}{\nu e}$",
            r"$R_H = 0$",
            "(a)",
            r"Klaus von Klitzing discovered that 2D Hall resistance is quantized in integer steps of the von Klitzing constant $R_K = h/e^2 \approx 25812.807\,\Omega$."
        ),
        (
            r"The work function $\Phi_m$ of a metal and electron affinity $\chi_s$ of an n-type semiconductor determine the junction barrier. An ideal rectifying Schottky barrier forms when:",
            r"$\Phi_m > \chi_s$ (for n-type semiconductor)",
            r"$\Phi_m < \chi_s$",
            r"$\Phi_m = \chi_s$",
            r"$\chi_s = 0$",
            "(a)",
            r"For $\Phi_m > \chi_s$, electrons flow from semiconductor to metal until a built-in barrier $q\phi_{Bn} = \Phi_m - \chi_s$ forms, creating a rectifying Schottky diode."
        ),
        (
            r"An Ohmic contact (low-resistance non-rectifying contact) on an n-type semiconductor requires:",
            r"$\Phi_m < \chi_s$ or extremely heavy surface doping ($n^+$ layer for field tunneling)",
            r"$\Phi_m \gg \chi_s$",
            r"An insulating oxide layer",
            r"Reverse bias operation",
            "(a)",
            r"Ohmic contacts have negligible barrier or are so heavily doped that electrons easily tunnel through the thin barrier."
        ),
        (
            r"Schottky diodes have a major switching speed advantage over standard p-n junction diodes because:",
            r"They are majority carrier devices with zero minority carrier storage time ($\tau_{rr} \approx 0$)",
            r"They have infinite bandgap",
            r"They operate without electrons",
            r"They generate high reverse voltages",
            "(a)",
            r"Conduction is purely via majority electrons, eliminating minority carrier recombination delays and allowing switching in picoseconds."
        ),
        (
            r"The forward turn-on voltage of a Silicon Schottky diode is typically:",
            r"$0.2\text{--}0.3\text{ V}$ (compared to $0.7\text{ V}$ for standard Si p-n diode)",
            r"$0.7\text{ V}$",
            r"$1.5\text{ V}$",
            r"$5.0\text{ V}$",
            "(a)",
            r"Lower barrier heights in Schottky junctions yield lower forward voltage drops ($\approx 0.2\text{--}0.3\text{ V}$), reducing conduction power losses."
        ),
        (
            r"In a Solar Cell under illumination, the short-circuit current $I_{sc}$ is directly proportional to:",
            r"The incident optical illumination intensity $P_{\text{opt}}$",
            r"The square of the illumination intensity",
            r"The temperature only",
            r"The load resistance",
            "(a)",
            r"Photogeneration rate $G = \eta_{\text{opt}}\Phi_{\text{photon}}$ is linearly proportional to incident photon flux: $I_{sc} \approx I_L \propto P_{\text{opt}}$."
        ),
        (
            r"The open-circuit voltage $V_{oc}$ of an ideal solar cell is given by:",
            r"$V_{oc} = \frac{k_B T}{q}\ln\left(\frac{I_{sc}}{I_0} + 1\right)$",
            r"$V_{oc} = \frac{I_{sc} R_s}{I_0}$",
            r"$V_{oc} = \frac{k_B T}{q}\left(\frac{I_{sc}}{I_0}\right)$",
            r"$V_{oc} = V_{bi}$",
            "(a)",
            r"Setting net current $I = 0 = I_{sc} - I_0(e^{qV_{oc}/k_BT}-1)$ yields $V_{oc} = V_T \ln(I_{sc}/I_0 + 1)$."
        ),
        (
            r"As the operating temperature of a Silicon solar cell increases, its efficiency $\eta$:",
            r"Decreases (due to exponential increase in reverse saturation current $I_0$ reducing $V_{oc}$)",
            r"Increases linearly",
            r"Remains perfectly constant",
            r"Doubles every $10^\circ\text{C}$",
            "(a)",
            r"Higher temperature dramatically increases intrinsic carrier density $n_i^2$, raising $I_0$ and reducing $V_{oc}$ by $\approx -2\text{ mV/}^\circ\text{C}$."
        ),
        (
            r"Anti-reflective coatings on solar cells (such as $\text{Si}_3\text{N}_4$ or $\text{TiO}_2$) with refractive index $n_{\text{ARC}} = \sqrt{n_{\text{Si}} n_{\text{air}}} \approx 1.9$ reduce bare silicon reflection from $\approx 35\%$ down to:",
            r"$< 2\text{--}3\%$",
            r"$25\%$",
            r"$50\%$",
            r"$0\%$ across all wavelengths",
            "(a)",
            r"Quarter-wavelength destructive interference coatings ($d = \lambda_0 / (4n_{\text{ARC}})$) eliminate front surface Fresnel reflections."
        ),
        (
            r"A Solar Cell has $V_{oc} = 0.62\text{ V}$, $I_{sc} = 4.0\text{ A}$, and maximum power $P_{\text{max}} = 1.984\text{ W}$. The Fill Factor $FF$ is:",
            r"$0.80$",
            r"$0.70$",
            r"$0.60$",
            r"$0.90$",
            "(a)",
            r"$FF = \frac{P_{\text{max}}}{V_{oc} I_{sc}} = \frac{1.984}{(0.62)(4.0)} = \frac{1.984}{2.48} = 0.80$."
        ),
        (
            r"The Shockley-Queisser theoretical efficiency limit for a single-junction Silicon solar cell under standard 1-Sun unconcentrated sunlight is approximately:",
            r"$\approx 33.7\%$",
            r"$100\%$",
            r"$50.0\%$",
            r"$15.0\%$",
            "(a)",
            r"Thermodynamic bandgap balance between unabsorbed sub-bandgap photons and thermalization losses limits single-junction cells to $\approx 33.7\%$."
        ),
        (
            r"In a Tunnel Diode (Esaki Diode), heavy degenerate doping on both p and n sides ($p^{++}$-$n^{++}$) creates a unique $I$-$V$ characteristic featuring:",
            r"Negative Differential Resistance (NDR) in the forward bias region",
            r"Infinite resistance",
            r"Zero current in all regimes",
            r"Strictly linear Ohm's law behavior",
            "(a)",
            r"Degenerate alignment of occupied conduction states with empty valence states allows tunneling, which drops as forward bias increases (NDR region)."
        ),
        (
            r"The Negative Differential Resistance (NDR) of a tunnel diode is widely used in high-frequency engineering for:",
            r"Microwave oscillators, high-speed pulse generators, and amplifiers",
            r"Solar power conversion",
            r"Battery charging",
            r"Audio loudspeakers",
            "(a)",
            r"NDR offsets circuit resistance losses, enabling microwave frequency oscillations in the gigahertz regime."
        ),

        # Part III: Advanced Mastery (81-100)
        (
            r"In the Kronig-Penney model, the dispersion relation is given by $P\frac{\sin(\alpha a)}{\alpha a} + \cos(\alpha a) = \cos(ka)$. The barrier strength parameter $P$ is defined as:",
            r"$P = \frac{m V_0 b a}{\hbar^2}$",
            r"$P = \frac{V_0}{E}$",
            r"$P = \frac{\hbar^2 k^2}{2m}$",
            r"$P = \frac{a}{b}$",
            "(a)",
            r"The dimensionless barrier strength $P = \frac{m V_0 b a}{\hbar^2}$ measures electron confinement; $P \to 0$ gives free electrons, $P \to \infty$ gives isolated atoms."
        ),
        (
            r"In the limit $P \to \infty$ in the Kronig-Penney dispersion relation, the energy spectrum reduces to:",
            r"Discrete, atomic-like bound states $\alpha a = n\pi \implies E_n = \frac{n^2 h^2}{8ma^2}$",
            r"A single continuous band",
            r"Zero energy everywhere",
            r"Negative infinity",
            "(a)",
            r"As $P \to \infty$, allowed energy bands shrink into infinitely sharp discrete atomic energy eigenvalues."
        ),
        (
            r"The first Brillouin zone for a 1D crystal lattice with lattice constant $a$ extends over the wavevector range:",
            r"$-\frac{\pi}{a} \le k \le +\frac{\pi}{a}$",
            r"$0 \le k \le \frac{\pi}{a}$",
            r"$-\frac{2\pi}{a} \le k \le +\frac{2\pi}{a}$",
            r"$-\infty < k < +\infty$",
            "(a)",
            r"The fundamental Wigner-Seitz cell in reciprocal space (first Brillouin zone) spans from $-\pi/a$ to $+\pi/a$."
        ),
        (
            r"At the edge of the first Brillouin zone ($k = \pm \pi/a$), the electron group velocity $v_g = \frac{1}{\hbar}\frac{dE}{dk}$ is:",
            r"$0$ (standing wave formation via Bragg reflection)",
            r"$c$",
            r"$v_F$",
            r"$\infty$",
            "(a)",
            r"At band edges, incident and Bragg-reflected waves form standing waves, meaning net forward group velocity vanishes ($v_g = 0$)."
        ),
        (
            r"The effective density of states in the conduction band $N_c$ for a 3D parabolic band is given by:",
            r"$N_c = 2 \left(\frac{2\pi m_e^* k_B T}{h^2}\right)^{3/2}$",
            r"$N_c = \left(\frac{m_e^* k_B T}{2\pi \hbar^2}\right)^{1/2}$",
            r"$N_c = 2 \frac{k_B T}{h}$",
            r"$N_c = \frac{n_i^2}{N_v}$",
            "(a)",
            r"Integrating density of states with Maxwell-Boltzmann tail gives $N_c = 2(2\pi m_e^* k_BT / h^2)^{3/2}$."
        ),
        (
            r"The effective density of states in the valence band $N_v$ is similarly:",
            r"$N_v = 2 \left(\frac{2\pi m_h^* k_B T}{h^2}\right)^{3/2}$",
            r"$N_v = N_c \frac{m_e^*}{m_h^*}$",
            r"$N_v = \sqrt{N_c}$",
            r"$N_v = 0$",
            "(a)",
            r"Similarly, the valence band effective density of states is $N_v = 2(2\pi m_h^* k_BT / h^2)^{3/2}$."
        ),
        (
            r"In the freeze-out temperature regime of an extrinsic n-type semiconductor ($T < 100\text{ K}$):",
            r"Thermal energy $k_BT$ is insufficient to ionize donor atoms, causing electrons to remain trapped in donor levels $E_d$",
            r"All electrons enter the conduction band",
            r"Resistivity drops to zero",
            r"The semiconductor melts",
            "(a)",
            r"At cryogenic temperatures, $k_BT \ll (E_c - E_d)$, so electrons freeze back into localized donor impurity states."
        ),
        (
            r"In the extrinsic saturation (exhaustion) regime ($150\text{ K} \le T \le 450\text{ K}$):",
            r"All donor atoms are $100\%$ ionized, maintaining a constant electron concentration $n \approx N_D$ independent of temperature",
            r"Carrier concentration drops exponentially",
            r"Intrinsic carriers exceed donors",
            r"Mobility becomes infinite",
            "(a)",
            r"Over normal operating temperatures, all dopants are fully ionized while intrinsic generation is negligible, keeping $n \approx N_D$ constant."
        ),
        (
            r"The Early Effect (Base-Width Modulation) in a Bipolar Junction Transistor (BJT) is caused by:",
            r"The widening of the reverse-biased collector-base depletion region narrowing the effective neutral base width $W_B$",
            r"Base melting",
            r"Thermal noise in emitter",
            r"Zener tunneling in the base",
            "(a)",
            r"Increasing reverse collector voltage $V_{CB}$ widens the space-charge layer into the base, reducing neutral base width $W_B$."
        ),
        (
            r"The Gunn Effect in III-V semiconductors (such as GaAs) arises from:",
            r"Field-induced transfer of conduction electrons from a high-mobility lower central valley ($\Gamma$) to low-mobility higher satellite valleys ($L$)",
            r"Acoustic phonon absorption",
            r"Photoelectric ionization",
            r"Nuclear magnetic resonance",
            "(a)",
            r"The Ridley-Watkins-Hilsum (RWH) transferred-electron mechanism creates negative differential mobility, producing microwave Gunn oscillations."
        ),
        (
            r"A Gunn Diode is widely used as a solid-state source of:",
            r"Microwave and Millimeter-wave radiation ($10\text{ GHz to }100\text{ GHz}$)",
            r"Visible red light",
            r"High-voltage DC power",
            r"Audio sound",
            "(a)",
            r"Transit of high-field dipole domains generates continuous microwave power in radar systems and wireless transceivers."
        ),
        (
            r"The IMPATT (Impact Ionization Avalanche Transit Time) diode generates high microwave power by combining:",
            r"Avalanche multiplication and carrier transit-time delay to create a $180^\circ$ phase lag between current and voltage",
            r"Direct bandgap emission",
            r"Photo-conduction",
            r"Superconducting flux pinning",
            "(a)",
            r"Impact ionization ($90^\circ$ phase lag) plus drift transit delay ($90^\circ$) yields a total $180^\circ$ phase shift, generating dynamic negative resistance."
        ),
        (
            r"The flat-band voltage $V_{\text{FB}}$ of a Metal-Oxide-Semiconductor (MOS) structure is given by:",
            r"$V_{\text{FB}} = \Phi_{\text{ms}} - \frac{Q_{\text{ox}}}{C_{\text{ox}}}$",
            r"$V_{\text{FB}} = \Phi_{\text{ms}} + \frac{Q_{\text{ox}}}{C_{\text{ox}}}$",
            r"$V_{\text{FB}} = \frac{Q_{\text{ox}}}{C_{\text{ox}}}$",
            r"$V_{\text{FB}} = 0$",
            "(a)",
            r"Flat-band voltage accounts for metal-semiconductor work function difference $\Phi_{\text{ms}}$ and fixed oxide charge: $V_{\text{FB}} = \Phi_{\text{ms}} - Q_{\text{ox}}/C_{\text{ox}}$."
        ),
        (
            r"In a MOSFET, strong inversion occurs when the surface potential $\psi_s$ reaches:",
            r"$\psi_s = 2 \phi_F = 2 \left(\frac{k_BT}{q}\right)\ln\left(\frac{N_A}{n_i}\right)$",
            r"$\psi_s = \phi_F$",
            r"$\psi_s = 0$",
            r"$\psi_s = V_{DD}$",
            "(a)",
            r"Strong inversion begins when the surface electron concentration equals the bulk majority hole concentration: $\psi_s = 2\phi_F$."
        ),
        (
            r"The subthreshold swing $S$ of an ideal MOSFET at room temperature ($300\text{ K}$) has a fundamental thermodynamic lower limit of:",
            r"$S \ge \ln(10)\frac{k_BT}{q} \approx 60\text{ mV/decade}$",
            r"$S = 0\text{ mV/decade}$",
            r"$S = 10\text{ mV/decade}$",
            r"$S = 100\text{ V/decade}$",
            "(a)",
            r"Boltzmann thermal tail limits subthreshold gate swing to $S = \ln(10)V_T \approx 2.3026 \times 25.85\text{ mV} \approx 60\text{ mV/decade}$."
        ),
        (
            r"Quantum confinement in a 2D electron gas (2DEG) formed at an $\text{AlGaAs/GaAs}$ heterojunction interface leads to:",
            r"Ultra-high electron mobility ($> 10^6\text{ cm}^2/\text{V}\cdot\text{s}$ at $4\text{ K}$) due to spatial separation of carriers from ionized donor dopants (Modulation Doping)",
            r"Zero conductivity",
            r"Insulating behavior",
            r"Loss of Fermi level",
            "(a)",
            r"High Electron Mobility Transistors (HEMT) use modulation doping to separate electrons in GaAs from ionized donors in AlGaAs, eliminating impurity scattering."
        ),
        (
            r"The Quantum Point Contact (QPC) demonstrates ballistic 1D transport where conductance is quantized in universal steps of:",
            r"$G = n \left(\frac{2 e^2}{h}\right) \quad (n = 1, 2, 3,\dots)$",
            r"$G = n \frac{e}{h}$",
            r"$G = \frac{h}{2e^2}$",
            r"$G = 0$",
            "(a)",
            r"Landauer formula for ballistic transport gives quantized conductance steps of $G_0 = \frac{2e^2}{h} \approx 77.48\,\mu\text{S} = \frac{1}{12.9\text{ k}\Omega}$."
        ),
        (
            r"In thermoelectric energy conversion, the figure of merit $ZT$ of a semiconductor is defined as:",
            r"$ZT = \frac{S^2 \sigma}{\kappa} T$",
            r"$ZT = \frac{S \sigma}{\kappa T}$",
            r"$ZT = \frac{\kappa}{S^2 \sigma T}$",
            r"$ZT = S \sigma \kappa T$",
            "(a)",
            r"Thermoelectric efficiency depends on Seebeck coefficient $S$, electrical conductivity $\sigma$, and thermal conductivity $\kappa$: $ZT = \frac{S^2 \sigma}{\kappa}T$."
        ),
        (
            r"Why are heavy-element semiconductors like Bismuth Telluride ($\text{Bi}_2\text{Te}_3$) and Silicon-Germanium ($\text{SiGe}$) preferred for thermoelectric generators?",
            r"They exhibit high power factors ($S^2\sigma$) and extremely low lattice thermal conductivity ($\kappa_{\text{lattice}}$) due to heavy atomic mass phonon scattering",
            r"They have infinite bandgap",
            r"They are transparent",
            r"They are magnetic",
            "(a)",
            r"Heavy atomic masses and complex unit cells scatter heat-carrying phonons, suppressing thermal conductivity $\kappa$ while preserving electrical conductivity $\sigma$."
        ),
        (
            r"The Hall coefficient for a high-purity p-type Silicon sample is measured as $R_H = +3.5 \times 10^{-2}\text{ m}^3/\text{C}$. The hole concentration $p$ is:",
            r"$1.78 \times 10^{20}\text{ m}^{-3} = 1.78 \times 10^{14}\text{ cm}^{-3}$",
            r"$3.50 \times 10^{16}\text{ cm}^{-3}$",
            r"$1.00 \times 10^{18}\text{ cm}^{-3}$",
            r"$5.00 \times 10^{12}\text{ cm}^{-3}$",
            "(a)",
            r"$p = \frac{1}{R_H q} = \frac{1}{(0.035\text{ m}^3/\text{C})(1.602 \times 10^{-19}\text{ C})} \approx 1.783 \times 10^{20}\text{ m}^{-3} = 1.78 \times 10^{14}\text{ cm}^{-3}$."
        )
    ]
    
    theory_qs = [
        (
            r"Explain the Classical Drude Free Electron Theory of Metals. Derive the expression for electrical conductivity $\sigma = \frac{n e^2 \tau}{m}$. State and derive the Wiedemann-Franz Law, and discuss the physical meaning of the Lorenz Number.",
            r"""\textbf{1. Assumptions of Drude Model}:
\begin{enumerate}
    \item A metal consists of positive lattice ion cores and a gas of free valence electrons of number density $n$.
    \item In the absence of an electric field, electrons move randomly with thermal velocity $\vec{v}_{\text{th}}$ ($\langle \vec{v}_{\text{th}} \rangle = 0$).
    \item Under an applied electric field $\vec{E}$, electrons experience an electrostatic force $\vec{F} = -e\vec{E}$ and accelerate between collisions.
    \item Collisions with lattice ions are instantaneous, resetting drift velocity to zero after average relaxation time $\tau$.
\end{enumerate}

\textbf{2. Derivation of Electrical Conductivity $\sigma$}:
The equation of motion of an electron under electric field $\vec{E}$ is:
\begin{equation}
m \frac{d\vec{v}_d}{dt} + \frac{m}{\tau}\vec{v}_d = -e\vec{E}
\end{equation}
In steady state ($\frac{d\vec{v}_d}{dt} = 0$):
\begin{equation}
\vec{v}_d = -\frac{e\tau}{m}\vec{E} = -\mu_n \vec{E}
\end{equation}
The resulting drift current density $\vec{J}$ is:
\begin{equation}
\vec{J} = -n e \vec{v}_d = -n e \left( -\frac{e\tau}{m}\vec{E} \right) = \left( \frac{n e^2 \tau}{m} \right)\vec{E}
\end{equation}
Comparing with Ohm's law $\vec{J} = \sigma \vec{E}$:
\begin{equation}
\mathbf{\sigma = \frac{n e^2 \tau}{m}}
\end{equation}

\textbf{3. Thermal Conductivity $K$ & Wiedemann-Franz Law}:
From classical kinetic theory of gases, thermal conductivity carried by electron gas is:
\begin{equation}
K = \frac{1}{3} C_v v_{\text{th}} \lambda_{\text{mfp}} = \frac{1}{3}\left(\frac{3}{2}n k_B\right) v_{\text{th}} (v_{\text{th}}\tau) = \frac{1}{2} n k_B \tau v_{\text{th}}^2
\end{equation}
Using equipartition theorem $\frac{1}{2}m v_{\text{th}}^2 = \frac{3}{2}k_BT \implies v_{\text{th}}^2 = \frac{3k_BT}{m}$:
\begin{equation}
K = \frac{3}{2}\frac{n k_B^2 T \tau}{m}
\end{equation}
Taking the ratio of thermal to electrical conductivity:
\begin{equation}
\mathbf{\frac{K}{\sigma} = \frac{\frac{3}{2}\frac{n k_B^2 T \tau}{m}}{\frac{n e^2 \tau}{m}} = \frac{3}{2}\left(\frac{k_B}{e}\right)^2 T = L_{\text{classical}} T}
\end{equation}
In quantum Sommerfeld theory (using Fermi-Dirac statistics):
\begin{equation}
\mathbf{\frac{K}{\sigma} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 T = L T}
\end{equation}
where $L = \frac{\pi^2 k_B^2}{3e^2} \approx \mathbf{2.44 \times 10^{-8}\text{ W}\cdot\Omega/\text{K}^2}$ is the universal \textbf{Lorenz Number}."""
        ),
        (
            r"Explain the physical origin of energy bands in solids using the Kronig-Penney Model. State Bloch's theorem and derive how periodic boundary conditions lead to allowed energy bands and forbidden gaps.",
            r"""\textbf{1. Bloch's Theorem}:
For an electron moving in a 1D periodic crystalline lattice potential $V(x + a) = V(x)$ of lattice constant $a$, the Schrödinger wavefunctions are modulated plane waves:
\begin{equation}
\mathbf{\psi_k(x) = e^{i k x} u_k(x)}
\end{equation}
where $u_k(x + a) = u_k(x)$ is a periodic function with the periodicity of the lattice, and $k$ is the crystal wavevector.

\textbf{2. Kronig-Penney Potential Model}:
The periodic crystal potential is modeled as an array of rectangular barrier wells:
\begin{equation}
V(x) = \begin{cases} 0 & 0 < x < a \quad (\text{well}) \\ V_0 & -b < x < 0 \quad (\text{barrier}) \end{cases}
\end{equation}
Period is $d = a + b$.

\textbf{3. Dispersion Relation}:
Applying boundary conditions on $\psi$ and $\frac{d\psi}{dx}$ at boundaries, and taking the Dirac delta-function limit ($V_0 \to \infty, b \to 0$ such that $V_0 b = \text{finite}$), yields the fundamental \textbf{Kronig-Penney Relation}:
\begin{equation}
\mathbf{P \frac{\sin(\alpha a)}{\alpha a} + \cos(\alpha a) = \cos(k a)}
\end{equation}
where $\alpha = \frac{\sqrt{2mE}}{\hbar}$ and $P = \frac{m V_0 b a}{\hbar^2}$ is the dimensionless barrier strength.

\textbf{4. Formation of Allowed Bands & Forbidden Gaps}:
Because the right side $\cos(ka)$ is bounded strictly between $-1$ and $+1$:
\begin{equation}
\mathbf{-1 \le P \frac{\sin(\alpha a)}{\alpha a} + \cos(\alpha a) \le +1}
\end{equation}
\begin{itemize}
    \item \textbf{Allowed Energy Bands}: Values of energy $E = \frac{\hbar^2\alpha^2}{2m}$ where the function lies inside $[-1, +1]$. In these ranges, real solutions for $k$ exist.
    \item \textbf{Forbidden Energy Gaps ($E_g$)}: Values of energy where the magnitude of the function exceeds $1.0$ ($|f(\alpha a)| > 1$). No real wavevector $k$ exists, creating forbidden energy gaps where electron transmission is impossible.
\end{itemize}"""
        ),
        (
            r"Derive the expressions for electron concentration $n$ and hole concentration $p$ in an intrinsic semiconductor. Obtain the Law of Mass Action $n \cdot p = n_i^2$ and derive the position of the intrinsic Fermi level $E_{Fi}$.",
            r"""\textbf{1. Electron Concentration in Conduction Band $n$}:
The electron density is obtained by integrating the density of states $g_c(E)$ multiplied by the Fermi-Dirac probability $f(E)$ from $E_c$ to $\infty$:
\begin{equation}
n = \int_{E_c}^\infty g_c(E) f(E) dE = \frac{1}{2\pi^2}\left(\frac{2m_e^*}{\hbar^2}\right)^{3/2} \int_{E_c}^\infty \frac{\sqrt{E - E_c}}{1 + e^{(E - E_F)/k_BT}} dE
\end{equation}
In non-degenerate semiconductors ($E_c - E_F \ge 3k_BT$), using the Maxwell-Boltzmann tail $f(E) \approx e^{-(E - E_F)/k_BT}$:
\begin{equation}
\mathbf{n = N_c e^{-(E_c - E_F)/k_BT}}
\end{equation}
where $N_c = 2\left(\frac{2\pi m_e^* k_BT}{h^2}\right)^{3/2}$ is the effective density of states in the conduction band.

\textbf{2. Hole Concentration in Valence Band $p$}:
Integrating vacant states $[1 - f(E)]$ in the valence band:
\begin{equation}
\mathbf{p = N_v e^{-(E_F - E_v)/k_BT}}
\end{equation}
where $N_v = 2\left(\frac{2\pi m_h^* k_BT}{h^2}\right)^{3/2}$ is the effective density of states in the valence band.

\textbf{3. Law of Mass Action}:
Multiplying $n$ and $p$:
\begin{align*}
n \cdot p &= \left(N_c e^{-(E_c - E_F)/k_BT}\right)\left(N_v e^{-(E_F - E_v)/k_BT}\right) = N_c N_v e^{-(E_c - E_v)/k_BT} \\
\mathbf{n \cdot p} &= \mathbf{N_c N_v e^{-E_g / k_BT} = n_i^2}
\end{align*}
where intrinsic carrier concentration is $\mathbf{n_i = \sqrt{N_c N_v} e^{-E_g / (2k_BT)}}$.

\textbf{4. Intrinsic Fermi Level $E_{Fi}$}:
In an intrinsic semiconductor, $n = p = n_i$:
\begin{align*}
N_c e^{-(E_c - E_{Fi})/k_BT} &= N_v e^{-(E_{Fi} - E_v)/k_BT} \\
e^{2E_{Fi}/k_BT} &= \frac{N_v}{N_c} e^{(E_c + E_v)/k_BT} = \left(\frac{m_h^*}{m_e^*}\right)^{3/2} e^{(E_c + E_v)/k_BT}
\end{align*}
Taking natural logarithms:
\begin{equation}
\frac{2E_{Fi}}{k_BT} = \frac{E_c + E_v}{k_BT} + \frac{3}{2}\ln\left(\frac{m_h^*}{m_e^*}\right) \implies \mathbf{E_{Fi} = \frac{E_c + E_v}{2} + \frac{3}{4}k_BT \ln\left(\frac{m_h^*}{m_e^*}\right)}
\end{equation}"""
        ),
        (
            r"Derive the complete mathematical expressions for the Hall Voltage $V_H$, Hall Electric Field $E_H$, Hall Coefficient $R_H$, and Hall Mobility $\mu_H$. Explain four vital practical engineering applications of the Hall Effect.",
            r"""\textbf{1. Physical Setup & Force Balance}:
Consider a rectangular semiconductor slab of width $w$ (along $y$), thickness $d$ (along $z$), and length $L$ (along $x$).
A direct current $I_x$ is passed along the $+x$ direction, and a uniform magnetic field $B_z$ is applied along the $+z$ direction.
\begin{enumerate}
    \item Charge carriers moving with drift velocity $\vec{v}_d = v_x \hat{i}$ experience magnetic Lorentz force:
    \begin{equation}
    \vec{F}_m = q (\vec{v}_d \times \vec{B}) = q (v_x \hat{i} \times B_z \hat{k}) = -q v_x B_z \hat{j}
    \end{equation}
    \item Deflected carriers accumulate on side faces, setting up a transverse electrostatic Hall electric field $\vec{E}_H = E_y \hat{j}$.
    \item In steady state, electrostatic force balances magnetic Lorentz force ($F_e + F_m = 0$):
    \begin{equation}
    q E_H = q v_x B_z \implies \mathbf{E_H = v_x B_z}
    \end{equation}
\end{enumerate}

\textbf{2. Derivation of Hall Coefficient $R_H$ & Hall Voltage $V_H$}:
Current density is $J_x = n q v_x \implies v_x = \frac{J_x}{n q}$.
Substituting $v_x$ into the electric field balance:
\begin{equation}
E_H = \left(\frac{J_x}{n q}\right) B_z = \left(\frac{1}{n q}\right) J_x B_z
\end{equation}
Defining the \textbf{Hall Coefficient $R_H$}:
\begin{equation}
\mathbf{R_H = \frac{E_H}{J_x B_z} = \frac{1}{n q}} \implies \begin{cases} R_H = -\frac{1}{n e} & (\text{n-type}) \\ R_H = +\frac{1}{p e} & (\text{p-type}) \end{cases}
\end{equation}
The induced transverse Hall Voltage $V_H$ across slab width $w$ is:
\begin{equation}
\mathbf{V_H = E_H \cdot w = R_H J_x B_z w = R_H \left(\frac{I_x}{w \cdot d}\right) B_z w = \frac{R_H I_x B_z}{d}}
\end{equation}
where $d$ is slab thickness along the magnetic field.

\textbf{3. Hall Mobility $\mu_H$}:
Using conductivity $\sigma = n q \mu$:
\begin{equation}
\mathbf{\mu_H = |R_H| \sigma = \left(\frac{1}{n q}\right)(n q \mu) = \mu}
\end{equation}

\textbf{4. Four Key Engineering Applications}:
\begin{enumerate}
    \item \textbf{Determination of Semiconductor Type}: Sign of $V_H$ ($R_H > 0 \implies \text{p-type}$; $R_H < 0 \implies \text{n-type}$).
    \item \textbf{Measurement of Carrier Density}: $n = 1/(|R_H|e)$.
    \item \textbf{Measurement of Carrier Mobility}: $\mu = |R_H|\sigma$.
    \item \textbf{Magnetic Field Sensors & Brushless DC Motor Commutators}: Linear Hall probes accurately measure magnetic flux densities from $\mu\text{T}$ to $> 10\text{ T}$."""
        ),
        (
            r"Derive the step-by-step expression for the built-in potential barrier $V_{bi}$ and depletion layer width $W$ across an abrupt p-n junction from Poisson's equation.",
            r"""\textbf{1. Poisson's Equation Formulation}:
Consider an abrupt p-n junction with acceptor doping $N_A$ on p-side ($-x_p \le x \le 0$) and donor doping $N_D$ on n-side ($0 \le x \le x_n$).
\begin{equation}
\frac{d^2 V}{dx^2} = -\frac{\rho(x)}{\epsilon_s} = \begin{cases} +\frac{q N_A}{\epsilon_s} & -x_p \le x \le 0 \\ -\frac{q N_D}{\epsilon_s} & 0 \le x \le x_n \end{cases}
\end{equation}

\textbf{2. Integrating for Electric Field $E(x) = -\frac{dV}{dx}$}:
Applying boundary conditions $E(-x_p) = 0$ and $E(x_n) = 0$:
\begin{equation}
E(x) = \begin{cases} -\frac{q N_A}{\epsilon_s}(x + x_p) & -x_p \le x \le 0 \\ -\frac{q N_D}{\epsilon_s}(x_n - x) & 0 \le x \le x_n \end{cases}
\end{equation}
Equating peak field at metallurgical junction $x=0$:
\begin{equation}
E(0) = -\frac{q N_A x_p}{\epsilon_s} = -\frac{q N_D x_n}{\epsilon_s} \implies \mathbf{N_A x_p = N_D x_n} \quad (\text{Charge Neutrality})
\end{equation}

\textbf{3. Integrating for Built-in Potential $V_{bi}$}:
Total potential drop across the depletion region equals the area under the triangular $E(x)$ field profile:
\begin{equation}
V_{bi} = -\int_{-x_p}^{x_n} E(x) dx = \frac{1}{2}|E_{\text{max}}| W = \frac{1}{2}\left(\frac{q N_D x_n}{\epsilon_s}\right)(x_p + x_n)
\end{equation}
Expressing in terms of carrier concentrations:
\begin{equation}
\mathbf{V_{bi} = \frac{k_BT}{q}\ln\left(\frac{N_A N_D}{n_i^2}\right)}
\end{equation}

\textbf{4. Total Depletion Width $W = x_p + x_n$}:
Using $x_p = W \frac{N_D}{N_A + N_D}$ and $x_n = W \frac{N_A}{N_A + N_D}$:
\begin{equation}
V_{bi} = \frac{q}{2\epsilon_s}\frac{N_A N_D}{N_A + N_D} W^2
\end{equation}
Under applied bias $V_a$ (forward $V_a > 0$, reverse $V_a = -V_R$):
\begin{equation}
\mathbf{W = \sqrt{\frac{2\epsilon_s}{q}\left(\frac{N_A + N_D}{N_A N_D}\right)(V_{bi} - V_a)} = \sqrt{\frac{2\epsilon_s}{q}\left(\frac{1}{N_A} + \frac{1}{N_D}\right)(V_{bi} - V_a)}}
\end{equation}"""
        ),
        (
            r"Describe the construction, working principle, energy band diagram, and $I$-$V$ characteristics of a Solar Cell. Define Open-Circuit Voltage ($V_{oc}$), Short-Circuit Current ($I_{sc}$), Fill Factor ($FF$), and Conversion Efficiency ($\eta$).",
            r"""\textbf{1. Construction}:
A solar cell is a large-area semiconductor p-n junction diode.
\begin{itemize}
    \item \textbf{Substrate}: Thick p-type Silicon wafer ($\sim 200\text{--}300\,\mu\text{m}$).
    \item \textbf{Emitter Layer}: Ultra-thin heavily doped n-type surface layer ($\sim 0.2\text{--}0.5\,\mu\text{m}$) to allow sunlight penetration.
    \item \textbf{Anti-Reflective Coating}: Thin film of $\text{Si}_3\text{N}_4$ ($n \approx 1.9$) to minimize surface reflection.
    \item \textbf{Contacts}: Metallic grid fingers on front surface (minimizing shading) and continuous solid metal contact on back.
\end{itemize}

\textbf{2. Working Principle}:
\begin{enumerate}
    \item \textbf{Photogeneration}: Sunlight with photon energy $h\nu \ge E_g$ penetrates the junction, exciting valence electrons into the conduction band and generating electron-hole pairs (EHPs).
    \item \textbf{Carrier Separation}: The strong built-in electric field in the space-charge region sweeps photo-generated electrons to the n-side and holes to the p-side before recombination can occur.
    \item \textbf{Power Delivery}: Carrier accumulation establishes an open-circuit photovoltage $V_{oc}$; connecting an external load resistor $R_L$ drives a continuous DC photocurrent.
\end{enumerate}

\textbf{3. Characteristic Parameters}:
\begin{enumerate}
    \item \textbf{Short-Circuit Current ($I_{sc}$)}: The maximum current when terminals are shorted ($V=0$):
    \begin{equation}
    I_{sc} \approx I_L = q A G (L_n + L_p + W) \propto P_{\text{incident}}
    \end{equation}
    \item \textbf{Open-Circuit Voltage ($V_{oc}$)}: The maximum voltage developed across open terminals ($I=0$):
    \begin{equation}
    \mathbf{V_{oc} = \frac{k_B T}{q}\ln\left(\frac{I_{sc}}{I_0} + 1\right)}
    \end{equation}
    \item \textbf{Fill Factor ($FF$)}: Ratio of maximum power rectangle to the product $V_{oc} I_{sc}$:
    \begin{equation}
    \mathbf{FF = \frac{P_{\text{max}}}{V_{oc} I_{sc}} = \frac{V_m I_m}{V_{oc} I_{sc}}}
    \end{equation}
    \item \textbf{Power Conversion Efficiency ($\eta$)}:
    \begin{equation}
    \mathbf{\eta = \frac{P_{\text{max}}}{P_{\text{in}}} = \frac{V_{oc} I_{sc} FF}{P_{\text{in}}} \times 100\%}
    \end{equation}
\end{enumerate}"""
        ),
        (
            r"Explain carrier transport in semiconductors under combined drift and diffusion. Derive the total electron and hole current density equations. State the continuity equation for excess minority carriers.",
            r"""\textbf{1. Drift Current}:
Drift current is driven by an applied electric field $\vec{E}$:
\begin{align}
\vec{J}_{n,\text{drift}} &= q n \mu_n \vec{E} \\
\vec{J}_{p,\text{drift}} &= q p \mu_p \vec{E}
\end{align}

\textbf{2. Diffusion Current}:
Diffusion current is driven by spatial carrier concentration gradients according to Fick's first law:
\begin{align}
\vec{J}_{n,\text{diff}} &= +q D_n \nabla n \\
\vec{J}_{p,\text{diff}} &= -q D_p \nabla p
\end{align}
where $D_n, D_p$ are electron and hole diffusion coefficients.

\textbf{3. Total Current Densities}:
Summing drift and diffusion components:
\begin{align}
\mathbf{\vec{J}_n = q n \mu_n \vec{E} + q D_n \nabla n} \\
\mathbf{\vec{J}_p = q p \mu_p \vec{E} - q D_p \nabla p}
\end{align}
Total conduction current density is $\vec{J}_{\text{total}} = \vec{J}_n + \vec{J}_p$.

\textbf{4. Continuity Equation for Excess Carriers}:
Applying conservation of charge to differential volume $A dx$:
\begin{align}
\mathbf{\frac{\partial (\Delta n)}{\partial t} = D_n \frac{\partial^2 (\Delta n)}{\partial x^2} + \mu_n E \frac{\partial (\Delta n)}{\partial x} + G_n - \frac{\Delta n}{\tau_n}} \\
\mathbf{\frac{\partial (\Delta p)}{\partial t} = D_p \frac{\partial^2 (\Delta p)}{\partial x^2} - \mu_p E \frac{\partial (\Delta p)}{\partial x} + G_p - \frac{\Delta p}{\tau_p}}
\end{align}
where $G$ is external generation rate and $\tau$ is minority carrier recombination lifetime."""
        ),
        (
            r"Discuss the temperature dependence of carrier concentration in an extrinsic n-type semiconductor. Explain the three distinct operational regimes: (a) Freeze-out regime, (b) Extrinsic saturation regime, and (c) Intrinsic transition regime.",
            r"""\textbf{1. Temperature Variation of Electron Concentration $n(T)$}:
A graph of $\ln(n)$ versus $1/T$ exhibits three distinct physical regimes:

\begin{enumerate}
    \item \textbf{Low-Temperature Freeze-Out Regime ($T < 100\text{ K}$)}:
    Thermal energy is lower than the donor ionization energy ($k_BT \ll E_c - E_d \approx 0.045\text{ eV}$).
    Electrons lack sufficient thermal energy to jump into the conduction band and freeze back into localized donor states.
    \begin{equation}
    n(T) \approx \sqrt{\frac{N_c N_D}{2}} \exp\left(-\frac{E_c - E_d}{2 k_B T}\right) \propto e^{-\Delta E_d / 2k_BT}
    \end{equation}
    Carrier concentration increases exponentially with rising temperature.

    \item \textbf{Moderate-Temperature Extrinsic (Saturation/Exhaustion) Regime ($100\text{ K} \le T \le 450\text{ K}$)}:
    Thermal energy ($k_BT \ge 26\text{ meV}$) is sufficient to ionize $100\%$ of all donor impurity atoms ($N_D^+ \approx N_D$), while intrinsic band-to-band thermal generation across the large bandgap ($E_g = 1.12\text{ eV}$) is still negligible ($n_i \ll N_D$).
    \begin{equation}
    \mathbf{n \approx N_D = \text{constant}}
    \end{equation}
    This is the stable operating regime for all standard silicon electronic devices.

    \item \textbf{High-Temperature Intrinsic Regime ($T > 500\text{ K}$)}:
    Thermal generation of electron-hole pairs across the main forbidden gap increases exponentially ($n_i(T) \propto T^{3/2}e^{-E_g/2k_BT}$) and quickly overwhelms the fixed dopant concentration ($n_i(T) \gg N_D$).
    \begin{equation}
    \mathbf{n \approx n_i(T) \propto e^{-E_g / 2k_BT}}
    \end{equation}
    The semiconductor loses its extrinsic properties and behaves as an intrinsic material, setting the upper thermal operating limit of silicon chips.
\end{enumerate}"""
        ),
        (
            r"Explain the Direct vs Indirect bandgap semiconductor concepts using $E$-$k$ energy-momentum diagrams. Discuss the optoelectronic selection rules and why indirect semiconductors cannot be used for efficient lasers or LEDs.",
            r"""\textbf{1. $E$-$k$ Diagram & Bandgap Classification}:
In solid-state physics, the energy states of electrons are plotted as parabolic bands $E(k)$ versus crystal momentum wavevector $k = p/\hbar$.
\begin{itemize}
    \item \textbf{Direct Bandgap Semiconductor (e.g., GaAs, InP, GaN)}:
    The conduction band minimum ($E_c$) and valence band maximum ($E_v$) align at the exact same wavevector coordinate ($k = 0$, $\Gamma$-point).
    \item \textbf{Indirect Bandgap Semiconductor (e.g., Si, Ge, GaP)}:
    The valence band maximum is at $k = 0$, but the conduction band minimum is located at an off-axis wavevector $k = k_0 \ne 0$ along the $(100)$ crystal direction.
\end{itemize}

\textbf{2. Conservation Laws for Optical Transitions}:
A photon carrying energy $h\nu \approx E_g \sim 1\text{ eV}$ has wavevector $k_{\text{photon}} = \frac{2\pi}{\lambda} \approx 10^7\text{ m}^{-1}$.
By contrast, the Brillouin zone boundary has $k_{\text{crystal}} = \pi/a \approx 10^{10}\text{ m}^{-1}$, which is $1000\times$ larger ($k_{\text{photon}} \approx 0$).

\begin{enumerate}
    \item \textbf{Direct Bandgap Recombination}:
    Because $\Delta k = 0$, an electron at the conduction band bottom recombines vertically with a hole at the valence band top. Momentum is conserved directly by the photon alone:
    \begin{equation}
    \mathbf{e^- + h^+ \to \text{Photon } (h\nu)} \quad (\text{Fast, 1st-order process: } \tau_{\text{rad}} \sim 1\text{ ns})
    \end{equation}
    Quantum radiative efficiency approaches $100\%$.

    \item \textbf{Indirect Bandgap Recombination}:
    Because $\Delta k = k_0 \ne 0$, an electron cannot drop vertically to the valence top without transferring substantial momentum to the crystal lattice.
    Recombination requires simultaneous emission or absorption of a lattice vibration quantum (\textbf{Phonon} $\hbar\Omega$):
    \begin{equation}
    \mathbf{e^- + h^+ \to \text{Photon } (h\nu) \pm \text{Phonon } (\hbar\Omega)} \quad (\text{Slow, 2nd-order 3-body process: } \tau_{\text{rad}} \sim 1\text{ ms})
    \end{equation}
    Because this process is $10^6\times$ slower, excited carriers undergo non-radiative defect recombination, releasing energy as useless heat rather than coherent light.
\end{enumerate}"""
        ),
        (
            r"A Hall effect measurement is performed on an unknown semiconductor slab of length $L = 1.0\text{ cm}$, width $w = 2.0\text{ mm}$, and thickness $d = 0.4\text{ mm}$. A current of $I = 15\text{ mA}$ is passed along the length in a magnetic field $B = 0.8\text{ T}$ applied along the thickness. A Hall voltage $V_H = -6.4\text{ mV}$ is measured across the width, and the voltage drop along the length is $V_L = 1.2\text{ V}$. Determine: (a) carrier type, (b) Hall coefficient $R_H$, (c) majority carrier concentration $n$, (d) electrical resistivity $\rho$ and conductivity $\sigma$, and (e) Hall mobility $\mu_H$.",
            r"""\textbf{1. Carrier Type}:
Because the measured Hall voltage is negative ($V_H = -6.4\text{ mV} < 0$), majority carriers are electrons. The sample is confirmed to be an \textbf{n-type semiconductor}.

\textbf{2. Hall Coefficient $R_H$}:
Thickness $d = 0.4\text{ mm} = 4.0 \times 10^{-4}\text{ m}$.
\begin{equation}
\mathbf{R_H = \frac{V_H d}{I B} = \frac{(-6.4 \times 10^{-3}\text{ V})(4.0 \times 10^{-4}\text{ m})}{(15 \times 10^{-3}\text{ A})(0.8\text{ T})} = \frac{-2.56 \times 10^{-6}}{0.012} = -2.133 \times 10^{-4}\text{ m}^3/\text{C}}
\end{equation}

\textbf{3. Carrier Concentration $n$}:
\begin{equation}
\mathbf{n = \frac{1}{|R_H| e} = \frac{1}{(2.133 \times 10^{-4}\text{ m}^3/\text{C})(1.602 \times 10^{-19}\text{ C})} \approx 2.926 \times 10^{22}\text{ m}^{-3} = 2.93 \times 10^{16}\text{ cm}^{-3}}
\end{equation}

\textbf{4. Electrical Resistivity $\rho$ & Conductivity $\sigma$}:
Cross-sectional area $A = w \times d = (2 \times 10^{-3}\text{ m})(4 \times 10^{-4}\text{ m}) = 8 \times 10^{-7}\text{ m}^2$.
Sample resistance $R = V_L / I = 1.2\text{ V} / (15 \times 10^{-3}\text{ A}) = 80\,\Omega$.
\begin{align*}
\mathbf{\rho} &= \frac{R A}{L} = \frac{(80\,\Omega)(8 \times 10^{-7}\text{ m}^2)}{1.0 \times 10^{-2}\text{ m}} = \mathbf{6.4 \times 10^{-3}\,\Omega\cdot\text{m}} \\
\mathbf{\sigma} &= \frac{1}{\rho} = \frac{1}{6.4 \times 10^{-3}} = \mathbf{156.25\text{ S/m}}
\end{align*}

\textbf{5. Hall Mobility $\mu_H$}:
\begin{align*}
\mathbf{\mu_H} &= |R_H| \sigma = (2.133 \times 10^{-4}\text{ m}^3/\text{C})(156.25\text{ S/m}) \\
&= \mathbf{0.0333\text{ m}^2/\text{V}\cdot\text{s} = 333.3\text{ cm}^2/\text{V}\cdot\text{s}}
\end{align*}"""
        )
    ]
    
    return unit_num, unit_title, mcqs, theory_qs
