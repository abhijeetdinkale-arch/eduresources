# Engineering Physics — Semester 1 Study & Practice Guide

**Publisher / Series**: LPU Engineering Open  
**Format**: Modular LaTeX Book (A4 Portrait, 11pt, `style.sty`)  
**Target Output**: `Physics/main.pdf`

---

## 📑 Subject Overview

This study guide covers the foundational Semester 1 Engineering Physics curriculum for first-year engineering students. It bridges theoretical fundamentals and practical engineering applications across 6 modular chapters:

- **Chapter 1**: Electromagnetic Theory
- **Chapter 2**: Lasers and Applications
- **Chapter 3**: Fiber Optics
- **Chapter 4**: Quantum Mechanics
- **Chapter 5**: Semiconductor Physics
- **Chapter 6**: Engineering Materials

---

## 📁 Folder Structure

```text
Physics/
├── main.tex              # Master book compiler
├── style.sty             # Design system, palettes, environments, macros
├── Makefile              # Build automation
├── README.md             # This guide
├── figures/              # Vector figures & graphics
├── tables/               # Standalone tables
├── build/                # Optional build directory
└── chapters/             # Modular chapter files
    ├── chapter-01-electromagnetic-theory.tex
    ├── chapter-02-lasers-and-applications.tex
    ├── chapter-03-fiber-optics.tex
    ├── chapter-04-quantum-mechanics.tex
    ├── chapter-05-semiconductor-physics.tex
    └── chapter-06-engineering-materials.tex
```

---

## 🔨 Compilation Instructions

To compile the full book:

```bash
# Two-pass pdflatex build
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Or using Make:
```bash
make
```

To clean intermediate files:
```bash
make clean
```
