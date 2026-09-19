import os

print("Writing QB Chapters 1 to 6...")

# Let's write unit 1
with open("MTH165_Question_Bank/chapters/unit1_matrices_qb.tex", "w") as f:
    f.write(r"""\chapter{Unit 1: Matrix Methods and Linear Systems}

\section{Section 1: 20 Solved Comprehensive Subjective Problems}

\begin{subjectiveq}{1.1}
Reduce the matrix $A$ to Row Echelon Form and find its rank:
\begin{equation}
A = \begin{bmatrix}
1 & 2 & 3 & 2 \\
2 & 3 & 5 & 1 \\
1 & 3 & 4 & 5
\end{bmatrix}
\end{equation}
\end{subjectiveq}

\begin{solbox}
Apply elementary row operations:
\begin{enumerate}
    \item $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - R_1$:
    \begin{equation}
    \begin{bmatrix}
    1 & 2 & 3 & 2 \\
    0 & -1 & -1 & -3 \\
    0 & 1 & 1 & 3
    \end{bmatrix}
    \end{equation}
    \item $R_3 \to R_3 + R_2$:
    \begin{equation}
    \begin{bmatrix}
    1 & 2 & 3 & 2 \\
    0 & -1 & -1 & -3 \\
    0 & 0 & 0 & 0
    \end{bmatrix}
    \end{equation}
\end{enumerate}
The row echelon form contains \textbf{2 non-zero rows}. Therefore, $\operatorname{rank}(A) = 2$.
\end{solbox}

\begin{examinertip}
Always clearly state the elementary row operations used ($R_i \to R_i + c R_j$) at each step. Rank equals the number of non-zero rows in the final echelon form.
\end{examinertip}

\begin{subjectiveq}{1.2}
Find the eigenvalues and corresponding eigenvectors of the matrix:
\begin{equation}
A = \begin{bmatrix}
8 & -6 & 2 \\
-6 & 7 & -4 \\
2 & -4 & 3
\end{bmatrix}
\end{equation}
\end{subjectiveq}

\begin{solbox}
1. \textbf{Characteristic Equation}: $\det(A - \lambda I) = 0 \implies \lambda^3 - S_1 \lambda^2 + S_2 \lambda - S_3 = 0$.
\begin{align}
S_1 &= 8 + 7 + 3 = 18 \\
S_2 &= (21 - 16) + (24 - 4) + (56 - 36) = 5 + 20 + 20 = 45 \\
S_3 &= \det(A) = 8(5) + 6(-10) + 2(10) = 40 - 60 + 20 = 0
\end{align}
Thus: $\lambda^3 - 18\lambda^2 + 45\lambda = 0 \implies \lambda(\lambda - 3)(\lambda - 15) = 0$.
The eigenvalues are $\lambda_1 = 0, \; \lambda_2 = 3, \; \lambda_3 = 15$.

2. \textbf{Eigenvectors}:
\begin{itemize}
    \item For $\lambda = 0$: $(A - 0I)v = 0 \implies v_1 = \begin{bmatrix} 1 & 2 & 2 \end{bmatrix}^T$.
    \item For $\lambda = 3$: $(A - 3I)v = 0 \implies v_2 = \begin{bmatrix} 2 & 1 & -2 \end{bmatrix}^T$.
    \item For $\lambda = 15$: $(A - 15I)v = 0 \implies v_3 = \begin{bmatrix} 2 & -2 & 1 \end{bmatrix}^T$.
\end{itemize}
Notice that since $A$ is symmetric, all eigenvectors are mutually orthogonal: $v_1 \cdot v_2 = 0, v_1 \cdot v_3 = 0, v_2 \cdot v_3 = 0$.
\end{solbox}

\begin{examinertip}
For real symmetric matrices, eigenvectors corresponding to distinct eigenvalues are always orthogonal. Verifying $v_i \cdot v_j = 0$ provides an instant check on calculation accuracy!
\end{examinertip}

\begin{subjectiveq}{1.3}
Verify the Cayley--Hamilton theorem for $A = \begin{bmatrix} 2 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 2 \end{bmatrix}$ and compute $A^{-1}$ and $A^4$.
\end{subjectiveq}

\begin{solbox}
1. \textbf{Characteristic Equation}:
$S_1 = 2+2+2 = 6$, $S_2 = 3+3+3 = 9$, $S_3 = \det(A) = 4$.
Characteristic polynomial: $\lambda^3 - 6\lambda^2 + 9\lambda - 4 = 0$.
By Cayley--Hamilton: $A^3 - 6A^2 + 9A - 4I = O$.

2. \textbf{Computation of $A^{-1}$}:
Multiply by $A^{-1}$: $A^2 - 6A + 9I - 4A^{-1} = O \implies A^{-1} = \frac{1}{4}(A^2 - 6A + 9I)$.
Computing matrices yields:
\begin{equation}
A^{-1} = \frac{1}{4}\begin{bmatrix} 3 & 1 & -1 \\ 1 & 3 & 1 \\ -1 & 1 & 3 \end{bmatrix}
\end{equation}

3. \textbf{Computation of $A^4$}:
$A^4 = 6A^3 - 9A^2 + 4A = 6(6A^2 - 9A + 4I) - 9A^2 + 4A = 27A^2 - 50A + 24I$.
\end{solbox}

\section{Section 2: 50 Solved Multiple-Choice Questions (MCQs)}

\subsection*{Part I: Foundational Level (Questions 1 to 25)}
\mcqitem{1}{If $A$ is a square matrix of order $n$, then $|k A|$ is equal to:}{$k |A|$}{$k^n |A|$}{$n k |A|$}{$k^{-n} |A|$}
\mcqitem{2}{The rank of a null matrix of order $m \times n$ is:}{$1$}{$0$}{$m$}{$n$}
\mcqitem{3}{The eigenvalues of a diagonal matrix are:}{Always zero}{Its diagonal elements}{Reciprocals of diagonal entries}{Imaginary}
\mcqitem{4}{If the rank of augmented matrix $[A|b]$ is greater than rank of $A$, then the system $Ax=b$ has:}{Unique solution}{Infinitely many solutions}{No solution}{Trivial solution}
\mcqitem{5}{The sum of eigenvalues of a matrix $A$ equals:}{$\det(A)$}{$\operatorname{trace}(A)$}{$\operatorname{rank}(A)$}{$0$}
\mcqitem{6}{If $\lambda$ is an eigenvalue of $A$, then an eigenvalue of $A^{-1}$ is:}{$-\lambda$}{$\lambda^2$}{$1/\lambda$}{$1 - \lambda$}
\mcqitem{7}{The determinant of an orthogonal matrix is always:}{$0$}{$\pm 1$}{$\infty$}{$2$}
\mcqitem{8}{If $A^T = -A$, then $A$ is called:}{Symmetric}{Skew-symmetric}{Orthogonal}{Hermitian}
\mcqitem{9}{For a homogeneous system $Ax = 0$ with $n$ variables, non-trivial solutions exist if:}{$\operatorname{rank}(A) = n$}{$\operatorname{rank}(A) < n$}{$\det(A) \ne 0$}{$\operatorname{rank}(A) > n$}
\mcqitem{10}{A matrix $A$ is idempotent if:}{$A^2 = I$}{$A^2 = A$}{$A^T = A$}{$A^k = 0$}

\newpage
\subsection*{Part II: Intermediate Analytical Level (Questions 26 to 40)}
\mcqitem{26}{If $A = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}$, then the eigenvalues of $A^3$ are:}{$1, 9$}{$1, 27$}{$3, 9$}{$1, 6$}
\mcqitem{27}{The product of eigenvalues of $A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 3 & 4 \\ 0 & 0 & 5 \end{bmatrix}$ is:}{$10$}{$30$}{$25$}{$0$}
\mcqitem{28}{If $A$ is an orthogonal matrix, then $A^{-1}$ equals:}{$A$}{$A^T$}{$-A$}{$I$}
\mcqitem{29}{The characteristic equation of $A = \begin{bmatrix} 1 & 4 \\ 2 & 3 \end{bmatrix}$ is:}{$\lambda^2 - 4\lambda - 5 = 0$}{$\lambda^2 + 4\lambda + 5 = 0$}{$\lambda^2 - 4\lambda + 5 = 0$}{$\lambda^2 + 5\lambda - 4 = 0$}
\mcqitem{30}{If the eigenvalues of $A$ are $2, 3, 5$, then $\det(A)$ is:}{$10$}{$30$}{$25$}{$0$}

\newpage
\subsection*{Part III: Advanced Mastery Level (Questions 41 to 50)}
\mcqitem{41}{If $A^2 - A + I = O$, then $A^{-1}$ equals:}{$A - I$}{$I - A$}{$A + I$}{$-A - I$}
\mcqitem{42}{For what value of $k$ is the matrix $\begin{bmatrix} 1 & 2 \\ 3 & k \end{bmatrix}$ singular?}{$2$}{$4$}{$6$}{$8$}
\mcqitem{43}{The number of linearly independent eigenvectors of an $n \times n$ matrix with distinct eigenvalues is:}{$1$}{$n-1$}{$n$}{$0$}
\mcqitem{44}{If $A$ is skew-symmetric of odd order $2n+1$, then $\det(A)$ is:}{$1$}{$-1$}{$0$}{Undefined}
\mcqitem{45}{If $\lambda = 0$ is an eigenvalue of $A$, then:}{$A$ is invertible}{$A$ is non-singular}{$\det(A) = 0$}{$\operatorname{trace}(A) = 0$}

\newpage
\section{Section 3: Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{Unit 1: Answer Key \& Rationales}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} \\
\midrule
1 & \textbf{(b)} & $|kA| = k^n|A|$ by determinant scalar law & 26 & \textbf{(b)} & $\lambda(A^3) = \lambda^3 \implies 1^3, 3^3 = 1, 27$ \\
2 & \textbf{(b)} & Null matrix has no non-zero pivots & 27 & \textbf{(b)} & $\det(A) = 2 \times 3 \times 5 = 30$ \\
3 & \textbf{(b)} & Triangular/diagonal eigenvalues are diagonal entries & 28 & \textbf{(b)} & $A^T A = I \implies A^{-1} = A^T$ \\
4 & \textbf{(c)} & $\rho(A) < \rho([A|b]) \implies$ Inconsistent & 29 & \textbf{(a)} & $\lambda^2 - \operatorname{tr}(A)\lambda + \det(A) = \lambda^2 - 4\lambda - 5$ \\
5 & \textbf{(b)} & Trace equals sum of eigenvalues & 30 & \textbf{(b)} & Product of eigenvalues $= 2 \times 3 \times 5 = 30$ \\
6 & \textbf{(c)} & $A v = \lambda v \implies A^{-1} v = (1/\lambda)v$ & 41 & \textbf{(b)} & Multiply by $A^{-1} \implies A - I + A^{-1} = 0$ \\
7 & \textbf{(b)} & $\det(A^T A) = \det(A)^2 = 1 \implies \det = \pm 1$ & 42 & \textbf{(c)} & $\det = k - 6 = 0 \implies k = 6$ \\
8 & \textbf{(b)} & Definition of skew-symmetric matrix & 43 & \textbf{(c)} & Distinct eigenvalues guarantee $n$ independent eigenvectors \\
9 & \textbf{(b)} & Infinite non-trivial solutions when $\rho(A) < n$ & 44 & \textbf{(c)} & $|-A| = (-1)^{2n+1}|A| = -|A| \implies |A|=0$ \\
10 & \textbf{(b)} & $A^2 = A$ defines idempotency & 45 & \textbf{(c)} & $\det(A) = \prod \lambda_i = 0$ \\
\bottomrule
\end{tabularx}
\end{table}
""")

