import os

print("Writing Textbook Chapters...")

# Chapter 1: Matrix Methods and Linear Systems
with open("MTH165/chapters/chapter-01-matrix-methods.tex", "w") as f:
    f.write(r"""\chapter{Matrix Methods and Linear Systems}
\label{chap:matrix-methods}

% ==============================================================================
% SECTION 1.1: OVERVIEW & LEARNING OBJECTIVES
% ==============================================================================
\section{Unit Overview \& Learning Objectives}

Matrix algebra and the theory of linear systems form the fundamental computational backbone of modern engineering disciplines. From structural finite element analysis and electrical circuit simulation to machine learning, robotics, and fluid dynamics, physical systems are routinely modeled as systems of linear equations and linear transformations.

This chapter develops the rigorous algebraic and geometric framework of matrices: elementary row and column operations, row echelon reductions, determinantal and echelon ranks, vector space independence, the solvability and consistency of linear systems ($Ax=b$ and $Ax=0$) via the Rouch\'e--Capelli theorem, matrix inversion techniques, spectral analysis (eigenvalues and eigenvectors), and the Cayley--Hamilton theorem.

\begin{important}[Core Learning Objectives]
After mastering this unit, the student will be able to:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Classify Matrix Types \& Properties}: Analyze symmetric, skew-symmetric, orthogonal, Hermitian, and unitary matrices.
    \item \textbf{Perform Elementary Transformations}: Reduce any matrix $A \in \mathbb{R}^{m\times n}$ to Row Echelon Form (REF) and Reduced Row Echelon Form (RREF).
    \item \textbf{Compute Matrix Rank}: Determine $\operatorname{rank}(A)$ using minor determinants and pivot counts in echelon forms.
    \item \textbf{Test Vector Independence}: Establish linear dependence or independence of a set of vectors $\{v_1, v_2, \dots, v_k\} \subset \mathbb{R}^n$.
    \item \textbf{Solve Linear Systems ($Ax=b$ and $Ax=0$)}: Characterize unique, infinite, and no-solution regimes using augmented matrices $[A|b]$ and the Rouch\'e--Capelli theorem.
    \item \textbf{Invert Matrices}: Compute $A^{-1}$ using the classical Adjugate formula and the Gauss--Jordan row-elimination method $[A | I] \sim [I | A^{-1}]$.
    \item \textbf{Compute Eigenvalues \& Eigenvectors}: Solve the characteristic equation $|A - \lambda I| = 0$, construct eigenspaces, and analyze algebraic vs. geometric multiplicity.
    \item \textbf{Apply the Cayley--Hamilton Theorem}: Verify that every square matrix satisfies its own characteristic polynomial, and compute matrix inverses $A^{-1}$ and powers $A^n$.
\end{enumerate}
\end{important}

% ==============================================================================
% SECTION 1.2: MATRIX FUNDAMENTALS & SPECIAL MATRICES
% ==============================================================================
\section{Matrix Fundamentals \& Classification}

\begin{definition}[Matrix Definition]
A matrix $A$ of order $m \times n$ is a rectangular array of $m \times n$ real or complex numbers arranged in $m$ horizontal rows and $n$ vertical columns:
\begin{equation}
A = [a_{ij}] = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}, \quad i \in \{1,\dots,m\}, \; j \in \{1,\dots,n\}
\end{equation}
\end{definition}

\subsection{Special Matrix Classes in Engineering}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Symmetric Matrix}: A square matrix $A$ where $A^T = A$, meaning $a_{ij} = a_{ji}$. All eigenvalues are strictly real.
    \item \textbf{Skew-Symmetric Matrix}: A square matrix where $A^T = -A$, meaning $a_{ij} = -a_{ji}$ and all diagonal entries $a_{ii} = 0$. Eigenvalues are either zero or purely imaginary.
    \item \textbf{Orthogonal Matrix}: A real square matrix $A$ satisfying $A^T A = A A^T = I$, so $A^{-1} = A^T$. The determinant satisfies $\det(A) = \pm 1$.
    \item \textbf{Hermitian Matrix}: A complex square matrix $A$ satisfying $A^* = (\bar{A})^T = A$.
    \item \textbf{Unitary Matrix}: A complex square matrix satisfying $A^* A = I$.
    \item \textbf{Idempotent Matrix}: A matrix satisfying $A^2 = A$. Its eigenvalues are always 0 or 1.
    \item \textbf{Nilpotent Matrix}: A matrix for which there exists an integer $k \ge 1$ such that $A^k = O$. All eigenvalues of a nilpotent matrix are 0.
\end{itemize}

% ==============================================================================
% SECTION 1.3: ELEMENTARY TRANSFORMATIONS & MATRIX RANK
% ==============================================================================
\section{Elementary Operations, Echelon Form \& Rank}

\subsection{Elementary Row and Column Operations}
There are three elementary row operations:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Interchange}: $R_i \leftrightarrow R_j$ (swap row $i$ and row $j$).
    \item \textbf{Scaling}: $R_i \to k R_i$ where $k \ne 0$ is a non-zero scalar.
    \item \textbf{Row Addition}: $R_i \to R_i + c R_j$ where $c \in \mathbb{R}$ and $j \ne i$.
\end{enumerate}
Elementary operations preserve the row space and rank of a matrix.

\begin{definition}[Row Echelon Form (REF)]
A matrix is in \textbf{Row Echelon Form (REF)} if:
\begin{enumerate}[leftmargin=1.5em]
    \item All all-zero rows are grouped at the bottom of the matrix.
    \item In each non-zero row, the leading entry (the first non-zero entry from the left, called the \textbf{pivot}) occurs strictly to the right of the leading entry of the row above it.
\end{enumerate}
If in addition each pivot is $1$ and is the only non-zero entry in its column, the matrix is in \textbf{Reduced Row Echelon Form (RREF)}.
\end{definition}

\begin{definition}[Rank of a Matrix]
The \textbf{rank} of a matrix $A$, denoted $\operatorname{rank}(A)$ or $\rho(A)$, is defined equivalently as:
\begin{enumerate}[leftmargin=1.5em]
    \item The maximum number of linearly independent row (or column) vectors of $A$.
    \item The number of non-zero rows in the Row Echelon Form of $A$.
    \item The order of the largest square submatrix of $A$ whose determinant is non-zero (determinantal rank).
\end{enumerate}
\end{definition}

\begin{example}[Rank via Row Reduction]
Determine the rank of the matrix:
\begin{equation}
A = \begin{bmatrix}
1 & 2 & -1 & 3 \\
2 & 4 & 1 & -2 \\
3 & 6 & 3 & -7
\end{bmatrix}
\end{equation}
\end{example}

\begin{solutionbox}
Apply elementary row operations to reduce $A$ to Row Echelon Form:
\begin{enumerate}[leftmargin=1.5em]
    \item $R_2 \to R_2 - 2R_1$:
    \begin{equation}
    \begin{bmatrix}
    1 & 2 & -1 & 3 \\
    0 & 0 & 3 & -8 \\
    3 & 6 & 3 & -7
    \end{bmatrix}
    \end{equation}
    \item $R_3 \to R_3 - 3R_1$:
    \begin{equation}
    \begin{bmatrix}
    1 & 2 & -1 & 3 \\
    0 & 0 & 3 & -8 \\
    0 & 0 & 6 & -16
    \end{bmatrix}
    \end{equation}
    \item $R_3 \to R_3 - 2R_2$:
    \begin{equation}
    \begin{bmatrix}
    1 & 2 & -1 & 3 \\
    0 & 0 & 3 & -8 \\
    0 & 0 & 0 & 0
    \end{bmatrix}
    \end{equation}
\end{enumerate}
The row echelon form contains \textbf{2 non-zero rows}. Therefore, $\operatorname{rank}(A) = 2$.
\end{solutionbox}

% ==============================================================================
% SECTION 1.4: LINEAR DEPENDENCE & INDEPENDENCE
% ==============================================================================
\section{Linear Dependence and Independence of Vectors}

\begin{definition}[Linear Independence]
A set of vectors $\{v_1, v_2, \dots, v_k\}$ in $\mathbb{R}^n$ is \textbf{linearly independent} if the vector equation:
\begin{equation}
c_1 v_1 + c_2 v_2 + \cdots + c_k v_k = \mathbf{0}
\end{equation}
admits only the trivial solution $c_1 = c_2 = \cdots = c_k = 0$. If there exists at least one non-zero scalar $c_i \ne 0$ satisfying the equation, the vectors are \textbf{linearly dependent}.
\end{definition}

\begin{theorem}[Matrix Criterion for Linear Independence]
Let $A = [v_1 | v_2 | \cdots | v_k]$ be the $n \times k$ matrix formed by placing the vectors as column vectors.
\begin{itemize}[leftmargin=1.5em]
    \item The vectors are linearly independent if and only if $\operatorname{rank}(A) = k$.
    \item For $n$ vectors in $\mathbb{R}^n$, the set is linearly independent if and only if $\det(A) \ne 0$.
\end{itemize}
\end{theorem}

% ==============================================================================
% SECTION 1.5: SYSTEMS OF LINEAR EQUATIONS
% ==============================================================================
\section{Systems of Linear Equations \& Rouch\'e--Capelli Theorem}

Consider a system of $m$ linear equations in $n$ unknowns:
\begin{equation}
Ax = b, \quad A \in \mathbb{R}^{m\times n}, \; x \in \mathbb{R}^n, \; b \in \mathbb{R}^m
\end{equation}
The augmented matrix is defined as $\tilde{A} = [A | b]$.

\begin{theorem}[Rouch\'e--Capelli Theorem]
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Inconsistent System (No Solution)}:
    \begin{equation}
    \operatorname{rank}(A) < \operatorname{rank}([A | b])
    \end{equation}
    \item \textbf{Consistent System with Unique Solution}:
    \begin{equation}
    \operatorname{rank}(A) = \operatorname{rank}([A | b]) = n \quad (\text{where } n \text{ is the number of unknowns})
    \end{equation}
    \item \textbf{Consistent System with Infinitely Many Solutions}:
    \begin{equation}
    \operatorname{rank}(A) = \operatorname{rank}([A | b]) = r < n
    \end{equation}
    The solution space has $(n - r)$ free parameters (degrees of freedom).
\end{enumerate}
\end{theorem}

\begin{theorem}[Homogeneous Linear Systems $Ax = 0$]
For a homogeneous system $Ax = 0$ ($n$ unknowns):
\begin{enumerate}[leftmargin=1.5em]
    \item The system is always consistent because $x = \mathbf{0}$ (the trivial solution) is always a solution.
    \item If $\operatorname{rank}(A) = n$, the system has \textbf{only the trivial solution}.
    \item If $\operatorname{rank}(A) < n$, the system possesses \textbf{infinitely many non-trivial solutions} with $(n - \operatorname{rank}(A))$ linearly independent basic solutions.
    \item For a square system $n \times n$, non-trivial solutions exist if and only if $\det(A) = 0$.
\end{enumerate}
\end{theorem}

\begin{example}[Parametric Consistency Investigation]
Investigate for what values of $\lambda$ and $\mu$ the following system has (i) no solution, (ii) a unique solution, and (iii) infinitely many solutions:
\begin{align}
x + y + z &= 6 \\
x + 2y + 3z &= 10 \\
x + 2y + \lambda z &= \mu
\end{align}
\end{example}

\begin{solutionbox}
Write the augmented matrix $[A|b]$ and row reduce:
\begin{equation}
[A|b] = \begin{bmatrix}
1 & 1 & 1 & 6 \\
1 & 2 & 3 & 10 \\
1 & 2 & \lambda & \mu
\end{bmatrix}
\end{equation}
Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:
\begin{equation}
\sim \begin{bmatrix}
1 & 1 & 1 & 6 \\
0 & 1 & 2 & 4 \\
0 & 1 & \lambda - 1 & \mu - 6
\end{bmatrix}
\end{equation}
Apply $R_3 \to R_3 - R_2$:
\begin{equation}
\sim \begin{bmatrix}
1 & 1 & 1 & 6 \\
0 & 1 & 2 & 4 \\
0 & 0 & \lambda - 3 & \mu - 10
\end{bmatrix}
\end{equation}

\textbf{Case Analysis}:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{No Solution}: Occurs when $\operatorname{rank}(A) \ne \operatorname{rank}([A|b])$.
    This requires $\lambda - 3 = 0$ and $\mu - 10 \ne 0 \implies \mathbf{\lambda = 3, \; \mu \ne 10}$. Then $\operatorname{rank}(A) = 2$ while $\operatorname{rank}([A|b]) = 3$.
    \item \textbf{Unique Solution}: Occurs when $\operatorname{rank}(A) = \operatorname{rank}([A|b]) = 3$.
    This requires $\lambda - 3 \ne 0 \implies \mathbf{\lambda \ne 3}$, for any real value of $\mu$.
    \item \textbf{Infinitely Many Solutions}: Occurs when $\operatorname{rank}(A) = \operatorname{rank}([A|b]) = 2 < 3$.
    This requires $\lambda - 3 = 0$ and $\mu - 10 = 0 \implies \mathbf{\lambda = 3, \; \mu = 10}$.
\end{enumerate}
\end{solutionbox}

% ==============================================================================
% SECTION 1.6: EIGENVALUES & EIGENVECTORS
% ==============================================================================
\section{Eigenvalues, Eigenvectors \& Spectral Properties}

\begin{definition}[Eigenvalue and Eigenvector]
Let $A$ be an $n \times n$ square matrix. A scalar $\lambda \in \mathbb{C}$ is called an \textbf{eigenvalue} (or characteristic root) of $A$ if there exists a non-zero vector $v \in \mathbb{C}^n$ such that:
\begin{equation}
A v = \lambda v \iff (A - \lambda I) v = \mathbf{0}
\end{equation}
The vector $v \ne \mathbf{0}$ is called the \textbf{eigenvector} corresponding to $\lambda$.
\end{definition}

\begin{definition}[Characteristic Equation]
The condition for non-trivial solutions to $(A - \lambda I) v = \mathbf{0}$ is:
\begin{equation}
\det(A - \lambda I) = 0
\end{equation}
For a $2 \times 2$ matrix $A$:
\begin{equation}
\lambda^2 - \operatorname{tr}(A) \lambda + \det(A) = 0
\end{equation}
For a $3 \times 3$ matrix $A$:
\begin{equation}
\lambda^3 - S_1 \lambda^2 + S_2 \lambda - S_3 = 0
\end{equation}
where $S_1 = \operatorname{tr}(A) = a_{11}+a_{22}+a_{33}$, $S_2 = M_{11}+M_{22}+M_{33}$ (sum of principal minors), and $S_3 = \det(A)$.
\end{definition}

\begin{theorem}[Fundamental Properties of Eigenvalues]
Let $\lambda_1, \lambda_2, \dots, \lambda_n$ be the eigenvalues of $A$:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Sum of Eigenvalues}: $\sum_{i=1}^n \lambda_i = \operatorname{trace}(A) = \sum_{i=1}^n a_{ii}$.
    \item \textbf{Product of Eigenvalues}: $\prod_{i=1}^n \lambda_i = \det(A)$.
    \item \textbf{Eigenvalues of Powers}: If $\lambda$ is an eigenvalue of $A$, then $\lambda^k$ is an eigenvalue of $A^k$ ($k \in \mathbb{N}$).
    \item \textbf{Eigenvalues of Inverse}: If $A$ is invertible, the eigenvalues of $A^{-1}$ are $1/\lambda_i$.
    \item \textbf{Eigenvalues of Transpose}: $A$ and $A^T$ have identical eigenvalues.
    \item \textbf{Triangular Matrices}: The eigenvalues of upper/lower triangular and diagonal matrices are simply their main diagonal elements.
\end{enumerate}
\end{theorem}

\begin{example}[Complete Spectral Decomposition]
Find the eigenvalues and corresponding eigenvectors of:
\begin{equation}
A = \begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix}
\end{equation}
\end{example}

\begin{solutionbox}
Compute the coefficients of the characteristic polynomial:
\begin{align}
S_1 &= \operatorname{tr}(A) = 2 + 3 + 2 = 7 \\
S_2 &= \begin{vmatrix} 3 & 1 \\ 2 & 2 \end{vmatrix} + \begin{vmatrix} 2 & 1 \\ 1 & 2 \end{vmatrix} + \begin{vmatrix} 2 & 2 \\ 1 & 3 \end{vmatrix} = (6 - 2) + (4 - 1) + (6 - 2) = 4 + 3 + 4 = 11 \\
S_3 &= \det(A) = 2(6-2) - 2(2-1) + 1(2-3) = 8 - 2 - 1 = 5
\end{align}
The characteristic equation is:
\begin{equation}
\lambda^3 - 7\lambda^2 + 11\lambda - 5 = 0
\end{equation}
Testing rational roots: $\lambda = 1 \implies 1 - 7 + 11 - 5 = 0$.
Factoring: $(\lambda - 1)(\lambda^2 - 6\lambda + 5) = (\lambda - 1)^2(\lambda - 5) = 0$.
Thus, the eigenvalues are $\mathbf{\lambda_1 = 5, \; \lambda_2 = 1, \; \lambda_3 = 1}$.

\textbf{Eigenvector for $\lambda = 5$}:
Solve $(A - 5I) v = 0$:
\begin{equation}
\begin{bmatrix}
-3 & 2 & 1 \\
1 & -2 & 1 \\
1 & 2 & -3
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
\end{equation}
From equations: $-3x + 2y + z = 0$ and $x - 2y + z = 0$.
Adding them: $-2x + 2z = 0 \implies x = z$.
Then $x - 2y + x = 0 \implies 2y = 2x \implies y = x$.
Setting $x = 1$, we obtain:
\begin{equation}
v_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
\end{equation}

\textbf{Eigenvectors for repeated eigenvalue $\lambda = 1$}:
Solve $(A - I) v = 0$:
\begin{equation}
\begin{bmatrix}
1 & 2 & 1 \\
1 & 2 & 1 \\
1 & 2 & 1
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
\end{equation}
This yields a single independent equation: $x + 2y + z = 0 \implies x = -2y - z$.
Since $\operatorname{rank}(A-I) = 1$, the geometric multiplicity is $n - r = 3 - 1 = 2$.
Choosing free parameters $(y=1, z=0)$ gives $v_2 = \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}$.
Choosing free parameters $(y=0, z=1)$ gives $v_3 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$.
\end{solutionbox}

% ==============================================================================
% SECTION 1.7: CAYLEY-HAMILTON THEOREM
% ==============================================================================
\section{The Cayley--Hamilton Theorem \& Applications}

\begin{theorem}[Cayley--Hamilton Theorem]
Every square matrix $A \in \mathbb{R}^{n\times n}$ satisfies its own characteristic equation. That is, if the characteristic polynomial of $A$ is:
\begin{equation}
p(\lambda) = \det(A - \lambda I) = (-1)^n \lambda^n + c_{n-1} \lambda^{n-1} + \cdots + c_1 \lambda + c_0
\end{equation}
then the matrix equation holds identically:
\begin{equation}
p(A) = (-1)^n A^n + c_{n-1} A^{n-1} + \cdots + c_1 A + c_0 I = O
\end{equation}
\end{theorem}

\subsection{Engineering Applications}
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Computation of Matrix Inverse}: If $A$ is non-singular ($c_0 \ne 0$), multiplying by $A^{-1}$ yields:
    \begin{equation}
    A^{-1} = -\frac{1}{c_0} \left[ (-1)^n A^{n-1} + c_{n-1} A^{n-2} + \cdots + c_1 I \right]
    \end{equation}
    \item \textbf{Reduction of Higher Matrix Powers}: Any polynomial $P(A)$ of degree $k \ge n$ can be reduced using polynomial division $P(\lambda) = Q(\lambda)p(\lambda) + R(\lambda)$ to a polynomial $R(A)$ of degree at most $n-1$:
    \begin{equation}
    P(A) = R(A) = r_{n-1} A^{n-1} + \cdots + r_1 A + r_0 I
    \end{equation}
\end{enumerate}

\begin{example}[Inverse and Higher Powers via Cayley--Hamilton]
Given $A = \begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix}$, verify the Cayley--Hamilton theorem, find $A^{-1}$, and evaluate $A^8$.
\end{example}

\begin{solutionbox}
1. \textbf{Characteristic Equation}:
\begin{equation}
|A - \lambda I| = \begin{vmatrix} 1 - \lambda & 2 \\ 2 & -1 - \lambda \end{vmatrix} = (1-\lambda)(-1-\lambda) - 4 = \lambda^2 - 1 - 4 = \lambda^2 - 5 = 0
\end{equation}
By Cayley--Hamilton, $A^2 - 5I = O \implies A^2 = 5I$.

2. \textbf{Verification}:
\begin{equation}
A^2 = \begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix} = \begin{bmatrix} 1+4 & 2-2 \\ 2-2 & 4+1 \end{bmatrix} = \begin{bmatrix} 5 & 0 \\ 0 & 5 \end{bmatrix} = 5I
\end{equation}
Hence $A^2 - 5I = O$ is verified.

3. \textbf{Computation of $A^{-1}$}:
Multiply $A^2 - 5I = O$ by $A^{-1}$:
\begin{equation}
A - 5A^{-1} = O \implies A^{-1} = \frac{1}{5}A = \frac{1}{5}\begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix}
\end{equation}

4. \textbf{Computation of $A^8$}:
Since $A^2 = 5I$:
\begin{equation}
A^8 = (A^2)^4 = (5I)^4 = 5^4 I = 625 I = \begin{bmatrix} 625 & 0 \\ 0 & 625 \end{bmatrix}
\end{equation}
\end{solutionbox}

\begin{examtip}[Speed Technique for Cayley--Hamilton]
When computing $A^n$ for large $n$, if the eigenvalues are distinct $\lambda_1, \lambda_2$, set $\lambda^n = q(\lambda)p(\lambda) + a\lambda + b$. Substituting $\lambda = \lambda_1, \lambda_2$ instantly gives the two linear equations for $a$ and $b$, avoiding tedious matrix multiplications!
\end{examtip}

""")

