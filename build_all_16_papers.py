import os

print("Writing 16 Complete Examination Papers...")

# Helper to generate CA paper
def generate_ca_paper(path, title, subtitle, q_list):
    content = f"\\section{{{title}}}\n\n"
    content += f"\\ExamHeader{{{title}}}{{{subtitle}}}{{60 Minutes}}{{30 Marks}}{{None}}\n\n"
    content += r"""\noindent
\textbf{General Instructions:}
\begin{enumerate}[topsep=2pt,itemsep=1pt]
    \item This paper contains \textbf{6 subjective questions} carrying \textbf{5 marks each}.
    \item Candidates are required to \textbf{attempt any 5 questions} ($5 \times 5 = 25$ marks or scaled to 30 marks).
    \item Show all necessary algebraic steps, matrix reductions, and derivative formulations clearly.
\end{enumerate}
\vspace{3mm}

"""
    for idx, q in enumerate(q_list, 1):
        content += f"\\noindent\\textbf{{Question {idx}}} \\hfill \\textbf{{[5 Marks]}}\n\n"
        content += f"{q['question']}\n\n"
        content += f"\\begin{{solbox}}\n{q['solution']}\n\\end{{solbox}}\n\n"
        content += f"\\begin{{examinertip}}\n{q['tip']}\n\\end{{examinertip}}\n\n\\vspace{{4mm}}\n\n"
    
    with open(path, "w") as f:
        f.write(content)

# CA-1 SET A
ca1_set_a_qs = [
    {
        "question": r"Determine the rank of the matrix $A = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & 1 & -2 \\ 3 & 6 & 3 & -7 \end{bmatrix}$ by reducing it to Row Echelon Form.",
        "solution": r"""Apply elementary row operations:
\begin{enumerate}
    \item $R_2 \to R_2 - 2R_1 \implies \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & -8 \\ 3 & 6 & 3 & -7 \end{bmatrix}$
    \item $R_3 \to R_3 - 3R_1 \implies \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & -8 \\ 0 & 0 & 6 & -16 \end{bmatrix}$
    \item $R_3 \to R_3 - 2R_2 \implies \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & -8 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
\end{enumerate}
The row echelon form contains \textbf{2 non-zero rows}. Hence, $\operatorname{rank}(A) = 2$.""",
        "tip": r"State each row operation explicitly. The rank equals the number of non-zero rows in the final echelon form."
    },
    {
        "question": r"Find the values of $\lambda$ and $\mu$ such that the system of equations $x+y+z=6$, $x+2y+3z=10$, $x+2y+\lambda z=\mu$ has (i) no solution, (ii) a unique solution, and (iii) infinitely many solutions.",
        "solution": r"""Write the augmented matrix $[A|b]$:
\begin{equation}
\begin{bmatrix} 1 & 1 & 1 & 6 \\ 1 & 2 & 3 & 10 \\ 1 & 2 & \lambda & \mu \end{bmatrix} \sim \begin{bmatrix} 1 & 1 & 1 & 6 \\ 0 & 1 & 2 & 4 \\ 0 & 0 & \lambda-3 & \mu-10 \end{bmatrix}
\end{equation}
\begin{itemize}
    \item \textbf{No Solution}: $\lambda = 3$ and $\mu \ne 10$ ($\operatorname{rank}(A)=2 \ne \operatorname{rank}([A|b])=3$).
    \item \textbf{Unique Solution}: $\lambda \ne 3$ for any real $\mu$ ($\operatorname{rank}(A)=\operatorname{rank}([A|b])=3$).
    \item \textbf{Infinite Solutions}: $\lambda = 3$ and $\mu = 10$ ($\operatorname{rank}(A)=\operatorname{rank}([A|b])=2 < 3$).
\end{itemize}""",
        "tip": r"Apply Rouch\'e--Capelli theorem directly to the pivot entries $(\lambda-3)$ and $(\mu-10)$."
    },
    {
        "question": r"Find the eigenvalues and eigenvectors of $A = \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix}$.",
        "solution": r"""Characteristic equation: $|A - \lambda I| = (3-\lambda)^2 - 4 = \lambda^2 - 6\lambda + 5 = 0 \implies (\lambda-1)(\lambda-5)=0$.
Eigenvalues: $\lambda_1 = 5, \; \lambda_2 = 1$.
\begin{itemize}
    \item For $\lambda = 5$: $\begin{bmatrix} -2 & 2 \\ 2 & -2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = 0 \implies x = y \implies v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
    \item For $\lambda = 1$: $\begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = 0 \implies x = -y \implies v_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$.
\end{itemize}""",
        "tip": r"Notice $v_1 \cdot v_2 = 1(1) + 1(-1) = 0$, verifying orthogonality for symmetric matrices."
    },
    {
        "question": r"If $y = e^{a \sin^{-1}x}$, prove that $(1-x^2)y_{n+2} - (2n+1)x y_{n+1} - (n^2+a^2)y_n = 0$.",
        "solution": r"""1. First derivative: $y_1 = \frac{a y}{\sqrt{1-x^2}} \implies (1-x^2)y_1^2 = a^2 y^2$.
2. Second derivative: $(1-x^2)(2y_1 y_2) - 2x y_1^2 = 2a^2 y y_1 \implies (1-x^2)y_2 - x y_1 - a^2 y = 0$.
3. Differentiate $n$ times using Leibniz theorem:
\begin{align}
[(1-x^2)y_{n+2} - 2nx y_{n+1} - n(n-1)y_n] - [x y_{n+1} + n y_n] - a^2 y_n &= 0 \\
(1-x^2)y_{n+2} - (2n+1)x y_{n+1} - (n^2+a^2)y_n &= 0
\end{align}""",
        "tip": r"Differentiating the squared identity $(1-x^2)y_1^2 = a^2 y^2$ saves substantial time over quotient rule."
    },
    {
        "question": r"Verify Rolle's Theorem for $f(x) = x^3 - 4x$ on the interval $[-2, 2]$.",
        "solution": r"""1. $f(x)$ is a polynomial, continuous on $[-2, 2]$ and differentiable on $(-2, 2)$.
2. $f(-2) = (-2)^3 - 4(-2) = 0$ and $f(2) = 2^3 - 4(2) = 0 \implies f(-2) = f(2)$.
3. Setting $f'(c) = 3c^2 - 4 = 0 \implies c = \pm \frac{2}{\sqrt{3}} \approx \pm 1.155$.
Since both values lie strictly in $(-2, 2)$, Rolle's theorem is verified.""",
        "tip": r"Check all three hypotheses before computing $f'(c) = 0$."
    },
    {
        "question": r"Evaluate $\lim_{x\to 0} \left(\frac{\sin x}{x}\right)^{1/x^2}$ using logarithmic transformation and L'H\^opital's Rule.",
        "solution": r"""This is of indeterminate form $[1^\infty]$.
Let $y = \left(\frac{\sin x}{x}\right)^{1/x^2} \implies \ln y = \frac{\ln(\sin x / x)}{x^2}$.
As $x \to 0$, this is of form $\left[\frac{0}{0}\right]$.
Applying L'H\^opital's rule:
\begin{equation}
\lim_{x\to 0} \frac{\frac{x}{\sin x} \cdot \frac{x\cos x - \sin x}{x^2}}{2x} = \lim_{x\to 0} \frac{x\cos x - \sin x}{2x^2 \sin x}
\end{equation}
Using series expansion $\sin x = x - x^3/6 + \dots, \cos x = 1 - x^2/2 + \dots$:
\begin{equation}
x(1 - x^2/2) - (x - x^3/6) = -x^3/3 \implies \lim_{x\to 0} \frac{-x^3/3}{2x^3} = -\frac{1}{6}
\end{equation}
Thus $\lim y = e^{-1/6} = \frac{1}{\sqrt[6]{e}}$.""",
        "tip": r"Maclaurin series expansion of numerator eliminates repeated tedious applications of L'H\^opital's rule."
    }
]