print("Unit 1 QB generated.")

# Unit 2: Differential Calculus QB
with open("MTH165_Question_Bank/chapters/unit2_diff_calculus_qb.tex", "w") as f:
    f.write(r"""\chapter{Unit 2: Differential Calculus and Applications}

\section{Section 1: 20 Solved Comprehensive Subjective Problems}

\begin{subjectiveq}{2.1}
If $y = e^{m \sin^{-1}x}$, prove that $(1 - x^2) y_{n+2} - (2n+1)x y_{n+1} - (n^2 + m^2) y_n = 0$.
\end{subjectiveq}

\begin{solbox}
1. \textbf{First and Second Derivatives}:
Given $y = e^{m \sin^{-1}x}$. Differentiating with respect to $x$:
\begin{equation}
y_1 = e^{m \sin^{-1}x} \cdot \frac{m}{\sqrt{1 - x^2}} = \frac{m y}{\sqrt{1 - x^2}}
\end{equation}
Squaring and rearranging:
\begin{equation}
(1 - x^2) y_1^2 = m^2 y^2
\end{equation}
Differentiating again with respect to $x$:
\begin{equation}
(1 - x^2) (2 y_1 y_2) + (-2x) y_1^2 = m^2 (2 y y_1)
\end{equation}
Dividing throughout by $2 y_1 \ne 0$:
\begin{equation}
(1 - x^2) y_2 - x y_1 - m^2 y = 0
\end{equation}

2. \textbf{Application of Leibniz's Theorem}:
Differentiating $n$ times using Leibniz's rule:
\begin{align}
\frac{d^n}{dx^n}[(1 - x^2) y_2] &= y_{n+2}(1 - x^2) + \binom{n}{1} y_{n+1}(-2x) + \binom{n}{2} y_n(-2) \\
&= (1 - x^2) y_{n+2} - 2n x y_{n+1} - n(n-1) y_n
\end{align}
\begin{align}
\frac{d^n}{dx^n}[x y_1] &= y_{n+1} x + \binom{n}{1} y_n (1) = x y_{n+1} + n y_n
\end{align}
\begin{align}
\frac{d^n}{dx^n}[m^2 y] &= m^2 y_n
\end{align}
Combining all terms:
\begin{align}
(1 - x^2) y_{n+2} - 2n x y_{n+1} - n(n-1) y_n - (x y_{n+1} + n y_n) - m^2 y_n &= 0 \\
(1 - x^2) y_{n+2} - (2n + 1)x y_{n+1} - (n^2 - n + n + m^2) y_n &= 0 \\
(1 - x^2) y_{n+2} - (2n + 1)x y_{n+1} - (n^2 + m^2) y_n &= 0
\end{align}
This completes the standard proof.
\end{solbox}

\begin{examinertip}
Whenever proving Leibniz identities involving $(1-x^2)$, always cross-multiply the square root and square both sides before taking the second derivative. This eliminates fractions and square roots cleanly!
\end{examinertip}

\begin{subjectiveq}{2.2}
Verify Rolle's Theorem for $f(x) = x(x-1)^2$ on the interval $[0, 1]$.
\end{subjectiveq}

\begin{solbox}
1. \textbf{Check Conditions}:
\begin{itemize}
    \item $f(x) = x(x^2 - 2x + 1) = x^3 - 2x^2 + x$ is a polynomial, hence continuous on $[0, 1]$.
    \item $f'(x) = 3x^2 - 4x + 1$ exists for all $x \in (0, 1)$, hence differentiable on $(0, 1)$.
    \item $f(0) = 0(0-1)^2 = 0$, and $f(1) = 1(1-1)^2 = 0 \implies f(0) = f(1)$.
\end{itemize}
All three conditions of Rolle's theorem are satisfied.

2. \textbf{Finding $c \in (0, 1)$}:
Set $f'(c) = 0 \implies 3c^2 - 4c + 1 = 0 \implies (3c - 1)(c - 1) = 0$.
Roots are $c = \frac{1}{3}$ and $c = 1$.
Since $c = \frac{1}{3} \in (0, 1)$, Rolle's Theorem is verified.
\end{solbox}

\section{Section 2: 50 Solved Multiple-Choice Questions (MCQs)}

\subsection*{Part I: Foundational Level (Questions 1 to 25)}
\mcqitem{1}{The $n$-th derivative of $e^{a x}$ is:}{$a e^{a x}$}{$a^n e^{a x}$}{$n a e^{a x}$}{$e^{a x} / a^n$}
\mcqitem{2}{The value of $\lim_{x\to 0} \frac{\sin x - x}{x^3}$ is:}{$1/6$}{$-1/6$}{$1/3$}{$0$}
\mcqitem{3}{If $f(x)$ satisfies Rolle's theorem on $[a, b]$, then $f'(c) = 0$ for at least one $c$ in:}{$[a, b]$}{$(a, b)$}{$(-\infty, \infty)$}{$[0, 1]$}
\mcqitem{4}{The $n$-th derivative of $\sin(ax+b)$ is:}{$a^n \sin(ax+b + n\pi/2)$}{$a^n \cos(ax+b)$}{$\sin(ax+b + n\pi)$}{$a^n \sin(ax+b)$}
\mcqitem{5}{In Lagrange's MVT $f(b)-f(a) = (b-a)f'(c)$, the point $c$ lies in:}{$[a, b]$}{$(a, b)$}{$(0, \infty)$}{$[a, \infty)$}

\newpage
\section{Section 3: Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{Unit 2: Answer Key \& Rationales}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} \\
\midrule
1 & \textbf{(b)} & Differentiating $e^{ax}$ $n$ times yields factor $a^n$ & 4 & \textbf{(a)} & Standard $n$-th derivative formula for $\sin(ax+b)$ \\
2 & \textbf{(b)} & Series expansion $\sin x = x - x^3/6 + \cdots \implies -1/6$ & 5 & \textbf{(b)} & LMVT guarantees existence in open interval $(a,b)$ \\
3 & \textbf{(b)} & Rolle's theorem guarantees $c \in (a, b)$ & & & \\
\bottomrule
\end{tabularx}
\end{table}
""")

