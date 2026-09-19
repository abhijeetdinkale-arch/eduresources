# MTH165: Mathematics — Master Content Blueprint & Syllabus Specification
## Comprehensive Engineering Problem-Solving Study & Practice Guide (Semester 1)

**Course Code**: MTH165  
**Course Title**: Mathematics / Engineering Mathematics I (Calculus, Multivariable Analysis & Vector Calculus)  
**Target Class**: Lovely Professional University (LPU) Semester 1 Engineering Students  
**Document Nature**: Authoritative Master Architectural Specification & Pedagogical Blueprint  
**Philosophy**: Exhaustive Mathematical Rigor, Problem-Solving Mastery, Method Recognition Heuristics, Step-by-Step Worked Derivations, and Exam Domination.

---

## 1. Executive Course Overview & Structural Organization

The **MTH165: Mathematics** course constitutes the foundational analytical bedrock for all engineering disciplines. Unlike descriptive computing subjects, MTH165 is fundamentally a **calculation-heavy, theorem-driven, problem-solving discipline**. This master blueprint establishes a comprehensive, multi-part curriculum architecture designed to take students from foundational single-variable calculus to advanced multivariable analysis, coordinate transformations, and vector field theorems.

```text
MTH165: Engineering Mathematics
├── Part I   / Unit 1: Single-Variable Differential Calculus & Mean Value Theorems
├── Part II  / Unit 2: Single-Variable Integral Calculus, Special Functions & Applications
├── Part III / Unit 3: Infinite Sequences, Series & Convergence Tests
├── Part IV  / Unit 4: Multivariable Differential Calculus, Optimization & Jacobians
├── Part V   / Unit 5: Multiple Integrals (Double & Triple) & Coordinate Transformations
├── Part VI  / Unit 6: Vector Calculus & Field Integral Theorems (Green, Stokes, Gauss)
├── Part VII / Master Comprehensive Formula, Method & Identity Sheet
├── Part VIII/ Multi-Unit Mixed Problem Practice Suites
└── Part IX  / Full-Length University Mock Examination Papers (100 Marks Each)
```

---

## 2. Standardized Pedagogical Learning Progression

To eliminate student guesswork and instill algorithmic problem-solving instincts, every mathematical topic in the textbook must adhere to the following **10-Step Pedagogical Workflow**:

```
[1. CONCEPT NAME]
       │
       ▼
[2. FORMAL DEFINITION & STATEMENT]
       │
       ▼
[3. FORMULA / THEOREM EQUATION]
       │
       ▼
[4. GEOMETRICAL & INTUITIVE MEANING]
       │
       ▼
[5. METHOD RECOGNITION (When & Why to use this technique)]
       │
       ▼
[6. ALGORITHMIC STEP-BY-STEP PROCEDURE]
       │
       ▼
[7. WORKED EXAMPLE 1 (Standard / Foundational Problem)]
       │
       ▼
[8. WORKED EXAMPLE 2 (Advanced / Exam-Tier Harder Problem)]
       │
       ▼
[9. COMMON STUDENT MISTAKES & EXAM TRAPS]
       │
       ▼
[10. GRADED PRACTICE PROBLEMS & FULL STEP-BY-STEP SOLUTIONS]
```

---

## 3. Detailed Unit Blueprints & Content Specifications

---

### PART I / UNIT 1: Single-Variable Differential Calculus & Mean Value Theorems

#### 1. Unit Metadata & Topic Hierarchy
- **1.1 Unit Overview & Learning Objectives**
- **1.2 Limits, Continuity and Differentiability**:
  - 1.2.1 Intuitive and Formal $\epsilon$-$\delta$ Definitions of Limits
  - 1.2.2 Left-Hand Limit (LHL) and Right-Hand Limit (RHL) Criteria
  - 1.2.3 Continuity at a Point and on an Interval; Types of Discontinuities (Removable, Jump, Infinite, Essential)
  - 1.2.4 Differentiability at a Point; Relation between Continuity and Differentiability (Differentiability $\implies$ Continuity; converse is false: $f(x)=|x|$)
- **1.3 Successive Differentiation & Leibniz's Theorem**:
  - 1.3.1 Standard $n$-th Derivatives: $e^{ax}, (ax+b)^m, \frac{1}{ax+b}, \ln(ax+b), \sin(ax+b), \cos(ax+b), e^{ax}\sin(bx+c), e^{ax}\cos(bx+c)$
  - 1.3.2 Statement and Rigorous Proof of **Leibniz's Theorem for the $n$-th Derivative of a Product**:
    $$y_n = (uv)_n = \sum_{k=0}^n \binom{n}{k} u_{n-k} v_k$$
  - 1.3.3 Differential Equation Transformations using Leibniz Theorem (e.g., if $y = (x^2-1)^n$ or $y = \sin^{-1}x$, establish $(1-x^2)y_{n+2} - (2n+1)xy_{n+1} - n^2 y_n = 0$)