print("Chapter 1 written successfully.")

# Chapter 2: Differential Calculus and its Applications
with open("MTH165/chapters/chapter-02-differential-calculus.tex", "w") as f:
    f.write(r"""\chapter{Differential Calculus and Applications}
\label{chap:differential-calculus}

% ==============================================================================
% SECTION 2.1: OVERVIEW & LEARNING OBJECTIVES
% ==============================================================================
\section{Unit Overview \& Learning Objectives}

Differential calculus investigates instantaneous rates of change, slopes of tangents, geometric curvatures, and local functional approximations. In engineering analysis, derivatives quantify velocities, accelerations, dynamic strain gradients, optimization criteria for structural design, and error margins.

\begin{important}[Core Learning Objectives]
After mastering this unit, the student will be able to:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Master Advanced Differentiation}: Execute implicit, parametric, and logarithmic differentiation on complex engineering relations.
    \item \textbf{Apply Successive Differentiation}: Compute the $n$-th derivatives of standard functions ($e^{ax}, \sin(ax+b), \cos(ax+b), (ax+b)^m, \ln(ax+b)$) and apply \textbf{Leibniz's Rule} for product differentiation.
    \item \textbf{Apply Mean Value Theorems}: Verify and apply Rolle's Theorem, Lagrange's Mean Value Theorem (LMVT), and Cauchy's Mean Value Theorem (CMVT) to establish analytical bounds and inequalities.
    \item \textbf{Expand Functions via Taylor and Maclaurin Series}: Construct polynomial approximations with remainder terms (Lagrange and Cauchy forms) and estimate approximation errors.
    \item \textbf{Resolve Indeterminate Forms}: Systematically apply L'H\^opital's Rule to indeterminate limits ($\frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty, \infty - \infty, 0^0, 1^\infty, \infty^0$).
    \item \textbf{Optimize Single-Variable Systems}: Identify critical points, apply the First and Second Derivative Tests, and solve real-world engineering optimization problems.
\end{enumerate}
\end{important}

% ==============================================================================
% SECTION 2.2: HIGHER-ORDER DIFFERENTIATION & LEIBNIZ RULE
% ==============================================================================
\section{Successive Differentiation \& Leibniz's Rule}

\subsection{Standard $n$-th Derivatives}
\begin{enumerate}[leftmargin=1.5em]
    \item $y = e^{ax} \implies y_n = a^n e^{ax}$
    \item $y = (ax+b)^m \implies y_n = m(m-1)\cdots(m-n+1) a^n (ax+b)^{m-n} = \frac{m!}{(m-n)!} a^n (ax+b)^{m-n}$
    \item $y = \frac{1}{ax+b} = (ax+b)^{-1} \implies y_n = \frac{(-1)^n n! a^n}{(ax+b)^{n+1}}$
    \item $y = \ln(ax+b) \implies y_n = \frac{(-1)^{n-1} (n-1)! a^n}{(ax+b)^n}$
    \item $y = \sin(ax+b) \implies y_n = a^n \sin\left(ax+b + \frac{n\pi}{2}\right)$
    \item $y = \cos(ax+b) \implies y_n = a^n \cos\left(ax+b + \frac{n\pi}{2}\right)$
    \item $y = e^{ax} \sin(bx+c) \implies y_n = (a^2+b^2)^{n/2} e^{ax} \sin\left(bx+c + n\tan^{-1}\frac{b}{a}\right)$
    \item $y = e^{ax} \cos(bx+c) \implies y_n = (a^2+b^2)^{n/2} e^{ax} \cos\left(bx+c + n\tan^{-1}\frac{b}{a}\right)$
\end{enumerate}

\begin{theorem}[Leibniz's Theorem for $n$-th Derivative of a Product]
If $u(x)$ and $v(x)$ are $n$-times differentiable functions, then:
\begin{equation}
(uv)_n = \sum_{k=0}^n \binom{n}{k} u_{n-k} v_k = u_n v + \binom{n}{1} u_{n-1} v_1 + \binom{n}{2} u_{n-2} v_2 + \cdots + u v_n
\end{equation}
\end{theorem}

\begin{example}[Successive Differentiation via Leibniz]
If $y = (x^2 - 1)^n$, prove that $(x^2 - 1)y_{n+2} + 2x y_{n+1} - n(n+1)y_n = 0$.
\end{example}

\begin{solutionbox}
Given $y = (x^2 - 1)^n$. Differentiating once with respect to $x$:
\begin{equation}
y_1 = n(x^2 - 1)^{n-1}(2x)
\end{equation}
Multiply both sides by $(x^2 - 1)$:
\begin{equation}
(x^2 - 1)y_1 = 2n x (x^2 - 1)^n = 2n x y
\end{equation}
Differentiating this equation $(n+1)$ times using Leibniz's Theorem:
\begin{align}
\frac{d^{n+1}}{dx^{n+1}}[(x^2 - 1)y_1] &= y_{n+2}(x^2 - 1) + \binom{n+1}{1}y_{n+1}(2x) + \binom{n+1}{2}y_n(2) \\
&= (x^2 - 1)y_{n+2} + 2(n+1)x y_{n+1} + n(n+1)y_n
\end{align}
And the right-hand side is:
\begin{align}
\frac{d^{n+1}}{dx^{n+1}}[2n x y] &= 2n \left[ y_{n+1} x + \binom{n+1}{1}y_n(1) \right] = 2n x y_{n+1} + 2n(n+1)y_n
\end{align}
Equating left and right sides:
\begin{align}
(x^2 - 1)y_{n+2} + 2(n+1)x y_{n+1} + n(n+1)y_n &= 2n x y_{n+1} + 2n(n+1)y_n \\
(x^2 - 1)y_{n+2} + 2x y_{n+1} - n(n+1)y_n &= 0
\end{align}
This completes the proof.
\end{solutionbox}

% ==============================================================================
% SECTION 2.3: MEAN VALUE THEOREMS
% ==============================================================================
\section{Mean Value Theorems (Rolle, Lagrange, Cauchy)}

\begin{theorem}[Rolle's Theorem]
Let $f:[a,b] \to \mathbb{R}$ be:
\begin{enumerate}[leftmargin=1.5em]
    \item Continuous on the closed interval $[a,b]$.
    \item Differentiable on the open interval $(a,b)$.
    \item $f(a) = f(b)$.
\end{enumerate}
Then there exists at least one point $c \in (a,b)$ such that $f'(c) = 0$.
\end{theorem}

\begin{theorem}[Lagrange's Mean Value Theorem (LMVT)]
Let $f:[a,b] \to \mathbb{R}$ be continuous on $[a,b]$ and differentiable on $(a,b)$. Then there exists at least one $c \in (a,b)$ such that:
\begin{equation}
f'(c) = \frac{f(b) - f(a)}{b - a}
\end{equation}
\end{theorem}

\begin{theorem}[Cauchy's Mean Value Theorem (CMVT)]
Let $f, g:[a,b] \to \mathbb{R}$ be continuous on $[a,b]$ and differentiable on $(a,b)$, with $g'(x) \ne 0$ on $(a,b)$. Then there exists at least one $c \in (a,b)$ such that:
\begin{equation}
\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}
\end{equation}
\end{theorem}

% ==============================================================================
% SECTION 2.4: TAYLOR & MACLAURIN EXPANSIONS
% ==============================================================================
\section{Taylor's and Maclaurin's Theorems with Remainders}

\begin{theorem}[Taylor's Theorem with Lagrange's Remainder]
If $f(x)$ and its first $n$ derivatives are continuous on $[a, a+h]$ and $f^{(n+1)}(x)$ exists on $(a, a+h)$, then:
\begin{equation}
f(a+h) = f(a) + h f'(a) + \frac{h^2}{2!} f''(a) + \cdots + \frac{h^n}{n!} f^{(n)}(a) + R_n
\end{equation}
where Lagrange's remainder is:
\begin{equation}
R_n = \frac{h^{n+1}}{(n+1)!} f^{(n+1)}(a + \theta h), \quad 0 < \theta < 1
\end{equation}
\end{theorem}

\subsection{Standard Maclaurin Series ($a = 0$)}
\begin{itemize}[leftmargin=1.5em]
    \item $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{n=0}^\infty \frac{x^n}{n!}, \quad \forall x \in \mathbb{R}$
    \item $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \quad \forall x \in \mathbb{R}$
    \item $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}, \quad \forall x \in \mathbb{R}$
    \item $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots, \quad -1 < x \le 1$
\end{itemize}

% ==============================================================================
% SECTION 2.5: INDETERMINATE FORMS & L'HOPITAL'S RULE
% ==============================================================================
\section{Indeterminate Forms and L'H\^opital's Rule}

\begin{theorem}[L'H\^opital's Rule for $\frac{0}{0}$ and $\frac{\infty}{\infty}$]
If $\lim_{x\to a} \frac{f(x)}{g(x)}$ is of the form $\left[\frac{0}{0}\right]$ or $\left[\frac{\pm\infty}{\pm\infty}\right]$, and $g'(x) \ne 0$ near $a$, then:
\begin{equation}
\lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f'(x)}{g'(x)}
\end{equation}
provided the latter limit exists or is $\pm\infty$.
\end{theorem}

\subsection{Transformations for Other Indeterminate Forms}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Product Form $[0 \cdot \infty]$}: Write $f(x) g(x) = \frac{f(x)}{1/g(x)}$ to obtain $\left[\frac{0}{0}\right]$ or $\left[\frac{\infty}{\infty}\right]$.
    \item \textbf{Difference Form $[\infty - \infty]$}: Combine into a common fraction: $\frac{1}{f} - \frac{1}{g} = \frac{g - f}{fg}$.
    \item \textbf{Exponential Forms $[0^0, 1^\infty, \infty^0]$}: Take the natural logarithm $y = [f(x)]^{g(x)} \implies \ln y = g(x) \ln f(x)$, find $L = \lim \ln y$, then $\lim y = e^L$.
\end{itemize}

\begin{example}[Evaluation of $1^\infty$ Form]
Evaluate $\lim_{x\to 0} (\cos x)^{1/x^2}$.
\end{example}

\begin{solutionbox}
This is an indeterminate form of type $[1^\infty]$.
Let $y = (\cos x)^{1/x^2}$. Taking natural logarithm:
\begin{equation}
\ln y = \frac{\ln(\cos x)}{x^2}
\end{equation}
As $x \to 0$, this is of form $\left[\frac{0}{0}\right]$. Applying L'H\^opital's rule:
\begin{equation}
\lim_{x\to 0} \frac{\frac{-\sin x}{\cos x}}{2x} = \lim_{x\to 0} \frac{-\tan x}{2x} = -\frac{1}{2} \lim_{x\to 0} \frac{\tan x}{x} = -\frac{1}{2}(1) = -\frac{1}{2}
\end{equation}
Therefore, $\lim_{x\to 0} y = e^{-1/2} = \frac{1}{\sqrt{e}}$.
\end{solutionbox}

% ==============================================================================
% SECTION 2.6: SINGLE-VARIABLE OPTIMIZATION
% ==============================================================================
\section{Single-Variable Optimization}

\begin{definition}[Critical Points \& Extrema Tests]
A point $x = c$ is a \textbf{critical point} if $f'(c) = 0$ or $f'(c)$ is undefined.
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Second Derivative Test}: If $f'(c) = 0$:
    \begin{itemize}
        \item $f''(c) < 0 \implies x = c$ is a \textbf{Local Maximum}.
        \item $f''(c) > 0 \implies x = c$ is a \textbf{Local Minimum}.
        \item $f''(c) = 0 \implies$ Test is inconclusive (use First Derivative Test).
    \end{itemize}
\end{itemize}
\end{definition}

""")