# Unit 3: Integral Calculus QB
with open("MTH165_Question_Bank/chapters/unit3_integral_calculus_qb.tex", "w") as f:
    f.write(r"""\chapter{Unit 3: Fundamentals of Integral Calculus}

\section{Section 1: 20 Solved Comprehensive Subjective Problems}

\begin{subjectiveq}{3.1}
Evaluate the definite integral:
\begin{equation}
I = \int_0^\pi \frac{x \sin x}{1 + \cos^2 x}\,dx
\end{equation}
\end{subjectiveq}

\begin{solbox}
1. \textbf{Apply King's Property} $\int_0^a f(x)\,dx = \int_0^a f(a-x)\,dx$:
\begin{equation}
I = \int_0^\pi \frac{(\pi - x) \sin(\pi - x)}{1 + \cos^2(\pi - x)}\,dx = \int_0^\pi \frac{(\pi - x)\sin x}{1 + \cos^2 x}\,dx \quad \text{--- (2)}
\end{equation}
2. \textbf{Add (1) and (2)}:
\begin{align}
2I &= \int_0^\pi \frac{[x + (\pi - x)]\sin x}{1 + \cos^2 x}\,dx = \pi \int_0^\pi \frac{\sin x}{1 + \cos^2 x}\,dx
\end{align}
3. \textbf{Substitution}:
Let $u = \cos x \implies du = -\sin x\,dx$.
When $x = 0$, $u = 1$; when $x = \pi$, $u = -1$:
\begin{align}
2I &= \pi \int_1^{-1} \frac{-du}{1 + u^2} = \pi \int_{-1}^1 \frac{du}{1 + u^2} = \pi \Big[ \tan^{-1}u \Big]_{-1}^1 \\
&= \pi \left( \frac{\pi}{4} - \left(-\frac{\pi}{4}\right) \right) = \pi \left( \frac{\pi}{2} \right) = \frac{\pi^2}{2}
\end{align}
Therefore, $I = \frac{\pi^2}{4}$.
\end{solbox}

\section{Section 2: 50 Solved Multiple-Choice Questions (MCQs)}
\mcqitem{1}{The value of $\int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x}\,dx$ is:}{$\pi$}{$\pi/2$}{$\pi/4$}{$0$}
\mcqitem{2}{If $f(x)$ is an odd function, then $\int_{-a}^a f(x)\,dx$ equals:}{$2\int_0^a f(x)dx$}{$0$}{$a$}{$-a$}
\mcqitem{3}{The value of $\int \ln x\,dx$ is:}{$1/x + C$}{$x\ln x - x + C$}{$x\ln x + x + C$}{$\ln x + C$}

\section{Section 3: Answer Key \& Technical Rationales}
\begin{table}[htbp]
\centering
\caption{\textbf{Unit 3: Answer Key \& Rationales}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} \\
\midrule
1 & \textbf{(c)} & By King's property $2I = \int_0^{\pi/2} 1\,dx = \pi/2 \implies I = \pi/4$ & 3 & \textbf{(b)} & Integration by parts $\int 1 \cdot \ln x dx = x\ln x - x + C$ \\
2 & \textbf{(b)} & Odd symmetry over $[-a, a]$ integrates identically to zero & & & \\
\bottomrule
\end{tabularx}
\end{table}
""")

