# LPU Engineering Open

**An open-source, academically serious, professional first-year engineering study guide series.**

---

## 📖 About the Project

**LPU Engineering Open** is an independent, community-driven open-source publishing initiative providing comprehensive, exam-oriented, and rigorously structured study and practice guides for first-year engineering students.

Unlike generic notes or automated AI summaries, these books are engineered to the standards of professional university textbooks:
- **Academically Serious & Technically Precise**: Rigorous derivations, SI-unit adherence, and standardized mathematical notation.
- **Beginner-Friendly & Intuitive**: Foundational explanations bridging high-school concepts to university engineering applications.
- **Exam-Oriented**: Includes mid-term and end-term focus points, common student mistakes, worked numerical problems, MCQs, and chapter tests.
- **Modular & Maintainable**: Authored in modular LaTeX with a centralized design system for print and PDF publication.
- **100% Free & Open-Source**: Transparent source code, open to student and educator contributions.

---

## ⚠️ Independent Resource Disclaimer

> **IMPORTANT NOTICE:**  
> **LPU Engineering Open** is an **independent, student-created educational project**.  
> It is **NOT** affiliated with, endorsed by, sponsored by, or produced by **Lovely Professional University (LPU)**.  
> All course structures, syllabus references, and exam patterns are referenced strictly for educational, fair-use study guidance.

---

## 📚 Books in the Series

| Subject | Status | Directory | Primary Output |
| :--- | :---: | :---: | :---: |
| **Engineering Physics** (Semester 1) | **Complete** | [`Physics/`](Physics/) | `Physics/main.pdf` |
| **CSE111: Fundamentals of Computing** | **Complete** | [`CSE111/`](CSE111/) | `CSE111/main.pdf` |
| **MTH165: Engineering Mathematics** | **Complete** | [`MTH165/`](MTH165/) | `MTH165/main.pdf` |
| **INT108: Python Programming** | **Complete** | [`INT108/`](INT108/) | `INT108/main.pdf` |
| **CSE326: Web Development** | **Complete** | [`CSE326/`](CSE326/) | `CSE326/main.pdf` |
| **ECE249: Digital Electronics & Arduino Interfacing** | **Complete** | [`ECE249/`](ECE249/) | `ECE249/main.pdf` |
| **ECE279: Basic Electrical & Electronics Practical** | **Complete** | [`ECE279/`](ECE279/) | `ECE279/main.pdf` |
| **MEC136: Engineering Graphics & AutoCAD** | **Complete** | [`MEC136/`](MEC136/) | `MEC136/main.pdf` |

---

## 🏗️ Repository Architecture

```text
.
├── README.md                 # Project vision, build instructions, and overview
├── LICENSE                   # Open-source and educational content license
├── CONTRIBUTING.md            # Guidelines for issues, corrections, and PRs
├── PROJECT.md                # Engineering roadmap, QA standards, and milestones
├── Makefile                  # Global build automation
│
├── Physics/                  # Engineering Physics Book Source
│   ├── README.md             # Subject-specific documentation
│   ├── main.tex              # Master book document
│   ├── style.sty             # Centralized design system & custom environments
│   ├── Makefile              # Subject build automation
│   ├── chapters/             # Modular chapter files (Chapters 1–6)
│   │   ├── chapter-01-electromagnetic-theory.tex
│   │   ├── chapter-02-lasers-and-applications.tex
│   │   ├── chapter-03-fiber-optics.tex
│   │   ├── chapter-04-quantum-mechanics.tex
│   │   ├── chapter-05-semiconductor-physics.tex
│   │   └── chapter-06-engineering-materials.tex
│   ├── figures/              # Vector diagrams and illustrations
│   └── tables/               # Standalone tables and data sheets
│
└── .agents/
    └── agents/               # Project-level agent QA guidelines & workflows
        ├── latex-build-qa.md
        ├── physics-editorial-qa.md
        ├── exam-pedagogy-qa.md
        ├── book-design-qa.md
        └── release-repo-qa.md
```

---

## ⚙️ How to Build the Books

### Prerequisites
You will need a working LaTeX distribution (such as **MacTeX**, **TeX Live**, or **MiKTeX**) containing `pdflatex` and standard packages (`tcolorbox`, `titlesec`, `fancyhdr`, `geometry`, `amsmath`, `hyperref`).

### Building via Terminal
To build the Engineering Physics book:

```bash
# Navigate to the Physics directory
cd Physics

# Compile using pdflatex (run twice to generate Table of Contents and references)
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Or using `make`:
```bash
make physics
```

The compiled PDF will be generated at `Physics/main.pdf`.

---

## 🤝 How to Contribute

We welcome contributions from students, teaching assistants, and subject experts! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for detailed guidelines on:
- Fixing typos, incorrect signs, or mathematical slips.
- Contributing clear, step-by-step worked examples.
- Providing original vector diagrams (TikZ/SVG).
- Submitting exam practice questions and verified answer keys.

---

## 📄 License

- **Text and Educational Content**: Licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSE).
- **LaTeX Styling & Build Code**: Licensed under the [MIT License](LICENSE).