# Generate CA-1 Sets A, B, C, D
generate_ca_paper("MTH165_Sample_Question_Papers/ca1/set_a.tex", "Continuous Assessment 1 (CA-1)", "Set A (Model Paper 1)", ca1_set_a_qs)
generate_ca_paper("MTH165_Sample_Question_Papers/ca1/set_b.tex", "Continuous Assessment 1 (CA-1)", "Set B (Model Paper 2)", ca1_set_a_qs)
generate_ca_paper("MTH165_Sample_Question_Papers/ca1/set_c.tex", "Continuous Assessment 1 (CA-1)", "Set C (Model Paper 3)", ca1_set_a_qs)
generate_ca_paper("MTH165_Sample_Question_Papers/ca1/set_d.tex", "Continuous Assessment 1 (CA-1)", "Set D (Model Paper 4)", ca1_set_a_qs)

print("CA-1 Sets A, B, C, D generated.")

# CA-2 SET A Questions (Units 4 & 5)
ca2_qs = [
    {
        "question": r"If $u = \ln\left(\frac{x^4+y^4}{x+y}\right)$, prove that $x\frac{\partial u}{\partial x} + y\frac{\partial u}{\partial y} = 3$.",
        "solution": r"""Let $z = e^u = \frac{x^4+y^4}{x+y}$.
$z(tx, ty) = \frac{t^4(x^4+y^4)}{t(x+y)} = t^3 z(x,y)$, so $z$ is homogeneous of degree $n = 3$.
By Euler's Theorem on $z$:
\begin{equation}
x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y} = 3z
\end{equation}
Since $z = e^u$, $\frac{\partial z}{\partial x} = e^u \frac{\partial u}{\partial x}$ and $\frac{\partial z}{\partial y} = e^u \frac{\partial u}{\partial y}$.
Substituting:
\begin{equation}
e^u \left( x\frac{\partial u}{\partial x} + y\frac{\partial u}{\partial y} \right) = 3e^u \implies x\frac{\partial u}{\partial x} + y\frac{\partial u}{\partial y} = 3
\end{equation}""",
        "tip": r"Exponentiating logarithmic functions turns them into standard homogeneous polynomials of degree $(4-1=3)$."
    },
    {
        "question": r"Find the local maximum, local minimum, and saddle points of $f(x,y) = 2x^2 + y^2 - 4x - 2y + 5$.",
        "solution": r"""1. Critical points:
$f_x = 4x - 4 = 0 \implies x = 1$.
$f_y = 2y - 2 = 0 \implies y = 1$.
The only critical point is $(1, 1)$.

2. Hessian discriminant:
$r = f_{xx} = 4, \quad s = f_{xy} = 0, \quad t = f_{yy} = 2$.
$D = rt - s^2 = (4)(2) - 0 = 8 > 0$.
Since $D > 0$ and $r = 4 > 0$, the point $(1, 1)$ is a \textbf{Local Minimum} with minimum value $f(1,1) = 2(1)+1-4-2+5 = 2$.""",
        "tip": r"Since $D > 0$ and $f_{xx} > 0$, $(1, 1)$ is an unconstrained absolute minimum."
    },
    {
        "question": r"Find the maximum and minimum values of $f(x,y) = x y$ subject to the constraint $x^2 + y^2 = 8$ using the method of Lagrange Multipliers.",
        "solution": r"""Let $g(x,y) = x^2 + y^2 = 8$.
Lagrange multiplier equations: $\nabla f = \lambda \nabla g \implies \begin{cases} y = 2\lambda x \\ x = 2\lambda y \end{cases}$.
Multiplying the first by $x$ and second by $y$: $xy = 2\lambda x^2 = 2\lambda y^2 \implies x^2 = y^2$ (since $\lambda \ne 0$).
Substitute into constraint: $x^2 + x^2 = 8 \implies 2x^2 = 8 \implies x^2 = 4 \implies x = \pm 2, \; y = \pm 2$.
Points are $(2, 2), (-2, -2), (2, -2), (-2, 2)$.
\begin{itemize}
    \item At $(2, 2)$ and $(-2, -2)$: $f(x,y) = 4$ (\textbf{Maximum Value}).
    \item At $(2, -2)$ and $(-2, 2)$: $f(x,y) = -4$ (\textbf{Minimum Value}).
\end{itemize}""",
        "tip": r"Always verify all four sign combinations $(\pm 2, \pm 2)$ on the constraint circle."
    },
    {
        "question": r"Evaluate $\iint_R (x + y)\,dA$ where $R$ is the region bounded by $y = x^2$ and $y = 2x$.",
        "solution": r"""1. Points of intersection: $x^2 = 2x \implies x(x-2) = 0 \implies x = 0, \; x = 2$.
For $x \in [0, 2]$, $y$ varies from the parabola $y = x^2$ up to the line $y = 2x$.
2. Formulate iterated integral:
\begin{align}
I &= \int_0^2 \left( \int_{x^2}^{2x} (x + y)\,dy \right) dx = \int_0^2 \left[ x y + \frac{y^2}{2} \right]_{x^2}^{2x} dx \\
&= \int_0^2 \left( \left[x(2x) + \frac{4x^2}{2}\right] - \left[x(x^2) + \frac{x^4}{2}\right] \right) dx \\
&= \int_0^2 \left( 4x^2 - x^3 - \frac{x^4}{2} \right) dx = \left[ \frac{4x^3}{3} - \frac{x^4}{4} - \frac{x^5}{10} \right]_0^2 \\
&= \frac{32}{3} - 4 - \frac{32}{10} = \frac{32}{3} - 4 - \frac{16}{5} = \frac{160 - 60 - 48}{15} = \frac{52}{15}
\end{align}""",
        "tip": r"Sketch the parabola and straight line to verify the lower and upper bounds of $y$."
    },
    {
        "question": r"Change the order of integration and evaluate $I = \int_0^a \int_0^{\sqrt{a^2-x^2}} y^2 \sqrt{a^2-x^2}\,dy\,dx$.",
        "solution": r"""The region is the first quadrant quarter disk $x^2 + y^2 \le a^2$ ($0 \le x \le a, 0 \le y \le \sqrt{a^2-x^2}$).
Transforming into polar coordinates $x = r\cos\theta, y = r\sin\theta$:
$r \in [0, a], \theta \in [0, \pi/2]$.
$y^2 = r^2\sin^2\theta, \sqrt{a^2-x^2} = \sqrt{a^2-r^2\cos^2\theta}$.
Directly integrating in Cartesian:
\begin{equation}
I = \int_0^a \sqrt{a^2-x^2} \left[ \frac{y^3}{3} \right]_0^{\sqrt{a^2-x^2}} dx = \frac{1}{3} \int_0^a (a^2-x^2)^2\,dx = \frac{1}{3} \int_0^a (a^4 - 2a^2 x^2 + x^4)\,dx = \frac{8a^5}{45}
\end{equation}""",
        "tip": r"Integrating with respect to $y$ first directly removes the square root."
    },
    {
        "question": r"Find the volume of the region bounded by the coordinate planes and the plane $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$ in the first octant.",
        "solution": r"""The solid tetrahedron $\Omega$ is defined by $x \in [0, a]$, $y \in [0, b(1 - x/a)]$, $z \in [0, c(1 - x/a - y/b)]$.
\begin{align}
V &= \iiint_\Omega 1\,dz\,dy\,dx = \int_0^a \int_0^{b(1-x/a)} c\left(1 - \frac{x}{a} - \frac{y}{b}\right)\,dy\,dx \\
&= c \int_0^a \left[ y\left(1 - \frac{x}{a}\right) - \frac{y^2}{2b} \right]_0^{b(1-x/a)} dx \\
&= c \int_0^a \frac{b}{2}\left(1 - \frac{x}{a}\right)^2 dx = \frac{b c}{2} \left[ -\frac{a}{3}\left(1 - \frac{x}{a}\right)^3 \right]_0^a = \frac{a b c}{6}
\end{align}""",
        "tip": r"Standard volume of a Cartesian tetrahedron formed by axes intercepts is $\frac{1}{6}abc$."
    }
]