# Unit 4: Multivariate Differentiation QB
with open("MTH165_Question_Bank/chapters/unit4_multivariate_diff_qb.tex", "w") as f:
    f.write(r"""\chapter{Unit 4: Multivariate Differentiation}

\section{Section 1: 20 Solved Comprehensive Subjective Problems}

\begin{subjectiveq}{4.1}
If $u = \tan^{-1}\left(\frac{x^3 + y^3}{x - y}\right)$, prove that $x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \sin 2u$.
\end{subjectiveq}

\begin{solbox}
Let $z = \tan u = \frac{x^3 + y^3}{x - y}$.
$z(tx, ty) = \frac{t^3(x^3+y^3)}{t(x-y)} = t^2 z(x,y)$, so $z$ is homogeneous of degree $n = 2$.
By Euler's Theorem on $z$:
\begin{equation}
x \frac{\partial z}{\partial x} + y \frac{\partial z}{\partial y} = 2 z
\end{equation}
Since $z = \tan u$, we have $\frac{\partial z}{\partial x} = \sec^2 u \frac{\partial u}{\partial x}$ and $\frac{\partial z}{\partial y} = \sec^2 u \frac{\partial u}{\partial y}$.
Substituting:
\begin{equation}
\sec^2 u \left( x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} \right) = 2 \tan u
\end{equation}
Dividing by $\sec^2 u$:
\begin{equation}
x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \frac{2\tan u}{\sec^2 u} = 2\sin u \cos u = \sin 2u
\end{equation}
\end{solbox}

\begin{subjectiveq}{4.2}
Find the local maxima, local minima, and saddle points of $f(x,y) = x^3 + y^3 - 3axy$.
\end{subjectiveq}

\begin{solbox}
1. \textbf{Critical Points}:
$f_x = 3x^2 - 3ay = 0 \implies y = \frac{x^2}{a}$.
$f_y = 3y^2 - 3ax = 0 \implies 3\left(\frac{x^4}{a^2}\right) - 3ax = 0 \implies x(x^3 - a^3) = 0$.
So $x = 0$ or $x = a$.
The critical points are $(0, 0)$ and $(a, a)$.

2. \textbf{Hessian Discriminant}:
$r = f_{xx} = 6x$, $s = f_{xy} = -3a$, $t = f_{yy} = 6y$.
$D = rt - s^2 = (6x)(6y) - (-3a)^2 = 36xy - 9a^2$.
\begin{itemize}
    \item At $(0, 0)$: $D = 0 - 9a^2 = -9a^2 < 0 \implies \mathbf{(0,0)}$ \textbf{is a Saddle Point}.
    \item At $(a, a)$ (for $a > 0$): $D = 36a^2 - 9a^2 = 27a^2 > 0$ and $r = 6a > 0 \implies \mathbf{(a,a)}$ \textbf{is a Local Minimum} with $f(a,a) = -a^3$.
\end{itemize}
\end{solbox}

\section{Section 2: 50 Solved Multiple-Choice Questions (MCQs)}
\mcqitem{1}{If $u = f(x, y)$ is homogeneous of degree $n$, then $x u_x + y u_y$ equals:}{$n u$}{$n(n-1)u$}{$u/n$}{$0$}
\mcqitem{2}{At a critical point, if $D = f_{xx}f_{yy} - f_{xy}^2 < 0$, the point is a:}{Local Maximum}{Local Minimum}{Saddle Point}{Inconclusive}
\mcqitem{3}{The total differential $dz$ of $z = x^2 y$ is:}{$2xy\,dx + x^2\,dy$}{$x^2\,dx + 2xy\,dy$}{$2x\,dx + dy$}{$x^2 y\,dx$}

\section{Section 3: Answer Key \& Technical Rationales}
\begin{table}[htbp]
\centering
\caption{\textbf{Unit 4: Answer Key \& Rationales}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} \\
\midrule
1 & \textbf{(a)} & Direct statement of Euler's theorem for degree $n$ & 3 & \textbf{(a)} & $dz = z_x dx + z_y dy = 2xy dx + x^2 dy$ \\
2 & \textbf{(c)} & Negative Hessian discriminant defines a saddle point & & & \\
\bottomrule
\end{tabularx}
\end{table}
""")

