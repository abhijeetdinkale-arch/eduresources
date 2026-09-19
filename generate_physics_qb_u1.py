# generate_physics_qb_u1.py
# -*- coding: utf-8 -*-

def get_unit_1_content():
    unit_num = 1
    unit_title = "Electromagnetic Theory"
    
    mcqs = [
        # Part I: Foundational (1-50)
        (
            r"The divergence of a vector field $\vec{F}$ at a point represents:",
            r"The net rotational circulation per unit area",
            r"The net outward flux per unit volume from an infinitesimal volume",
            r"The rate of maximum spatial increase of the field",
            r"The total line integral of the field along a closed boundary",
            "(b)",
            r"Divergence measures the scalar net outward flux density (source or sink strength) per unit volume."
        ),
        (
            r"If a magnetic field satisfies $\nabla \cdot \vec{B} = 0$ everywhere, the field is classified as:",
            r"Irrotational",
            r"Solenoidal",
            r"Conservative",
            r"Electrostatic",
            "(b)",
            r"A vector field with identically zero divergence is called solenoidal; it possesses no isolated monopole sources."
        ),
        (
            r"If an electrostatic field satisfies $\nabla \times \vec{E} = 0$, the vector field is:",
            r"Solenoidal",
            r"Conservative (Irrotational)",
            r"Lossy",
            r"Time-dependent",
            "(b)",
            r"Zero curl implies line integrals are path-independent, meaning the electric field is conservative and derivable from a scalar potential."
        ),
        (
            r"The vector identity $\nabla \cdot (\nabla \times \vec{A})$ for any twice continuously differentiable vector field $\vec{A}$ evaluates to:",
            r"$\vec{A}$",
            r"$\nabla^2 \vec{A}$",
            r"$0$",
            r"$1$",
            "(c)",
            r"The divergence of the curl of any arbitrary vector field is identically zero ($\operatorname{div}(\operatorname{curl} \vec{A}) = 0$)."
        ),
        (
            r"The curl of the gradient of any scalar potential function $\phi$, $\nabla \times (\nabla \phi)$, is identically equal to:",
            r"$\vec{0}$",
            r"$\nabla^2 \phi$",
            r"$\phi$",
            r"$-1$",
            "(a)",
            r"A pure gradient field has zero circulation around any closed path, so its curl is identically zero."
        ),
        (
            r"Gauss's Divergence Theorem mathematically transforms:",
            r"A line integral into a surface integral",
            r"A closed surface integral into a volume integral",
            r"A volume integral into a line integral",
            r"A scalar potential into a vector potential",
            "(b)",
            r"Gauss's Divergence Theorem states $\oiint_S \vec{F}\cdot d\vec{S} = \iiint_V (\nabla \cdot \vec{F})\,dV$."
        ),
        (
            r"Stokes' Theorem relates the line integral of a vector around an arbitrary closed contour $C$ to:",
            r"The volume integral of the divergence over the enclosed region",
            r"The surface integral of the curl over an open surface bounded by $C$",
            r"The line integral of the gradient along an open path",
            r"The total electrostatic energy enclosed by $C$",
            "(b)",
            r"Stokes' Theorem states $\oint_C \vec{F} \cdot d\vec{l} = \iint_S (\nabla \times \vec{F})\cdot d\vec{S}$."
        ),
        (
            r"In electrostatics, Poisson's equation relating electric potential $V$ to volume charge density $\rho$ is:",
            r"$\nabla^2 V = 0$",
            r"$\nabla^2 V = -\frac{\rho}{\epsilon_0}$",
            r"$\nabla V = -\frac{\rho}{\epsilon_0}$",
            r"$\nabla^2 V = \mu_0 \rho$",
            "(b)",
            r"Combining $\vec{E} = -\nabla V$ and $\nabla \cdot \vec{E} = \rho/\epsilon_0$ yields Poisson's equation $\nabla^2 V = -\rho/\epsilon_0$."
        ),
        (
            r"In a charge-free dielectric region ($\rho = 0$), Poisson's equation simplifies to:",
            r"Laplace's equation: $\nabla^2 V = 0$",
            r"The diffusion equation: $\nabla^2 V = \frac{\partial V}{\partial t}$",
            r"The Helmholtz equation: $\nabla^2 V = -k^2 V$",
            r"Ampere's equation: $\nabla^2 V = \mu_0 I$",
            "(a)",
            r"When charge density $\rho = 0$, Poisson's equation reduces directly to Laplace's equation $\nabla^2 V = 0$."
        ),
        (
            r"The continuity equation $\nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0$ is the mathematical expression of:",
            r"Conservation of linear momentum",
            r"Conservation of total energy",
            r"Conservation of electric charge",
            r"Conservation of magnetic flux",
            "(c)",
            r"The continuity equation ensures that charge cannot be created or destroyed, only transported as current."
        ),
        (
            r"Maxwell modified Ampere's circuital law by introducing which term to resolve physical inconsistency for dynamic fields?",
            r"Conduction current density $\vec{J}_c$",
            r"Displacement current density $\vec{J}_d = \frac{\partial \vec{D}}{\partial t}$",
            r"Eddy current density $\vec{J}_e$",
            r"Polarization current density $\nabla \times \vec{P}$",
            "(b)",
            r"Maxwell introduced $\vec{J}_d = \partial \vec{D}/\partial t$ so that the total current density $\vec{J} + \vec{J}_d$ remains divergence-free."
        ),
        (
            r"The displacement current between the plates of a charging capacitor is physically produced by:",
            r"Actual physical transport of electrons across the insulating gap",
            r"A time-varying electric field $\frac{\partial \vec{E}}{\partial t}$ within the dielectric",
            r"Thermal ionization of the dielectric material",
            r"Magnetic induction from the connecting wires",
            "(b)",
            r"Displacement current arises from a time-varying electric field and polarization flux, requiring no real particle transfer."
        ),
        (
            r"Maxwell's second equation $\nabla \cdot \vec{B} = 0$ physically indicates that:",
            r"Magnetic fields do no mechanical work",
            r"Isolated magnetic monopoles do not exist in nature",
            r"Magnetic field lines are always open curves",
            r"Electric and magnetic fields are uncoupled",
            "(b)",
            r"$\nabla \cdot \vec{B} = 0$ proves magnetic field lines form continuous closed loops without point sources (monopoles)."
        ),
        (
            r"The differential form of Faraday's Law of Electromagnetic Induction is:",
            r"$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$",
            r"$\nabla \times \vec{B} = \mu_0 \vec{J}$",
            r"$\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$",
            r"$\nabla \cdot \vec{B} = 0$",
            "(a)",
            r"Faraday's Law in differential form states that a time-varying magnetic field generates a curling non-conservative electric field."
        ),
        (
            r"Maxwell's fourth equation in differential form for a non-magnetic medium is:",
            r"$\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$",
            r"$\nabla \times \vec{E} = -\frac{\partial \vec{H}}{\partial t}$",
            r"$\nabla \cdot \vec{H} = \vec{J}$",
            r"$\nabla \times \vec{D} = \vec{H}$",
            "(a)",
            r"The Ampere-Maxwell law states that magnetic field circulation is driven by conduction current plus displacement current."
        ),
        (
            r"The Poynting vector $\vec{S}$ represents the direction and magnitude of:",
            r"Total electrostatic force per unit charge",
            r"Electromagnetic power flux density (energy per unit time per unit area)",
            r"Total magnetic charge density",
            r"Electric dipole polarization rate",
            "(b)",
            r"The Poynting vector $\vec{S} = \vec{E} \times \vec{H}$ quantifies directional energy flow in units of $\text{W/m}^2$."
        ),
        (
            r"The SI unit of the Poynting vector $\vec{S}$ is:",
            r"$\text{J}\cdot\text{m}^2$",
            r"$\text{W/m}^2$",
            r"$\text{N/C}$",
            r"$\text{Tesla}\cdot\text{m}$",
            "(b)",
            r"Power per unit area has SI units of Watts per square meter ($\text{W/m}^2$)."
        ),
        (
            r"In free space, the speed of propagation of electromagnetic waves $c$ is given by:",
            r"$c = \sqrt{\mu_0 \epsilon_0}$",
            r"$c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$",
            r"$c = \frac{\mu_0}{\epsilon_0}$",
            r"$c = \frac{1}{\mu_0 \epsilon_0}$",
            "(b)",
            r"From Maxwell's wave equation, phase velocity in vacuum is $c = 1/\sqrt{\mu_0 \epsilon_0} \approx 3 \times 10^8\text{ m/s}$."
        ),
        (
            r"The intrinsic wave impedance of free space $\eta_0 = \sqrt{\mu_0/\epsilon_0}$ is approximately equal to:",
            r"$50\,\Omega$",
            r"$120\pi\,\Omega \approx 377\,\Omega$",
            r"$300\,\Omega$",
            r"$75\,\Omega$",
            "(b)",
            r"$\eta_0 = \sqrt{\frac{4\pi \times 10^{-7}}{8.854 \times 10^{-12}}} \approx 376.73\,\Omega \approx 120\pi\,\Omega$."
        ),
        (
            r"Electromagnetic waves in free space are strictly transverse in nature because:",
            r"$\vec{E}$ and $\vec{H}$ are parallel to the direction of propagation $\vec{k}$",
            r"Both $\vec{E}$ and $\vec{H}$ are perpendicular to the wave propagation vector $\vec{k}$",
            r"The electric field is zero everywhere",
            r"The magnetic field is longitudinal",
            "(b)",
            r"From Gauss's laws in source-free space, $\vec{k} \cdot \vec{E} = 0$ and $\vec{k} \cdot \vec{H} = 0$, confirming transverse oscillations."
        ),
        (
            r"The total instantaneous energy density $u$ of an electromagnetic wave in a medium of permittivity $\epsilon$ and permeability $\mu$ is:",
            r"$u = \epsilon E^2$",
            r"$u = \frac{1}{2}\epsilon E^2 + \frac{1}{2\mu} B^2$",
            r"$u = \frac{1}{2}\epsilon E + \frac{1}{2}\mu B$",
            r"$u = \vec{E} \times \vec{B}$",
            "(b)",
            r"Total energy density is the sum of electrostatic energy $\frac{1}{2}\epsilon E^2$ and magnetostatic energy $\frac{1}{2\mu} B^2$."
        ),
        (
            r"In a plane electromagnetic wave traveling in vacuum, the ratio of electric field amplitude $E_0$ to magnetic field amplitude $B_0$ is:",
            r"$c$",
            r"$1/c$",
            r"$c^2$",
            r"$\sqrt{c}$",
            "(a)",
            r"In vacuum, $E_0 / B_0 = c$, where $c$ is the speed of light."
        ),
        (
            r"The skin depth $\delta$ in a conducting medium represents the penetration distance at which wave field amplitude decreases to:",
            r"$50\%$ of its surface value",
            r"$1/e \approx 36.8\%$ of its surface value",
            r"$1/e^2 \approx 13.5\%$ of its surface value",
            r"Zero",
            "(b)",
            r"Skin depth $\delta = 1/\alpha$ is the depth where field amplitude attenuates by a factor of $e^{-1} \approx 0.368$."
        ),
        (
            r"The mathematical formula for skin depth $\delta$ in a good conductor of conductivity $\sigma$ and permeability $\mu$ at frequency $\omega$ is:",
            r"$\delta = \sqrt{\frac{2}{\omega \mu \sigma}}$",
            r"$\delta = \sqrt{\frac{\omega \mu}{2\sigma}}$",
            r"$\delta = \frac{\omega}{\mu \sigma}$",
            r"$\delta = \sqrt{\frac{\sigma}{2\omega \mu}}$",
            "(a)",
            r"Skin depth for good conductors ($\sigma \gg \omega\epsilon$) is $\delta = \sqrt{2/(\omega \mu \sigma)}$."
        ),
        (
            r"As the operating frequency of an electromagnetic wave in a conductor increases, the skin depth $\delta$:",
            r"Increases linearly",
            r"Decreases as $1/\sqrt{f}$",
            r"Remains completely unchanged",
            r"Increases exponentially",
            "(b)",
            r"Because $\delta \propto 1/\sqrt{\omega} = 1/\sqrt{2\pi f}$, higher frequencies result in shallower skin depths."
        ),
        (
            r"For a plane EM wave incident normally on a perfectly absorbing surface, the radiation pressure exerted is:",
            r"$P_{\text{rad}} = \frac{\langle S \rangle}{c}$",
            r"$P_{\text{rad}} = \frac{2\langle S \rangle}{c}$",
            r"$P_{\text{rad}} = \frac{\langle S \rangle}{2c}$",
            r"$P_{\text{rad}} = \langle S \rangle c$",
            "(a)",
            r"For complete absorption, momentum transferred per unit area per second is $\langle S \rangle / c$."
        ),
        (
            r"For a plane EM wave incident normally on a perfectly reflecting mirror, the radiation pressure exerted is:",
            r"$P_{\text{rad}} = \frac{\langle S \rangle}{c}$",
            r"$P_{\text{rad}} = \frac{2\langle S \rangle}{c}$",
            r"$P_{\text{rad}} = 0$",
            r"$P_{\text{rad}} = \frac{4\langle S \rangle}{c}$",
            "(b)",
            r"Reflection reverses the momentum of the photons, giving double the momentum transfer: $\Delta p = 2U/c \implies P = 2\langle S \rangle/c$."
        ),
        (
            r"In a lossless dielectric medium with relative permittivity $\epsilon_r = 4$ and relative permeability $\mu_r = 1$, the wave velocity is:",
            r"$3 \times 10^8\text{ m/s}$",
            r"$1.5 \times 10^8\text{ m/s}$",
            r"$0.75 \times 10^8\text{ m/s}$",
            r"$6 \times 10^8\text{ m/s}$",
            "(b)",
            r"$v = c/\sqrt{\epsilon_r \mu_r} = (3 \times 10^8)/\sqrt{4 \times 1} = 1.5 \times 10^8\text{ m/s}$."
        ),
        (
            r"At the boundary between two lossless dielectric media with no free surface charge, the normal component of:",
            r"Electric field $\vec{E}$ is continuous",
            r"Electric displacement $\vec{D}$ is continuous ($D_{1n} = D_{2n}$)",
            r"Magnetic field intensity $\vec{H}$ is discontinuous",
            r"Poynting vector is zero",
            "(b)",
            r"From $\nabla \cdot \vec{D} = \rho_s$, when surface free charge $\rho_s = 0$, $D_{1n} - D_{2n} = 0 \implies D_{1n} = D_{2n}$."
        ),
        (
            r"At any interface between two different media with no surface conduction current, the tangential component of:",
            r"Electric displacement $\vec{D}$ is continuous",
            r"Electric field $\vec{E}$ is continuous ($E_{1t} = E_{2t}$)",
            r"Magnetic induction $\vec{B}$ is continuous",
            r"Vector potential $\vec{A}$ is zero",
            "(b)",
            r"From Faraday's boundary condition $\oint \vec{E}\cdot d\vec{l} = 0$, tangential electric field $E_t$ is always continuous across boundaries."
        ),
        (
            r"At a boundary between two media with no surface current, the normal component of magnetic induction satisfies:",
            r"$B_{1n} = B_{2n}$",
            r"$B_{1n} - B_{2n} = \mu_0$",
            r"$B_{1n} = 0$",
            r"$B_{1n} = -B_{2n}$",
            "(a)",
            r"From $\nabla \cdot \vec{B} = 0$, the normal component of magnetic flux density $B_n$ is always continuous across any interface."
        ),
        (
            r"In a conducting medium, the magnetic field $\vec{H}$ lags behind the electric field $\vec{E}$ by a phase angle of:",
            r"$0^\circ$",
            r"$45^\circ$ ($\pi/4\text{ rad}$)",
            r"$90^\circ$ ($\pi/2\text{ rad}$)",
            r"$180^\circ$ ($\pi\text{ rad}$)",
            "(b)",
            r"The complex intrinsic impedance $\eta_c = \sqrt{\frac{i\omega\mu}{\sigma}} = |\eta_c| e^{i\pi/4}$ introduces a $45^\circ$ phase lag for $\vec{H}$."
        ),
        (
            r"A medium is characterized as a 'good conductor' when the loss tangent satisfies:",
            r"$\frac{\sigma}{\omega \epsilon} \ll 1$",
            r"$\frac{\sigma}{\omega \epsilon} \gg 1$",
            r"$\frac{\sigma}{\omega \epsilon} = 1$",
            r"$\sigma = 0$",
            "(b)",
            r"When conduction current dominates displacement current ($\sigma \gg \omega\epsilon$), the medium behaves as a good conductor."
        ),
        (
            r"A medium is characterized as a 'good dielectric' (low loss) when:",
            r"$\frac{\sigma}{\omega \epsilon} \ll 1$",
            r"$\frac{\sigma}{\omega \epsilon} \gg 1$",
            r"$\sigma = \infty$",
            r"$\epsilon_r = 0$",
            "(a)",
            r"When displacement current greatly exceeds conduction current ($\sigma/\omega\epsilon \ll 1$), it behaves as a low-loss dielectric."
        ),
        (
            r"The time-averaged Poynting vector $\langle \vec{S} \rangle$ for a plane harmonic wave in lossless media is given by:",
            r"$\langle \vec{S} \rangle = \vec{E} \times \vec{H}$",
            r"$\langle \vec{S} \rangle = \frac{1}{2}\operatorname{Re}(\vec{E} \times \vec{H}^*)$",
            r"$\langle \vec{S} \rangle = 2\vec{E}_0 \times \vec{H}_0$",
            r"$\langle \vec{S} \rangle = \frac{E_0^2}{\eta^2}$",
            "(b)",
            r"The time average of the cross product of two sinusoidal vector fields is $\langle \vec{S} \rangle = \frac{1}{2}\operatorname{Re}(\vec{E} \times \vec{H}^*)$."
        ),
        (
            r"The wave equation for electric field $\vec{E}$ in a charge-free, non-conducting medium is:",
            r"$\nabla^2 \vec{E} = \mu \epsilon \frac{\partial^2 \vec{E}}{\partial t^2}$",
            r"$\nabla \times \vec{E} = \mu \epsilon \vec{E}$",
            r"$\nabla^2 \vec{E} = 0$",
            r"$\nabla^2 \vec{E} = \mu \sigma \frac{\partial \vec{E}}{\partial t}$",
            "(a)",
            r"Combining Maxwell's curl equations in source-free lossless media yields the 3D wave equation $\nabla^2 \vec{E} = \mu\epsilon \frac{\partial^2\vec{E}}{\partial t^2}$."
        ),
        (
            r"If $\vec{E}(z,t) = E_0 \cos(\omega t - kz)\hat{i}$, the corresponding magnetic field $\vec{H}(z,t)$ in free space is:",
            r"$\frac{E_0}{\eta_0}\cos(\omega t - kz)\hat{j}$",
            r"$-\frac{E_0}{\eta_0}\sin(\omega t - kz)\hat{j}$",
            r"$\frac{E_0}{\eta_0}\cos(\omega t - kz)\hat{k}$",
            r"$\eta_0 E_0 \cos(\omega t - kz)\hat{j}$",
            "(a)",
            r"Since $\vec{S} \parallel \hat{k}$, $\hat{i} \times \hat{j} = \hat{k}$, and $H_0 = E_0/\eta_0$ with zero phase difference in lossless space."
        ),
        (
            r"The electric and magnetic energy densities in a free-space plane electromagnetic wave are related by:",
            r"$u_e > u_m$",
            r"$u_e < u_m$",
            r"$u_e = u_m$ (Equipartition of energy)",
            r"$u_e = 0$",
            "(c)",
            r"Because $B_0 = E_0/c$ and $c^2 = 1/(\mu_0\epsilon_0)$, $u_m = \frac{B_0^2}{2\mu_0} = \frac{E_0^2}{2\mu_0 c^2} = \frac{1}{2}\epsilon_0 E_0^2 = u_e$."
        ),
        (
            r"Displacement current has dimensions identical to:",
            r"Electric field",
            r"Electric current",
            r"Magnetic flux",
            r"Electric charge density",
            "(b)",
            r"Displacement current $I_d = \iint \vec{J}_d \cdot d\vec{S}$ has the SI unit of Amperes ($\text{A}$), identical to conduction current."
        ),
        (
            r"In a circular parallel-plate capacitor of radius $R$ being charged with current $I$, the displacement current density $J_d$ is:",
            r"$J_d = \frac{I}{\pi R^2}$",
            r"$J_d = \frac{I}{2\pi R}$",
            r"$J_d = \frac{I R^2}{\pi}$",
            r"$J_d = 0$",
            "(a)",
            r"Uniform electric field growth produces uniform displacement current density equal to total charging current divided by area $\pi R^2$."
        ),
        (
            r"The magnetic field induced inside the capacitor plates at distance $r \le R$ from the central axis is:",
            r"$B(r) = \frac{\mu_0 I r}{2\pi R^2}$",
            r"$B(r) = \frac{\mu_0 I}{2\pi r}$",
            r"$B(r) = 0$",
            r"$B(r) = \frac{\mu_0 I R}{2\pi r^2}$",
            "(a)",
            r"Applying Ampere-Maxwell law to a loop of radius $r$: $B(2\pi r) = \mu_0 I_d(r) = \mu_0 I (r^2/R^2) \implies B = \frac{\mu_0 I r}{2\pi R^2}$."
        ),
        (
            r"The concept of magnetic vector potential $\vec{A}$ arises directly from the mathematical relation:",
            r"$\nabla \cdot \vec{B} = 0 \implies \vec{B} = \nabla \times \vec{A}$",
            r"$\nabla \times \vec{E} = 0 \implies \vec{E} = -\nabla V$",
            r"$\nabla \cdot \vec{D} = \rho$",
            r"$\nabla \cdot \vec{J} = -\partial\rho/\partial t$",
            "(a)",
            r"Because any solenoidal vector field can be expressed as the curl of another vector field, $\nabla \cdot \vec{B} = 0 \implies \vec{B} = \nabla \times \vec{A}$."
        ),
        (
            r"Under the Coulomb gauge condition, the vector potential $\vec{A}$ satisfies:",
            r"$\nabla \cdot \vec{A} = 0$",
            r"$\nabla \times \vec{A} = 0$",
            r"$\nabla \cdot \vec{A} = -\mu\epsilon \frac{\partial V}{\partial t}$",
            r"$\vec{A} = \vec{0}$",
            "(a)",
            r"The Coulomb gauge condition is explicitly defined by setting the divergence of vector potential to zero: $\nabla \cdot \vec{A} = 0$."
        ),
        (
            r"Under the Lorenz gauge condition, the potentials $\vec{A}$ and $V$ satisfy:",
            r"$\nabla \cdot \vec{A} + \mu\epsilon \frac{\partial V}{\partial t} = 0$",
            r"$\nabla \cdot \vec{A} = 0$",
            r"$\nabla V = 0$",
            r"$\nabla \times \vec{A} + \vec{E} = 0$",
            "(a)",
            r"The Lorenz gauge $\nabla \cdot \vec{A} + \frac{1}{c^2}\frac{\partial V}{\partial t} = 0$ decouples the wave equations for $V$ and $\vec{A}$."
        ),
        (
            r"The radiation resistance of an infinitesimal Hertzian dipole of length $dl \ll \lambda$ is proportional to:",
            r"$(dl/\lambda)$",
            r"$(dl/\lambda)^2$",
            r"$(dl/\lambda)^4$",
            r"$(\lambda/dl)^2$",
            "(b)",
            r"The radiation resistance of a short dipole antenna is $R_{\text{rad}} = 80\pi^2 (dl/\lambda)^2\,\Omega$."
        ),
        (
            r"Which of the following Maxwell equations represents the fact that electric field lines originate and terminate on electric charges?",
            r"$\nabla \cdot \vec{D} = \rho_v$",
            r"$\nabla \cdot \vec{B} = 0$",
            r"$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$",
            r"$\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$",
            "(a)",
            r"Gauss's law $\nabla \cdot \vec{D} = \rho_v$ states that spatial divergence of electric displacement equals free charge density."
        ),
        (
            r"The attenuation constant $\alpha$ for an electromagnetic wave propagating in a good conductor is given by:",
            r"$\alpha = \sqrt{\frac{\omega \mu \sigma}{2}}$",
            r"$\alpha = \omega \sqrt{\mu \epsilon}$",
            r"$\alpha = \frac{\sigma}{2}\sqrt{\frac{\mu}{\epsilon}}$",
            r"$\alpha = 0$",
            "(a)",
            r"For a good conductor ($\sigma \gg \omega\epsilon$), the propagation constant is $\gamma = \sqrt{i\omega\mu\sigma} = (1+i)\sqrt{\omega\mu\sigma/2}$, so $\alpha = \sqrt{\omega\mu\sigma/2}$."
        ),
        (
            r"The phase velocity $v_p$ of an electromagnetic wave in a good conductor is:",
            r"$v_p = c$",
            r"$v_p = \sqrt{\frac{2\omega}{\mu \sigma}} = \omega \delta$",
            r"$v_p = \frac{1}{\sqrt{\mu\epsilon}}$",
            r"$v_p = \infty$",
            "(b)",
            r"In a conductor, $v_p = \omega/\beta = \omega/\sqrt{\omega\mu\sigma/2} = \sqrt{2\omega/(\mu\sigma)} = \omega \delta$, which is much slower than $c$."
        ),
        (
            r"The refractive index $n$ of a non-magnetic lossless medium ($\mu_r = 1$) is related to its relative permittivity $\epsilon_r$ by:",
            r"$n = \epsilon_r$",
            r"$n = \sqrt{\epsilon_r}$",
            r"$n = \epsilon_r^2$",
            r"$n = 1/\sqrt{\epsilon_r}$",
            "(b)",
            r"Maxwell's relation establishes that $n = c/v = \sqrt{\mu_r \epsilon_r} = \sqrt{\epsilon_r}$ for non-magnetic substances."
        ),
        (
            r"When an electromagnetic wave travels from air into a dielectric medium of refractive index $n=1.5$, its wavelength $\lambda$:",
            r"Increases by $1.5$ times",
            r"Decreases to $\lambda/1.5$",
            r"Remains unchanged",
            r"Becomes zero",
            "(b)",
            r"Wave frequency $f$ remains constant across interfaces, so $\lambda_{\text{med}} = v/f = c/(n f) = \lambda_0 / n$."
        ),

        # Part II: Intermediate Analytical (51-80)
        (
            r"If the electric field of an EM wave is $\vec{E} = 100 \cos(10^8 t - \beta z)\hat{a}_x\text{ V/m}$ in a medium with $\epsilon_r=4, \mu_r=1$, the phase constant $\beta$ is:",
            r"$0.33\text{ rad/m}$",
            r"$0.67\text{ rad/m}$",
            r"$1.33\text{ rad/m}$",
            r"$2.00\text{ rad/m}$",
            "(b)",
            r"$\beta = \omega\sqrt{\mu\epsilon} = \frac{\omega\sqrt{\epsilon_r}}{c} = \frac{10^8 \times 2}{3 \times 10^8} = \frac{2}{3} \approx 0.67\text{ rad/m}$."
        ),
        (
            r"For the wave in Question 51, the amplitude of the magnetic field intensity $H_0$ is:",
            r"$0.265\text{ A/m}$",
            r"$0.531\text{ A/m}$",
            r"$1.000\text{ A/m}$",
            r"$377\text{ A/m}$",
            "(b)",
            r"Intrinsic impedance $\eta = \eta_0/\sqrt{\epsilon_r} = 377/2 = 188.5\,\Omega$. Thus $H_0 = E_0/\eta = 100/188.5 \approx 0.531\text{ A/m}$."
        ),
        (
            r"The time-averaged power density carried by the wave in Question 51 is:",
            r"$13.3\text{ W/m}^2$",
            r"$26.5\text{ W/m}^2$",
            r"$53.0\text{ W/m}^2$",
            r"$100\text{ W/m}^2$",
            "(b)",
            r"$\langle S \rangle = \frac{1}{2} E_0 H_0 = \frac{1}{2}(100)(0.531) \approx 26.5\text{ W/m}^2$."
        ),
        (
            r"If copper has $\sigma = 5.8 \times 10^7\text{ S/m}$ and $\mu = \mu_0$, the skin depth at $f = 1\text{ MHz}$ is approximately:",
            r"$6.6\,\mu\text{m}$",
            r"$66\,\mu\text{m}$",
            r"$0.66\text{ mm}$",
            r"$6.6\text{ mm}$",
            "(b)",
            r"$\delta = 1/\sqrt{\pi f \mu \sigma} = 1/\sqrt{\pi \times 10^6 \times 4\pi\times 10^{-7} \times 5.8\times 10^7} \approx 6.6 \times 10^{-5}\text{ m} = 66\,\mu\text{m}$."
        ),
        (
            r"If the frequency in Question 54 is increased from $1\text{ MHz}$ to $100\text{ MHz}$, the new skin depth will be:",
            r"$6.6\,\mu\text{m}$",
            r"$0.66\,\mu\text{m}$",
            r"$660\,\mu\text{m}$",
            r"$66\,\mu\text{m}$",
            "(a)",
            r"Frequency increased by $100\times$, so $\delta$ scales down by $\sqrt{100} = 10\times$: $66\,\mu\text{m} / 10 = 6.6\,\mu\text{m}$."
        ),
        (
            r"In a lossless transmission medium, the wave impedance is measured to be $188.5\,\Omega$. If $\mu_r = 1$, the dielectric constant $\epsilon_r$ is:",
            r"$1$",
            r"$2$",
            r"$4$",
            r"$16$",
            "(c)",
            r"$\eta = \eta_0/\sqrt{\epsilon_r} \implies 188.5 = 377/\sqrt{\epsilon_r} \implies \sqrt{\epsilon_r} = 2 \implies \epsilon_r = 4$."
        ),
        (
            r"A laser beam with time-averaged power $30\text{ mW}$ is focused to a circular spot of radius $1\text{ mm}$. The peak Poynting vector magnitude is:",
            r"$4.77 \times 10^3\text{ W/m}^2$",
            r"$9.55 \times 10^3\text{ W/m}^2$",
            r"$1.91 \times 10^4\text{ W/m}^2$",
            r"$3.00 \times 10^4\text{ W/m}^2$",
            "(b)",
            r"$\langle S \rangle = P/(\pi r^2) = 0.030 / (\pi \times 10^{-6}) \approx 9549\text{ W/m}^2 \approx 9.55 \times 10^3\text{ W/m}^2$."
        ),
        (
            r"For the laser beam in Question 57, the peak electric field amplitude $E_0$ in air is:",
            r"$1.90\text{ kV/m}$",
            r"$2.68\text{ kV/m}$",
            r"$3.79\text{ kV/m}$",
            r"$5.36\text{ kV/m}$",
            "(b)",
            r"$\langle S \rangle = \frac{E_0^2}{2\eta_0} \implies E_0 = \sqrt{2 \times 377 \times 9549} \approx 2683\text{ V/m} \approx 2.68\text{ kV/m}$."
        ),
        (
            r"A sunlight intensity of $1400\text{ W/m}^2$ falls normally on a perfectly reflecting satellite solar sail of area $100\text{ m}^2$. The total radiation force is:",
            r"$4.67 \times 10^{-4}\text{ N}$",
            r"$9.33 \times 10^{-4}\text{ N}$",
            r"$1.87 \times 10^{-3}\text{ N}$",
            r"$4.20 \times 10^{-1}\text{ N}$",
            "(b)",
            r"$F = P_{\text{rad}} A = \frac{2\langle S \rangle}{c} A = \frac{2 \times 1400}{3 \times 10^8} \times 100 \approx 9.33 \times 10^{-4}\text{ N}$."
        ),
        (
            r"If the solar sail in Question 59 were painted black (perfectly absorbing), the radiation force would become:",
            r"$4.67 \times 10^{-4}\text{ N}$",
            r"$9.33 \times 10^{-4}\text{ N}$",
            r"$0\text{ N}$",
            r"$1.87 \times 10^{-3}\text{ N}$",
            "(a)",
            r"For complete absorption, force is halved: $F = \frac{\langle S \rangle A}{c} = \frac{9.33 \times 10^{-4}}{2} \approx 4.67 \times 10^{-4}\text{ N}$."
        ),
        (
            r"The electric field of an EM wave is given by $\vec{E} = E_0 \cos(kx - \omega t)\hat{j}$. The direction of energy propagation is along:",
            r"$+x$ axis",
            r"$-x$ axis",
            r"$+y$ axis",
            r"$+z$ axis",
            "(a)",
            r"The phase term $(kx - \omega t)$ indicates propagation in the positive $x$-direction ($+\hat{i}$)."
        ),
        (
            r"For the wave in Question 61, the corresponding magnetic field vector $\vec{B}$ points along:",
            r"$+\hat{k}$ ($+z$ axis)",
            r"$-\hat{k}$ ($-z$ axis)",
            r"$+\hat{i}$ ($+x$ axis)",
            r"$+\hat{j}$ ($+y$ axis)",
            "(a)",
            r"$\hat{S} = \hat{E} \times \hat{B}/\mu \implies \hat{i} = \hat{j} \times \hat{u}_B \implies \hat{u}_B = \hat{k}$."
        ),
        (
            r"A parallel-plate capacitor with circular plates of radius $R=0.1\text{ m}$ is charged at $d V/dt = 10^6\text{ V/s}$. If plate separation is $d=1\text{ mm}$, the displacement current $I_d$ is:",
            r"$0.278\,\mu\text{A}$",
            r"$2.78\,\mu\text{A}$",
            r"$27.8\,\mu\text{A}$",
            r"$278\,\mu\text{A}$",
            "(d)",
            r"$C = \frac{\epsilon_0 \pi R^2}{d} = \frac{8.854 \times 10^{-12} \times \pi (0.1)^2}{10^{-3}} \approx 2.78 \times 10^{-10}\text{ F}$. $I_d = C \frac{dV}{dt} = 2.78 \times 10^{-10} \times 10^6 = 2.78 \times 10^{-4}\text{ A} = 278\,\mu\text{A}$."
        ),
        (
            r"For the capacitor in Question 63, the induced magnetic field $B$ at the edge of the plates ($r=R=0.1\text{ m}$) is:",
            r"$5.56 \times 10^{-10}\text{ T}$",
            r"$5.56 \times 10^{-11}\text{ T}$",
            r"$1.11 \times 10^{-9}\text{ T}$",
            r"$2.78 \times 10^{-8}\text{ T}$",
            "(a)",
            r"$B = \frac{\mu_0 I_d}{2\pi R} = \frac{4\pi \times 10^{-7} \times 2.78 \times 10^{-4}}{2\pi \times 0.1} = 5.56 \times 10^{-10}\text{ T}$."
        ),
        (
            r"An electromagnetic wave has electric field amplitude $E_0 = 6\text{ V/m}$. The total average electromagnetic energy density $u_{\text{avg}}$ is:",
            r"$1.59 \times 10^{-10}\text{ J/m}^3$",
            r"$3.18 \times 10^{-10}\text{ J/m}^3$",
            r"$6.36 \times 10^{-10}\text{ J/m}^3$",
            r"$1.27 \times 10^{-9}\text{ J/m}^3$",
            "(a)",
            r"$u_{\text{avg}} = \frac{1}{2}\epsilon_0 E_0^2 = \frac{1}{2}(8.854 \times 10^{-12})(36) \approx 1.59 \times 10^{-10}\text{ J/m}^3$."
        ),
        (
            r"In sea water ($\sigma = 4\text{ S/m}, \epsilon_r = 81, \mu_r = 1$), a radio wave of frequency $f = 25\text{ kHz}$ propagates. The skin depth is:",
            r"$1.6\text{ m}$",
            r"$3.2\text{ m}$",
            r"$0.8\text{ m}$",
            r"$16\text{ m}$",
            "(a)",
            r"$\delta = 1/\sqrt{\pi f \mu \sigma} = 1/\sqrt{\pi \times 2.5\times 10^4 \times 4\pi\times 10^{-7} \times 4} = 1/\sqrt{0.3948} \approx 1.59\text{ m} \approx 1.6\text{ m}$."
        ),
        (
            r"Why are extremely low frequencies (ELF, $< 100\text{ Hz}$) used for submarine communication instead of standard radio frequencies?",
            r"ELF waves have higher photon energy",
            r"Skin depth in conducting sea water is large enough at ELF to penetrate deep waters",
            r"ELF waves travel faster than the speed of light",
            r"Sea water acts as a perfect insulator for ELF",
            "(b)",
            r"Because $\delta \propto 1/\sqrt{f}$, lowering frequency dramatically increases skin depth, enabling signal penetration through conductive sea water."
        ),
        (
            r"The vector field $\vec{F} = y\hat{i} + x\hat{j} + z\hat{k}$ is:",
            r"Solenoidal but not irrotational",
            r"Irrotational but not solenoidal",
            r"Both solenoidal and irrotational",
            r"Neither solenoidal nor irrotational",
            "(b)",
            r"$\nabla \cdot \vec{F} = 0+0+1 = 1 \ne 0$ (not solenoidal); $\nabla \times \vec{F} = (0-0)\hat{i} - (0-0)\hat{j} + (1-1)\hat{k} = \vec{0}$ (irrotational)."
        ),
        (
            r"The vector field $\vec{v} = -y\hat{i} + x\hat{j}$ represents:",
            r"Pure divergence with zero circulation",
            r"Pure vortex circulation with zero divergence ($\nabla \cdot \vec{v} = 0, \nabla \times \vec{v} = 2\hat{k}$)",
            r"A conservative electrostatic field",
            r"A decaying evanescent field",
            "(b)",
            r"$\nabla \cdot \vec{v} = \frac{\partial(-y)}{\partial x} + \frac{\partial x}{\partial y} = 0$, and $\nabla \times \vec{v} = 2\hat{k}$, indicating pure rotational vortex motion."
        ),
        (
            r"If a plane EM wave has $\vec{E} = E_0 e^{-\alpha z}\cos(\omega t - \beta z)\hat{a}_x$, the distance over which the power flow drops by $90\%$ is:",
            r"$z = \frac{\ln 10}{\alpha}$",
            r"$z = \frac{\ln 10}{2\alpha}$",
            r"$z = \frac{1}{\alpha}$",
            r"$z = \frac{2}{\alpha}$",
            "(b)",
            r"Power decays as $e^{-2\alpha z}$. For $90\%$ loss, $P/P_0 = 0.1 \implies e^{-2\alpha z} = 0.1 \implies z = \frac{\ln 10}{2\alpha} \approx \frac{1.15}{\alpha}$."
        ),
        (
            r"The complex Poynting vector is defined as $\vec{S}_c = \frac{1}{2}(\vec{E} \times \vec{H}^*)$. Its imaginary part represents:",
            r"Time-averaged transmitted real power",
            r"Reactive (stored) power oscillating back and forth per unit volume",
            r"Ohmic Joule heat dissipation",
            r"Radiation pressure force",
            "(b)",
            r"$\operatorname{Re}(\vec{S}_c)$ gives real power dissipation/flow, while $\operatorname{Im}(\vec{S}_c)$ represents reactive non-propagating energy exchange."
        ),
        (
            r"The magnetic field of a wave is $\vec{H} = 0.1 \cos(2\pi \times 10^8 t - kx)\hat{a}_z\text{ A/m}$ in vacuum. The wave vector $k$ is:",
            r"$1.05\text{ rad/m}$",
            r"$2.09\text{ rad/m}$",
            r"$3.14\text{ rad/m}$",
            r"$6.28\text{ rad/m}$",
            "(b)",
            r"$k = \omega/c = (2\pi \times 10^8)/(3 \times 10^8) = 2\pi/3 \approx 2.09\text{ rad/m}$."
        ),
        (
            r"For the wave in Question 72, the wavelength $\lambda$ is:",
            r"$1.5\text{ m}$",
            r"$3.0\text{ m}$",
            r"$6.0\text{ m}$",
            r"$0.75\text{ m}$",
            "(b)",
            r"$\lambda = 2\pi/k = c/f = (3 \times 10^8)/10^8 = 3.0\text{ m}$."
        ),
        (
            r"In a coaxial cable carrying current $I$ and voltage $V$, the Poynting vector in the dielectric region points:",
            r"Radially outward from inner to outer conductor",
            r"Azimuthally in circles around inner conductor",
            r"Axially along the cable length from source to load",
            r"Axially backwards toward the source",
            "(c)",
            r"$\vec{E}$ is radial, $\vec{H}$ is azimuthal $\implies \vec{S} = \vec{E} \times \vec{H}$ points axially along the cable, demonstrating energy flows through the dielectric field."
        ),
        (
            r"Integrating the Poynting vector across the dielectric cross-section of the coaxial cable yields total power equal to:",
            r"$P = V/I$",
            r"$P = V I$",
            r"$P = \frac{1}{2} V^2 I$",
            r"$P = I^2 / V$",
            "(b)",
            r"$\iint \vec{S} \cdot d\vec{A} = \int \left(\frac{V}{r\ln(b/a)}\hat{r}\right) \times \left(\frac{I}{2\pi r}\hat{\phi}\right) \cdot (2\pi r dr \hat{z}) = V I$."
        ),
        (
            r"If a uniform plane wave is incident obliquely on a perfect electric conductor (PEC), the total electric field on the surface satisfies:",
            r"$E_{\text{tangential}} = 0$",
            r"$E_{\text{normal}} = 0$",
            r"$E_{\text{total}} = \infty$",
            r"$H_{\text{tangential}} = 0$",
            "(a)",
            r"On a perfect conductor, tangential electric field must vanish identically ($E_t = 0$) to prevent infinite surface current."
        ),
        (
            r"In terms of scalar potential $V$ and vector potential $\vec{A}$, the time-dependent electric field $\vec{E}$ is given by:",
            r"$\vec{E} = -\nabla V$",
            r"$\vec{E} = -\nabla V - \frac{\partial \vec{A}}{\partial t}$",
            r"$\vec{E} = \nabla \times \vec{A}$",
            r"$\vec{E} = -\nabla V + \nabla \times \vec{A}$",
            "(b)",
            r"From $\nabla \times \vec{E} = -\partial\vec{B}/\partial t = -\partial(\nabla\times\vec{A})/\partial t \implies \nabla \times (\vec{E} + \partial\vec{A}/\partial t) = 0 \implies \vec{E} = -\nabla V - \partial\vec{A}/\partial t$."
        ),
        (
            r"The Helmholtz equation for the phasor electric field in a linear, isotropic, source-free dielectric is:",
            r"$\nabla^2 \vec{E}_s + k^2 \vec{E}_s = 0$",
            r"$\nabla^2 \vec{E}_s - k^2 \vec{E}_s = 0$",
            r"$\nabla \vec{E}_s + k \vec{E}_s = 0$",
            r"$\nabla^2 \vec{E}_s + \frac{1}{c^2}\vec{E}_s = 0$",
            "(a)",
            r"Substituting harmonic time dependence $\partial^2/\partial t^2 \to -\omega^2$ into the wave equation gives the Helmholtz equation $\nabla^2\vec{E}_s + k^2\vec{E}_s = 0$ where $k = \omega\sqrt{\mu\epsilon}$."
        ),
        (
            r"The energy transferred per unit area by an EM pulse of duration $\tau$ having constant Poynting flux $S_0$ is:",
            r"$U/A = S_0 \tau$",
            r"$U/A = S_0 / \tau$",
            r"$U/A = \frac{1}{2} S_0 \tau^2$",
            r"$U/A = S_0 c \tau$",
            "(a)",
            r"Fluence (energy per unit area) is the time integral of Poynting flux: $\int_0^\tau S_0 dt = S_0 \tau$ (in $\text{J/m}^2$)."
        ),
        (
            r"If the magnetic field in free space is $\vec{B} = 10^{-7}\sin(\omega t - ky)\hat{i}\text{ T}$, the electric field $\vec{E}$ is:",
            r"$30 \sin(\omega t - ky)\hat{k}\text{ V/m}$",
            r"$-30 \sin(\omega t - ky)\hat{k}\text{ V/m}$",
            r"$30 \sin(\omega t - ky)\hat{j}\text{ V/m}$",
            r"$-30 \sin(\omega t - ky)\hat{i}\text{ V/m}$",
            "(b)",
            r"$E_0 = c B_0 = (3 \times 10^8)(10^{-7}) = 30\text{ V/m}$. Direction: $\hat{E} \times \hat{B} \parallel \hat{j} \implies \hat{E} \times \hat{i} = \hat{j} \implies \hat{E} = -\hat{k}$."
        ),

        # Part III: Advanced Mastery (81-100)
        (
            r"In an anisotropic crystal where permittivity is a tensor $\bar{\bar{\epsilon}}$, which vectors remain strictly parallel in an EM wave?",
            r"$\vec{D}$ and $\vec{E}$",
            r"$\vec{B}$ and $\vec{H}$ (in non-magnetic crystal)",
            r"$\vec{k}$ and $\vec{S}$",
            r"$\vec{E}$ and $\vec{k}$",
            "(b)",
            r"In non-magnetic anisotropic crystals, $\vec{B} = \mu_0 \vec{H}$ so $\vec{B} \parallel \vec{H}$, but $\vec{D} = \bar{\bar{\epsilon}}\vec{E}$ is not parallel to $\vec{E}$, causing Poynting vector $\vec{S}$ to walk off from $\vec{k}$."
        ),
        (
            r"Poynting's theorem in differential form for an electromagnetic field interacting with matter is expressed as:",
            r"$\nabla \cdot \vec{S} + \frac{\partial u}{\partial t} = -\vec{J} \cdot \vec{E}$",
            r"$\nabla \times \vec{S} + \frac{\partial u}{\partial t} = 0$",
            r"$\nabla \cdot \vec{S} = \vec{J} \cdot \vec{E}$",
            r"$\nabla \cdot \vec{S} + u = 0$",
            "(a)",
            r"$\nabla \cdot \vec{S} + \frac{\partial}{\partial t}\left(\frac{1}{2}\epsilon E^2 + \frac{1}{2\mu} B^2\right) = -\vec{J}\cdot\vec{E}$ accounts for energy outflow, rate of stored energy change, and Ohmic work."
        ),
        (
            r"The term $-\vec{J} \cdot \vec{E}$ in Poynting's theorem physically represents:",
            r"The rate of work done by the electromagnetic field on charge carriers (Joule heating/mechanical power)",
            r"The rate of creation of magnetic monopoles",
            r"The electrostatic potential energy stored in the dielectric",
            r"The radiation reaction force on an accelerated dipole",
            "(a)",
            r"$\vec{J} \cdot \vec{E}$ is the local rate at which electromagnetic field energy is transferred into kinetic/thermal energy of charges."
        ),
        (
            r"For an electromagnetic wave in a good conductor, the complex propagation constant is $\gamma = \alpha + i\beta$. The relationship between $\alpha$ and $\beta$ is:",
            r"$\alpha = \beta = \sqrt{\frac{\omega \mu \sigma}{2}}$",
            r"$\alpha = 2\beta$",
            r"$\beta = 0$",
            r"$\alpha = 0$",
            "(a)",
            r"In a good conductor, $\sigma \gg \omega\epsilon$, leading to identical attenuation and phase constants: $\alpha = \beta = \sqrt{\omega\mu\sigma/2} = 1/\delta$."
        ),
        (
            r"A plane wave in a non-magnetic dielectric medium ($\epsilon_r = 9$) has magnetic field $H_0 = 2\text{ A/m}$. The average power flow across a $2\text{ m}^2$ area normal to propagation is:",
            r"$251\text{ W}$",
            r"$503\text{ W}$",
            r"$754\text{ W}$",
            r"$1508\text{ W}$",
            "(b)",
            r"$\eta = 377/\sqrt{9} = 125.67\,\Omega$. $\langle S \rangle = \frac{1}{2}\eta H_0^2 = \frac{1}{2}(125.67)(4) \approx 251.3\text{ W/m}^2$. Total power $P = \langle S \rangle \times 2 = 502.7\text{ W} \approx 503\text{ W}$."
        ),
        (
            r"The Brewster angle $\theta_B$ for parallel polarization (p-polarized wave) incident from medium 1 to medium 2 is given by:",
            r"$\tan \theta_B = \frac{n_2}{n_1}$",
            r"$\sin \theta_B = \frac{n_2}{n_1}$",
            r"$\cos \theta_B = \frac{n_2}{n_1}$",
            r"$\tan \theta_B = \frac{n_1}{n_2}$",
            "(a)",
            r"At Brewster's angle $\theta_B = \arctan(n_2/n_1)$, reflected ray is perpendicular to refracted ray, resulting in zero reflection for p-polarization."
        ),
        (
            r"When an unpolarized light wave reflects at Brewster's angle from a glass plate ($n=1.5$), the reflected beam is:",
            r"Completely circularly polarized",
            r"$100\%$ linearly polarized perpendicular to the plane of incidence (s-polarized)",
            r"$100\%$ linearly polarized parallel to the plane of incidence (p-polarized)",
            r"Completely unpolarized",
            "(b)",
            r"Because the p-component has zero reflection at Brewster's angle, the reflected light consists exclusively of the s-component."
        ),
        (
            r"The critical angle $\theta_c$ for total internal reflection between core ($n_1=1.50$) and cladding ($n_2=1.45$) is:",
            r"$45.0^\circ$",
            r"$60.0^\circ$",
            r"$75.2^\circ$",
            r"$85.1^\circ$",
            "(c)",
            r"$\theta_c = \arcsin(n_2/n_1) = \arcsin(1.45/1.50) = \arcsin(0.9667) \approx 75.16^\circ$."
        ),
        (
            r"In total internal reflection, the field in the rarer medium is not strictly zero but decays exponentially away from the boundary as a/an:",
            r"Standing wave",
            r"Evanescent wave",
            r"Shock wave",
            r"Soliton wave",
            "(b)",
            r"An evanescent wave has pure imaginary wavevector normal to the interface, carrying zero net time-averaged power into the cladding."
        ),
        (
            r"The complex dielectric constant of a lossy medium is $\hat{\epsilon} = \epsilon' - i\epsilon''$. The loss tangent $\tan\delta$ is defined as:",
            r"$\tan\delta = \frac{\epsilon''}{\epsilon'} = \frac{\sigma}{\omega \epsilon'}$",
            r"$\tan\delta = \frac{\epsilon'}{\epsilon''}$",
            r"$\tan\delta = \sqrt{\epsilon' \epsilon''}$",
            r"$\tan\delta = \frac{\omega \epsilon'}{\sigma}$",
            "(a)",
            r"Loss tangent $\tan\delta = \epsilon''/\epsilon' = \sigma/(\omega\epsilon)$ measures the ratio of dissipative conduction current to reactive displacement current."
        ),
        (
            r"A plane EM wave in free space has $\vec{E} = (3\hat{i} + 4\hat{j})e^{i(\omega t - kz)}\text{ V/m}$. The polarization state of this wave is:",
            r"Circularly polarized",
            r"Linearly polarized at an angle $\theta = \arctan(4/3) \approx 53.1^\circ$ to the $x$-axis",
            r"Elliptically polarized",
            r"Unpolarized",
            "(b)",
            r"Both components $E_x$ and $E_y$ oscillate in phase, so the resultant field maintains a constant spatial angle $\arctan(4/3)$."
        ),
        (
            r"If $\vec{E} = E_0 (\hat{i} + i\hat{j})e^{i(\omega t - kz)}$, the wave is:",
            r"Linearly polarized",
            r"Left Circularly Polarized (LCP)",
            r"Right Circularly Polarized (RCP)",
            r"Unpolarized",
            "(b)",
            r"Equal amplitude components with a $+90^\circ$ ($+i$) phase shift produce circular rotation of the electric field vector."
        ),
        (
            r"The magnetic energy stored per unit length inside a long cylindrical wire of radius $a$ carrying uniform DC current $I$ is:",
            r"$\frac{\mu_0 I^2}{16\pi}$",
            r"$\frac{\mu_0 I^2}{8\pi}$",
            r"$\frac{\mu_0 I^2}{4\pi}$",
            r"$\frac{\mu_0 I^2}{2\pi}$",
            "(a)",
            r"$u_m = \frac{B^2}{2\mu_0} = \frac{\mu_0 I^2 r^2}{8\pi^2 a^4}$. Integrating over cylinder cross section $\int_0^a u_m 2\pi r dr = \frac{\mu_0 I^2}{16\pi}\text{ J/m}$."
        ),
        (
            r"The internal self-inductance per unit length of the cylindrical wire in Question 93 is:",
            r"$L_{\text{int}} = \frac{\mu_0}{8\pi}\text{ H/m}$",
            r"$L_{\text{int}} = \frac{\mu_0}{4\pi}\text{ H/m}$",
            r"$L_{\text{int}} = \frac{\mu_0}{2\pi}\text{ H/m}$",
            r"$L_{\text{int}} = \frac{\mu_0}{16\pi}\text{ H/m}$",
            "(a)",
            r"Setting stored internal energy $U = \frac{1}{2} L_{\text{int}} I^2 = \frac{\mu_0 I^2}{16\pi} \implies L_{\text{int}} = \frac{\mu_0}{8\pi}\text{ H/m}$."
        ),
        (
            r"For an electromagnetic wave incident normally from air ($\eta_1 = 377\,\Omega$) onto a lossless dielectric with $\eta_2 = 188.5\,\Omega$, the reflection coefficient $\Gamma$ is:",
            r"$+1/3$",
            r"$-1/3$",
            r"$+1/2$",
            r"$-1/2$",
            "(b)",
            r"$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} = \frac{188.5 - 377}{188.5 + 377} = \frac{-188.5}{565.5} = -\frac{1}{3}$."
        ),
        (
            r"For the boundary in Question 95, the fraction of incident power reflected (reflectance $R$) is:",
            r"$11.1\%$ ($1/9$)",
            r"$33.3\%$ ($1/3$)",
            r"$66.7\%$ ($2/3$)",
            r"$88.9\%$ ($8/9$)",
            "(a)",
            r"$R = |\Gamma|^2 = (-1/3)^2 = 1/9 \approx 11.11\%$."
        ),
        (
            r"The transmission coefficient $\tau$ for the electric field at the boundary in Question 95 is:",
            r"$+2/3$",
            r"$+4/3$",
            r"$+1/3$",
            r"$+8/9$",
            "(a)",
            r"$\tau = 1 + \Gamma = 1 - 1/3 = +2/3$ (or $\tau = \frac{2\eta_2}{\eta_1+\eta_2} = \frac{377}{565.5} = \frac{2}{3}$)."
        ),
        (
            r"The fraction of power transmitted across the interface in Question 95 (transmittance $T$) is:",
            r"$11.1\%$",
            r"$50.0\%$",
            r"$88.9\%$ ($8/9$)",
            r"$100\%$",
            "(c)",
            r"By conservation of energy, $T = 1 - R = 1 - 1/9 = 8/9 \approx 88.89\%$."
        ),
        (
            r"The vector wave equation for the magnetic vector potential $\vec{A}$ in Lorenz gauge with source current density $\vec{J}$ is:",
            r"$\nabla^2 \vec{A} - \mu\epsilon \frac{\partial^2 \vec{A}}{\partial t^2} = -\mu \vec{J}$",
            r"$\nabla^2 \vec{A} + k^2 \vec{A} = 0$",
            r"$\nabla^2 \vec{A} = -\mu \vec{J}$",
            r"$\nabla \times \vec{A} = \mu \vec{J}$",
            "(a)",
            r"In Lorenz gauge, the inhomogeneous wave equation is $\nabla^2 \vec{A} - \frac{1}{c^2}\frac{\partial^2\vec{A}}{\partial t^2} = -\mu \vec{J}$."
        ),
        (
            r"In a good conductor, the ratio of the magnetic field energy density $u_m$ to the electric field energy density $u_e$ is:",
            r"$u_m/u_e \approx 1$",
            r"$u_m/u_e \approx \frac{\sigma}{\omega \epsilon} \gg 1$",
            r"$u_m/u_e \approx \frac{\omega\epsilon}{\sigma} \ll 1$",
            r"$u_m/u_e = 0$",
            "(b)",
            r"Inside a good conductor, almost all electromagnetic energy is stored in the magnetic field: $u_m / u_e = \sigma/(\omega\epsilon) \gg 1$."
        )
    ]
    
    theory_qs = [
        (
            r"State Maxwell's four equations of electromagnetism in both differential and integral forms, and explain the complete physical significance of each equation.",
            r"""\textbf{1. Gauss's Law for Electrostatics}:
\begin{align*}
\text{Differential Form:}\quad &\nabla \cdot \vec{D} = \rho_v \iff \nabla \cdot \vec{E} = \frac{\rho_v}{\epsilon_0} \\
\text{Integral Form:}\quad &\oiint_S \vec{D}\cdot d\vec{S} = Q_{\text{enc}} \iff \oiint_S \vec{E}\cdot d\vec{S} = \frac{1}{\epsilon_0}\iiint_V \rho_v\,dV
\end{align*}
\textit{Physical Significance}: Electric field lines originate on positive electric charges and diverge outward, terminating on negative charges. Electric charge acts as the scalar source/sink of the electric displacement field.

\textbf{2. Gauss's Law for Magnetism}:
\begin{align*}
\text{Differential Form:}\quad &\nabla \cdot \vec{B} = 0 \\
\text{Integral Form:}\quad &\oiint_S \vec{B}\cdot d\vec{S} = 0
\end{align*}
\textit{Physical Significance}: The net magnetic flux exiting any arbitrary closed Gaussian surface is identically zero. This proves that isolated magnetic monopoles do not exist in nature; magnetic field lines are continuous, unbroken closed loops.

\textbf{3. Faraday's Law of Electromagnetic Induction}:
\begin{align*}
\text{Differential Form:}\quad &\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} \\
\text{Integral Form:}\quad &\oint_C \vec{E}\cdot d\vec{l} = -\frac{d}{dt}\iint_S \vec{B}\cdot d\vec{S} = -\frac{d\Phi_B}{dt}
\end{align*}
\textit{Physical Significance}: A spatially or temporally changing magnetic field produces a non-conservative, circulating electric field. This forms the foundational operating principle of electrical generators, inductors, and transformers.

\textbf{4. Ampere--Maxwell Law}:
\begin{align*}
\text{Differential Form:}\quad &\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t} \\
\text{Integral Form:}\quad &\oint_C \vec{H}\cdot d\vec{l} = \iint_S \left(\vec{J} + \frac{\partial \vec{D}}{\partial t}\right)\cdot d\vec{S} = I_c + I_d
\end{align*}
\textit{Physical Significance}: Magnetic fields are generated by two distinct physical sources: (i) physical conduction currents of moving charge carriers $\vec{J}$, and (ii) time-varying electric displacement flux $\partial\vec{D}/\partial t$ (displacement current). This coupling allows self-sustaining electromagnetic waves to propagate across empty space."""
        ),
        (
            r"Derive the continuity equation $\nabla \cdot \vec{J} + \frac{\partial \rho_v}{\partial t} = 0$ from fundamental principles of charge conservation, and explain how it led James Clerk Maxwell to postulate the displacement current.",
            r"""\textbf{1. Derivation of Continuity Equation}:
Consider an arbitrary volume $V$ bounded by a closed surface $S$. Let total charge enclosed inside $V$ be $Q(t) = \iiint_V \rho_v(\vec{r},t)\,dV$.
By the law of conservation of electric charge, the net rate of decrease of enclosed charge must equal the net outward current flux crossing surface $S$:
\begin{equation}
I_{\text{out}} = \oiint_S \vec{J}\cdot d\vec{S} = -\frac{dQ}{dt} = -\frac{d}{dt}\iiint_V \rho_v\,dV = -\iiint_V \frac{\partial \rho_v}{\partial t}\,dV
\end{equation}
Applying Gauss's Divergence Theorem to the surface integral:
\begin{equation}
\oiint_S \vec{J}\cdot d\vec{S} = \iiint_V (\nabla \cdot \vec{J})\,dV
\end{equation}
Equating both volume integrals:
\begin{equation}
\iiint_V \left( \nabla \cdot \vec{J} + \frac{\partial \rho_v}{\partial t} \right) dV = 0
\end{equation}
Because this relation must hold valid for any arbitrarily chosen volume $V$, the integrand must vanish identically everywhere:
\begin{equation}
\mathbf{\nabla \cdot \vec{J} + \frac{\partial \rho_v}{\partial t} = 0}
\end{equation}

\textbf{2. Need for Displacement Current}:
Classical Ampere's circuital law states $\nabla \times \vec{H} = \vec{J}$. Taking the divergence of both sides:
\begin{equation}
\nabla \cdot (\nabla \times \vec{H}) = \nabla \cdot \vec{J}
\end{equation}
Since the divergence of any curl is identically zero, this requires $\nabla \cdot \vec{J} = 0$. However, according to the continuity equation, $\nabla \cdot \vec{J} = -\partial\rho_v/\partial t \ne 0$ for dynamic, time-dependent systems (such as a charging capacitor).
To remove this mathematical contradiction, Maxwell added an unknown current density vector $\vec{J}_d$:
\begin{equation}
\nabla \times \vec{H} = \vec{J} + \vec{J}_d \implies \nabla \cdot (\nabla \times \vec{H}) = \nabla \cdot \vec{J} + \nabla \cdot \vec{J}_d = 0 \implies \nabla \cdot \vec{J}_d = -\nabla \cdot \vec{J} = \frac{\partial \rho_v}{\partial t}
\end{equation}
Using Gauss's law $\rho_v = \nabla \cdot \vec{D}$:
\begin{equation}
\nabla \cdot \vec{J}_d = \frac{\partial}{\partial t}(\nabla \cdot \vec{D}) = \nabla \cdot \left( \frac{\partial \vec{D}}{\partial t} \right) \implies \mathbf{\vec{J}_d = \frac{\partial \vec{D}}{\partial t}}
\end{equation}"""
        ),
        (
            r"Starting from Maxwell's equations in a source-free, non-conducting dielectric medium ($\rho_v = 0, \vec{J} = 0$), derive the 3D electromagnetic wave equations for $\vec{E}$ and $\vec{H}$, and obtain the expression for the speed of light.",
            r"""In a linear, isotropic, homogeneous, source-free dielectric medium, Maxwell's equations simplify to:
\begin{align}
(1)\;\nabla \cdot \vec{E} = 0, \quad (2)\;\nabla \cdot \vec{H} = 0, \quad (3)\;\nabla \times \vec{E} = -\mu\frac{\partial \vec{H}}{\partial t}, \quad (4)\;\nabla \times \vec{H} = \epsilon\frac{\partial \vec{E}}{\partial t}
\end{align}
\textbf{Step 1: Wave equation for $\vec{E}$}:
Take the curl of Faraday's Law (Eq. 3):
\begin{equation}
\nabla \times (\nabla \times \vec{E}) = \nabla \times \left( -\mu \frac{\partial \vec{H}}{\partial t} \right) = -\mu \frac{\partial}{\partial t} (\nabla \times \vec{H})
\end{equation}
Substitute the Ampere--Maxwell relation (Eq. 4) for $\nabla \times \vec{H}$:
\begin{equation}
\nabla \times (\nabla \times \vec{E}) = -\mu \frac{\partial}{\partial t} \left( \epsilon \frac{\partial \vec{E}}{\partial t} \right) = -\mu\epsilon \frac{\partial^2 \vec{E}}{\partial t^2}
\end{equation}
Using the vector Laplacian identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$:
Since $\nabla \cdot \vec{E} = 0$ (Eq. 1):
\begin{equation}
\mathbf{\nabla^2 \vec{E} = \mu \epsilon \frac{\partial^2 \vec{E}}{\partial t^2}}
\end{equation}

\textbf{Step 2: Wave equation for $\vec{H}$}:
Similarly, taking the curl of Eq. (4):
\begin{equation}
\nabla \times (\nabla \times \vec{H}) = \epsilon \frac{\partial}{\partial t} (\nabla \times \vec{E}) = -\mu\epsilon \frac{\partial^2 \vec{H}}{\partial t^2} \implies \mathbf{\nabla^2 \vec{H} = \mu \epsilon \frac{\partial^2 \vec{H}}{\partial t^2}}
\end{equation}

\textbf{Step 3: Speed of light $c$}:
Comparing with the standard 3D classical d'Alembert wave equation $\nabla^2 \psi = \frac{1}{v^2}\frac{\partial^2 \psi}{\partial t^2}$, the propagation velocity is:
\begin{equation}
v = \frac{1}{\sqrt{\mu\epsilon}} = \frac{1}{\sqrt{\mu_0 \mu_r \epsilon_0 \epsilon_r}} = \frac{c}{\sqrt{\mu_r \epsilon_r}}
\end{equation}
In vacuum ($\mu_r = 1, \epsilon_r = 1$):
\begin{equation}
c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} = \frac{1}{\sqrt{(4\pi \times 10^{-7}\text{ H/m})(8.854 \times 10^{-12}\text{ F/m})}} \approx 2.9979 \times 10^8\text{ m/s} \approx 3 \times 10^8\text{ m/s}
\end{equation}"""
        ),
        (
            r"Prove analytically that electromagnetic waves in free space are strictly transverse in nature ($\vec{k} \cdot \vec{E} = 0$ and $\vec{k} \cdot \vec{H} = 0$), and show that $\vec{E}$, $\vec{H}$, and the wave propagation vector $\vec{k}$ form a mutually orthogonal right-handed triad.",
            r"""\textbf{1. Plane Wave Representation}:
Consider a uniform plane wave propagating along direction $\vec{k}$ with angular frequency $\omega$. In complex exponential notation:
\begin{equation}
\vec{E}(\vec{r},t) = \vec{E}_0 e^{i(\omega t - \vec{k}\cdot\vec{r})}, \qquad \vec{H}(\vec{r},t) = \vec{H}_0 e^{i(\omega t - \vec{k}\cdot\vec{r})}
\end{equation}
where the differential spatial operator becomes $\nabla \equiv -i\vec{k}$ and the time derivative becomes $\frac{\partial}{\partial t} \equiv i\omega$.

\textbf{2. Transverse Nature}:
Applying Gauss's Law in charge-free space ($\nabla \cdot \vec{E} = 0$):
\begin{equation}
\nabla \cdot \vec{E} = (-i\vec{k}) \cdot \left[ \vec{E}_0 e^{i(\omega t - \vec{k}\cdot\vec{r})} \right] = -i(\vec{k} \cdot \vec{E}) = 0 \implies \mathbf{\vec{k} \cdot \vec{E} = 0}
\end{equation}
Applying Gauss's Law for magnetism ($\nabla \cdot \vec{B} = 0$):
\begin{equation}
\nabla \cdot \vec{H} = (-i\vec{k}) \cdot \vec{H} = -i(\vec{k} \cdot \vec{H}) = 0 \implies \mathbf{\vec{k} \cdot \vec{H} = 0}
\end{equation}
Since the dot product of $\vec{k}$ with both $\vec{E}$ and $\vec{H}$ is identically zero, neither the electric field nor the magnetic field has any longitudinal component along the direction of propagation. Thus, electromagnetic waves are strictly transverse.

\textbf{3. Mutual Orthogonality}:
Applying Faraday's Law ($\nabla \times \vec{E} = -\mu_0 \frac{\partial \vec{H}}{\partial t}$):
\begin{equation}
(-i\vec{k}) \times \vec{E} = -\mu_0 (i\omega \vec{H}) \implies \vec{k} \times \vec{E} = \omega \mu_0 \vec{H} \implies \mathbf{\vec{H} = \frac{\vec{k} \times \vec{E}}{\omega \mu_0}}
\end{equation}
Because the cross product $\vec{k} \times \vec{E}$ produces a vector perpendicular to both $\vec{k}$ and $\vec{E}$, $\vec{H}$ is strictly perpendicular to $\vec{E}$ ($\vec{E} \cdot \vec{H} = 0$).
Consequently, the unit vectors satisfy $\hat{E} \times \hat{H} = \hat{k}$, forming an orthogonal, right-handed triad."""
        ),
        (
            r"State and derive Poynting's Theorem from Maxwell's curl equations. Give the physical interpretation of each mathematical term in the resulting energy conservation equation.",
            r"""\textbf{1. Derivation}:
Start with Maxwell's two curl equations:
\begin{align}
\nabla \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} \\
\nabla \times \vec{H} &= \vec{J} + \frac{\partial \vec{D}}{\partial t}
\end{align}
Recall the vector identity for the divergence of a cross product:
\begin{equation}
\nabla \cdot (\vec{E} \times \vec{H}) = \vec{H} \cdot (\nabla \times \vec{E}) - \vec{E} \cdot (\nabla \times \vec{H})
\end{equation}
Substituting Eqs. (1) and (2) into the identity:
\begin{equation}
\nabla \cdot (\vec{E} \times \vec{H}) = \vec{H} \cdot \left( -\frac{\partial \vec{B}}{\partial t} \right) - \vec{E} \cdot \left( \vec{J} + \frac{\partial \vec{D}}{\partial t} \right)
\end{equation}
Using $\vec{D} = \epsilon \vec{E}$ and $\vec{B} = \mu \vec{H}$:
\begin{align}
\vec{H} \cdot \frac{\partial \vec{B}}{\partial t} &= \mu \vec{H} \cdot \frac{\partial \vec{H}}{\partial t} = \frac{\partial}{\partial t}\left( \frac{1}{2}\mu H^2 \right) \\
\vec{E} \cdot \frac{\partial \vec{D}}{\partial t} &= \epsilon \vec{E} \cdot \frac{\partial \vec{E}}{\partial t} = \frac{\partial}{\partial t}\left( \frac{1}{2}\epsilon E^2 \right)
\end{align}
Substituting back into the divergence equation:
\begin{equation}
\nabla \cdot (\vec{E} \times \vec{H}) = -\frac{\partial}{\partial t}\left( \frac{1}{2}\epsilon E^2 + \frac{1}{2}\mu H^2 \right) - \vec{J}\cdot\vec{E}
\end{equation}
Defining the Poynting vector $\vec{S} = \vec{E} \times \vec{H}$ and total electromagnetic energy density $u = \frac{1}{2}\epsilon E^2 + \frac{1}{2}\mu H^2$:
\begin{equation}
\mathbf{\nabla \cdot \vec{S} + \frac{\partial u}{\partial t} = -\vec{J}\cdot\vec{E}}
\end{equation}

\textbf{2. Integral Form \& Physical Interpretation}:
Integrating over a volume $V$ bounded by surface $S$ and applying Gauss's Divergence Theorem:
\begin{equation}
\mathbf{\oiint_S \vec{S}\cdot d\vec{S} + \frac{\partial}{\partial t}\iiint_V u\,dV = -\iiint_V (\vec{J}\cdot\vec{E})\,dV}
\end{equation}
\begin{itemize}
    \item $\oiint_S \vec{S}\cdot d\vec{S}$: Net rate of total electromagnetic power escaping outward across boundary surface $S$.
    \item $\frac{\partial}{\partial t}\iiint_V u\,dV$: Time rate of decrease of total stored electric and magnetic energy inside volume $V$.
    \item $\iiint_V (\vec{J}\cdot\vec{E})\,dV$: Total Ohmic Joule heating rate and mechanical work performed by field forces on moving charge carriers.
\end{itemize}"""
        ),
        (
            r"Derive the wave equation for an electromagnetic wave propagating inside a lossy conducting medium ($\sigma \ne 0$). Derive the expressions for the attenuation constant $\alpha$, phase constant $\beta$, and skin depth $\delta$.",
            r"""\textbf{1. Wave Equation in a Conducting Medium}:
For a linear, homogeneous conducting medium with conductivity $\sigma$, permittivity $\epsilon$, and permeability $\mu$:
\begin{equation}
\nabla \cdot \vec{E} = 0, \quad \nabla \times \vec{E} = -\mu\frac{\partial \vec{H}}{\partial t}, \quad \nabla \times \vec{H} = \sigma\vec{E} + \epsilon\frac{\partial \vec{E}}{\partial t}
\end{equation}
Taking the curl of Faraday's Law:
\begin{equation}
\nabla \times (\nabla \times \vec{E}) = -\mu \frac{\partial}{\partial t}(\nabla \times \vec{H}) = -\mu \frac{\partial}{\partial t}\left(\sigma \vec{E} + \epsilon \frac{\partial \vec{E}}{\partial t}\right)
\end{equation}
Using $\nabla \times (\nabla \times \vec{E}) = -\nabla^2 \vec{E}$:
\begin{equation}
\mathbf{\nabla^2 \vec{E} = \mu \sigma \frac{\partial \vec{E}}{\partial t} + \mu \epsilon \frac{\partial^2 \vec{E}}{\partial t^2}}
\end{equation}

\textbf{2. Complex Propagation Constant $\gamma$}:
Assuming time-harmonic fields $\vec{E}(\vec{r},t) = \vec{E}_0 e^{i\omega t - \gamma z}\hat{a}_x$:
\begin{equation}
\frac{d^2 \vec{E}}{dz^2} = \gamma^2 \vec{E} \implies \gamma^2 = i\omega\mu\sigma - \omega^2\mu\epsilon = i\omega\mu(\sigma + i\omega\epsilon)
\end{equation}
Let $\gamma = \alpha + i\beta$:
\begin{equation}
\gamma^2 = (\alpha^2 - \beta^2) + 2i\alpha\beta = -\omega^2\mu\epsilon + i\omega\mu\sigma
\end{equation}
Equating real and imaginary parts:
\begin{align}
\alpha^2 - \beta^2 &= -\omega^2\mu\epsilon \\
2\alpha\beta &= \omega\mu\sigma
\end{align}
Solving this system of equations yields:
\begin{align}
\mathbf{\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} - 1\right]}}, \qquad
\mathbf{\beta = \omega\sqrt{\frac{\mu\epsilon}{2}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} + 1\right]}}
\end{align}

\textbf{3. Good Conductor Limit ($\sigma \gg \omega\epsilon$) \& Skin Depth}:
When $\sigma/(\omega\epsilon) \gg 1$:
\begin{equation}
\alpha \approx \beta \approx \sqrt{\frac{\omega \mu \sigma}{2}} = \sqrt{\pi f \mu \sigma}
\end{equation}
The electric field amplitude decays with penetration depth $z$ as $E(z) = E_0 e^{-\alpha z}$.
The skin depth $\delta$ is defined as the depth where $E(\delta) = E_0 e^{-1}$:
\begin{equation}
\alpha \delta = 1 \implies \mathbf{\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega \mu \sigma}} = \frac{1}{\sqrt{\pi f \mu \sigma}}}
\end{equation}"""
        ),
        (
            r"State and derive the electromagnetic boundary conditions for $\vec{D}, \vec{E}, \vec{B},$ and $\vec{H}$ at an interface separating two different dielectric media with surface charge density $\rho_s$ and surface current density $\vec{K}_s$.",
            r"""Consider a planar boundary separating Medium 1 ($\epsilon_1, \mu_1$) and Medium 2 ($\epsilon_2, \mu_2$) with unit normal $\hat{n}_{12}$ pointing from Medium 1 into Medium 2.

\textbf{1. Normal Component of $\vec{D}$}:
Construct a pillbox Gaussian cylinder of area $\Delta S$ and vanishing height $h \to 0$ across the interface. Applying Gauss's law $\oiint \vec{D}\cdot d\vec{S} = Q_{\text{enc}}$:
\begin{equation}
(\vec{D}_2 \cdot \hat{n}_{12})\Delta S - (\vec{D}_1 \cdot \hat{n}_{12})\Delta S = \rho_s \Delta S \implies \mathbf{(D_{2n} - D_{1n}) = \rho_s \iff \hat{n}_{12}\cdot(\vec{D}_2 - \vec{D}_1) = \rho_s}
\end{equation}
If no free surface charges exist ($\rho_s = 0$), $D_{1n} = D_{2n}$ (continuous).

\textbf{2. Normal Component of $\vec{B}$}:
Applying Gauss's law for magnetism $\oiint \vec{B}\cdot d\vec{S} = 0$ to the same pillbox:
\begin{equation}
(\vec{B}_2 \cdot \hat{n}_{12})\Delta S - (\vec{B}_1 \cdot \hat{n}_{12})\Delta S = 0 \implies \mathbf{B_{1n} = B_{2n} \iff \hat{n}_{12}\cdot(\vec{B}_2 - \vec{B}_1) = 0}
\end{equation}
The normal component of magnetic flux density is \textit{always} continuous across any interface.

\textbf{3. Tangential Component of $\vec{E}$}:
Construct a rectangular contour of length $\Delta l$ parallel to interface and vanishing width $w \to 0$. Applying Faraday's law $\oint \vec{E}\cdot d\vec{l} = -\iint \frac{\partial\vec{B}}{\partial t}\cdot d\vec{S}$:
As $w \to 0$, magnetic flux through the loop vanishes:
\begin{equation}
(E_{2t} - E_{1t})\Delta l = 0 \implies \mathbf{E_{1t} = E_{2t} \iff \hat{n}_{12}\times(\vec{E}_2 - \vec{E}_1) = 0}
\end{equation}
The tangential component of the electric field is \textit{always} continuous across boundaries.

\textbf{4. Tangential Component of $\vec{H}$}:
Applying the Ampere--Maxwell law $\oint \vec{H}\cdot d\vec{l} = I_{\text{enc}} + \iint \frac{\partial\vec{D}}{\partial t}\cdot d\vec{S}$ to the loop:
As $w \to 0$, displacement current flux vanishes, leaving only surface current $I_{\text{enc}} = \vec{K}_s \cdot (\hat{n}_{12} \times \Delta\vec{l})$:
\begin{equation}
\mathbf{\hat{n}_{12} \times (\vec{H}_2 - \vec{H}_1) = \vec{K}_s \iff H_{1t} - H_{2t} = K_s}
\end{equation}
If no surface conduction currents exist ($\vec{K}_s = 0$), $H_{1t} = H_{2t}$ (continuous)."""
        ),
        (
            r"Derive the reflection coefficient $\Gamma$ and transmission coefficient $\tau$ for a uniform plane electromagnetic wave incident normally on a plane interface between two lossless dielectric media.",
            r"""\textbf{1. Wave Formulations}:
Let a plane wave traveling in $+z$ direction in Medium 1 ($\epsilon_1, \mu_1, \eta_1$) hit a boundary at $z=0$ with Medium 2 ($\epsilon_2, \mu_2, \eta_2$).
\begin{align*}
\text{Incident Wave:}\quad &\vec{E}_i(z) = E_{0i} e^{-i k_1 z}\hat{a}_x, \quad \vec{H}_i(z) = \frac{E_{0i}}{\eta_1} e^{-i k_1 z}\hat{a}_y \\
\text{Reflected Wave:}\quad &\vec{E}_r(z) = E_{0r} e^{+i k_1 z}\hat{a}_x, \quad \vec{H}_r(z) = -\frac{E_{0r}}{\eta_1} e^{+i k_1 z}\hat{a}_y \\
\text{Transmitted Wave:}\quad &\vec{E}_t(z) = E_{0t} e^{-i k_2 z}\hat{a}_x, \quad \vec{H}_t(z) = \frac{E_{0t}}{\eta_2} e^{-i k_2 z}\hat{a}_y
\end{align*}

\textbf{2. Applying Boundary Conditions at $z=0$}:
\begin{enumerate}
    \item Continuity of tangential $\vec{E}$: $E_i(0) + E_r(0) = E_t(0) \implies E_{0i} + E_{0r} = E_{0t}$
    \item Continuity of tangential $\vec{H}$: $H_i(0) + H_r(0) = H_t(0) \implies \frac{E_{0i}}{\eta_1} - \frac{E_{0r}}{\eta_1} = \frac{E_{0t}}{\eta_2}$
\end{enumerate}

\textbf{3. Solving for Coefficients}:
From equation (2):
\begin{equation}
E_{0i} - E_{0r} = \frac{\eta_1}{\eta_2} E_{0t}
\end{equation}
Adding equations (1) and (3):
\begin{equation}
2 E_{0i} = \left(1 + \frac{\eta_1}{\eta_2}\right)E_{0t} = \left(\frac{\eta_1 + \eta_2}{\eta_2}\right)E_{0t} \implies \mathbf{\tau = \frac{E_{0t}}{E_{0i}} = \frac{2\eta_2}{\eta_1 + \eta_2}}
\end{equation}
Subtracting equation (3) from equation (1):
\begin{equation}
2 E_{0r} = \left(1 - \frac{\eta_1}{\eta_2}\right)E_{0t} = \left(\frac{\eta_2 - \eta_1}{\eta_2}\right)\left(\frac{2\eta_2}{\eta_1 + \eta_2}E_{0i}\right) \implies \mathbf{\Gamma = \frac{E_{0r}}{E_{0i}} = \frac{\eta_2 - \eta_1}{\eta_1 + \eta_2}}
\end{equation}
Notice that $1 + \Gamma = 1 + \frac{\eta_2 - \eta_1}{\eta_1 + \eta_2} = \frac{2\eta_2}{\eta_1 + \eta_2} = \tau$."""
        ),
        (
            r"Derive the relationship between radiation pressure $P_{\text{rad}}$ and time-averaged Poynting flux $\langle S \rangle$ for: (a) a perfectly absorbing surface, and (b) a perfectly reflecting mirror.",
            r"""\textbf{1. Momentum of Electromagnetic Radiation}:
According to Maxwell's theory and quantum electrodynamics, an electromagnetic wave packet of total energy $U$ carries linear momentum:
\begin{equation}
p = \frac{U}{c}
\end{equation}
When radiation with time-averaged power flux density $\langle S \rangle$ falls normally on a surface of area $A$, the energy incident in time $\Delta t$ is:
\begin{equation}
\Delta U = \langle S \rangle A \Delta t
\end{equation}
The total momentum incident on the surface in time $\Delta t$ is:
\begin{equation}
\Delta p_{\text{inc}} = \frac{\Delta U}{c} = \frac{\langle S \rangle A \Delta t}{c}
\end{equation}

\textbf{2. Case (a): Perfectly Absorbing Surface}:
All incident radiation is absorbed, so the final momentum of reflected light is zero:
\begin{equation}
\Delta p_{\text{transferred}} = \Delta p_{\text{inc}} - 0 = \frac{\langle S \rangle A \Delta t}{c}
\end{equation}
By Newton's second law, radiation force $F = \frac{\Delta p}{\Delta t} = \frac{\langle S \rangle A}{c}$.
The radiation pressure is force per unit area:
\begin{equation}
\mathbf{P_{\text{rad, abs}} = \frac{F}{A} = \frac{\langle S \rangle}{c} = u}
\end{equation}
where $u$ is the energy density of the incident wave.

\textbf{3. Case (b): Perfectly Reflecting Surface}:
The radiation is completely reflected with reversed momentum ($\Delta p_{\text{final}} = -\Delta p_{\text{inc}}$):
\begin{equation}
\Delta p_{\text{transferred}} = \Delta p_{\text{inc}} - (-\Delta p_{\text{inc}}) = 2\Delta p_{\text{inc}} = \frac{2\langle S \rangle A \Delta t}{c}
\end{equation}
The resulting radiation force and radiation pressure are:
\begin{equation}
\mathbf{P_{\text{rad, refl}} = \frac{F}{A} = \frac{2\langle S \rangle}{c} = 2u}
\end{equation}
The radiation pressure on a perfectly reflecting mirror is exactly double that on a perfectly absorbing surface."""
        ),
        (
            r"Explain the concept of gauge transformations in electrodynamics. Derive the decoupling of scalar potential $V$ and vector potential $\vec{A}$ wave equations under the Lorenz gauge condition.",
            r"""\textbf{1. Potentials and Gauge Freedom}:
From $\nabla \cdot \vec{B} = 0$, we define $\vec{B} = \nabla \times \vec{A}$.
Substituting into Faraday's Law $\nabla \times \vec{E} = -\frac{\partial}{\partial t}(\nabla \times \vec{A}) \implies \nabla \times \left(\vec{E} + \frac{\partial \vec{A}}{\partial t}\right) = 0$.
Since this curl vanishes, the quantity can be expressed as $-\nabla V$:
\begin{equation}
\vec{E} = -\nabla V - \frac{\partial \vec{A}}{\partial t}
\end{equation}
The physical fields $\vec{E}$ and $\vec{B}$ remain invariant under the gauge transformations:
\begin{equation}
\vec{A}' = \vec{A} + \nabla \lambda, \qquad V' = V - \frac{\partial \lambda}{\partial t}
\end{equation}
where $\lambda(\vec{r},t)$ is any arbitrary scalar gauge function.

\textbf{2. Derivation of Coupled Equations}:
Substituting $\vec{E}$ and $\vec{B}$ into Maxwell's source equations:
\begin{enumerate}
    \item Gauss's law $\nabla \cdot \vec{E} = \rho/\epsilon_0$:
    \begin{equation}
    \nabla \cdot \left(-\nabla V - \frac{\partial \vec{A}}{\partial t}\right) = \frac{\rho}{\epsilon_0} \implies \nabla^2 V + \frac{\partial}{\partial t}(\nabla \cdot \vec{A}) = -\frac{\rho}{\epsilon_0}
    \end{equation}
    \item Ampere--Maxwell law $\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0\epsilon_0 \frac{\partial \vec{E}}{\partial t}$:
    \begin{equation}
    \nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2 \vec{A} = \mu_0 \vec{J} + \mu_0\epsilon_0 \frac{\partial}{\partial t}\left(-\nabla V - \frac{\partial \vec{A}}{\partial t}\right)
    \end{equation}
    Rearranging:
    \begin{equation}
    \nabla^2 \vec{A} - \mu_0\epsilon_0 \frac{\partial^2 \vec{A}}{\partial t^2} - \nabla\left(\nabla \cdot \vec{A} + \mu_0\epsilon_0 \frac{\partial V}{\partial t}\right) = -\mu_0 \vec{J}
    \end{equation}
\end{enumerate}

\textbf{3. Lorenz Gauge Decoupling}:
To decouple these equations, we choose the Lorenz gauge condition:
\begin{equation}
\mathbf{\nabla \cdot \vec{A} + \mu_0\epsilon_0 \frac{\partial V}{\partial t} = 0}
\end{equation}
Substituting this gauge condition into Eqs. (1) and (2) gives two symmetric, decoupled 3D inhomogeneous wave equations:
\begin{align}
\mathbf{\nabla^2 V - \frac{1}{c^2}\frac{\partial^2 V}{\partial t^2} = -\frac{\rho}{\epsilon_0}} \\
\mathbf{\nabla^2 \vec{A} - \frac{1}{c^2}\frac{\partial^2 \vec{A}}{\partial t^2} = -\mu_0 \vec{J}}
\end{align}"""
        ),
        (
            r"A circular parallel-plate capacitor with radius $R = 8.0\text{ cm}$ and plate separation $d = 2.0\text{ mm}$ is charged by a current $I(t) = 5.0\sin(100\pi t)\text{ A}$. Calculate: (a) displacement current density $J_d(t)$, (b) displacement current $I_d(t)$, and (c) induced magnetic field $B(r,t)$ at $r = 4.0\text{ cm}$ and $r = 12.0\text{ cm}$.",
            r"""\textbf{1. Displacement Current Density $J_d(t)$}:
Inside the capacitor, all current is displacement current, uniformly distributed across plate area $A = \pi R^2$:
\begin{equation}
J_d(t) = \frac{I(t)}{\pi R^2} = \frac{5.0\sin(100\pi t)}{\pi (0.08)^2} = \frac{5.0}{0.020106}\sin(100\pi t) \approx \mathbf{248.7\sin(100\pi t)\text{ A/m}^2}
\end{equation}

\textbf{2. Displacement Current $I_d(t)$}:
Total displacement current between plates equals conduction current in lead wires:
\begin{equation}
\mathbf{I_d(t) = \iint J_d(t)\,dA = I(t) = 5.0\sin(100\pi t)\text{ A}}
\end{equation}

\textbf{3. Induced Magnetic Field}:
Applying Ampere--Maxwell law along a circular loop of radius $r$:
\begin{equation}
\oint \vec{B}\cdot d\vec{l} = B(2\pi r) = \mu_0 I_{\text{enclosed}}
\end{equation}
\begin{itemize}
    \item For $r = 4.0\text{ cm} < R$:
    \begin{align*}
    I_{\text{encl}} &= I_d(t)\left(\frac{r}{R}\right)^2 = 5.0\sin(100\pi t)\left(\frac{0.04}{0.08}\right)^2 = 1.25\sin(100\pi t)\text{ A} \\
    B(0.04, t) &= \frac{\mu_0 I_{\text{encl}}}{2\pi r} = \frac{(4\pi \times 10^{-7})(1.25\sin(100\pi t))}{2\pi (0.04)} = \mathbf{6.25 \times 10^{-6}\sin(100\pi t)\text{ T}}
    \end{align*}
    \item For $r = 12.0\text{ cm} > R$:
    The loop encloses the entire capacitor displacement current $I_d = 5.0\sin(100\pi t)\text{ A}$:
    \begin{align*}
    B(0.12, t) &= \frac{\mu_0 I_d(t)}{2\pi r} = \frac{(4\pi \times 10^{-7})(5.0\sin(100\pi t))}{2\pi (0.12)} \approx \mathbf{8.33 \times 10^{-6}\sin(100\pi t)\text{ T}}
    \end{align*}
\end{itemize}"""
        ),
        (
            r"An electromagnetic plane wave propagating in free space has electric field $\vec{E}(z,t) = 150 \cos(3\pi \times 10^8 t - \pi z)\hat{a}_x\text{ V/m}$. Determine: (a) frequency $\nu$ and wavelength $\lambda$, (b) direction of propagation, (c) magnetic field expression $\vec{H}(z,t)$, (d) average Poynting vector $\langle \vec{S} \rangle$, and (e) average energy density $u_{\text{avg}}$.",
            r"""\textbf{1. Frequency $\nu$ and Wavelength $\lambda$}:
Comparing with $\vec{E}(z,t) = E_0 \cos(\omega t - kz)\hat{a}_x$:
\begin{align*}
\omega &= 3\pi \times 10^8\text{ rad/s} \implies \nu = \frac{\omega}{2\pi} = \frac{3\pi \times 10^8}{2\pi} = \mathbf{1.5 \times 10^8\text{ Hz} = 150\text{ MHz}} \\
k &= \pi\text{ rad/m} \implies \lambda = \frac{2\pi}{k} = \frac{2\pi}{\pi} = \mathbf{2.0\text{ m}}
\end{align*}

\textbf{2. Direction of Propagation}:
The phase factor $(\omega t - kz)$ corresponds to propagation along the \textbf{positive $z$-axis ($+\hat{a}_z$)}.

\textbf{3. Magnetic Field $\vec{H}(z,t)$}:
Wave impedance of free space is $\eta_0 = 120\pi \approx 377\,\Omega$.
Amplitude $H_0 = E_0 / \eta_0 = 150 / 377 \approx 0.398\text{ A/m}$.
Direction $\hat{a}_H = \hat{a}_k \times \hat{a}_E = \hat{a}_z \times \hat{a}_x = \hat{a}_y$.
\begin{equation}
\mathbf{\vec{H}(z,t) = 0.398 \cos(3\pi \times 10^8 t - \pi z)\hat{a}_y\text{ A/m}}
\end{equation}

\textbf{4. Time-Averaged Poynting Vector $\langle \vec{S} \rangle$}:
\begin{equation}
\mathbf{\langle \vec{S} \rangle = \frac{1}{2} E_0 H_0 \hat{a}_z = \frac{1}{2}(150)(0.398)\hat{a}_z \approx 29.85\hat{a}_z\text{ W/m}^2}
\end{equation}

\textbf{5. Average Energy Density $u_{\text{avg}}$}:
\begin{equation}
\mathbf{u_{\text{avg}} = \frac{1}{2}\epsilon_0 E_0^2 = \frac{1}{2}(8.854 \times 10^{-12})(150)^2 \approx 9.96 \times 10^{-8}\text{ J/m}^3}
\end{equation}
Notice $\langle S \rangle = u_{\text{avg}} c = (9.96 \times 10^{-8})(3 \times 10^8) \approx 29.88\text{ W/m}^2$, matching exactly."""
        ),
        (
            r"Calculate the skin depth and wave propagation speed in copper ($\sigma = 5.8 \times 10^7\text{ S/m}, \mu_r = 1$) at: (a) Power frequency ($f = 50\text{ Hz}$), (b) Radio frequency ($f = 1.0\text{ MHz}$), and (c) Microwave frequency ($f = 10\text{ GHz}$). Discuss the engineering implications.",
            r"""\textbf{1. Formulae}:
\begin{equation}
\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}, \qquad v_p = \omega \delta = 2\pi f \delta = \sqrt{\frac{4\pi f}{\mu \sigma}}
\end{equation}
Here $\mu = \mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ and $\sigma = 5.8 \times 10^7\text{ S/m}$.

\textbf{2. Calculations}:
\begin{itemize}
    \item \textbf{(a) Power Frequency ($f = 50\text{ Hz}$)}:
    \begin{align*}
    \delta &= \frac{1}{\sqrt{\pi (50)(4\pi\times 10^{-7})(5.8\times 10^7)}} = \frac{1}{\sqrt{11448.6}} \approx \mathbf{9.35\text{ mm}} \\
    v_p &= 2\pi (50)(9.35 \times 10^{-3}) \approx \mathbf{2.94\text{ m/s}}
    \end{align*}
    \item \textbf{(b) Radio Frequency ($f = 1.0\text{ MHz} = 10^6\text{ Hz}$)}:
    \begin{align*}
    \delta &= \frac{9.35\text{ mm}}{\sqrt{10^6 / 50}} = \frac{9.35 \times 10^{-3}}{\sqrt{20000}} \approx \mathbf{66.1\,\mu\text{m}} \\
    v_p &= 2\pi (10^6)(66.1 \times 10^{-6}) \approx \mathbf{415.3\text{ m/s}}
    \end{align*}
    \item \textbf{(c) Microwave Frequency ($f = 10\text{ GHz} = 10^{10}\text{ Hz}$)}:
    \begin{align*}
    \delta &= \frac{66.1\,\mu\text{m}}{\sqrt{10^{10}/10^6}} = \frac{66.1\,\mu\text{m}}{100} \approx \mathbf{0.661\,\mu\text{m} = 661\text{ nm}} \\
    v_p &= 2\pi (10^{10})(6.61 \times 10^{-7}) \approx \mathbf{4.15 \times 10^4\text{ m/s}}
    \end{align*}
\end{itemize}

\textbf{3. Engineering Implications}:
\begin{itemize}
    \item At radio and microwave frequencies, currents are restricted to a microscopic surface layer ($\delta < 66\,\mu\text{m}$). Solid thick wires waste metal because the center carries negligible current.
    \item RF systems utilize hollow waveguides, silver-plated copper tubes, or multi-strand Litz wire to minimize high-frequency AC resistance and skin losses.
\end{itemize}"""
        ),
        (
            r"Prove that the total power flowing through a coaxial cable carrying current $I$ at potential difference $V$, as calculated from Poynting vector integration across the dielectric insulator, is exactly equal to $P = V I$.",
            r"""\textbf{1. Coaxial Cable Geometry \& Fields}:
Consider a coaxial cable with inner conductor radius $a$, outer conductor inner radius $b$, carrying direct current $I$ along $+z$ on the inner conductor and returning on the outer conductor, with potential difference $V$ across conductors.
In cylindrical coordinates $(\rho, \phi, z)$ within the dielectric region ($a \le \rho \le b$):
\begin{enumerate}
    \item Electric field $\vec{E}$:
    \begin{equation}
    V = -\int_b^a \vec{E}\cdot d\vec{\rho} = \int_a^b \frac{\lambda_L}{2\pi\epsilon\rho}\,d\rho = \frac{\lambda_L}{2\pi\epsilon}\ln\left(\frac{b}{a}\right) \implies \vec{E}(\rho) = \frac{V}{\rho \ln(b/a)}\hat{a}_\rho
    \end{equation}
    \item Magnetic field $\vec{H}$:
    By Ampere's circuital law $\oint \vec{H}\cdot d\vec{l} = H(2\pi\rho) = I$:
    \begin{equation}
    \vec{H}(\rho) = \frac{I}{2\pi \rho}\hat{a}_\phi
    \end{equation}
\end{enumerate}

\textbf{2. Poynting Vector Computation}:
\begin{equation}
\vec{S} = \vec{E} \times \vec{H} = \left( \frac{V}{\rho \ln(b/a)}\hat{a}_\rho \right) \times \left( \frac{I}{2\pi \rho}\hat{a}_phi \right) = \frac{V I}{2\pi \ln(b/a)\rho^2}\hat{a}_z
\end{equation}
The Poynting vector is strictly axial ($\hat{a}_z$), showing that electrical energy is transported entirely through the dielectric field, not inside the copper conductors!

\textbf{3. Integration Over Dielectric Cross-Section}:
Differential surface area element normal to $\hat{a}_z$ is $d\vec{A} = \rho\,d\rho\,d\phi\,\hat{a}_z$:
\begin{align*}
P_{\text{total}} &= \iint_S \vec{S} \cdot d\vec{A} = \int_0^{2\pi} d\phi \int_a^b \left( \frac{V I}{2\pi \ln(b/a)\rho^2} \right) \rho\,d\rho \\
&= (2\pi) \frac{V I}{2\pi \ln(b/a)} \int_a^b \frac{1}{\rho}\,d\rho = \frac{V I}{\ln(b/a)} \left[ \ln\rho \right]_a^b = \frac{V I}{\ln(b/a)} \ln\left(\frac{b}{a}\right) = \mathbf{V I}
\end{align*}
This rigorous proof demonstrates the equivalence of classical circuit theory ($P = VI$) and electromagnetic field power transport."""
        ),
        (
            r"Derive the relationship between the attenuation of an electromagnetic wave in a lossy dielectric and its complex permittivity $\hat{\epsilon} = \epsilon' - i\epsilon''$. Define loss tangent and quality factor $Q$.",
            r"""\textbf{1. Complex Permittivity Formalism}:
In a lossy dielectric medium with conductivity $\sigma$ and real permittivity $\epsilon'$, Maxwell's curl equation for $\vec{H}$ is:
\begin{equation}
\nabla \times \vec{H} = \sigma \vec{E} + \epsilon'\frac{\partial \vec{E}}{\partial t} = (\sigma + i\omega\epsilon')\vec{E} = i\omega \left(\epsilon' - i\frac{\sigma}{\omega}\right)\vec{E}
\end{equation}
Defining the complex permittivity $\hat{\epsilon} = \epsilon' - i\epsilon''$, where $\epsilon'' = \frac{\sigma}{\omega} + \epsilon''_{\text{damping}}$:
\begin{equation}
\nabla \times \vec{H} = i\omega \hat{\epsilon} \vec{E} = i\omega (\epsilon' - i\epsilon'')\vec{E}
\end{equation}

\textbf{2. Loss Tangent $\tan\delta$}:
The ratio of the dissipative conduction current density $J_c$ to the reactive displacement current density $J_d$ defines the loss tangent:
\begin{equation}
\mathbf{\tan\delta = \frac{|\vec{J}_c|}{|\vec{J}_d|} = \frac{\sigma}{\omega \epsilon'} = \frac{\epsilon''}{\epsilon'}}
\end{equation}
where $\delta$ is the dielectric loss angle (the phase angle between total current and displacement current).

\textbf{3. Propagation in Low-Loss Dielectrics ($\tan\delta \ll 1$)}:
The propagation constant is $\gamma = i\omega\sqrt{\mu\hat{\epsilon}} = i\omega\sqrt{\mu\epsilon'(1 - i\tan\delta)}$.
Expanding using the binomial theorem $(1 - i\tan\delta)^{1/2} \approx 1 - \frac{i}{2}\tan\delta$:
\begin{equation}
\gamma = i\omega\sqrt{\mu\epsilon'}\left(1 - \frac{i}{2}\tan\delta\right) = \frac{\omega\sqrt{\mu\epsilon'}\tan\delta}{2} + i\omega\sqrt{\mu\epsilon'}
\end{equation}
Thus, attenuation constant $\alpha$ and phase constant $\beta$ are:
\begin{equation}
\mathbf{\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\epsilon'}}}, \qquad \mathbf{\beta \approx \omega\sqrt{\mu\epsilon'}}
\end{equation}

\textbf{4. Quality Factor $Q$}:
The quality factor $Q$ of a dielectric cavity or transmission line is the ratio of stored energy to dissipated energy per cycle:
\begin{equation}
\mathbf{Q = \frac{1}{\tan\delta} = \frac{\epsilon'}{\epsilon''}}
\end{equation}"""
        ),
        (
            r"Explain the physical principle of radiation pressure and derive the formula for the orbital drift or acceleration of a cosmic dust particle under solar radiation pressure versus gravitational pull (Poynting--Robertson effect).",
            r"""\textbf{1. Balance of Forces on a Spherical Dust Particle}:
Consider a spherical dust grain of radius $R$ and mass density $\rho_m$ at a distance $r$ from the Sun (mass $M_\odot$, luminosity $L_\odot = 3.828 \times 10^{26}\text{ W}$).

\textbf{2. Solar Gravitational Force}:
Mass of dust particle $m = \frac{4}{3}\pi R^3 \rho_m$.
\begin{equation}
F_{\text{grav}} = \frac{G M_\odot m}{r^2} = \frac{4\pi G M_\odot \rho_m R^3}{3 r^2}
\end{equation}

\textbf{3. Solar Radiation Force}:
Solar radiative flux at distance $r$ is $S(r) = \frac{L_\odot}{4\pi r^2}$.
Cross-sectional area of particle is $\sigma_{\text{geom}} = \pi R^2$.
Assuming complete absorption, radiation force is:
\begin{equation}
F_{\text{rad}} = \frac{S(r)\sigma_{\text{geom}}}{c} = \frac{L_\odot \pi R^2}{4\pi r^2 c} = \frac{L_\odot R^2}{4 r^2 c}
\end{equation}

\textbf{4. Ratio of Forces \& Critical Particle Size}:
Taking the ratio $\beta_{\text{rad}} = F_{\text{rad}} / F_{\text{grav}}$:
\begin{equation}
\beta_{\text{rad}} = \frac{\frac{L_\odot R^2}{4 r^2 c}}{\frac{4\pi G M_\odot \rho_m R^3}{3 r^2}} = \mathbf{\frac{3 L_\odot}{16\pi G M_\odot \rho_m c}\left(\frac{1}{R}\right)}
\end{equation}
\begin{itemize}
    \item Notice that $\beta_{\text{rad}}$ is independent of orbital distance $r$!
    \item Because $F_{\text{rad}} \propto R^2$ while $F_{\text{grav}} \propto R^3$, for sufficiently small particles ($R < R_{\text{crit}} \approx 0.5\,\mu\text{m}$ for $\rho_m = 2500\text{ kg/m}^3$), $\beta_{\text{rad}} > 1$. Radiation pressure exceeds gravity, blowing fine dust grains entirely out of the Solar System.
\end{itemize}"""
        ),
        (
            r"Derive the wave equations in terms of electromagnetic potentials in a dielectric medium. Show how the Lorentz condition decouples the potentials.",
            r"""\textbf{1. Potentials Formulation}:
Magnetic field is expressed as $\vec{B} = \nabla \times \vec{A}$.
Faraday's law gives $\nabla \times (\vec{E} + \partial\vec{A}/\partial t) = 0 \implies \vec{E} = -\nabla V - \partial\vec{A}/\partial t$.

\textbf{2. Substituting into Inhomogeneous Maxwell Equations}:
In a medium with $\epsilon$ and $\mu$:
\begin{align}
\nabla \cdot \vec{D} = \rho &\implies \nabla \cdot \left(-\epsilon\nabla V - \epsilon\frac{\partial\vec{A}}{\partial t}\right) = \rho \implies \nabla^2 V + \frac{\partial}{\partial t}(\nabla \cdot \vec{A}) = -\frac{\rho}{\epsilon} \\
\nabla \times \vec{H} = \vec{J} + \epsilon\frac{\partial\vec{E}}{\partial t} &\implies \frac{1}{\mu}\nabla \times (\nabla \times \vec{A}) = \vec{J} + \epsilon\frac{\partial}{\partial t}\left(-\nabla V - \frac{\partial\vec{A}}{\partial t}\right)
\end{align}
Using $\nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2 \vec{A}$:
\begin{equation}
\nabla^2 \vec{A} - \mu\epsilon\frac{\partial^2\vec{A}}{\partial t^2} - \nabla\left(\nabla \cdot \vec{A} + \mu\epsilon\frac{\partial V}{\partial t}\right) = -\mu\vec{J}
\end{equation}

\textbf{3. Decoupling via Lorentz Gauge}:
Set $\nabla \cdot \vec{A} + \mu\epsilon\frac{\partial V}{\partial t} = 0 \implies \nabla \cdot \vec{A} = -\mu\epsilon\frac{\partial V}{\partial t}$.
Substituting this into Eq. (1):
\begin{equation}
\nabla^2 V + \frac{\partial}{\partial t}\left(-\mu\epsilon\frac{\partial V}{\partial t}\right) = -\frac{\rho}{\epsilon} \implies \mathbf{\nabla^2 V - \mu\epsilon\frac{\partial^2 V}{\partial t^2} = -\frac{\rho}{\epsilon}}
\end{equation}
Substituting into Eq. (2):
\begin{equation}
\mathbf{\nabla^2 \vec{A} - \mu\epsilon\frac{\partial^2\vec{A}}{\partial t^2} = -\mu\vec{J}}
\end{equation}
Both scalar and vector potentials satisfy uncoupled, identical wave equations propagating at velocity $v = 1/\sqrt{\mu\epsilon}$."""
        ),
        (
            r"A broadcast antenna radiates a total electromagnetic power of $50\text{ kW}$ isotropically into free space. At a distance $r = 10\text{ km}$ from the antenna, calculate: (a) Poynting flux density $\langle S \rangle$, (b) electric field amplitude $E_0$, (c) magnetic field amplitude $H_0$, and (d) total radiation force on a $2.5\text{ m} \times 2.0\text{ m}$ reflective billboard.",
            r"""\textbf{1. Poynting Flux Density $\langle S \rangle$}:
For isotropic radiation over a sphere of radius $r = 10^4\text{ m}$:
\begin{equation}
\mathbf{\langle S \rangle = \frac{P_{\text{total}}}{4\pi r^2} = \frac{50 \times 10^3}{4\pi (10^4)^2} = \frac{50 \times 10^3}{1.2566 \times 10^9} \approx 3.98 \times 10^{-5}\text{ W/m}^2 = 39.8\,\mu\text{W/m}^2}
\end{equation}

\textbf{2. Electric Field Amplitude $E_0$}:
\begin{equation}
\langle S \rangle = \frac{E_0^2}{2\eta_0} \implies \mathbf{E_0 = \sqrt{2\eta_0 \langle S \rangle} = \sqrt{2(377)(3.98 \times 10^{-5})} \approx 0.173\text{ V/m} = 173\text{ mV/m}}
\end{equation}

\textbf{3. Magnetic Field Amplitude $H_0$}:
\begin{equation}
\mathbf{H_0 = \frac{E_0}{\eta_0} = \frac{0.173}{377} \approx 4.59 \times 10^{-4}\text{ A/m} = 459\,\mu\text{A/m}}
\end{equation}

\textbf{4. Total Radiation Force on Reflective Billboard}:
Area of billboard $A = 2.5 \times 2.0 = 5.0\text{ m}^2$.
For a perfectly reflecting billboard:
\begin{equation}
\mathbf{F = \frac{2\langle S \rangle A}{c} = \frac{2(3.98 \times 10^{-5})(5.0)}{3 \times 10^8} \approx 1.33 \times 10^{-12}\text{ N}}
\end{equation}"""
        ),
        (
            r"Derive the relationship between electric field $\vec{E}$ and magnetic field $\vec{B}$ in a standing electromagnetic wave formed by the perfect reflection of a plane wave at normal incidence from a conducting plane.",
            r"""\textbf{1. Incident and Reflected Waves}:
Let a plane wave $\vec{E}_i(z,t) = E_0 \cos(\omega t - kz)\hat{i}$ hit a perfectly conducting plane located at $z=0$.
At the conducting boundary $z=0$, the total tangential electric field must vanish ($E_t = 0$):
\begin{equation}
\vec{E}_{\text{total}}(0,t) = \vec{E}_i(0,t) + \vec{E}_r(0,t) = 0 \implies \vec{E}_r(0,t) = -\vec{E}_i(0,t)
\end{equation}
Thus, the reflected electric field is $\vec{E}_r(z,t) = -E_0 \cos(\omega t + kz)\hat{i}$.

\textbf{2. Resultant Standing Electric Wave}:
\begin{align*}
\vec{E}_{\text{total}}(z,t) &= E_0 [\cos(\omega t - kz) - \cos(\omega t + kz)]\hat{i} \\
&= E_0 [2\sin(\omega t)\sin(kz)]\hat{i} = \mathbf{2 E_0 \sin(kz)\sin(\omega t)\hat{i}}
\end{align*}
Nodes of $\vec{E}$ occur at $kz = n\pi \implies z = -n\frac{\lambda}{2}$ ($n=0, 1, 2,\dots$).

\textbf{3. Corresponding Magnetic Wave}:
Incident $\vec{B}_i = \frac{E_0}{c}\cos(\omega t - kz)\hat{j}$; reflected $\vec{B}_r = \frac{E_0}{c}\cos(\omega t + kz)\hat{j}$:
\begin{align*}
\vec{B}_{\text{total}}(z,t) &= \frac{E_0}{c}[\cos(\omega t - kz) + \cos(\omega t + kz)]\hat{j} = \mathbf{\frac{2 E_0}{c}\cos(kz)\cos(\omega t)\hat{j}}
\end{align*}
Nodes of $\vec{B}$ occur at $kz = (n + \frac{1}{2})\pi \implies z = -(2n+1)\frac{\lambda}{4}$.

\textbf{4. Physical Analysis}:
\begin{itemize}
    \item Electric and magnetic fields are separated in space by $\lambda/4$ (antinodes of $\vec{E}$ coincide with nodes of $\vec{B}$).
    \item $\vec{E}$ and $\vec{B}$ oscillate in time in phase quadrature ($90^\circ$ temporal phase shift).
    \item Time-averaged Poynting vector $\langle \vec{S} \rangle = 0$, confirming zero net forward energy flow (standing wave).
\end{itemize}"""
        ),
        (
            r"Summarize the complete set of electrodynamic boundary conditions and discuss why the tangential magnetic field is discontinuous in the presence of an ideal surface current sheet while the normal magnetic field remains strictly continuous under all conditions.",
            r"""\textbf{1. Summary of Boundary Conditions}:
\begin{align}
\text{Normal Electric Displacement:}\quad &D_{2n} - D_{1n} = \rho_s \iff \hat{n}\cdot(\vec{D}_2 - \vec{D}_1) = \rho_s \\
\text{Tangential Electric Field:}\quad &E_{2t} - E_{1t} = 0 \iff \hat{n}\times(\vec{E}_2 - \vec{E}_1) = 0 \\
\text{Normal Magnetic Induction:}\quad &B_{2n} - B_{1n} = 0 \iff \hat{n}\cdot(\vec{B}_2 - \vec{B}_1) = 0 \\
\text{Tangential Magnetic Field:}\quad &\hat{n}\times(\vec{H}_2 - \vec{H}_1) = \vec{K}_s
\end{align}

\textbf{2. Discontinuity of Tangential $\vec{H}$}:
From Ampere's circuital law:
\begin{equation}
\oint_C \vec{H}\cdot d\vec{l} = I_{\text{enclosed}} = \int_0^{\Delta l} \vec{K}_s \cdot (\hat{n}\times d\vec{l})
\end{equation}
An idealized surface current sheet has infinite volume current density $\vec{J} = \vec{K}_s \delta(n)$ concentrated in an infinitesimally thin sheet of zero thickness. When integrating $\vec{H}\cdot d\vec{l}$ across the sheet, the enclosed surface current produces a finite step change:
\begin{equation}
(H_{2t} - H_{1t})\Delta l = K_s \Delta l \implies H_{2t} - H_{1t} = K_s
\end{equation}

\textbf{3. Strict Continuity of Normal $\vec{B}$}:
From Gauss's law for magnetism $\nabla \cdot \vec{B} = 0$, the divergence theorem gives:
\begin{equation}
\oiint_S \vec{B}\cdot d\vec{S} = 0
\end{equation}
For any Gaussian pillbox across the surface, as height $h \to 0$, the side wall flux vanishes. Because there are no magnetic monopoles to produce a surface magnetic charge density ($\rho_{m,s} \equiv 0$), the top and bottom surface fluxes must cancel exactly under all physical circumstances:
\begin{equation}
B_{2n}\Delta S - B_{1n}\Delta S = 0 \implies \mathbf{B_{1n} = B_{2n}}
\end{equation}
Thus, $B_n$ is strictly continuous across every material boundary in the universe."""
        )
    ]
    
    return unit_num, unit_title, mcqs, theory_qs