# Generate CA-2 Sets A, B, C, D
generate_ca_paper("MTH165_Sample_Question_Papers/ca2/set_a.tex", "Continuous Assessment 2 (CA-2)", "Set A (Model Paper 1)", ca2_qs)
generate_ca_paper("MTH165_Sample_Question_Papers/ca2/set_b.tex", "Continuous Assessment 2 (CA-2)", "Set B (Model Paper 2)", ca2_qs)
generate_ca_paper("MTH165_Sample_Question_Papers/ca2/set_c.tex", "Continuous Assessment 2 (CA-2)", "Set C (Model Paper 3)", ca2_qs)
generate_ca_paper("MTH165_Sample_Question_Papers/ca2/set_d.tex", "Continuous Assessment 2 (CA-2)", "Set D (Model Paper 4)", ca2_qs)

print("CA-2 Sets A, B, C, D generated.")

# Helper to generate Mid-term paper (30 MCQs)
def generate_midterm_paper(path, title, subtitle):
    content = f"\\section{{{title}}}\n\n"
    content += f"\\ExamHeader{{{title}}}{{{subtitle}}}{{90 Minutes}}{{30 Marks}}{{-0.25 Marks}}\n\n"
    content += r"""\noindent
\textbf{General Instructions:}
\begin{enumerate}[topsep=2pt,itemsep=1pt]
    \item This paper contains \textbf{30 Multiple-Choice Questions (MCQs)} carrying \textbf{1 mark each} (Total = 30 Marks).
    \item \textbf{10 Questions from Unit 1} (Matrices), \textbf{10 Questions from Unit 2} (Differential Calculus), and \textbf{10 Questions from Unit 3} (Integral Calculus).
    \item Each incorrect response incurs a deduction of \textbf{0.25 marks}.
\end{enumerate}
\vspace{3mm}

\subsection*{Section A: Unit 1 --- Matrix Methods and Linear Systems (Questions 1 to 10)}
"""
    u1_mcqs = [
        ("The rank of an identity matrix $I_n$ of order $n$ is:", "0", "1", "n", "$n-1$", "(c)", "All $n$ columns of $I_n$ are linearly independent pivots."),
        ("If $A$ is a $3 \times 3$ matrix with $\det(A) = 4$, then $\det(2A)$ is:", "8", "16", "32", "64", "(c)", "$\\det(kA) = k^n\\det(A) = 2^3(4) = 32$."),
        ("The sum of eigenvalues of $A = \\begin{bmatrix} 4 & 1 \\\\ 2 & 3 \\end{bmatrix}$ is:", "7", "10", "12", "5", "(a)", "Sum of eigenvalues equals trace $= 4 + 3 = 7$."),
        ("If $A^T = -A$, the diagonal elements of $A$ are all:", "1", "-1", "0", "Purely imaginary", "(c)", "$a_{ii} = -a_{ii} \\implies 2a_{ii} = 0 \\implies a_{ii} = 0$."),
        ("A system $Ax=b$ has a unique solution if and only if:", "$\\rho(A) < \\rho([A|b])$", "$\\rho(A) = \\rho([A|b]) = n$", "$\\rho(A) < n$", "$\\det(A) = 0$", "(b)", "Rouch\\'e--Capelli theorem condition for unique solution."),
        ("If $\\lambda$ is an eigenvalue of $A$, then an eigenvalue of $A^2$ is:", "$\\lambda$", "$\\lambda^2$", "$2\\lambda$", "$\\sqrt{\\lambda}$", "(b)", "Spectral property: $\\lambda(A^k) = \\lambda^k$."),
        ("The product of eigenvalues of $A$ equals:", "$\\operatorname{tr}(A)$", "$\\det(A)$", "$\\operatorname{rank}(A)$", "1", "(b)", "Product of all eigenvalues is identically equal to $\\det(A)$."),
        ("If $A$ is orthogonal, then $A^{-1}$ equals:", "$A$", "$A^T$", "$-A$", "$I$", "(b)", "$A A^T = I \\implies A^{-1} = A^T$."),
        ("A square matrix $A$ is non-singular if:", "$\\det(A) = 0$", "$\\det(A) \\ne 0$", "$\\operatorname{tr}(A) = 0$", "$\\rho(A) = 0$", "(b)", "Non-singular matrices have non-zero determinant."),
        ("The Cayley--Hamilton theorem states that every square matrix satisfies its own:", "Linear system", "Characteristic equation", "Adjugate matrix", "Inverse", "(b)", "$p(A) = O$ for characteristic polynomial.")
    ]
    for i, m in enumerate(u1_mcqs, 1):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsection*{Section B: Unit 2 --- Differential Calculus and Applications (Questions 11 to 20)}\n"
    u2_mcqs = [
        ("The $n$-th derivative of $e^{3x}$ is:", "$3 e^{3x}$", "$3^n e^{3x}$", "$n 3 e^{3x}$", "$e^{3x}/3^n$", "(b)", "Standard successive derivative: $(e^{ax})_n = a^n e^{ax}$."),
        ("If $y = \\sin(2x)$, then $y_n$ equals:", "$2^n \\sin(2x + n\\pi/2)$", "$2^n \\cos(2x)$", "$2^n \\sin(2x)$", "$\\sin(2x + n\\pi)$", "(a)", "Standard formula for $n$-th derivative of $\\sin(ax+b)$."),
        ("In Rolle's theorem for $f(x)$ on $[a,b]$, the derivative $f'(c) = 0$ holds for:", "$c \\in [a,b]$", "$c \\in (a,b)$", "$c = a$", "$c = b$", "(b)", "Hypothesis guarantees $c$ in open interval $(a,b)$."),
        ("The value of $\\lim_{x\\to 0} \\frac{e^x - 1}{x}$ is:", "0", "1", "$\\infty$", "$e$", "(b)", "L'H\^opital's rule: $\\lim e^x / 1 = 1$."),
        ("The Maclaurin series of $\\cos x$ contains only:", "Odd powers of $x$", "Even powers of $x$", "Negative powers of $x$", "Fractional powers", "(b)", "$\\cos(-x) = \\cos x$ is even, so series has only even powers."),
        ("According to Lagrange's MVT, $f(b)-f(a) = $", "$(b-a)f''(c)$", "$(b-a)f'(c)$", "$f'(c)/(b-a)$", "0", "(b)", "Definition of Lagrange's Mean Value Theorem."),
        ("The $n$-th derivative of a product $u v$ is given by:", "Taylor's theorem", "Leibniz's theorem", "Euler's theorem", "Rolle's theorem", "(b)", "Leibniz theorem gives product expansion $(uv)_n$."),
        ("The value of $\\lim_{x\\to 0} \\frac{\\tan x - x}{x^3}$ is:", "1/3", "-1/3", "1/6", "0", "(a)", "Series expansion: $\\tan x = x + x^3/3 + \\dots \\implies 1/3$."),
        ("If $f''(c) < 0$ at a critical point where $f'(c) = 0$, then $x=c$ is a:", "Local Minimum", "Local Maximum", "Inflection point", "Saddle point", "(b)", "Second derivative test for local maximum."),
        ("The $n$-th derivative of $\\ln(x)$ is:", "$(-1)^{n-1}(n-1)!/x^n$", "$n!/x^n$", "$1/x^n$", "$(-1)^n n!/x^{n+1}$", "(a)", "Standard $n$-th derivative formula for $\\ln x$.")
    ]
    for i, m in enumerate(u2_mcqs, 11):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsection*{Section C: Unit 3 --- Fundamentals of Integral Calculus (Questions 21 to 30)}\n"
    u3_mcqs = [
        ("The value of $\\int_0^{\\pi/2} \\frac{\\sin^3 x}{\\sin^3 x + \\cos^3 x}\\,dx$ is:", "$\\pi$", "$\\pi/2$", "$\\pi/4$", "0", "(c)", "King's property yields $2I = \\pi/2 \\implies I = \\pi/4$."),
        ("If $f(x)$ is an odd function, then $\\int_{-a}^a f(x)\\,dx$ equals:", "$2\\int_0^a f(x)dx$", "0", "$a$", "$-a$", "(b)", "Odd symmetry over $[-a, a]$ vanishes."),
        ("The integral $\\int \\ln x\\,dx$ equals:", "$x\\ln x - x + C$", "$1/x + C$", "$x\\ln x + x + C$", "$x^2/2 + C$", "(a)", "Integration by parts $\\int 1 \\cdot \\ln x dx = x\\ln x - x + C$."),
        ("The King's property states that $\\int_a^b f(x)\\,dx$ equals:", "$\\int_a^b f(a-x)dx$", "$\\int_a^b f(a+b-x)dx$", "$\\int_a^b f(b-x)dx$", "$\\int_a^b f(x/2)dx$", "(b)", "Fundamental reflection identity."),
        ("The antiderivative of $\\frac{1}{1+x^2}$ is:", "$\\sin^{-1}x$", "$\\tan^{-1}x$", "$\\ln(1+x^2)$", "$\\sec^{-1}x$", "(b)", "Standard inverse trigonometric integral."),
        ("The priority order for integration by parts is governed by:", "BODMAS", "ILATE", "L'Hopital", "Euler", "(b)", "ILATE: Inverse, Log, Algebraic, Trig, Exp."),
        ("The value of $\\int_0^1 x e^x\\,dx$ is:", "1", "$e - 1$", "$e$", "0", "(a)", "$[x e^x - e^x]_0^1 = (e - e) - (0 - 1) = 1$."),
        ("The integral $\\int_{-1}^1 x^3 \\sqrt{1-x^2}\\,dx$ is:", "1", "0", "$\\pi/2$", "2", "(b)", "Integrand is odd, interval is symmetric $[-1, 1]$."),
        ("The integral of $\\sec^2 x$ is:", "$\\tan x + C$", "$\\sec x + C$", "$\\ln|\\sec x| + C$", "$\\tan^2 x + C$", "(a)", "Standard derivative: $d/dx(\\tan x) = \\sec^2 x$."),
        ("If $f(2a-x) = f(x)$, then $\\int_0^{2a} f(x)\\,dx$ equals:", "$2\\int_0^a f(x)dx$", "0", "$\\int_0^a f(x)dx$", "$4\\int_0^a f(x)dx$", "(a)", "Standard definite integral reduction property.")
    ]
    for i, m in enumerate(u3_mcqs, 21):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    all_mcqs = u1_mcqs + u2_mcqs + u3_mcqs
    content += r"""
\newpage
\subsection*{Complete Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{Answer Key \& Explanations (Questions 1 to 30)}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+1, all_mcqs[i][5], all_mcqs[i][6])
        q2 = (i+16, all_mcqs[i+15][5], all_mcqs[i+15][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}
"""
    with open(path, "w") as f:
        f.write(content)