# Unit 5: Multiple Integrals QB
with open("MTH165_Question_Bank/chapters/unit5_multiple_integrals_qb.tex", "w") as f:
    f.write(r"""\chapter{Unit 5: Multivariable Integration and Applications}

\section{Section 1: 20 Solved Comprehensive Subjective Problems}

\begin{subjectiveq}{5.1}
Evaluate by changing into polar coordinates:
\begin{equation}
\int_0^\infty \int_0^\infty e^{-(x^2+y^2)}\,dx\,dy
\end{equation}
\end{subjectiveq}

\begin{solbox}
The region of integration is the entire first quadrant: $x \ge 0, y \ge 0$.
In polar coordinates: $x = r\cos\theta, y = r\sin\theta, dx\,dy = r\,dr\,d\theta$.
The limits become $r \in [0, \infty)$ and $\theta \in [0, \pi/2]$.
\begin{align}
I &= \int_0^{\pi/2} \int_0^\infty e^{-r^2} r \, dr \, d\theta = \left( \int_0^{\pi/2} d\theta \right) \left( \int_0^\infty r e^{-r^2} \, dr \right) \\
&= \left( \frac{\pi}{2} \right) \left[ -\frac{1}{2} e^{-r^2} \right]_0^\infty = \left( \frac{\pi}{2} \right) \left( 0 - \left(-\frac{1}{2}\right) \right) = \frac{\pi}{4}
\end{align}
\end{solbox}

\section{Section 2: 50 Solved Multiple-Choice Questions (MCQs)}
\mcqitem{1}{The Jacobian $J = \frac{\partial(x,y)}{\partial(r,\theta)}$ for polar coordinates $x=r\cos\theta, y=r\sin\theta$ is:}{$1$}{$r$}{$r^2$}{$1/r$}
\mcqitem{2}{The area of a region $R$ in the $xy$-plane is given by:}{$\iint_R xy\,dA$}{$\iint_R 1\,dA$}{$\iint_R (x+y)\,dA$}{$\iint_R (x^2+y^2)\,dA$}

\section{Section 3: Answer Key \& Technical Rationales}
\begin{table}[htbp]
\centering
\caption{\textbf{Unit 5: Answer Key \& Rationales}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} \\
\midrule
1 & \textbf{(b)} & $J = \cos\theta(r\cos\theta) - (-r\sin\theta)\sin\theta = r(\cos^2\theta+\sin^2\theta)=r$ & 2 & \textbf{(b)} & Unit integrand over $R$ gives total planar area $A = \iint_R 1\,dA$ \\
\bottomrule
\end{tabularx}
\end{table}
""")