- **1.4 Mean Value Theorems**:
  - 1.4.1 **Rolle's Theorem**: Statement, Geometric Interpretation (horizontal tangent $f'(c)=0$), Algebraic Verification, and Finding $c \in (a,b)$
  - 1.4.2 **Lagrange's Mean Value Theorem (LMVT)**: Statement ($f'(c) = \frac{f(b)-f(a)}{b-a}$), Geometric Interpretation (secant slope = tangent slope), Analytical Applications, and Proving Inequalities
  - 1.4.3 **Cauchy's Mean Value Theorem (CMVT)**: Statement ($\frac{f'(c)}{g'(c)} = \frac{f(b)-f(a)}{g(b)-g(a)}$), Geometrical meaning, and Verification
- **1.5 Indeterminate Forms & L'Hôpital's Rule**:
  - 1.5.1 Primary Fractional Forms: $\left[\frac{0}{0}\right]$ and $\left[\frac{\infty}{\infty}\right]$; Conditions for applying L'Hôpital's Rule: $\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$
  - 1.5.2 Product Form $[0 \times \infty]$ and Difference Form $[\infty - \infty]$ (Algebraic transformation to $\frac{0}{0}$ or $\frac{\infty}{\infty}$)
  - 1.5.3 Exponential Forms: $\left[0^0\right], \left[\infty^0\right], \left[1^\infty\right]$ (Logarithmic transformation method: $y = f(x)^{g(x)} \implies \ln y = g(x)\ln f(x)$)
- **1.6 Taylor's & Maclaurin's Theorems (Single Variable)**:
  - 1.6.1 Taylor's Theorem with Remainder (Lagrange's Form $R_n = \frac{(x-a)^n}{n!}f^{(n)}(c)$ and Cauchy's Form)
  - 1.6.2 Maclaurin's Infinite Series Expansion: $f(x) = \sum_{k=0}^\infty \frac{f^{(k)}(0)}{k!} x^k$
  - 1.6.3 Standard Series Expansions: $e^x, \sin x, \cos x, \ln(1+x), \ln\left(\frac{1+x}{1-x}\right), (1+x)^m, \tan^{-1}x, \sin^{-1}x$
- **1.7 Curvature & Asymptotes**:
  - 1.7.1 Definition of Curvature $\kappa$ and Radius of Curvature $\rho = \frac{1}{\kappa}$
  - 1.7.2 Radius of Curvature Formulae:
    - Cartesian: $\rho = \frac{\left[1 + (y')^2\right]^{3/2}}{|y''|}$
    - Parametric: $\rho = \frac{(\dot{x}^2 + \dot{y}^2)^{3/2}}{|\dot{x}\ddot{y} - \dot{y}\ddot{x}|}$
    - Polar: $\rho = \frac{(r^2 + r_1^2)^{3/2}}{|r^2 + 2r_1^2 - r r_2|}$ where $r_1 = \frac{dr}{d\theta}, r_2 = \frac{d^2r}{d\theta^2}$
  - 1.7.3 Asymptotes: Parallel Asymptotes (equating coefficients of highest powers) and Oblique Asymptotes ($y = mx+c$ via $\phi_n(m)=0$ and $c\phi_n'(m) + \phi_{n-1}(m) = 0$).

#### 2. Method Recognition Guide & Decision Matrices
- *When to apply Leibniz's Rule*: Look for equations involving product of two functions differentiated $n$ times, especially where one function is a polynomial $x^2$ or $x$ whose derivatives terminate after 2 or 3 steps ($v_1=2x, v_2=2, v_3=0$).
- *When to apply L'Hôpital vs. Series Expansion*: If repeated differentiation becomes algebraically messy (e.g., trigonometric powers), replace $\sin x, \cos x, e^x$ with their first 2–3 terms of Maclaurin series.
- *Exponential Indeterminate Forms*: Always take the natural logarithm $y = \lim f(x)^{g(x)} \implies \ln y = \lim g(x)\ln f(x)$, resolve the $[0 \times \infty]$ form, compute the limit $L$, and conclude $\lim = e^L$.

#### 3. Required Worked Problems (Minimum 10 Fully Solved)
1. Find the $n$-th derivative of $y = e^{2x} \sin(3x) \cos(x)$.
2. If $y = (x + \sqrt{1+x^2})^m$, prove that $(1+x^2)y_{n+2} + (2n+1)xy_{n+1} + (n^2-m^2)y_n = 0$, and find $y_n(0)$.
3. Verify Rolle's Theorem for $f(x) = e^x(\sin x - \cos x)$ on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$ and find $c$.
4. Use Lagrange's MVT to prove the inequality $\frac{x}{1+x} < \ln(1+x) < x$ for all $x > 0$.
5. Evaluate $\lim_{x\to 0} \left(\frac{1}{x^2} - \frac{1}{\sin^2 x}\right)$ (Difference form $[\infty - \infty]$).
6. Evaluate $\lim_{x\to 0} (\cos x)^{1/x^2}$ (Exponential form $[1^\infty]$).
7. Expand $f(x) = \tan^{-1}x$ in powers of $x$ up to the term containing $x^5$ using Maclaurin's Theorem.
8. Find the radius of curvature for the cycloid $x = a(\theta - \sin\theta), y = a(1 - \cos\theta)$ at any point $\theta$.
9. Find the radius of curvature of the cardioid $r = a(1 + \cos\theta)$ at $\theta = \pi/2$.
10. Find all the asymptotes of the cubic curve $x^3 + 2x^2y - xy^2 - 2y^3 + 4xy + 2x - 1 = 0$.

#### 4. Pedagogical Sections
- Common Student Traps Box: Forgetting that L'Hôpital applies **only** to $\frac{0}{0}$ and $\frac{\infty}{\infty}$; confusing $\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]$ (quotient rule) with L'Hôpital's $\frac{f'(x)}{g'(x)}$; forgetting $e^L$ at the end of exponential limits.
- High-Yield Quick Revision: Summary table of standard $n$-th derivatives, Leibniz formula, MVT formulas, radius of curvature formulas.
- Graded Practice Set: 10 Problems (Level 1 Foundation, Level 2 Exam Standard, Level 3 Challenge).
- 10 High-Quality MCQs with detailed mathematical explanations.
- 25-Mark Unit Test with step-by-step scoring scheme.

---

### PART II / UNIT 2: Single-Variable Integral Calculus, Special Functions & Applications

#### 1. Unit Metadata & Topic Hierarchy
- **2.1 Unit Overview & Learning Objectives**
- **2.2 Definite Integrals and Fundamental Properties**:
  - 2.2.1 Fundamental Theorem of Calculus: $\frac{d}{dx}\left[\int_a^x f(t)dt\right] = f(x)$ and $\int_a^b f(x)dx = F(b) - F(a)$
  - 2.2.2 Leibniz Rule for Differentiation under the Integral Sign:
    $$\frac{d}{dx}\left[\int_{u(x)}^{v(x)} f(x,t)\,dt\right] = \int_{u(x)}^{v(x)} \frac{\partial f}{\partial x}\,dt + f(x, v(x)) v'(x) - f(x, u(x)) u'(x)$$
  - 2.2.3 Core Definite Integral Properties (King's Property $\int_a^b f(x)dx = \int_a^b f(a+b-x)dx$, Symmetry for Even/Odd functions, Periodicity)
- **2.3 Reduction Formulae**:
  - 2.3.1 Derivation and Evaluation of:
    $$I_n = \int \sin^n x\,dx = -\frac{\sin^{n-1}x \cos x}{n} + \frac{n-1}{n} I_{n-2}$$
    $$J_n = \int \cos^n x\,dx = \frac{\cos^{n-1}x \sin x}{n} + \frac{n-1}{n} J_{n-2}$$
    $$T_n = \int \tan^n x\,dx = \frac{\tan^{n-1}x}{n-1} - T_{n-2}$$
    $$S_n = \int \sec^n x\,dx = \frac{\sec^{n-2}x \tan x}{n-1} + \frac{n-2}{n-1} S_{n-2}$$
  - 2.3.2 Combined Reduction Formula for $\int \sin^m x \cos^n x\,dx$
  - 2.3.3 **Walli's Formula** for Definite Integrals on $\left[0, \frac{\pi}{2}\right]$:
    $$\int_0^{\pi/2} \sin^n x\,dx = \int_0^{\pi/2} \cos^n x\,dx = \begin{cases} \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{1}{2} \cdot \frac{\pi}{2} & (n \text{ even}) \\ \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{2}{3} \cdot 1 & (n \text{ odd}) \end{cases}$$
- **2.4 Improper Integrals**:
  - 2.4.1 Type I Improper Integrals (Infinite Intervals: $\int_a^\infty, \int_{-\infty}^b, \int_{-\infty}^\infty$)
  - 2.4.2 Type II Improper Integrals (Discontinuous Integrands with vertical asymptotes)
  - 2.4.3 Convergence Tests: Direct Comparison Test, Limit Comparison Test, $\mu$-test for infinite intervals and finite singularities
- **2.5 Beta and Gamma Functions (Special Functions)**:
  - 2.5.1 **Gamma Function** Definition: $\Gamma(n) = \int_0^\infty e^{-t} t^{n-1}\,dt \quad (n > 0)$
  - 2.5.2 Recurrence and Properties: $\Gamma(n+1) = n\Gamma(n)$, $\Gamma(n+1) = n!$ for positive integers, $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$
  - 2.5.3 **Beta Function** Definition: $B(m,n) = \int_0^1 x^{m-1}(1-x)^{n-1}\,dx \quad (m > 0, n > 0)$
  - 2.5.4 Trigonometric and Alternate Forms of Beta Function:
    $$B(m,n) = 2\int_0^{\pi/2} \sin^{2m-1}\theta \cos^{2n-1}\theta\,d\theta = \int_0^\infty \frac{y^{m-1}}{(1+y)^{m+n}}\,dy$$
  - 2.5.5 Fundamental Relation between Beta and Gamma Functions:
    $$B(m,n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)}$$
  - 2.5.6 Legendre's Duplication Formula: $\Gamma(m)\Gamma\left(m + \frac{1}{2}\right) = \frac{\sqrt{\pi}}{2^{2m-1}} \Gamma(2m)$
- **2.6 Geometric Applications of Definite Integrals**:
  - 2.6.1 **Quadrature (Area Computation)**: Cartesian ($A = \int_a^b [y_2(x)-y_1(x)]dx$), Parametric, and Polar ($A = \frac{1}{2}\int_{\alpha}^\beta r^2\,d\theta$)
  - 2.6.2 **Rectification (Arc Length of Curves)**:
    - Cartesian: $s = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$
    - Parametric: $s = \int_{t_1}^{t_2} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$
    - Polar: $s = \int_{\alpha}^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$
  - 2.6.3 **Volumes of Solids of Revolution**:
    - Rotation about $x$-axis: $V = \pi \int_a^b y^2\,dx$ (Disk Method), $V = \pi \int_a^b (y_2^2 - y_1^2)\,dx$ (Washer Method)
    - Rotation about $y$-axis: $V = 2\pi \int_a^b x y\,dx$ (Cylindrical Shell Method)
  - 2.6.4 **Surface Areas of Solids of Revolution**: $S = 2\pi \int y\,ds$ (about $x$-axis) and $S = 2\pi \int x\,ds$ (about $y$-axis).

#### 2. Method Recognition Guide & Decision Matrices
- *Evaluating $\int_0^{\pi/2} \sin^p\theta \cos^q\theta\,d\theta$*: Set $2m-1=p \implies m=\frac{p+1}{2}$ and $2n-1=q \implies n=\frac{q+1}{2}$. Then the integral evaluates to $\frac{1}{2} B(m,n) = \frac{\Gamma\left(\frac{p+1}{2}\right)\Gamma\left(\frac{q+1}{2}\right)}{2\Gamma\left(\frac{p+q+2}{2}\right)}$.
- *Recognizing Improper Integrals*: Always scan the integrand for singularities within the integration limits (e.g., $\int_0^2 \frac{1}{(x-1)^2}dx$ has a singularity at $x=1$ and must be split into $\int_0^1 + \int_1^2$).

#### 3. Required Worked Problems (Minimum 10 Fully Solved)
1. Prove the reduction formula for $I_n = \int \cos^n x\,dx$, and evaluate $\int_0^{\pi/2} \cos^7 x\,dx$.
2. Evaluate $\int_0^{\pi/2} \sin^6 x \cos^4 x\,dx$ using Walli's formula / Beta-Gamma functions.
3. Show that $\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}$, and deduce $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.
4. Evaluate $\int_0^1 x^4 (1-\sqrt{x})^5\,dx$ using Beta-Gamma transformations.
5. Prove that $\int_0^{\pi/2} \sqrt{\tan\theta}\,d\theta = \frac{\pi}{\sqrt{2}}$.
6. Test the convergence of the improper integral $\int_0^\infty \frac{x^2}{1+x^4}\,dx$.
7. Find the entire length of the perimeter of the astroid $x^{2/3} + y^{2/3} = a^{2/3}$ (Parametric: $x = a\cos^3 t, y = a\sin^3 t$).
8. Find the area enclosed between the parabola $y^2 = 4ax$ and the line $y = mx$.
9. Find the volume of the solid generated by revolving the cardioid $r = a(1+\cos\theta)$ about the initial line.
10. Find the surface area of the sphere formed by rotating the semicircle $y = \sqrt{a^2-x^2}$ about the $x$-axis.

#### 4. Pedagogical Sections
- Common Student Traps Box: Forgetting the factor of $\frac{1}{2}$ in the trigonometric form of Beta function; improper cancellation when $n$ is a half-integer in $\Gamma(n)$; forgetting to test endpoint singularities in improper integrals.
- High-Yield Quick Revision: Master formula sheet of Beta/Gamma relations, Walli's tables, arc length differentials ($ds$), and volume integrals.
- Graded Practice Set: 10 Problems across three difficulty tiers.
- 10 High-Quality MCQs with complete analytical rationale.
- 25-Mark Unit Test with scoring rubric and solutions.

---

### PART III / UNIT 3: Infinite Sequences, Series & Convergence Tests

#### 1. Unit Metadata & Topic Hierarchy
- **3.1 Unit Overview & Learning Objectives**
- **3.2 Sequences and Convergence**:
  - 3.2.1 Definition of a Sequence $\{a_n\}$, Limit of a Sequence $\lim_{n\to\infty} a_n = L$
  - 3.2.2 Monotonic Sequences (Increasing, Decreasing) and Bounded Sequences (Bounded Above, Bounded Below)
  - 3.2.3 **Monotone Convergence Theorem**: Every bounded monotonic sequence converges
  - 3.2.4 Sandwich (Squeeze) Theorem for Sequences
- **3.3 Infinite Series Foundations**:
  - 3.3.1 Definition of an Infinite Series $\sum_{n=1}^\infty a_n$ and Sequence of Partial Sums $\{S_n\}$
  - 3.3.2 Convergence, Divergence, and Oscillation of Series
  - 3.3.3 **$n$-th Term Test for Divergence**: If $\lim_{n\to\infty} a_n \ne 0$, the series $\sum a_n$ diverges (Converse is false: Harmonic series $\sum \frac{1}{n}$ diverges even though $\lim \frac{1}{n} = 0$)
  - 3.3.4 **Geometric Series Test**: $\sum_{n=0}^\infty a r^n$ converges to $\frac{a}{1-r}$ if $|r| < 1$, diverges if $|r| \ge 1$
  - 3.3.5 **$p$-Series (Hyper-Harmonic) Test**: $\sum_{n=1}^\infty \frac{1}{n^p}$ converges if $p > 1$, diverges if $p \le 1$
- **3.4 Tests for Convergence of Positive Term Series**:
  - 3.4.1 **Direct Comparison Test**: If $0 \le a_n \le b_n$, $\sum b_n$ conv $\implies \sum a_n$ conv; $\sum a_n$ div $\implies \sum b_n$ div
  - 3.4.2 **Limit Comparison Test**: If $\lim_{n\to\infty} \frac{a_n}{b_n} = L$ where $0 < L < \infty$, both $\sum a_n$ and $\sum b_n$ converge or diverge together
  - 3.4.3 **D'Alembert's Ratio Test**: $\lim_{n\to\infty} \frac{a_{n+1}}{a_n} = L$; Converges if $L < 1$, Diverges if $L > 1$, **Test Fails if $L = 1$**
  - 3.4.4 **Cauchy's Root Test**: $\lim_{n\to\infty} (a_n)^{1/n} = L$; Converges if $L < 1$, Diverges if $L > 1$, **Test Fails if $L = 1$**
  - 3.4.5 **Raabe's Test (Higher Ratio Test)**: When D'Alembert's test fails ($L=1$), compute:
    $$\lim_{n\to\infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right) = R$$
    Converges if $R > 1$, Diverges if $R < 1$, Test Fails if $R = 1$
  - 3.4.6 **Logarithmic Test**: When Ratio Test fails and $\frac{a_n}{a_{n+1}}$ involves $e$, compute:
    $$\lim_{n\to\infty} \left( n \ln\frac{a_n}{a_{n+1}} \right) = L$$
    Converges if $L > 1$, Diverges if $L < 1$
  - 3.4.7 **Cauchy's Integral Test**: If $f(x)$ is positive, continuous, and decreasing for $x \ge 1$, $\sum_{n=1}^\infty a_n$ and $\int_1^\infty f(x)dx$ converge or diverge together
- **3.5 Alternating Series & Absolute Convergence**:
  - 3.5.1 **Leibniz's Test (Alternating Series Test)**: For $\sum_{n=1}^\infty (-1)^{n-1} a_n$ where $a_n > 0$, the series converges if:
    1. $a_{n+1} \le a_n$ for all $n$ (strictly decreasing magnitude)
    2. $\lim_{n\to\infty} a_n = 0$
  - 3.5.2 **Absolute vs. Conditional Convergence**:
    - $\sum a_n$ is **Absolutely Convergent** if $\sum |a_n|$ converges
    - $\sum a_n$ is **Conditionally Convergent** if $\sum a_n$ converges by Leibniz's test but $\sum |a_n|$ diverges (e.g., Alternating Harmonic Series $\sum \frac{(-1)^{n-1}}{n}$)
- **3.6 Power Series**:
  - 3.6.1 Definition of Power Series $\sum_{n=0}^\infty c_n (x-a)^n$ centered at $x=a$
  - 3.6.2 **Radius of Convergence ($R$)**:
    $$R = \lim_{n\to\infty} \left| \frac{c_n}{c_{n+1}} \right| \quad \text{or} \quad R = \frac{1}{\lim_{n\to\infty} \sqrt[n]{|c_n|}}$$
  - 3.6.3 **Interval of Convergence**: $(a-R, a+R)$ and rigorous convergence testing at endpoints $x = a-R$ and $x = a+R$.

#### 2. Method Selection Flowchart for Series Testing
```
Is the series alternating?
├── YES ──► Check Leibniz Test: (1) decreasing? (2) limit=0? ──► Test Absolute Convergence sum(|an|)
└── NO (Positive terms)
     ├── Involves factorials (n!) or exponentials (x^n)? ──► D'Alembert's Ratio Test
     │    └── Ratio Test gives L = 1? ──► Use Raabe's Test or Logarithmic Test
     ├── Involves whole n-th powers (e.g., [ ... ]^n)? ──► Cauchy's Root Test
     ├── Involves rational algebraic functions of n? ──► Limit Comparison Test with p-series
     └── Involves 1 / (n * ln(n))? ──► Cauchy's Integral Test
```

#### 3. Required Worked Problems (Minimum 10 Fully Solved)
1. Test the convergence of the series $\sum_{n=1}^\infty \frac{\sqrt{n+1} - \sqrt{n}}{n^p}$.
2. Test the convergence of $\sum_{n=1}^\infty \frac{n^3 + 1}{2^n + n}$.
3. Test the convergence of $\sum_{n=1}^\infty \frac{x^n}{n!}$ for all $x > 0$.
4. Test the convergence of the series $\sum_{n=1}^\infty \frac{1 \cdot 3 \cdot 5 \cdots (2n-1)}{2 \cdot 4 \cdot 6 \cdots (2n)} x^n$ ($x > 0$) (Requires D'Alembert $\rightarrow$ Raabe's Test at $x=1$).
5. Test the convergence of $\sum_{n=1}^\infty \left(1 + \frac{1}{\sqrt{n}}\right)^{-n^{3/2}}$ using Cauchy's Root Test.
6. Test the convergence of $\sum_{n=2}^\infty \frac{1}{n (\ln n)^p}$ using the Integral Test.
7. Test the alternating series $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{\sqrt{n}}$ for absolute and conditional convergence.
8. Test the series $\sum_{n=1}^\infty (-1)^n \frac{n}{2n-1}$ using the $n$-th term divergence test.
9. Find the radius and interval of convergence of the power series $\sum_{n=1}^\infty \frac{(x-2)^n}{n \cdot 3^n}$, testing both endpoints.
10. Find the radius of convergence of $\sum_{n=0}^\infty \frac{n!}{(2n)!} x^n$.

#### 4. Pedagogical Sections
- Common Student Traps Box: Confusing $L < 1$ (convergence in Ratio/Root test) with $R > 1$ (convergence in Raabe's test); assuming $\lim a_n = 0$ guarantees convergence; forgetting to test power series endpoints separately.
- High-Yield Quick Revision: Master convergence tests summary matrix with failure conditions and escalation paths.
- Graded Practice Set: 10 Problems across three difficulty tiers.
- 10 High-Quality MCQs with complete mathematical explanations.
- 25-Mark Unit Test with scoring rubric and complete solutions.

---

### PART IV / UNIT 4: Multivariable Differential Calculus, Optimization & Jacobians

#### 1. Unit Metadata & Topic Hierarchy
- **4.1 Unit Overview & Learning Objectives**
- **4.2 Functions of Several Variables, Limits & Continuity**:
  - 4.2.1 Real-valued functions of two and three variables $z = f(x,y)$, Domain, Range, Level Curves, and Contour Surfaces
  - 4.2.2 Limits of Two-Variable Functions $\lim_{(x,y)\to(x_0,y_0)} f(x,y) = L$
  - 4.2.3 Non-existence of Limits via Path-Dependence: Testing linear paths $y = mx$, parabolic paths $y = kx^2$, and polar substitution ($x = r\cos\theta, y = r\sin\theta$)
  - 4.2.4 Continuity in Two Variables ($\lim_{(x,y)\to(a,b)} f(x,y) = f(a,b)$)
- **4.3 Partial Differentiation & Higher-Order Derivatives**:
  - 4.3.1 First-order partial derivatives: $f_x = \frac{\partial f}{\partial x} = \lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}{h}$ and $f_y = \frac{\partial f}{\partial y}$
  - 4.3.2 Higher-order partial derivatives ($f_{xx}, f_{yy}, f_{xy}, f_{yx}$)
  - 4.3.3 **Clairaut's (Schwarz's) Theorem on Mixed Partials**: Equality of mixed partials $f_{xy} = f_{yx}$ when second derivatives are continuous
- **4.4 Euler's Theorem on Homogeneous Functions**:
  - 4.4.1 Definition of Homogeneous Function of Degree $n$: $f(tx, ty) = t^n f(x,y)$
  - 4.4.2 **Euler's Theorem (First-Order)**: If $u = f(x,y)$ is homogeneous of degree $n$, then:
    $$x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = n u$$
  - 4.4.3 **Euler's Theorem (Second-Order Extension)**:
    $$x^2 \frac{\partial^2 u}{\partial x^2} + 2xy \frac{\partial^2 u}{\partial x \partial y} + y^2 \frac{\partial^2 u}{\partial y^2} = n(n-1) u$$
  - 4.4.4 Composite Homogeneous Functions (e.g., $u = \sin^{-1}\left(\frac{x^2+y^2}{x+y}\right) \implies \sin u = f(x,y)$ homogeneous of degree 1)
- **4.5 Total Derivatives & Chain Rule**:
  - 4.5.1 Total Differential: $dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$
  - 4.5.2 Chain Rule Case 1: $z = f(x,y)$ where $x = x(t), y = y(t) \implies \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}$
  - 4.5.3 Chain Rule Case 2: $z = f(u,v)$ where $u = u(x,y), v = v(x,y) \implies \frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$
  - 4.5.4 Implicit Function Differentiation: If $F(x,y) = 0$, then $\frac{dy}{dx} = -\frac{F_x}{F_y}$; If $F(x,y,z) = 0$, then $\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}$ and $\frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$
- **4.6 Tangent Planes, Normal Lines & Taylor's Theorem (Two Variables)**:
  - 4.6.1 Tangent Plane to Surface $z = f(x,y)$ at $(x_0, y_0, z_0)$: $z - z_0 = f_x(x_0,y_0)(x - x_0) + f_y(x_0,y_0)(y - y_0)$
  - 4.6.2 Tangent Plane to Implicit Surface $F(x,y,z) = 0$: $F_x(x-x_0) + F_y(y-y_0) + F_z(z-z_0) = 0$
  - 4.6.3 Normal Line Equations: $\frac{x-x_0}{F_x} = \frac{y-y_0}{F_y} = \frac{z-z_0}{F_z}$
  - 4.6.4 Taylor's and Maclaurin's Expansion for $f(x,y)$ up to quadratic terms
- **4.7 Maxima and Minima of Functions of Two Variables**:
  - 4.7.1 Critical Points / Stationary Points ($f_x(a,b) = 0$ and $f_y(a,b) = 0$)
  - 4.7.2 **Second Derivative Test (Hessian Discriminant)**: Define $r = f_{xx}(a,b), s = f_{xy}(a,b), t = f_{yy}(a,b)$, and Discriminant $D = rt - s^2$:
    - **Local Minimum**: If $rt - s^2 > 0$ and $r > 0$
    - **Local Maximum**: If $rt - s^2 > 0$ and $r < 0$
    - **Saddle Point**: If $rt - s^2 < 0$ (neither max nor min)
    - **Inconclusive Test**: If $rt - s^2 = 0$ (higher-order investigation required)
  - 4.7.3 **Lagrange's Method of Undetermined Multipliers** for Constrained Optimization:
    - Optimize $f(x,y,z)$ subject to constraint $g(x,y,z) = 0$: Solve $\nabla f = \lambda \nabla g$ along with $g=0$
    - Two Constraints $g_1 = 0, g_2 = 0$: Solve $\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2$
- **4.8 Jacobians (Functional Determinants)**:
  - 4.8.1 Definition for Two and Three Variables:
    $$J = \frac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{vmatrix}, \quad \frac{\partial(u,v,w)}{\partial(x,y,z)} = \begin{vmatrix} u_x & u_y & u_z \\ v_x & v_y & v_z \\ w_x & w_y & w_z \end{vmatrix}$$
  - 4.8.2 Reciprocal Property: $J \cdot J' = \frac{\partial(u,v)}{\partial(x,y)} \cdot \frac{\partial(x,y)}{\partial(u,v)} = 1$
  - 4.8.3 Chain Rule for Jacobians: $\frac{\partial(u,v)}{\partial(r,\theta)} = \frac{\partial(u,v)}{\partial(x,y)} \cdot \frac{\partial(x,y)}{\partial(r,\theta)}$
  - 4.8.4 **Functional Dependence Criterion**: Functions $u, v, w$ are functionally dependent if and only if $\frac{\partial(u,v,w)}{\partial(x,y,z)} = 0$.

#### 2. Method Recognition Guide & Decision Matrices
- *Testing Unconstrained Extrema vs. Constrained Extrema*: If the problem asks for maximum/minimum of $f(x,y)$ without side conditions, use the $rt - s^2$ Hessian test. If side constraints like $x+y+z=1$ or $x^2+y^2=a^2$ are given, use Lagrange Multipliers.
- *Euler's Theorem on Non-Algebraic Functions*: If $u = \ln\left(\frac{x^4+y^4}{x+y}\right)$, do NOT apply Euler directly to $u$. Rewrite as $e^u = \frac{x^4+y^4}{x+y} = f(x,y)$ (homogeneous of degree $n=3$), then apply $x(e^u)_x + y(e^u)_y = 3e^u \implies x u_x + y u_y = 3$.

#### 3. Required Worked Problems (Minimum 10 Fully Solved)
1. Show that the limit $\lim_{(x,y)\to(0,0)} \frac{xy^2}{x^2 + y^4}$ does not exist by testing the paths $x = my^2$.
2. If $u = \tan^{-1}\left(\frac{x^3+y^3}{x-y}\right)$, prove that $x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \sin 2u$, and $x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = \sin 4u - \sin 2u$.
3. If $z = f(x,y)$ where $x = e^u + e^{-v}$ and $y = e^{-u} - e^v$, prove that $\frac{\partial z}{\partial u} - \frac{\partial z}{\partial v} = x \frac{\partial z}{\partial x} - y \frac{\partial z}{\partial y}$.
4. If $x^y + y^x = c$, find $\frac{dy}{dx}$ using partial derivatives.
5. Find the equations of the tangent plane and normal line to the surface $x^2 + 2y^2 + 3z^2 = 12$ at the point $(1, 2, 1)$.
6. Expand $f(x,y) = e^x \cos y$ in powers of $x$ and $y$ up to terms of degree 2 using Taylor's Theorem.
7. Find all local maxima, local minima, and saddle points of $f(x,y) = x^3 + y^3 - 3xy$.
8. Find the dimensions of a rectangular box of maximum volume that can be inscribed in the ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ using Lagrange's Multipliers.
9. If $x = r\sin\theta\cos\phi, y = r\sin\theta\sin\phi, z = r\cos\theta$, compute the Jacobian $\frac{\partial(x,y,z)}{\partial(r,\theta,\phi)}$ and prove it equals $r^2 \sin\theta$.
10. Verify whether $u = x + y + z$, $v = xy + yz + zx$, and $w = x^2 + y^2 + z^2$ are functionally dependent, and if so, find the functional relation between them.

#### 4. Pedagogical Sections
- Common Student Traps Box: Forgetting that $y=mx$ is insufficient to prove limit existence (must test higher-degree paths like $y=kx^2$); sign error in implicit differentiation formula ($\frac{dy}{dx} = -F_x/F_y$); forgetting that $rt-s^2 < 0$ represents a saddle point, not an inconclusive test.
- High-Yield Quick Revision: Summary matrix of Euler's theorem variants, Hessian decision rules, and Jacobian algebraic identities.
- Graded Practice Set: 10 Problems across three difficulty tiers.
- 10 High-Quality MCQs with complete mathematical explanations.
- 25-Mark Unit Test with scoring rubric and complete solutions.

---

### PART V / UNIT 5: Multiple Integrals & Coordinate Transformations

#### 1. Unit Metadata & Topic Hierarchy
- **5.1 Unit Overview & Learning Objectives**
- **5.2 Double Integrals in Cartesian Coordinates**:
  - 5.2.1 Definition of Double Integral $\iint_R f(x,y)\,dA$ as Limit of Riemann Sums
  - 5.2.2 Double Integrals over Rectangular Regions (Fubini's Theorem: $\int_a^b \int_c^d f(x,y) dy dx = \int_c^d \int_a^b f(x,y) dx dy$)
  - 5.2.3 Double Integrals over Non-Rectangular Regions:
    - **Type I ($y$-Simple / Vertically Simple)**: $R = \{(x,y) \mid a \le x \le b, \, g_1(x) \le y \le g_2(x)\}$, Evaluated as $\int_a^b \left[\int_{g_1(x)}^{g_2(x)} f(x,y) dy\right] dx$
    - **Type II ($x$-Simple / Horizontally Simple)**: $R = \{(x,y) \mid c \le y \le d, \, h_1(y) \le x \le h_2(y)\}$, Evaluated as $\int_c^d \left[\int_{h_1(y)}^{h_2(y)} f(x,y) dx\right] dy$
  - 5.2.4 Systematic Procedure for Sketching Boundaries and Determining Integration Limits
- **5.3 Change of Order of Integration**:
  - 5.3.1 Motivation: Transforming intractable single-step antiderivatives (e.g., $\int e^{x^2} dx$, $\int \frac{\sin x}{x} dx$, $\int \sqrt{1+y^3} dy$) into easily integrable forms
  - 5.3.2 4-Step Algorithmic Procedure:
    1. Extract initial limits and write down boundary curve equations.
    2. Sketch the exact 2D bounded region $R$ in the $xy$-plane, identifying intersection vertices.
    3. Change slicing from vertical strips ($dx$ outer) to horizontal strips ($dy$ outer), or vice-versa.
    4. Formulate the new inner and outer limits (splitting into sub-regions if boundary curves change) and evaluate.
- **5.4 Double Integrals in Polar Coordinates**:
  - 5.4.1 Coordinate Transformation: $x = r\cos\theta, y = r\sin\theta$, Area Differential $dA = dx dy = r dr d\theta$
  - 5.4.2 Determining Limits of Radial Rays ($r_1(\theta) \le r \le r_2(\theta)$) and Sector Angles ($\alpha \le \theta \le \beta$)
  - 5.4.3 Integration over Circles, Semicircles, Cardioids ($r = a(1+\cos\theta)$), and Lemniscates ($r^2 = a^2\cos 2\theta$)
- **5.5 Triple Integrals in Cartesian Coordinates**:
  - 5.5.1 Definition $\iiint_V f(x,y,z)\,dV = \int_{x_1}^{x_2} \int_{y_1(x)}^{y_2(x)} \int_{z_1(x,y)}^{z_2(x,y)} f(x,y,z)\,dz dy dx$
  - 5.5.2 Setting up 3D Limits over Tetrahedrons, Paraboloids, Cylinders, and Spheres
- **5.6 General Change of Variables in Multiple Integrals via Jacobians**:
  - 5.6.1 2D Transformation: $\iint_R f(x,y)\,dx dy = \iint_{R'} f(x(u,v), y(u,v)) \left| \frac{\partial(x,y)}{\partial(u,v)} \right| du dv$
  - 5.6.2 Elliptic Coordinate Transformations: $x = ar\cos\theta, y = br\sin\theta \implies dx dy = ab\,r\,dr\,d\theta$
  - 5.6.3 **Cylindrical Coordinates**: $x = r\cos\theta, y = r\sin\theta, z = z \implies dV = r dr d\theta dz$
  - 5.6.4 **Spherical Polar Coordinates**: $x = \rho\sin\phi\cos\theta, y = \rho\sin\phi\sin\theta, z = \rho\cos\phi \implies dV = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$
- **5.7 Applications of Multiple Integrals**:
  - 5.7.1 Area of Plane Bounded Regions: $\text{Area} = \iint_R dx dy = \iint_R r dr d\theta$
  - 5.7.2 Volume of 3D Enclosed Solids: $\text{Volume} = \iiint_V dV = \iint_R [z_{\text{top}}(x,y) - z_{\text{bottom}}(x,y)] dx dy$
  - 5.7.3 Mass of Lamina with Variable Density $\rho(x,y)$: $M = \iint_R \rho(x,y)\,dA$
  - 5.7.4 Center of Gravity / Centroids: $\bar{x} = \frac{1}{M}\iint_R x\,\rho\,dA, \quad \bar{y} = \frac{1}{M}\iint_R y\,\rho\,dA$
  - 5.7.5 Moments of Inertia: $I_x = \iint_R y^2 \rho\,dA, \quad I_y = \iint_R x^2 \rho\,dA, \quad I_0 = I_x + I_y = \iint_R (x^2+y^2)\rho\,dA$.

#### 2. Method Recognition Guide & Decision Matrices
- *When to convert to Polar Coordinates*: Look for expressions containing $x^2 + y^2$ (which becomes $r^2$), circular boundaries $x^2+y^2 \le a^2$, or integrations over cardioids/sectors.
- *When to convert to Spherical Coordinates in Triple Integrals*: Look for spheres $x^2+y^2+z^2 \le R^2$, cones $z = \sqrt{x^2+y^2}$, or integrands containing $(x^2+y^2+z^2)^{k}$.
- *Recognizing Change of Order Necessity*: If an integral like $\int_0^1 \int_x^1 e^{y^2} dy dx$ cannot be integrated with respect to $y$ in elementary terms, reverse the order to $dx dy$, integrating $\int x$ first.

#### 3. Required Worked Problems (Minimum 10 Fully Solved)
1. Evaluate $\iint_R xy(x+y)\,dx dy$ over the region bounded between $y = x^2$ and $y = x$.
2. Change the order of integration and evaluate $\int_0^1 \int_{y^2}^1 y e^{x^2}\,dx dy$.
3. Change the order of integration and evaluate $\int_0^a \int_{\sqrt{ax}}^{a} \frac{y^2}{\sqrt{y^4 - a^2 x^2}}\,dy dx$.
4. Evaluate $\iint_R \frac{r}{\sqrt{a^2 - r^2}}\,dr d\theta$ over one loop of the lemniscate $r^2 = a^2 \cos 2\theta$.
5. Evaluate $\iint_R e^{-(x^2+y^2)}\,dx dy$ over the entire positive quadrant $x \ge 0, y \ge 0$ by transforming to polar coordinates, and deduce $\int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}$.
6. Evaluate $\iiint_V (x+y+z)\,dx dy dz$ over the tetrahedron bounded by $x=0, y=0, z=0$ and $x+y+z=1$.
7. Find the volume of the cylinder $x^2+y^2 \le 2ax$ bounded above by the paraboloid $z = x^2+y^2$ and below by $z=0$ using cylindrical coordinates.
8. Evaluate $\iiint_V \frac{1}{\sqrt{1 - x^2 - y^2 - z^2}}\,dx dy dz$ throughout the volume of the positive octant of the unit sphere using spherical polar coordinates.
9. Find the area enclosed between the cardioids $r = a(1+\cos\theta)$ and $r = a(1-\cos\theta)$ using double integration.
10. Find the center of gravity of a uniform lamina bounded by the parabola $y^2 = 4ax$ and its latus rectum $x = a$.

#### 4. Pedagogical Sections
- Common Student Traps Box: Forgetting the Jacobian factor $r$ in polar coordinates ($dx dy \to r dr d\theta$) and $\rho^2 \sin\phi$ in spherical polar coordinates ($dV \to \rho^2 \sin\phi d\rho d\phi d\theta$); incorrect outer limits containing variables (outer limits must ALWAYS be constants!).
- High-Yield Quick Revision: Master table of coordinate transformation differentials, Jacobian conversion factors, and change-of-order templates.
- Graded Practice Set: 10 Problems across three difficulty tiers.
- 10 High-Quality MCQs with complete mathematical explanations.
- 25-Mark Unit Test with scoring rubric and complete solutions.

---

### PART VI / UNIT 6: Vector Calculus & Field Integral Theorems

#### 1. Unit Metadata & Topic Hierarchy
- **6.1 Unit Overview \& Learning Objectives**
- **6.2 Vector Differential Calculus**:
  - 6.2.1 Scalar and Vector Fields (Definitions, Physical examples: Temperature field vs. Fluid velocity field)
  - 6.2.2 The Del Vector Operator ($\nabla = \hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}$)
  - 6.2.3 **Gradient of a Scalar Field ($\nabla \phi = \text{grad}\,\phi$)**:
    - Formula: $\nabla \phi = \frac{\partial \phi}{\partial x}\hat{i} + \frac{\partial \phi}{\partial y}\hat{j} + \frac{\partial \phi}{\partial z}\hat{k}$
    - Physical \& Geometrical Significance: Vector pointing in the direction of **maximum rate of increase** of $\phi$; **Normal vector** to the level surface $\phi(x,y,z) = c$
    - Unit Normal Vector: $\hat{n} = \frac{\nabla \phi}{|\nabla \phi|}$
  - 6.2.4 **Directional Derivative**:
    - Rate of change of $\phi$ in the direction of a given unit vector $\hat{u}$: $D_{\hat{u}}\phi = \nabla \phi \cdot \hat{u} = |\nabla \phi| \cos\theta$
    - Maximum Directional Derivative: Occurs along $\hat{u} = \frac{\nabla \phi}{|\nabla \phi|}$ and equals $|\nabla \phi|$
  - 6.2.5 **Divergence of a Vector Field ($\nabla \cdot \vec{F} = \text{div}\,\vec{F}$)**:
    - Formula: If $\vec{F} = F_1\hat{i} + F_2\hat{j} + F_3\hat{k}$, then $\text{div}\,\vec{F} = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z}$
    - Physical Significance: Net volume flux per unit volume outward from a point (Source if $\text{div} > 0$, Sink if $\text{div} < 0$)
    - **Solenoidal Vector Field**: A vector field whose divergence is everywhere zero ($\nabla \cdot \vec{F} = 0$, incompressible fluid)
  - 6.2.6 **Curl of a Vector Field ($\nabla \times \vec{F} = \text{curl}\,\vec{F}$)**:
    - Formula: $\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_1 & F_2 & F_3 \end{vmatrix}$
    - Physical Significance: Measure of local rotation / angular velocity of a fluid ($\vec{v} = \vec{\omega} \times \vec{r} \implies \vec{\omega} = \frac{1}{2}\text{curl}\,\vec{v}$)
    - **Irrotational Vector Field**: A vector field whose curl is everywhere zero ($\nabla \times \vec{F} = \vec{0}$)
    - **Scalar Potential ($\phi$)**: If $\vec{F}$ is irrotational, there exists a scalar potential $\phi$ such that $\vec{F} = \nabla \phi$ (Conservative Field)
  - 6.2.7 Master Vector Differential Identities:
    - $\text{curl}(\text{grad}\,\phi) = \nabla \times (\nabla \phi) = \vec{0}$ (Gradient fields are irrotational)
    - $\text{div}(\text{curl}\,\vec{F}) = \nabla \cdot (\nabla \times \vec{F}) = 0$ (Curl fields are solenoidal)
    - Laplacian: $\nabla^2 \phi = \nabla \cdot (\nabla \phi) = \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2}$