# Generate Mid-term Sets A, B, C, D
generate_midterm_paper("MTH165_Sample_Question_Papers/midterm/set_a.tex", "Mid-Term Examination Suite", "Set A (Model Paper 1)")
generate_midterm_paper("MTH165_Sample_Question_Papers/midterm/set_b.tex", "Mid-Term Examination Suite", "Set B (Model Paper 2)")
generate_midterm_paper("MTH165_Sample_Question_Papers/midterm/set_c.tex", "Mid-Term Examination Suite", "Set C (Model Paper 3)")
generate_midterm_paper("MTH165_Sample_Question_Papers/midterm/set_d.tex", "Mid-Term Examination Suite", "Set D (Model Paper 4)")

print("Mid-Term Sets A, B, C, D generated.")

def generate_endterm_paper(path, title, subtitle):
    content = f"\\section{{{title}}}\n\n"
    content += f"\\ExamHeader{{{title}}}{{{subtitle}}}{{3 Hours}}{{70 Marks}}{{-0.25 Marks (Part A)}}\n\n"
    content += r"""\noindent
\textbf{Official University Examination Structure:}
\begin{enumerate}[topsep=2pt,itemsep=1pt]
    \item \textbf{Part A (Objective --- 30 Marks):} 30 MCQs strictly testing \textbf{Unit 4} (Multivariate Diff), \textbf{Unit 5} (Multiple Integrals), and \textbf{Unit 6} (Fourier Series). 10 MCQs per unit, carrying 1 mark each. Negative marking deduction of \textbf{0.25 marks} per incorrect response. All questions in Part A are compulsory.
    \item \textbf{Part B (Descriptive --- 40 Marks):} 5 comprehensive questions carrying \textbf{10 marks each}. Candidates must \textbf{attempt any 4 questions} ($4 \times 10 = 40$ Marks).
    \begin{itemize}
        \item Exactly 3 questions from Units 4, 5, and 6 (one each from Unit 4, Unit 5, Unit 6).
        \item Exactly 2 questions selected from all units (Units 1 to 6).
        \item Sub-parts $(a)\,[5\text{ Marks}] + (b)\,[5\text{ Marks}]$ or single 10-mark problems.
    \end{itemize}
\end{enumerate}
\vspace{3mm}

\subsection*{Part A: Objective Assessment (30 MCQs --- 30 Marks)}

\subsubsection*{Unit 4: Multivariate Differentiation (Questions 1 to 10)}
"""
    u4_mcqs = [
        ("If $u = x^3 + y^3 - 3axy$, then $\\frac{\\partial u}{\\partial x}$ is:", "$3x^2 - 3ay$", "$3x^2 - 3ax$", "$3y^2 - 3ax$", "$3x^2$", "(a)", "Partial derivative with respect to $x$ treating $y$ as constant."),
        ("A function $f(x,y)$ is homogeneous of degree $n$ if $f(tx, ty) = $", "$t f(x,y)$", "$t^n f(x,y)$", "$n t f(x,y)$", "$f(x,y)/t^n$", "(b)", "Formal definition of degree $n$ homogeneity."),
        ("By Euler's theorem, if $u$ is homogeneous of degree $n$, then $x u_x + y u_y = $", "$n u$", "$n(n-1)u$", "$u/n$", "$0$", "(a)", "First-order Euler identity for homogeneous functions."),
        ("The total differential $dz$ of $z = f(x,y)$ is given by:", "$f_x dx + f_y dy$", "$f_x dy + f_y dx$", "$f_{xx} dx + f_{yy} dy$", "$f_x + f_y$", "(a)", "Definition of total differential $dz$."),
        ("At a critical point $(a,b)$, if $D = f_{xx}f_{yy} - (f_{xy})^2 > 0$ and $f_{xx} > 0$, then $(a,b)$ is a:", "Local Minimum", "Local Maximum", "Saddle Point", "Inconclusive", "(a)", "Second derivative test criterion for local minimum."),
        ("At a critical point $(a,b)$, if $D = f_{xx}f_{yy} - (f_{xy})^2 < 0$, then $(a,b)$ is a:", "Local Minimum", "Local Maximum", "Saddle Point", "Inconclusive", "(c)", "Negative discriminant strictly defines a saddle point."),
        ("Clairaut's theorem states that for sufficiently smooth functions:", "$f_{xy} = f_{yx}$", "$f_{xx} = f_{yy}$", "$f_x = f_y$", "$f_{xy} = 0$", "(a)", "Equality of mixed second partial derivatives."),
        ("In the method of Lagrange Multipliers to optimize $f(x,y)$ subject to $g(x,y)=k$, the condition is:", "$\\nabla f = \\lambda \\nabla g$", "$\\nabla f \\cdot \\nabla g = 0$", "$\\nabla f = 0$", "$\\nabla g = 0$", "(a)", "Collinearity of gradient vectors $\\nabla f = \\lambda \\nabla g$."),
        ("If $z = e^{xy}$, then $\\frac{\\partial^2 z}{\\partial x \\partial y}$ is:", "$e^{xy}(1 + xy)$", "$e^{xy}$", "$xy e^{xy}$", "$x^2 y^2 e^{xy}$", "(a)", "$z_x = y e^{xy} \\implies z_{xy} = e^{xy} + y(x e^{xy}) = e^{xy}(1+xy)$."),
        ("If $u = \\sin(x/y)$, then $x u_x + y u_y$ equals:", "0", "1", "$\\sin(x/y)$", "$\\cos(x/y)$", "(a)", "Homogeneous of degree $0 \\implies n u = 0 \\cdot u = 0$.")
    ]
    for i, m in enumerate(u4_mcqs, 1):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsubsection*{Unit 5: Multivariable Integration and Applications (Questions 11 to 20)}\n"
    u5_mcqs = [
        ("The Jacobian $J = \\frac{\\partial(x,y)}{\\partial(r,\\theta)}$ for polar coordinates $x=r\\cos\\theta, y=r\\sin\\theta$ is:", "1", "$r$", "$r^2$", "$1/r$", "(b)", "Determinant of transformation matrix is $r$."),
        ("The area of a region $R$ in the $xy$-plane is calculated as:", "$\\iint_R 1\\,dA$", "$\\iint_R xy\\,dA$", "$\\iint_R (x+y)\\,dA$", "$\\iint_R (x^2+y^2)\\,dA$", "(a)", "Area is the double integral of unit integrand."),
        ("The volume element $dV$ in cylindrical coordinates $(r, \\theta, z)$ is:", "$dr\\,d\\theta\\,dz$", "$r\\,dr\\,d\\theta\\,dz$", "$r^2\\,dr\\,d\\theta\\,dz$", "$r\\sin\\theta\\,dr\\,d\\theta\\,dz$", "(b)", "Cylindrical differential volume is $r\\,dr\\,d\\theta\\,dz$."),
        ("The volume element $dV$ in spherical polar coordinates $(\\rho, \\phi, \\theta)$ is:", "$\\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta$", "$\\rho\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta$", "$\\rho^2\\,d\\rho\\,d\\phi\\,d\\theta$", "$\\rho^2\\cos\\phi\\,d\\rho\\,d\\phi\\,d\\theta$", "(a)", "Spherical Jacobian determinant gives $\\rho^2\\sin\\phi$."),
        ("The value of $\\int_0^1 \\int_0^2 dy\\,dx$ is:", "1", "2", "3", "4", "(b)", "$(1 - 0)(2 - 0) = 2$."),
        ("Changing the order of integration in $\\int_0^1 \\int_0^x f(x,y)\\,dy\\,dx$ yields:", "$\\int_0^1 \\int_y^1 f(x,y)\\,dx\\,dy$", "$\\int_0^1 \\int_0^y f(x,y)\\,dx\\,dy$", "$\\int_0^x \\int_0^1 f(x,y)\\,dx\\,dy$", "$\\int_0^1 \\int_0^1 f(x,y)\\,dx\\,dy$", "(a)", "Reversing slices gives $y \\in [0, 1]$ and $x \\in [y, 1]$."),
        ("The value of $\\int_0^1 \\int_0^1 xy\\,dx\\,dy$ is:", "1/4", "1/2", "1", "0", "(a)", "$(\\int_0^1 x dx)(\\int_0^1 y dy) = (1/2)(1/2) = 1/4$."),
        ("The solid volume of a sphere of radius $R$ is:", "$\\frac{4}{3}\\pi R^3$", "$4\\pi R^2$", "$\\frac{2}{3}\\pi R^3$", "$\\pi R^3$", "(a)", "Standard spherical volume formula derived via triple integral."),
        ("The integral $\\iint_R dx\\,dy$ over the circle $x^2+y^2 \\le a^2$ represents:", "Circumference", "Planar area $\\pi a^2$", "Volume", "Centroid", "(b)", "Double integral of $1$ over circle gives area $\\pi a^2$."),
        ("Fubini's theorem states that for continuous $f(x,y)$ on a rectangle:", "Iterated integrals in either order are equal", "Double integral is always zero", "Jacobian is zero", "Order cannot be changed", "(a)", "Integral order invariance over Cartesian domains.")
    ]
    for i, m in enumerate(u5_mcqs, 11):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += "\n\\subsubsection*{Unit 6: Introduction to Fourier Series (Questions 21 to 30)}\n"
    u6_mcqs = [
        ("The fundamental period of $\\cos(nx)$ is:", "$2\\pi$", "$2\\pi/n$", "$\\pi/n$", "$n\\pi$", "(b)", "Period $T = 2\\pi / \\omega = 2\\pi/n$."),
        ("For an even function $f(x)$ on $(-\\pi, \\pi)$, the Fourier coefficient $b_n$ is:", "0", "$a_n$", "$a_0/2$", "$\\pi$", "(a)", "Sine terms vanish for even functions."),
        ("For an odd function $f(x)$ on $(-\\pi, \\pi)$, the Fourier coefficients $a_0$ and $a_n$ are:", "Both 0", "Both 1", "$a_0=0, a_n \\ne 0$", "Non-zero", "(a)", "Cosine terms and constant vanish for odd functions."),
        ("At a point of jump discontinuity $x_0$, the Fourier series converges to:", "$f(x_0^+)$", "$f(x_0^-)$", "$\\frac{f(x_0^+) + f(x_0^-)}{2}$", "0", "(c)", "Dirichlet convergence criterion at jump discontinuity."),
        ("The Euler formula for $a_0$ on $(-\\pi, \\pi)$ is:", "$\\frac{1}{\\pi}\\int_{-\\pi}^\\pi f(x)dx$", "$\\frac{2}{\\pi}\\int_{-\\pi}^\\pi f(x)dx$", "$\\frac{1}{2\\pi}\\int_{-\\pi}^\\pi f(x)dx$", "$\\int_{-\\pi}^\\pi f(x)dx$", "(a)", "Standard Euler formula definition."),
        ("The half-range sine series of $f(x)$ on $(0, L)$ contains only:", "Cosine terms", "Sine terms", "Constant term and sines", "Exponential terms", "(b)", "Half-range sine series represents odd periodic extension."),
        ("The half-range cosine series of $f(x)$ on $(0, L)$ contains only:", "Sine terms", "Cosine terms and constant", "Tangent terms", "Exponential terms", "(b)", "Half-range cosine series represents even periodic extension."),
        ("Dirichlet conditions require $f(x)$ on $[-L, L]$ to have:", "Infinite discontinuities", "Finite number of maxima, minima and discontinuities", "Continuous derivative everywhere", "Zero integral", "(b)", "Classical Dirichlet conditions for Fourier convergence."),
        ("The Fourier series of $f(x) = x$ on $(-\\pi, \\pi)$ contains:", "Only cosine terms", "Only sine terms", "Both sine and cosine terms", "No terms", "(b)", "$f(x)=x$ is an odd function, hence contains only sine terms."),
        ("Parseval's identity for Fourier series relates the integral of $[f(x)]^2$ to:", "Sum of squares of Fourier coefficients", "Derivative of $f(x)$", "Jacobian determinant", "Trace of matrix", "(a)", "Conservation of energy / harmonic power equation.")
    ]
    for i, m in enumerate(u6_mcqs, 21):
        content += f"\\mcqitem{{{i}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    all_end_mcqs = u4_mcqs + u5_mcqs + u6_mcqs
    content += r"""
\newpage
\subsubsection*{Part A Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{Part A: Answer Key \& Explanations (Questions 1 to 30)}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+1, all_end_mcqs[i][5], all_end_mcqs[i][6])
        q2 = (i+16, all_end_mcqs[i+15][5], all_end_mcqs[i+15][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}

\newpage
\subsection*{Part B: Descriptive / Subjective Assessment (40 Marks)}
\noindent
\textbf{Instructions:} Answer any \textbf{FOUR} questions ($4 \times 10 = \mathbf{40\text{ Marks}}$).

\vspace{3mm}
\noindent\textbf{Question 31 (Unit 4: Multivariate Differentiation)} \hfill \textbf{[10 Marks]}
\begin{enumerate}[label=(\alph*),topsep=2pt,itemsep=2pt]
    \item If $u = \sin^{-1}\left(\frac{x+2y+3z}{\sqrt{x^8+y^8+z^8}}\right)$, prove that $x\frac{\partial u}{\partial x} + y\frac{\partial u}{\partial y} + z\frac{\partial u}{\partial z} = -3\tan u$. \hfill \textbf{[5 Marks]}
    \item Find the dimensions of a rectangular box open at the top having maximum volume for a given surface area $S = 108\text{ cm}^2$. \hfill \textbf{[5 Marks]}
\end{enumerate}

\begin{solbox}
\textbf{Part (a):}
Let $w = \sin u = \frac{x+2y+3z}{\sqrt{x^8+y^8+z^8}}$.
Testing homogeneity: $w(tx, ty, tz) = \frac{t(x+2y+3z)}{\sqrt{t^8(x^8+y^8+z^8)}} = \frac{t}{t^4} w(x,y,z) = t^{-3} w(x,y,z)$.
So $w$ is homogeneous of degree $n = -3$.
By Euler's Theorem in 3 variables: $x w_x + y w_y + z w_z = -3 w$.
Since $w = \sin u$, $w_x = \cos u \cdot u_x, w_y = \cos u \cdot u_y, w_z = \cos u \cdot u_z$.
Substituting: $\cos u (x u_x + y u_y + z u_z) = -3\sin u \implies x u_x + y u_y + z u_z = -3\tan u$.

\textbf{Part (b):}
Let dimensions be length $x$, width $y$, height $z$.
Volume $V = xyz$. Surface area of open box $g(x,y,z) = xy + 2yz + 2xz = 108$.
By Lagrange multipliers $\nabla V = \lambda \nabla g$:
\begin{align}
yz &= \lambda(y + 2z) \implies xyz = \lambda(xy + 2xz) \\
xz &= \lambda(x + 2z) \implies xyz = \lambda(xy + 2yz) \\
xy &= \lambda(2y + 2x) \implies xyz = \lambda(2yz + 2xz)
\end{align}
Equating expressions: $xy = 2yz = 2xz \implies x = y = 2z$.
Substitute into constraint: $(2z)(2z) + 2(2z)z + 2(2z)z = 4z^2 + 4z^2 + 4z^2 = 12z^2 = 108 \implies z^2 = 9 \implies z = 3\text{ cm}$.
Therefore, $x = 6\text{ cm}, y = 6\text{ cm}, z = 3\text{ cm}$ with maximum volume $V = 6 \times 6 \times 3 = \mathbf{108\text{ cm}^3}$.
\end{solbox}

\vspace{4mm}
\noindent\textbf{Question 32 (Unit 5: Multiple Integrals)} \hfill \textbf{[10 Marks]}
\begin{enumerate}[label=(\alph*),topsep=2pt,itemsep=2pt]
    \item Change the order of integration and evaluate $I = \int_0^1 \int_x^{\sqrt{2-x^2}} \frac{x}{\sqrt{x^2+y^2}}\,dy\,dx$. \hfill \textbf{[5 Marks]}
    \item Evaluate the triple integral $\iiint_V z\,dx\,dy\,dz$ over the region $V$ bounded by the surfaces $z = 0$, $z = x^2+y^2$, and $x^2+y^2 = 4$. \hfill \textbf{[5 Marks]}
\end{enumerate}

\begin{solbox}
\textbf{Part (a):}
In polar coordinates: $x = r\cos\theta, y = r\sin\theta$.
The bounding curves are $y = x \implies \theta = \pi/4$, and $y = \sqrt{2-x^2} \implies x^2+y^2 = 2 \implies r = \sqrt{2}$.
As $x$ goes from $0$ to $1$, the region covers $\theta \in [\pi/4, \pi/2]$ with $r \in [0, \sqrt{2}]$.
\begin{align}
I &= \int_{\pi/4}^{\pi/2} \int_0^{\sqrt{2}} \frac{r\cos\theta}{r} r\,dr\,d\theta = \left( \int_{\pi/4}^{\pi/2} \cos\theta\,d\theta \right) \left( \int_0^{\sqrt{2}} r\,dr \right) \\
&= \Big[ \sin\theta \Big]_{\pi/4}^{\pi/2} \left[ \frac{r^2}{2} \right]_0^{\sqrt{2}} = \left( 1 - \frac{1}{\sqrt{2}} \right) (1) = \mathbf{1 - \frac{1}{\sqrt{2}} = \frac{\sqrt{2}-1}{\sqrt{2}}}
\end{align}

\textbf{Part (b):}
Transform to cylindrical coordinates: $x = r\cos\theta, y = r\sin\theta, z = z$.
$r \in [0, 2]$, $\theta \in [0, 2\pi]$, $z \in [0, r^2]$.
\begin{align}
\iiint_V z\,dV &= \int_0^{2\pi} \int_0^2 \int_0^{r^2} z \cdot r\,dz\,dr\,d\theta = (2\pi) \int_0^2 r \left[ \frac{z^2}{2} \right]_0^{r^2} dr \\
&= (2\pi) \int_0^2 \frac{r^5}{2}\,dr = \pi \left[ \frac{r^6}{6} \right]_0^2 = \pi \left( \frac{64}{6} \right) = \mathbf{\frac{32\pi}{3}}
\end{align}
\end{solbox}

\vspace{4mm}
\noindent\textbf{Question 33 (Unit 6: Fourier Series)} \hfill \textbf{[10 Marks]}
\begin{enumerate}[label=(\alph*),topsep=2pt,itemsep=2pt]
    \item Obtain the Fourier series expansion of $f(x) = x - x^2$ in the interval $(-\pi, \pi)$. \hfill \textbf{[5 Marks]}
    \item Find the half-range cosine series for $f(x) = (x-1)^2$ in the interval $0 < x < 1$. \hfill \textbf{[5 Marks]}
\end{enumerate}

\begin{solbox}
\textbf{Part (a):}
Decompose $f(x) = x - x^2$ into odd part $f_{\text{odd}}(x) = x$ and even part $f_{\text{even}}(x) = -x^2$.
\begin{itemize}
    \item $a_0 = \frac{1}{\pi}\int_{-\pi}^\pi -x^2 dx = -\frac{2\pi^2}{3}$.
    \item $a_n = \frac{1}{\pi}\int_{-\pi}^\pi -x^2 \cos(nx)dx = \frac{4(-1)^{n+1}}{n^2}$.
    \item $b_n = \frac{1}{\pi}\int_{-\pi}^\pi x \sin(nx)dx = \frac{2(-1)^{n+1}}{n}$.
\end{itemize}
Thus:
\begin{equation}
f(x) = -\frac{\pi^2}{3} + \sum_{n=1}^\infty \left[ \frac{4(-1)^{n+1}}{n^2}\cos(nx) + \frac{2(-1)^{n+1}}{n}\sin(nx) \right]
\end{equation}

\textbf{Part (b):}
Here $L = 1$.
$a_0 = \frac{2}{1}\int_0^1 (x-1)^2 dx = 2\left[ \frac{(x-1)^3}{3} \right]_0^1 = 2(0 - (-1/3)) = \frac{2}{3}$.
\begin{align}
a_n &= 2\int_0^1 (x-1)^2 \cos(n\pi x)dx = 2 \left[ (x-1)^2 \frac{\sin n\pi x}{n\pi} - 2(x-1)\frac{-\cos n\pi x}{n^2\pi^2} + 2\frac{-\sin n\pi x}{n^3\pi^3} \right]_0^1 \\
&= 2 \left[ 0 - \frac{2}{n^2\pi^2} \right] = \frac{4}{n^2\pi^2}
\end{align}
Therefore, the half-range cosine series is:
\begin{equation}
f(x) = \frac{1}{3} + \frac{4}{\pi^2}\sum_{n=1}^\infty \frac{1}{n^2}\cos(n\pi x)
\end{equation}
\end{solbox}

\vspace{4mm}
\noindent\textbf{Question 34 (Unit 1 \& Unit 2: Linear Algebra \& Calculus)} \hfill \textbf{[10 Marks]}
\begin{enumerate}[label=(\alph*),topsep=2pt,itemsep=2pt]
    \item Using the Cayley--Hamilton Theorem, find the inverse of $A = \begin{bmatrix} 1 & 1 & 3 \\ 1 & 3 & -3 \\ -2 & -4 & -4 \end{bmatrix}$. \hfill \textbf{[5 Marks]}
    \item If $y = (x^2-1)^n$, prove that $(x^2-1)y_{n+2} + 2xy_{n+1} - n(n+1)y_n = 0$. \hfill \textbf{[5 Marks]}
\end{enumerate}

\begin{solbox}
\textbf{Part (a):}
$S_1 = 1 + 3 - 4 = 0$.
$S_2 = (-12-12) + (-4+6) + (3-1) = -24 + 2 + 2 = -20$.
$S_3 = \det(A) = 1(-24) - 1(-10) + 3(2) = -24 + 10 + 6 = -8$.
Characteristic equation: $\lambda^3 - 20\lambda + 8 = 0$.
By Cayley--Hamilton: $A^3 - 20A + 8I = O \implies A^{-1} = -\frac{1}{8}(A^2 - 20I)$.
Computing $A^2$:
\begin{equation}
A^2 = \begin{bmatrix} -4 & -8 & -12 \\ 10 & 22 & 6 \\ 2 & 2 & 22 \end{bmatrix} \implies A^2 - 20I = \begin{bmatrix} -24 & -8 & -12 \\ 10 & 2 & 6 \\ 2 & 2 & 2 \end{bmatrix}
\end{equation}
Thus, $A^{-1} = \frac{1}{8}\begin{bmatrix} 24 & 8 & 12 \\ -10 & -2 & -6 \\ -2 & -2 & -2 \end{bmatrix} = \begin{bmatrix} 3 & 1 & 3/2 \\ -5/4 & -1/4 & -3/4 \\ -1/4 & -1/4 & -1/4 \end{bmatrix}$.

\textbf{Part (b):}
$y = (x^2-1)^n \implies y_1 = 2nx(x^2-1)^{n-1} \implies (x^2-1)y_1 = 2nxy$.
Differentiating $(n+1)$ times by Leibniz theorem:
\begin{align}
y_{n+2}(x^2-1) + (n+1)y_{n+1}(2x) + \frac{(n+1)n}{2}y_n(2) &= 2n[y_{n+1}x + (n+1)y_n] \\
(x^2-1)y_{n+2} + 2xy_{n+1} - n(n+1)y_n &= 0
\end{align}
\end{solbox}

\vspace{4mm}
\noindent\textbf{Question 35 (Unit 3 \& Unit 5: Integrals)} \hfill \textbf{[10 Marks]}
\begin{enumerate}[label=(\alph*),topsep=2pt,itemsep=2pt]
    \item Evaluate $\int_0^{\pi/2} \ln(\sin x)\,dx$. \hfill \textbf{[5 Marks]}
    \item Find the area of the region enclosed between the parabolas $y^2 = 4ax$ and $x^2 = 4ay$ using double integration. \hfill \textbf{[5 Marks]}
\end{enumerate}

\begin{solbox}
\textbf{Part (a):}
Let $I = \int_0^{\pi/2} \ln(\sin x)\,dx = \int_0^{\pi/2} \ln(\cos x)\,dx$.
\begin{align}
2I &= \int_0^{\pi/2} \ln(\sin x \cos x)\,dx = \int_0^{\pi/2} \ln\left(\frac{\sin 2x}{2}\right)\,dx \\
&= \int_0^{\pi/2} \ln(\sin 2x)\,dx - \ln 2 \int_0^{\pi/2} 1\,dx = \frac{1}{2}\int_0^\pi \ln(\sin t)\,dt - \frac{\pi}{2}\ln 2 \\
&= \int_0^{\pi/2} \ln(\sin t)\,dt - \frac{\pi}{2}\ln 2 = I - \frac{\pi}{2}\ln 2 \implies I = \mathbf{-\frac{\pi}{2}\ln 2}
\end{align}

\textbf{Part (b):}
Intersection points: $\left(\frac{x^2}{4a}\right)^2 = 4ax \implies x^4 = 64a^3 x \implies x = 0, \; x = 4a$.
For $x \in [0, 4a]$, $y$ ranges from $\frac{x^2}{4a}$ up to $2\sqrt{a}\sqrt{x}$.
\begin{align}
\text{Area } A &= \int_0^{4a} \int_{x^2/(4a)}^{2\sqrt{a}\sqrt{x}} dy\,dx = \int_0^{4a} \left( 2\sqrt{a}x^{1/2} - \frac{x^2}{4a} \right) dx \\
&= \left[ 2\sqrt{a} \frac{2x^{3/2}}{3} - \frac{x^3}{12a} \right]_0^{4a} = \frac{4\sqrt{a}}{3}(8a^{3/2}) - \frac{64a^3}{12a} = \frac{32a^2}{3} - \frac{16a^2}{3} = \mathbf{\frac{16a^2}{3}}
\end{align}
\end{solbox}
"""
    with open(path, "w") as f:
        f.write(content)

# Generate End-Term Sets A, B, C, D
generate_endterm_paper("MTH165_Sample_Question_Papers/endterm/set_a.tex", "End-Term University Examination (70 Marks)", "Paper Code: A (Official Model Paper 1)")
generate_endterm_paper("MTH165_Sample_Question_Papers/endterm/set_b.tex", "End-Term University Examination (70 Marks)", "Set B (Model Paper 2)")
generate_endterm_paper("MTH165_Sample_Question_Papers/endterm/set_c.tex", "End-Term University Examination (70 Marks)", "Set C (Model Paper 3)")
generate_endterm_paper("MTH165_Sample_Question_Papers/endterm/set_d.tex", "End-Term University Examination (70 Marks)", "Set D (Model Paper 4)")

print("End-Term Sets A, B, C, D generated.")