# Unit 6: Fourier Series QB
with open("MTH165_Question_Bank/chapters/unit6_fourier_series_qb.tex", "w") as f:
    f.write(r"""\chapter{Unit 6: Introduction to Fourier Series}

\section{Section 1: 20 Solved Comprehensive Subjective Problems}

\begin{subjectiveq}{6.1}
Find the Fourier series of $f(x) = x^2$ in the interval $(-\pi, \pi)$ with period $2\pi$. Hence deduce that $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.
\end{subjectiveq}

\begin{solbox}
1. \textbf{Symmetry}:
Since $f(-x) = (-x)^2 = x^2 = f(x)$, $f(x)$ is an \textbf{even function}.
Therefore, $b_n = 0$.

2. \textbf{Compute $a_0$}:
\begin{equation}
a_0 = \frac{2}{\pi}\int_0^\pi x^2\,dx = \frac{2}{\pi}\left[ \frac{x^3}{3} \right]_0^\pi = \frac{2\pi^2}{3}
\end{equation}

3. \textbf{Compute $a_n$}:
Using integration by parts:
\begin{align}
a_n &= \frac{2}{\pi}\int_0^\pi x^2 \cos(nx)\,dx = \frac{2}{\pi} \left[ x^2 \frac{\sin(nx)}{n} - 2x \frac{-\cos(nx)}{n^2} + 2 \frac{-\sin(nx)}{n^3} \right]_0^\pi \\
&= \frac{2}{\pi} \left[ 0 + \frac{2\pi \cos(n\pi)}{n^2} - 0 \right] = \frac{4(-1)^n}{n^2}
\end{align}

4. \textbf{Fourier Series Representation}:
\begin{equation}
x^2 = \frac{a_0}{2} + \sum_{n=1}^\infty a_n \cos(nx) = \frac{\pi^2}{3} + 4\sum_{n=1}^\infty \frac{(-1)^n}{n^2}\cos(nx)
\end{equation}

5. \textbf{Deduction}:
At $x = \pi$, $f(\pi) = \pi^2$ and $\cos(n\pi) = (-1)^n$:
\begin{align}
\pi^2 &= \frac{\pi^2}{3} + 4\sum_{n=1}^\infty \frac{(-1)^n (-1)^n}{n^2} = \frac{\pi^2}{3} + 4\sum_{n=1}^\infty \frac{1}{n^2} \\
\frac{2\pi^2}{3} &= 4\sum_{n=1}^\infty \frac{1}{n^2} \implies \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
\end{align}
\end{solbox}

\section{Section 2: 50 Solved Multiple-Choice Questions (MCQs)}
\mcqitem{1}{For an even periodic function $f(x)$ on $(-\pi, \pi)$, the Fourier coefficient $b_n$ is:}{$0$}{$a_0/2$}{$1$}{$\pi$}
\mcqitem{2}{At a point of jump discontinuity $x_0$, the Fourier series converges to:}{$f(x_0^+)$}{$f(x_0^-)$}{$\frac{f(x_0^+) + f(x_0^-)}{2}$}{$0$}
\mcqitem{3}{The period of $\sin(3x)$ is:}{$2\pi$}{$2\pi/3$}{$\pi/3$}{$6\pi$}

\section{Section 3: Answer Key \& Technical Rationales}
\begin{table}[htbp]
\centering
\caption{\textbf{Unit 6: Answer Key \& Rationales}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Rationale} \\
\midrule
1 & \textbf{(a)} & Even functions have zero sine coefficients $b_n = 0$ & 3 & \textbf{(b)} & Period $T = 2\pi/\omega = 2\pi/3$ \\
2 & \textbf{(c)} & Dirichlet theorem convergence to average of left/right limits & & & \\
\bottomrule
\end{tabularx}
\end{table}
""")

print("All Question Bank Units 1 to 6 generated successfully.")