- **6.3 Vector Integral Calculus**:
  - 6.3.1 **Line Integrals ($\int_C \vec{F} \cdot d\vec{r}$)**:
    - Evaluation along parametric path $\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$: $\int_{t_1}^{t_2} [F_1 x'(t) + F_2 y'(t) + F_3 z'(t)] dt$
    - Physical Application: **Total Work Done** by a force field along curve $C$
    - **Conservative Vector Fields \& Path Independence**: $\int_A^B \vec{F}\cdot d\vec{r} = \phi(B) - \phi(A)$ depends only on endpoints; $\oint_C \vec{F}\cdot d\vec{r} = 0$ for any closed curve
  - 6.3.2 **Surface Integrals ($\iint_S \vec{F} \cdot \hat{n}\,dS$)**:
    - Evaluation via 2D projection onto coordinate planes ($xy, yz, zx$):
      $$\iint_S \vec{F}\cdot\hat{n}\,dS = \iint_{R_{xy}} \vec{F}\cdot\hat{n} \frac{dx dy}{|\hat{n}\cdot\hat{k}|}$$
    - Physical Application: **Total Vector Flux** passing through surface $S$
  - 6.3.3 **Volume Integrals ($\iiint_V \phi\,dV$ and $\iiint_V \vec{F}\,dV$)**
- **6.4 Fundamental Integral Theorems of Vector Calculus**:
  - 6.4.1 **Green's Theorem in the Plane**:
    - Statement: Let $C$ be a positively oriented, piecewise-smooth, simple closed curve in a plane, bounding region $R$. If $P(x,y)$ and $Q(x,y)$ have continuous partial derivatives on $R$, then:
      $$\oint_C (P\,dx + Q\,dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy$$
    - Area of Enclosed Region: $\text{Area} = \frac{1}{2}\oint_C (x\,dy - y\,dx)$
    - Verification and Step-by-Step Evaluation Workflows
  - 6.4.2 **Stokes' Theorem**:
    - Statement: Let $S$ be an oriented piecewise-smooth open surface bounded by a simple closed boundary curve $C$. If $\vec{F}$ is a continuously differentiable vector field, then:
      $$\oint_C \vec{F} \cdot d\vec{r} = \iint_S (\nabla \times \vec{F}) \cdot \hat{n} \, dS$$
    - Transformation between Line Integrals around closed 3D loops and Surface Integrals of Curl over capping surfaces
    - Verification on Hemispheres, Paraboloids, and Triangular Planar Segments
  - 6.4.3 **Gauss's Divergence Theorem**:
    - Statement: Let $V$ be a volume bounded by a closed, orientable surface $S$ with outward unit normal $\hat{n}$. If $\vec{F}$ is a continuously differentiable vector field, then:
      $$\iint_S \vec{F} \cdot \hat{n} \, dS = \iiint_V (\nabla \cdot \vec{F}) \, dV$$
    - Transformation between Closed Surface Flux Integrals and Volume Integrals of Divergence
    - Verification on Cubes, Cylinders, and Spheres.

#### 2. Method Recognition Guide & Decision Matrices
- *Evaluating $\oint_C \vec{F}\cdot d\vec{r}$ in a 2D plane*: Use **Green's Theorem** ($\iint_R (Q_x - P_y)dA$).
- *Evaluating $\oint_C \vec{F}\cdot d\vec{r}$ around a 3D non-planar curve*: Use **Stokes' Theorem** ($\iint_S (\text{curl}\,\vec{F})\cdot\hat{n} dS$), choosing the simplest planar capping surface $S$.
- *Evaluating $\iint_S \vec{F}\cdot\hat{n} dS$ over a CLOSED 3D surface (sphere, cube, closed cylinder)*: Use **Gauss's Divergence Theorem** ($\iiint_V (\text{div}\,\vec{F}) dV$). Computing $\text{div}\,\vec{F}$ often yields a constant, reducing the problem to a trivial volume calculation!

#### 3. Required Worked Problems (Minimum 10 Fully Solved)
1. Find the directional derivative of $\phi = x^2 y z + 4 x z^2$ at the point $(1, -2, -1)$ in the direction of the vector $2\hat{i} - \hat{j} - 2\hat{k}$.
2. Find the angle between the surfaces $x^2 + y^2 + z^2 = 9$ and $z = x^2 + y^2 - 3$ at the point $(2, -1, 2)$ using gradients.
3. Determine the constants $a, b, c$ such that $\vec{F} = (x + 2y + az)\hat{i} + (bx - 3y - z)\hat{j} + (4x + cy + 2z)\hat{k}$ is irrotational, and find its scalar potential $\phi$ such that $\vec{F} = \nabla\phi$.
4. Prove that $\vec{F} = \frac{\vec{r}}{r^3}$ is both solenoidal and irrotational for $r \ne 0$.
5. Evaluate the line integral $\int_C \vec{F}\cdot d\vec{r}$ where $\vec{F} = (3x^2 + 6y)\hat{i} - 14yz\hat{j} + 20xz^2\hat{k}$ along the straight line path from $(0,0,0)$ to $(1,1,1)$.
6. Verify Green's Theorem in the plane for $\oint_C [(xy + y^2)dx + x^2 dy]$ where $C$ is the closed boundary bounded by $y = x$ and $y = x^2$.
7. Use Green's Theorem to find the area of the region enclosed by the ellipse $x = a\cos t, y = b\sin t$.
8. Verify Stokes' Theorem for $\vec{F} = (2x - y)\hat{i} - yz^2\hat{j} - y^2 z\hat{k}$ over the upper hemisphere $x^2+y^2+z^2 = 1, z \ge 0$.
9. Verify Gauss's Divergence Theorem for $\vec{F} = 4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}$ taken over the region bounded by the cylinder $x^2+y^2 = 4$, $z=0$, and $z=3$.
10. Evaluate the surface flux $\iint_S \vec{F}\cdot\hat{n}\,dS$ where $\vec{F} = x^3\hat{i} + y^3\hat{j} + z^3\hat{k}$ and $S$ is the closed surface of the sphere $x^2+y^2+z^2 = a^2$ using Gauss's Divergence Theorem.

#### 4. Pedagogical Sections
- Common Student Traps Box: Applying Gauss's Theorem to an OPEN surface (Gauss Divergence applies ONLY to closed surfaces bounding a volume; for open surfaces, you must add capping lids or use Stokes' Theorem); forgetting that $\hat{n}$ must be a UNIT normal vector; sign errors in computing cross-product determinants for curl.
- High-Yield Quick Revision: Master vector theorem comparison matrix (Green vs. Stokes vs. Gauss), Del operator identities, and differential surface area formulas.
- Graded Practice Set: 10 Problems across three difficulty tiers.
- 10 High-Quality MCQs with complete mathematical explanations.
- 25-Mark Unit Test with scoring rubric and complete solutions.

---

## 4. Supplementary Pedagogical Parts Specification

### PART VII: Master Formula, Method Recognition & Identity Sheet
- Complete compilation of all 6 Units' formulas on a consolidated reference matrix:
  - Table 1: Standard Derivatives & $n$-th Differential Rules
  - Table 2: Definite Integrals, Reduction Formulae & Beta-Gamma Equivalences
  - Table 3: Infinite Series Convergence Test Decision Tree & Standard $p$-Series
  - Table 4: Multivariable Calculus: Euler's Theorem, Hessian Rules, Jacobians
  - Table 5: Coordinate Transformation Jacobians (Cartesian, Polar, Cylindrical, Spherical)
  - Table 6: Vector Calculus Differential Identities & Field Theorems (Green, Stokes, Gauss).

### PART VIII: Mixed Multi-Unit Problem Practice Suites
- 30 Comprehensive, Multi-Unit Exam-Style Problems integrating concepts across calculus, series, multivariable analysis, and vector theorems.

### PART IX: Full-Length University Mock Examination Papers (100 Marks Each)
- **Mock Exam 1 (Mid-Term / End-Term Pattern - 100 Marks)**:
  - Section A: 10 Short-Answer Compulsory Questions ($10 \times 2 = 20$ Marks)
  - Section B: 6 Analytical Medium-Length Problems ($6 \times 5 = 30$ Marks)
  - Section C: 5 Comprehensive Descriptive / Verification Problems ($5 \times 10 = 50$ Marks)
  - **Complete Step-by-Step Scoring Solutions and Rubrics**.
- **Mock Exam 2 (Challenging Final Exam Standard - 100 Marks)**:
  - Section A, B, and C with full marking schemes and worked analytical solutions.

---

## 5. Complete Course Syllabus Map & Topic Metrics

| Unit / Part | Unit Title | Major Topics | Subtopics | Formula-Heavy Focus | Problem-Heavy Focus |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Unit 1** | Single-Variable Differential Calculus & MVTs | 7 | 24 | Leibniz rule, MVT forms, Curvature $\rho$, Asymptotes | Leibniz equations, L'Hôpital forms, MVT inequality proofs |
| **Unit 2** | Single-Variable Integrals, Special Functions \& Apps | 6 | 21 | Reduction formulas, Walli's, Beta-Gamma relations | Beta-Gamma integrals, Arc length, Volume of revolution |
| **Unit 3** | Infinite Sequences, Series & Convergence | 6 | 22 | Ratio, Root, Raabe's, Logarithmic, Integral tests | Series testing (Ratio $\to$ Raabe's), Power series intervals |
| **Unit 4** | Multivariable Calculus, Optimization & Jacobians | 8 | 26 | Euler's theorem, Hessian $rt-s^2$, Jacobians, Lagrange | Path limits, Euler extensions, Extrema, Jacobians |
| **Unit 5** | Multiple Integrals & Coordinate Transformations | 7 | 23 | Polar/Spherical Jacobians, Area/Volume integrals | Change of order, Polar conversion, Cylindrical volumes |
| **Unit 6** | Vector Calculus & Field Integral Theorems | 4 | 22 | Grad, Div, Curl, Green's, Stokes', Gauss's theorems | Directional derivatives, Scalar potential, Theorem verifications |
| **Part VII** | Master Formula & Method Sheet | 6 Tables | — | Comprehensive synthesis | Quick-lookup method recognition |
| **Part VIII**| Mixed Problem Practice Suites | 30 Probs | — | Cross-unit synthesis | Advanced multi-step calculus problems |
| **Part IX** | Full-Length Mock Exams (2 Papers) | 2 Sets | 42 Probs | Full syllabus | Timed examination conditioning (100 Marks each) |