print("Chapter 2 written successfully.")

# Chapter 3: Fundamentals of Integral Calculus
with open("MTH165/chapters/chapter-03-integral-calculus.tex", "w") as f:
    f.write(r"""\chapter{Fundamentals of Integral Calculus}
\label{chap:integral-calculus}

% ==============================================================================
% SECTION 3.1: OVERVIEW & LEARNING OBJECTIVES
% ==============================================================================
\section{Unit Overview \& Learning Objectives}

Integral calculus represents the mathematical foundation for total accumulation, distributed loads, work done, geometric areas, volumes of revolution, and probability densities. In this chapter, we develop essential analytical integration techniques and the fundamental properties of definite integrals.

\begin{important}[Core Learning Objectives]
After mastering this unit, the student will be able to:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Execute Standard Antiderivatives}: Apply linearity and master standard algebraic, trigonometric, exponential, and hyperbolic antiderivative forms.
    \item \textbf{Perform Integration by Substitution}: Reverse the chain rule efficiently and transform limits of integration correctly.
    \item \textbf{Apply Integration by Parts}: Utilize the ILATE rule convention and establish recursive reduction formulas.
    \item \textbf{Decompose Rational Integrals}: Integrate using partial fractions for distinct linear, repeated linear, and irreducible quadratic factors.
    \item \textbf{Exploit Definite Integral Properties}: Apply interval splitting, reflection (King's property), and even/odd symmetry to evaluate complex definite integrals in closed form.
\end{enumerate}
\end{important}

% ==============================================================================
% SECTION 3.2: INTEGRATION TECHNIQUES
% ==============================================================================
\section{Advanced Methods of Integration}

\subsection{Integration by Substitution}
If $u = g(x)$, then $du = g'(x)\,dx$, yielding:
\begin{equation}
\int f(g(x)) g'(x)\,dx = \int f(u)\,du
\end{equation}
For definite integrals:
\begin{equation}
\int_a^b f(g(x)) g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du
\end{equation}

\subsection{Integration by Parts (ILATE Convention)}
\begin{equation}
\int u\,v\,dx = u \int v\,dx - \int \left( \frac{du}{dx} \int v\,dx \right) dx
\end{equation}
The priority for choosing $u$ is given by \textbf{ILATE}:
\begin{enumerate}
    \item \textbf{I}: Inverse Trigonometric functions ($\sin^{-1}x, \tan^{-1}x$)
    \item \textbf{L}: Logarithmic functions ($\ln x, \log_a x$)
    \item \textbf{A}: Algebraic polynomials ($x^n, x^2+1$)
    \item \textbf{T}: Trigonometric functions ($\sin x, \cos x$)
    \item \textbf{E}: Exponential functions ($e^{ax}, a^x$)
\end{enumerate}

\subsection{Partial Fractions Decomposition}
For proper rational functions $P(x)/Q(x)$:
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Distinct Linear Factor} $(ax+b)$: $\frac{A}{ax+b}$
    \item \textbf{Repeated Linear Factor} $(ax+b)^k$: $\frac{A_1}{ax+b} + \frac{A_2}{(ax+b)^2} + \cdots + \frac{A_k}{(ax+b)^k}$
    \item \textbf{Irreducible Quadratic Factor} $(ax^2+bx+c)$: $\frac{Ax+B}{ax^2+bx+c}$
\end{itemize}

% ==============================================================================
% SECTION 3.3: DEFINITE INTEGRALS & SPECIAL PROPERTIES
% ==============================================================================
\section{Definite Integrals \& Symmetry Properties}

\begin{theorem}[Master Properties of Definite Integrals]
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Dummy Variable Invariance}: $\int_a^b f(x)\,dx = \int_a^b f(t)\,dt$
    \item \textbf{Order Inversion}: $\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$
    \item \textbf{Interval Splitting}: $\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$
    \item \textbf{King's Reflection Property}:
    \begin{equation}
    \int_a^b f(x)\,dx = \int_a^b f(a + b - x)\,dx
    \end{equation}
    Special case ($a = 0$): $\int_0^a f(x)\,dx = \int_0^a f(a - x)\,dx$.
    \item \textbf{Symmetric Interval for Even/Odd Functions}:
    \begin{equation}
    \int_{-a}^a f(x)\,dx = \begin{cases}
    2 \int_0^a f(x)\,dx, & \text{if } f(-x) = f(x) \text{ (Even)} \\
    0, & \text{if } f(-x) = -f(x) \text{ (Odd)}
    \end{cases}
    \end{equation}
    \item \textbf{Periodic Function Property}: If $f(x+T) = f(x)$, then $\int_0^{nT} f(x)\,dx = n \int_0^T f(x)\,dx$.
\end{enumerate}
\end{theorem}

\begin{example}[Evaluation via King's Property]
Evaluate $I = \int_0^{\pi/2} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}}\,dx$.
\end{example}

\begin{solutionbox}
Let:
\begin{equation}
I = \int_0^{\pi/2} \frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}}\,dx \quad \text{--- (1)}
\end{equation}
Apply King's property $\int_0^a f(x)\,dx = \int_0^a f(a - x)\,dx$ with $a = \pi/2$:
\begin{equation}
I = \int_0^{\pi/2} \frac{\sqrt{\sin(\pi/2 - x)}}{\sqrt{\sin(\pi/2 - x)} + \sqrt{\cos(\pi/2 - x)}}\,dx = \int_0^{\pi/2} \frac{\sqrt{\cos x}}{\sqrt{\cos x} + \sqrt{\sin x}}\,dx \quad \text{--- (2)}
\end{equation}
Adding equations (1) and (2):
\begin{equation}
2I = \int_0^{\pi/2} \frac{\sqrt{\sin x} + \sqrt{\cos x}}{\sqrt{\sin x} + \sqrt{\cos x}}\,dx = \int_0^{\pi/2} 1\,dx = \frac{\pi}{2}
\end{equation}
Therefore, $I = \frac{\pi}{4}$.
\end{solutionbox}

""")

