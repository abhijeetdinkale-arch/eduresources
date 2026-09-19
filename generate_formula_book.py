import os

print("Generating MTH165 Formula & Rapid Revision Book...")

# 1. formula_style.sty
with open("MTH165_Formula_Book/formula_style.sty", "w") as f:
    f.write(r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{formula_style}[2026/09/16 v1.0 MTH165 Formula Book Style]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=18mm,top=22mm,bottom=22mm,headheight=20pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts,mathtools,physics,bm}
\RequirePackage{xcolor}
\RequirePackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\RequirePackage{enumitem}
\RequirePackage{fancyhdr}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{titlesec}
\RequirePackage{booktabs}
\RequirePackage{microtype}
\RequirePackage[hidelinks,colorlinks=true,linkcolor=LPUNavy,urlcolor=LPUOrange,citecolor=LPUNavy]{hyperref}

% Palette
\definecolor{LPUNavy}{RGB}{15, 32, 67}
\definecolor{LPUOrange}{RGB}{232, 90, 16}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{FormulaBg}{RGB}{245, 248, 255}
\definecolor{FormulaBorder}{RGB}{15, 44, 89}
\definecolor{TipBg}{RGB}{255, 250, 235}
\definecolor{TipBorder}{RGB}{232, 90, 16}

% Header/Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{LPUNavy}\textbf{MTH165: Mathematics for Engineers --- Formula Handbook}}
\fancyhead[R]{\small\color{LPUOrange}\textbf{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

% Section styling
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{LPUNavy}}{\chaptertitlename\ \thechapter}{12pt}{\Huge}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{LPUNavy}}{\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{LPUOrange}}{\thesubsection}{1em}{}

% Boxes
\newtcolorbox{formulabox}[2][]{
    enhanced,
    breakable,
    colback=FormulaBg,
    colframe=FormulaBorder,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    title={#2},
    boxrule=1pt,
    arc=2mm,
    top=2.5mm, bottom=2.5mm, left=3mm, right=3mm,
    #1
}

\newtcolorbox{memorytip}[1][]{
    enhanced,
    breakable,
    colback=TipBg,
    colframe=TipBorder,
    fonttitle=\bfseries\color{TipBorder},
    title={\textbf{High-Yield Memory Shortcut / Exam Trap:}},
    boxrule=0.8pt,
    arc=2mm,
    top=2mm, bottom=2mm, left=3mm, right=3mm,
    #1
}
""")

# 2. main.tex
with open("MTH165_Formula_Book/main.tex", "w") as f:
    f.write(r"""\documentclass[a4paper,11pt,oneside,openany]{book}
\usepackage{formula_style}

\title{MTH165: Mathematics for Engineers --- Master Formula \& Rapid Revision Book}
\author{LPU Engineering Open Series}
\date{Academic Year 2024--2025 / 2025--2026}

\begin{document}

\frontmatter
\input{frontmatter/cover}

\tableofcontents
\newpage

\mainmatter

\input{chapters/unit1_matrix_formulas}
\input{chapters/unit2_diff_formulas}
\input{chapters/unit3_integral_formulas}
\input{chapters/unit4_multivariate_formulas}
\input{chapters/unit5_multivariable_integral_formulas}
\input{chapters/unit6_fourier_formulas}
\input{chapters/high_yield_cheatsheet}

\end{document}
""")

# 3. frontmatter/cover.tex
with open("MTH165_Formula_Book/frontmatter/cover.tex", "w") as f:
    f.write(r"""\begin{titlepage}
\centering
\vspace*{1.5cm}
{\Huge \textbf{\color{LPUNavy}MTH165: Mathematics for Engineers}}\\[0.5cm]
{\LARGE \textbf{\color{LPUOrange}Master Formula \& Rapid Revision Book}}\\[0.3cm]
{\large \textit{Complete Theorem Checklists, Standard Derivative/Integral Tables \& High-Yield Memorization Sheets}}\\[2cm]

\rule{\linewidth}{1.5pt}\\[0.5cm]
{\large \textbf{B.Tech / B.E. Semester 1 Curriculum | Lovely Professional University}}\\[0.5cm]
\rule{\linewidth}{1.5pt}\\[2.5cm]

\vfill
{\large \textbf{LPU Engineering Open Publishing Initiative}}\\[0.2cm]
{\small Independent Open-Source Academic Guide Series}
\end{titlepage}
\newpage
""")

# 4. Chapters 1 to 6 and cheatsheet
with open("MTH165_Formula_Book/chapters/unit1_matrix_formulas.tex", "w") as f:
    f.write(r"""\chapter{Unit 1: Matrix Methods and Linear Systems}

\begin{formulabox}{Matrix Rank \& Determinantal Minor Laws}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Rank Definition}: $\operatorname{rank}(A) = \rho(A) = $ Number of non-zero rows in Row Echelon Form (REF).
    \item If $A$ is $m \times n$, then $\rho(A) \le \min(m, n)$.
    \item $\rho(AB) \le \min(\rho(A), \rho(B))$.
    \item $\rho(A + B) \le \rho(A) + \rho(B)$.
    \item $\rho(A^T) = \rho(A) = \rho(A^T A) = \rho(A A^T)$.
