# generate_physics_qb_u3.py
# -*- coding: utf-8 -*-

def get_unit_3_content():
    unit_num = 3
    unit_title = "Fiber Optics"
    
    mcqs = [
        # Part I: Foundational (1-50)
        (
            r"Light propagation along the core of an optical fiber is governed by the physical principle of:",
            r"Total Internal Reflection (TIR)",
            r"Total Internal Refraction",
            r"Continuous Fraunhofer Diffraction",
            r"Constructive Polarization Scattering",
            "(a)",
            r"Optical fibers guide light within the higher-index core via repeated Total Internal Reflection (TIR) at the core-cladding interface."
        ),
        (
            r"For Total Internal Reflection to occur at the core-cladding boundary, the refractive index of the core $n_1$ and cladding $n_2$ must satisfy:",
            r"$n_1 < n_2$",
            r"$n_1 > n_2$",
            r"$n_1 = n_2$",
            r"$n_2 = 1.0$ always",
            "(b)",
            r"TIR strictly requires light to travel from a denser optical medium to a rarer optical medium ($n_{\text{core}} > n_{\text{cladding}}$)."
        ),
        (
            r"The critical angle of incidence $\phi_c$ at the core-cladding interface is given by:",
            r"$\phi_c = \sin^{-1}\left(\frac{n_2}{n_1}\right)$",
            r"$\phi_c = \cos^{-1}\left(\frac{n_2}{n_1}\right)$",
            r"$\phi_c = \tan^{-1}\left(\frac{n_1}{n_2}\right)$",
            r"$\phi_c = \sin^{-1}\left(\frac{n_1}{n_2}\right)$",
            "(a)",
            r"By Snell's law, when the angle of refraction equals $90^\circ$: $n_1 \sin\phi_c = n_2 \sin 90^\circ \implies \phi_c = \arcsin(n_2/n_1)$."
        ),
        (
            r"The Acceptance Angle $\theta_a$ of an optical fiber is defined as:",
            r"The maximum launch angle at the fiber entrance face for which light rays are totally internally reflected within the core",
            r"The critical angle at the cladding boundary",
            r"The Brewster angle of the front facet",
            r"The angle between core axis and cladding normal",
            "(a)",
            r"The acceptance angle $\theta_a$ defines the half-angle of the input acceptance cone for guided mode propagation."
        ),
        (
            r"The Numerical Aperture ($\text{NA}$) of a step-index optical fiber launched from air ($n_0 = 1$) is defined as:",
            r"$\text{NA} = \sin\theta_a = \sqrt{n_1^2 - n_2^2}$",
            r"$\text{NA} = \cos\theta_a = n_1 - n_2$",
            r"$\text{NA} = \frac{n_1^2 - n_2^2}{n_1}$",
            r"$\text{NA} = \sqrt{n_1 + n_2}$",
            "(a)",
            r"Numerical Aperture represents the light-gathering capacity: $\text{NA} = \sin\theta_a = \sqrt{n_1^2 - n_2^2}$."
        ),
        (
            r"The Fractional Refractive Index Difference $\Delta$ is defined by:",
            r"$\Delta = \frac{n_1 - n_2}{n_1}$",
            r"$\Delta = \frac{n_1 - n_2}{n_2}$",
            r"$\Delta = \frac{n_1 + n_2}{n_1}$",
            r"$\Delta = \frac{n_2}{n_1}$",
            "(a)",
            r"$\Delta = (n_1 - n_2)/n_1$ represents the relative index difference between core and cladding."
        ),
        (
            r"In terms of core index $n_1$ and fractional index difference $\Delta$, the Numerical Aperture is approximated by:",
            r"$\text{NA} \approx n_1 \sqrt{2\Delta}$",
            r"$\text{NA} \approx n_1 \Delta$",
            r"$\text{NA} \approx 2 n_1 \Delta^2$",
            r"$\text{NA} \approx \sqrt{n_1 \Delta}$",
            "(a)",
            r"Using $n_1^2 - n_2^2 = (n_1 - n_2)(n_1 + n_2) \approx (\Delta n_1)(2n_1)$, we obtain $\text{NA} \approx n_1\sqrt{2\Delta}$."
        ),
        (
            r"Rays that pass through the central longitudinal axis of the fiber core are known as:",
            r"Skew rays",
            r"Meridional rays",
            r"Evanescent rays",
            r"Leaky cladding rays",
            "(b)",
            r"Meridional rays remain confined to a single plane passing through the fiber's central symmetry axis."
        ),
        (
            r"Rays that follow helical, non-planar zigzag paths without ever intersecting the fiber axis are called:",
            r"Meridional rays",
            r"Skew rays",
            r"Axial modes",
            r"Fundamental modes",
            "(b)",
            r"Skew rays propagate through continuous helical reflections around the core without crossing the central axis."
        ),
        (
            r"The Normalized Frequency parameter ($V$-number) of a step-index fiber of core radius $a$ at operating wavelength $\lambda$ is:",
            r"$V = \frac{2\pi a}{\lambda}\text{NA} = \frac{2\pi a}{\lambda}\sqrt{n_1^2 - n_2^2}$",
            r"$V = \frac{\pi a}{\lambda}\text{NA}$",
            r"$V = \frac{2\pi}{\lambda a}\sqrt{n_1 - n_2}$",
            r"$V = \frac{a}{\lambda}\text{NA}^2$",
            "(a)",
            r"The $V$-number is the dimensionless normalized frequency parameter: $V = \frac{2\pi a}{\lambda}\text{NA}$."
        ),
        (
            r"For a step-index fiber to operate in single-mode regime ($\text{HE}_{11}$ mode only), the $V$-number must satisfy:",
            r"$V \le 2.405$",
            r"$V \ge 2.405$",
            r"$V = 3.832$",
            r"$V > 10$",
            "(a)",
            r"The first higher-order mode cutoff occurs at the first zero of the Bessel function $J_0(x)$, giving the single-mode condition $V \le 2.405$."
        ),
        (
            r"The cutoff wavelength $\lambda_c$ for single-mode operation in a step-index fiber is given by:",
            r"$\lambda_c = \frac{2\pi a}{2.405}\text{NA}$",
            r"$\lambda_c = \frac{2.405}{2\pi a}\text{NA}$",
            r"$\lambda_c = \frac{2\pi a \text{NA}}{3.832}$",
            r"$\lambda_c = \frac{a \text{NA}}{2.405}$",
            "(a)",
            r"Setting $V = 2.405 \implies \frac{2\pi a}{\lambda_c}\text{NA} = 2.405 \implies \lambda_c = \frac{2\pi a}{2.405}\text{NA}$."
        ),
        (
            r"For single-mode transmission through an optical fiber, the actual operating wavelength $\lambda$ must be:",
            r"$\lambda < \lambda_c$",
            r"$\lambda \ge \lambda_c$",
            r"$\lambda = \lambda_c / 2$",
            r"$\lambda \to 0$",
            "(b)",
            r"Because $V \propto 1/\lambda$, single-mode operation ($V \le 2.405$) requires operating at wavelengths greater than or equal to cutoff ($\lambda \ge \lambda_c$)."
        ),
        (
            r"The total number of guided modes $M_{\text{SI}}$ in a multimode step-index fiber with large $V$-number is approximately:",
            r"$M_{\text{SI}} \approx \frac{V^2}{2}$",
            r"$M_{\text{SI}} \approx V^2$",
            r"$M_{\text{SI}} \approx \frac{V^2}{4}$",
            r"$M_{\text{SI}} \approx 2V$",
            "(a)",
            r"Accounting for two orthogonal polarization states per spatial mode, total guided mode volume is $M_{\text{SI}} \approx V^2/2$."
        ),
        (
            r"The total number of guided modes $M_{\text{GRIN}}$ in a parabolic Graded-Index fiber with the same core radius and NA is:",
            r"$M_{\text{GRIN}} \approx \frac{V^2}{2}$",
            r"$M_{\text{GRIN}} \approx \frac{V^2}{4}$",
            r"$M_{\text{GRIN}} \approx V^2$",
            r"$M_{\text{GRIN}} \approx \frac{V^2}{8}$",
            "(b)",
            r"In a graded-index fiber with parabolic profile ($\alpha=2$), the mode volume is exactly half that of a step-index fiber: $M_{\text{GRIN}} \approx V^2/4$."
        ),
        (
            r"In a Graded-Index (GRIN) optical fiber, the refractive index profile $n(r)$ within the core ($r \le a$) varies as:",
            r"$n(r) = n_1 \sqrt{1 - 2\Delta\left(\frac{r}{a}\right)^2}$",
            r"$n(r) = n_1 \left(1 - \frac{r}{a}\right)$",
            r"$n(r) = n_1 e^{-r/a}$",
            r"$n(r) = \text{constant}$",
            "(a)",
            r"A parabolic index profile decreases smoothly from peak $n_1$ on the axis to $n_2$ at core boundary $r=a$ as $n(r) = n_1\sqrt{1-2\Delta(r/a)^2}$."
        ),
        (
            r"Why do light rays taking longer helical paths in a GRIN fiber arrive at nearly the same time as axial rays?",
            r"They travel through outer regions of lower refractive index where the speed of light $v = c/n(r)$ is faster",
            r"They are accelerated by magnetic fields",
            r"They jump across quantum tunneling paths",
            r"They carry higher photon energy",
            "(a)",
            r"Since velocity $v(r) = c/n(r)$ is higher in lower-index outer regions, longer off-axis paths are compensated by higher transit speeds."
        ),
        (
            r"Optical signal attenuation $\alpha$ in an optical fiber of length $L\text{ km}$ is defined in $\text{dB/km}$ by:",
            r"$\alpha = \frac{10}{L}\log_{10}\left(\frac{P_{\text{in}}}{P_{\text{out}}}\right)$",
            r"$\alpha = \frac{1}{L}\ln\left(\frac{P_{\text{in}}}{P_{\text{out}}}\right)$",
            r"$\alpha = \frac{20}{L}\log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right)$",
            r"$\alpha = 10 \log_{10}(P_{\text{in}} P_{\text{out}})$",
            "(a)",
            r"Standard decibel loss per unit length is defined as $\alpha = \frac{10}{L}\log_{10}(P_{\text{in}}/P_{\text{out}})\text{ dB/km}$."
        ),
        (
            r"Rayleigh scattering attenuation in silica optical fibers is caused by:",
            r"Microscopic, sub-wavelength fluctuations in silica glass density and refractive index frozen into the glass during cooling",
            r"Dust particles inside the core",
            r"Absorption by metallic impurities",
            r"Thermal radiation from the cladding",
            "(a)",
            r"Random microscopic density and compositional fluctuations on a scale smaller than $\lambda$ cause fundamental Rayleigh scattering."
        ),
        (
            r"Rayleigh scattering loss $\alpha_{\text{Rayleigh}}$ varies with operating wavelength $\lambda$ as:",
            r"$\alpha_{\text{Rayleigh}} \propto \frac{1}{\lambda^4}$",
            r"$\alpha_{\text{Rayleigh}} \propto \frac{1}{\lambda^2}$",
            r"$\alpha_{\text{Rayleigh}} \propto \lambda^4$",
            r"$\alpha_{\text{Rayleigh}} \propto \frac{1}{\lambda}$",
            "(a)",
            r"By Rayleigh's scattering law, scattering cross-section is strictly inversely proportional to the fourth power of wavelength ($1/\lambda^4$)."
        ),
        (
            r"The strong extrinsic absorption peak near $\lambda = 1383\text{ nm}$ ($1.38\,\mu\text{m}$) in standard silica fibers is caused by:",
            r"Fundamental vibrations of Silicon-Oxygen bonds",
            r"Overtone vibrational resonances of hydroxyl ($\text{OH}^-$) water impurity ions",
            r"Iron ($\text{Fe}^{3+}$) metallic impurities",
            r"Nitrogen contamination",
            "(b)",
            r"The fundamental $\text{OH}^-$ stretch at $2.73\,\mu\text{m}$ creates a strong second overtone harmonic absorption peak at $1.383\,\mu\text{m}$."
        ),
        (
            r"The three standard optical telecommunication windows centered at $850\text{ nm}$, $1310\text{ nm}$, and $1550\text{ nm}$ correspond to regions of:",
            r"Maximum dispersion",
            r"Minimal combined optical attenuation and favorable dispersion characteristics",
            r"Maximum reflection loss",
            r"Total optical opacity",
            "(b)",
            r"These spectral windows exploit valleys in the silica attenuation curve: $850\text{ nm}$ (GaAs source), $1310\text{ nm}$ (zero dispersion), $1550\text{ nm}$ (lowest loss)."
        ),
        (
            r"The lowest optical attenuation in pure silica glass optical fibers occurs in the third window ($\lambda \approx 1550\text{ nm}$) with a loss of approximately:",
            r"$20\text{ dB/km}$",
            r"$2.0\text{ dB/km}$",
            r"$0.2\text{ dB/km}$",
            r"$0.002\text{ dB/km}$",
            "(c)",
            r"Modern ultra-pure silica single-mode fibers achieve an absolute minimum attenuation of $\approx 0.18\text{--}0.20\text{ dB/km}$ at $1550\text{ nm}$."
        ),
        (
            r"Intermodal (modal) dispersion occurs exclusively in:",
            r"Single-mode fibers",
            r"Multimode fibers",
            r"Planar waveguides with $V < 1$",
            r"Free space beams",
            "(b)",
            r"Intermodal dispersion results from different spatial modes traveling along different path lengths with different transit times in multimode fibers."
        ),
        (
            r"The intermodal pulse broadening $\Delta \tau_{\text{modal}}$ over a step-index fiber of length $L$ is given by:",
            r"$\Delta \tau_{\text{modal}} \approx \frac{L n_1 \Delta}{c}$",
            r"$\Delta \tau_{\text{modal}} \approx \frac{L n_1 \Delta^2}{c}$",
            r"$\Delta \tau_{\text{modal}} \approx \frac{L c \Delta}{n_1}$",
            r"$\Delta \tau_{\text{modal}} \approx \frac{L}{c n_1 \Delta}$",
            "(a)",
            r"$\Delta\tau = t_{\text{slowest}} - t_{\text{fastest}} = \frac{L n_1^2}{c n_2} - \frac{L n_1}{c} \approx \frac{L n_1 \Delta}{c}$."
        ),
        (
            r"Why is intermodal dispersion completely absent in Single-Mode Fibers (SMF)?",
            r"Because only one single fundamental spatial mode ($\text{HE}_{11}$) can propagate, eliminating mode transit time differences",
            r"Because single-mode fibers have zero core index",
            r"Because light travels as a sound wave",
            r"Because the cladding absorbs all light",
            "(a)",
            r"In single-mode fibers, light propagates strictly as a solitary spatial mode, completely eliminating intermodal time delays."
        ),
        (
            r"Intramodal (chromatic) dispersion in single-mode fibers is the combined sum of:",
            r"Material dispersion ($D_M$) and Waveguide dispersion ($D_W$)",
            r"Intermodal dispersion and Polarization dispersion",
            r"Rayleigh scattering and Bending loss",
            r"Absorption loss and Splice loss",
            "(a)",
            r"Total chromatic dispersion is $D_{\text{chromatic}} = D_M + D_W$, where $D_M$ arises from wavelength-dependent refractive index $n(\lambda)$ and $D_W$ from waveguide geometry."
        ),
        (
            r"In standard single-mode silica fibers (ITU-T G.652), the zero-material-dispersion wavelength $\lambda_0$ naturally occurs near:",
            r"$850\text{ nm}$",
            r"$1310\text{ nm}$",
            r"$1550\text{ nm}$",
            r"$2000\text{ nm}$",
            "(b)",
            r"In pure fused silica, material dispersion $D_M$ crosses zero at $\approx 1270\text{ nm}$, yielding net chromatic dispersion zero at $\approx 1310\text{ nm}$."
        ),
        (
            r"In Dispersion-Shifted Fibers (DSF, ITU-T G.653), the zero-dispersion wavelength is shifted from $1310\text{ nm}$ to $1550\text{ nm}$ by:",
            r"Modifying the core refractive index profile to increase negative waveguide dispersion $D_W$",
            r"Increasing the fiber diameter to $1\text{ mm}$",
            r"Doping the fiber with copper",
            r"Operating at absolute zero",
            "(a)",
            r"Designing a triangular or segmented index core tailors waveguide dispersion $D_W$ to cancel material dispersion $D_M$ directly at $1550\text{ nm}$."
        ),
        (
            r"Macrobending loss in an optical fiber occurs when:",
            r"The fiber is bent into a curve with a radius comparable to or smaller than a critical bend radius $R_c$",
            r"The fiber is stretched longitudinally",
            r"The temperature rises by $1^\circ\text{C}$",
            r"Light frequency decreases by $1\text{ Hz}$",
            "(a)",
            r"When bend radius $R \le R_c$, the angle of incidence at the outer cladding boundary drops below the critical angle, causing light to radiate into the cladding."
        ),
        (
            r"Microbending losses are caused by:",
            r"Microscopic microscopic axis imperfections, localized pressure, and microscopic crinkles along the fiber core interface",
            r"Large loops of fiber coils",
            r"Total internal reflection",
            r"Photodiode dark current",
            "(a)",
            r"Random microscopic lateral displacements ($< 1\,\mu\text{m}$) couple energy from guided core modes into lossy radiation cladding modes."
        ),
        (
            r"The maximum bit-rate capacity $B$ of an optical communication link limited by pulse broadening $\Delta \tau$ is approximately:",
            r"$B \approx \frac{1}{2\Delta\tau}$ (or $\frac{1}{4\sigma_\tau}$)",
            r"$B \approx 2\Delta\tau$",
            r"$B \approx \Delta\tau^2$",
            r"$B \approx \frac{c}{\Delta\tau}$",
            "(a)",
            r"To avoid inter-symbol interference (ISI) between adjacent pulses, bit period $T_b \ge 2\Delta\tau \implies B = 1/T_b \le 1/(2\Delta\tau)$."
        ),
        (
            r"An Erbium-Doped Fiber Amplifier (EDFA) provides direct optical amplification without electronic conversion in which telecommunication band?",
            r"O-band ($1260\text{--}1360\text{ nm}$)",
            r"C-band ($1530\text{--}1565\text{ nm}$) and L-band ($1565\text{--}1625\text{ nm}$)",
            r"Visible spectrum ($400\text{--}700\text{ nm}$)",
            r"Microwave spectrum ($1\text{--}10\text{ GHz}$)",
            "(b)",
            r"The $^4I_{13/2} \to ^4I_{15/2}$ transition in $\text{Er}^{3+}$ ions provides wide optical gain directly overlapping the $1550\text{ nm}$ low-loss window."
        ),
        (
            r"Which optical source is preferred for long-haul, ultra-high-speed ($> 10\text{ Gbps}$) fiber optic communication systems?",
            r"Surface-emitting LED",
            r"Distributed Feedback (DFB) Semiconductor Laser Diode",
            r"Tungsten halogen bulb",
            r"Neon indicator lamp",
            "(b)",
            r"DFB laser diodes provide single-longitudinal-mode emission with extremely narrow linewidth ($\Delta\lambda < 0.1\text{ nm}$), minimizing chromatic dispersion."
        ),
        (
            r"An Avalanche Photodiode (APD) offers higher sensitivity than a PIN photodiode because:",
            r"It has zero dark current",
            r"It exhibits internal current multiplication gain through impact ionization",
            r"It generates photons rather than electrons",
            r"It requires no bias voltage",
            "(b)",
            r"High reverse bias accelerates photo-generated carriers to create secondary electron-hole pairs via impact ionization, providing internal gain ($M \sim 10\text{--}100$)."
        ),
        (
            r"In fiber optics, fusion splicing involves:",
            r"Joining two cleaved fiber ends using an electric arc to melt and fuse the glass permanently",
            r"Gluing fibers with epoxy resin",
            r"Twisting the glass cores together",
            r"Taping fibers with electrical tape",
            "(a)",
            r"Fusion splicers align fiber cores with sub-micron precision and fuse them using an electric arc, achieving insertion loss $< 0.02\text{ dB}$."
        ),
        (
            r"Fiber Bragg Grating (FBG) sensors operate on the principle of reflecting a specific narrow wavelength $\lambda_B$ given by:",
            r"$\lambda_B = 2 n_{\text{eff}} \Lambda$",
            r"$\lambda_B = \frac{n_{\text{eff}}}{2\Lambda}$",
            r"$\lambda_B = n_{\text{eff}} \Lambda^2$",
            r"$\lambda_B = \frac{2\Lambda}{n_{\text{eff}}}$",
            "(a)",
            r"The Bragg resonance condition reflects wavelength $\lambda_B = 2 n_{\text{eff}} \Lambda$, where $\Lambda$ is grating period and $n_{\text{eff}}$ is effective index."
        ),
        (
            r"When an FBG sensor is subjected to mechanical strain $\epsilon$ or temperature change $\Delta T$, its reflected Bragg wavelength $\lambda_B$:",
            r"Shifts linearly ($\Delta\lambda_B / \lambda_B = P_e \epsilon + \alpha_T \Delta T$)",
            r"Remains completely unchanged",
            r"Disappears completely",
            r"Doubles in amplitude with zero wavelength shift",
            "(a)",
            r"Mechanical elongation changes period $\Lambda$ and photoelastic index; temperature changes index via thermo-optic effect, shifting $\lambda_B$."
        ),
        (
            r"A typical Single-Mode Fiber (SMF-28) has a core diameter and cladding diameter of:",
            r"$9\,\mu\text{m}$ core and $125\,\mu\text{m}$ cladding",
            r"$50\,\mu\text{m}$ core and $125\,\mu\text{m}$ cladding",
            r"$62.5\,\mu\text{m}$ core and $125\,\mu\text{m}$ cladding",
            r"$200\,\mu\text{m}$ core and $500\,\mu\text{m}$ cladding",
            "(a)",
            r"Standard telecom single-mode fiber (G.652) features a nominal core diameter of $8.2\text{--}9.0\,\mu\text{m}$ and cladding diameter of $125\,\mu\text{m}$."
        ),
        (
            r"A step-index fiber has core index $n_1 = 1.50$ and cladding index $n_2 = 1.45$. The critical angle $\phi_c$ is:",
            r"$45.0^\circ$",
            r"$60.0^\circ$",
            r"$75.2^\circ$",
            r"$85.0^\circ$",
            "(c)",
            r"$\phi_c = \arcsin(1.45/1.50) = \arcsin(0.9667) \approx 75.16^\circ$."
        ),
        (
            r"For the fiber in Question 40, the Numerical Aperture ($\text{NA}$) in air is:",
            r"$0.150$",
            r"$0.384$",
            r"$0.500$",
            r"$0.707$",
            "(b)",
            r"$\text{NA} = \sqrt{n_1^2 - n_2^2} = \sqrt{(1.50)^2 - (1.45)^2} = \sqrt{2.25 - 2.1025} = \sqrt{0.1475} \approx 0.384$."
        ),
        (
            r"For the fiber in Question 40, the Acceptance Angle $\theta_a$ in air is:",
            r"$12.5^\circ$",
            r"$22.6^\circ$",
            r"$30.0^\circ$",
            r"$45.0^\circ$",
            "(b)",
            r"$\theta_a = \arcsin(\text{NA}) = \arcsin(0.384) \approx 22.58^\circ$."
        ),
        (
            r"If the fiber in Question 40 is immersed in water ($n_0 = 1.33$), its new acceptance angle $\theta_a'$ becomes:",
            r"$16.8^\circ$",
            r"$22.6^\circ$",
            r"$30.2^\circ$",
            r"$8.4^\circ$",
            "(a)",
            r"$\sin\theta_a' = \frac{\text{NA}}{n_0} = \frac{0.384}{1.33} \approx 0.2887 \implies \theta_a' = \arcsin(0.2887) \approx 16.78^\circ$."
        ),
        (
            r"A $10\text{ km}$ fiber optical link has input power $P_{\text{in}} = 2.0\text{ mW}$ and output power $P_{\text{out}} = 0.2\text{ mW}$. The attenuation coefficient $\alpha$ is:",
            r"$0.1\text{ dB/km}$",
            r"$1.0\text{ dB/km}$",
            r"$2.0\text{ dB/km}$",
            r"$10\text{ dB/km}$",
            "(b)",
            r"$\alpha = \frac{10}{L}\log_{10}\left(\frac{P_{\text{in}}}{P_{\text{out}}}\right) = \frac{10}{10}\log_{10}\left(\frac{2.0}{0.2}\right) = 1.0 \times \log_{10}(10) = 1.0\text{ dB/km}$."
        ),
        (
            r"If an optical signal of power $10\text{ mW}$ is launched into a fiber with attenuation $0.3\text{ dB/km}$, the power remaining after $20\text{ km}$ is:",
            r"$1.0\text{ mW}$",
            r"$2.5\text{ mW}$",
            r"$5.0\text{ mW}$",
            r"$7.5\text{ mW}$",
            "(b)",
            r"Total loss = $0.3\text{ dB/km} \times 20\text{ km} = 6\text{ dB}$. A $6\text{ dB}$ loss corresponds to a factor of $4$ reduction ($10^{-0.6} \approx 0.251$): $P_{\text{out}} = 10 \times 0.251 \approx 2.51\text{ mW}$."
        ),
        (
            r"A step-index fiber has $n_1 = 1.48$ and $\Delta = 1\% = 0.01$. The transit time difference per kilometer ($\Delta\tau/L$) due to intermodal dispersion is approximately:",
            r"$4.93\text{ ns/km}$",
            r"$49.3\text{ ns/km}$",
            r"$493\text{ ns/km}$",
            r"$0.49\text{ ns/km}$",
            "(b)",
            r"$\frac{\Delta\tau}{L} \approx \frac{n_1 \Delta}{c} = \frac{1.48 \times 0.01}{3 \times 10^8\text{ m/s}} = \frac{0.0148}{3 \times 10^8} \approx 4.93 \times 10^{-11}\text{ s/m} = 49.3\text{ ns/km}$."
        ),
        (
            r"For the fiber in Question 46, the maximum bit rate $B$ achievable over a link of $5\text{ km}$ without equalization is:",
            r"$2.03\text{ Mbps}$",
            r"$20.3\text{ Mbps}$",
            r"$203\text{ Mbps}$",
            r"$2.03\text{ Gbps}$",
            "(a)",
            r"Total delay $\Delta\tau = 49.3\text{ ns/km} \times 5\text{ km} = 246.5\text{ ns}$. $B \approx \frac{1}{2\Delta\tau} = \frac{1}{2(246.5 \times 10^{-9}\text{ s})} \approx 2.03 \times 10^6\text{ bps} = 2.03\text{ Mbps}$."
        ),
        (
            r"Why is the bandwidth of a graded-index (GRIN) fiber roughly $100\text{ to }1000\times$ higher than a step-index fiber of identical core size?",
            r"Parabolic grading equalizes the group velocities of different spatial modes",
            r"GRIN fibers absorb all higher-order modes",
            r"GRIN fibers have zero core radius",
            r"Light travels at twice the speed of light in GRIN cores",
            "(a)",
            r"Modal delay spread in parabolic GRIN fibers scales as $\Delta^2$ rather than $\Delta$: $\Delta\tau_{\text{GRIN}} \approx \frac{L n_1 \Delta^2}{2c}$, reducing modal dispersion by up to $1000\times$."
        ),
        (
            r"Optical fibers are completely immune to electromagnetic interference (EMI) and radio frequency interference (RFI) because:",
            r"They are fabricated entirely from dielectric insulator materials (silica glass) that carry light photons rather than electrical currents",
            r"They are shielded with heavy lead jackets",
            r"They operate at high DC voltages",
            r"They are grounded at both ends",
            "(a)",
            r"Silica optical fibers are all-dielectric optical channels, carrying no electrical charges and experiencing zero electromagnetic cross-talk."
        ),
        (
            r"In medical endoscopy, a coherent bundle of optical fibers is used to:",
            r"Transmit clear spatial optical images of internal human organs with high fidelity",
            r"Generate high-voltage X-rays",
            r"Deliver electrical shocks to muscles",
            r"Record brain EEG signals",
            "(a)",
            r"Coherent fiber bundles maintain exact relative fiber spatial alignment at both ends, faithfully transmitting real-time 2D color images from inside body cavities."
        ),

        # Part II: Intermediate Analytical (51-80)
        (
            r"A step-index fiber has a core radius $a = 25\,\mu\text{m}$, $n_1 = 1.48$, and $n_2 = 1.46$. At $\lambda = 850\text{ nm}$, the $V$-number is:",
            r"$11.3$",
            r"$22.4$",
            r"$44.8$",
            r"$89.6$",
            "(b)",
            r"$\text{NA} = \sqrt{1.48^2 - 1.46^2} = \sqrt{2.1904 - 2.1316} = \sqrt{0.0588} \approx 0.2425$. $V = \frac{2\pi (25 \times 10^{-6})}{0.85 \times 10^{-6}}(0.2425) = \frac{157.08}{0.85}(0.2425) \approx 44.8 \times 0.5 \approx 22.40$."
        ),
        (
            r"For the fiber in Question 51, the total number of guided modes $M_{\text{SI}}$ is approximately:",
            r"$125$",
            r"$251$",
            r"$502$",
            r"$1004$",
            "(b)",
            r"$M_{\text{SI}} \approx \frac{V^2}{2} = \frac{(22.40)^2}{2} = \frac{501.76}{2} \approx 251\text{ modes}$."
        ),
        (
            r"If the fiber in Question 51 had a parabolic Graded-Index profile ($M_{\text{GRIN}}$), the number of modes would be:",
            r"$63$",
            r"$125$",
            r"$251$",
            r"$502$",
            "(b)",
            r"$M_{\text{GRIN}} \approx \frac{V^2}{4} = \frac{501.76}{4} \approx 125\text{ modes}$."
        ),
        (
            r"A single-mode step-index fiber has $n_1 = 1.465$ and $n_2 = 1.460$. The maximum core radius $a_{\text{max}}$ for single-mode propagation at $\lambda = 1310\text{ nm}$ is:",
            r"$2.4\,\mu\text{m}$",
            r"$4.1\,\mu\text{m}$",
            r"$8.2\,\mu\text{m}$",
            r"$12.5\,\mu\text{m}$",
            "(b)",
            r"$\text{NA} = \sqrt{1.465^2 - 1.460^2} = \sqrt{0.014625} \approx 0.1209$. $a \le \frac{2.405 \lambda}{2\pi \text{NA}} = \frac{2.405(1.31 \times 10^{-6})}{2\pi (0.1209)} = \frac{3.1505 \times 10^{-6}}{0.7596} \approx 4.148\,\mu\text{m}$."
        ),
        (
            r"For the fiber in Question 54, the maximum allowable core diameter is:",
            r"$4.1\,\mu\text{m}$",
            r"$8.3\,\mu\text{m}$",
            r"$16.6\,\mu\text{m}$",
            r"$50.0\,\mu\text{m}$",
            "(b)",
            r"$\text{Diameter} = 2a_{\text{max}} = 2 \times 4.148\,\mu\text{m} \approx 8.30\,\mu\text{m}$."
        ),
        (
            r"If the operating wavelength in Question 54 is shifted to $\lambda = 1550\text{ nm}$, the fiber:",
            r"Remains strictly single-mode with an even smaller $V$-number ($V < 2.405$)",
            r"Becomes multimode",
            r"Stops guiding light completely",
            r"Increases its cutoff wavelength",
            "(a)",
            r"Because $V \propto 1/\lambda$, increasing wavelength from $1310\text{ nm}$ to $1550\text{ nm}$ lowers $V$ further below $2.405$, preserving single-mode operation."
        ),
        (
            r"An optical communication link of length $L = 50\text{ km}$ uses fiber with loss $0.22\text{ dB/km}$. The link contains 4 fusion splices ($0.05\text{ dB}$ each) and 2 connectors ($0.5\text{ dB}$ each). The total link loss is:",
            r"$11.0\text{ dB}$",
            r"$12.2\text{ dB}$",
            r"$15.0\text{ dB}$",
            r"$22.0\text{ dB}$",
            "(b)",
            r"$\text{Fiber loss} = 50 \times 0.22 = 11.0\text{ dB}$. $\text{Splice loss} = 4 \times 0.05 = 0.2\text{ dB}$. $\text{Connector loss} = 2 \times 0.5 = 1.0\text{ dB}$. $\text{Total} = 11.0 + 0.2 + 1.0 = 12.2\text{ dB}$."
        ),
        (
            r"If the transmitter launches $+3\text{ dBm}$ optical power into the link in Question 57, the received power in $\text{dBm}$ is:",
            r"$-9.2\text{ dBm}$",
            r"$-15.2\text{ dBm}$",
            r"$+15.2\text{ dBm}$",
            r"$-12.2\text{ dBm}$",
            "(a)",
            r"$P_{\text{rx}}(\text{dBm}) = P_{\text{tx}}(\text{dBm}) - \text{Total Loss} = +3\text{ dBm} - 12.2\text{ dB} = -9.2\text{ dBm}$."
        ),
        (
            r"The received power in microwatts ($\mu\text{W}$) for $P_{\text{rx}} = -9.2\text{ dBm}$ is approximately:",
            r"$12\mu\text{W}$",
            r"$120\mu\text{W}$",
            r"$1.2\text{ mW}$",
            r"$1.2\mu\text{W}$",
            "(b)",
            r"$P(\text{mW}) = 10^{-9.2/10} = 10^{-0.92} \approx 0.1202\text{ mW} = 120.2\,\mu\text{W}$."
        ),
        (
            r"A single-mode fiber has chromatic dispersion parameter $D = 17\text{ ps/(nm}\cdot\text{km)}$ at $1550\text{ nm}$. A DFB laser with spectral width $\Delta\lambda = 0.1\text{ nm}$ transmits over $80\text{ km}$. The total chromatic pulse broadening is:",
            r"$13.6\text{ ps}$",
            r"$136\text{ ps}$",
            r"$1.36\text{ ns}$",
            r"$13.6\text{ ns}$",
            "(b)",
            r"$\Delta\tau_{\text{chrom}} = |D| \cdot L \cdot \Delta\lambda = 17\text{ ps/(nm}\cdot\text{km)} \times 80\text{ km} \times 0.1\text{ nm} = 136\text{ ps}$."
        ),
        (
            r"For the link in Question 60, the maximum NRZ bit rate $B \approx 1/(2\Delta\tau)$ limited by chromatic dispersion is approximately:",
            r"$3.68\text{ Gbps}$",
            r"$7.35\text{ Gbps}$",
            r"$36.8\text{ Gbps}$",
            r"$368\text{ Mbps}$",
            "(a)",
            r"$B \approx \frac{1}{2(136 \times 10^{-12}\text{ s})} = \frac{1}{2.72 \times 10^{-10}} \approx 3.68 \times 10^9\text{ bps} = 3.68\text{ Gbps}$."
        ),
        (
            r"If the transmitter in Question 60 were replaced by an inexpensive Fabry-Perot laser with broad linewidth $\Delta\lambda = 2.0\text{ nm}$, the pulse broadening would become:",
            r"$136\text{ ps}$",
            r"$2.72\text{ ns}$",
            r"$27.2\text{ ns}$",
            r"$0.272\text{ ns}$",
            "(b)",
            r"$\Delta\tau = 17 \times 80 \times 2.0 = 2720\text{ ps} = 2.72\text{ ns}$ (severely degrading maximum bit rate to $\sim 184\text{ Mbps}$)."
        ),
        (
            r"The critical radius of curvature $R_c$ for macrobending loss in a single-mode fiber with core index $n_1$ and fractional difference $\Delta$ is given by:",
            r"$R_c \approx \frac{3 n_1^2 \lambda}{4\pi (n_1^2 - n_2^2)^{3/2}} = \frac{3 \lambda}{4\pi n_1 \sqrt{2}\Delta^{3/2}}$",
            r"$R_c \approx \frac{\lambda}{\Delta}$",
            r"$R_c \approx \frac{a^2}{\lambda}$",
            r"$R_c \approx \frac{2\pi a}{\text{NA}}$",
            "(a)",
            r"The critical bend radius varies inversely with $\Delta^{3/2}$: $R_c \approx \frac{3\lambda}{4\pi n_1 (2\Delta)^{3/2}}$."
        ),
        (
            r"If the relative index difference $\Delta$ is doubled ($2\times$), the critical macrobending radius $R_c$:",
            r"Decreases by a factor of $2^{3/2} \approx 2.83$ (making the fiber much more bend-tolerant)",
            r"Increases by $4\times$",
            r"Remains unchanged",
            r"Doubles",
            "(a)",
            r"Because $R_c \propto \Delta^{-3/2}$, increasing $\Delta$ reduces $R_c$, which is the principle used in bend-insensitive fibers (G.657)."
        ),
        (
            r"The field of an evanescent wave in the cladding decays with distance $r$ from core boundary as $e^{-\gamma (r-a)}$. The penetration depth $d_p = 1/\gamma$ is on the order of:",
            r"A few centimeters",
            r"A few millimeters",
            r"One wavelength ($\sim 1\,\mu\text{m}$)",
            r"Zero",
            "(c)",
            r"The evanescent tail decays exponentially within a distance comparable to the optical wavelength ($d_p \sim \lambda / (2\pi\sqrt{n_1^2\sin^2\phi - n_2^2}) \approx 1\,\mu\text{m}$)."
        ),
        (
            r"Why must the cladding thickness of an optical fiber be at least $20\text{--}50\,\mu\text{m}$ thick?",
            r"To ensure that the decaying evanescent wave tail reaches zero before encountering the lossy outer protective plastic jacket",
            r"To conduct electrical power",
            r"To protect the core from cosmic rays",
            r"To increase fiber weight",
            "(a)",
            r"If the cladding is too thin, the evanescent field penetrates into the high-loss buffer coating, causing massive optical leakage."
        ),
        (
            r"An optical fiber with $n_1 = 1.480$ and $n_2 = 1.475$ has a core radius $a = 4.5\,\mu\text{m}$. The cutoff wavelength $\lambda_c$ for single-mode operation is:",
            r"$1.05\,\mu\text{m}$",
            r"$1.43\,\mu\text{m}$",
            r"$1.75\,\mu\text{m}$",
            r"$2.10\,\mu\text{m}$",
            "(b)",
            r"$\text{NA} = \sqrt{1.48^2 - 1.475^2} = \sqrt{0.014775} \approx 0.12155$. $\lambda_c = \frac{2\pi a \text{NA}}{2.405} = \frac{2\pi (4.5\,\mu\text{m})(0.12155)}{2.405} = \frac{3.436}{2.405} \approx 1.429\,\mu\text{m}$."
        ),
        (
            r"For the fiber in Question 67, if light of wavelength $\lambda = 1310\text{ nm}$ ($1.31\,\mu\text{m}$) is launched, the fiber will support:",
            r"Strictly single-mode ($\text{HE}_{11}$ only)",
            r"Two or more guided modes (multimode operation, because $\lambda < \lambda_c$)",
            r"Zero modes",
            r"Infinite modes",
            "(b)",
            r"Since $\lambda = 1.31\,\mu\text{m} < \lambda_c = 1.43\,\mu\text{m}$, the $V$-number exceeds $2.405$ ($V \approx 2.62$), allowing higher-order modes ($\text{TE}_{01}, \text{TM}_{01}, \text{HE}_{21}$)."
        ),
        (
            r"Rayleigh scattering loss in silica at $850\text{ nm}$ is measured to be $\approx 1.8\text{ dB/km}$. The estimated Rayleigh scattering loss at $1550\text{ nm}$ is approximately:",
            r"$0.16\text{ dB/km}$",
            r"$0.50\text{ dB/km}$",
            r"$0.90\text{ dB/km}$",
            r"$1.20\text{ dB/km}$",
            "(a)",
            r"$\alpha(1550) = \alpha(850)\left(\frac{850}{1550}\right)^4 = 1.8 \times (0.5484)^4 = 1.8 \times 0.0904 \approx 0.163\text{ dB/km}$."
        ),
        (
            r"The Mode Field Diameter (MFD) of a single-mode fiber is slightly larger than the physical core diameter because:",
            r"A significant portion ($\sim 10\text{--}20\%$) of the fundamental mode's optical power travels in the cladding as an evanescent field",
            r"The core expands when heated by the laser",
            r"Light refracts at the input face",
            r"Photons bounce off the outer jacket",
            "(a)",
            r"The Gaussian field envelope of the $\text{HE}_{11}$ mode extends across the core boundary into the inner cladding."
        ),
        (
            r"In a Wavelength Division Multiplexing (WDM) network, multiple optical signals are transmitted over a single fiber by:",
            r"Assigning each communication channel to a distinct, non-overlapping laser optical wavelength",
            r"Time-slicing a single wavelength",
            r"Sending radio signals through the cladding",
            r"Switching the core diameter dynamically",
            "(a)",
            r"WDM multiplexes dozens of distinct laser channels ($\lambda_1, \lambda_2,\dots,\lambda_N$) simultaneously onto a single fiber."
        ),
        (
            r"Dense Wavelength Division Multiplexing (DWDM) typically uses ITU channel frequency grid spacings of:",
            r"$50\text{ GHz to }100\text{ GHz}$ ($\Delta\lambda \approx 0.4\text{ to }0.8\text{ nm}$)",
            r"$10\text{ THz}$",
            r"$1\text{ MHz}$",
            r"$100\text{ nm}$",
            "(a)",
            r"DWDM packs up to $80\text{--}160$ channels into the $1550\text{ nm}$ C-band using standardized $50\text{ GHz}$ or $100\text{ GHz}$ grid spacings."
        ),
        (
            r"Coarse Wavelength Division Multiplexing (CWDM) uses a wider standardized channel spacing of:",
            r"$20\text{ nm}$",
            r"$0.8\text{ nm}$",
            r"$1\text{ nm}$",
            r"$100\text{ nm}$",
            "(a)",
            r"CWDM specifies $20\text{ nm}$ channel spacing from $1270\text{ nm}$ to $1610\text{ nm}$, utilizing uncooled, lower-cost laser transmitters."
        ),
        (
            r"An Optical Time Domain Reflectometer (OTDR) locates fiber breaks, splices, and faults along a link by measuring:",
            r"The time delay and intensity of Rayleigh backscattered light and Fresnel reflections",
            r"The electrical resistance of the glass",
            r"The temperature of the cable",
            r"The gravitational pull on the fiber",
            "(a)",
            r"OTDR launches optical pulses and records backscattered light vs. time to create a spatial loss and event map of the link."
        ),
        (
            r"Polarization Mode Dispersion (PMD) in single-mode fibers is caused by:",
            r"Slight core non-circularity (ellipticity) and asymmetric mechanical stress creating birefringence between orthogonal polarization modes",
            r"Different light colors traveling at different speeds",
            r"Intermodal group delays",
            r"Thermal expansion of the cladding",
            "(a)",
            r"Fiber asymmetry breaks the degeneracy of the two orthogonal polarization states of $\text{HE}_{11}$, causing a differential group delay (DGD)."
        ),
        (
            r"The PMD coefficient of a modern single-mode telecom fiber is typically less than:",
            r"$0.1\text{ ps}/\sqrt{\text{km}}$",
            r"$100\text{ ps}/\sqrt{\text{km}}$",
            r"$10\text{ ns}/\sqrt{\text{km}}$",
            r"$1.0\,\mu\text{s}/\sqrt{\text{km}}$",
            "(a)",
            r"High-grade modern fiber exhibits $\text{PMD} < 0.05\text{--}0.1\text{ ps}/\sqrt{\text{km}}$, essential for $\ge 40\text{ Gbps}$ networks."
        ),
        (
            r"In an extrinsic fiber optic sensor:",
            r"The fiber acts solely as a light guide to convey light to and from an external sensing region",
            r"The fiber core itself is modified to become the transducer",
            r"No light is used",
            r"Sound waves replace photons",
            "(a)",
            r"In extrinsic sensors, light exits the fiber into an external transducer and re-enters, while in intrinsic sensors the fiber itself is the sensing medium."
        ),
        (
            r"A Fiber Optic Gyroscope (FOG) measures angular rotational velocity $\Omega$ by exploiting the:",
            r"Sagnac Effect in a multi-turn optical fiber coil",
            r"Doppler effect",
            r"Faraday magneto-optic effect",
            r"Hall effect",
            "(a)",
            r"Counter-propagating light beams in a closed fiber coil experience a phase difference $\Delta\Phi_S = \frac{8\pi N A \Omega}{\lambda c}$ proportional to rotation rate $\Omega$."
        ),
        (
            r"A fiber has a core of radius $a = 4.0\,\mu\text{m}$ and $\text{NA} = 0.14$. The single-mode cutoff wavelength $\lambda_c$ is:",
            r"$1.46\,\mu\text{m}$",
            r"$1.22\,\mu\text{m}$",
            r"$0.98\,\mu\text{m}$",
            r"$1.65\,\mu\text{m}$",
            "(a)",
            r"$\lambda_c = \frac{2\pi a \text{NA}}{2.405} = \frac{2\pi (4.0)(0.14)}{2.405} = \frac{3.5186}{2.405} \approx 1.463\,\mu\text{m}$."
        ),
        (
            r"The dynamic range of an optical receiver is defined as the difference between:",
            r"The maximum allowable input power before saturation (overload) and minimum input power for required bit-error-rate (sensitivity)",
            r"The input voltage and ground",
            r"The dark current and photocurrent",
            r"The laser wavelength and photodiode cutoff",
            "(a)",
            r"$\text{Dynamic Range (dB)} = P_{\text{saturation}}(\text{dBm}) - P_{\text{sensitivity}}(\text{dBm})$."
        ),

        # Part III: Advanced Mastery (81-100)
        (
            r"The exact modal electromagnetic fields in a weakly guiding step-index fiber ($\Delta \ll 1$) are described in the LP (Linearly Polarized) approximation using:",
            r"Bessel functions of the first kind $J_l(ur/a)$ in the core and Modified Bessel functions of the second kind $K_l(wr/a)$ in the cladding",
            r"Hermite-Gaussian polynomials exclusively",
            r"Legendre polynomials",
            r"Chebyshev polynomials",
            "(a)",
            r"For $\Delta \ll 1$, radial solutions are $J_l(ur/a)$ in the core ($r < a$) and decaying modified Bessel functions $K_l(wr/a)$ in the cladding ($r > a$)."
        ),
        (
            r"The core parameter $u$, cladding decay parameter $w$, and normalized frequency $V$ satisfy the circle relation:",
            r"$u^2 + w^2 = V^2$",
            r"$u^2 - w^2 = V^2$",
            r"$u + w = V$",
            r"$u w = V^2$",
            "(a)",
            r"From wave equations: $u = a\sqrt{k_0^2 n_1^2 - \beta^2}$ and $w = a\sqrt{\beta^2 - k_0^2 n_2^2} \implies u^2 + w^2 = a^2 k_0^2(n_1^2 - n_2^2) = V^2$."
        ),
        (
            r"The fundamental linearly polarized mode in an optical fiber is designated as:",
            r"$\text{LP}_{01}$ (corresponding to the exact vector mode $\text{HE}_{11}$)",
            r"$\text{LP}_{11}$",
            r"$\text{LP}_{00}$",
            r"$\text{LP}_{21}$",
            "(a)",
            r"The fundamental mode has zero azimuthal nodes ($l=0, m=1$), termed $\text{LP}_{01}$, formed by the two degenerate states of $\text{HE}_{11}$."
        ),
        (
            r"The second group of guided modes that emerge when $V > 2.405$ is designated as $\text{LP}_{11}$, comprising the vector modes:",
            r"$\text{TE}_{01}, \text{TM}_{01},$ and two degenerate states of $\text{HE}_{21}$ (total 4 mode states)",
            r"Only $\text{EH}_{11}$",
            r"$\text{HE}_{12}$ only",
            r"Sixteen degenerate modes",
            "(a)",
            r"$\text{LP}_{11}$ is a four-fold degenerate mode group combining $\text{TE}_{01}$, $\text{TM}_{01}$, and both polarization states of $\text{HE}_{21}$."
        ),
        (
            r"The material dispersion parameter $D_M$ is mathematically defined from the second derivative of refractive index with respect to wavelength as:",
            r"$D_M = -\frac{\lambda}{c}\frac{d^2 n}{d\lambda^2}$",
            r"$D_M = -\frac{c}{\lambda}\frac{dn}{d\lambda}$",
            r"$D_M = \frac{\lambda^2}{c}\frac{d^2 n}{d\lambda^2}$",
            r"$D_M = -\frac{1}{\lambda c}\frac{dn}{d\lambda}$",
            "(a)",
            r"Material dispersion arises from group delay variation: $D_M = \frac{d\tau_g}{d\lambda} = -\frac{\lambda}{c}\frac{d^2 n}{d\lambda^2}$, in $\text{ps/(nm}\cdot\text{km)}$."
        ),
        (
            r"Waveguide dispersion $D_W$ in a single-mode fiber arises physically because:",
            r"The distribution of optical power between the higher-index core and lower-index cladding varies with wavelength",
            r"The glass changes color when heated",
            r"Photons collide with each other",
            r"The fiber expands axially",
            "(a)",
            r"At longer wavelengths, the mode spreads further into the faster cladding, decreasing the effective index and creating waveguide dispersion."
        ),
        (
            r"In Non-Zero Dispersion-Shifted Fibers (NZ-DSF, ITU-T G.655), why is the chromatic dispersion intentionally maintained at a small non-zero value ($2\text{--}6\text{ ps/(nm}\cdot\text{km)}$) across the C-band?",
            r"To suppress Four-Wave Mixing (FWM) and non-linear cross-talk between adjacent DWDM channels by preventing phase-matching",
            r"To maximize signal attenuation",
            r"To reduce the speed of light",
            r"To eliminate the need for laser sources",
            "(a)",
            r"Zero dispersion enables perfect phase-matching for non-linear four-wave mixing; a small non-zero dispersion breaks phase-matching."
        ),
        (
            r"Self-Phase Modulation (SPM) in optical fibers is a non-linear effect caused by:",
            r"The intensity-dependent refractive index (optical Kerr effect: $n = n_0 + n_2 I$)",
            r"Thermal expansion",
            r"Core diameter variations",
            r"Acoustic vibrations",
            "(a)",
            r"High optical intensity modulates the local refractive index via the Kerr non-linearity $n_2$, inducing a time-dependent phase shift across the pulse."
        ),
        (
            r"An optical soliton is a stable wavepacket that propagates over thousands of kilometers without broadening due to the exact balance between:",
            r"Anomalous chromatic group velocity dispersion (GVD) and Self-Phase Modulation (SPM non-linearity)",
            r"Rayleigh scattering and Raman gain",
            r"Intermodal dispersion and Birefringence",
            r"Absorption and Reflection",
            "(a)",
            r"In the anomalous dispersion regime ($\beta_2 < 0$), SPM induces a positive frequency chirp that precisely counteracts GVD pulse broadening."
        ),
        (
            r"The fundamental non-linear Schrödinger equation (NLSE) governing pulse envelope $A(z,t)$ in an optical fiber is:",
            r"$i\frac{\partial A}{\partial z} - \frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2} + \gamma |A|^2 A = 0$",
            r"$\frac{\partial A}{\partial z} + v \frac{\partial A}{\partial t} = 0$",
            r"$\nabla^2 A + k^2 A = 0$",
            r"$i\hbar\frac{\partial A}{\partial t} = \hat{H}A$",
            "(a)",
            r"The NLSE $i\frac{\partial A}{\partial z} = \frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2} - \gamma |A|^2 A$ mathematically models dispersion ($\beta_2$) and Kerr non-linearity ($\gamma$)."
        ),
        (
            r"Stimulated Brillouin Scattering (SBS) in optical fibers is an inelastic non-linear interaction between the optical wave and:",
            r"Acoustic phonons (density sound waves) in the glass lattice, creating a backward-propagating Stokes wave",
            r"Optical phonons exclusively",
            r"Free electrons",
            r"Radio waves",
            "(a)",
            r"SBS couples an intense forward pump wave to acoustic density waves via electrostriction, generating a frequency-downshifted backward Stokes wave."
        ),
        (
            r"The frequency shift in Stimulated Brillouin Scattering (SBS) in silica at $1550\text{ nm}$ is approximately:",
            r"$11\text{ GHz}$",
            r"$13\text{ THz}$",
            r"$100\text{ MHz}$",
            r"$1\text{ THz}$",
            "(a)",
            r"Acoustic velocity in silica ($v_a \approx 5960\text{ m/s}$) yields an SBS frequency Doppler shift $\nu_B = \frac{2 n v_a}{\lambda} \approx 11.1\text{ GHz}$."
        ),
        (
            r"Stimulated Raman Scattering (SRS) in optical fibers couples optical photons to optical phonon molecular vibrations, producing a broad gain spectrum with peak shift around:",
            r"$13.2\text{ THz}$ ($\sim 100\text{ nm}$)",
            r"$11\text{ GHz}$",
            r"$100\text{ kHz}$",
            r"$500\text{ THz}$",
            "(a)",
            r"SRS involves high-frequency optical vibrational modes of Si-O-Si bonds, creating a broad Raman amplification band centered at $\Delta\nu_R \approx 13.2\text{ THz}$."
        ),
        (
            r"Photonic Crystal Fibers (PCF), or microstructured holey fibers, guide light using:",
            r"A 2D periodic array of microscopic air holes running along the fiber cladding",
            r"Solid metal cladding",
            r"Liquid mercury cores",
            r"Radio frequency plasma",
            "(a)",
            r"PCFs utilize microscopic air-hole lattices to guide light either via effective index contrast or Photonic Bandgap (PBG) confinement."
        ),
        (
            r"Hollow-Core Photonic Bandgap Fibers (HC-PBGF) can guide light in an empty air/vacuum core because:",
            r"The microstructured cladding creates a 2D photonic bandgap that forbids light of that frequency from escaping into the cladding",
            r"Air has a higher refractive index than silica",
            r"Total internal reflection occurs at the air boundary",
            r"The core is coated with gold mirrors",
            "(a)",
            r"Photonic bandgap structures act as distributed Bragg mirrors in all radial directions, trapping light in a lower-index air core."
        ),
        (
            r"Guiding light in an air core in Hollow-Core Fibers reduces optical latency by:",
            r"$\approx 30\%$ (since light travels at $c \approx 3 \times 10^8\text{ m/s}$ in air vs. $c/1.45 \approx 2.07 \times 10^8\text{ m/s}$ in silica)",
            r"$50\%$",
            r"$100\%$",
            r"$1\%$",
            "(a)",
            r"In glass $n=1.45$, latency is $\approx 4.88\,\mu\text{s/km}$; in hollow air-core ($n \approx 1.00$), latency drops to $\approx 3.33\,\mu\text{s/km}$ (critical for high-frequency trading)."
        ),
        (
            r"A Distributed Acoustic Sensing (DAS) system uses phase-sensitive OTDR ($\Phi$-OTDR) over fiber cables to detect:",
            r"Acoustic vibrations, perimeter intrusions, pipeline leaks, and seismic waves along $100\text{ km}$ infrastructure",
            r"Atmospheric wind on Mars",
            r"Magnetic pole reversals",
            r"Solar sunspots",
            "(a)",
            r"Coherent Rayleigh backscattering detects nanometer strain variations along standard telecommunication fiber cables, turning them into continuous acoustic sensor arrays."
        ),
        (
            r"The Petermann-II Mode Field Radius $w_p$ in single-mode fibers is fundamentally related to the far-field divergence angle $\theta_{\text{ff}}$ by:",
            r"$w_p = \frac{\lambda}{\pi \theta_{\text{ff}}}$",
            r"$w_p = \frac{\pi \theta_{\text{ff}}}{\lambda}$",
            r"$w_p = \sqrt{\lambda \theta_{\text{ff}}}$",
            r"$w_p = \frac{1}{\lambda \theta_{\text{ff}}}$",
            "(a)",
            r"The Petermann-II definition characterizes waveguide dispersion and splice misalignment loss: $w_p = \frac{\lambda}{\pi \theta_{\text{ff}}}$."
        ),
        (
            r"The non-linear coefficient $\gamma$ of a single-mode optical fiber is given by:",
            r"$\gamma = \frac{2\pi n_2}{\lambda A_{\text{eff}}}$",
            r"$\gamma = \frac{n_2 A_{\text{eff}}}{\lambda}$",
            r"$\gamma = \frac{2\pi \lambda}{n_2 A_{\text{eff}}}$",
            r"$\gamma = \frac{\lambda n_2}{2\pi}$",
            "(a)",
            r"The Kerr non-linear coefficient is $\gamma = \frac{2\pi n_2}{\lambda A_{\text{eff}}}\text{ W}^{-1}\text{km}^{-1}$, where $n_2$ is non-linear index and $A_{\text{eff}}$ is effective area."
        ),
        (
            r"In high-speed coherent optical transmission ($100\text{--}800\text{ Gbps}$), electronic Digital Signal Processing (DSP) at the receiver completely compensates for:",
            r"All accumulated chromatic dispersion ($D$) and polarization mode dispersion (PMD) digitally without optical dispersion compensating fibers",
            r"Fiber physical cuts",
            r"Thermal damage to the cable",
            r"Photon absorption by water",
            "(a)",
            r"Coherent detection with local oscillator lasers recovers full amplitude and phase, allowing digital finite impulse response (FIR) filters to invert dispersion."
        )
    ]
    
    theory_qs = [
        (
            r"Derive from ray optics the expressions for the Acceptance Angle $\theta_a$ and Numerical Aperture ($\text{NA}$) of a step-index optical fiber. Prove the approximation $\text{NA} \approx n_1\sqrt{2\Delta}$ where $\Delta$ is the fractional refractive index difference.",
            r"""\textbf{1. Geometric Ray Analysis at Fiber Entrance}:
Consider a cylindrical step-index fiber with core index $n_1$ and cladding index $n_2$ ($n_1 > n_2$) launched from an external medium of refractive index $n_0$ (usually air, $n_0 = 1$).
Let a light ray enter the flat entrance face of the core at an incident angle $\theta_i$ with the fiber axis.
\begin{enumerate}
    \item \textbf{Snell's Law of Refraction at Entrance Face}:
    \begin{equation}
    n_0 \sin\theta_i = n_1 \sin\theta_r
    \end{equation}
    where $\theta_r$ is the angle of refraction inside the core.
    \item \textbf{Condition at Core-Cladding Boundary}:
    The ray strikes the core-cladding interface at an angle of incidence $\phi$.
    From right-triangle geometry inside the core:
    \begin{equation}
    \theta_r + \phi = 90^\circ \implies \theta_r = 90^\circ - \phi \implies \sin\theta_r = \sin(90^\circ - \phi) = \cos\phi
    \end{equation}
    Substituting Eq. (2) into Eq. (1):
    \begin{equation}
    n_0 \sin\theta_i = n_1 \cos\phi
    \end{equation}
    \item \textbf{Total Internal Reflection Condition}:
    For the ray to be guided along the core by TIR, $\phi \ge \phi_c$, where critical angle is $\sin\phi_c = \frac{n_2}{n_1}$.
    The maximum launch angle $\theta_i = \theta_a$ (Acceptance Angle) occurs when $\phi = \phi_c$:
    \begin{equation}
    \cos\phi_c = \sqrt{1 - \sin^2\phi_c} = \sqrt{1 - \left(\frac{n_2}{n_1}\right)^2} = \frac{\sqrt{n_1^2 - n_2^2}}{n_1}
    \end{equation}
    Substituting Eq. (4) into Eq. (3):
    \begin{equation}
    n_0 \sin\theta_a = n_1 \left( \frac{\sqrt{n_1^2 - n_2^2}}{n_1} \right) = \sqrt{n_1^2 - n_2^2}
    \end{equation}
    For air ($n_0 = 1$):
    \begin{equation}
    \mathbf{\sin\theta_a = \sqrt{n_1^2 - n_2^2} \implies \theta_a = \sin^{-1}\left(\sqrt{n_1^2 - n_2^2}\right)}
    \end{equation}
    \item \textbf{Numerical Aperture ($\text{NA}$)}:
    \begin{equation}
    \mathbf{\text{NA} = n_0 \sin\theta_a = \sqrt{n_1^2 - n_2^2}}
    \end{equation}
\end{enumerate}

\textbf{2. Proof of Approximation $\text{NA} \approx n_1\sqrt{2\Delta}$}:
Define fractional index difference $\Delta = \frac{n_1 - n_2}{n_1} \implies n_1 - n_2 = n_1 \Delta$.
Factoring the difference of squares:
\begin{equation}
n_1^2 - n_2^2 = (n_1 - n_2)(n_1 + n_2) = (n_1 \Delta)(n_1 + n_2)
\end{equation}
In weakly guiding optical fibers ($\Delta \ll 1$), $n_1 \approx n_2 \implies n_1 + n_2 \approx 2 n_1$:
\begin{equation}
n_1^2 - n_2^2 \approx (n_1 \Delta)(2 n_1) = 2 n_1^2 \Delta
\end{equation}
Taking the square root on both sides:
\begin{equation}
\mathbf{\text{NA} = \sqrt{n_1^2 - n_2^2} \approx n_1 \sqrt{2\Delta}}
\end{equation}"""
        ),
        (
            r"Derive the formula for intermodal pulse dispersion delay $\Delta \tau_{\text{modal}}$ in a step-index multimode fiber. Calculate the resulting maximum bit rate and bandwidth-distance product.",
            r"""\textbf{1. Ray Transit Time Derivation}:
Consider a step-index fiber of length $L$.
\begin{enumerate}
    \item \textbf{Fastest Ray (Axial Ray)}:
    A ray traveling along the central axis ($\theta = 0^\circ$) covers physical distance $L$ with speed $v = c/n_1$:
    \begin{equation}
    t_{\text{min}} = \frac{L}{v} = \frac{L n_1}{c}
    \end{equation}
    \item \textbf{Slowest Ray (Extreme Zigzag Ray)}:
    The ray entering at acceptance angle $\theta_a$ reflects at the critical angle $\phi_c$. The zigzag path length is $L_{\text{max}} = L/\sin\phi_c = L(n_1/n_2)$:
    \begin{equation}
    t_{\text{max}} = \frac{L_{\text{max}}}{v} = \frac{L(n_1/n_2)}{c/n_1} = \frac{L n_1^2}{c n_2}
    \end{equation}
    \item \textbf{Intermodal Delay Difference ($\Delta \tau_{\text{modal}}$)}:
    \begin{equation}
    \Delta \tau_{\text{modal}} = t_{\text{max}} - t_{\text{min}} = \frac{L n_1^2}{c n_2} - \frac{L n_1}{c} = \frac{L n_1}{c}\left(\frac{n_1 - n_2}{n_2}\right)
    \end{equation}
    Using $n_2 \approx n_1$ and $\Delta = (n_1 - n_2)/n_1$:
    \begin{equation}
    \mathbf{\Delta \tau_{\text{modal}} \approx \frac{L n_1 \Delta}{c} = \frac{L (\text{NA})^2}{2 n_1 c}}
    \end{equation}
\end{enumerate}

\textbf{2. Maximum Bit Rate & Bandwidth-Distance Product}:
To prevent overlapping of adjacent digital pulses (Inter-Symbol Interference), the bit period must satisfy $T_b \ge 2\Delta\tau$:
\begin{equation}
\mathbf{B_{\text{max}} = \frac{1}{T_b} \approx \frac{1}{2\Delta \tau_{\text{modal}}} = \frac{c}{2 L n_1 \Delta}}
\end{equation}
The Bandwidth-Distance product ($B \times L$) is invariant for a given fiber:
\begin{equation}
\mathbf{B \times L \approx \frac{c}{2 n_1 \Delta}}
\end{equation}"""
        ),
        (
            r"Explain the structure and refractive index profile of a Graded-Index (GRIN) optical fiber. Derive how the parabolic profile equalizes modal group velocities, and compare its dispersion with a step-index fiber.",
            r"""\textbf{1. Refractive Index Profile}:
In a parabolic Graded-Index fiber, the core index is continuously graded as a function of radial distance $r$:
\begin{equation}
n(r) = \begin{cases}
n_1 \sqrt{1 - 2\Delta\left(\frac{r}{a}\right)^2} \approx n_1 \left[1 - \Delta\left(\frac{r}{a}\right)^2\right] & \text{for } r \le a \\
n_1 \sqrt{1 - 2\Delta} = n_2 & \text{for } r \ge a
\end{cases}
\end{equation}

\textbf{2. Physical Mechanism of Modal Delay Equalization}:
\begin{itemize}
    \item Axial rays travel along the highest refractive index path ($n = n_1$), moving at the slowest local speed $v_{\text{axis}} = c/n_1$.
    \item Higher-order off-axis rays follow sinusoidal/helical curving paths. Although their physical path length is longer, they spend most of their transit time in the outer regions of the core where the refractive index $n(r) < n_1$ is lower, meaning local light velocity $v(r) = c/n(r)$ is faster.
    \item By selecting an optimal profile parameter ($\alpha \approx 2 - 2\Delta$), the faster velocity in outer zones precisely offsets the extra geometric path length.
\end{itemize}

\textbf{3. Mathematical Comparison of Intermodal Dispersion}:
\begin{itemize}
    \item \textbf{Step-Index Multimode Fiber}:
    \begin{equation}
    \Delta \tau_{\text{SI}} \approx \frac{L n_1 \Delta}{c} \quad (\text{Linear in } \Delta)
    \end{equation}
    \item \textbf{Optimal Parabolic GRIN Fiber}:
    \begin{equation}
    \Delta \tau_{\text{GRIN}} \approx \frac{L n_1 \Delta^2}{8 c} \text{ to } \frac{L n_1 \Delta^2}{2 c} \quad (\text{Quadratic in } \Delta)
    \end{equation}
    \item \textbf{Improvement Factor}:
    \begin{equation}
    \frac{\Delta \tau_{\text{SI}}}{\Delta \tau_{\text{GRIN}}} \approx \frac{\Delta}{\Delta^2 / 2} = \frac{2}{\Delta}
    \end{equation}
    For a typical fiber with $\Delta = 1\% = 0.01$, the dispersion is reduced by $\frac{2}{0.01} = \mathbf{200\times \text{ to } 1000\times}$, dramatically increasing data transmission bandwidth."""
        ),
        (
            r"Define the Normalized Frequency ($V$-number) of an optical fiber. Derive the single-mode cutoff condition $V \le 2.405$ and obtain the formula for cutoff wavelength $\lambda_c$. Explain the physical meaning of mode cutoff.",
            r"""\textbf{1. Definition of $V$-Number}:
The $V$-number (normalized frequency) is a dimensionless parameter combining core radius $a$, operating wavelength $\lambda$, and Numerical Aperture:
\begin{equation}
\mathbf{V = \frac{2\pi a}{\lambda}\text{NA} = \frac{2\pi a}{\lambda}\sqrt{n_1^2 - n_2^2} = \frac{2\pi a}{\lambda}n_1\sqrt{2\Delta}}
\end{equation}

\textbf{2. Electromagnetic Wave Equation & Cutoff Condition}:
Inside a cylindrical dielectric waveguide, Maxwell's equations yield the Bessel differential equation for the axial electric field $E_z(r,\phi) = A J_l(ur/a)\cos(l\phi)$.
In the cladding ($r > a$), fields decay as modified Bessel functions $K_l(wr/a)$, where $u^2 + w^2 = V^2$.
\begin{itemize}
    \item Mode cutoff occurs when the field in the cladding ceases to be evanescently bound ($w \to 0$), meaning the mode spreads infinitely into the cladding and escapes guidance.
    \item At cutoff ($w = 0$), $u = V$.
    \item The fundamental mode ($\text{HE}_{11} \iff \text{LP}_{01}$) has $l=0$ and exhibits \textit{no cutoff} ($V_{\text{cutoff}} = 0$). It remains guided for all $V > 0$.
    \item The first set of higher-order modes ($\text{TE}_{01}, \text{TM}_{01}, \text{HE}_{21} \iff \text{LP}_{11}$) have cutoff governed by the first root of $J_0(V) = 0$:
    \begin{equation}
    V_{\text{cutoff}} = 2.4048 \approx \mathbf{2.405}
    \end{equation}
\end{itemize}

\textbf{3. Single-Mode Condition and Cutoff Wavelength $\lambda_c$}:
To enforce strictly single-mode propagation ($\text{LP}_{01}$ only):
\begin{equation}
V \le 2.405 \implies \frac{2\pi a}{\lambda}\text{NA} \le 2.405 \implies \mathbf{\lambda \ge \lambda_c = \frac{2\pi a}{2.405}\text{NA}}
\end{equation}
\textit{Physical Meaning}: $\lambda_c$ is the shortest wavelength at which the fiber supports only a single guided mode. Operating at $\lambda < \lambda_c$ allows multiple modes to propagate."""
        ),
        (
            r"Discuss in detail the various signal attenuation mechanisms in optical fibers: (a) Material Absorption (Intrinsic & Extrinsic), (b) Rayleigh Scattering, and (c) Bending Losses (Macrobending & Microbending). Sketch the spectral attenuation curve of silica fiber.",
            r"""\textbf{1. Material Absorption}:
\begin{enumerate}
    \item \textbf{Intrinsic Absorption}: Inherent electronic bandgap transitions in pure $\text{SiO}_2$ in the deep UV ($\lambda < 0.4\,\mu\text{m}$) and vibrational lattice absorption of Si-O bonds in the infrared ($\lambda > 1.6\,\mu\text{m}$).
    \item \textbf{Extrinsic Absorption}: Caused by metallic transition-ion impurities ($\text{Fe}^{2+}, \text{Cu}^{2+}, \text{Cr}^{3+}$) and hydroxyl ($\text{OH}^-$) water ions. $\text{OH}^-$ introduces sharp vibrational overtone absorption peaks at $950\text{ nm}, 1240\text{ nm},$ and prominently at \textbf{$1383\text{ nm}$ ($1.38\,\mu\text{m}$)}.
\end{enumerate}

\textbf{2. Rayleigh Scattering Loss}:
Caused by sub-microscopic compositional and thermal density fluctuations frozen into the glass during draw cooling.
\begin{equation}
\alpha_{\text{Rayleigh}} = \frac{8\pi^3}{3\lambda^4}(n^8 p^2)(k_B T_f \beta_T) \propto \mathbf{\frac{1}{\lambda^4}}
\end{equation}
It dominates the short-wavelength loss ($> 2\text{ dB/km}$ at $850\text{ nm}$) and drops to $< 0.16\text{ dB/km}$ at $1550\text{ nm}$.

\textbf{3. Bending Losses}:
\begin{enumerate}
    \item \textbf{Macrobending Loss}: When the fiber is curved with radius $R \le R_c$, the phase velocity of the evanescent field in the outer cladding would have to exceed the local speed of light $c/n_2$ to keep up with the wavefront. Since this is physically impossible, the power in the outer tail radiates away as loss.
    \item \textbf{Microbending Loss}: Microscopic axial irregularities, localized jacket pressure, or surface roughness ($< 1\,\mu\text{m}$) couple guided core modes into radiating cladding modes.
\end{enumerate}

\textbf{4. Silica Spectral Attenuation Spectrum}:
\begin{itemize}
    \item \textbf{First Window ($850\text{ nm}$)}: $\alpha \approx 2.0\text{--}2.5\text{ dB/km}$ (limited by Rayleigh scattering; uses inexpensive GaAs LEDs).
    \item \textbf{Second Window ($1310\text{ nm}$)}: $\alpha \approx 0.35\text{ dB/km}$ (zero chromatic dispersion in standard silica).
    \item \textbf{Third Window ($1550\text{ nm}$)}: $\alpha \approx 0.18\text{--}0.20\text{ dB/km}$ (\textbf{Absolute Lowest Loss}; compatible with EDFA amplifiers).
\end{itemize}"""
        ),
        (
            r"Explain Intramodal (Chromatic) Dispersion in single-mode fibers. Distinguish between Material Dispersion ($D_M$) and Waveguide Dispersion ($D_W$). Explain how Dispersion-Shifted (DSF) and Dispersion-Flattened (DFF) fibers are engineered.",
            r"""\textbf{1. Chromatic Dispersion Concept}:
Even in a single-mode fiber where intermodal dispersion is zero, an optical pulse containing a range of spectral wavelengths $\Delta\lambda$ spreads in time because different spectral components travel at different group velocities:
\begin{equation}
\mathbf{D_{\text{total}} = D_M + D_W = -\frac{\lambda}{c}\frac{d^2 n}{d\lambda^2} - \frac{n_2 \Delta}{c \lambda}\left[ V \frac{d^2(V b)}{dV^2} \right] \quad \left[\frac{\text{ps}}{\text{nm}\cdot\text{km}}\right]}
\end{equation}

\textbf{2. Components}:
\begin{itemize}
    \item \textbf{Material Dispersion ($D_M$)}: Arises from the wavelength dependence of the refractive index of fused silica ($n(\lambda)$) described by the Sellmeier equation. $D_M$ is negative for $\lambda < 1270\text{ nm}$, crosses zero at $\approx 1270\text{ nm}$, and becomes positive ($+17\text{ ps/(nm}\cdot\text{km)}$) at $1550\text{ nm}$.
    \item \textbf{Waveguide Dispersion ($D_W$)}: Arises from fiber boundary geometry. As $\lambda$ increases, the mode spreads deeper into the lower-index cladding, lowering the effective index $n_{\text{eff}}(\lambda)$. $D_W$ is naturally negative across the telecommunication band.
\end{itemize}

\textbf{3. Engineered Fiber Profiles}:
\begin{enumerate}
    \item \textbf{Standard SMF (ITU-T G.652)}:
    $D_M$ and $D_W$ cancel out at \textbf{$\lambda_0 \approx 1310\text{ nm}$}. At $1550\text{ nm}$, $D \approx +17\text{ ps/(nm}\cdot\text{km)}$.
    \item \textbf{Dispersion-Shifted Fiber (DSF, ITU-T G.653)}:
    By using a segmented triangular or graded-core profile, the negative waveguide dispersion $D_W$ is increased in magnitude, shifting the net zero-dispersion wavelength $\lambda_0$ from $1310\text{ nm}$ directly to the minimum-loss window at \textbf{$1550\text{ nm}$}.
    \item \textbf{Dispersion-Flattened Fiber (DFF)}:
    Using quadruple-clad (W-profile) index designs, $D_W$ balances $D_M$ over a broad wavelength range ($1300\text{--}1600\text{ nm}$), providing low dispersion across the entire spectrum.
\end{enumerate}"""
        ),
        (
            r"Describe the architecture, components, and working of an Optical Fiber Communication Link. Draw a complete block diagram showing Transmitter, Optical Fiber Channel, Repeaters/EDFA, and Receiver.",
            r"""\textbf{1. Block Diagram of Optical Fiber Link}:
A complete point-to-point fiber optic communication link comprises four principal subsystems:
\begin{itemize}
    \item \textbf{1. Transmitter}:
    \begin{enumerate}
        \item \textit{Data Encoder & Modulator}: Converts digital bit streams into electrical driving pulses.
        \item \textit{Optical Source}: Semiconductor Laser Diode (DFB/VCSEL) or LED that converts electrical signals into optical pulses.
        \item \textit{Drive Circuit & Temperature Controller}: Stabilizes laser bias current and TEC temperature.
    \end{enumerate}
    \item \textbf{2. Optical Fiber Channel}:
    Single-mode or multimode silica fibers packaged into armored optical cables.
    \item \textbf{3. Optical Amplifiers / Repeaters}:
    Erbium-Doped Fiber Amplifiers (EDFA) periodically placed every $50\text{--}80\text{ km}$ to boost attenuated optical signals directly in the optical domain without electronic conversion.
    \item \textbf{4. Receiver}:
    \begin{enumerate}
        \item \textit{Photodetector (PIN / APD)}: Converts incoming photons into electrical photocurrent.
        \item \textit{Transimpedance Pre-amplifier (TIA)}: Amplifies weak microampere photocurrents into voltage signals.
        \item \textit{Equalizer & Clock Recovery (CDR)}: Removes inter-symbol interference and synchronizes digital clock.
        \item \textit{Decision Circuit / DSP}: Regenerates the original digital bit stream.
    \end{enumerate}
\end{itemize}

\textbf{2. Power Budget Equation}:
\begin{equation}
\mathbf{P_{\text{tx}}(\text{dBm}) - P_{\text{rx, sens}}(\text{dBm}) \ge \alpha L + N_{\text{splice}} L_{\text{splice}} + N_{\text{conn}} L_{\text{conn}} + \text{System Margin}}
\end{equation}"""
        ),
        (
            r"Explain the principle, construction, and working of Fiber Bragg Grating (FBG) Sensors. Derive the Bragg resonance wavelength condition and explain how FBGs measure strain and temperature.",
            r"""\textbf{1. Construction & Principle}:
A Fiber Bragg Grating (FBG) is an intrinsic optical sensor created by exposing the core of a photosensitive Germanium-doped single-mode fiber to an intense UV laser interference pattern.
This inscribes a permanent, periodic modulation of the core refractive index with spatial pitch $\Lambda$ (typically $\sim 0.5\,\mu\text{m}$).

\textbf{2. Bragg Reflection Condition}:
When a broadband spectrum of light is launched into the fiber, wavelets reflected from each successive index fringe interfere constructively at the \textbf{Bragg Wavelength $\lambda_B$}:
\begin{equation}
\mathbf{\lambda_B = 2 n_{\text{eff}} \Lambda}
\end{equation}
where $n_{\text{eff}}$ is the effective modal refractive index and $\Lambda$ is the grating pitch.
A narrow wavelength band centered at $\lambda_B$ is reflected backward, while all other wavelengths pass through unattenuated.

\textbf{3. Strain and Temperature Sensing Mechanism}:
Differentiating the Bragg condition:
\begin{equation}
\Delta\lambda_B = 2\left(\Delta n_{\text{eff}} \Lambda + n_{\text{eff}} \Delta\Lambda\right) \implies \frac{\Delta\lambda_B}{\lambda_B} = \frac{\Delta\Lambda}{\Lambda} + \frac{\Delta n_{\text{eff}}}{n_{\text{eff}}}
\end{equation}
\begin{enumerate}
    \item \textbf{Mechanical Strain ($\epsilon = \Delta L/L$)}:
    Elongation stretches the grating pitch ($\Delta\Lambda/\Lambda = \epsilon$) and changes index via the photoelastic tensor ($p_e \approx 0.22$):
    \begin{equation}
    \left(\frac{\Delta\lambda_B}{\lambda_B}\right)_{\text{strain}} = (1 - p_e)\epsilon \approx 0.78 \epsilon \implies \mathbf{\Delta\lambda_B \approx 1.2\text{ pm}/\mu\epsilon \text{ at } 1550\text{ nm}}
    \end{equation}
    \item \textbf{Temperature Change ($\Delta T$)}:
    Thermal expansion ($\alpha_{\text{glass}} \approx 0.5 \times 10^{-6}\text{ K}^{-1}$) and the thermo-optic effect ($\xi = \frac{1}{n}\frac{dn}{dT} \approx 6.8 \times 10^{-6}\text{ K}^{-1}$) shift the wavelength:
    \begin{equation}
    \left(\frac{\Delta\lambda_B}{\lambda_B}\right)_{\text{temp}} = (\alpha_{\text{glass}} + \xi)\Delta T \implies \mathbf{\Delta\lambda_B \approx 10\text{--}13\text{ pm}/^\circ\text{C}}
    \end{equation}
\end{enumerate}

\textbf{4. Engineering Applications}:
Structural health monitoring of bridges, smart dams, aircraft wings, turbine blades, and nuclear reactors through multiplexed FBG arrays along a single optical fiber."""
        ),
        (
            r"An optical fiber communication link of length $L = 60\text{ km}$ operates at $\lambda = 1550\text{ nm}$. The fiber attenuation is $\alpha = 0.20\text{ dB/km}$. The link includes 6 splices with $0.05\text{ dB}$ loss each and 2 connectors with $0.6\text{ dB}$ loss each. The transmitter launches $+2\text{ dBm}$ power and receiver sensitivity is $-28\text{ dBm}$. Calculate: (a) total link loss, (b) received optical power in $\text{dBm}$ and $\mu\text{W}$, (c) link power safety margin, and (d) maximum possible transmission distance for a $6\text{ dB}$ safety margin.",
            r"""\textbf{1. Total Link Loss $\alpha_{\text{total}}$}:
\begin{align*}
\text{Fiber Loss} &= 60\text{ km} \times 0.20\text{ dB/km} = 12.0\text{ dB} \\
\text{Splice Loss} &= 6 \times 0.05\text{ dB} = 0.30\text{ dB} \\
\text{Connector Loss} &= 2 \times 0.60\text{ dB} = 1.20\text{ dB} \\
\mathbf{\text{Total Loss}} &= 12.0 + 0.30 + 1.20 = \mathbf{13.50\text{ dB}}
\end{align*}

\textbf{2. Received Optical Power $P_{\text{rx}}$}:
\begin{align*}
\mathbf{P_{\text{rx}}(\text{dBm})} &= P_{\text{tx}}(\text{dBm}) - \text{Total Loss} = +2\text{ dBm} - 13.50\text{ dB} = \mathbf{-11.50\text{ dBm}} \\
\mathbf{P_{\text{rx}}(\mu\text{W})} &= 10^{-11.5/10}\text{ mW} = 10^{-1.15}\text{ mW} \approx 0.0708\text{ mW} = \mathbf{70.8\,\mu\text{W}}
\end{align*}

\textbf{3. Link Power Safety Margin}:
\begin{equation}
\mathbf{\text{Margin} = P_{\text{rx}}(\text{dBm}) - P_{\text{sensitivity}}(\text{dBm}) = -11.50\text{ dBm} - (-28.0\text{ dBm}) = +16.50\text{ dB}}
\end{equation}
Since margin is $+16.50\text{ dB} > 0$, the optical link operates with excellent reliability.

\textbf{4. Maximum Distance $L_{\text{max}}$ with $6\text{ dB}$ Safety Margin}:
Total allowable loss = $P_{\text{tx}} - P_{\text{sens}} - \text{Margin} = 2 - (-28) - 6 = 24.0\text{ dB}$.
Fixed losses = $\text{Splices} + \text{Connectors} = 0.30 + 1.20 = 1.50\text{ dB}$.
Allowable fiber loss = $24.0 - 1.50 = 22.5\text{ dB}$.
\begin{equation}
\mathbf{L_{\text{max}} = \frac{22.5\text{ dB}}{0.20\text{ dB/km}} = 112.5\text{ km}}
\end{equation}"""
        ),
        (
            r"Explain the physical principles and applications of: (a) Double-Heterostructure Semiconductor Lasers in optical communications, and (b) Erbium-Doped Fiber Amplifiers (EDFA) in undersea transatlantic optical cables.",
            r"""\textbf{1. Double-Heterostructure (DH) Lasers}:
\begin{itemize}
    \item \textbf{Carrier Confinement}: A thin active direct-bandgap semiconductor (GaAs, $E_g = 1.42\text{ eV}$) is sandwiched between p-type and n-type cladding layers of wider bandgap ($\text{Al}_{0.3}\text{Ga}_{0.7}\text{As}$, $E_g = 1.8\text{ eV}$). Potential energy barriers trap injected electrons and holes inside the active layer, drastically reducing threshold current density $J_{\text{th}}$ from $50,000\text{ A/cm}^2$ (homojunction) to $< 1000\text{ A/cm}^2$, enabling room-temperature CW operation.
    \item \textbf{Optical Confinement}: The active GaAs layer has a higher refractive index ($n \approx 3.6$) than AlGaAs cladding ($n \approx 3.4$). This forms a slab optical dielectric waveguide, confining photons tightly to the active gain region.
\end{itemize}

\textbf{2. Erbium-Doped Fiber Amplifiers (EDFA)}:
\begin{itemize}
    \item \textbf{Principle}: Silica fiber doped with $\approx 1000\text{ ppm}$ of Erbium ions ($\text{Er}^{3+}$) is pumped by $980\text{ nm}$ or $1480\text{ nm}$ laser diodes, creating population inversion between $^4I_{13/2}$ and $^4I_{15/2}$.
    \item Incoming $1550\text{ nm}$ optical data pulses trigger stimulated emission, multiplying photon flux directly in the optical domain without electronic conversion.
    \item \textbf{Role in Submarine Cables}: Transatlantic undersea cables (e.g., TAT-14, MAREA) traverse $> 6000\text{ km}$. Submersible EDFAs placed every $60\text{ km}$ amplify all DWDM channels ($> 100\text{ wavelengths}$) simultaneously with high gain ($> 30\text{ dB}$), low noise figure ($< 5\text{ dB}$), and complete protocol/data-rate transparency."""
        ),
        (
            r"A graded-index fiber with parabolic index profile has core radius $a = 30\,\mu\text{m}$, $n_1 = 1.48$, and $\Delta = 1.2\%$. Calculate: (a) Numerical aperture on the fiber axis, (b) $V$-number at $\lambda = 1300\text{ nm}$, (c) total number of guided modes $M_{\text{GRIN}}$, and (d) pulse broadening per km $\Delta\tau/L$ and compare it with an equivalent step-index fiber.",
            r"""\textbf{1. Numerical Aperture ($\text{NA}$)}:
\begin{equation}
\mathbf{\text{NA} \approx n_1 \sqrt{2\Delta} = 1.48 \sqrt{2(0.012)} = 1.48 \sqrt{0.024} = 1.48(0.1549) \approx 0.2293}
\end{equation}

\textbf{2. $V$-Number at $\lambda = 1300\text{ nm} = 1.3\,\mu\text{m}$}:
\begin{equation}
\mathbf{V = \frac{2\pi a}{\lambda}\text{NA} = \frac{2\pi (30\,\mu\text{m})}{1.3\,\mu\text{m}}(0.2293) = \frac{188.5}{1.3}(0.2293) \approx 33.25}
\end{equation}

\textbf{3. Total Guided Modes $M_{\text{GRIN}}$}:
\begin{equation}
\mathbf{M_{\text{GRIN}} \approx \frac{V^2}{4} = \frac{(33.25)^2}{4} = \frac{1105.56}{4} \approx 276\text{ modes}}
\end{equation}

\textbf{4. Pulse Broadening Comparison}:
\begin{itemize}
    \item \textbf{Graded-Index (GRIN) Fiber}:
    \begin{equation}
    \mathbf{\frac{\Delta\tau_{\text{GRIN}}}{L} \approx \frac{n_1 \Delta^2}{2 c} = \frac{1.48(0.012)^2}{2(3 \times 10^8)} = \frac{1.48(1.44 \times 10^{-4})}{6 \times 10^8} \approx 3.55 \times 10^{-13}\text{ s/m} = 0.355\text{ ns/km}}
    \end{equation}
    \item \textbf{Step-Index (SI) Fiber}:
    \begin{equation}
    \mathbf{\frac{\Delta\tau_{\text{SI}}}{L} \approx \frac{n_1 \Delta}{c} = \frac{1.48(0.012)}{3 \times 10^8} = 5.92 \times 10^{-11}\text{ s/m} = 59.2\text{ ns/km}}
    \end{equation}
    \item \textbf{Ratio}:
    \begin{equation}
    \frac{\Delta\tau_{\text{SI}}}{\Delta\tau_{\text{GRIN}}} = \frac{59.2}{0.355} \approx \mathbf{167\times \text{ bandwidth improvement!}}
    \end{equation}
\end{itemize}"""
        ),
        (
            r"Explain the physical principles and differences between: (a) Fusion Splicing and Mechanical Splicing of optical fibers, and (b) Intrinsic vs Extrinsic fiber optic sensors.",
            r"""\textbf{1. Fusion vs. Mechanical Splicing}:
\begin{itemize}
    \item \textbf{Fusion Splicing}:
    \begin{itemize}
        \item Two cleanly cleaved fiber ends are precisely aligned using core-imaging camera systems.
        \item An automated electric arc melts and fuses the glass ends permanently into a seamless monolithic joint.
        \item Insertion loss is exceptionally low ($< 0.02\text{ dB}$); back-reflection is virtually zero ($< -60\text{ dB}$).
        \item Standard permanent method for outdoor long-haul telecommunication cables.
    \end{itemize}
    \item \textbf{Mechanical Splicing}:
    \begin{itemize}
        \item Two cleaved fibers are inserted into a precision V-groove mechanical alignment sleeve containing index-matching optical gel.
        \item Clamped mechanically without melting.
        \item Insertion loss is higher ($\approx 0.1\text{--}0.2\text{ dB}$).
        \item Used for rapid emergency repairs and indoor FTTH installations where fusion equipment is unavailable.
    \end{itemize}
\end{itemize}

\textbf{2. Intrinsic vs. Extrinsic Fiber Optic Sensors}:
\begin{itemize}
    \item \textbf{Intrinsic Sensors}:
    The optical fiber itself acts as the sensing element. Environmental physical parameters (strain, pressure, temperature, acoustic fields) modulate the optical properties inside the fiber core directly (e.g., Fiber Bragg Gratings, microbending sensors, distributed Raman/Brillouin temperature sensors).
    \item \textbf{Extrinsic Sensors}:
    The optical fiber serves exclusively as an optical conduit (light pipe) to transport light to an external non-fiber sensing transducer and collect the modulated light back to the detector (e.g., optical displacement probes, laser Doppler velocimeters, turbidity sensors).
\end{itemize}"""
        ),
        (
            r"Derive the formula for Rayleigh scattering attenuation in optical fibers. Explain why Rayleigh scattering imposes a fundamental lower limit on optical fiber transmission loss.",
            r"""\textbf{1. Microscopic Origin}:
Silica glass is an amorphous solid formed by cooling molten silica through its glass transition temperature $T_f \approx 1400\text{ K}$.
Thermodynamic density and compositional fluctuations frozen into the glass matrix produce microscopic variations in dielectric constant $\delta\epsilon$ on a scale much smaller than optical wavelength ($d \ll \lambda$).

\textbf{2. Mathematical Derivation}:
Applying dipole scattering theory, each localized fluctuation acts as an oscillating electric dipole radiating scattered power:
\begin{equation}
P_{\text{scattered}} = \frac{\omega^4 p_0^2}{12\pi \epsilon_0 c^3} \propto \frac{1}{\lambda^4}
\end{equation}
Integrating the scattering cross section over all solid angles yields the turbidity/attenuation coefficient:
\begin{equation}
\mathbf{\alpha_{\text{Rayleigh}} = \frac{8\pi^3}{3\lambda^4}(n^8 p^2)(k_B T_f \beta_T)}
\end{equation}
where:
\begin{itemize}
    \item $n$: Refractive index of fused silica ($1.458$).
    \item $p$: Average photoelastic coefficient ($0.286$).
    \item $k_B$: Boltzmann constant ($1.38 \times 10^{-23}\text{ J/K}$).
    \item $T_f$: Fictive (glass freeze-in) temperature ($\approx 1400\text{ K}$).
    \item $\beta_T$: Isothermal compressibility of silica ($7 \times 10^{-11}\text{ m}^2/\text{N}$).
\end{itemize}

\textbf{3. Fundamental Physical Limit}:
Because thermal fluctuations are an unavoidable thermodynamic property of any liquid-quenched amorphous glass, Rayleigh scattering cannot be eliminated by chemical purification.
At $\lambda = 1550\text{ nm}$, $\alpha_{\text{Rayleigh}} \approx 0.15\text{ dB/km}$. Combined with the infrared multiphonon absorption edge, this establishes the immutable physical floor for silica fiber transmission loss at \textbf{$\approx 0.15\text{--}0.18\text{ dB/km}$ at $1550\text{ nm}$.}"""
        ),
        (
            r"Discuss the operating principle and classification of Photonic Crystal Fibers (PCFs). Compare Index-Guiding PCFs with Photonic Bandgap Hollow-Core PCFs.",
            r"""\textbf{1. Photonic Crystal Fiber (PCF) Concept}:
Photonic Crystal Fibers (microstructured fibers) possess a silica cladding perforated by a 2D periodic array of microscopic longitudinal air holes (diameter $d$, pitch $\Lambda$).

\textbf{2. Classification}:
\begin{enumerate}
    \item \textbf{Index-Guiding PCF (Solid-Core)}:
    \begin{itemize}
        \item \textit{Structure}: A solid silica core surrounded by a microstructured air-hole cladding.
        \item \textit{Guidance}: Operates via Modified Total Internal Reflection (M-TIR). The presence of air holes lowers the average effective cladding index ($n_{\text{cl,eff}} < n_{\text{core}} = n_{\text{silica}}$).
        \item \textit{Unique Properties}: \textbf{Endlessly single-mode} operation across all wavelengths from $300\text{ nm}$ to $2000\text{ nm}$ if hole-to-pitch ratio $d/\Lambda \le 0.45$.
    \end{itemize}
    \item \textbf{Photonic Bandgap Fiber (Hollow-Core PCF)}:
    \begin{itemize}
        \item \textit{Structure}: A hollow air/vacuum core surrounded by a strictly periodic triangular air-hole lattice.
        \item \textit{Guidance}: Operates via the Photonic Bandgap (PBG) effect. The cladding acts as a 2D photonic crystal that forbids light of specific frequencies from propagating radially, trapping light inside the lower-index hollow core.
        \item \textit{Unique Properties}: $99.9\%$ of optical energy travels in air/vacuum.
    \end{itemize}
\end{enumerate}

\textbf{3. Key Advantages of Hollow-Core PCFs}:
\begin{itemize}
    \item \textbf{Ultra-Low Latency}: Speed of light in vacuum core is $c$, reducing transmission latency by $30\%$ ($3.33\,\mu\text{s/km}$ vs $4.88\,\mu\text{s/km}$ in silica).
    \item \textbf{Ultra-High Damage Threshold}: Absence of solid glass eliminates non-linear effects (Kerr SPM/XPM) and permits megawatt high-power laser beam delivery.
\end{itemize}"""
        ),
        (
            r"A step-index fiber of length $25\text{ km}$ has $n_1 = 1.470$ and $n_2 = 1.465$ with core diameter $8.0\,\mu\text{m}$. Calculate: (a) Numerical aperture, (b) single-mode cutoff wavelength $\lambda_c$, (c) $V$-number at $1550\text{ nm}$, (d) mode field diameter at $1550\text{ nm}$ using Marcuse formula ($w/a \approx 0.65 + 1.619 V^{-1.5} + 2.879 V^{-6}$), and (e) total pulse broadening if $D = 18\text{ ps/(nm}\cdot\text{km)}$ and source linewidth is $0.05\text{ nm}$.",
            r"""\textbf{1. Numerical Aperture ($\text{NA}$)}:
\begin{equation}
\mathbf{\text{NA} = \sqrt{n_1^2 - n_2^2} = \sqrt{1.470^2 - 1.465^2} = \sqrt{2.1609 - 2.146225} = \sqrt{0.014675} \approx 0.1211}
\end{equation}

\textbf{2. Cutoff Wavelength $\lambda_c$}:
Core radius $a = 4.0\,\mu\text{m} = 4 \times 10^{-6}\text{ m}$.
\begin{equation}
\mathbf{\lambda_c = \frac{2\pi a \text{NA}}{2.405} = \frac{2\pi (4.0\,\mu\text{m})(0.1211)}{2.405} = \frac{3.0436}{2.405} \approx 1.265\,\mu\text{m} = 1265\text{ nm}}
\end{equation}

\textbf{3. $V$-Number at $\lambda = 1550\text{ nm}$}:
\begin{equation}
\mathbf{V = \frac{2\pi a}{\lambda}\text{NA} = \frac{2\pi (4.0)}{1.55}(0.1211) = \frac{3.0436}{1.55} \approx 1.9636}
\end{equation}
Since $V = 1.964 < 2.405$, the fiber is strictly single-mode at $1550\text{ nm}$.

\textbf{4. Mode Field Diameter (MFD)}:
Using the Marcuse empirical equation:
\begin{align*}
\frac{w}{a} &= 0.65 + 1.619(1.9636)^{-1.5} + 2.879(1.9636)^{-6} \\
&= 0.65 + 1.619(0.3637) + 2.879(0.0175) = 0.65 + 0.5888 + 0.0504 \approx 1.2892 \\
w &= 1.2892 \times 4.0\,\mu\text{m} \approx 5.157\,\mu\text{m} \\
\mathbf{\text{MFD}} &= 2w \approx 2(5.157\,\mu\text{m}) \approx \mathbf{10.31\,\mu\text{m}}
\end{align*}

\textbf{5. Chromatic Pulse Broadening}:
\begin{equation}
\mathbf{\Delta\tau = |D| \cdot L \cdot \Delta\lambda = (18\text{ ps/(nm}\cdot\text{km)}) \times (25\text{ km}) \times (0.05\text{ nm}) = 22.5\text{ ps}}
\end{equation}"""
        ),
        (
            r"Explain the principle and operation of Optical Time Domain Reflectometry (OTDR). Detail how an OTDR trace identifies and quantifies fiber attenuation slope, fusion splice losses, connector reflections, and fiber break locations.",
            r"""\textbf{1. Principle of Operation}:
An Optical Time Domain Reflectometer (OTDR) is an advanced optoelectronic instrument used to diagnose and characterize fiber optic links non-destructively from a single end.
\begin{itemize}
    \item High-power, narrow optical laser pulses are injected periodically into the fiber under test via a directional optical coupler.
    \item As the pulse propagates, Rayleigh backscattering and Fresnel reflections return light back toward the instrument.
    \item An avalanche photodiode (APD) records the returning optical power as a function of time delay $t$.
    \item Distance $z$ along the fiber is determined from time-of-flight:
    \begin{equation}
    \mathbf{z = \frac{c \cdot t}{2 n_{\text{group}}}}
    \end{equation}
    where factor of 2 accounts for the two-way round-trip transit.
\end{itemize}

\textbf{2. Interpretation of an OTDR Trace ($\text{dB}$ vs Distance $z$)}:
\begin{enumerate}
    \item \textbf{Continuous Downward Slope}: Represents uniform distributed Rayleigh backscattering loss along the fiber. The gradient equals the fiber attenuation coefficient $\alpha = -\frac{1}{2}\frac{d(\text{dB})}{dz}$ in $\text{dB/km}$.
    \item \textbf{Non-Reflective Step Drop}: Indicates a localized loss event without reflection, such as a fusion splice ($\approx 0.02\text{--}0.05\text{ dB}$) or a sharp macrobend.
    \item \textbf{Reflective Spike with Downward Step}: Caused by Fresnel reflection ($\approx 4\%$ glass-air reflection) at mechanical connectors, patch panels, or mechanical splices.
    \item \textbf{Large Final Reflective Spike followed by Noise Floor}: Marks the clean end-face of the fiber or a physical cable cut.
\end{enumerate}"""
        ),
        (
            r"Describe the nonlinear optical phenomena in fibers: (a) Four-Wave Mixing (FWM), (b) Self-Phase Modulation (SPM), and (c) Cross-Phase Modulation (XPM). Explain their impact on DWDM optical networks.",
            r"""\textbf{1. Nonlinear Refractive Index (Kerr Effect)}:
At high optical power densities inside the microscopic core ($A_{\text{eff}} \approx 50\text{--}80\,\mu\text{m}^2$), silica exhibits third-order optical susceptibility $\chi^{(3)}$, producing an intensity-dependent refractive index:
\begin{equation}
n(I) = n_0 + n_2 I = n_0 + n_2 \left(\frac{P}{A_{\text{eff}}}\right)
\end{equation}
where $n_2 \approx 2.6 \times 10^{-20}\text{ m}^2/\text{W}$ is the nonlinear Kerr index.

\textbf{2. Key Nonlinear Phenomena}:
\begin{enumerate}
    \item \textbf{Self-Phase Modulation (SPM)}:
    An intense optical pulse's own intensity profile $I(t)$ modulates its phase: $\phi_{\text{NL}}(t) = -\gamma P(t) z$. This generates new frequencies (chirp), broadening the pulse spectrum and accelerating dispersion degradation.
    \item \textbf{Cross-Phase Modulation (XPM)}:
    In multi-channel DWDM systems, the intensity fluctuations of a pulse on wavelength $\lambda_1$ modulate the nonlinear phase of overlapping pulses on adjacent wavelengths $\lambda_2$, producing inter-channel timing jitter and spectral distortion.
    \item \textbf{Four-Wave Mixing (FWM)}:
    Three optical frequencies ($\nu_i, \nu_j, \nu_k$) interact via third-order susceptibility to generate a fourth phantom frequency:
    \begin{equation}
    \nu_{\text{new}} = \nu_i + \nu_j - \nu_k
    \end{equation}
    If channels are uniformly spaced on a frequency grid and chromatic dispersion is near zero, $\nu_{\text{new}}$ coincides exactly with an existing data channel, causing severe coherent cross-talk.
\end{enumerate}

\textbf{3. Network Mitigation Strategies}:
\begin{itemize}
    \item Using Non-Zero Dispersion-Shifted Fibers (NZ-DSF) with small non-zero dispersion ($D \approx 3\text{ ps/(nm}\cdot\text{km)}$) to break the phase-matching condition for FWM.
    \item Enlarging fiber effective core area ($A_{\text{eff}} > 100\,\mu\text{m}^2$) to reduce optical power intensity.
    \item Implementing digital non-linear compensation algorithms in coherent DSP receivers.
\end{itemize}"""
        ),
        (
            r"A step-index single-mode fiber with core index $n_1 = 1.465$ and $n_2 = 1.460$ is used in a communication link at $1550\text{ nm}$. The core radius is $a = 4.2\,\mu\text{m}$. Calculate: (a) Numerical aperture, (b) $V$-number, (c) fractional power in the core using Gloge's formula ($P_{\text{core}}/P_{\text{total}} \approx 1 - V^{-2}$), and (d) explain the trade-offs of choosing smaller vs larger core radius in telecom fibers.",
            r"""\textbf{1. Numerical Aperture ($\text{NA}$)}:
\begin{equation}
\mathbf{\text{NA} = \sqrt{1.465^2 - 1.460^2} = \sqrt{2.146225 - 2.1316} = \sqrt{0.014625} \approx 0.1209}
\end{equation}

\textbf{2. $V$-Number at $\lambda = 1550\text{ nm} = 1.55\,\mu\text{m}$}:
\begin{equation}
\mathbf{V = \frac{2\pi a}{\lambda}\text{NA} = \frac{2\pi (4.2\,\mu\text{m})}{1.55\,\mu\text{m}}(0.1209) = \frac{26.389}{1.55}(0.1209) \approx 2.058}
\end{equation}
Since $V = 2.058 < 2.405$, the fiber is confirmed to operate in the single-mode regime.

\textbf{3. Fractional Power in Core ($P_{\text{core}}/P_{\text{total}}$)}:
Using Gloge's power distribution approximation for single-mode fibers:
\begin{equation}
\mathbf{\frac{P_{\text{core}}}{P_{\text{total}}} \approx 1 - V^{-2} = 1 - (2.058)^{-2} = 1 - \frac{1}{4.235} = 1 - 0.2361 = 0.7639 \approx 76.4\%}
\end{equation}
Thus, $\approx 76.4\%$ of optical power propagates inside the physical core, while $\approx 23.6\%$ travels in the cladding as an evanescent wave.

\textbf{4. Engineering Trade-Offs}:
\begin{itemize}
    \item \textbf{Smaller Core Radius ($a < 4\,\mu\text{m}$)}:
    Increases cutoff wavelength safety margin ($V \ll 2.405$), but expands the evanescent field deeper into cladding, increasing macrobending/microbending sensitivity and reducing effective area $A_{\text{eff}}$, which increases non-linear distortions (SPM/XPM).
    \item \textbf{Larger Core Radius ($a > 5\,\mu\text{m}$)}:
    Increases effective area ($A_{\text{eff}} \approx 100\,\mu\text{m}^2$) and coupling tolerance, but risks multi-mode operation ($V > 2.405$) if $\lambda$ drops below cutoff.
\end{itemize}"""
        ),
        (
            r"Derive the pulse spreading relation for polarization mode dispersion (PMD) in single-mode fibers. Explain the random walk model $\Delta \tau_{\text{PMD}} = D_{\text{PMD}}\sqrt{L}$ and methods for PMD compensation.",
            r"""\textbf{1. Physical Origin}:
A real single-mode fiber does not possess perfectly cylindrical symmetry. Minor mechanical stress, thermal gradients, and geometric core ellipticity induce modal birefringence $B = |n_x - n_y|$.
The fundamental $\text{HE}_{11}$ mode splits into two orthogonal polarization eigenstates traveling at slightly different phase and group velocities.

\textbf{2. Random Walk Model}:
In short fibers ($L < L_{\text{coupling}} \sim 100\text{ m}$), differential group delay (DGD) accumulates linearly: $\Delta\tau = \frac{L \Delta n_g}{c}$.
Over long transmission fibers ($L \gg 1\text{ km}$), random perturbations cause continuous polarization mode coupling (random cross-talk between axes).
The differential group delay accumulates as a 1D statistical random walk:
\begin{equation}
\mathbf{\langle \Delta \tau_{\text{PMD}} \rangle = D_{\text{PMD}} \sqrt{L}}
\end{equation}
where $D_{\text{PMD}}$ is the PMD parameter (in $\text{ps}/\sqrt{\text{km}}$) and $L$ is fiber link length.

\textbf{3. Bit Rate Limitation}:
To ensure bit error rate $\text{BER} < 10^{-12}$, the mean DGD must not exceed $10\%$ of the bit slot period $T_b$:
\begin{equation}
\langle \Delta \tau_{\text{PMD}} \rangle \le 0.10 T_b = \frac{0.10}{B} \implies \mathbf{B_{\text{max}} \le \frac{0.10}{D_{\text{PMD}}\sqrt{L}}}
\end{equation}

\textbf{4. PMD Compensation}:
\begin{itemize}
    \item \textbf{Optical PMD Compensators}: Dynamic polarization controllers followed by variable differential delay lines that apply inverse DGD.
    \item \textbf{Coherent Digital Signal Processing (DSP)}: Digital equalization using $2 \times 2$ adaptive MIMO (Multiple-Input Multiple-Output) butterfly FIR filters that track and cancel polarization rotations in real-time.
\end{itemize}"""
        ),
        (
            r"Summarize the complete international standards for optical telecommunication fibers (ITU-T G.652, G.653, G.655, G.657). Explain the unique structural specifications and target deployment applications for each fiber class.",
            r"""\textbf{1. ITU-T G.652 (Standard Single-Mode Fiber / SSMF)}:
\begin{itemize}
    \item \textbf{Specifications}: Core diameter $\approx 8.2\text{--}9.0\,\mu\text{m}$, cladding $125\,\mu\text{m}$. Zero dispersion at $\lambda_0 \approx 1310\text{ nm}$; dispersion at $1550\text{ nm}$ is $+17\text{ ps/(nm}\cdot\text{km)}$.
    \item \textbf{G.652.D (Low Water Peak)}: Eliminates the $\text{OH}^-$ absorption peak at $1383\text{ nm}$, opening the entire spectrum from $1260\text{ nm}$ to $1625\text{ nm}$ (Full-Spectrum CWDM).
    \item \textbf{Application}: Global backbone terrestrial networks and metropolitan area networks.
\end{itemize}

\textbf{2. ITU-T G.653 (Dispersion-Shifted Fiber / DSF)}:
\begin{itemize}
    \item \textbf{Specifications}: Zero dispersion wavelength shifted to $\lambda_0 = 1550\text{ nm}$, coinciding with lowest loss ($0.2\text{ dB/km}$).
    \item \textbf{Limitation}: Severe Four-Wave Mixing (FWM) under multi-channel DWDM.
    \item \textbf{Application}: Legacy single-channel long-haul links.
\end{itemize}

\textbf{3. ITU-T G.655 (Non-Zero Dispersion-Shifted Fiber / NZ-DSF)}:
\begin{itemize}
    \item \textbf{Specifications}: Maintains a small, strictly non-zero chromatic dispersion ($2\text{--}6\text{ ps/(nm}\cdot\text{km)}$) across the entire C-band ($1530\text{--}1565\text{ nm}$).
    \item \textbf{Application}: High-capacity DWDM submarine and terrestrial backbone transmission, suppressing FWM.
\end{itemize}

\textbf{4. ITU-T G.657 (Bend-Insensitive Single-Mode Fiber)}:
\begin{itemize}
    \item \textbf{Specifications}: Uses high $\Delta$ or a nano-engineered refractive index trench around the core to reduce minimum bend radius down to $R = 7.5\text{ mm}$ (G.657.A) and $R = 5.0\text{ mm}$ (G.657.B) with negligible bend loss.
    \item \textbf{Application}: Fiber-to-the-Home (FTTH) indoor drop cables, data center high-density routing, and tight building corners.
\end{itemize}"""
        )
    ]
    
    return unit_num, unit_title, mcqs, theory_qs