print("Chapter 3 written successfully.")

# Chapter 4: Multivariate Differentiation
with open("MTH165/chapters/chapter-04-multivariate-differentiation.tex", "w") as f:
    f.write(r"""\chapter{Multivariate Differentiation}
\label{chap:multivariate-differentiation}

% ==============================================================================
% SECTION 4.1: OVERVIEW & LEARNING OBJECTIVES
% ==============================================================================
\section{Unit Overview \& Learning Objectives}

Multivariate differential calculus extends rate-of-change and optimization principles to functions of several independent variables $z = f(x,y)$ or $w = f(x,y,z)$. In engineering applications, physical quantities (such as thermodynamic state variables, stress distributions, electrodynamic potentials, and machine learning cost landscapes) depend on multiple spatial and temporal coordinates simultaneously.

\begin{important}[Core Learning Objectives]
After mastering this unit, the student will be able to:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Evaluate Multivariable Limits \& Continuity}: Test limits using the two-path test and polar coordinates ($x = r\cos\theta, y = r\sin\theta$).
    \item \textbf{Compute Partial Derivatives}: Calculate first-order and higher-order partial derivatives and apply Clairaut's Theorem ($f_{xy} = f_{yx}$).
    \item \textbf{Calculate Total Differentials}: Formulate $dz = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$, perform linear approximations, and quantify error propagation.
    \item \textbf{Apply Chain Rules}: Differentiate composite functions dependent on single or multiple parameters.
    \item \textbf{Apply Euler's Theorem on Homogeneous Functions}: Verify degree $n$ homogeneity and apply 1st and 2nd order Euler identities.
    \item \textbf{Perform 2D Optimization}: Find critical points, evaluate the Hessian discriminant $D = f_{xx}f_{yy} - f_{xy}^2$, and classify local minima, local maxima, and saddle points.
    \item \textbf{Solve Constrained Optimization}: Implement the method of \textbf{Lagrange Multipliers} ($\nabla f = \lambda \nabla g$).
\end{enumerate}
\end{important}

% ==============================================================================
% SECTION 4.2: LIMITS, CONTINUITY & PARTIAL DERIVATIVES
% ==============================================================================
\section{Limits, Continuity \& Partial Derivatives}

\begin{definition}[Limit in Two Variables]
We write $\lim_{(x,y)\to (x_0,y_0)} f(x,y) = L$ if for every $\epsilon > 0$, there exists a $\delta > 0$ such that $0 < \sqrt{(x-x_0)^2 + (y-y_0)^2} < \delta \implies |f(x,y) - L| < \epsilon$.
\end{definition}

\begin{theorem}[Two-Path Test for Non-Existence of Limit]
If $f(x,y)$ approaches different values along two distinct paths approaching $(x_0,y_0)$ (e.g., $y = mx$ vs $y = kx^2$), then $\lim_{(x,y)\to (x_0,y_0)} f(x,y)$ does not exist.
\end{theorem}

\begin{theorem}[Clairaut's Theorem / Schwarz's Theorem]
If $f(x,y)$ and its partial derivatives $f_x, f_y, f_{xy}, f_{yx}$ are continuous on an open region containing $(x_0,y_0)$, then the mixed second-order partial derivatives are identical:
\begin{equation}
\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} \quad (f_{yx} = f_{xy})
\end{equation}
\end{theorem}

% ==============================================================================
% SECTION 4.3: TOTAL DIFFERENTIAL & ERROR PROPAGATION
% ==============================================================================
\section{Total Differentials \& Error Propagation}

\begin{definition}[Total Differential]
For a differentiable function $z = f(x,y)$, the \textbf{total differential} $dz$ is:
\begin{equation}
dz = \frac{\partial z}{\partial x} dx + \frac{\partial z}{\partial y} dy
\end{equation}
For small increments $\Delta x$ and $\Delta y$, the estimated absolute change is:
\begin{equation}
\Delta z \approx \frac{\partial z}{\partial x} \Delta x + \frac{\partial z}{\partial y} \Delta y
\end{equation}
The percentage / relative error is given by:
\begin{equation}
\frac{\Delta z}{z} \times 100\% = \left( \frac{1}{z} \frac{\partial z}{\partial x} \Delta x + \frac{1}{z} \frac{\partial z}{\partial y} \Delta y \right) \times 100\%
\end{equation}
\end{definition}

% ==============================================================================
% SECTION 4.4: EULER'S THEOREM FOR HOMOGENEOUS FUNCTIONS
% ==============================================================================
\section{Euler's Theorem on Homogeneous Functions}

\begin{definition}[Homogeneous Function]
A function $f(x,y)$ is said to be \textbf{homogeneous of degree $n$} if:
\begin{equation}
f(tx, ty) = t^n f(x,y) \quad \text{for all } t > 0
\end{equation}
\end{definition}

\begin{theorem}[Euler's Theorem for Homogeneous Functions]
If $u = f(x,y)$ is a homogeneous function of degree $n$ having continuous partial derivatives, then:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{First-Order Form}:
    \begin{equation}
    x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = n u
    \end{equation}
    \item \textbf{Second-Order Form}:
    \begin{equation}
    x^2 \frac{\partial^2 u}{\partial x^2} + 2xy \frac{\partial^2 u}{\partial x \partial y} + y^2 \frac{\partial^2 u}{\partial y^2} = n(n-1)u
    \end{equation}
\end{enumerate}
\end{theorem}

\begin{example}[Euler's Theorem Application]
If $u = \sin^{-1}\left(\frac{x^2 + y^2}{x + y}\right)$, prove that $x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \tan u$.
\end{example}

\begin{solutionbox}
Let $z = \sin u = \frac{x^2 + y^2}{x + y}$.
Testing homogeneity:
\begin{equation}
z(tx, ty) = \frac{(tx)^2 + (ty)^2}{tx + ty} = \frac{t^2(x^2 + y^2)}{t(x+y)} = t^1 \frac{x^2+y^2}{x+y} = t^1 z(x,y)
\end{equation}
Thus, $z$ is a homogeneous function of degree $n = 1$.
By Euler's Theorem on $z$:
\begin{equation}
x \frac{\partial z}{\partial x} + y \frac{\partial z}{\partial y} = 1 \cdot z = z
\end{equation}
Since $z = \sin u$, we have $\frac{\partial z}{\partial x} = \cos u \frac{\partial u}{\partial x}$ and $\frac{\partial z}{\partial y} = \cos u \frac{\partial u}{\partial y}$.
Substituting:
\begin{equation}
x \left(\cos u \frac{\partial u}{\partial x}\right) + y \left(\cos u \frac{\partial u}{\partial y}\right) = \sin u
\end{equation}
Dividing throughout by $\cos u$:
\begin{equation}
x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \frac{\sin u}{\cos u} = \tan u
\end{equation}
\end{solutionbox}

% ==============================================================================
% SECTION 4.5: UNCONSTRAINED & CONSTRAINED OPTIMIZATION
% ==============================================================================
\section{Multivariable Extrema \& Lagrange Multipliers}

\begin{theorem}[Second Partial Derivative Test (Hessian Discriminant)]
Let $(a,b)$ be a critical point of $f(x,y)$ such that $f_x(a,b) = 0$ and $f_y(a,b) = 0$.
Define $r = f_{xx}(a,b)$, $s = f_{xy}(a,b)$, $t = f_{yy}(a,b)$, and the discriminant:
\begin{equation}
D = r t - s^2 = f_{xx} f_{yy} - (f_{xy})^2
\end{equation}
\begin{enumerate}[leftmargin=1.5em]
    \item If $D > 0$ and $r > 0$ (or $t > 0$), then $(a,b)$ is a \textbf{Local Minimum}.
    \item If $D > 0$ and $r < 0$ (or $t < 0$), then $(a,b)$ is a \textbf{Local Maximum}.
    \item If $D < 0$, then $(a,b)$ is a \textbf{Saddle Point}.
    \item If $D = 0$, the test is \textbf{Inconclusive}.
\end{enumerate}
\end{theorem}

\begin{theorem}[Method of Lagrange Multipliers]
To find the extreme values of $f(x,y,z)$ subject to the constraint $g(x,y,z) = c$ (where $\nabla g \ne 0$):
Solve the system of equations:
\begin{equation}
\nabla f = \lambda \nabla g \iff \begin{cases}
f_x = \lambda g_x \\
f_y = \lambda g_y \\
f_z = \lambda g_z \\
g(x,y,z) = c
\end{cases}
\end{equation}
where $\lambda$ is the \textbf{Lagrange multiplier}.
\end{theorem}

""")

