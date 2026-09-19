# LPU Engineering Open — Project Master Specification

## 1. Vision & Identity
**LPU Engineering Open** is a serious, open-source educational publishing initiative producing university-grade study guides and textbooks for first-year engineering students.

- **Primary Audience**: First-year undergraduate engineering students (B.Tech / B.E.).
- **Pedagogical Strategy**: Bridge the gap between high-level lecture slides and dense reference textbooks. Provide crystal-clear concept exposition, comprehensive derivations with every algebraic step, exam tips, pitfall warnings, and robust practice sets.
- **Publisher Identity**: Independent open-source educational project. Completely independent of and not endorsed by Lovely Professional University.

---

## 2. Subject Architecture & Roadmap

### Active Subject: Engineering Physics (Semester 1)
- **Book Title**: Engineering Physics
- **Subtitle**: Semester 1 Study & Practice Guide
- **Class**: `book` (A4 paper, 11pt, oneside, openany)
- **Target Length**: ~90–110 pages across 6 cohesive chapters.

#### Chapter Outline:
1. **Chapter 1: Electromagnetic Theory**
   - Coulomb's law, Gauss's law, continuity equation, displacement current.
   - Maxwell's equations in differential and integral forms.
   - Electromagnetic wave propagation in free space and dielectric media.
   - Poynting vector, Poynting theorem, radiation pressure, energy density.
2. **Chapter 2: Lasers and Applications**
   - Principles of absorption, spontaneous emission, stimulated emission.
   - Einstein's coefficients and relations. Population inversion and pumping methods.
   - Optical resonators, metastable states, threshold gain condition.
   - Laser systems: Ruby Laser, He-Ne Laser, Semiconductor Diode Laser.
   - Industrial, medical, optical communication, and holographic applications.
3. **Chapter 3: Fiber Optics**
   - Principle of total internal reflection and light guidance in optical fibers.
   - Acceptance angle, numerical aperture (NA), fractional refractive index change.
   - Classification: Step-Index vs Graded-Index, Single-Mode vs Multi-Mode.
   - Attenuation mechanisms (absorption, scattering, bending) and dispersion.
   - Fiber optic communication systems, splicing, connectors, and fiber sensors.
4. **Chapter 4: Quantum Mechanics**
   - Inadequacy of classical physics, de Broglie hypothesis, matter waves, Davisson-Germer experiment.
   - Phase velocity vs group velocity relations. Heisenberg uncertainty principle.
   - Wave function $\psi$, physical interpretation, Born statistical postulate, normalization.
   - Time-dependent and time-independent Schrödinger wave equations.
   - Particle in a 1D infinite potential well (eigenvalues, normalized eigenfunctions, zero-point energy).
5. **Chapter 5: Semiconductor Physics**
   - Energy band theory in solids (metals, semiconductors, insulators).
   - Intrinsic semiconductors (carrier concentration, Fermi level position).
   - Extrinsic semiconductors ($n$-type and $p$-type, donor/acceptor levels, Fermi level temperature dependence).
   - Carrier transport: Drift velocity, mobility, conductivity, diffusion current, Einstein relation.
   - Hall effect (Hall coefficient, Hall voltage derivation, experimental setup, practical applications).
   - $p$-$n$ junction diode fundamentals (depletion layer, built-in potential, band diagram).
6. **Chapter 6: Engineering Materials**
   - Dielectrics: Polarization mechanisms (electronic, ionic, orientational, space charge), dielectric constant, Clausius-Mossotti equation.
   - Magnetic Materials: Dia-, para-, ferro-, antiferro-, and ferrimagnetism; domain theory, hysteresis loop ($B$-$H$ curve), soft vs hard magnetic materials.
   - Superconductivity: Zero electrical resistance, critical temperature $T_c$, Meissner effect, Type-I and Type-II superconductors, BCS theory basics, applications (SQUIDs, Maglev).
   - Nanomaterials: Quantum confinement, surface-to-volume ratio, synthesis overview (sol-gel, CVD), applications in engineering.

---

## 3. Standard Chapter Blueprint

Every chapter must adhere to a standardized 10-part structural framework:
1. **Chapter Header & Overview**: Introduction to physical context and real-world significance.
2. **Learning Objectives**: 4–6 measurable bulleted outcomes.
3. **Core Theoretical Concepts & Principles**: Explanations with formal `definition` boxes.
4. **Mathematical Formulations & Derivations**: Clean step-by-step algebra with `keyequation` highlights.
5. **Symbols, Units & Physical Significance**: Explicit definitions of every symbol and SI unit.
6. **Worked Numerical Examples**: Solved problems formatted as `Problem`, `Given`, `Formula`, `Step-by-step Calculation`, and `Final Answer with Units`.
7. **Exam Tips & Common Mistakes**: Highlight common exam pitfalls using `examtip` and `commonmistake` boxes.
8. **Summary & Quick Revision**: High-yield key points table and formula cheat sheet.
9. **Practice Exercises**: Graded Conceptual Review, Numerical Problems, and Multiple-Choice Questions (MCQs).
10. **Chapter Test & Solutions**: Comprehensive test set with detailed answer keys.

---

## 4. Quality Control & QA Pipeline

```
[Manuscript Drafting]
        │
        ▼
[LaTeX Compilation] ──► [Zero Errors / Clean Log]
        │
        ▼
[Editorial QA] ───────► [Physics accuracy, correct signs & units]
        │
        ▼
[Pedagogy QA] ────────► [Student-friendly clarity, exam relevance]
        │
        ▼
[Design & Layout QA] ─► [No overfull hbox, balanced pages, clean boxes]
        │
        ▼
[Release & Tagging] ──► [Published PDF artifact]
```
