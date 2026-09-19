# Contributing to LPU Engineering Open

Thank you for your interest in contributing to **LPU Engineering Open**!  
We are building high-quality, open-source first-year engineering textbooks and study guides. Every contribution—whether fixing a single formula typo or contributing a full worked derivation—helps thousands of engineering students.

---

## 🎯 Code of Quality & Principles

1. **Originality**: All text, pedagogical commentary, and worked examples must be original. **Never copy-paste copyrighted textbooks or course material.**
2. **Academic Precision**: Ensure standard SI units, correct physical signs, standard notation (vectors in bold or with arrows, tensors, hats for quantum operators), and verified arithmetic.
3. **Beginner-Friendly & Rigorous**: Provide intuitive physical motivation before diving into heavy mathematics. Never skip critical intermediate steps in derivations.
4. **Exam Relevance**: Focus on concepts, derivations, and numerical types frequently tested in university examinations.

---

## 🛠️ Types of Contributions

- **Typo & Error Fixes**: Fix typos, incorrect signs, bad indexing, or misleading explanations.
- **Worked Examples**: Add step-by-step solved numerical and conceptual problems.
- **Visuals & Diagrams**: Contribute clean vector diagrams using TikZ or standalone SVG/PDF graphics.
- **Practice Sets & MCQs**: Submit conceptual questions, numerical sets, and chapter tests with complete verified solutions.
- **LaTeX & Typography Refinements**: Optimize style definitions, spacing, table formatting, and cross-referencing.

---

## 📐 LaTeX Style & Authoring Rules

- **Use Centralized Environments**: Never hand-craft custom box tables or hardcode colors inside chapter files. Use the standard environments from `style.sty`:
  - `\begin{definition}[Title] ... \end{definition}`
  - `\begin{important}[Title] ... \end{important}`
  - `\begin{keyequation}[Title] ... \end{keyequation}`
  - `\begin{example}[Problem Title] ... \end{example}`
  - `\begin{examtip}[Title] ... \end{examtip}`
  - `\begin{commonmistake}[Title] ... \end{commonmistake}`
  - `\begin{practiceset}[Title] ... \end{practiceset}`
  - `\begin{quickrevision}[Title] ... \end{quickrevision}`
  - `\begin{chaptertest}[Title] ... \end{chaptertest}`
- **Standard Math Notation**:
  - Use `\mathbf{E}`, `\mathbf{B}`, `\mathbf{D}`, `\mathbf{H}` for electromagnetic vector fields.
  - Use `\nabla \cdot \mathbf{D} = \rho_v` and `\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}` for Maxwell's equations.
  - Use `\hat{H}\psi = E\psi` for quantum operators.
- **Tables**: Use `booktabs` rules (`\toprule`, `\midrule`, `\bottomrule`) with centered/aligned column specifiers.
- **Pandoc / Markdown Compatibility**: Do not manually delete `\tightlist` if converted; `style.sty` defines `\providecommand{\tightlist}{}` centrally.

---

## 🚀 How to Submit Changes

1. **Fork the repository** and create a feature branch (`git checkout -b feature/ch02-laser-efficiency`).
2. **Make your changes** in the relevant chapter file under `Physics/chapters/`.
3. **Compile and verify locally**:
   ```bash
   cd Physics
   pdflatex -interaction=nonstopmode -halt-on-error main.tex
   pdflatex -interaction=nonstopmode -halt-on-error main.tex
   ```
4. **Inspect the PDF output** to confirm that:
   - There are no compilation errors or fatal warnings.
   - All references and labels resolve properly (`??` does not appear).
   - No text or math overflows page margins.
5. **Commit cleanly** with descriptive messages (e.g., `fix(physics/ch01): correct sign in Poynting theorem derivation`).
6. **Open a Pull Request** describing the changes, motivation, and verification steps.