print("Chapter 4 written successfully.")

# Chapter 5: Multivariable Integration and Applications
with open("MTH165/chapters/chapter-05-multivariable-integration.tex", "w") as f:
    f.write(r"""\chapter{Multivariable Integration and Applications}
\label{chap:multivariable-integration}

% ==============================================================================
% SECTION 5.1: OVERVIEW & LEARNING OBJECTIVES
% ==============================================================================
\section{Unit Overview \& Learning Objectives}

Multiple integrals extend the concepts of single-variable integration to calculate multi-dimensional geometric quantities and physical properties. In mechanical, civil, and electrical engineering, double and triple integrals provide the exact analytical tools to evaluate planar areas, spatial volumes, centers of mass, moments of inertia, and total charge / flux distributions over complex domains.

\begin{important}[Core Learning Objectives]
After mastering this unit, the student will be able to:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Evaluate Double Integrals}: Compute iterated double integrals over Cartesian rectangular and general non-rectangular Type I / Type II domains.
    \item \textbf{Execute Change of Order of Integration}: Sketch integration regions, reverse the order of integration ($dx\,dy \leftrightarrow dy\,dx$), and evaluate otherwise intractable integrals.
    \item \textbf{Apply Jacobians and Coordinate Transformations}: Transform Cartesian double and triple integrals into Polar, Cylindrical, and Spherical coordinate systems using Jacobian scaling factors.
    \item \textbf{Evaluate Triple Integrals}: Compute volume integrals over bounding surfaces such as planes, paraboloids, cylinders, cones, and spheres.
    \item \textbf{Calculate Geometric Area and Volume}: Determine planar areas $A = \iint_R 1\,dA$ and 3D solid volumes $V = \iiint_V 1\,dV$.
\end{enumerate}
\end{important}

% ==============================================================================
% SECTION 5.2: DOUBLE INTEGRALS & CHANGE OF ORDER
% ==============================================================================
\section{Double Integrals \& Change of Order}

\begin{definition}[Double Integral over Planar Region]
For a continuous function $f(x,y)$ over a bounded region $R \subset \mathbb{R}^2$, the double integral is defined via Fubini's Theorem:
\begin{equation}
\iint_R f(x,y)\,dA = \int_{a}^b \int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx = \int_{c}^d \int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy
\end{equation}
\end{definition}

\begin{methodbox}[Algorithm for Changing the Order of Integration]
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Extract Domain Inequalities}: Read the given outer and inner limits: e.g., $x \in [a,b]$ and $y \in [g_1(x), g_2(x)]$.
    \item \textbf{Sketch the Exact Region $R$}: Plot the boundary curves $y = g_1(x)$, $y = g_2(x)$, $x = a$, and $x = b$.
    \item \textbf{Re-slice the Domain Horizontally}:
    \begin{itemize}
        \item Find the global $y$-range: $y \in [c, d]$.
        \item Determine the left boundary $x = h_1(y)$ and right boundary $x = h_2(y)$.
    \end{itemize}
    \item \textbf{Formulate and Evaluate the New Integral}:
    \begin{equation}
    \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx \longrightarrow \int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy
    \end{equation}
\end{enumerate}
\end{methodbox}

\begin{example}[Change of Order of Integration]
Evaluate by changing the order of integration:
\begin{equation}
I = \int_0^1 \int_y^1 e^{x^2}\,dx\,dy
\end{equation}
\end{example}

\begin{solutionbox}
1. \textbf{Identify Original Region $R$}:
The limits of integration are $y \le x \le 1$ with $0 \le y \le 1$.
The bounding lines are $x = y$, $x = 1$, and $y = 0$.

2. \textbf{Change Order of Integration (Vertical Slices)}:
In the new order, $x$ varies globally from $0$ to $1$: $x \in [0, 1]$.
For a fixed $x$, $y$ varies from the $x$-axis ($y = 0$) up to the line $y = x$: $y \in [0, x]$.

3. \textbf{Transformed Integral}:
\begin{align}
I &= \int_0^1 \left( \int_0^x e^{x^2}\,dy \right) dx = \int_0^1 e^{x^2} \Big[ y \Big]_0^x \, dx = \int_0^1 x e^{x^2}\,dx
\end{align}
Substitute $u = x^2 \implies du = 2x\,dx$:
\begin{equation}
I = \frac{1}{2} \int_0^1 e^u\,du = \frac{1}{2} \Big[ e^u \Big]_0^1 = \frac{e - 1}{2}
\end{equation}
\end{solutionbox}

% ==============================================================================
% SECTION 5.3: COORDINATE TRANSFORMATIONS & JACOBIANS
% ==============================================================================
\section{Jacobian Transformations \& Polar / Cylindrical / Spherical Systems}

\begin{definition}[Jacobian Transformation Matrix]
For a 2D transformation $x = x(u,v), y = y(u,v)$:
\begin{equation}
J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{vmatrix}, \quad dA = dx\,dy = |J|\,du\,dv
\end{equation}
For a 3D transformation $x = x(u,v,w), y = y(u,v,w), z = z(u,v,w)$:
\begin{equation}
J = \frac{\partial(x,y,z)}{\partial(u,v,w)} = \begin{vmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\
\frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
\end{vmatrix}, \quad dV = dx\,dy\,dz = |J|\,du\,dv\,dw
\end{equation}
\end{definition}

\subsection{Standard Engineering Coordinate Systems}
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Polar Coordinates (2D)}:
    \begin{equation}
    x = r\cos\theta, \quad y = r\sin\theta \implies J = r \implies dA = r\,dr\,d\theta
    \end{equation}
    \item \textbf{Cylindrical Coordinates (3D)}:
    \begin{equation}
    x = r\cos\theta, \quad y = r\sin\theta, \quad z = z \implies J = r \implies dV = r\,dr\,d\theta\,dz
    \end{equation}
    \item \textbf{Spherical Polar Coordinates (3D)}:
    \begin{equation}
    x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi
    \end{equation}
    \begin{equation}
    J = \rho^2 \sin\phi \implies dV = \rho^2 \sin\phi\,d\rho\,d\phi\,d\theta
    \end{equation}
    where $\rho \in [0, \infty)$, $\phi \in [0, \pi]$ (polar angle from $+z$), $\theta \in [0, 2\pi]$ (azimuthal angle).
\end{enumerate}

% ==============================================================================
% SECTION 5.4: TRIPLE INTEGRALS & SOLID VOLUMES
% ==============================================================================
\section{Triple Integrals \& Solid Volumes}

\begin{definition}[Volume via Triple Integration]
The solid volume $V$ of a closed 3D bounded domain $\Omega$ is:
\begin{equation}
V = \iiint_\Omega 1\,dV
\end{equation}
\end{definition}

\begin{example}[Volume of Sphere via Spherical Coordinates]
Calculate the volume of a sphere of radius $R$ defined by $x^2 + y^2 + z^2 \le R^2$.
\end{example}

\begin{solutionbox}
Transform to spherical coordinates:
$\rho \in [0, R]$, $\phi \in [0, \pi]$, $\theta \in [0, 2\pi]$.
\begin{align}
V &= \int_0^{2\pi} \int_0^\pi \int_0^R \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta \\
&= \left( \int_0^{2\pi} d\theta \right) \left( \int_0^\pi \sin\phi \, d\phi \right) \left( \int_0^R \rho^2 \, d\rho \right) \\
&= (2\pi) \Big[ -\cos\phi \Big]_0^\pi \left[ \frac{\rho^3}{3} \right]_0^R = (2\pi)(1 - (-1))\left( \frac{R^3}{3} \right) = \frac{4}{3}\pi R^3
\end{align}
\end{solutionbox}

""")

