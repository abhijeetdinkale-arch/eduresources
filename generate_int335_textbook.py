# -*- coding: utf-8 -*-
import os

os.makedirs("INT335/chapters", exist_ok=True)
os.makedirs("INT335/figures", exist_ok=True)
os.makedirs("INT335/tables", exist_ok=True)

# 1. INT335/style.sty
style_content = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{style}[2026/08/28 v1.0 INT335 Design Thinking Style Package]

% ==============================================================================
% 1. CORE ENCODING, FONTS & MICRO-TYPOGRAPHY
% ==============================================================================
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern}
\RequirePackage{microtype}
\RequirePackage{textcomp}

% ==============================================================================
% 2. PAGE GEOMETRY & LAYOUT
% ==============================================================================
\RequirePackage{geometry}
\geometry{
    a4paper,
    top=25mm,
    bottom=25mm,
    left=25mm,
    right=25mm,
    headheight=15pt,
    headsep=18pt,
    footskip=14mm
}

% ==============================================================================
% 3. MATHEMATICS, SYMBOLS & CODE LISTINGS
% ==============================================================================
\RequirePackage{amsmath,amssymb,amsfonts,mathtools}
\RequirePackage{bm}
\RequirePackage{siunitx}
\sisetup{
    separate-uncertainty = true,
    inter-unit-product = \ensuremath{{}\cdot{}}
}

\RequirePackage{listings}
\lstset{
    basicstyle=\small\ttfamily,
    backgroundcolor=\color{boxgraybg},
    frame=single,
    rulecolor=\color{boxgrayborder},
    keywordstyle=\color{brandblue}\bfseries,
    commentstyle=\color{brandslate}\itshape,
    stringstyle=\color{brandaccent},
    breaklines=true,
    breakatwhitespace=true,
    tabsize=4,
    showstringspaces=false,
    captionpos=b
}

% ==============================================================================
% 4. COLOR PALETTE
% ==============================================================================
\RequirePackage[table,dvipsnames,svgnames]{xcolor}

\definecolor{brandnavy}{RGB}{234, 88, 12}       % LPU Primary Orange #EA580C
\definecolor{brandblue}{RGB}{194, 65, 12}       % Deep Terracotta #C2410C
\definecolor{brandslate}{RGB}{71, 85, 105}      % Muted Slate #475569
\definecolor{branddark}{RGB}{15, 23, 42}        % Text Dark #0F172A
\definecolor{brandaccent}{RGB}{217, 4, 41}      % Vivid Accent Crimson
\definecolor{brandgold}{RGB}{217, 119, 6}       % Amber Gold

\definecolor{boxnavyborder}{RGB}{234, 88, 12}
\definecolor{boxnavybg}{RGB}{255, 247, 237}

\definecolor{boxamberborder}{RGB}{217, 119, 6}
\definecolor{boxamberbg}{RGB}{255, 251, 235}

\definecolor{boxgreenborder}{RGB}{13, 148, 136}
\definecolor{boxgreenbg}{RGB}{240, 253, 250}

\definecolor{boxroseborder}{RGB}{225, 29, 72}
\definecolor{boxrosebg}{RGB}{255, 241, 242}

\definecolor{boxskyborder}{RGB}{2, 132, 199}
\definecolor{boxskybg}{RGB}{240, 249, 255}

\definecolor{boxpurpleborder}{RGB}{126, 34, 206}
\definecolor{boxpurplebg}{RGB}{250, 245, 255}

\definecolor{boxgrayborder}{RGB}{148, 163, 184}
\definecolor{boxgraybg}{RGB}{248, 250, 252}
\definecolor{boxslatebg}{RGB}{241, 245, 249}
\definecolor{boxgoldbg}{RGB}{254, 243, 199}

% ==============================================================================
% 5. BOXES & CALLOUT ENVIRONMENTS (tcolorbox)
% ==============================================================================
\RequirePackage[most]{tcolorbox}
\tcbuselibrary{skins,breakable,hooks}