\end{itemize}
\end{formulabox}

\begin{formulabox}{Linear Systems Solvability ($Ax=b$)}
Let $\tilde{A} = [A | b]$ be the augmented matrix for an $m \times n$ system:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Inconsistent (No Solution)}: $\rho(A) < \rho([A|b])$.
    \item \textbf{Consistent (Unique Solution)}: $\rho(A) = \rho([A|b]) = n$ (number of unknowns).
    \item \textbf{Consistent (Infinite Solutions)}: $\rho(A) = \rho([A|b]) = r < n$, with $(n - r)$ free independent parameters.
\end{enumerate}
For homogeneous systems $Ax = 0$:
\begin{itemize}
    \item Non-trivial solutions exist $\iff \rho(A) < n \iff \det(A) = 0$ (for square matrix).
\end{itemize}
\end{formulabox}

\begin{formulabox}{Eigenvalues \& Cayley--Hamilton Formulae}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Characteristic Equation} ($3 \times 3$):
    \begin{equation}
    \lambda^3 - S_1 \lambda^2 + S_2 \lambda - S_3 = 0
    \end{equation}
    where $S_1 = \operatorname{tr}(A)$, $S_2 = M_{11}+M_{22}+M_{33}$, and $S_3 = \det(A)$.
    \item \textbf{Sum of Eigenvalues}: $\sum \lambda_i = \operatorname{tr}(A) = a_{11}+a_{22}+a_{33}$.
    \item \textbf{Product of Eigenvalues}: $\prod \lambda_i = \det(A)$.
    \item \textbf{Cayley--Hamilton Theorem}: Every square matrix satisfies its characteristic polynomial:
    \begin{equation}
    A^3 - S_1 A^2 + S_2 A - S_3 I = O
    \end{equation}
    \item \textbf{Matrix Inverse}: $A^{-1} = \frac{1}{S_3}(A^2 - S_1 A + S_2 I)$.
\end{itemize}
\end{formulabox}
""")

with open("MTH165_Formula_Book/chapters/unit2_diff_formulas.tex", "w") as f:
    f.write(r"""\chapter{Unit 2: Differential Calculus and Applications}

\begin{formulabox}{Standard $n$-th Derivatives}
\begin{itemize}[leftmargin=1.5em]
    \item $\frac{d^n}{dx^n}[e^{ax}] = a^n e^{ax}$
    \item $\frac{d^n}{dx^n}[(ax+b)^m] = \frac{m!}{(m-n)!} a^n (ax+b)^{m-n}$
    \item $\frac{d^n}{dx^n}\left[\frac{1}{ax+b}\right] = \frac{(-1)^n n! a^n}{(ax+b)^{n+1}}$
    \item $\frac{d^n}{dx^n}[\ln(ax+b)] = \frac{(-1)^{n-1} (n-1)! a^n}{(ax+b)^n}$
    \item $\frac{d^n}{dx^n}[\sin(ax+b)] = a^n \sin\left(ax+b + \frac{n\pi}{2}\right)$
    \item $\frac{d^n}{dx^n}[\cos(ax+b)] = a^n \cos\left(ax+b + \frac{n\pi}{2}\right)$
    \item $\frac{d^n}{dx^n}[e^{ax}\sin(bx+c)] = (a^2+b^2)^{n/2} e^{ax}\sin\left(bx+c + n\tan^{-1}\frac{b}{a}\right)$
\end{itemize}
\end{formulabox}