---

## 6. Ambiguities & Clarifications in Source Material

1. **Course Title vs. Code**: In LPU curriculum documents, MTH165 is titled *"Mathematics"* or *"Engineering Mathematics I"*, covering single-variable calculus, series, multivariable calculus, multiple integrals, and vector calculus. This blueprint faithfully captures the full multi-part mathematical scope without omitting foundational or advanced topics.
2. **Raabe's and Logarithmic Tests in Series**: Standard university exams frequently include borderline series where D'Alembert's ratio test yields $L=1$. This blueprint includes Raabe's test and the Logarithmic test as formal escalation procedures to ensure complete problem-solving competence.
3. **Change of Variables Jacobians**: Both 2D (polar, elliptical) and 3D (cylindrical, spherical polar) coordinate systems are systematically derived with their Jacobian transformation factors ($r$ and $\rho^2\sin\phi$).

---

## 7. Projected Textbook Dimensions

- **Total Units**: 6 Core Units + 3 Supplementary Practice/Exam Modules (9 Parts total)
- **Estimated Page Count**: **180–250 Pages** (Unconstrained by artificial page limits; prioritizes complete worked mathematical solutions, method recognitions, and exam rigor).
- **Target Compilation Engine**: Two-pass `pdflatex` via `MTH165/Makefile`.