% Definition Box
\newtcolorbox{definition}[1][]{
    enhanced,
    breakable,
    colback=boxnavybg,
    colframe=boxnavyborder,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Definition}{Definition: #1}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=brandnavy,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Key Equation / Key Principle Box
\newtcolorbox{keyequation}[1][]{
    enhanced,
    breakable,
    colback=boxgoldbg,
    colframe=boxamberborder,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Key Concept / Formula}{#1}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=brandgold,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Worked Example Box
\newtcolorbox{example}[1][]{
    enhanced,
    breakable,
    colback=boxskybg,
    colframe=boxskyborder,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Case Study / Worked Example}{Case Study: #1}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=boxskyborder,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Exam Tip Box
\newtcolorbox{examtip}[1][]{
    enhanced,
    breakable,
    colback=boxgreenbg,
    colframe=boxgreenborder,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Exam Tip \& High-Yield Strategy}{Exam Tip: #1}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=boxgreenborder,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Common Student Mistake Box
\newtcolorbox{commonmistake}[1][]{
    enhanced,
    breakable,
    colback=boxrosebg,
    colframe=boxroseborder,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Common Student Pitfall / Exam Trap}{Common Pitfall: #1}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=boxroseborder,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Alias for examalert
\let\examalert\commonmistake
\let\endexamalert\endcommonmistake

% Quick Revision Box
\newtcolorbox{quickrevision}[1][]{
    enhanced,
    breakable,
    colback=boxslatebg,
    colframe=brandslate,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Quick Revision Summary}{Quick Revision: #1}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=brandslate,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Practice Set Box
\newtcolorbox{practiceset}[1][]{
    enhanced,
    breakable,
    colback=boxnavybg,
    colframe=brandblue,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Practice Exercises}{Practice Exercises: #1}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=brandblue,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Chapter Test Box
\newtcolorbox{chaptertest}[1][]{
    enhanced,
    breakable,
    colback=boxamberbg,
    colframe=brandgold,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Self-Assessment Unit Test (25 Marks)}{Unit Test: #1 (25 Marks)}},
    boxrule=1.2pt,
    leftrule=4.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=brandgold,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% Solution Box
\newtcolorbox{solutionbox}[1][]{
    enhanced,
    breakable,
    colback=boxgraybg,
    colframe=boxgrayborder,
    fonttitle=\bfseries\sffamily,
    title={\ifstrempty{#1}{Complete Step-by-Step Solutions}{#1}},
    boxrule=1.0pt,
    leftrule=3.5pt,
    arc=3pt,
    left=8pt,
    right=8pt,
    top=6pt,
    bottom=6pt,
    coltitle=branddark,
    attach title to upper={\par\vspace{4pt}},
    after title={\par\smallskip\noindent}
}

% ==============================================================================
% 6. GRAPHICS & TIKZ
% ==============================================================================
\RequirePackage{graphicx}
\RequirePackage{tikz}
\usetikzlibrary{shapes,arrows.meta,positioning,calc,decorations.pathmorphing,patterns,backgrounds,fit}

% ==============================================================================
% 7. TABLES, LISTS & ENUMERATIONS
% ==============================================================================
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{enumitem}
\setlist{itemsep=3pt, topsep=4pt, parsep=1pt}

% ==============================================================================
% 8. HEADERS, FOOTERS & SECTION TITLES
% ==============================================================================
\RequirePackage[breakall]{truncate}
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}

\renewcommand{\chaptermark}[1]{\markboth{\thechapter.\ #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}

\fancyhead[L]{\small\sffamily\color{brandslate}\textbf{INT335} \textbar\ Design Thinking}
\fancyhead[R]{\small\sffamily\color{brandnavy}\truncate{0.55\linewidth}{\nouppercase{\leftmark}}}
\fancyfoot[L]{\small\sffamily\color{brandslate}LPU Engineering Open}
\fancyfoot[R]{\small\sffamily\bfseries\color{brandnavy}\thepage}

\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[L]{\small\sffamily\color{brandslate}LPU Engineering Open}
    \fancyfoot[R]{\small\sffamily\bfseries\color{brandnavy}\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

\RequirePackage{titlesec}

% Chapter style: Clean numbered banner with bottom accent rule
\titleformat{\chapter}[display]
  {\normalfont\sffamily\raggedright}
  {\color{brandblue}\large\bfseries\MakeUppercase{\chaptertitlename\ \thechapter}}
  {4pt}
  {\Huge\bfseries\color{brandnavy}}
  [\vspace{4pt}{\color{brandblue}\rule{\linewidth}{1.5pt}}\vspace{10pt}]

\titlespacing*{\chapter}{0pt}{-10pt}{20pt}

\titleformat{\section}
  {\normalfont\Large\bfseries\sffamily\color{brandnavy}}
  {\thesection}{1em}{}
  [\vspace{2pt}{\color{brandslate!40}\rule{\linewidth}{0.5pt}}]

\titlespacing*{\section}{0pt}{14pt}{6pt}

\titleformat{\subsection}
  {\normalfont\large\bfseries\sffamily\color{brandblue}}
  {\thesubsection}{0.8em}{}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}

\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries\sffamily\color{branddark}}
  {\thesubsubsection}{0.6em}{}
\titlespacing*{\subsubsection}{0pt}{8pt}{3pt}

% ==============================================================================
% 9. HYPERLINKS & PDF METADATA
% ==============================================================================
\RequirePackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=brandblue,
    citecolor=boxgreenborder,
    urlcolor=brandblue,
    pdfauthor={LPU Engineering Open Contributors},
    pdftitle={INT335: Design Thinking Comprehensive Study & Practice Guide},
    pdfsubject={Semester 3 B.Tech CSE Course Study & Practice Guide},
    pdfkeywords={INT335, Design Thinking, Innovation, Empathy, Prototyping, Usability, LPU},
    plainpages=false,
    bookmarksnumbered=true,
    pdfpagelayout=OneColumn,
    pdfpagemode=UseOutlines
}

\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}

% ==============================================================================
% 10. FRONTMATTER MACROS: COVER, COPYRIGHT & DISCLAIMER
% ==============================================================================

\newcommand{\makebookcover}{%
\begin{titlepage}
\pagenumbering{Alph}
\pagecolor{boxnavybg}
\begin{flushleft}
    \vspace*{1.2cm}
    {\Huge\bfseries\sffamily\color{brandnavy} INT335: DESIGN THINKING}\\[0.4cm]
    {\LARGE\sffamily\color{brandblue} A Comprehensive Study, Practice \& Innovation Guide}\\[0.8cm]
    \noindent{\color{brandnavy}\rule{\linewidth}{2.5pt}}\\[1.2cm]
    
    {\large\sffamily\textbf{Target Audience:}}\\
    {\normalsize\sffamily B.Tech Computer Science \& Engineering \textbar\ Semester 3}\\
    {\normalsize\sffamily Lovely Professional University}\\[1.5cm]
    
    \begin{tcolorbox}[enhanced, colback=white, colframe=brandnavy, boxrule=1.5pt, arc=4pt, width=0.95\linewidth]
        \sffamily\bfseries\large Key Pedagogical Features:
        \begin{itemize}[leftmargin=1.2em, itemsep=3pt, topsep=4pt]
            \item \textbf{Unit 1 \& 2:} Foundations of Learning, Creativity, Empathy Mapping \& AEIOU Framework.
            \item \textbf{Unit 3 \& 4:} SCAMPER, Brainwriting, Wireframing, Lo-Fi vs. Hi-Fi Prototyping \& MVP Models.
            \item \textbf{Unit 5 \& 6:} Usability Testing, WCAG Accessibility, PDCA Loops, NABC Model \& Elevator Pitches.
            \item \textbf{Comprehensive Question Bank:} Unit tests, step-by-step case studies, and 180 verified exam MCQs.
        \end{itemize}
    \end{tcolorbox}
    
    \vfill
    
    {\sffamily\small\textbf{Editorial Team / Publisher:}\\
    LPU Engineering Open Publishing Project\\
    \url{https://github.com/LPU-Engineering-Open}}
\end{flushleft}
\end{titlepage}
\nopagecolor
\pagenumbering{roman}
}

\newcommand{\copyrightpage}{%
\newpage
\thispagestyle{empty}
\vspace*{\fill}
\noindent
\textbf{\sffamily\large INT335: Design Thinking --- Textbook \& Exam Companion}\\
\textit{\sffamily An Open-Source Educational Publication}\\

\vspace{0.6cm}
\noindent
\textbf{\sffamily Published by:} LPU Engineering Open Initiative\\
\textbf{\sffamily Release Edition:} 2026 Comprehensive Edition\\
\textbf{\sffamily Primary Source Repository:} \url{https://github.com/LPU-Engineering-Open}\\

\vspace{0.6cm}
\noindent
\textbf{\sffamily Licensing:}\\
\textcopyright\ 2026 The Contributors of LPU Engineering Open.\\
This manuscript, diagrams, and educational text are distributed under the terms of the \textbf{Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)} License. To view a copy of this license, visit \url{https://creativecommons.org/licenses/by-nc-sa/4.0/}.\\

\noindent
The accompanying LaTeX macros, shell scripts, and build files are distributed under the terms of the \textbf{MIT License}.\\

\vspace{0.6cm}
\noindent
\textbf{\sffamily Suggested Citation:}\\
LPU Engineering Open Contributors, \textit{INT335: Design Thinking --- Study \& Practice Guide}, 2026 ed. Open Educational Resources.

\vspace*{\fill}
\newpage
}

\newcommand{\disclaimerpage}{%
\newpage
\thispagestyle{empty}
\vspace*{2cm}
\begin{tcolorbox}[
    enhanced,
    colback=boxamberbg,
    colframe=boxamberborder,
    boxrule=1.5pt,
    arc=4pt,
    title={\Large\bfseries\sffamily Important Disclaimer \& Institutional Non-Affiliation}
]
\sffamily\normalsize\setlength{\parskip}{8pt}

\textbf{1. Independent Student-Created Resource}\\
This book is an independent, non-profit, student-led open educational resource designed to aid students in understanding Design Thinking methodologies and preparing for academic examinations.

\textbf{2. Non-Affiliation Notice}\\
\textbf{LPU Engineering Open is NOT affiliated with, sponsored by, authorized by, or endorsed by Lovely Professional University (LPU).} Lovely Professional University is not responsible for the contents, factual accuracy, exam representations, or editorial choices in this book.

\textbf{3. Trademark \& Fair Use}\\
Any references to university curriculum structures, course codes (e.g., INT335), subject syllabi, or exam formats are made strictly under educational \textbf{fair use} principles to provide appropriate context and academic alignment for students studying these topics.

\textbf{4. Accuracy \& Corrections}\\
While every effort has been made by student and educator contributors to verify factual accuracy and pedagogical clarity, the publishers provide this material on an ``as-is'' basis. Readers are encouraged to report any typographical or technical errors on the project's repository.
\end{tcolorbox}
\vfill
\newpage
}

\endinput
"""

with open("INT335/style.sty", "w", encoding="utf-8") as f:
    f.write(style_content)

# 2. INT335/main.tex
main_tex_content = r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{style}

% Global compatibility for Pandoc/Markdown converted elements
\providecommand{\tightlist}{}

\title{INT335: Design Thinking}
\author{LPU Engineering Open}
\date{Semester 3 Study Guide}

\begin{document}

% ==============================================================================
% FRONTMATTER: Cover, Copyright, Disclaimer, and Table of Contents
% ==============================================================================
\frontmatter

\makebookcover
\copyrightpage
\disclaimerpage

\tableofcontents
\newpage

\mainmatter

% ==============================================================================
% CHAPTER INPUTS (UNITS 1 TO 6)
% ==============================================================================
\input{chapters/chapter-01-foundations-of-learning-creativity-and-design-thinking}
\input{chapters/chapter-02-empathy-observation-and-problem-identification}
\input{chapters/chapter-03-ideation-and-creative-problem-solving}
\input{chapters/chapter-04-product-design-and-prototyping}
\input{chapters/chapter-05-testing-validation-and-customer-experience}
\input{chapters/chapter-06-innovation-project-re-design-and-product-presentation}

\end{document}
"""

with open("INT335/main.tex", "w", encoding="utf-8") as f:
    f.write(main_tex_content)

# 3. INT335/Makefile
makefile_content = r"""PDFLATEX ?= pdflatex
LATEXFLAGS ?= -interaction=nonstopmode -halt-on-error

.PHONY: all clean distclean

all: main.pdf

main.pdf: main.tex style.sty chapters/*.tex
	@echo "==> Pass 1: Compiling INT335/main.tex..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Pass 2: Resolving TOC and Cross-References..."
	$(PDFLATEX) $(LATEXFLAGS) main.tex
	@echo "==> Successfully compiled INT335/main.pdf"

clean:
	@echo "==> Cleaning INT335 auxiliary build files..."
	@rm -f *.aux *.log *.out *.toc *.synctex.gz *.bcf *.run.xml *.fls *.fdb_latexmk
	@rm -f chapters/*.aux

distclean: clean
	@echo "==> Removing compiled INT335 PDF..."
	@rm -f main.pdf
"""

with open("INT335/Makefile", "w", encoding="utf-8") as f:
    f.write(makefile_content)

# 4. INT335/README.md
readme_content = r"""# INT335: Design Thinking
## Comprehensive Semester 3 University Study & Practice Guide

**Author**: Independent Student Educational Publishing Initiative  
**License**: CC BY-NC-SA 4.0 (Text & Educational Material) / MIT License (Build Code)  
**Target Class**: Lovely Professional University (LPU) Semester 3 B.Tech CSE / IT Students

---

### Course Modules & Syllabus Architecture
- **Unit 1**: Foundations of Learning, Creativity, and Design Thinking (Wicked Problems, IDEO 3 Lenses, Cognitive Science, Historical Milestones, Global Case Studies)
- **Unit 2**: Empathy, Observation, and Problem Identification (Computational Empathy, AEIOU Framework, Inquiry & Laddering, Personas, Empathy Mapping, POV & HMW)
- **Unit 3**: Ideation and Creative Problem Solving (Divergence vs. Convergence, 4 Creativity Dimensions, Brainstorming, SCAMPER, Mind Mapping, Screening Matrices, Impact-Effort Grid)
- **Unit 4**: Product Design and Prototyping (Rapid Learning, Lo-Fi vs. Hi-Fi, Paper Prototyping, Storyboarding, UI Wireframing Conventions, User Flows, MVP Types)
- **Unit 5**: Testing, Validation, and Customer Experience (Show Don't Tell, Neutral Facilitation, Task Scenarios, Feedback Capture Matrix, Usability vs. CX, WCAG POUR Accessibility)
- **Unit 6**: Innovation Project, Re-Design, and Product Presentation (Iteration Loops, Design Refactoring vs. Re-Design, Strategic Pivots, NABC Framework, Elevator Pitching, Case Study Deliverables)

---

### Compilation Instructions

To build the complete study guide PDF:

```bash
make clean
make
```
"""

with open("INT335/README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

# 5. INT335/CONTENT_BLUEPRINT.md
blueprint_content = r"""# INT335 Content Blueprint & Pedagogical Structure

This document outlines the rigorous pedagogical standards and structure of the INT335 Design Thinking core textbook.

Each chapter is systematically partitioned into:
1. **Unit Overview & Learning Objectives** (tcolorbox)
2. **Foundational Theoretical Principles** (Formal definitions, core tenets, psychological & cognitive science mechanisms)
3. **Methodological Frameworks & Step-by-Step Workflows**
4. **Concrete Real-World Case Studies & Architectural Analysis**
5. **Exam Tips, Traps & Common Student Pitfalls**
6. **Quick Revision Summary & Synthesis Tables**
7. **End-of-Chapter Self-Assessment Unit Test with Step-by-Step Solutions**
"""

with open("INT335/CONTENT_BLUEPRINT.md", "w", encoding="utf-8") as f:
    f.write(blueprint_content)

print("INT335 project structure created successfully!")
