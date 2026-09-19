# generate_physics_qb_u2.py
# -*- coding: utf-8 -*-

def get_unit_2_content():
    unit_num = 2
    unit_title = "Lasers and Applications"
    
    mcqs = [
        # Part I: Foundational (1-50)
        (
            r"The acronym LASER stands for:",
            r"Light Amplification by Stimulated Emission of Radiation",
            r"Light Absorption by Stimulated Energy Radiation",
            r"Linear Amplification of Spectral Electromagnetic Rays",
            r"Light Alteration by Synchronous Emission of Rays",
            "(a)",
            r"LASER is the standard acronym for Light Amplification by Stimulated Emission of Radiation."
        ),
        (
            r"In spontaneous emission, the emitted photon has:",
            r"The exact same phase, polarization, and direction as the incident photon",
            r"Random phase, random direction, and random polarization",
            r"A frequency double that of the incident radiation",
            r"Strictly zero quantum energy",
            "(b)",
            r"Spontaneous emission occurs randomly and independently without external electromagnetic phase correlation."
        ),
        (
            r"In stimulated emission, the emitted photon and incident trigger photon are:",
            r"Oppositely directed with opposite phases",
            r"Identical in frequency, phase, direction of propagation, and polarization state",
            r"Orthogonal in polarization with a $\pi/2$ phase shift",
            r"Separated by a half-integer quantum number",
            "(b)",
            r"Stimulated emission generates a replica photon that is identical in phase, frequency, direction, and polarization (quantum coherence)."
        ),
        (
            r"Einstein's $A_{21}$ coefficient represents the probability per unit time for:",
            r"Induced absorption ($1 \to 2$)",
            r"Spontaneous emission ($2 \to 1$)",
            r"Stimulated emission ($2 \to 1$)",
            r"Non-radiative phonon decay",
            "(b)",
            r"Einstein $A_{21}$ is the transition probability per unit time for spontaneous radiative decay from level 2 to level 1."
        ),
        (
            r"Einstein's $B_{12}$ and $B_{21}$ coefficients for non-degenerate states satisfy the fundamental relation:",
            r"$B_{12} > B_{21}$",
            r"$B_{12} = B_{21}$",
            r"$B_{12} < B_{21}$",
            r"$B_{12} B_{21} = 1$",
            "(b)",
            r"Microscopic time-reversal symmetry requires equal transition probabilities for absorption and stimulated emission: $B_{12} = B_{21}$."
        ),
        (
            r"The ratio of Einstein's coefficients $A_{21} / B_{21}$ in free space is given by:",
            r"$\frac{8\pi h \nu^3}{c^3}$",
            r"$\frac{8\pi h \nu^2}{c^2}$",
            r"$\frac{4\pi h \nu}{c}$",
            r"$\frac{h \nu}{c^2}$",
            "(a)",
            r"Comparing the rate equation balance with Planck's blackbody radiation law yields $A_{21}/B_{21} = 8\pi h \nu^3 / c^3$."
        ),
        (
            r"The ratio of stimulated emission rate to spontaneous emission rate in thermal equilibrium at temperature $T$ is:",
            r"$e^{h\nu/k_BT} - 1$",
            r"$\frac{1}{e^{h\nu/k_BT} - 1}$",
            r"$\frac{1}{e^{h\nu/k_BT} + 1}$",
            r"$e^{-h\nu/k_BT}$",
            "(b)",
            r"$\frac{R_{\text{stim}}}{R_{\text{spont}}} = \frac{B_{21} u(\nu)}{A_{21}} = \frac{1}{e^{h\nu/k_BT} - 1}$."
        ),
        (
            r"For visible light ($\lambda \approx 500\text{ nm}$) at room temperature ($T = 300\text{ K}$), $h\nu \gg k_BT$. This implies:",
            r"Stimulated emission dominates overwhelmingly",
            r"Spontaneous emission dominates overwhelmingly ($R_{\text{spont}} \gg R_{\text{stim}}$)",
            r"Both rates are exactly equal",
            r"No atomic transitions can occur",
            "(b)",
            r"At optical frequencies at $300\text{ K}$, $h\nu/k_BT \approx 100$, so $e^{100} \ggg 1$ and spontaneous emission completely dominates thermal systems."
        ),
        (
            r"A state of 'population inversion' between two energy levels $E_2 > E_1$ means:",
            r"$N_2 = N_1$",
            r"$N_2 > N_1$",
            r"$N_2 < N_1$",
            r"$N_2 = 0$",
            "(b)",
            r"Population inversion is the non-equilibrium condition where the higher energy state has a greater population of atoms than the lower state ($N_2 > N_1$)."
        ),
        (
            r"Why is a 'metastable state' essential for achieving population inversion in a laser medium?",
            r"It has an extremely short lifetime ($\approx 10^{-12}\text{ s}$)",
            r"It has an unusually long radiative lifetime ($\approx 10^{-3}\text{ s}$), allowing atoms to accumulate in large numbers",
            r"It emits gamma rays exclusively",
            r"It prevents any stimulated emission from occurring",
            "(b)",
            r"Metastable states possess lifetimes $10^5$ times longer than ordinary excited states ($\sim 10^{-3}\text{ s}$ vs $10^{-8}\text{ s}$), enabling atomic storage."
        ),
        (
            r"The process of supplying external energy to achieve population inversion in an active medium is called:",
            r"Doping",
            r"Pumping",
            r"Quenching",
            r"Sputtering",
            "(b)",
            r"Pumping is the excitation process that raises ground-state atoms to higher energy levels to maintain population inversion."
        ),
        (
            r"Optical pumping using intense flashlamps is the standard excitation method employed in:",
            r"Helium-Neon (He-Ne) gas lasers",
            r"Ruby and Nd:YAG solid-state lasers",
            r"Carbon Dioxide ($\text{CO}_2$) lasers",
            r"Semiconductor diode lasers",
            "(b)",
            r"Solid-state lasers (such as Ruby and Nd:YAG) use optical pumping from xenon flashlamps or laser diode arrays."
        ),
        (
            r"Electric discharge pumping via inelastic electron impact collisions is primarily used in:",
            r"Ruby lasers",
            r"Gas lasers like He-Ne and $\text{CO}_2$",
            r"Dye lasers",
            r"Glass lasers",
            "(b)",
            r"Gas lasers are pumped by passing high-voltage electric discharges through the low-pressure gas mixture."
        ),
        (
            r"An optical resonator cavity in a laser consists of:",
            r"A single convex lens and a prism",
            r"A pair of parallel aligned mirrors (one $100\%$ reflecting, one partially transmitting output coupler)",
            r"A diffraction grating enclosed in a magnetic solenoid",
            r"A photodiode and a fiber splitter",
            "(b)",
            r"An optical cavity uses a high-reflectivity mirror ($R_1 \approx 100\%$) and an output coupler ($R_2 \approx 95\text{--}99\%$) to provide positive optical feedback."
        ),
        (
            r"The standing wave condition for an optical cavity of length $L$ with refractive index $n$ is:",
            r"$L = m \frac{\lambda}{2n} \quad (m = 1, 2, 3,\dots)$",
            r"$L = m \lambda$",
            r"$L = (2m+1)\frac{\lambda}{4}$",
            r"$L = \frac{c}{2\nu}$",
            "(a)",
            r"Constructive interference requires an integer number of half-wavelengths to fit the cavity: $2nL = m\lambda \implies L = m\lambda/(2n)$."
        ),
        (
            r"The frequency spacing $\Delta \nu$ between two adjacent longitudinal cavity modes in a laser of length $L$ (in vacuum) is:",
            r"$\Delta \nu = \frac{c}{L}$",
            r"$\Delta \nu = \frac{c}{2L}$",
            r"$\Delta \nu = \frac{2c}{L}$",
            r"$\Delta \nu = \frac{c}{4L}$",
            "(b)",
            r"$\nu_m = \frac{m c}{2L} \implies \Delta\nu = \nu_{m+1} - \nu_m = \frac{c}{2L}$."
        ),
        (
            r"In a 3-level laser system (like the Ruby laser), the ground state is also:",
            r"The lower laser level $E_1$",
            r"The upper laser level $E_2$",
            r"The pump level $E_3$",
            r"A non-existent state",
            "(a)",
            r"In a 3-level system, the lower lasing state is the ground state itself, requiring more than $50\%$ of all atoms to be excited to achieve inversion."
        ),
        (
            r"Why is a 4-level laser (like He-Ne or Nd:YAG) much more energy efficient than a 3-level laser?",
            r"The lower laser level $E_2$ lies above the ground state and is rapidly depopulated thermally ($N_2 \approx 0$ initially)",
            r"It emits at four different colors simultaneously",
            r"It uses no optical mirrors",
            r"It does not require any pumping",
            "(a)",
            r"In a 4-level laser, level 2 is naturally empty at equilibrium ($N_2 \approx 0$). Pumping even a few atoms into level 3 creates population inversion ($N_3 > N_2$)."
        ),
        (
            r"The active medium in a Ruby laser consists of:",
            r"Pure liquid ruby",
            r"$\text{Al}_2\text{O}_3$ (sapphire crystal) doped with $\approx 0.05\%\text{ Cr}^{3+}$ (chromium ions)",
            r"Gallium Arsenide",
            r"Helium-Neon gas mix",
            "(b)",
            r"The active lasing ions in a ruby laser are chromium ions ($\text{Cr}^{3+}$) embedded in a host corundum ($\text{Al}_2\text{O}_3$) crystal lattice."
        ),
        (
            r"The emission wavelength of a Ruby laser is in the visible red spectrum at:",
            r"$532.0\text{ nm}$",
            r"$632.8\text{ nm}$",
            r"$694.3\text{ nm}$",
            r"$1064.0\text{ nm}$",
            "(c)",
            r"The $^2E \to ^4A_2$ transition in $\text{Cr}^{3+}$ produces laser emission at $694.3\text{ nm}$."
        ),
        (
            r"In a Helium-Neon (He-Ne) gas laser, the ratio of Helium to Neon gas in the tube is typically:",
            r"$1:1$",
            r"$10:1$",
            r"$1:10$",
            r"$100:1$",
            "(b)",
            r"The gas mixture is maintained at approximately $10:1$ (or $7:1$ to $10:1$) He to Ne at low pressure ($\sim 1\text{ Torr}$)."
        ),
        (
            r"In a He-Ne laser, the primary role of Helium atoms is to:",
            r"Directly emit the red laser light",
            r"Absorb electrical discharge energy and transfer it to Neon atoms via resonant collision",
            r"Cool down the discharge tube walls",
            r"Act as optical reflectors",
            "(b)",
            r"Helium atoms are excited to metastable states $2^1S$ and $2^3S$ by electron collision and transfer energy to Neon levels $3s$ and $2s$ by resonant collisions."
        ),
        (
            r"The most common visible output transition in a He-Ne laser occurs at:",
            r"$694.3\text{ nm}$ (deep red)",
            r"$632.8\text{ nm}$ (bright red)",
            r"$532.0\text{ nm}$ (green)",
            r"$10.6\,\mu\text{m}$ (infrared)",
            "(b)",
            r"The $3s_2 \to 2p_4$ transition in Neon atoms produces the famous $632.8\text{ nm}$ red laser line."
        ),
        (
            r"The output beam of a He-Ne laser is characterized as:",
            r"Pulsed with gigawatt peak powers",
            r"Continuous Wave (CW) with exceptional spatial and temporal coherence",
            r"Ultraviolet polychromatic emission",
            r"Thermal white light",
            "(b)",
            r"He-Ne lasers operate in continuous wave (CW) mode with high beam directionality and long coherence lengths."
        ),
        (
            r"The active medium in a semiconductor diode laser is:",
            r"A direct bandgap p-n junction (such as GaAs)",
            r"An indirect bandgap silicon diode",
            r"A helium gas chamber",
            r"A neodymium crystal",
            "(a)",
            r"Semiconductor lasers require direct bandgap semiconductors (e.g., GaAs, InGaAsP) where radiative electron-hole recombination is efficient without phonons."
        ),
        (
            r"The optical feedback in a semiconductor diode laser is achieved by:",
            r"External curved concave dielectric mirrors",
            r"The naturally cleaved, polished end-facets of the semiconductor crystal",
            r"A mechanical chopper wheel",
            r"A quartz prism",
            "(b)",
            r"The high refractive index of GaAs ($n \approx 3.6$) provides $\sim 32\%$ Fresnel reflectance at each cleaved facet, serving as built-in cavity mirrors."
        ),
        (
            r"The laser emission wavelength $\lambda$ of a semiconductor diode laser is determined by its bandgap $E_g$ via:",
            r"$\lambda = \frac{h c}{E_g}$",
            r"$\lambda = \frac{E_g}{h c}$",
            r"$\lambda = \sqrt{\frac{h c}{E_g}}$",
            r"$\lambda = \frac{h}{E_g c}$",
            "(a)",
            r"Photons are emitted by direct band-to-band carrier recombination: $h\nu = E_g \implies \lambda = hc/E_g$."
        ),
        (
            r"The Nd:YAG laser operates as a:",
            r"2-level gas laser",
            r"3-level liquid dye laser",
            r"4-level solid-state laser emitting at $1064\text{ nm}$",
            r"1-level chemical laser",
            "(c)",
            r"Nd:YAG ($\text{Y}_3\text{Al}_5\text{O}_{12}:\text{Nd}^{3+}$) is a robust 4-level solid-state laser emitting near-infrared light at $1.064\,\mu\text{m}$ ($1064\text{ nm}$)."
        ),
        (
            r"The Carbon Dioxide ($\text{CO}_2$) laser generates high-power radiation in the far-infrared region at:",
            r"$632.8\text{ nm}$",
            r"$1.06\,\mu\text{m}$",
            r"$10.6\,\mu\text{m}$",
            r"$0.193\,\mu\text{m}$",
            "(c)",
            r"$\text{CO}_2$ lasers lase between quantized molecular vibrational-rotational energy states at $\lambda = 10.6\,\mu\text{m}$."
        ),
        (
            r"Coherence length $L_c$ is related to coherence time $\tau_c$ and spectral linewidth $\Delta \nu$ by:",
            r"$L_c = c \tau_c = \frac{c}{\Delta \nu}$",
            r"$L_c = \frac{c}{\tau_c} = c \Delta \nu$",
            r"$L_c = \tau_c / c$",
            r"$L_c = \frac{\Delta \nu}{c}$",
            "(a)",
            r"Coherence length is the spatial distance over which light maintains definite phase: $L_c = c\tau_c = c/\Delta\nu$."
        ),
        (
            r"The spatial divergence angle $\theta$ of a diffraction-limited laser beam of wavelength $\lambda$ and aperture diameter $D$ is proportional to:",
            r"$\theta \propto \frac{\lambda}{D}$",
            r"$\theta \propto \frac{D}{\lambda}$",
            r"$\theta \propto \lambda D$",
            r"$\theta \propto \frac{1}{\lambda D}$",
            "(a)",
            r"By Fraunhofer diffraction, the beam angular divergence is $\theta \approx 1.22 \lambda / D$, which is extremely small for lasers."
        ),
        (
            r"Holography was invented by Dennis Gabor and is fundamentally a technique for:",
            r"Recording 2D intensity distributions only",
            r"Recording and reconstructing both the amplitude and phase of an optical wavefront (full 3D image)",
            r"Thermal imaging in the dark",
            r"Measuring electrical conductivity of solids",
            "(b)",
            r"Holography records the complete optical wavefront (both amplitude and phase) through interference and reconstructs it via diffraction."
        ),
        (
            r"In the recording of a hologram, the photographic film records the interference pattern produced between:",
            r"Two incoherent white light bulbs",
            r"The scattered object beam and a coherent reference beam from the same laser source",
            r"The transmitted beam and a radio wave",
            r"An electron beam and an X-ray beam",
            "(b)",
            r"Interference between the scattered light from the 3D object and an unscattered reference beam forms the microscopic holographic fringes."
        ),
        (
            r"When a recorded transmission hologram is illuminated by the original reference laser beam, the reconstructed wavefront forms:",
            r"Only a 2D flat photograph",
            r"A virtual 3D image behind the plate and a real 3D image in front of the plate",
            r"A rainbow spectrum of colors",
            r"A single black-and-white shadow",
            "(b)",
            r"Diffraction of the reading beam creates a 3D virtual image (viewed by looking through the plate) and a conjugate real image."
        ),
        (
            r"Which key feature fundamentally distinguishes holography from conventional photography?",
            r"Photography records both amplitude and phase; holography records only intensity",
            r"Photography records 2D intensity only; holography records both amplitude and phase information to preserve true 3D depth and parallax",
            r"Photography requires coherent laser light; holography requires sunlight",
            r"Photography uses no lenses",
            "(b)",
            r"Conventional photos capture only 2D intensity ($I \propto |E|^2$), discarding phase; holograms encode phase via interferometry."
        ),
        (
            r"The Q-switching technique in lasers is used to generate:",
            r"Ultra-short laser pulses with exceptionally high peak power (megawatts to gigawatts)",
            r"Low-power continuous wave light",
            r"Multiple laser beams of different colors",
            r"Zero electromagnetic output",
            "(a)",
            r"Q-switching spoils the cavity quality factor $Q$ to store huge population inversion, then rapidly restores $Q$ to release a giant pulse."
        ),
        (
            r"Mode-locking in lasers produces periodic trains of ultra-short pulses in the time domain with durations on the order of:",
            r"Seconds to milliseconds",
            r"Microseconds",
            r"Picoseconds to femtoseconds ($10^{-12}\text{ s}$ to $10^{-15}\text{ s}$)",
            r"Minutes",
            "(c)",
            r"Mode-locking locks the phases of all longitudinal cavity modes, producing femtosecond/picosecond pulse trains."
        ),
        (
            r"In eye surgery (LASIK), which type of laser is used for precision corneal reshaping due to its non-thermal photoablation in the UV spectrum?",
            r"$\text{CO}_2$ laser",
            r"Ruby laser",
            r"Excimer laser (e.g., ArF at $193\text{ nm}$)",
            r"He-Ne laser",
            "(c)",
            r"Argon Fluoride (ArF) excimer lasers ($193\text{ nm}$ UV) break molecular bonds with sub-micron precision without thermal tissue damage."
        ),
        (
            r"The threshold gain coefficient $g_{\text{th}}$ for laser oscillation in a cavity of length $L$ with mirror reflectivities $R_1, R_2$ and distributed loss $\alpha_s$ is:",
            r"$g_{\text{th}} = \alpha_s + \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right)$",
            r"$g_{\text{th}} = \alpha_s - \frac{1}{L}\ln(R_1 R_2)$",
            r"$g_{\text{th}} = \frac{\alpha_s}{2L}\ln(R_1 R_2)$",
            r"$g_{\text{th}} = \alpha_s + 2L\ln(R_1 R_2)$",
            "(a)",
            r"Round-trip loop gain condition $R_1 R_2 e^{2(g_{\text{th}} - \alpha_s)L} = 1 \implies g_{\text{th}} = \alpha_s + \frac{1}{2L}\ln(1/(R_1 R_2))$."
        ),
        (
            r"In a He-Ne laser, the discharge tube is often fitted with Brewster angle windows at its ends to ensure that the output beam is:",
            r"Completely unpolarized",
            r"$100\%$ linearly polarized with zero reflection losses for p-polarized light",
            r"Circularly polarized",
            r"Deflected by $90^\circ$",
            "(b)",
            r"Brewster angle windows transmit p-polarized light with zero reflection loss, resulting in a strictly linearly polarized laser beam."
        ),
        (
            r"What type of laser transition occurs in the Semiconductor Diode Laser?",
            r"Electronic transitions between localized discrete ionic states",
            r"Interband transitions of electrons from conduction band to valence band",
            r"Vibrational transitions of symmetric stretch modes",
            r"Rotational transitions of diatomic molecules",
            "(b)",
            r"Recombination of conduction band electrons with valence band holes across the direct bandgap produces photon emission."
        ),
        (
            r"The active lasing ion in the Nd:YAG laser is:",
            r"$\text{Y}^{3+}$",
            r"$\text{Al}^{3+}$",
            r"$\text{Nd}^{3+}$ (Neodymium ion)",
            r"$\text{Cr}^{3+}$",
            "(c)",
            r"Neodymium ions ($\text{Nd}^{3+}$) substitute for Yttrium ($\text{Y}^{3+}$) ions in the host YAG crystal and undergo 4-level lasing transitions."
        ),
        (
            r"The beam waist $w_0$ of a Gaussian laser beam represents:",
            r"The position where beam diameter is maximum",
            r"The focal region where beam radius shrinks to its absolute minimum",
            r"The distance where power drops to zero",
            r"The mirror spacing in the laser head",
            "(b)",
            r"Beam waist $w_0$ is the location of minimum spot size along the propagation axis of a Gaussian laser beam."
        ),
        (
            r"The Rayleigh range $z_R$ of a Gaussian beam with beam waist $w_0$ is given by:",
            r"$z_R = \frac{\pi w_0^2}{\lambda}$",
            r"$z_R = \frac{\lambda}{\pi w_0^2}$",
            r"$z_R = \pi w_0 \lambda$",
            r"$z_R = \frac{2\lambda}{w_0}$",
            "(a)",
            r"The Rayleigh range $z_R = \pi w_0^2/\lambda$ is the distance over which the beam cross-sectional area doubles."
        ),
        (
            r"Which industrial process uses high-power $\text{CO}_2$ or fiber lasers for slicing thick steel plates?",
            r"Laser ablation",
            r"Laser cutting and welding",
            r"Laser annealing",
            r"Photolithography",
            "(b)",
            r"High-power $\text{CO}_2$ and fiber lasers provide focused multikilowatt thermal power for precision industrial metal cutting and welding."
        ),
        (
            r"A Helium-Neon laser has a coherence time $\tau_c = 10^{-8}\text{ s}$. Its coherence length $L_c$ is:",
            r"$0.3\text{ m}$",
            r"$3.0\text{ m}$",
            r"$30\text{ m}$",
            r"$300\text{ m}$",
            "(b)",
            r"$L_c = c \tau_c = (3 \times 10^8\text{ m/s})(10^{-8}\text{ s}) = 3.0\text{ m}$."
        ),
        (
            r"If a laser has an emission linewidth $\Delta \lambda = 0.002\text{ nm}$ at central wavelength $\lambda = 500\text{ nm}$, its coherence length $L_c$ is:",
            r"$1.25\text{ cm}$",
            r"$12.5\text{ cm}$",
            r"$1.25\text{ m}$",
            r"$12.5\text{ m}$",
            "(b)",
            r"$L_c \approx \frac{\lambda^2}{\Delta\lambda} = \frac{(500 \times 10^{-9})^2}{0.002 \times 10^{-9}} = \frac{2.5 \times 10^{-13}}{2 \times 10^{-12}} = 0.125\text{ m} = 12.5\text{ cm}$."
        ),
        (
            r"A laser resonator has a mirror cavity length $L = 30\text{ cm}$. The longitudinal mode spacing $\Delta \nu$ is:",
            r"$250\text{ MHz}$",
            r"$500\text{ MHz}$",
            r"$1000\text{ MHz}$ ($1\text{ GHz}$)",
            r"$1500\text{ MHz}$",
            "(b)",
            r"$\Delta \nu = \frac{c}{2L} = \frac{3 \times 10^8}{2 \times 0.30} = \frac{3 \times 10^8}{0.60} = 5 \times 10^8\text{ Hz} = 500\text{ MHz}$."
        ),
        (
            r"In a He-Ne laser, the transition that produces the $632.8\text{ nm}$ red laser line occurs between which energy levels of Neon?",
            r"$2s \to 2p$",
            r"$3s_2 \to 2p_4$",
            r"$3p \to 3s$",
            r"$1s \to 2s$",
            "(b)",
            r"The famous $632.8\text{ nm}$ line corresponds specifically to the $3s_2 \to 2p_4$ transition in the Paschen notation for Neon."
        ),
        (
            r"Why is the laser beam highly monochromatic compared to emission from a regular discharge lamp?",
            r"Because stimulated emission selectively amplifies only cavity-resonant frequencies within the narrow atomic gain profile",
            r"Because all other colors are absorbed by the glass walls",
            r"Because the laser uses a color filter",
            r"Because atoms only possess one single quantum energy level",
            "(a)",
            r"Repeated passes through the resonant cavity provide selective gain strictly to resonant standing-wave frequencies, narrowing the spectral linewidth."
        ),

        # Part II: Intermediate Analytical (51-80)
        (
            r"A laser cavity of length $L = 50\text{ cm}$ has a Doppler gain bandwidth $\Delta \nu_D = 1.5\text{ GHz}$ for its active medium. The maximum number of oscillating longitudinal modes is:",
            r"$3$",
            r"$5$",
            r"$10$",
            r"$15$",
            "(b)",
            r"Mode spacing $\Delta \nu = \frac{c}{2L} = \frac{3 \times 10^8}{2(0.5)} = 300\text{ MHz} = 0.3\text{ GHz}$. Number of modes $N \approx \frac{\Delta\nu_D}{\Delta\nu} = \frac{1.5}{0.3} = 5$."
        ),
        (
            r"A ruby laser rod has length $L = 10\text{ cm}$, scattering loss $\alpha_s = 0.05\text{ m}^{-1}$, and end mirrors with reflectivities $R_1 = 1.0$ and $R_2 = 0.85$. The threshold gain coefficient $g_{\text{th}}$ is:",
            r"$0.86\text{ m}^{-1}$",
            r"$0.91\text{ m}^{-1}$",
            r"$1.68\text{ m}^{-1}$",
            r"$2.15\text{ m}^{-1}$",
            "(a)",
            r"$g_{\text{th}} = \alpha_s + \frac{1}{2L}\ln\frac{1}{R_1 R_2} = 0.05 + \frac{1}{2(0.10)}\ln\frac{1}{0.85} = 0.05 + 5(0.1625) = 0.05 + 0.8125 \approx 0.8625\text{ m}^{-1}$."
        ),
        (
            r"A GaAs semiconductor laser has an energy bandgap $E_g = 1.424\text{ eV}$. The expected laser emission wavelength $\lambda$ is:",
            r"$632.8\text{ nm}$",
            r"$871\text{ nm}$",
            r"$1064\text{ nm}$",
            r"$1550\text{ nm}$",
            "(b)",
            r"$\lambda = \frac{hc}{E_g} = \frac{1240\text{ eV}\cdot\text{nm}}{1.424\text{ eV}} \approx 870.8\text{ nm} \approx 871\text{ nm}$."
        ),
        (
            r"If an InGaAsP semiconductor laser emits at $\lambda = 1550\text{ nm}$, the corresponding bandgap energy $E_g$ is:",
            r"$0.80\text{ eV}$",
            r"$1.12\text{ eV}$",
            r"$1.42\text{ eV}$",
            r"$2.10\text{ eV}$",
            "(a)",
            r"$E_g = \frac{hc}{\lambda} = \frac{1240\text{ eV}\cdot\text{nm}}{1550\text{ nm}} = 0.80\text{ eV}$."
        ),
        (
            r"A pulsed laser produces pulses of duration $\tau_p = 10\text{ ns}$ with energy $E_p = 50\text{ mJ}$ per pulse. The peak output power during each pulse is:",
            r"$5\text{ kW}$",
            r"$50\text{ kW}$",
            r"$5\text{ MW}$",
            r"$50\text{ MW}$",
            "(c)",
            r"$P_{\text{peak}} = \frac{E_p}{\tau_p} = \frac{50 \times 10^{-3}\text{ J}}{10 \times 10^{-9}\text{ s}} = 5 \times 10^6\text{ W} = 5\text{ MW}$."
        ),
        (
            r"If the pulsed laser in Question 55 operates at a pulse repetition rate of $20\text{ Hz}$, the average power output is:",
            r"$1.0\text{ W}$",
            r"$10\text{ W}$",
            r"$100\text{ W}$",
            r"$5\text{ mW}$",
            "(a)",
            r"$P_{\text{avg}} = E_p \times f_{\text{rep}} = (50 \times 10^{-3}\text{ J}) \times 20\text{ s}^{-1} = 1.0\text{ W}$."
        ),
        (
            r"A laser beam with $\lambda = 632.8\text{ nm}$ has an aperture diameter $D = 2\text{ mm}$. When projected onto the Moon ($d = 3.84 \times 10^8\text{ m}$), the angular spread produces a spot diameter of approximately:",
            r"$150\text{ m}$",
            r"$1.5\text{ km}$",
            r"$148\text{ km}$",
            r"$1480\text{ km}$",
            "(c)",
            r"$\theta \approx \frac{1.22\lambda}{D} = \frac{1.22(632.8 \times 10^{-9})}{2 \times 10^{-3}} \approx 3.86 \times 10^{-4}\text{ rad}$. Spot diameter $W = \theta d = (3.86 \times 10^{-4})(3.84 \times 10^8) \approx 1.48 \times 10^5\text{ m} = 148\text{ km}$."
        ),
        (
            r"The coherence length of a sodium discharge yellow line ($\lambda = 589\text{ nm}, \Delta\lambda = 0.01\text{ nm}$) is approximately:",
            r"$3.5\text{ cm}$",
            r"$35\text{ cm}$",
            r"$3.5\text{ m}$",
            r"$35\text{ m}$",
            "(a)",
            r"$L_c \approx \frac{\lambda^2}{\Delta\lambda} = \frac{(589 \times 10^{-9})^2}{10^{-11}} \approx \frac{3.47 \times 10^{-13}}{10^{-11}} = 0.0347\text{ m} \approx 3.5\text{ cm}$."
        ),
        (
            r"By comparison, a single-mode stabilized He-Ne laser with $\Delta \nu = 10\text{ kHz}$ has a coherence length $L_c$ of:",
            r"$30\text{ m}$",
            r"$300\text{ m}$",
            r"$3\text{ km}$",
            r"$30\text{ km}$",
            "(d)",
            r"$L_c = \frac{c}{\Delta\nu} = \frac{3 \times 10^8\text{ m/s}}{10^4\text{ Hz}} = 3 \times 10^4\text{ m} = 30\text{ km}$."
        ),
        (
            r"The population ratio $N_2/N_1$ between two atomic energy levels separated by $\Delta E = 2.0\text{ eV}$ in thermal equilibrium at $T = 300\text{ K}$ is ($k_B T \approx 0.0259\text{ eV}$):",
            r"$\approx 1.0$",
            r"$\approx 0.5$",
            r"$\approx 2.6 \times 10^{-34}$",
            r"$\approx 10^{-3}$",
            "(c)",
            r"$N_2/N_1 = e^{-\Delta E / k_BT} = e^{-2.0 / 0.0259} = e^{-77.2} \approx 2.6 \times 10^{-34}$, showing the upper level is practically unpopulated at room temperature."
        ),
        (
            r"In a 4-level laser, if level 2 (lower lasing level) has a lifetime $\tau_2$ and level 3 (upper lasing level) has lifetime $\tau_3$, sustained population inversion strictly requires:",
            r"$\tau_3 \gg \tau_2$",
            r"$\tau_3 \ll \tau_2$",
            r"$\tau_3 = \tau_2$",
            r"$\tau_2 = \infty$",
            "(a)",
            r"Level 3 must be long-lived (metastable) to store atoms, while level 2 must empty extremely rapidly ($\tau_2 \ll \tau_3$) to prevent bottleneck accumulation."
        ),
        (
            r"In a He-Ne laser, the lifetime of the Ne $3s_2$ level is $\approx 100\text{ ns}$ while that of the $2p_4$ level is $\approx 10\text{ ns}$. This condition guarantees:",
            r"Self-quenching of the beam",
            r"Continuous maintenance of population inversion ($N_3 > N_2$)",
            r"Inversion breakdown into pulsed operation",
            r"Absorption of emitted photons",
            "(b)",
            r"Since atoms leave the lower level $10\times$ faster than they arrive from above, population inversion is continuously sustained during CW operation."
        ),
        (
            r"The role of the small tube diameter (typically $1\text{--}2\text{ mm}$) in a He-Ne laser is to:",
            r"Reduce manufacturing costs",
            r"Enable fast de-excitation of Ne atoms from the $1s$ state to the ground state via tube wall collisions",
            r"Increase gas pressure to $100\text{ atm}$",
            r"Focus the electric discharge",
            "(b)",
            r"Neon atoms in the metastable $1s$ level must collide with tube walls to return to the ground state; a narrow bore ensures high wall-collision rates."
        ),
        (
            r"A laser beam focused by a lens of focal length $f = 10\text{ cm}$ with beam diameter $D = 5\text{ mm}$ at $\lambda = 1064\text{ nm}$ forms a spot radius $w_0$ of approximately:",
            r"$2.7\,\mu\text{m}$",
            r"$27\,\mu\text{m}$",
            r"$270\,\mu\text{m}$",
            r"$2.7\text{ mm}$",
            "(b)",
            r"$w_0 \approx \frac{4\lambda f}{\pi D} = \frac{4(1.064 \times 10^{-6})(0.10)}{\pi (5 \times 10^{-3})} = \frac{4.256 \times 10^{-7}}{0.0157} \approx 2.7 \times 10^{-5}\text{ m} = 27\,\mu\text{m}$."
        ),
        (
            r"If a $100\text{ W}$ continuous laser is focused to a spot of radius $w_0 = 25\,\mu\text{m}$, the power intensity at the focus is:",
            r"$5.1 \times 10^5\text{ W/m}^2$",
            r"$5.1 \times 10^7\text{ W/m}^2$",
            r"$5.1 \times 10^9\text{ W/m}^2$",
            r"$5.1 \times 10^{11}\text{ W/m}^2$",
            "(c)",
            r"$I = \frac{P}{\pi w_0^2} = \frac{100}{\pi (25 \times 10^{-6})^2} = \frac{100}{1.963 \times 10^{-9}} \approx 5.09 \times 10^9\text{ W/m}^2$."
        ),
        (
            r"The high optical intensity in Question 65 is responsible for:",
            r"Instantaneous melting, vaporization, and drilling of hard metals and alloys",
            r"Cooling down optical lenses",
            r"Photoelectric conversion in solar panels",
            r"Creating nuclear fission in air",
            "(a)",
            r"Intensities exceeding $10^9\text{ W/m}^2$ rapidly heat metals above their boiling points, enabling industrial cutting and drilling."
        ),
        (
            r"In holography, the required coherence length of the laser source must be:",
            r"Less than the microscopic grain size of the film",
            r"Greater than the maximum path length difference between the reference beam and object beam",
            r"Zero",
            r"Strictly equal to $1\text{ mm}$",
            "(b)",
            r"To form clear, high-contrast interference fringes over the entire 3D depth of the object, $L_c > \Delta L_{\text{path}}$."
        ),
        (
            r"If the angle between the reference beam and object beam during holographic recording is $\theta = 30^\circ$ at $\lambda = 632.8\text{ nm}$, the fringe spacing $d$ is:",
            r"$0.61\,\mu\text{m}$",
            r"$1.22\,\mu\text{m}$",
            r"$2.44\,\mu\text{m}$",
            r"$6.33\,\mu\text{m}$",
            "(b)",
            r"$d = \frac{\lambda}{2\sin(\theta/2)} = \frac{632.8\text{ nm}}{2\sin(15^\circ)} = \frac{632.8}{2(0.2588)} \approx 1222\text{ nm} \approx 1.22\,\mu\text{m}$."
        ),
        (
            r"The spatial resolution required for a holographic recording photographic emulsion is typically:",
            r"$10\text{--}50\text{ lines/mm}$",
            r"$100\text{--}200\text{ lines/mm}$",
            r"$1000\text{--}5000\text{ lines/mm}$",
            r"$1\text{ line/mm}$",
            "(c)",
            r"Because holographic fringe spacings are on the order of $\approx 1\,\mu\text{m}$, ultra-high resolution plates ($> 1000\text{ lines/mm}$) are mandatory."
        ),
        (
            r"Why cannot a hologram be recorded using ordinary sunlight or white LED illumination?",
            r"White light has too short a coherence length ($\sim 1\,\mu\text{m}$) and multiple uncorrelated wavelengths, washing out interference fringes",
            r"White light carries no energy",
            r"Sunlight cannot be reflected from objects",
            r"Photographic plates do not react to sunlight",
            "(a)",
            r"Interference requires high temporal and spatial coherence. White light's broad spectrum creates zero sustained fringe contrast across depth."
        ),
        (
            r"The threshold current density $J_{\text{th}}$ in a semiconductor diode laser increases sharply when:",
            r"The temperature $T$ of the diode increases",
            r"The temperature decreases toward absolute zero",
            r"The cavity length is increased to infinity",
            r"The bandgap is reduced to zero",
            "(a)",
            r"At higher temperatures, thermal carrier spreading and non-radiative Auger recombination increase, causing $J_{\text{th}}(T) \propto e^{T/T_0}$."
        ),
        (
            r"In a Nd:YAG laser, the pumping transition excites $\text{Nd}^{3+}$ ions from ground level $^4I_{9/2}$ to pump bands $^4F_{5/2}, ^4H_{9/2}$. The atoms then decay non-radiatively to which metastable level?",
            r"$^4F_{3/2}$",
            r"$^4I_{11/2}$",
            r"$^4I_{13/2}$",
            r"$^2P_{1/2}$",
            "(a)",
            r"The metastable upper lasing level is $^4F_{3/2}$ ($\tau \approx 230\,\mu\text{s}$), from which the $1064\text{ nm}$ transition to $^4I_{11/2}$ occurs."
        ),
        (
            r"The $1064\text{ nm}$ emission of a Nd:YAG laser is frequently converted to green light ($532\text{ nm}$) using:",
            r"A spatial filter",
            r"Second Harmonic Generation (SHG) in a non-linear crystal (e.g., KTP or BBO)",
            r"A He-Ne discharge tube",
            r"A Brewster window",
            "(b)",
            r"Second Harmonic Generation doubles the optical frequency ($\nu' = 2\nu$), halving wavelength from $1064\text{ nm}$ (IR) to $532\text{ nm}$ (green)."
        ),
        (
            r"The cavity quality factor $Q$ of an optical resonator is defined by:",
            r"$Q = 2\pi \frac{\text{Energy Stored in Cavity}}{\text{Energy Dissipated per Cycle}}$",
            r"$Q = \frac{\text{Energy Dissipated}}{\text{Energy Stored}}$",
            r"$Q = \frac{\text{Length}}{\text{Wavelength}}$",
            r"$Q = 1 / R_1 R_2$",
            "(a)",
            r"$Q = \omega_0 \frac{U_{\text{stored}}}{P_{\text{loss}}} = 2\pi \frac{U_{\text{stored}}}{U_{\text{dissipated/cycle}}}$, measuring cavity photon retention efficiency."
        ),
        (
            r"An electro-optic Pockels cell or acousto-optic modulator is placed inside a laser cavity primarily to execute:",
            r"Passive cooling",
            r"Active Q-switching for giant pulse generation",
            r"Pumping",
            r"Beam expansion",
            "(b)",
            r"A fast electro-optic Pockels cell acts as a nanosecond optical shutter to switch the cavity $Q$-factor rapidly."
        ),
        (
            r"In a gas laser, Doppler broadening of spectral lines is caused by:",
            r"The random Maxwellian thermal velocities of the gas atoms along the line of sight",
            r"Collisions with the tube walls",
            r"Spontaneous emission lifetime uncertainty",
            r"The presence of mirror coatings",
            "(a)",
            r"Thermal motion gives individual atoms velocity $v_z$, shifting their perceived absorption/emission frequencies by $\Delta\nu = \nu_0(v_z/c)$."
        ),
        (
            r"Homogeneous line broadening in solid-state lasers is predominantly caused by:",
            r"Doppler shifts",
            r"Phonon scattering and finite radiative lifetime affecting all active ions identically",
            r"Crystal lattice imperfections only",
            r"External magnetic field gradients",
            "(b)",
            r"Thermal phonon interactions perturb all ions in an identical statistical manner, creating homogeneous Lorentzian broadening."
        ),
        (
            r"The Fresnel number $N_F$ of a laser cavity of mirror radius $a$, length $L$, and wavelength $\lambda$ is:",
            r"$N_F = \frac{a^2}{\lambda L}$",
            r"$N_F = \frac{\lambda L}{a^2}$",
            r"$N_F = \frac{a \lambda}{L}$",
            r"$N_F = \frac{L^2}{\lambda a}$",
            "(a)",
            r"The Fresnel number $N_F = a^2/(\lambda L)$ characterizes diffraction loss in an optical resonator ($N_F \gg 1$ implies low diffraction loss)."
        ),
        (
            r"A dye laser is uniquely valuable in scientific spectroscopy because it provides:",
            r"Fixed single-frequency emission only in the gamma ray range",
            r"Continuous wavelength tunability across broad spectral ranges (UV to near-IR)",
            r"Nuclear radiation",
            r"Infinite power without pumping",
            "(b)",
            r"Organic dye solutions possess broad continuous vibrational-rotational band manifolds, allowing laser emission to be continuously tuned."
        ),
        (
            r"In LiDAR (Light Detection and Ranging) systems, short laser pulses are used to:",
            r"Measure high-precision distances, atmospheric profiles, and 3D topographic terrain maps via time-of-flight",
            r"Melt targets at infinite distance",
            r"Transmit electrical DC power through clouds",
            r"Detect subterranean radio stations",
            "(a)",
            r"LiDAR sends nanosecond laser pulses and records time-of-flight $\Delta t$ to determine target distances with millimeter accuracy: $d = c\Delta t/2$."
        ),

        # Part III: Advanced Mastery (81-100)
        (
            r"The Schawlow-Townes formula predicts the fundamental quantum limit for the spectral linewidth $\Delta \nu_{\text{laser}}$ of a single-mode laser as:",
            r"$\Delta \nu_{\text{laser}} = \frac{2\pi h \nu (\Delta \nu_c)^2}{P_{\text{out}}}$",
            r"$\Delta \nu_{\text{laser}} = \frac{P_{\text{out}}}{2\pi h \nu}$",
            r"$\Delta \nu_{\text{laser}} = \frac{c}{2L}$",
            r"$\Delta \nu_{\text{laser}} = 0$",
            "(a)",
            r"The fundamental quantum phase-noise linewidth is given by the Schawlow-Townes equation $\Delta\nu = \frac{2\pi h\nu (\Delta\nu_c)^2}{P_{\text{out}}}$."
        ),
        (
            r"In a ring laser gyroscope used in aerospace inertial navigation, rotation of the platform induces a frequency difference between counter-propagating beams via the:",
            r"Zeeman effect",
            r"Sagnac effect",
            r"Stark effect",
            r"Kerr effect",
            "(b)",
            r"The Sagnac effect introduces a differential optical path length $\Delta L = \frac{4\vec{A}\cdot\vec{\Omega}}{c}$, producing a beat frequency proportional to rotation rate $\Omega$."
        ),
        (
            r"Spatial hole burning in a linear standing-wave laser cavity occurs because:",
            r"Atoms located at the electric field nodes do not experience stimulated emission and remain un-depleted",
            r"The laser mirrors burn physical holes in the active rod",
            r"The pump light fails to penetrate the center",
            r"Thermal currents melt the cavity ends",
            "(a)",
            r"Standing wave nodes have zero optical field ($E=0$), leaving local gain un-saturated and allowing adjacent modes to oscillate."
        ),
        (
            r"To eliminate spatial hole burning and achieve pure single-frequency operation, laser cavities are designed as:",
            r"Planar Fabry-Perot cavities",
            r"Unidirectional Ring Resonators (travelling-wave cavities)",
            r"Hemispherical cavities",
            r"Concentric resonators",
            "(b)",
            r"In a unidirectional ring cavity, light travels as a pure traveling wave without standing-wave nodes, preventing spatial hole burning."
        ),
        (
            r"In optical amplification, the small-signal gain coefficient $\gamma_0(\nu)$ saturates with increasing optical intensity $I$ according to:",
            r"$\gamma(\nu) = \frac{\gamma_0(\nu)}{1 + I/I_s}$",
            r"$\gamma(\nu) = \gamma_0(\nu)(1 + I/I_s)$",
            r"$\gamma(\nu) = \gamma_0(\nu) e^{+I/I_s}$",
            r"$\gamma(\nu) = \gamma_0(\nu) - I I_s$",
            "(a)",
            r"Intense stimulated emission depopulates the upper state, causing gain saturation: $\gamma(I) = \gamma_0 / (1 + I/I_s)$, where $I_s$ is saturation intensity."
        ),
        (
            r"The saturation intensity $I_s$ of an active laser transition with cross-section $\sigma_{21}$ and upper state lifetime $\tau_2$ is:",
            r"$I_s = \frac{h\nu}{\sigma_{21} \tau_2}$",
            r"$I_s = h\nu \sigma_{21} \tau_2$",
            r"$I_s = \frac{\sigma_{21} \tau_2}{h\nu}$",
            r"$I_s = \frac{h\nu \tau_2}{\sigma_{21}}$",
            "(a)",
            r"Saturation intensity is the beam intensity where stimulated emission rate equals spontaneous decay rate: $I_s = h\nu/(\sigma_{21}\tau_2)$."
        ),
        (
            r"What optical element is used in a passively mode-locked ultrafast laser to absorb low-intensity continuous background while transmitting intense pulse peaks?",
            r"A partial reflector",
            r"A Saturable Absorber (e.g., SESAM or dye)",
            r"A Faraday rotator",
            r"A quarter-wave plate",
            "(b)",
            r"Saturable absorbers bleach (become transparent) under high peak intensity, favoring short pulse formation over continuous background light."
        ),
        (
            r"The relationship between the pulse duration $\Delta t_p$ and spectral bandwidth $\Delta \nu_p$ of a transform-limited Gaussian laser pulse is:",
            r"$\Delta t_p \cdot \Delta \nu_p \ge 0.441$",
            r"$\Delta t_p \cdot \Delta \nu_p = 0$",
            r"$\Delta t_p / \Delta \nu_p = 1$",
            r"$\Delta t_p \cdot \Delta \nu_p \ge 100$",
            "(a)",
            r"Fourier transform theory imposes the time-bandwidth product limit $\Delta t_p \cdot \Delta\nu_p \ge 0.441$ for transform-limited Gaussian pulses."
        ),
        (
            r"A Ti:Sapphire laser produces femtosecond pulses centered at $800\text{ nm}$ with a bandwidth $\Delta \lambda = 40\text{ nm}$. The transform-limited pulse duration $\Delta t_p$ is approximately:",
            r"$2.4\text{ fs}$",
            r"$23.5\text{ fs}$",
            r"$235\text{ fs}$",
            r"$2.35\text{ ps}$",
            "(b)",
            r"$\Delta\nu = \frac{c}{\lambda^2}\Delta\lambda = \frac{3 \times 10^8}{(800 \times 10^{-9})^2}(40 \times 10^{-9}) = 1.875 \times 10^{13}\text{ Hz}$. $\Delta t_p = \frac{0.441}{\Delta\nu} = \frac{0.441}{1.875 \times 10^{13}} \approx 2.35 \times 10^{-14}\text{ s} = 23.5\text{ fs}$."
        ),
        (
            r"The stability criterion for an optical resonator with mirrors of radii of curvature $R_1, R_2$ and separation $L$ in terms of $g$-parameters ($g_i = 1 - L/R_i$) is:",
            r"$0 \le g_1 g_2 \le 1$",
            r"$g_1 g_2 > 1$",
            r"$g_1 g_2 < 0$",
            r"$g_1 + g_2 = 0$",
            "(a)",
            r"Ray matrix analysis confirms that an optical cavity stably confines ray trajectories if and only if $0 \le g_1 g_2 \le 1$."
        ),
        (
            r"A symmetric confocal resonator has mirror radii $R_1 = R_2 = L$. Its $g$-parameters evaluate to:",
            r"$g_1 = g_2 = 1 \implies g_1 g_2 = 1$",
            r"$g_1 = g_2 = 0 \implies g_1 g_2 = 0$ (Stable)",
            r"$g_1 = g_2 = -1 \implies g_1 g_2 = 1$",
            r"$g_1 g_2 = -1$ (Unstable)",
            "(b)",
            r"$g_1 = g_2 = 1 - L/L = 0$. Thus $g_1 g_2 = 0$, lying inside the stable resonator domain $[0, 1]$."
        ),
        (
            r"In volume (Bragg) holograms recorded in thick media, the reconstruction beam must satisfy:",
            r"Brewster's angle condition",
            r"Bragg's diffraction angle condition ($2d\sin\theta = \lambda$)",
            r"Total internal reflection",
            r"Snell's critical angle condition",
            "(b)",
            r"Thick volume holograms act as 3D photonic lattices, requiring the illumination beam to match the specific Bragg angle for reconstruction."
        ),
        (
            r"Rainbow holography (Benton holograms) allows viewing under ordinary white incandescent light by:",
            r"Using fluorescent inks",
            r"Eliminating vertical parallax via a narrow horizontal slit to avoid chromatic image blur",
            r"Using polarized glasses",
            r"Recording in complete darkness",
            "(b)",
            r"Benton rainbow holograms sacrifice vertical parallax to display crisp, non-overlapping monochromatic slices under white light."
        ),
        (
            r"In laser-induced optical breakdown (LIOB), plasma formation occurs when the focused laser electric field exceeds:",
            r"The dielectric breakdown strength of the material ($\sim 10^9\text{--}10^{10}\text{ V/m}$)",
            r"$1\text{ V/m}$",
            r"The earth's magnetic field",
            r"The work function of tungsten",
            "(a)",
            r"Multiphoton and avalanche ionization create micro-plasmas when field strengths exceed material dielectric breakdown thresholds."
        ),
        (
            r"In a Double Heterostructure (DH) semiconductor laser, carrier and optical confinement are achieved by:",
            r"Surrounding a narrow bandgap active layer (GaAs) with wider bandgap, lower refractive index cladding layers (AlGaAs)",
            r"Using metal shields around the p-n junction",
            r"Cooling the diode to liquid helium temperatures",
            r"Using external convex mirrors",
            "(a)",
            r"The energy steps create potential wells confining electrons and holes, while refractive index steps form a dielectric waveguide for photons."
        ),
        (
            r"The transition rate of spontaneous emission $A_{21}$ scales with the optical frequency $\nu$ as:",
            r"$A_{21} \propto \nu$",
            r"$A_{21} \propto \nu^2$",
            r"$A_{21} \propto \nu^3$",
            r"$A_{21} \propto \nu^4$",
            "(c)",
            r"From $A_{21} = \frac{8\pi h \nu^3}{c^3} B_{21}$, spontaneous emission scales cubically ($\nu^3$), making X-ray lasers extraordinarily challenging."
        ),
        (
            r"In an optical parametric oscillator (OPO), a pump photon of frequency $\nu_p$ is converted inside a non-linear crystal into:",
            r"Two photons: a higher-frequency 'signal' ($\nu_s$) and a lower-frequency 'idler' ($\nu_i$) such that $\nu_p = \nu_s + \nu_i$",
            r"Three identical electron-positron pairs",
            r"A single gamma ray",
            r"Sound waves exclusively",
            "(a)",
            r"Parametric down-conversion splits a pump photon into signal and idler photons preserving energy: $\hbar\omega_p = \hbar\omega_s + \hbar\omega_i$."
        ),
        (
            r"The beam quality factor $M^2$ (M-squared) of an ideal fundamental Gaussian beam ($\text{TEM}_{00}$) is:",
            r"$M^2 = 0$",
            r"$M^2 = 1.0$",
            r"$M^2 = \pi$",
            r"$M^2 = \infty$",
            "(b)",
            r"An ideal diffraction-limited $\text{TEM}_{00}$ Gaussian beam has $M^2 = 1.0$; all real beams have $M^2 > 1.0$."
        ),
        (
            r"A laser has an output power of $10\text{ W}$ at $\lambda = 1064\text{ nm}$. The number of photons emitted per second is approximately:",
            r"$5.35 \times 10^{19}\text{ photons/s}$",
            r"$5.35 \times 10^{18}\text{ photons/s}$",
            r"$1.87 \times 10^{20}\text{ photons/s}$",
            r"$3.20 \times 10^{16}\text{ photons/s}$",
            "(a)",
            r"$E_{\text{photon}} = \frac{hc}{\lambda} = \frac{(6.626 \times 10^{-34})(3 \times 10^8)}{1.064 \times 10^{-6}} \approx 1.868 \times 10^{-19}\text{ J}$. Rate $N = \frac{P}{E_{\text{photon}}} = \frac{10}{1.868 \times 10^{-19}} \approx 5.35 \times 10^{19}\text{ s}^{-1}$."
        ),
        (
            r"Optical tweezers utilize the gradient force of a tightly focused Gaussian laser beam to:",
            r"Trap, hold, and manipulate microscopic dielectric objects and living cells non-invasively",
            r"Cut metallic sheets",
            r"Initiate nuclear fusion",
            r"Transmit FM radio signals",
            "(a)",
            r"Arthur Ashkin's optical tweezers use dipole gradient forces in a focused laser beam to trap and steer micro-particles and biological cells."
        )
    ]
    
    theory_qs = [
        (
            r"Explain the three fundamental processes of radiation-matter interaction: Induced Absorption, Spontaneous Emission, and Stimulated Emission. Derive Einstein's Relations connecting the transition coefficients $A_{21}, B_{12},$ and $B_{21}$.",
            r"""\textbf{1. Three Radiative Processes}:
Consider a two-level atomic system with ground state $E_1$ (population density $N_1$) and excited state $E_2$ (population density $N_2$) exposed to radiation energy density $u(\nu)$ at resonant frequency $\nu = (E_2 - E_1)/h$.
\begin{enumerate}
    \item \textbf{Induced (Stimulated) Absorption}: An atom in level $E_1$ absorbs a photon of energy $h\nu$ and transitions to level $E_2$.
    \begin{equation}
    R_{\text{abs}} = B_{12} N_1 u(\nu)
    \end{equation}
    where $B_{12}$ is Einstein's coefficient of induced absorption.
    \item \textbf{Spontaneous Emission}: An excited atom in level $E_2$ transitions spontaneously to $E_1$, emitting a photon of energy $h\nu$ with random direction, phase, and polarization.
    \begin{equation}
    R_{\text{spont}} = A_{21} N_2
    \end{equation}
    where $A_{21}$ is Einstein's coefficient of spontaneous emission.
    \item \textbf{Stimulated Emission}: An incident trigger photon of energy $h\nu$ perturbs an excited atom in $E_2$, stimulating it to transition to $E_1$ while emitting an identical clone photon.
    \begin{equation}
    R_{\text{stim}} = B_{21} N_2 u(\nu)
    \end{equation}
    where $B_{21}$ is Einstein's coefficient of stimulated emission.
\end{enumerate}

\textbf{2. Equilibrium Rate Balance and Derivation of Einstein's Relations}:
In thermal equilibrium at temperature $T$, the total rate of upward transitions must equal the total rate of downward transitions:
\begin{equation}
R_{\text{abs}} = R_{\text{spont}} + R_{\text{stim}} \implies B_{12} N_1 u(\nu) = A_{21} N_2 + B_{21} N_2 u(\nu)
\end{equation}
Solving for radiation spectral density $u(\nu)$:
\begin{equation}
u(\nu)\left[ B_{12} N_1 - B_{21} N_2 \right] = A_{21} N_2 \implies u(\nu) = \frac{A_{21} N_2}{B_{12} N_1 - B_{21} N_2} = \frac{A_{21}/B_{21}}{\left(\frac{B_{12}}{B_{21}}\right)\left(\frac{N_1}{N_2}\right) - 1}
\end{equation}
According to the Boltzmann distribution law:
\begin{equation}
\frac{N_1}{N_2} = e^{(E_2 - E_1)/k_BT} = e^{h\nu / k_BT}
\end{equation}
Substituting this into the density relation:
\begin{equation}
u(\nu) = \frac{A_{21}/B_{21}}{\left(\frac{B_{12}}{B_{21}}\right)e^{h\nu/k_BT} - 1}
\end{equation}
Comparing with Planck's Law of Blackbody Radiation:
\begin{equation}
u(\nu) = \frac{8\pi h \nu^3}{c^3}\left(\frac{1}{e^{h\nu/k_BT} - 1}\right)
\end{equation}
Matching term by term yields the two fundamental \textbf{Einstein Relations}:
\begin{equation}
\mathbf{B_{12} = B_{21}}, \qquad \mathbf{\frac{A_{21}}{B_{21}} = \frac{8\pi h \nu^3}{c^3}}
\end{equation}"""
        ),
        (
            r"Derive the ratio of stimulated to spontaneous emission rates in thermal equilibrium. Explain why optical laser action is impossible in thermal equilibrium and requires non-thermal pumping to establish population inversion.",
            r"""\textbf{1. Derivation of the Ratio}:
The ratio of the stimulated transition rate to the spontaneous transition rate is:
\begin{equation}
\frac{R_{\text{stim}}}{R_{\text{spont}}} = \frac{B_{21} N_2 u(\nu)}{A_{21} N_2} = \left(\frac{B_{21}}{A_{21}}\right)u(\nu)
\end{equation}
Substituting Planck's radiation energy density $u(\nu) = \frac{8\pi h \nu^3}{c^3}\frac{1}{e^{h\nu/k_BT} - 1}$ and Einstein's relation $\frac{A_{21}}{B_{21}} = \frac{8\pi h\nu^3}{c^3}$:
\begin{equation}
\mathbf{\frac{R_{\text{stim}}}{R_{\text{spont}}} = \frac{1}{e^{h\nu/k_BT} - 1}}
\end{equation}

\textbf{2. Quantitative Analysis at Optical Frequencies}:
For visible green light ($\lambda = 500\text{ nm} \implies \nu = 6 \times 10^{14}\text{ Hz}$):
Photon energy $h\nu = (6.626 \times 10^{-34})(6 \times 10^{14}) \approx 3.98 \times 10^{-19}\text{ J} \approx 2.48\text{ eV}$.
At room temperature ($T = 300\text{ K}$), thermal energy is $k_B T \approx 0.0259\text{ eV}$.
The exponent is:
\begin{equation}
\frac{h\nu}{k_BT} = \frac{2.48}{0.0259} \approx 95.8
\end{equation}
Evaluating the ratio:
\begin{equation}
\frac{R_{\text{stim}}}{R_{\text{spont}}} = \frac{1}{e^{95.8} - 1} \approx e^{-95.8} \approx 10^{-42} \lll 1
\end{equation}
\textit{Conclusion}: In thermal equilibrium at optical frequencies, spontaneous emission completely dominates over stimulated emission by over 40 orders of magnitude!

\textbf{3. Requirement of Non-Thermal Pumping}:
Under Boltzmann equilibrium, $N_2/N_1 = e^{-h\nu/k_BT} \approx 10^{-42}$, meaning practically zero atoms reside in the excited state. Light passing through will be heavily absorbed.
To achieve light amplification ($\frac{dI}{dz} > 0$), we strictly require $(N_2 - N_1) > 0 \implies N_2 > N_1$ (Population Inversion). This non-equilibrium condition can only be created by pumping external energy into the medium."""
        ),
        (
            r"Describe the construction, energy level transitions, pumping mechanism, and working of a Ruby Laser. Why is it inherently difficult to achieve continuous wave (CW) operation in a 3-level laser system?",
            r"""\textbf{1. Construction}:
\begin{itemize}
    \item \textbf{Active Medium}: Synthetic cylindrical pink ruby crystal rod ($\text{Al}_2\text{O}_3$ sapphire matrix doped with $\approx 0.05\%$ trivalent chromium $\text{Cr}^{3+}$ ions). Typical rod dimensions: length $5\text{--}10\text{ cm}$, diameter $1\text{ cm}$.
    \item \textbf{Pumping Source}: Helical Xenon flashlamp coiled around the ruby rod, driven by high-voltage capacitor discharge pulses.
    \item \textbf{Resonator Cavity}: The flat, parallel end-faces of the ruby rod are silvered/dielectric coated (one $100\%$ fully reflective mirror, the other $\approx 80\text{--}90\%$ partially transmitting output coupler).
\end{itemize}

\textbf{2. Energy Level Scheme \& Transitions (3-Level System)}:
\begin{enumerate}
    \item \textbf{Ground State ($^4A_2$)}: Initial state where all $\text{Cr}^{3+}$ ions reside.
    \item \textbf{Pump Bands ($^4F_1, ^4F_2$)}: Optical flash radiation in the green ($\sim 550\text{ nm}$) and blue ($\sim 400\text{ nm}$) excites ions from $^4A_2 \to ^4F_1, ^4F_2$.
    \item \textbf{Fast Radiationless Transition}: Excited ions relax extremely rapidly ($\tau \approx 10^{-11}\text{ s}$) via phonon lattice collisions to the metastable level $^2E$.
    \item \textbf{Metastable State ($^2E$)}: Possesses an exceptionally long lifetime ($\tau \approx 3\text{ ms} = 3 \times 10^{-3}\text{ s}$), allowing large accumulation of chromium ions.
    \item \textbf{Laser Transition ($^2E \to ^4A_2$)}: Stimulated radiative transition produces coherent laser light at \textbf{$\lambda = 694.3\text{ nm}$} (deep red).
\end{enumerate}

\textbf{3. Difficulty of Continuous Wave (CW) Operation in 3-Level Systems}:
In a 3-level system, the lower laser level is the ground state itself ($E_1 = E_{\text{ground}}$).
To achieve population inversion ($N_2 > N_1$), more than $50\%$ of all ground state chromium ions in the entire crystal must be simultaneously pumped into the metastable state:
\begin{equation}
N_2 > \frac{N_{\text{total}}}{2}
\end{equation}
This requires an enormous continuous optical pump power, which generates massive thermal heating that would crack or destroy the ruby crystal. Consequently, ruby lasers operate exclusively in pulsed mode."""
        ),
        (
            r"With the help of a neat energy level diagram, explain the principle, construction, and working of a Helium-Neon (He-Ne) Gas Laser. Explain the exact mechanism of resonant collision excitation.",
            r"""\textbf{1. Construction}:
\begin{itemize}
    \item \textbf{Discharge Tube}: A long, narrow fused-silica glass tube (length $\approx 30\text{--}50\text{ cm}$, bore diameter $\approx 1\text{--}2\text{ mm}$) filled with a gas mixture of Helium and Neon in a $10:1$ ratio at total pressure of $\approx 1\text{ Torr}$.
    \item \textbf{Electrodes \& Pumping}: DC high-voltage supply ($1\text{--}2\text{ kV}$, current $5\text{--}10\text{ mA}$) creates an electrical discharge.
    \item \textbf{Brewster Windows \& Mirrors}: Windows oriented at Brewster's angle $\theta_B$ at tube ends minimize reflection losses and polarize the beam. External concave cavity mirrors provide alignment stability.
\end{itemize}

\textbf{2. Working & Resonant Collision Excitation}:
\begin{enumerate}
    \item \textbf{Direct Electron Impact Excitation of He}: High-velocity electrons in the discharge collide with ground-state He atoms:
    \begin{equation}
    e^- + \text{He}(1^1S_0) \to \text{He}^*(2^3S_1, 2^1S_0) + e^-
    \end{equation}
    These He states ($2^3S_1$ at $19.82\text{ eV}$ and $2^1S_0$ at $20.61\text{ eV}$) are strictly metastable (optical transitions to ground are dipole forbidden).
    \item \textbf{Resonant Inelastic Collision Transfer to Ne}: Neon has excited states $2s$ ($19.78\text{ eV}$) and $3s$ ($20.66\text{ eV}$) that coincide almost perfectly in energy with the He metastable levels. Helium atoms transfer their excitation energy to Neon via resonant collision:
    \begin{equation}
    \text{He}^*(2^1S_0) + \text{Ne}(1s) \to \text{He}(1^1S_0) + \text{Ne}^*(3s_2) \pm \Delta E
    \end{equation}
    \item \textbf{Laser Emission}: Ne atoms in level $3s_2$ undergo stimulated transition to $2p_4$, emitting the famous \textbf{$\lambda = 632.8\text{ nm}$} (bright red) laser line.
    \item \textbf{Depopulation}:
    From $2p_4$, Ne atoms decay rapidly by spontaneous emission ($\tau \approx 10\text{ ns}$) to the $1s$ level.
    From $1s$, Ne atoms de-excite non-radiatively to the ground state via physical collisions with the narrow tube walls.
\end{enumerate}

\textbf{3. Continuous Wave (CW) Operation}:
Because the lower state $2p_4$ empties $10\times$ faster than the upper $3s_2$ state ($\tau_{2p} \approx 10\text{ ns} \ll \tau_{3s} \approx 100\text{ ns}$), $N_{3s} > N_{2p}$ is maintained indefinitely, enabling continuous laser output."""
        ),
        (
            r"Derive the threshold condition for laser oscillation and obtain the formula for threshold gain coefficient $g_{\text{th}}$ in terms of mirror reflectivities $R_1, R_2$, cavity length $L$, and distributed loss coefficient $\alpha_s$.",
            r"""\textbf{1. Physical Setup}:
Consider an optical resonator of length $L$ filled with an active medium possessing a net power gain coefficient $g$ per unit length and a distributed internal scattering/absorption loss coefficient $\alpha_s$ per unit length.
Let the two end mirrors have power reflectivities $R_1$ and $R_2$.

\textbf{2. Round-Trip Loop Gain}:
Let an optical wave start at mirror $M_1$ with initial intensity $I_0$ traveling in the $+z$ direction.
\begin{enumerate}
    \item After traveling distance $L$ to mirror $M_2$, intensity becomes:
    \begin{equation}
    I_1 = I_0 e^{(g - \alpha_s)L}
    \end{equation}
    \item Upon reflection at mirror $M_2$ (reflectivity $R_2$):
    \begin{equation}
    I_2 = R_2 I_1 = R_2 I_0 e^{(g - \alpha_s)L}
    \end{equation}
    \item Returning through the medium distance $L$ back to mirror $M_1$:
    \begin{equation}
    I_3 = I_2 e^{(g - \alpha_s)L} = R_2 I_0 e^{2(g - \alpha_s)L}
    \end{equation}
    \item Upon reflection at mirror $M_1$ (reflectivity $R_1$), completing one full round trip:
    \begin{equation}
    I_{\text{round-trip}} = R_1 I_3 = R_1 R_2 I_0 e^{2(g - \alpha_s)L}
    \end{equation}
\end{enumerate}

\textbf{3. Threshold Condition}:
For sustained steady-state laser oscillation, the round-trip loop gain must equal unity ($I_{\text{round-trip}} = I_0$):
\begin{equation}
R_1 R_2 e^{2(g_{\text{th}} - \alpha_s)L} = 1
\end{equation}
Taking the natural logarithm on both sides:
\begin{align}
\ln(R_1 R_2) + 2(g_{\text{th}} - \alpha_s)L = 0 \\
2(g_{\text{th}} - \alpha_s)L = -\ln(R_1 R_2) = \ln\left(\frac{1}{R_1 R_2}\right)
\end{align}
Dividing by $2L$:
\begin{equation}
g_{\text{th}} - \alpha_s = \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right)
\end{equation}
Thus, the \textbf{Threshold Gain Coefficient} is:
\begin{equation}
\mathbf{g_{\text{th}} = \alpha_s + \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right) = \alpha_s + \alpha_{\text{mirror}}}
\end{equation}
where $\alpha_{\text{mirror}} = \frac{1}{2L}\ln(1/R_1 R_2)$ represents mirror transmission losses."""
        ),
        (
            r"Describe the construction, principle of operation, and characteristics of a Semiconductor Diode Laser (GaAs). Discuss why direct bandgap materials are mandatory for diode lasers.",
            r"""\textbf{1. Construction}:
\begin{itemize}
    \item \textbf{Material}: Heavily doped p-n junction made of a direct bandgap semiconductor such as Gallium Arsenide ($\text{GaAs}$, $E_g \approx 1.42\text{ eV}$) or quaternary alloy $\text{InGaAsP}$.
    \item \textbf{Heterostructure}: Modern laser diodes employ Double Heterostructures (DH) where a thin active GaAs layer ($\sim 0.1\,\mu\text{m}$) is sandwiched between wider bandgap $\text{Al}_x\text{Ga}_{1-x}\text{As}$ cladding layers to provide optical waveguiding and carrier confinement.
    \item \textbf{Cavity Formation}: The crystal is cleaved along natural parallel cleavage planes $(110)$ perpendicular to the junction. Due to high semiconductor refractive index ($n \approx 3.6$), Fresnel reflection at the semiconductor-air interface ($R \approx 32\%$) provides natural cavity mirrors without external coatings.
\end{itemize}

\textbf{2. Principle of Operation}:
\begin{enumerate}
    \item Under large forward bias voltage ($V > E_g/q$), massive numbers of electrons are injected into the conduction band and holes into the valence band within the microscopic active depletion region (Degenerate Carrier Inversion).
    \item Conduction electrons recombine directly with valence holes across the bandgap, releasing coherent photons of energy $h\nu \approx E_g$.
    \item Light propagating along the junction plane undergoes stimulated emission amplification and oscillates between the cleaved facets.
\end{enumerate}

\textbf{3. Emission Wavelength}:
\begin{equation}
\mathbf{\lambda = \frac{h c}{E_g}} \approx \frac{1240\text{ eV}\cdot\text{nm}}{1.42\text{ eV}} \approx \mathbf{870\text{--}904\text{ nm}} \quad (\text{Near-Infrared for GaAs})
\end{equation}

\textbf{4. Direct vs. Indirect Bandgap Requirement}:
\begin{itemize}
    \item In \textbf{direct bandgap} semiconductors (GaAs, InP), the conduction band minimum and valence band maximum lie at the exact same crystal momentum ($k = 0$). Electron-hole recombination occurs directly with $100\%$ photon emission without momentum transfer.
    \item In \textbf{indirect bandgap} materials (Silicon, Germanium), the band extrema are displaced in $k$-space. Recombination requires simultaneous emission/absorption of a lattice vibration (phonon) to conserve momentum. This three-particle process is extremely slow and predominantly generates thermal vibrations rather than light, making silicon incapable of laser action.
\end{itemize}"""
        ),
        (
            r"Explain the principle of Holography. Describe in detail the two distinct stages: (a) Recording of a Hologram (Interference), and (b) Reconstruction of a Hologram (Diffraction). Compare Holography with Conventional Photography.",
            r"""\textbf{1. Basic Principle}:
Invented by Dennis Gabor, holography is a two-step lensless imaging technique that records the complete optical wavefront (both \textbf{amplitude} and \textbf{phase}) scattered by a 3D object using laser coherence, and subsequently reconstructs the authentic 3D optical wavefield.

\textbf{2. Stage 1: Recording of the Hologram (Interference)}:
\begin{itemize}
    \item A coherent, expanded laser beam is divided into two beams by a beam splitter:
    \begin{enumerate}
        \item \textbf{Object Beam ($U_O = A_O e^{i\phi_O}$)}: Illuminates the 3D object and reflects scattered wavelets carrying object depth information.
        \item \textbf{Reference Beam ($U_R = A_R e^{i\phi_R}$)}: Directed straight onto a high-resolution photographic emulsion plate without hitting the object.
    \end{enumerate}
    \item On the plate, the two mutually coherent beams superimpose to form a microscopic interference pattern:
    \begin{align*}
    I(x,y) &= |U_R + U_O|^2 = (U_R + U_O)(U_R^* + U_O^*) \\
    &= |U_R|^2 + |U_O|^2 + U_R U_O^* + U_R^* U_O
    \end{align*}
    The term $U_R^* U_O = A_R A_O e^{i(\phi_O - \phi_R)}$ explicitly encodes the phase $\phi_O(x,y)$ of the object wave into intensity fringe variations.
\end{itemize}

\textbf{3. Stage 2: Reconstruction of the Hologram (Diffraction)}:
\begin{itemize}
    \item The developed photographic plate (hologram) has amplitude transmittance $t(x,y) \propto I(x,y)$.
    \item When illuminated by the original reference beam $U_R$:
    \begin{equation}
    U_{\text{diffracted}} = U_R \cdot t(x,y) \propto U_R \left[ |U_R|^2 + |U_O|^2 \right] + |U_R|^2 U_O + U_R^2 U_O^*
    \end{equation}
    \begin{enumerate}
        \item Term 1 ($U_R [|U_R|^2 + |U_O|^2]$): Undiffracted zero-order transmitted beam.
        \item Term 2 ($|U_R|^2 U_O = A_R^2 U_O$): Reconstructs the exact original diverging object wavefront, forming a \textbf{Virtual 3D Image} behind the plate showing true parallax.
        \item Term 3 ($U_R^2 U_O^*$): Forms a converging conjugate wave producing a \textbf{Real 3D Image} in front of the plate.
    \end{enumerate}
\end{itemize}

\textbf{4. Comparison between Photography and Holography}:
\begin{center}
\begin{tabularx}{\linewidth}{|l|X|X|}
\hline

\textbf{Parameter} & \textbf{Conventional Photography} & \textbf{Holography} \\
\hline
Information recorded & Amplitude (intensity) only ($I \propto |E|^2$) & Both Amplitude and Phase \\
Light source & Incoherent ordinary/sun light & High-coherence laser light \\
Image dimensionality & 2D flat planar image & True 3D image with full parallax \\
Lens required & Yes, camera focusing lens required & No lens required (lensless imaging) \\
Damage impact & Cutting photo destroys that portion & Every piece of hologram reproduces full image \\
\hline
\end{tabularx}
\end{center}"""
        ),
        (
            r"Define temporal coherence and spatial coherence. Derive the relationships connecting coherence time $\tau_c$, coherence length $L_c$, and spectral linewidth $\Delta \nu$. Calculate $L_c$ for a laser with linewidth $\Delta \lambda = 0.001\text{ \AA}$ at $\lambda = 600\text{ nm}$.",
            r"""\textbf{1. Definitions}:
\begin{itemize}
    \item \textbf{Temporal Coherence}: The measure of the correlation between the phase of a light wave at a given point in space at time $t$ and at a later time $t + \tau$. It characterizes monochromaticity and spectral purity.
    \item \textbf{Spatial Coherence}: The measure of the phase correlation between two distinct spatial points across the cross-section of a wavefront at the same instant of time. It characterizes wavefront uniformity and directional focusability.
\end{itemize}

\textbf{2. Mathematical Derivations}:
A wave train emitted during average uninterrupted duration $\tau_c$ (coherence time) has a spatial length:
\begin{equation}
\mathbf{L_c = c \tau_c}
\end{equation}
From Fourier transform analysis of a truncated wavepacket, frequency spread $\Delta\nu$ and time duration $\tau_c$ satisfy:
\begin{equation}
\tau_c \approx \frac{1}{\Delta \nu} \implies \mathbf{L_c = \frac{c}{\Delta \nu}}
\end{equation}
Since $\nu = c/\lambda$, differentiating gives $|d\nu| = \frac{c}{\lambda^2}|d\lambda| \implies \Delta\nu = \frac{c}{\lambda^2}\Delta\lambda$.
Substituting into the coherence length formula:
\begin{equation}
\mathbf{L_c = \frac{c}{(c/\lambda^2)\Delta\lambda} = \frac{\lambda^2}{\Delta \lambda}}
\end{equation}

\textbf{3. Numerical Problem}:
Given $\lambda = 600\text{ nm} = 600 \times 10^{-9}\text{ m} = 6 \times 10^{-7}\text{ m}$, and $\Delta\lambda = 0.001\text{ \AA} = 10^{-13}\text{ m}$.
\begin{align*}
L_c &= \frac{\lambda^2}{\Delta\lambda} = \frac{(6 \times 10^{-7}\text{ m})^2}{10^{-13}\text{ m}} = \frac{3.6 \times 10^{-13}}{10^{-13}} = \mathbf{3.6\text{ m}} \\
\tau_c &= \frac{L_c}{c} = \frac{3.6\text{ m}}{3 \times 10^8\text{ m/s}} = \mathbf{1.2 \times 10^{-8}\text{ s} = 12\text{ ns}} \\
\Delta\nu &= \frac{1}{\tau_c} = \frac{1}{1.2 \times 10^{-8}} \approx \mathbf{8.33 \times 10^7\text{ Hz} = 83.3\text{ MHz}}
\end{align*}"""
        ),
        (
            r"Discuss the Nd:YAG laser in detail, including its crystal host, dopant ion, 4-level energy scheme, optical pumping methods, and industrial/medical applications.",
            r"""\textbf{1. Crystal Architecture}:
\begin{itemize}
    \item \textbf{Host Crystal}: Yttrium Aluminum Garnet ($\text{Y}_3\text{Al}_5\text{O}_{12}$, abbreviated YAG), an optically isotropic crystal with high thermal conductivity and mechanical hardness.
    \item \textbf{Active Dopant}: Triply ionized Neodymium ($\text{Nd}^{3+}$) substituting for $\approx 1.0\text{ at}\%\text{ Y}^{3+}$ sites.
    \item \textbf{Pumping}: Krypton/xenon arc flashlamps or high-power $808\text{ nm}$ AlGaAs semiconductor laser diode arrays.
\end{itemize}

\textbf{2. 4-Level Energy Scheme & Working}:
\begin{enumerate}
    \item \textbf{Ground Level ($^4I_{9/2}$)}: Ground state of $\text{Nd}^{3+}$.
    \item \textbf{Pumping ($^4I_{9/2} \to ^4F_{5/2}, ^4F_{7/2}$)}: Optical pump light around $808\text{ nm}$ excites ions to higher absorption bands.
    \item \textbf{Fast Non-Radiative Relaxation}: Ions decay non-radiatively in $\sim 10^{-9}\text{ s}$ to the upper lasing metastable level $^4F_{3/2}$.
    \item \textbf{Metastable State ($^4F_{3/2}$)}: Lifetime $\tau \approx 230\,\mu\text{s}$, providing efficient population storage.
    \item \textbf{Laser Emission ($^4F_{3/2} \to ^4I_{11/2}$)}: Stimulated transitions produce intense near-infrared light at \textbf{$\lambda = 1064\text{ nm}$ ($1.064\,\mu\text{m}$)}.
    \item \textbf{Fast Terminal Depopulation ($^4I_{11/2} \to ^4I_{9/2}$)}: The lower laser level $^4I_{11/2}$ lies $\approx 0.25\text{ eV}$ above ground and empties in $\sim 30\text{ ns}$ via phonon emission, preventing bottlenecking.
\end{enumerate}

\textbf{3. Frequency Doubling}:
Using second harmonic generation (SHG) in a non-linear crystal (KTP), the $1064\text{ nm}$ beam is doubled to green light at \textbf{$532\text{ nm}$}.

\textbf{4. Key Engineering Applications}:
\begin{itemize}
    \item \textbf{Industrial}: Precision laser drilling of turbine blade cooling holes, micro-welding, laser marking, and sheet-metal cutting.
    \item \textbf{Medical}: Ophthalmology (Nd:YAG capsulotomy), dermatology (tattoo removal), oncology (photocoagulation of vascular tumors), and dental surgery.
    \item \textbf{Defense & Aerospace}: Laser rangefinders, target designators, and airborne LiDAR.
\end{itemize}"""
        ),
        (
            r"Explain the principles of Q-switching and Mode-locking in laser systems. Compare the pulse durations, peak powers, and operational mechanisms of both techniques.",
            r"""\textbf{1. Q-Switching (Giant Pulse Generation)}:
\begin{itemize}
    \item \textbf{Mechanism}: The quality factor $Q = 2\pi(\text{Stored Energy}/\text{Loss per Cycle})$ of the optical cavity is intentionally spoiled (kept low) during pumping. This prevents laser oscillation while population inversion builds up to an extraordinarily high level far above normal threshold.
    \item When inversion reaches maximum, the cavity $Q$-factor is rapidly switched to a high value in nanoseconds using an electro-optic Pockels cell or rotating prism.
    \item The massive stored energy is released in a single, colossal \textbf{Giant Pulse}.
    \item \textbf{Output Characteristics}: Pulse width $\sim 1\text{--}20\text{ ns}$, Peak power $\sim 10\text{ MW to }1\text{ GW}$.
\end{itemize}

\textbf{2. Mode-Locking (Ultrafast Pulse Trains)}:
\begin{itemize}
    \item \textbf{Mechanism}: In a standard multimode laser, hundreds of longitudinal cavity modes oscillate with random, uncorrelated phases.
    \item In mode-locking, an active (acoustic/electro-optic) or passive (saturable absorber) element forces all oscillating modes to lock in constant phase relationship ($\phi_m - \phi_{m-1} = \Delta\phi$).
    \item Superposition of $N$ phase-locked modes creates constructive interference at periodic intervals $\Delta T = 2L/c$, forming a continuous train of ultra-short pulses.
    \item \textbf{Output Characteristics}: Pulse width $\Delta t \approx \frac{1}{N\Delta\nu} \sim 10\text{ fs to }10\text{ ps}$, Peak power $\sim 1\text{ GW to }100\text{ TW}$, Repetition rate $\sim 80\text{ MHz}$.
\end{itemize}

\textbf{3. Comprehensive Comparison}:
\begin{center}
\begin{tabularx}{\linewidth}{|l|X|X|}
\hline

\textbf{Feature} & \textbf{Q-Switching} & \textbf{Mode-Locking} \\
\hline
Pulse Duration & Nanoseconds ($10^{-9}\text{ s}$) & Femtoseconds to Picoseconds ($10^{-15}\text{--}10^{-12}\text{ s}$) \\
Physical Mechanism & Sudden modulation of cavity loss ($Q$) & Phase synchronization across longitudinal modes \\
Pulse Repetition & Single pulse or $1\text{--}100\text{ Hz}$ & High repetition train ($50\text{--}100\text{ MHz}$) \\
Spectral Bandwidth & Narrowband ($\sim\text{MHz}$) & Extremely broad ($\Delta\lambda \sim 10\text{--}100\text{ nm}$) \\
Typical Application & Laser drilling, tattoo removal, LIDAR & Femtosecond spectroscopy, multiphoton microscopy \\
\hline
\end{tabularx}
\end{center}"""
        ),
        (
            r"A helium-neon laser with cavity length $L = 40\text{ cm}$ operates at $\lambda = 632.8\text{ nm}$. The active medium Doppler gain linewidth is $\Delta \nu_D = 1.4\text{ GHz}$. Calculate: (a) longitudinal mode spacing $\Delta \nu$, (b) number of oscillating modes, (c) coherence length $L_c$ of a single mode if its linewidth is $20\text{ kHz}$, and (d) the beam divergence angle for output aperture $D = 1.5\text{ mm}$.",
            r"""\textbf{1. Longitudinal Mode Spacing $\Delta \nu$}:
\begin{equation}
\mathbf{\Delta \nu = \frac{c}{2L} = \frac{3 \times 10^8\text{ m/s}}{2(0.40\text{ m})} = \frac{3 \times 10^8}{0.80} = 3.75 \times 10^8\text{ Hz} = 375\text{ MHz}}
\end{equation}

\textbf{2. Number of Oscillating Modes $N$}:
\begin{equation}
N \approx \frac{\Delta \nu_D}{\Delta \nu} = \frac{1.4 \times 10^9\text{ Hz}}{3.75 \times 10^8\text{ Hz}} \approx 3.73 \implies \mathbf{N = 3 \text{ to } 4\text{ oscillating modes}}
\end{equation}

\textbf{3. Coherence Length $L_c$ of Single Mode ($\Delta\nu = 20\text{ kHz}$)}:
\begin{equation}
\mathbf{L_c = \frac{c}{\Delta\nu} = \frac{3 \times 10^8\text{ m/s}}{20 \times 10^3\text{ Hz}} = 1.5 \times 10^4\text{ m} = 15\text{ km}}
\end{equation}

\textbf{4. Beam Divergence Angle $\theta$}:
For aperture diameter $D = 1.5\text{ mm} = 1.5 \times 10^{-3}\text{ m}$:
\begin{equation}
\mathbf{\theta \approx \frac{1.22 \lambda}{D} = \frac{1.22(632.8 \times 10^{-9}\text{ m})}{1.5 \times 10^{-3}\text{ m}} \approx 5.15 \times 10^{-4}\text{ rad} = 0.515\text{ mrad} \approx 0.0295^\circ}
\end{equation}"""
        ),
        (
            r"Explain the structural differences and working of 3-level vs 4-level laser systems. Derive why the threshold pumping power required for a 3-level laser is substantially higher than that for a 4-level laser.",
            r"""\textbf{1. 3-Level Laser Dynamics (e.g., Ruby)}:
In a 3-level laser:
\begin{itemize}
    \item Pumping excites atoms from Ground ($E_1$) to Pump Band ($E_3$).
    \item Atoms decay rapidly to Metastable level ($E_2$).
    \item Laser transition occurs between $E_2 \to E_1$ (Ground State).
\end{itemize}
Total population $N_{\text{total}} = N_1 + N_2 + N_3 \approx N_1 + N_2$ (since $N_3 \approx 0$).
To achieve inversion ($N_2 > N_1$):
\begin{equation}
N_2 > N_1 \implies N_2 > N_{\text{total}} - N_2 \implies \mathbf{N_2 > \frac{N_{\text{total}}}{2}}
\end{equation}
More than $50\%$ of all atoms in the active medium must be pumped out of the ground state before laser action can even begin.

\textbf{2. 4-Level Laser Dynamics (e.g., Nd:YAG, He-Ne)}:
In a 4-level laser:
\begin{itemize}
    \item Level $E_0$ is Ground, $E_3$ is Pump Band, $E_2$ is Metastable Upper Laser Level, and $E_1$ is Lower Laser Level ($E_1 > E_0$).
    \item At thermal equilibrium, the population in $E_1$ is:
    \begin{equation}
    N_1 = N_0 e^{-(E_1 - E_0)/k_BT}
    \end{equation}
    Since $(E_1 - E_0) \gg k_BT$ (typically $> 0.2\text{ eV} \approx 10 k_BT$), $N_1 \approx 0$.
    \item Inversion condition:
    \begin{equation}
    N_2 > N_1 \approx 0 \implies \mathbf{N_2 > 0}
    \end{equation}
    Laser action begins as soon as even a tiny fraction of atoms ($< 0.1\%$) are pumped into level $E_2$.
\end{itemize}

\textbf{3. Threshold Power Ratio}:
The minimum threshold pump power is proportional to the minimum population required:
\begin{equation}
\frac{P_{\text{th, 3-level}}}{P_{\text{th, 4-level}}} \approx \frac{N_{\text{total}}/2}{N_{\text{th, cavity}}} \approx 10^3 \text{ to } 10^4
\end{equation}
Thus, 4-level lasers require 3 to 4 orders of magnitude less pumping threshold power, easily enabling continuous-wave (CW) operation."""
        ),
        (
            r"Discuss the medical applications of lasers in ophthalmology, dermatology, and general surgery. Explain the biophysical mechanisms of Photoablation, Photocoagulation, and Photodynamic Therapy (PDT).",
            r"""\textbf{1. Biophysical Mechanisms of Laser-Tissue Interaction}:
\begin{enumerate}
    \item \textbf{Photoablation}: High-energy ultraviolet photons (e.g., $193\text{ nm}$ ArF excimer laser) break molecular covalent peptide bonds directly without thermal heating, cleanly vaporizing microscopic tissue layers with sub-micron precision.
    \item \textbf{Photocoagulation}: Absorption of visible/infrared laser light (e.g., Argon green $514\text{ nm}$ or Nd:YAG $1064\text{ nm}$) converts optical power into controlled heat ($60\text{--}80^\circ\text{C}$), denaturing proteins and sealing bleeding blood vessels instantly (hemostasis).
    \item \textbf{Photodynamic Therapy (PDT)}: A photosensitizer drug (e.g., porphyrin) is injected and selectively absorbed by tumor cells. Low-power laser light ($630\text{--}690\text{ nm}$) activates the drug, producing highly reactive singlet oxygen ($^1\text{O}_2$) that destroys cancerous cells locally.
\end{enumerate}

\textbf{2. Clinical Applications}:
\begin{itemize}
    \item \textbf{Ophthalmology}:
    \begin{itemize}
        \item \textit{LASIK}: Excimer laser reshapes the corneal stroma to correct myopia, hyperopia, and astigmatism.
        \item \textit{Retinal Photocoagulation}: Argon/diode laser seals leaking retinal micro-vessels in diabetic retinopathy and repairs retinal detachments.
        \item \textit{Nd:YAG Capsulotomy}: Clears posterior lens capsule opacification following cataract surgery.
    \end{itemize}
    \item \textbf{Dermatology}: Q-switched lasers remove tattoos and hyperpigmentation; pulsed dye lasers treat vascular port-wine stains.
    \item \textbf{Surgery}: $\text{CO}_2$ laser scalpel provides bloodless tissue incision in ENT, neurosurgery, and laparoscopic surgery."""
        ),
        (
            r"A $10\text{ mW}$ He-Ne laser ($\lambda = 632.8\text{ nm}$) has a circular beam diameter $D = 1.2\text{ mm}$. Calculate: (a) beam area, (b) power intensity (irradiance), (c) electric field amplitude $E_0$, and (d) compare its brightness with the Sun's surface intensity ($I_{\text{sun}} \approx 6.4 \times 10^7\text{ W/m}^2$).",
            r"""\textbf{1. Beam Cross-Sectional Area $A$}:
Radius $r = D/2 = 0.6\text{ mm} = 6 \times 10^{-4}\text{ m}$.
\begin{equation}
\mathbf{A = \pi r^2 = \pi (6 \times 10^{-4}\text{ m})^2 \approx 1.131 \times 10^{-6}\text{ m}^2}
\end{equation}

\textbf{2. Power Intensity (Irradiance) $I$}:
\begin{equation}
\mathbf{I = \frac{P}{A} = \frac{10 \times 10^{-3}\text{ W}}{1.131 \times 10^{-6}\text{ m}^2} \approx 8.84 \times 10^3\text{ W/m}^2}
\end{equation}

\textbf{3. Electric Field Amplitude $E_0$}:
\begin{equation}
I = \frac{E_0^2}{2\eta_0} \implies \mathbf{E_0 = \sqrt{2 \eta_0 I} = \sqrt{2(377)(8.84 \times 10^3)} = \sqrt{6.665 \times 10^6} \approx 2582\text{ V/m} \approx 2.58\text{ kV/m}}
\end{equation}

\textbf{4. Comparison with Focused Laser Intensity & Brightness}:
When this modest $10\text{ mW}$ laser is focused by a microscope lens to a $2\,\mu\text{m}$ spot ($r = 1\,\mu\text{m}$):
\begin{equation}
I_{\text{focused}} = \frac{10^{-2}\text{ W}}{\pi (10^{-6})^2} \approx \mathbf{3.18 \times 10^9\text{ W/m}^2}
\end{equation}
The focused laser intensity ($3.18 \times 10^9\text{ W/m}^2$) is nearly \textbf{50 times brighter} than the direct surface of the Sun ($6.4 \times 10^7\text{ W/m}^2$)."""
        ),
        (
            r"Derive the optical resonator cavity stability condition using ABCD ray transfer matrix analysis. Explain the significance of the $g$-parameters $g_1 = 1 - L/R_1$ and $g_2 = 1 - L/R_2$.",
            r"""\textbf{1. Ray Transfer Matrix for a Round Trip}:
An optical resonator consists of mirror $M_1$ (radius of curvature $R_1$) and mirror $M_2$ (radius of curvature $R_2$) separated by distance $L$.
A ray is represented by vector $\begin{bmatrix} r \\ r' \end{bmatrix}$, where $r$ is height and $r'$ is slope.
The round-trip ABCD matrix starting from mirror 1 is:
\begin{equation}
M = \begin{bmatrix} 1 & 0 \\ -2/R_1 & 1 \end{bmatrix} \begin{bmatrix} 1 & L \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ -2/R_2 & 1 \end{bmatrix} \begin{bmatrix} 1 & L \\ 0 & 1 \end{bmatrix}
\end{equation}

\textbf{2. Eigenvalue & Stability Condition}:
For the ray to remain confined inside the cavity after an arbitrary number of round trips ($n \to \infty$), the eigenvalues of $M$ must be complex exponentials ($e^{\pm i\theta}$), requiring:
\begin{equation}
-1 \le \frac{A + D}{2} \le 1
\end{equation}
Carrying out the matrix multiplication yields the trace:
\begin{equation}
\frac{A + D}{2} = 2\left(1 - \frac{L}{R_1}\right)\left(1 - \frac{L}{R_2}\right) - 1
\end{equation}

\textbf{3. Definition of $g$-Parameters}:
Define the dimensionless resonator stability parameters:
\begin{equation}
g_1 = 1 - \frac{L}{R_1}, \qquad g_2 = 1 - \frac{L}{R_2}
\end{equation}
Substituting into the trace stability inequality:
\begin{align}
-1 \le 2 g_1 g_2 - 1 \le 1 \\
0 \le 2 g_1 g_2 \le 2 \implies \mathbf{0 \le g_1 g_2 \le 1}
\end{align}
\textit{Significance}: An optical cavity is stable against ray walk-off losses if and only if the product $g_1 g_2$ lies strictly between $0$ and $1$."""
        ),
        (
            r"Explain the principle and construction of the Carbon Dioxide ($\text{CO}_2$) Molecular Laser. Detail the vibrational modes of the $\text{CO}_2$ molecule and the role of Nitrogen ($\text{N}_2$) and Helium ($\text{He}$) gas additives.",
            r"""\textbf{1. Molecular Vibrational Modes of $\text{CO}_2$}:
$\text{CO}_2$ is a linear triatomic molecule with three fundamental vibrational modes:
\begin{enumerate}
    \item \textbf{Symmetric Stretch Mode ($100$)}: Both Oxygen atoms oscillate symmetrically away from the central Carbon atom ($\nu_1$).
    \item \textbf{Bending Mode ($010$)}: Carbon and Oxygen atoms vibrate perpendicularly to the molecular axis ($\nu_2$, doubly degenerate).
    \item \textbf{Asymmetric Stretch Mode ($001$)}: Carbon oscillates in one direction while both Oxygen atoms oscillate oppositely ($\nu_3$).
\end{enumerate}

\textbf{2. Laser Transition}:
Laser emission occurs between the asymmetric stretch level ($001$) and the symmetric stretch level ($100$), yielding \textbf{$\lambda = 10.6\,\mu\text{m}$} (far infrared). A second transition to $(020)$ gives $\lambda = 9.6\,\mu\text{m}$.

\textbf{3. Role of Gas Additives}:
\begin{itemize}
    \item \textbf{Nitrogen ($\text{N}_2$)}: Nitrogen is a homonuclear diatomic molecule whose first vibrational level ($v=1$ at $2331\text{ cm}^{-1}$) closely matches the $\text{CO}_2$ ($001$) level ($2349\text{ cm}^{-1}$). Discharge electrons excite $\text{N}_2$, which resonantly transfers energy to $\text{CO}_2$, dramatically increasing pumping efficiency.
    \item \textbf{Helium ($\text{He}$)}: Helium depopulates the lower $(010)$ bending level by collisional de-excitation, cools the gas mix via high thermal conductivity, and prevents thermal bottlenecking.
\end{itemize}

\textbf{4. Performance}:
$\text{CO}_2$ lasers provide continuous power from $100\text{ W}$ to $> 50\text{ kW}$ with high electrical-to-optical conversion efficiency ($\approx 15\text{--}20\%$)."""
        ),
        (
            r"A pulsed Ruby laser produces a $1.5\text{ J}$ pulse of duration $\Delta t = 20\text{ ns}$ at $\lambda = 694.3\text{ nm}$. If the beam diameter is $5\text{ mm}$ and divergence is $0.5\text{ mrad}$, calculate: (a) peak power, (b) number of photons in the pulse, (c) pulse energy density, and (d) beam spot diameter at distance $1\text{ km}$.",
            r"""\textbf{1. Peak Power $P_{\text{peak}}$}:
\begin{equation}
\mathbf{P_{\text{peak}} = \frac{E_{\text{pulse}}}{\Delta t} = \frac{1.5\text{ J}}{20 \times 10^{-9}\text{ s}} = 7.5 \times 10^7\text{ W} = 75\text{ MW}}
\end{equation}

\textbf{2. Number of Photons $N$}:
Single photon energy $E_{\text{ph}} = \frac{hc}{\lambda} = \frac{(6.626 \times 10^{-34})(3 \times 10^8)}{694.3 \times 10^{-9}} \approx 2.863 \times 10^{-19}\text{ J}$.
\begin{equation}
\mathbf{N = \frac{1.5\text{ J}}{2.863 \times 10^{-19}\text{ J}} \approx 5.24 \times 10^{18}\text{ photons}}
\end{equation}

\textbf{3. Pulse Energy Density (Fluence)}:
Beam area $A = \pi (2.5 \times 10^{-3}\text{ m})^2 \approx 1.963 \times 10^{-5}\text{ m}^2$.
\begin{equation}
\mathbf{\text{Fluence} = \frac{E_{\text{pulse}}}{A} = \frac{1.5\text{ J}}{1.963 \times 10^{-5}\text{ m}^2} \approx 7.64 \times 10^4\text{ J/m}^2 = 7.64\text{ J/cm}^2}
\end{equation}

\textbf{4. Spot Diameter at $1\text{ km}$ ($z = 1000\text{ m}$)}:
\begin{equation}
\mathbf{D(z) = D_0 + \theta z = 5 \times 10^{-3}\text{ m} + (0.5 \times 10^{-3}\text{ rad})(1000\text{ m}) = 0.005 + 0.500 = 0.505\text{ m} = 50.5\text{ cm}}
\end{equation}"""
        ),
        (
            r"Explain the Gaussian beam propagation model for laser light. Define beam waist $w_0$, Rayleigh range $z_R$, wavefront curvature $R(z)$, and far-field divergence angle $\theta$.",
            r"""\textbf{1. Gaussian Beam Profile}:
The fundamental spatial transverse mode ($\text{TEM}_{00}$) of a laser has a radial Gaussian intensity profile:
\begin{equation}
I(r, z) = I_0 \left(\frac{w_0}{w(z)}\right)^2 \exp\left(-\frac{2r^2}{w^2(z)}\right)
\end{equation}
where $w(z)$ is the beam radius (spot size) at which intensity falls to $1/e^2 \approx 13.5\%$ of its axial value.

\textbf{2. Key Parameters}:
\begin{enumerate}
    \item \textbf{Beam Waist ($w_0$)}: The minimum spot radius located at the focus ($z = 0$).
    \item \textbf{Rayleigh Range ($z_R$)}: The distance from the waist where the cross-sectional area doubles ($w(z_R) = \sqrt{2}w_0$):
    \begin{equation}
    \mathbf{z_R = \frac{\pi w_0^2}{\lambda}}
    \end{equation}
    \item \textbf{Beam Radius Evolution $w(z)$}:
    \begin{equation}
    \mathbf{w(z) = w_0 \sqrt{1 + \left(\frac{z}{z_R}\right)^2}}
    \end{equation}
    \item \textbf{Radius of Wavefront Curvature $R(z)$}:
    \begin{equation}
    \mathbf{R(z) = z \left[ 1 + \left(\frac{z_R}{z}\right)^2 \right]}
    \end{equation}
    At the waist ($z=0$), $R \to \infty$ (planar wavefront).
    \item \textbf{Far-Field Divergence Half-Angle ($\theta$)}:
    For $z \gg z_R$, the asymptotic cone half-angle is:
    \begin{equation}
    \mathbf{\theta = \lim_{z\to\infty}\frac{w(z)}{z} = \frac{w_0}{z_R} = \frac{\lambda}{\pi w_0}}
    \end{equation}
\end{enumerate}"""
        ),
        (
            r"Describe the principle, classification, and applications of Fiber Lasers. Why have high-power Ytterbium-doped fiber lasers largely replaced $\text{CO}_2$ and Nd:YAG lasers in modern industrial manufacturing?",
            r"""\textbf{1. Principle & Architecture}:
\begin{itemize}
    \item A fiber laser uses a rare-earth doped optical fiber (typically $\text{Yb}^{3+}$, $\text{Er}^{3+}$, or $\text{Tm}^{3+}$) as the active gain medium.
    \item \textbf{Cladding Pumping (Double-Clad Fiber)}: High-power, multimode diode pump light is launched into a large inner cladding and absorbed along the length by the single-mode central core.
    \item \textbf{Built-in Resonator}: Fiber Bragg Gratings (FBGs) inscribed directly inside the core act as integrated cavity mirrors.
\end{itemize}

\textbf{2. Advantages of Ytterbium ($\text{Yb}^{3+}$) Fiber Lasers ($\lambda = 1070\text{ nm}$)}:
\begin{enumerate}
    \item \textbf{Exceptional Thermal Management}: The high surface-area-to-volume ratio of long fibers ($> 10\text{ m}$) allows continuous natural cooling without thermal lensing or crystal cracking.
    \item \textbf{High Electrical Efficiency}: Wall-plug efficiency reaches $35\text{--}45\%$ (compared to $< 10\%$ for Nd:YAG and $< 15\%$ for $\text{CO}_2$).
    \item \textbf{Diffraction-Limited Beam Quality}: The single-mode core enforces pure fundamental $\text{TEM}_{00}$ mode ($M^2 \approx 1.05$), focusing to extremely tight spots.
    \item \textbf{Maintenance-Free Monolithic Design}: All-fiber spliced architecture eliminates free-space mirrors, vibrations, and dust misalignment.
\end{enumerate}

\textbf{3. Industrial Impact}:
Fiber lasers ranging from $1\text{ kW}$ to $> 100\text{ kW}$ have become the undisputed global standard for precision automotive sheet-metal cutting, EV battery welding, additive manufacturing (3D metal printing), and shipbuilding."""
        ),
        (
            r"Summarize the essential safety classifications of laser systems (Class 1 to Class 4). Discuss ocular hazards, maximum permissible exposure (MPE), and standard laser laboratory safety protocols.",
            r"""\textbf{1. International Laser Safety Classification (IEC 60825-1 / ANSI Z136.1)}:
\begin{itemize}
    \item \textbf{Class 1}: Safe under all reasonably foreseeable operating conditions (e.g., enclosed CD/DVD players, laser printers).
    \item \textbf{Class 1M / 2M}: Safe for naked eye viewing; hazardous if viewed through magnifying optics (telescopes/microscopes).
    \item \textbf{Class 2}: Visible lasers ($400\text{--}700\text{ nm}$) with power $< 1\text{ mW}$. The human blink reflex ($0.25\text{ s}$) provides natural eye protection (e.g., standard supermarket barcode scanners, educational pointers).
    \item \textbf{Class 3R}: Power $1\text{--}5\text{ mW}$. Low risk of injury if exposure is brief.
    \item \textbf{Class 3B}: Power $5\text{--}500\text{ mW}$. Direct beam and specular reflections cause instantaneous, irreversible retinal damage. Diffuse reflections are generally safe (e.g., research lasers, physiotherapy).
    \item \textbf{Class 4}: Power $> 500\text{ mW}$ ($0.5\text{ W}$ to multikilowatts). Extreme hazard! Direct beam, specular, and diffuse reflections cause severe retinal burning and blindness. Poses skin burn hazards and initiates fires.
\end{itemize}

\textbf{2. Ocular Hazards & Mechanisms}:
\begin{itemize}
    \item The eye's cornea and lens focus incoming collimated laser light onto the retina with an optical gain of $\approx 100,000\times$. A $10\text{ mW}$ beam produces a focal intensity $> 10^6\text{ W/m}^2$, destroying photoreceptor cells instantly.
    \item Visible and Near-IR ($400\text{--}1400\text{ nm}$): Penetrates to the retina (Retinal Hazard Region).
    \item UV ($< 400\text{ nm}$) and Far-IR ($> 1400\text{ nm}$): Absorbed by cornea and lens, causing photokeratitis or cataracts.
\end{itemize}

\textbf{3. Safety Protocols}:
\begin{enumerate}
    \item Wavelength-specific certified laser safety goggles with adequate Optical Density ($\text{OD} \ge 5$).
    \item Interlocked lab doors, warning indicator lamps, beam dumps, and non-reflective matte tools.
\end{enumerate}"""
        )
    ]
    
    return unit_num, unit_title, mcqs, theory_qs