print("Chapter 5 written successfully.")

# Chapter 6: Introduction to Fourier Series
with open("MTH165/chapters/chapter-06-fourier-series.tex", "w") as f:
    f.write(r"""\chapter{Introduction to Fourier Series}
\label{chap:fourier-series}

% ==============================================================================
% SECTION 6.1: OVERVIEW & LEARNING OBJECTIVES
% ==============================================================================
\section{Unit Overview \& Learning Objectives}

Fourier series is one of the most transformative mathematical tools in modern engineering, enabling arbitrary periodic piecewise continuous waveforms to be decomposed into infinite sums of fundamental and harmonic sinusoids. In electrical signal processing, telecommunications, acoustics, mechanical vibration analysis, and heat diffusion PDEs, Fourier analysis converts complex time-domain signals into transparent frequency-domain spectra.

\begin{important}[Core Learning Objectives]
After mastering this unit, the student will be able to:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Analyze Periodic Functions}: Determine fundamental period $T$ and angular frequency $\omega_0 = \frac{2\pi}{T}$.
    \item \textbf{Evaluate Euler Coefficients}: Compute the Fourier coefficients $a_0, a_n, b_n$ over intervals of length $2\pi$ ($(-\pi, \pi)$) and general length $2L$ ($(-L, L)$).
    \item \textbf{Apply Dirichlet's Conditions}: Verify convergence criteria and calculate the sum of the Fourier series at continuous points and jump discontinuities ($\frac{f(x_0^+) + f(x_0^-)}{2}$).
    \item \textbf{Exploit Symmetry}: Expand even functions into Fourier Cosine Series ($b_n = 0$) and odd functions into Fourier Sine Series ($a_0 = a_n = 0$).
    \item \textbf{Construct Half-Range Series}: Derive Half-Range Cosine and Sine Expansions over $(0, L)$.
    \item \textbf{Apply Parseval's Theorem}: Calculate total harmonic power / energy and sum infinite numeric series.
\end{enumerate}
\end{important}

% ==============================================================================
% SECTION 6.2: TRIGONOMETRIC FOURIER SERIES & EULER FORMULAE
% ==============================================================================
\section{Trigonometric Fourier Series \& Euler's Formulae}

\begin{definition}[Fourier Series Representation on $(-\pi, \pi)$]
A periodic function $f(x)$ with period $T = 2\pi$ satisfying Dirichlet's conditions can be represented as:
\begin{equation}
f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[ a_n \cos(nx) + b_n \sin(nx) \right]
\end{equation}
where the \textbf{Euler coefficients} are given by:
\begin{align}
a_0 &= \frac{1}{\pi} \int_{-\pi}^\pi f(x)\,dx \\
a_n &= \frac{1}{\pi} \int_{-\pi}^\pi f(x)\cos(nx)\,dx, \quad n = 1, 2, 3, \dots \\
b_n &= \frac{1}{\pi} \int_{-\pi}^\pi f(x)\sin(nx)\,dx, \quad n = 1, 2, 3, \dots
\end{align}
\end{definition}

\begin{definition}[Fourier Series on Arbitrary Interval $(-L, L)$]
For a periodic function with period $T = 2L$:
\begin{equation}
f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[ a_n \cos\left(\frac{n\pi x}{L}\right) + b_n \sin\left(\frac{n\pi x}{L}\right) \right]
\end{equation}
with Euler coefficients:
\begin{align}
a_0 &= \frac{1}{L} \int_{-L}^L f(x)\,dx \\
a_n &= \frac{1}{L} \int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\,dx \\
b_n &= \frac{1}{L} \int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx
\end{align}
\end{definition}

% ==============================================================================
% SECTION 6.3: DIRICHLET CONDITIONS & CONVERGENCE
% ==============================================================================
\section{Dirichlet's Conditions \& Pointwise Convergence}

\begin{theorem}[Dirichlet's Conditions for Convergence]
A periodic function $f(x)$ of period $2L$ can be expanded in a convergent Fourier series if on $[-L, L]$:
\begin{enumerate}[leftmargin=1.5em]
    \item $f(x)$ is single-valued and bounded (has at most finite absolute values).
    \item $f(x)$ is piecewise continuous with at most a finite number of jump discontinuities.
    \item $f(x)$ has at most a finite number of local maxima and minima.
\end{enumerate}
\end{theorem}

\begin{theorem}[Value of Fourier Series at Discontinuities]
Let $S(x)$ denote the Fourier series of $f(x)$:
\begin{enumerate}[leftmargin=1.5em]
    \item If $x = x_0$ is a point of \textbf{continuity}, then $S(x_0) = f(x_0)$.
    \item If $x = x_0$ is a point of \textbf{jump discontinuity}, then:
    \begin{equation}
    S(x_0) = \frac{f(x_0^+) + f(x_0^-)}{2}
    \end{equation}
    where $f(x_0^+) = \lim_{h\to 0^+} f(x_0 + h)$ and $f(x_0^-) = \lim_{h\to 0^+} f(x_0 - h)$.
    \item At the interval endpoints $x = \pm L$, the series converges to the periodic boundary average:
    \begin{equation}
    S(\pm L) = \frac{f(-L^+) + f(L^-)}{2}
    \end{equation}
\end{enumerate}
\end{theorem}

% ==============================================================================
% SECTION 6.4: SYMMETRY & HALF-RANGE EXPANSIONS
% ==============================================================================
\section{Symmetry Simplifications \& Half-Range Expansions}

\subsection{Even and Odd Function Expansions}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Even Function} ($f(-x) = f(x)$ on $(-L, L)$):
    \begin{equation}
    b_n = 0, \quad a_0 = \frac{2}{L}\int_0^L f(x)\,dx, \quad a_n = \frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\,dx
    \end{equation}
    The series contains only cosine terms (\textbf{Fourier Cosine Series}).
    \item \textbf{Odd Function} ($f(-x) = -f(x)$ on $(-L, L)$):
    \begin{equation}
    a_0 = 0, \quad a_n = 0, \quad b_n = \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx
    \end{equation}
    The series contains only sine terms (\textbf{Fourier Sine Series}).
\end{itemize}

\subsection{Half-Range Expansions on $(0, L)$}
When $f(x)$ is defined only on the half-interval $(0, L)$:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Half-Range Cosine Series} (Even Extension):
    \begin{equation}
    f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty a_n \cos\left(\frac{n\pi x}{L}\right), \quad a_0 = \frac{2}{L}\int_0^L f(x)\,dx, \; a_n = \frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\,dx
    \end{equation}
    \item \textbf{Half-Range Sine Series} (Odd Extension):
    \begin{equation}
    f(x) = \sum_{n=1}^\infty b_n \sin\left(\frac{n\pi x}{L}\right), \quad b_n = \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx
    \end{equation}
\end{enumerate}

% ==============================================================================
% SECTION 6.5: PARSEVAL'S IDENTITY
% ==============================================================================
\section{Parseval's Identity \& Harmonic Energy}

\begin{theorem}[Parseval's Identity for Fourier Series]
If $f(x)$ has Fourier coefficients $a_0, a_n, b_n$ on $(-L, L)$, then:
\begin{equation}
\frac{1}{L} \int_{-L}^L [f(x)]^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^\infty (a_n^2 + b_n^2)
\end{equation}
\end{theorem}

\begin{example}[Complete Fourier Series of a Square Wave]
Find the Fourier series for $f(x) = \begin{cases} -k, & -\pi < x < 0 \\ k, & 0 < x < \pi \end{cases}$ with period $2\pi$. Hence deduce $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots$.
\end{example}

\begin{solutionbox}
Since $f(-x) = -f(x)$, $f(x)$ is an \textbf{odd function}.
Therefore, $a_0 = 0$ and $a_n = 0$.
We evaluate $b_n$:
\begin{align}
b_n &= \frac{2}{\pi}\int_0^\pi k \sin(nx)\,dx = \frac{2k}{\pi} \left[ \frac{-\cos(nx)}{n} \right]_0^\pi = \frac{2k}{n\pi}(1 - (-1)^n) \\
&= \begin{cases}
\frac{4k}{n\pi}, & \text{for } n \text{ odd} \\
0, & \text{for } n \text{ even}
\end{cases}
\end{align}
Thus, the Fourier series is:
\begin{equation}
f(x) = \frac{4k}{\pi} \left( \sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \frac{\sin 7x}{7} + \cdots \right)
\end{equation}
At $x = \pi/2$, $f(\pi/2) = k$, $\sin(\pi/2) = 1$, $\sin(3\pi/2) = -1$, $\sin(5\pi/2) = 1$:
\begin{equation}
k = \frac{4k}{\pi} \left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots \right) \implies \frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots
\end{equation}
\end{solutionbox}

""")