\begin{formulabox}{Leibniz's Product Rule}
\begin{equation}
(uv)_n = \sum_{k=0}^n \binom{n}{k} u_{n-k} v_k = u_n v + \binom{n}{1} u_{n-1} v_1 + \binom{n}{2} u_{n-2} v_2 + \cdots + u v_n
\end{equation}
\end{formulabox}

\begin{formulabox}{Mean Value Theorems \& Series Expansions}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Rolle's}: $f(a)=f(b) \implies f'(c) = 0$ for some $c \in (a,b)$.
    \item \textbf{LMVT}: $f'(c) = \frac{f(b)-f(a)}{b-a}$ for some $c \in (a,b)$.
    \item \textbf{CMVT}: $\frac{f'(c)}{g'(c)} = \frac{f(b)-f(a)}{g(b)-g(a)}$ for some $c \in (a,b)$.
    \item \textbf{Taylor's Series}: $f(a+h) = \sum_{k=0}^n \frac{h^k}{k!} f^{(k)}(a) + \frac{h^{n+1}}{(n+1)!} f^{(n+1)}(a+\theta h)$.
\end{itemize}
\end{formulabox}
""")

with open("MTH165_Formula_Book/chapters/unit3_integral_formulas.tex", "w") as f:
    f.write(r"""\chapter{Unit 3: Fundamentals of Integral Calculus}

\begin{formulabox}{Master Properties of Definite Integrals}
\begin{itemize}[leftmargin=1.5em]
    \item $\int_a^b f(x)\,dx = \int_a^b f(a+b-x)\,dx$ (\textbf{King's Property})
    \item $\int_0^a f(x)\,dx = \int_0^a f(a-x)\,dx$
    \item $\int_{-a}^a f(x)\,dx = \begin{cases} 2\int_0^a f(x)\,dx, & f(-x) = f(x) \text{ (Even)} \\ 0, & f(-x) = -f(x) \text{ (Odd)} \end{cases}$
    \item $\int_0^{2a} f(x)\,dx = \begin{cases} 2\int_0^a f(x)\,dx, & f(2a-x) = f(x) \\ 0, & f(2a-x) = -f(x) \end{cases}$
\end{itemize}
\end{formulabox}
""")

with open("MTH165_Formula_Book/chapters/unit4_multivariate_formulas.tex", "w") as f:
    f.write(r"""\chapter{Unit 4: Multivariate Differentiation}

\begin{formulabox}{Euler's Theorem on Homogeneous Functions}
If $u(x,y)$ is homogeneous of degree $n$:
\begin{align}
x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} &= n u \\
x^2 \frac{\partial^2 u}{\partial x^2} + 2xy \frac{\partial^2 u}{\partial x \partial y} + y^2 \frac{\partial^2 u}{\partial y^2} &= n(n-1)u
\end{align}
\end{formulabox}

\begin{formulabox}{2D Extrema \& Lagrange Multipliers}
\begin{itemize}[leftmargin=1.5em]
    \item Critical points: $f_x = 0, \; f_y = 0$.
    \item Discriminant $D = r t - s^2 = f_{xx} f_{yy} - (f_{xy})^2$:
    \begin{itemize}
        \item $D > 0, r > 0 \implies$ \textbf{Local Minimum}
        \item $D > 0, r < 0 \implies$ \textbf{Local Maximum}
        \item $D < 0 \implies$ \textbf{Saddle Point}
        \item $D = 0 \implies$ \textbf{Inconclusive}
    \end{itemize}
    \item \textbf{Lagrange Multipliers}: $\nabla f = \lambda \nabla g$.
\end{itemize}
\end{formulabox}
""")

with open("MTH165_Formula_Book/chapters/unit5_multivariable_integral_formulas.tex", "w") as f:
    f.write(r"""\chapter{Unit 5: Multivariable Integration and Applications}

\begin{formulabox}{Coordinate Transformations \& Jacobians}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Polar}: $x = r\cos\theta, y = r\sin\theta \implies dA = r\,dr\,d\theta$.
    \item \textbf{Cylindrical}: $x = r\cos\theta, y = r\sin\theta, z = z \implies dV = r\,dr\,d\theta\,dz$.
    \item \textbf{Spherical}: $x = \rho\sin\phi\cos\theta, y = \rho\sin\phi\sin\theta, z = \rho\cos\phi \implies dV = \rho^2 \sin\phi\,d\rho\,d\phi\,d\theta$.
    \item \textbf{Planar Area}: $A = \iint_R 1\,dA$.
    \item \textbf{Solid Volume}: $V = \iiint_\Omega 1\,dV$.
\end{itemize}
\end{formulabox}
""")

with open("MTH165_Formula_Book/chapters/unit6_fourier_formulas.tex", "w") as f:
    f.write(r"""\chapter{Unit 6: Introduction to Fourier Series}

\begin{formulabox}{Euler Formulae on $(-L, L)$}
\begin{equation}
f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[ a_n \cos\left(\frac{n\pi x}{L}\right) + b_n \sin\left(\frac{n\pi x}{L}\right) \right]
\end{equation}
\begin{align}
a_0 &= \frac{1}{L} \int_{-L}^L f(x)\,dx \\
a_n &= \frac{1}{L} \int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\,dx \\
b_n &= \frac{1}{L} \int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx
\end{align}
\end{formulabox}

\begin{formulabox}{Symmetry \& Half-Range Formulae}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Even Function}: $b_n = 0$, $a_0 = \frac{2}{L}\int_0^L f(x)dx$, $a_n = \frac{2}{L}\int_0^L f(x)\cos(\frac{n\pi x}{L})dx$.
    \item \textbf{Odd Function}: $a_0 = a_n = 0$, $b_n = \frac{2}{L}\int_0^L f(x)\sin(\frac{n\pi x}{L})dx$.
    \item \textbf{Parseval's Identity}: $\frac{1}{L} \int_{-L}^L [f(x)]^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^\infty (a_n^2 + b_n^2)$.
\end{itemize}
\end{formulabox}
""")

with open("MTH165_Formula_Book/chapters/high_yield_cheatsheet.tex", "w") as f:
    f.write(r"""\chapter{High-Yield Examination Cheatsheet}

\section{Master Quick Reference Table}

\begin{table}[htbp]
\centering
\caption{\textbf{MTH165 Complete High-Yield Summary}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l p{4cm} X}
\toprule
\textbf{Unit} & \textbf{Core Topic} & \textbf{Essential Formula / Criterion} \\
\midrule
\textbf{Unit 1} & Matrix Rank \& Echelon & $\rho(A) = \text{\# pivots in REF}; \quad \rho(A) = \rho([A|b]) \implies \text{Consistent}$ \\
& Eigenvalues \& Cayley--Ham & $\lambda^3 - S_1\lambda^2 + S_2\lambda - S_3 = 0; \quad A^3 - S_1 A^2 + S_2 A - S_3 I = O$ \\
\addlinespace
\textbf{Unit 2} & Leibniz Product Rule & $(uv)_n = \sum_{k=0}^n \binom{n}{k} u_{n-k} v_k$ \\
& Mean Value Theorems & Rolle: $f'(c)=0$; LMVT: $f'(c) = \frac{f(b)-f(a)}{b-a}$; CMVT: $\frac{f'(c)}{g'(c)} = \frac{\Delta f}{\Delta g}$ \\
\addlinespace
\textbf{Unit 3} & King's Definite Property & $\int_a^b f(x)dx = \int_a^b f(a+b-x)dx$ \\
& Symmetry Properties & Even: $2\int_0^a f(x)dx$; Odd: $0$ \\
\addlinespace
\textbf{Unit 4} & Euler's Homogeneous Thm & $x u_x + y u_y = n u; \quad x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = n(n-1)u$ \\
& 2D Extrema Discriminant & $D = f_{xx}f_{yy} - (f_{xy})^2 > 0, f_{xx} > 0 \implies \text{Min}; D < 0 \implies \text{Saddle}$ \\
\addlinespace
\textbf{Unit 5} & Jacobians \& Coordinates & Polar: $r dr d\theta$; Cyl: $r dr d\theta dz$; Spherical: $\rho^2 \sin\phi d\rho d\phi d\theta$ \\
& Area \& Volume & $A = \iint_R 1 dA; \quad V = \iiint_\Omega 1 dV$ \\
\addlinespace
\textbf{Unit 6} & Fourier Trigonometric & $a_0 = \frac{1}{L}\int_{-L}^L f dx; \; a_n = \frac{1}{L}\int_{-L}^L f \cos\frac{n\pi x}{L} dx; \; b_n = \frac{1}{L}\int_{-L}^L f \sin\frac{n\pi x}{L} dx$ \\
& Jump Discontinuity & $S(x_0) = \frac{f(x_0^+) + f(x_0^-)}{2}$ \\
\bottomrule
\end{tabularx}
\end{table}
""")

# 5. Makefile
with open("MTH165_Formula_Book/Makefile", "w") as f:
    f.write(r"""all:
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
""")

print("Formula Book generated successfully.")