# Chapter 7: Formula and Methods Sheet
with open("MTH165/chapters/chapter-07-formula-and-methods-sheet.tex", "w") as f:
    f.write(r"""\chapter{Master Formula and Methods Sheet}
\label{chap:formula-methods-sheet}

\section{Unit 1: Matrix Methods and Linear Systems}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Rank Definition}: $\rho(A) =$ Number of non-zero rows in REF $=$ Order of largest non-vanishing minor.
    \item \textbf{Rouch\'e--Capelli Theorem}:
    \begin{itemize}
        \item Inconsistent (No Solution): $\rho(A) < \rho([A|b])$
        \item Unique Solution: $\rho(A) = \rho([A|b]) = n$
        \item Infinitely Many Solutions: $\rho(A) = \rho([A|b]) = r < n$ ($n-r$ free variables)
    \end{itemize}
    \item \textbf{Eigenvalues \& Cayley--Hamilton}:
    \begin{itemize}
        \item Characteristic Eq: $|A - \lambda I| = 0 \implies \lambda^3 - S_1 \lambda^2 + S_2 \lambda - S_3 = 0$
        \item Cayley--Hamilton: $A^3 - S_1 A^2 + S_2 A - S_3 I = O$
        \item $\sum \lambda_i = \operatorname{tr}(A), \quad \prod \lambda_i = \det(A)$
    \end{itemize}
\end{itemize}

\section{Unit 2: Differential Calculus}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Leibniz Rule}: $(uv)_n = \sum_{k=0}^n \binom{n}{k} u_{n-k} v_k$
    \item \textbf{Mean Value Theorems}:
    \begin{itemize}
        \item Rolle's: $f'(c) = 0$ for $c \in (a,b)$ when $f(a)=f(b)$.
        \item LMVT: $f'(c) = \frac{f(b)-f(a)}{b-a}$
        \item CMVT: $\frac{f'(c)}{g'(c)} = \frac{f(b)-f(a)}{g(b)-g(a)}$
    \end{itemize}
    \item \textbf{Taylor's Theorem}: $f(a+h) = \sum_{k=0}^n \frac{h^k}{k!} f^{(k)}(a) + \frac{h^{n+1}}{(n+1)!} f^{(n+1)}(a+\theta h)$
\end{itemize}

\section{Unit 3: Integral Calculus}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Integration by Parts}: $\int u v'\,dx = uv - \int u' v\,dx$ (ILATE order)
    \item \textbf{King's Property}: $\int_a^b f(x)\,dx = \int_a^b f(a+b-x)\,dx$
    \item \textbf{Even/Odd Property}: $\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$ (even), $0$ (odd).
\end{itemize}

\section{Unit 4: Multivariate Differentiation}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Euler's Theorem}: $x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = n u$
    \item \textbf{Hessian Discriminant}: $D = f_{xx}f_{yy} - (f_{xy})^2$. If $D > 0, f_{xx} > 0 \implies$ Min; $D > 0, f_{xx} < 0 \implies$ Max; $D < 0 \implies$ Saddle point.
    \item \textbf{Lagrange Multipliers}: $\nabla f = \lambda \nabla g$.
\end{itemize}

\section{Unit 5: Multivariable Integration}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Polar}: $dA = r\,dr\,d\theta$
    \item \textbf{Cylindrical}: $dV = r\,dr\,d\theta\,dz$
    \item \textbf{Spherical}: $dV = \rho^2 \sin\phi\,d\rho\,d\phi\,d\theta$
\end{itemize}

\section{Unit 6: Fourier Series}
\begin{itemize}[leftmargin=1.5em]
    \item $f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty [a_n \cos(nx) + b_n \sin(nx)]$
    \item $a_0 = \frac{1}{\pi}\int_{-\pi}^\pi f(x)dx, \; a_n = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\cos(nx)dx, \; b_n = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\sin(nx)dx$
    \item Even: $b_n = 0$; Odd: $a_0 = a_n = 0$.
    \item Discontinuity Average: $S(x_0) = \frac{f(x_0^+) + f(x_0^-)}{2}$.
\end{itemize}
""")

print("All Textbook Chapters generated successfully.")
