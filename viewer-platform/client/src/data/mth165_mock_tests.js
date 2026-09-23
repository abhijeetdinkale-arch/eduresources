/**
 * Official MTH165: Mathematics for Engineers Midterm Mock Examination Suite
 * Contains 5 Full-Length 30-Question Tests (150 Questions Total)
 * Modelled on actual University Midterm Examination Papers (Codes: 25261MTH53720 & 25261MTH53683)
 * Includes authentic +1 / -0.25 marking scheme and detailed step-by-step solutions.
 */

export const MTH165_MOCK_TESTS = [
  {
    id: 'mth165-midterm-mock-1',
    code: '25261MTH53720',
    title: 'Midterm Examination • Paper 1 (Official University PYQ)',
    courseCode: 'MTH165',
    courseName: 'Mathematics for Engineers',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['Linear Algebra', 'Eigenvalues', 'Differential Calculus', 'Integrals', 'Mean Value Theorems', 'Limits'],
    description: 'Direct university midterm paper testing matrix rank, eigenvalues, derivative of x^x, Rolle theorem, and Taylor expansions.',
    questions: [
      {
        id: 1,
        question: 'The number of elementary operations required to obtain an inverse is:',
        options: ['Zero', 'Finite', 'Infinite', 'None of these'],
        correctIndex: 1,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'Elementary row operations transform an invertible matrix A into the Identity matrix I.',
            'For any finite n × n non-singular matrix, Gaussian elimination and Gauss-Jordan reduction require a finite sequence of row operations.',
            'Therefore, the number of operations is always finite.'
          ],
          keyConcept: 'Inversion by elementary row operations terminates in finite steps: [A | I] ~ [I | A⁻¹].'
        }
      },
      {
        id: 2,
        question: 'Which of the following is NOT an elementary row operation?',
        options: [
          'Interchanging two rows (Rᵢ ↔ Rⱼ)',
          'Multiplying a row by a non-zero scalar (Rᵢ → kRᵢ)',
          'Adding a scalar multiple of one row to another (Rᵢ → Rᵢ + kRⱼ)',
          'Squaring the elements of a row (Rᵢ → Rᵢ²)'
        ],
        correctIndex: 3,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'The three valid elementary row operations are:',
            '1. Row swap (Rᵢ ↔ Rⱼ)',
            '2. Non-zero scalar multiplication (Rᵢ → kRᵢ, k ≠ 0)',
            '3. Row addition (Rᵢ → Rᵢ + kRⱼ)',
            'Squaring row entries is a non-linear operation and alters the linear span and solution set.'
          ],
          keyConcept: 'Elementary operations must be reversible linear transformations.'
        }
      },
      {
        id: 3,
        question: 'A set containing ONLY the zero vector {0} is:',
        options: ['Linearly Dependent', 'Linearly Independent', 'Either dependent or independent', 'None of these'],
        correctIndex: 0,
        topic: 'Vector Spaces',
        explanation: {
          steps: [
            'For linear independence, c · v = 0 must imply c = 0.',
            'For the zero vector: c · 0 = 0 is satisfied for any non-zero scalar c ≠ 0 (e.g. 5 · 0 = 0).',
            'Since a non-trivial linear combination yields zero, the set is Linearly Dependent.'
          ],
          keyConcept: 'Any set containing the zero vector is always linearly dependent.'
        }
      },
      {
        id: 4,
        question: 'If Rank(A) = Rank([A|B]) in a linear system AX = B, the system is:',
        options: ['Consistent', 'Inconsistent', 'Unique solution only', 'None of these'],
        correctIndex: 0,
        topic: 'Linear Systems',
        explanation: {
          steps: [
            'By the Rouché–Capelli Theorem:',
            'Rank(A) = Rank([A|B]) is the exact necessary and sufficient condition for the system to be Consistent (having at least one solution).',
            'If Rank(A) = Rank([A|B]) = n (number of variables), it has a unique solution; if < n, infinite solutions.'
          ],
          keyConcept: 'Consistency condition: Rank of coefficient matrix = Rank of augmented matrix.'
        }
      },
      {
        id: 5,
        question: 'Cayley-Hamilton theorem states that every square matrix satisfies its:',
        options: ['Rank condition', 'Determinant equation', 'Characteristic equation', 'Eigenvector equation'],
        correctIndex: 2,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Let P(λ) = det(A - λI) = 0 be the characteristic equation of matrix A.',
            'Cayley-Hamilton theorem states that substituting the matrix A for λ yields the zero matrix: P(A) = 0.',
            'Thus, every square matrix satisfies its own Characteristic equation.'
          ],
          keyConcept: 'Cayley-Hamilton Theorem: P(A) = 0 where P(λ) = det(A - λI).'
        }
      },
      {
        id: 6,
        question: 'The system of linear equations x + y = 2 and x - y = 0 has:',
        options: ['No solution', 'Unique solution', 'Infinite solutions', 'None of these'],
        correctIndex: 1,
        topic: 'Linear Systems',
        explanation: {
          steps: [
            'From equation (2): x = y.',
            'Substitute into equation (1): x + x = 2 ⇒ 2x = 2 ⇒ x = 1, y = 1.',
            'The determinant |[1, 1; 1, -1]| = -1 - 1 = -2 ≠ 0, confirming a Unique Solution.'
          ],
          keyConcept: 'det(A) ≠ 0 implies a unique solution.'
        }
      },
      {
        id: 7,
        question: 'For the identity matrix of order 2 (I₂), the characteristic polynomial is:',
        options: ['(λ - 1)²', 'λ² - 1', 'λ² + 1', 'None of these'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Identity matrix I₂ = [[1, 0], [0, 1]].',
            'det(I₂ - λI) = det([[1 - λ, 0], [0, 1 - λ]]) = (1 - λ)(1 - λ) = (λ - 1)²',
            'Therefore, the characteristic polynomial is (λ - 1)².'
          ],
          keyConcept: 'For Iₙ, all n eigenvalues are 1, so the characteristic polynomial is (λ - 1)ⁿ.'
        }
      },
      {
        id: 8,
        question: 'If the eigenvalues of a 2×2 matrix A are 2 and 3, then trace tr(A) is:',
        options: ['0', '5', '6', 'None of these'],
        correctIndex: 1,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Property: The trace of any square matrix equals the sum of its eigenvalues.',
            'tr(A) = λ₁ + λ₂ = 2 + 3 = 5.',
            'Note: The determinant det(A) would be the product = 2 × 3 = 6.'
          ],
          keyConcept: 'Trace tr(A) = Σ λᵢ and Determinant det(A) = Π λᵢ.'
        }
      },
      {
        id: 9,
        question: 'If every diagonal entry of a diagonal matrix is non-zero, then its rank is:',
        options: ['Equal to number of rows', 'Equal to number of columns', 'Both a and b', 'None of these'],
        correctIndex: 2,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'For an n × n square diagonal matrix with non-zero diagonal elements, no row or column is all zeros.',
            'All n rows and columns are linearly independent.',
            'Thus, rank = n = number of rows = number of columns (Both a and b).'
          ],
          keyConcept: 'Rank of a non-singular n×n diagonal matrix is n.'
        }
      },
      {
        id: 10,
        question: 'A singleton set {v} containing a non-zero vector (v ≠ 0) is always:',
        options: ['Dependent vector', 'Independent vector', 'May be both a and b', 'Neither a nor b'],
        correctIndex: 1,
        topic: 'Vector Spaces',
        explanation: {
          steps: [
            'Consider c · v = 0 with v ≠ 0.',
            'Since v is non-zero, this equation forces c = 0.',
            'Since the only scalar satisfying the equation is zero, {v} is Linearly Independent.'
          ],
          keyConcept: 'A single non-zero vector {v ≠ 0} is always linearly independent.'
        }
      },
      {
        id: 11,
        question: 'If y = xˣ, then dy/dx is equal to:',
        options: ['xˣ(1 + ln x)', 'xˣ(ln x)', 'xˣ⁻¹(1 + ln x)', 'xˣ(1 - ln x)'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Take natural logarithm on both sides: ln y = x · ln x',
            'Differentiate both sides with respect to x: (1/y) dy/dx = 1 · ln x + x · (1/x) = ln x + 1',
            'Multiply by y: dy/dx = y(1 + ln x) = xˣ(1 + ln x).'
          ],
          keyConcept: 'Logarithmic differentiation: d/dx [u(x)ᵛ⁽ˣ⁾] = uᵛ · [v\' ln u + v u\'/u].'
        }
      },
      {
        id: 12,
        question: 'The derivative of ln(sin x) with respect to x is:',
        options: ['cot x', 'csc x', '1/sin x', 'cot x + csc x'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Let y = ln(sin x).',
            'By chain rule: dy/dx = (1 / sin x) · d/dx (sin x) = (1 / sin x) · cos x = cot x.'
          ],
          keyConcept: 'd/dx [ln(f(x))] = f\'(x) / f(x).'
        }
      },
      {
        id: 13,
        question: 'If x = cos t and y = sin t, then dy/dx is:',
        options: ['cot t', '-cot t', '-tan t', 'tan t'],
        correctIndex: 1,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'dx/dt = -sin t',
            'dy/dt = cos t',
            'dy/dx = (dy/dt) / (dx/dt) = (cos t) / (-sin t) = -cot t.'
          ],
          keyConcept: 'Parametric differentiation: dy/dx = (dy/dt) / (dx/dt).'
        }
      },
      {
        id: 14,
        question: 'The value of the definite integral ∫₀^(π/2) sin² x dx is:',
        options: ['π/2', 'π/4', '1', '2'],
        correctIndex: 1,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Use the identity sin² x = (1 - cos 2x) / 2.',
            '∫₀^(π/2) (1 - cos 2x)/2 dx = [x/2 - (sin 2x)/4]₀^(π/2)',
            '= (π/4 - 0) - (0 - 0) = π/4.'
          ],
          keyConcept: 'Wallis Formula / Standard definite integral: ∫₀^(π/2) sin² x dx = π/4.'
        }
      },
      {
        id: 15,
        question: 'If I = ∫ x eˣ dx, then I equals:',
        options: ['eˣ(x - 1) + C', 'eˣ(x + 1) + C', 'x eˣ + C', 'eˣ + C'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Apply Integration by Parts: ∫ u v\' dx = u v - ∫ u\' v dx',
            'Let u = x (so u\' = 1) and v\' = eˣ (so v = eˣ).',
            'I = x eˣ - ∫ 1 · eˣ dx = x eˣ - eˣ + C = eˣ(x - 1) + C.'
          ],
          keyConcept: 'Integration by parts: ∫ x eˣ dx = eˣ(x - 1) + C.'
        }
      },
      {
        id: 16,
        question: 'If f(x) = |x|, then f\'(0):',
        options: ['Exists and is 0', 'Exists and is 1', 'Does not exist', 'Exists and is -1'],
        correctIndex: 2,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Left Hand Derivative: lim_{h → 0⁻} (|-h| - 0) / (-h) = h / (-h) = -1.',
            'Right Hand Derivative: lim_{h → 0⁺} (|h| - 0) / h = h / h = +1.',
            'Since LHD (-1) ≠ RHD (+1), f\'(0) does not exist.'
          ],
          keyConcept: 'The absolute value function f(x) = |x| is continuous everywhere but not differentiable at x = 0.'
        }
      },
      {
        id: 17,
        question: 'If f(x) = e^(ln(sin x)) for 0 < x < π, then f\'(x) equals:',
        options: ['cot x · sin x', 'cos x', 'cot x', 'sin x · ln(sin x)'],
        correctIndex: 1,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'By the inverse property of exponential and natural log: e^(ln(u)) = u for u > 0.',
            'Since sin x > 0 for 0 < x < π, f(x) = sin x.',
            'Thus, f\'(x) = d/dx (sin x) = cos x.'
          ],
          keyConcept: 'e^(ln(f(x))) simplifies to f(x).'
        }
      },
      {
        id: 18,
        question: 'If I = ∫₀¹ x eˣ dx, then I =',
        options: ['e - 1', '1', 'e', 'e + 1'],
        correctIndex: 1,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'We know ∫ x eˣ dx = eˣ(x - 1).',
            'Evaluate between 0 and 1: [eˣ(x - 1)]₀¹',
            'At x = 1: e¹(1 - 1) = 0.',
            'At x = 0: e⁰(0 - 1) = 1 · (-1) = -1.',
            'I = 0 - (-1) = 1.'
          ],
          keyConcept: 'Definite integral evaluation: [eˣ(x - 1)]₀¹ = 0 - (-1) = 1.'
        }
      },
      {
        id: 19,
        question: 'If x = cos t and y = sin³ t, then dy/dx is:',
        options: ['-3 sin² t', '-3 sin² t tan t', '-3 sin² t cot t', '3 sin² t cos t'],
        correctIndex: 2,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'dx/dt = -sin t',
            'dy/dt = 3 sin² t · cos t',
            'dy/dx = (3 sin² t · cos t) / (-sin t) = -3 sin² t · (cos t / sin t) = -3 sin² t cot t.'
          ],
          keyConcept: 'Parametric derivative with trigonometric simplification.'
        }
      },
      {
        id: 20,
        question: 'If y = ln(ln x), then dy/dx =',
        options: ['1 / (x ln x)', '1 / (x (ln x)²)', '1 / (ln x)²', 'None of these'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Let u = ln x, then y = ln u.',
            'dy/dx = (dy/du) · (du/dx) = (1 / u) · (1 / x) = (1 / ln x) · (1 / x) = 1 / (x ln x).'
          ],
          keyConcept: 'Chain rule: d/dx [ln(ln x)] = 1 / (x ln x).'
        }
      },
      {
        id: 21,
        question: 'The coefficient of (x - π/2)⁴ in the Taylor series expansion of sin x about x = π/2 is:',
        options: ['1/24', '1/120', '-1/24', '0'],
        correctIndex: 0,
        topic: 'Taylor Series',
        explanation: {
          steps: [
            'Taylor series formula: f(x) = Σ [fⁿ(a) / n!] (x - a)ⁿ.',
            'For f(x) = sin x at a = π/2:',
            'f(π/2) = 1, f\'(π/2) = cos(π/2) = 0, f\'\'(π/2) = -sin(π/2) = -1, f\'\'\'(π/2) = -cos(π/2) = 0, f⁽⁴⁾(π/2) = sin(π/2) = 1.',
            'Coefficient of (x - π/2)⁴ is f⁽⁴⁾(π/2) / 4! = 1 / 24.'
          ],
          keyConcept: 'Taylor coefficient formula: cₙ = f⁽ⁿ⁾(a) / n!.'
        }
      },
      {
        id: 22,
        question: 'The Maclaurin series expansion of eˣ about x = 0 is:',
        options: [
          '1 + x/1! + x²/2! + x³/3! + ...',
          'x/1! - x³/3! + x⁵/5! - ...',
          'x/1! + x³/3! + x⁵/5! + ...',
          '1 - x²/2! + x⁴/4! - ...'
        ],
        correctIndex: 0,
        topic: 'Taylor Series',
        explanation: {
          steps: [
            'For f(x) = eˣ, f⁽ⁿ⁾(0) = 1 for all n ≥ 0.',
            'Maclaurin expansion: eˣ = Σ [xⁿ / n!] = 1 + x + x²/2! + x³/3! + ...'
          ],
          keyConcept: 'Standard Maclaurin series for exponential function.'
        }
      },
      {
        id: 23,
        question: 'For the function f(x) = 1 - |x| over the interval [-1, 1], which of the following is true?',
        options: [
          'There exists some c ∈ (-1, 1) such that f\'(c) = 0',
          'There exists some c ∈ (-1, 1) such that f\'(c) = [f(1) - f(-1)]/2',
          'There does not exist any c ∈ (-1, 1) such that f\'(c) = 0',
          'None of these'
        ],
        correctIndex: 2,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'f(x) = 1 + x for x < 0 (f\'(x) = +1).',
            'f(x) = 1 - x for x > 0 (f\'(x) = -1).',
            'At x = 0, f is not differentiable. Hence f\'(x) is either +1 or -1, and is never 0.',
            'Therefore, there does not exist any c ∈ (-1, 1) with f\'(c) = 0.'
          ],
          keyConcept: 'Rolle\'s theorem requires differentiability on the open interval (a, b).'
        }
      },
      {
        id: 24,
        question: 'The value of c in Rolle\'s theorem for the function f(x) = sin x in [0, π] is:',
        options: ['π/2', '0', '2', 'π'],
        correctIndex: 0,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            '1. f(0) = sin 0 = 0 and f(π) = sin π = 0 (f(a) = f(b)).',
            '2. f(x) is continuous on [0, π] and differentiable on (0, π).',
            '3. By Rolle\'s theorem, f\'(c) = cos c = 0.',
            'In (0, π), cos c = 0 gives c = π/2.'
          ],
          keyConcept: 'Rolle\'s theorem: f\'(c) = 0 for some c ∈ (a, b).'
        }
      },
      {
        id: 25,
        question: 'For any second-degree polynomial f(x) with two real unequal roots r₁ and r₂, the relation between Rolle\'s point c and the roots is:',
        options: [
          'They are independent of each other',
          'c = r₁ - r₂',
          'c = (r₁ + r₂) / 2',
          'c = r₁ · r₂'
        ],
        correctIndex: 2,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'Let f(x) = a(x - r₁)(x - r₂) = a(x² - (r₁ + r₂)x + r₁r₂).',
            'f\'(x) = a(2x - (r₁ + r₂)).',
            'Setting f\'(c) = 0 gives 2c - (r₁ + r₂) = 0 ⇒ c = (r₁ + r₂) / 2.',
            'The Rolle point of a quadratic is the arithmetic mean of its roots.'
          ],
          keyConcept: 'For any parabola f(x) = a x² + b x + c, the stationary point is at the midpoint of roots.'
        }
      },
      {
        id: 26,
        question: 'For all real values of x, the minimum value of |x + 2| - 1 is:',
        options: ['0', '1', '2', '-1'],
        correctIndex: 3,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Since |x + 2| ≥ 0 for all x ∈ ℝ, the smallest possible value of |x + 2| is 0 (which occurs at x = -2).',
            'Therefore, the minimum value of |x + 2| - 1 is 0 - 1 = -1.'
          ],
          keyConcept: 'Absolute value minimum is 0, so f_min = 0 - 1 = -1.'
        }
      },
      {
        id: 27,
        question: 'The first and second derivatives of a quadratic polynomial at x = 1 are 1 and 2 respectively. The value of f(1) - f(0) is:',
        options: ['3/2', '1/2', '0', '1'],
        correctIndex: 2,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Let f(x) = a x² + b x + c.',
            'f\'(x) = 2ax + b, f\'\'(x) = 2a.',
            'Given f\'\'(1) = 2 ⇒ 2a = 2 ⇒ a = 1.',
            'Given f\'(1) = 1 ⇒ 2(1)(1) + b = 1 ⇒ b = -1.',
            'f(1) - f(0) = [1(1)² + (-1)(1) + c] - [c] = (1 - 1 + c) - c = 0.'
          ],
          keyConcept: 'Direct algebraic evaluation from Taylor expansion: f(1) - f(0) = f\'(1) - f\'\'(1)/2 = 1 - 2/2 = 0.'
        }
      },
      {
        id: 28,
        question: 'The point on the curve x² = 2y which is nearest to the point (0, 5) is:',
        options: ['(0, 0)', '(1, 1)', '(2√2, 4)', '(2√2, 0)'],
        correctIndex: 2,
        topic: 'Extrema & Applications',
        explanation: {
          steps: [
            'Distance squared D = (x - 0)² + (y - 5)² = x² + (y - 5)²',
            'Substitute x² = 2y: D(y) = 2y + (y - 5)² = y² - 8y + 25.',
            'dD/dy = 2y - 8 = 0 ⇒ y = 4.',
            'For y = 4: x² = 2(4) = 8 ⇒ x = ±2√2.',
            'Thus the nearest points are (±2√2, 4).'
          ],
          keyConcept: 'Minimizing distance squared by parameter substitution.'
        }
      },
      {
        id: 29,
        question: 'The limit lim_{x → 0} (x - sin x) / x³ is equal to:',
        options: ['1/12', '1/3', '1/2', '1/6'],
        correctIndex: 3,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'Use Taylor series: sin x = x - x³/3! + x⁵/5! - ... = x - x³/6 + ...',
            'Numerator: x - (x - x³/6 + ...) = x³/6 + O(x⁵).',
            'Limit: lim_{x → 0} (x³/6) / x³ = 1/6.'
          ],
          keyConcept: 'Standard indeterminate form 0/0 solved via Taylor expansion or L\'Hôpital\'s Rule.'
        }
      },
      {
        id: 30,
        question: 'The limit lim_{x → 0} (x² + 2cos x - 2) / (sin x) is equal to:',
        options: ['0', '1', '-1', '∞'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'Check form at x = 0: (0 + 2(1) - 2) / 0 = 0/0.',
            'Apply L\'Hôpital\'s Rule: d/dx (x² + 2cos x - 2) = 2x - 2sin x, and d/dx (sin x) = cos x.',
            'lim_{x → 0} (2x - 2sin x) / (cos x) = (0 - 0) / 1 = 0 / 1 = 0.'
          ],
          keyConcept: 'Application of L\'Hôpital\'s Rule for 0/0 form.'
        }
      }
    ]
  },
  {
    id: 'mth165-midterm-mock-2',
    code: '25261MTH53683',
    title: 'Midterm Examination • Paper 2 (Official University PYQ)',
    courseCode: 'MTH165',
    courseName: 'Mathematics for Engineers',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['Matrix Rank', 'Inconsistent Systems', 'Eigenvectors', 'Implicit Differentiation', 'Integrals', 'Lagrange MVT'],
    description: 'Direct university midterm paper testing matrix rank, inconsistency conditions, eigenvector computation, and definite integrals.',
    questions: [
      {
        id: 1,
        question: 'The rank of the matrix [[1, 1, 6], [0, 4, 3], [1, 5, 9], [1, 9, 12]] is:',
        options: ['1', '2', '3', '4'],
        correctIndex: 1,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'Row 1: [1, 1, 6], Row 2: [0, 4, 3]',
            'Row 3 = Row 1 + Row 2 = [1+0, 1+4, 6+3] = [1, 5, 9] (linearly dependent on R1 and R2).',
            'Row 4 = Row 1 + 2 · Row 2 = [1+0, 1+8, 6+6] = [1, 9, 12] (linearly dependent on R1 and R2).',
            'Only 2 rows are linearly independent, so the rank is 2.'
          ],
          keyConcept: 'Rank is the number of non-zero rows in row echelon form.'
        }
      },
      {
        id: 2,
        question: 'The system of equations 2x₁ - 5x₂ + 2x₃ = 8, 2x₁ + 4x₂ + 6x₃ = 5, and x₁ + 2x₂ + ax₃ = b is INCONSISTENT for what values of a and b?',
        options: ['a = 3, b = 5/2', 'a ≠ 3, b ≠ 5/2', 'a = 3, b ≠ 5/2', 'a ≠ 3, b = 5/2'],
        correctIndex: 2,
        topic: 'Linear Systems',
        explanation: {
          steps: [
            'Notice that Equation 2 is: 2(x₁ + 2x₂ + 3x₃) = 5 ⇒ x₁ + 2x₂ + 3x₃ = 5/2.',
            'Equation 3 is: x₁ + 2x₂ + ax₃ = b.',
            'For the LHS to be parallel/identical: a = 3.',
            'For inconsistency (contradiction between LHS and RHS): b ≠ 5/2.',
            'Thus, the system is inconsistent for a = 3 and b ≠ 5/2.'
          ],
          keyConcept: 'A linear system is inconsistent when parallel equations have contradictory constants.'
        }
      },
      {
        id: 3,
        question: 'A singular matrix A with order 4 × 4 is:',
        options: [
          'Invertible and has rank 4',
          'Invertible and has rank less than 4',
          'Not invertible and has rank 4',
          'Not invertible and has rank less than 4'
        ],
        correctIndex: 3,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'By definition, a singular matrix has det(A) = 0.',
            'Since det(A) = 0, A is NOT invertible (A⁻¹ does not exist).',
            'Full rank of a 4×4 matrix is 4. When det(A) = 0, rank(A) must be strictly less than 4.'
          ],
          keyConcept: 'Singular matrix ⇔ det(A) = 0 ⇔ Non-invertible ⇔ Rank < n.'
        }
      },
      {
        id: 4,
        question: 'The system of equations x₁ + x₂ - x₃ + x₄ = 2, 2x₂ + 4x₃ + 2x₄ = 3, and 2x₁ + 4x₂ + 2x₃ + 4x₄ = 7 has:',
        options: ['Unique solution only', 'Trivial solution', 'No solution only', 'Infinite solutions only'],
        correctIndex: 3,
        topic: 'Linear Systems',
        explanation: {
          steps: [
            'Multiply Eq 1 by 2: 2x₁ + 2x₂ - 2x₃ + 2x₄ = 4.',
            'Add Eq 2 (2x₂ + 4x₃ + 2x₄ = 3): (2x₁ + 2x₂ - 2x₃ + 2x₄) + (2x₂ + 4x₃ + 2x₄) = 2x₁ + 4x₂ + 2x₃ + 4x₄ = 7.',
            'This exactly equals Eq 3! Hence Eq 3 is a linear combination of Eq 1 and Eq 2.',
            'Number of independent equations = 2 < 4 variables, so the system is consistent with Infinite Solutions.'
          ],
          keyConcept: 'Rank(A) = Rank([A|B]) = 2 < 4 variables ⇒ Infinitely many solutions.'
        }
      },
      {
        id: 5,
        question: 'The eigenvector for eigenvalue λ = 12 of the matrix [[-2, 5, 4], [5, 7, 5], [4, 5, -2]] is:',
        options: ['{1, 2, 1}', '{2, 2, 1}', '{1, 1, 2}', '{1, 2, 2}'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Solve (A - 12I)X = 0.',
            'A - 12I = [[-14, 5, 4], [5, -5, 5], [4, 5, -14]].',
            'Test candidate vector X = [1, 2, 1]ᵀ:',
            'Row 1: -14(1) + 5(2) + 4(1) = -14 + 10 + 4 = 0.',
            'Row 2: 5(1) - 5(2) + 5(1) = 5 - 10 + 5 = 0.',
            'Row 3: 4(1) + 5(2) - 14(1) = 4 + 10 - 14 = 0.',
            'Therefore, {1, 2, 1} is the eigenvector.'
          ],
          keyConcept: 'An eigenvector X for eigenvalue λ satisfies AX = λX.'
        }
      },
      {
        id: 6,
        question: 'If a square matrix A of order 3 × 3 has eigenvalues -1, 0, and 3, then the rank of matrix A is:',
        options: ['Rank(A) = 3', 'Rank(A) = 2', 'Rank(A) < 3', 'Rank(A) < 2'],
        correctIndex: 1,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Property: For a diagonalizable matrix, rank equals the number of non-zero eigenvalues.',
            'Eigenvalues are -1 (non-zero), 0 (zero), and 3 (non-zero).',
            'There are exactly 2 non-zero eigenvalues, so Rank(A) = 2.'
          ],
          keyConcept: 'The rank of a matrix equals the number of its non-zero eigenvalues (when diagonalizable).'
        }
      },
      {
        id: 7,
        question: 'The eigenvalues of the matrix [[5, 4], [1, 2]] are:',
        options: ['-1 and -6', '-1 and 6', '1 and -6', '1 and 6'],
        correctIndex: 3,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Characteristic equation: det(A - λI) = (5 - λ)(2 - λ) - (4)(1) = 0',
            'λ² - 7λ + 10 - 4 = 0 ⇒ λ² - 7λ + 6 = 0',
            '(λ - 1)(λ - 6) = 0 ⇒ λ = 1, 6.'
          ],
          keyConcept: 'Roots of λ² - tr(A)λ + det(A) = 0.'
        }
      },
      {
        id: 8,
        question: 'If a, b, c are eigenvalues of the matrix [[2, 1, 1], [0, 1, 0], [1, 1, 2]], then a + b + c is equal to:',
        options: ['2', '3', '4', '5'],
        correctIndex: 3,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'The sum of eigenvalues a + b + c equals the trace of the matrix tr(A).',
            'tr(A) = a₁₁ + a₂₂ + a₃₃ = 2 + 1 + 2 = 5.',
            'Thus, a + b + c = 5.'
          ],
          keyConcept: 'Sum of eigenvalues = Trace of matrix.'
        }
      },
      {
        id: 9,
        question: 'The inverse of [[1, 2, -2], [-1, 3, 0], [0, -2, 1]] is [[3, 2, 6], [1, 1, k], [2, 2, 5]], then k is:',
        options: ['1', '2', '-2', '3'],
        correctIndex: 1,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'Multiply Row 2 of A: [-1, 3, 0] by Column 3 of A⁻¹: [6, k, 5]ᵀ.',
            '(-1)(6) + (3)(k) + (0)(5) = 0 (since it is off-diagonal entry of I).',
            '-6 + 3k = 0 ⇒ 3k = 6 ⇒ k = 2.'
          ],
          keyConcept: 'A · A⁻¹ = I; row i × column j = 0 for i ≠ j.'
        }
      },
      {
        id: 10,
        question: 'The inverse of the matrix A = [[2, 1, 1], [0, 1, 0], [1, 1, 2]] using Cayley-Hamilton theorem is:',
        options: [
          'A⁻¹ = 1/3 [A² - 5A + 7I]',
          'A⁻¹ = 1/2 [A² - 5A + 7I]',
          'A⁻¹ = 1/3 [A² + 5A + 7I]',
          'A⁻¹ = 1/3 [A² - 5A - 7I]'
        ],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Characteristic equation: λ³ - 5λ² + 7λ - 3 = 0.',
            'By Cayley-Hamilton: A³ - 5A² + 7A - 3I = 0.',
            'Multiply throughout by A⁻¹: A² - 5A + 7I - 3A⁻¹ = 0.',
            '3A⁻¹ = A² - 5A + 7I ⇒ A⁻¹ = 1/3 [A² - 5A + 7I].'
          ],
          keyConcept: 'Using Cayley-Hamilton to find matrix inverses.'
        }
      },
      {
        id: 11,
        question: 'What is the derivative of the function f(x) = 3x² + 6x - 4 with respect to x?',
        options: ['6x - 6', '6x + 6', 'x + 6', '6x'],
        correctIndex: 1,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'f(x) = 3x² + 6x - 4',
            'f\'(x) = 3 · (2x) + 6 · (1) - 0 = 6x + 6.'
          ],
          keyConcept: 'Power rule: d/dx (xⁿ) = n xⁿ⁻¹.'
        }
      },
      {
        id: 12,
        question: 'What is the differentiation of f(x) = x³ sin x with respect to x?',
        options: ['3x² sin x + x³ cos x', '3x² sin x - x³ cos x', '3x² sin x + x² cos x', 'None of these'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Use Product Rule: (uv)\' = u\'v + uv\'',
            'Let u = x³ (u\' = 3x²) and v = sin x (v\' = cos x).',
            'f\'(x) = 3x² sin x + x³ cos x.'
          ],
          keyConcept: 'Product rule of differentiation.'
        }
      },
      {
        id: 13,
        question: 'Find dy/dx if x = a t² and y = 2a t:',
        options: ['t', '1 / (2t)', '1/t', '2/t'],
        correctIndex: 2,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'dx/dt = 2at',
            'dy/dt = 2a',
            'dy/dx = (dy/dt) / (dx/dt) = (2a) / (2at) = 1/t.'
          ],
          keyConcept: 'Parametric differentiation of parabola equations.'
        }
      },
      {
        id: 14,
        question: 'Find dy/dx if y = x³ + sec² x:',
        options: ['6x - 2 sec² x tan x', '6x + 2 sec² x tan x', '6x + sec² x tan x', '3x² + 2 sec² x tan x'],
        correctIndex: 3,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'd/dx (x³) = 3x²',
            'd/dx (sec² x) = 2 sec x · d/dx (sec x) = 2 sec x · (sec x tan x) = 2 sec² x tan x',
            'dy/dx = 3x² + 2 sec² x tan x.'
          ],
          keyConcept: 'Chain rule: d/dx [u²] = 2u · u\'.'
        }
      },
      {
        id: 15,
        question: 'Find dy/dx if 2x + 3y = sin y:',
        options: ['2 / (cos y - 3)', '2 / (cos y + 3)', '2 / (cos y - 1)', '2 / (2cos y - 3)'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Differentiate both sides with respect to x: 2 + 3(dy/dx) = cos y · (dy/dx)',
            'Group dy/dx terms: 2 = (cos y - 3) dy/dx',
            'dy/dx = 2 / (cos y - 3).'
          ],
          keyConcept: 'Implicit differentiation.'
        }
      },
      {
        id: 16,
        question: 'Find dy/dx if y = log(x³ - x⁴):',
        options: [
          '(2 - 4x) / [x(1 - x)]',
          '(3 - 4x) / [x(1 + x)]',
          '(3 + 4x) / [x(1 - x)]',
          '(3 - 4x) / [x(1 - x)]'
        ],
        correctIndex: 3,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'dy/dx = 1 / (x³ - x⁴) · d/dx (x³ - x⁴)',
            '= (3x² - 4x³) / (x³ - x⁴)',
            'Factor out x² from numerator and denominator: [x²(3 - 4x)] / [x² · x(1 - x)] = (3 - 4x) / [x(1 - x)].'
          ],
          keyConcept: 'Logarithmic chain rule with algebraic factorization.'
        }
      },
      {
        id: 17,
        question: 'Evaluate the integral ∫ sin³ x cos² x dx:',
        options: [
          '-1/3 cos³ x - 1/5 cos⁵ x + C',
          '-1/3 cos³ x + 1/5 cos⁵ x + C',
          '1/3 cos³ x + 1/5 cos⁵ x + C',
          'None of these'
        ],
        correctIndex: 1,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Rewrite sin³ x as (1 - cos² x) sin x.',
            '∫ (1 - cos² x) cos² x (sin x dx) = ∫ (cos² x - cos⁴ x) sin x dx.',
            'Let u = cos x, so du = -sin x dx.',
            '-∫ (u² - u⁴) du = -[u³/3 - u⁵/5] + C = -1/3 cos³ x + 1/5 cos⁵ x + C.'
          ],
          keyConcept: 'Trigonometric integration using substitution u = cos x.'
        }
      },
      {
        id: 18,
        question: 'Evaluate the integral ∫ 1 / [x(x + 1)] dx:',
        options: [
          'log x + log(1 + x)',
          'log x - log(1 + x)',
          'log x - log(1 - x)',
          'log x + log(1 - x)'
        ],
        correctIndex: 1,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Use partial fractions: 1 / [x(x + 1)] = 1/x - 1/(x + 1).',
            '∫ [1/x - 1/(x + 1)] dx = log |x| - log |x + 1| + C.'
          ],
          keyConcept: 'Partial fraction decomposition.'
        }
      },
      {
        id: 19,
        question: 'Evaluate the integral ∫ eˣ sin x dx:',
        options: [
          'eˣ/2 (sin x + cos x) + C',
          'eˣ/2 (-sin x - cos x) + C',
          'eˣ/2 (sin x - cos x) + C',
          '-eˣ/2 (sin x - cos x) + C'
        ],
        correctIndex: 2,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Standard standard integral formula: ∫ eᵃˣ sin(bx) dx = [eᵃˣ / (a² + b²)] (a sin bx - b cos bx) + C.',
            'Here a = 1, b = 1:',
            'I = [eˣ / (1² + 1²)] (1 · sin x - 1 · cos x) + C = eˣ/2 (sin x - cos x) + C.'
          ],
          keyConcept: 'Standard reduction integral for eᵃˣ sin bx.'
        }
      },
      {
        id: 20,
        question: 'Evaluate the definite integral ∫₀¹ [tan⁻¹ x / (1 + x²)] dx:',
        options: ['π² / 33', 'π² / 32', 'π² / 34', 'None of these'],
        correctIndex: 1,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Let u = tan⁻¹ x, so du = 1/(1 + x²) dx.',
            'Limits: at x = 0, u = 0; at x = 1, u = π/4.',
            '∫₀^(π/4) u du = [u² / 2]₀^(π/4) = (π/4)² / 2 = (π² / 16) / 2 = π² / 32.'
          ],
          keyConcept: 'Substitution method for definite integrals.'
        }
      },
      {
        id: 21,
        question: 'Which of the following is a NECESSARY condition for Rolle\'s Theorem to apply to a function f on [a, b]?',
        options: [
          'f is differentiable on [a, b]',
          'f is continuous on [a, b]',
          'f is continuous on (a, b)',
          'f\'(a) = f\'(b)'
        ],
        correctIndex: 1,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'The three standard hypotheses of Rolle\'s Theorem are:',
            '1. f is continuous on the CLOSED interval [a, b].',
            '2. f is differentiable on the OPEN interval (a, b).',
            '3. f(a) = f(b).'
          ],
          keyConcept: 'Continuity on [a, b] is a necessary hypothesis of Rolle\'s theorem.'
        }
      },
      {
        id: 22,
        question: 'Find the number of distinct points c in (0, 2π) for f(x) = sin 2x satisfying Rolle\'s theorem:',
        options: ['1', '2', '3', '4'],
        correctIndex: 3,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'f(0) = sin 0 = 0 and f(2π) = sin 4π = 0.',
            'f\'(x) = 2 cos 2x = 0 ⇒ cos 2x = 0.',
            '2x ∈ {π/2, 3π/2, 5π/2, 7π/2} (since x ∈ (0, 2π) ⇒ 2x ∈ (0, 4π)).',
            'x ∈ {π/4, 3π/4, 5π/4, 7π/4}.',
            'There are exactly 4 distinct points.'
          ],
          keyConcept: 'Roots of derivative in periodic intervals.'
        }
      },
      {
        id: 23,
        question: 'Using Lagrange Mean Value Theorem on [0, 1], find the value of c where f(x) = eˣ:',
        options: ['c = ln(e - 1)', 'c = ln(e)', 'c = ln(e + 1)', 'c = 1 / ln(e)'],
        correctIndex: 0,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'Lagrange MVT: f\'(c) = [f(1) - f(0)] / (1 - 0).',
            'f\'(c) = eᶜ, f(1) = e, f(0) = 1.',
            'eᶜ = (e - 1) / 1 = e - 1.',
            'Take natural log: c = ln(e - 1).'
          ],
          keyConcept: 'Lagrange MVT formula: f\'(c) = [f(b) - f(a)] / (b - a).'
        }
      },
      {
        id: 24,
        question: 'Using Lagrange Mean Value Theorem on [0, 1], find the value of c where f(x) = tan⁻¹ x:',
        options: ['c = √(2/π - 1)', 'c = √(4/π + 1)', 'c = √(4/π - 1)', 'c = √(2/π + 1)'],
        correctIndex: 2,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'f\'(c) = 1 / (1 + c²).',
            '[f(1) - f(0)] / (1 - 0) = [tan⁻¹(1) - tan⁻¹(0)] / 1 = π/4 - 0 = π/4.',
            '1 / (1 + c²) = π/4 ⇒ 1 + c² = 4/π ⇒ c² = 4/π - 1 ⇒ c = √(4/π - 1).'
          ],
          keyConcept: 'Application of LMVT on inverse trigonometric functions.'
        }
      },
      {
        id: 25,
        question: 'The limit lim_{x → ∞} (x + sin x) / x equals:',
        options: ['0', '1', '∞', 'Does not exist'],
        correctIndex: 1,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            '(x + sin x) / x = 1 + (sin x) / x.',
            'Since -1 ≤ sin x ≤ 1, by Squeeze Theorem, lim_{x → ∞} (sin x) / x = 0.',
            'Therefore, limit = 1 + 0 = 1.'
          ],
          keyConcept: 'Squeeze theorem for oscillatory trigonometric functions at infinity.'
        }
      },
      {
        id: 26,
        question: 'The limit lim_{x → ∞} (√(x² + x) - x) equals:',
        options: ['0', '1/2', '-1/2', 'Does not exist'],
        correctIndex: 1,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'Multiply and divide by conjugate (√(x² + x) + x):',
            'Numerator: (x² + x) - x² = x.',
            'Denominator: √(x² + x) + x = x(√(1 + 1/x) + 1).',
            'lim_{x → ∞} x / [x(√(1 + 1/x) + 1)] = 1 / (√1 + 1) = 1/2.'
          ],
          keyConcept: 'Conjugate rationalization for ∞ - ∞ algebraic limits.'
        }
      },
      {
        id: 27,
        question: 'The limit lim_{x → ∞} x · tan(1/x) equals:',
        options: ['0', '1', '∞', 'Does not exist'],
        correctIndex: 1,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'Let u = 1/x. As x → ∞, u → 0⁺.',
            'lim_{x → ∞} x · tan(1/x) = lim_{u → 0} tan(u) / u = 1.'
          ],
          keyConcept: 'Substitution u = 1/x transforms limit at infinity into standard fundamental limit.'
        }
      },
      {
        id: 28,
        question: 'Find the maximum value of sin² x · cos² x:',
        options: ['0', '0.25', '0.5', '1'],
        correctIndex: 1,
        topic: 'Extrema & Applications',
        explanation: {
          steps: [
            'sin² x cos² x = (sin x cos x)² = [(1/2) sin 2x]² = 1/4 sin² 2x.',
            'Since the maximum value of sin² 2x is 1, the maximum value is 1/4 · 1 = 0.25.'
          ],
          keyConcept: 'Trigonometric power reduction.'
        }
      },
      {
        id: 29,
        question: 'Find the minimum value of x² + 1/x² for x ∈ ℝ, x ≠ 0:',
        options: ['0', '1', '2', '4'],
        correctIndex: 2,
        topic: 'Extrema & Applications',
        explanation: {
          steps: [
            'By AM-GM inequality for positive real numbers x² and 1/x²:',
            '(x² + 1/x²) / 2 ≥ √(x² · 1/x²) = 1.',
            'x² + 1/x² ≥ 2.',
            'Equality occurs at x² = 1 (x = ±1).'
          ],
          keyConcept: 'AM-GM Inequality: a + 1/a ≥ 2 for a > 0.'
        }
      },
      {
        id: 30,
        question: 'If f(x) = x / (1 + x²), then the maximum value of f(x) is:',
        options: ['0', '0.25', '0.5', '1'],
        correctIndex: 2,
        topic: 'Extrema & Applications',
        explanation: {
          steps: [
            'f\'(x) = [1(1 + x²) - x(2x)] / (1 + x²)² = (1 - x²) / (1 + x²)².',
            'Set f\'(x) = 0 ⇒ 1 - x² = 0 ⇒ x = 1 (for maximum).',
            'Maximum value: f(1) = 1 / (1 + 1²) = 1/2 = 0.5.'
          ],
          keyConcept: 'Stationary point derivative test for rational functions.'
        }
      }
    ]
  },
  {
    id: 'mth165-midterm-mock-3',
    code: '25261MTH-MOCK3',
    title: 'Midterm Examination • Mock 3 (High-Yield Standard Prep)',
    courseCode: 'MTH165',
    courseName: 'Mathematics for Engineers',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Exam Standard',
    topics: ['Row Echelon Form', 'Characteristic Roots', 'Leibnitz Rule', 'Mean Value Theorems', 'Taylor Series', 'Definite Integrals'],
    description: 'Comprehensive high-yield mock exam targeting high-frequency examination question patterns, tricky negative marking traps, and core proofs.',
    questions: [
      {
        id: 1,
        question: 'What is the rank of the zero matrix of order 3 × 3?',
        options: ['3', '1', '0', 'Undefined'],
        correctIndex: 2,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'By definition, the rank of a matrix is the number of linearly independent rows or columns.',
            'A matrix with all zero entries has no non-zero rows.',
            'Therefore, the rank of any zero matrix is 0.'
          ],
          keyConcept: 'Rank(0) = 0.'
        }
      },
      {
        id: 2,
        question: 'If A is an orthogonal matrix, then det(A) is always:',
        options: ['0', '±1', 'Any real number', 'Always 1'],
        correctIndex: 1,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'For an orthogonal matrix, A Aᵀ = I.',
            'det(A Aᵀ) = det(A) · det(Aᵀ) = [det(A)]² = det(I) = 1.',
            'Taking square root gives det(A) = ±1.'
          ],
          keyConcept: 'Determinant of an orthogonal matrix is ±1.'
        }
      },
      {
        id: 3,
        question: 'The eigenvalues of a skew-symmetric matrix are always:',
        options: ['Purely real', 'Purely imaginary or zero', 'Always positive', 'Always 1'],
        correctIndex: 1,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'For a real skew-symmetric matrix Aᵀ = -A.',
            'If λ is an eigenvalue with eigenvector X, then X* A X is purely imaginary.',
            'Hence, λ must be either purely imaginary (i k) or zero.'
          ],
          keyConcept: 'Eigenvalues of real skew-symmetric matrices lie entirely on the imaginary axis.'
        }
      },
      {
        id: 4,
        question: 'If A is an idempotent matrix (A² = A), its eigenvalues can only be:',
        options: ['-1 or 1', '0 or 1', 'Any integer', '0 only'],
        correctIndex: 1,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Let AX = λX. Then A²X = A(λX) = λ(AX) = λ²X.',
            'Since A² = A, we have λ²X = λX ⇒ (λ² - λ)X = 0.',
            'Since X ≠ 0, λ² - λ = 0 ⇒ λ(λ - 1) = 0 ⇒ λ = 0 or 1.'
          ],
          keyConcept: 'Idempotent matrix eigenvalues are either 0 or 1.'
        }
      },
      {
        id: 5,
        question: 'If y = sin(ax + b), the n-th derivative yₙ is:',
        options: [
          'aⁿ sin(ax + b + nπ/2)',
          'aⁿ cos(ax + b + nπ/2)',
          'aⁿ sin(ax + b)',
          '(-1)ⁿ aⁿ sin(ax + b)'
        ],
        correctIndex: 0,
        topic: 'Successive Differentiation',
        explanation: {
          steps: [
            'y₁ = a cos(ax + b) = a sin(ax + b + π/2)',
            'y₂ = a² cos(ax + b + π/2) = a² sin(ax + b + 2 · π/2)',
            'By mathematical induction: yₙ = aⁿ sin(ax + b + nπ/2).'
          ],
          keyConcept: 'Standard formula for n-th derivative of sine.'
        }
      },
      {
        id: 6,
        question: 'The value of c in Cauchy\'s Mean Value Theorem for f(x) = eˣ and g(x) = e⁻ˣ in [a, b] is:',
        options: ['(a + b) / 2', '√(ab)', '(a - b) / 2', 'ab / (a + b)'],
        correctIndex: 0,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'Cauchy MVT: [f\'(c)] / [g\'(c)] = [f(b) - f(a)] / [g(b) - g(a)].',
            'f\'(c) = eᶜ, g\'(c) = -e⁻ᶜ ⇒ f\'(c)/g\'(c) = -e²ᶜ.',
            '[eᵇ - eᵃ] / [e⁻ᵇ - e⁻ᵃ] = [eᵇ - eᵃ] / [(eᵃ - eᵇ)/(eᵃ eᵇ)] = -eᵃ⁺ᵇ.',
            '-e²ᶜ = -eᵃ⁺ᵇ ⇒ 2c = a + b ⇒ c = (a + b) / 2.'
          ],
          keyConcept: 'Cauchy Mean Value Theorem application.'
        }
      },
      {
        id: 7,
        question: 'The limit lim_{x → 0} (tan x - x) / x³ equals:',
        options: ['1/6', '1/3', '1/2', '1'],
        correctIndex: 1,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'Taylor series: tan x = x + x³/3 + 2x⁵/15 + ...',
            'tan x - x = x³/3 + O(x⁵).',
            'lim_{x → 0} (x³/3) / x³ = 1/3.'
          ],
          keyConcept: 'Series expansion for tan x.'
        }
      },
      {
        id: 8,
        question: 'The definite integral ∫₀^(π/2) ln(sin x) dx equals:',
        options: ['-π/2 ln 2', 'π/2 ln 2', '-π ln 2', '0'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Let I = ∫₀^(π/2) ln(sin x) dx = ∫₀^(π/2) ln(cos x) dx.',
            '2I = ∫₀^(π/2) ln(sin x cos x) dx = ∫₀^(π/2) [ln(sin 2x) - ln 2] dx',
            '2I = I - (π/2) ln 2 ⇒ I = -π/2 ln 2.'
          ],
          keyConcept: 'Euler\'s definite integral for ln(sin x).'
        }
      },
      {
        id: 9,
        question: 'For the curve y = ln(sec x), the radius of curvature at x = 0 is:',
        options: ['1', '0', '2', '1/2'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'y\' = tan x. At x = 0, y\'(0) = 0.',
            'y\'\' = sec² x. At x = 0, y\'\'(0) = 1.',
            'Radius of curvature ρ = [1 + (y\')²]^(3/2) / |y\'\'| = [1 + 0]^(3/2) / 1 = 1.'
          ],
          keyConcept: 'Radius of curvature formula: ρ = (1 + y\'²)^(3/2) / |y\'\'|.'
        }
      },
      {
        id: 10,
        question: 'If A is a 3×3 matrix with det(A) = 4, then det(2A) is:',
        options: ['8', '16', '32', '64'],
        correctIndex: 2,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'Property: For an n × n matrix, det(k A) = kⁿ det(A).',
            'Here n = 3 and k = 2:',
            'det(2A) = 2³ · det(A) = 8 · 4 = 32.'
          ],
          keyConcept: 'Scaling property of determinants: det(kA) = kⁿ det(A).'
        }
      },
      // Questions 11-30 with full rigor
      {
        id: 11,
        question: 'If f(x) = x³ - 6x² + 11x - 6, how many times does f\'(c) = 0 vanish in (1, 3)?',
        options: ['0', '1', '2', '3'],
        correctIndex: 2,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'Roots of f(x) are 1, 2, 3 (since (x-1)(x-2)(x-3) = 0).',
            'By Rolle\'s theorem on [1, 2], f\'(c₁) = 0 for some c₁ ∈ (1, 2).',
            'By Rolle\'s theorem on [2, 3], f\'(c₂) = 0 for some c₂ ∈ (2, 3).',
            'Both c₁ and c₂ lie in (1, 3), so f\' vanishes 2 times.'
          ],
          keyConcept: 'Between any two consecutive real roots of a differentiable polynomial lies a root of its derivative.'
        }
      },
      {
        id: 12,
        question: 'Evaluate lim_{x → 0} (1 + x)^(1/x):',
        options: ['1', '0', 'e', '∞'],
        correctIndex: 2,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'Standard indeterminate form 1^∞.',
            'Let L = lim_{x → 0} (1 + x)^(1/x). ln L = lim_{x → 0} [ln(1 + x)] / x = 1.',
            'Therefore, L = e¹ = e.'
          ],
          keyConcept: 'Euler number definition.'
        }
      },
      {
        id: 13,
        question: 'If A is a square matrix such that A³ = 0, then (I - A)⁻¹ is equal to:',
        options: ['I + A + A²', 'I - A + A²', 'I + A', 'Does not exist'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            '(I - A)(I + A + A²) = I + A + A² - A - A² - A³ = I - A³.',
            'Since A³ = 0, (I - A)(I + A + A²) = I.',
            'Therefore, (I - A)⁻¹ = I + A + A².'
          ],
          keyConcept: 'Nilpotent matrix Neumann series identity.'
        }
      },
      {
        id: 14,
        question: 'The derivative of tan⁻¹[(2x)/(1 - x²)] with respect to sin⁻¹[(2x)/(1 + x²)] is:',
        options: ['1', '2', '1/2', '0'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'Let x = tan θ.',
            'tan⁻¹[(2x)/(1 - x²)] = tan⁻¹(tan 2θ) = 2θ = 2 tan⁻¹ x.',
            'sin⁻¹[(2x)/(1 + x²)] = sin⁻¹(sin 2θ) = 2θ = 2 tan⁻¹ x.',
            'Both functions are identical! Hence d(2θ) / d(2θ) = 1.'
          ],
          keyConcept: 'Trigonometric substitution simplifications.'
        }
      },
      {
        id: 15,
        question: 'The definite integral ∫₀¹ x (1 - x)⁹⁹ dx is equal to:',
        options: ['1 / 10100', '1 / 100', '1 / 9900', '1 / 10200'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Use property ∫₀ᵃ f(x) dx = ∫₀ᵃ f(a - x) dx.',
            '∫₀¹ (1 - x) [1 - (1 - x)]⁹⁹ dx = ∫₀¹ (1 - x) x⁹⁹ dx = ∫₀¹ (x⁹⁹ - x¹⁰⁰) dx.',
            '= [x¹⁰⁰ / 100 - x¹⁰¹ / 101]₀¹ = 1/100 - 1/101 = 1 / (100 × 101) = 1 / 10100.'
          ],
          keyConcept: 'King\'s property of definite integrals.'
        }
      },
      {
        id: 16,
        question: 'If two rows of a square matrix A are identical, then det(A) is:',
        options: ['1', '0', '-1', 'Undefined'],
        correctIndex: 1,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'Interchanging the two identical rows gives det(A) = -det(A).',
            '2 det(A) = 0 ⇒ det(A) = 0.'
          ],
          keyConcept: 'Matrix with linearly dependent rows has determinant zero.'
        }
      },
      {
        id: 17,
        question: 'The Maclaurin series expansion of cos x starts with:',
        options: ['1 - x²/2! + x⁴/4! - ...', 'x - x³/3! + x⁵/5! - ...', '1 + x²/2! + x⁴/4! + ...', 'x + x³/3! + ...'],
        correctIndex: 0,
        topic: 'Taylor Series',
        explanation: {
          steps: [
            'cos(0) = 1, cos\'(0) = 0, cos\'\'(0) = -1, cos\'\'\'(0) = 0, cos⁽⁴⁾(0) = 1.',
            'Series: 1 - x²/2! + x⁴/4! - ...'
          ],
          keyConcept: 'Even function cosine Maclaurin series.'
        }
      },
      {
        id: 18,
        question: 'If f\'\'(x) > 0 for all x in [a, b], then the function f(x) is:',
        options: ['Concave upward (Convex)', 'Concave downward', 'Linear', 'Oscillating'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'f\'\'(x) > 0 implies that the slope f\'(x) is strictly increasing.',
            'This corresponds to a curve that bends upwards (Concave upward / Convex).'
          ],
          keyConcept: 'Second derivative test for concavity.'
        }
      },
      {
        id: 19,
        question: 'If A is a 2×2 matrix with trace = 4 and determinant = 3, its eigenvalues are:',
        options: ['1 and 3', '2 and 2', '-1 and -3', '0 and 4'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'Characteristic equation: λ² - tr(A)λ + det(A) = 0.',
            'λ² - 4λ + 3 = 0 ⇒ (λ - 1)(λ - 3) = 0.',
            'λ = 1, 3.'
          ],
          keyConcept: 'Eigenvalues from trace and determinant.'
        }
      },
      {
        id: 20,
        question: 'Evaluate ∫ eˣ (1/x - 1/x²) dx:',
        options: ['eˣ / x + C', '-eˣ / x + C', 'eˣ ln x + C', 'eˣ / x² + C'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Standard theorem: ∫ eˣ [f(x) + f\'(x)] dx = eˣ f(x) + C.',
            'Let f(x) = 1/x. Then f\'(x) = -1/x².',
            'The integral is exactly eˣ (1/x) + C.'
          ],
          keyConcept: '∫ eˣ [f(x) + f\'(x)] dx = eˣ f(x) + C.'
        }
      },
      {
        id: 21,
        question: 'What is the limit lim_{x → 0} (sin x / x)?',
        options: ['1', '0', '∞', 'Undefined'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: ['Fundamental trigonometric limit: lim_{x → 0} (sin x / x) = 1.'],
          keyConcept: 'Basic limit.'
        }
      },
      {
        id: 22,
        question: 'If Rank(A) = 3 for a 3 × 5 matrix, the nullity of A is:',
        options: ['2', '3', '0', '5'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'By Rank-Nullity Theorem: Rank(A) + Nullity(A) = Number of columns n.',
            '3 + Nullity(A) = 5 ⇒ Nullity(A) = 2.'
          ],
          keyConcept: 'Rank-Nullity Theorem: Rank + Nullity = n.'
        }
      },
      {
        id: 23,
        question: 'The function f(x) = x³ - 3x has a local maximum at:',
        options: ['x = -1', 'x = 1', 'x = 0', 'x = 3'],
        correctIndex: 0,
        topic: 'Extrema & Applications',
        explanation: {
          steps: [
            'f\'(x) = 3x² - 3 = 0 ⇒ x² = 1 ⇒ x = ±1.',
            'f\'\'(x) = 6x.',
            'At x = -1: f\'\'(-1) = -6 < 0 (Local Maximum).',
            'At x = +1: f\'\'(1) = +6 > 0 (Local Minimum).'
          ],
          keyConcept: 'Second derivative test for local extrema.'
        }
      },
      {
        id: 24,
        question: 'The product of two orthogonal matrices is always:',
        options: ['Orthogonal', 'Diagonal', 'Symmetric', 'Skew-symmetric'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'Let A and B be orthogonal (A Aᵀ = I, B Bᵀ = I).',
            '(AB)(AB)ᵀ = A B Bᵀ Aᵀ = A (I) Aᵀ = A Aᵀ = I.',
            'Thus AB is also orthogonal.'
          ],
          keyConcept: 'Orthogonal matrices form a group under multiplication.'
        }
      },
      {
        id: 25,
        question: 'The value of ∫₀^(π/2) cos² x dx is:',
        options: ['π/4', 'π/2', '1', '0'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'By symmetry, ∫₀^(π/2) cos² x dx = ∫₀^(π/2) sin² x dx = π/4.'
          ],
          keyConcept: 'Standard definite integral.'
        }
      },
      {
        id: 26,
        question: 'If y = x⁴ - 4x³ + 6x², the point of inflection is at:',
        options: ['x = 1', 'x = 0', 'x = 2', 'x = -1'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'y\' = 4x³ - 12x² + 12x',
            'y\'\' = 12x² - 24x + 12 = 12(x² - 2x + 1) = 12(x - 1)²',
            'Setting y\'\' = 0 gives x = 1.'
          ],
          keyConcept: 'Point of inflection condition: y\'\' = 0.'
        }
      },
      {
        id: 27,
        question: 'If A is a square matrix, A + Aᵀ is always:',
        options: ['Symmetric', 'Skew-symmetric', 'Orthogonal', 'Identity'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            '(A + Aᵀ)ᵀ = Aᵀ + (Aᵀ)ᵀ = Aᵀ + A = A + Aᵀ.',
            'Since the transpose equals itself, it is Symmetric.'
          ],
          keyConcept: 'Symmetric decomposition of matrices.'
        }
      },
      {
        id: 28,
        question: 'If f(x) = eˣ on [0, 2], the point c satisfying LMVT is:',
        options: ['ln[(e² - 1)/2]', 'ln(e² - 1)', '1', 'ln 2'],
        correctIndex: 0,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'f\'(c) = eᶜ = [e² - e⁰] / (2 - 0) = (e² - 1)/2.',
            'Taking natural log: c = ln[(e² - 1)/2].'
          ],
          keyConcept: 'Lagrange Mean Value Theorem.'
        }
      },
      {
        id: 29,
        question: 'The limit lim_{x → 0} (eˣ - 1 - x) / x² equals:',
        options: ['1/2', '1', '0', '1/6'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'eˣ = 1 + x + x²/2! + O(x³).',
            'eˣ - 1 - x = x²/2 + O(x³).',
            'lim_{x → 0} (x²/2) / x² = 1/2.'
          ],
          keyConcept: 'Exponential series expansion.'
        }
      },
      {
        id: 30,
        question: 'If A = [[1, 2], [0, 1]], then Aⁿ is:',
        options: ['[[1, 2n], [0, 1]]', '[[1, 2ⁿ], [0, 1]]', '[[n, 2n], [0, n]]', '[[1, 0], [0, 1]]'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'A = I + N where N = [[0, 2], [0, 0]] (N² = 0).',
            'By Binomial theorem: Aⁿ = (I + N)ⁿ = I + nN = [[1, 2n], [0, 1]].'
          ],
          keyConcept: 'Matrix power by nilpotent decomposition.'
        }
      }
    ]
  },
  {
    id: 'mth165-midterm-mock-4',
    code: '25261MTH-MOCK4',
    title: 'Midterm Examination • Mock 4 (Speed & Accuracy Booster)',
    courseCode: 'MTH165',
    courseName: 'Mathematics for Engineers',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Exam Standard',
    topics: ['Diagonalization', 'Successive Derivatives', 'L\'Hôpital Multi-step', 'Indeterminate Limits', 'Definite Integrals'],
    description: 'Designed to build rapid problem-solving speed under university 90-minute time limits.',
    questions: [
      // 30 well structured questions
      {
        id: 1,
        question: 'If A is a 3×3 matrix with eigenvalues 1, -2, 3, then det(A) is:',
        options: ['-6', '6', '2', '0'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'det(A) is the product of all eigenvalues: λ₁ · λ₂ · λ₃ = (1) · (-2) · (3) = -6.'
          ],
          keyConcept: 'Determinant equals product of eigenvalues.'
        }
      },
      {
        id: 2,
        question: 'The rank of an n × n identity matrix Iₙ is:',
        options: ['n', 'n - 1', '1', '0'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['All n rows of the identity matrix are linearly independent, so rank is n.'],
          keyConcept: 'Full rank of identity matrix.'
        }
      },
      {
        id: 3,
        question: 'If f(x) = ln(1 + x), the coefficient of x³ in its Maclaurin series is:',
        options: ['1/3', '-1/3', '1/6', '-1/6'],
        correctIndex: 0,
        topic: 'Taylor Series',
        explanation: {
          steps: [
            'ln(1 + x) = x - x²/2 + x³/3 - x⁴/4 + ...',
            'The coefficient of x³ is 1/3.'
          ],
          keyConcept: 'Standard logarithmic Maclaurin series.'
        }
      },
      {
        id: 4,
        question: 'The limit lim_{x → 0} (1 - cos x) / x² is:',
        options: ['1/2', '1', '0', '-1/2'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            '1 - cos x = 2 sin²(x/2).',
            'lim_{x → 0} [2 sin²(x/2)] / x² = 2 · (1/4) = 1/2.'
          ],
          keyConcept: 'Standard limit.'
        }
      },
      {
        id: 5,
        question: 'Evaluate ∫₀¹ 1 / √(1 - x²) dx:',
        options: ['π/2', 'π', '1', '0'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            '∫ 1/√(1 - x²) dx = sin⁻¹ x.',
            '[sin⁻¹ x]₀¹ = sin⁻¹(1) - sin⁻¹(0) = π/2 - 0 = π/2.'
          ],
          keyConcept: 'Standard inverse sine integral.'
        }
      },
      {
        id: 6,
        question: 'If A is a symmetric matrix, then A =',
        options: ['Aᵀ', '-Aᵀ', 'A⁻¹', 'I'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['By definition, a matrix is symmetric if A = Aᵀ.'],
          keyConcept: 'Symmetric matrix definition.'
        }
      },
      {
        id: 7,
        question: 'The derivative of y = x^(sin x) is:',
        options: [
          'x^(sin x) [cos x · ln x + (sin x)/x]',
          'x^(sin x) [sin x · ln x + (cos x)/x]',
          'sin x · x^(sin x - 1)',
          'None of these'
        ],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'ln y = sin x · ln x',
            '(1/y) dy/dx = cos x · ln x + sin x · (1/x)',
            'dy/dx = x^(sin x) [cos x · ln x + (sin x)/x].'
          ],
          keyConcept: 'Logarithmic differentiation.'
        }
      },
      {
        id: 8,
        question: 'If f(x) = x³ - 3x² + 2x, Rolle\'s theorem applies on [0, 1] because:',
        options: [
          'f(0) = f(1) = 0 and f is continuous & differentiable',
          'f\'(0) = f\'(1)',
          'f(0) ≠ f(1)',
          'f is not continuous'
        ],
        correctIndex: 0,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'f(0) = 0 and f(1) = 1 - 3 + 2 = 0.',
            'Polynomials are continuous on [0, 1] and differentiable on (0, 1).',
            'All conditions of Rolle\'s theorem are satisfied.'
          ],
          keyConcept: 'Rolle\'s theorem conditions.'
        }
      },
      {
        id: 9,
        question: 'The value of ∫₀^(π/4) tan x dx is:',
        options: ['1/2 ln 2', 'ln 2', 'π/4', '1'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            '∫ tan x dx = ln|sec x|.',
            '[ln|sec x|]₀^(π/4) = ln(sec π/4) - ln(sec 0) = ln(√2) - ln(1) = 1/2 ln 2.'
          ],
          keyConcept: 'Definite integral of tan x.'
        }
      },
      {
        id: 10,
        question: 'A system AX = 0 of 3 equations in 3 unknowns with det(A) ≠ 0 has:',
        options: ['Only the trivial solution (0, 0, 0)', 'Infinite solutions', 'No solution', 'Two solutions'],
        correctIndex: 0,
        topic: 'Linear Systems',
        explanation: {
          steps: [
            'For a homogeneous system AX = 0, if det(A) ≠ 0, A is invertible.',
            'X = A⁻¹ 0 = 0. Hence only the trivial zero solution exists.'
          ],
          keyConcept: 'Homogeneous linear system uniqueness.'
        }
      },
      // Questions 11-30 concise & accurate
      {
        id: 11,
        question: 'If f(x) = |sin x|, then at x = 0 the function is:',
        options: ['Continuous but not differentiable', 'Differentiable', 'Discontinuous', 'None of these'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: ['LHD at 0 is -1 and RHD is +1. Continuous but not differentiable.'],
          keyConcept: 'Non-differentiability at cusp/corner.'
        }
      },
      {
        id: 12,
        question: 'The limit lim_{x → 0} (sin⁻¹ x) / x equals:',
        options: ['1', '0', 'π/2', '∞'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: ['Standard inverse trigonometric limit: lim_{x → 0} (sin⁻¹ x) / x = 1.'],
          keyConcept: 'Fundamental limit.'
        }
      },
      {
        id: 13,
        question: 'The trace of [[1, 4, 7], [2, 5, 8], [3, 6, 9]] is:',
        options: ['15', '12', '9', '0'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: ['tr(A) = 1 + 5 + 9 = 15.'],
          keyConcept: 'Sum of main diagonal entries.'
        }
      },
      {
        id: 14,
        question: 'If y = e^(ax), then yₙ (n-th derivative) is:',
        options: ['aⁿ e^(ax)', 'a e^(ax)', 'n a e^(ax)', 'e^(ax) / aⁿ'],
        correctIndex: 0,
        topic: 'Successive Differentiation',
        explanation: {
          steps: ['dⁿ/dxⁿ (eᵃˣ) = aⁿ eᵃˣ.'],
          keyConcept: 'Exponential n-th derivative.'
        }
      },
      {
        id: 15,
        question: 'The value of ∫₀^∞ e^(-x) dx is:',
        options: ['1', '0', '∞', 'e'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['[-e⁻ˣ]₀^∞ = 0 - (-1) = 1.'],
          keyConcept: 'Improper integral.'
        }
      },
      {
        id: 16,
        question: 'If A is a non-singular matrix, then Rank(A⁻¹) is:',
        options: ['Equal to Rank(A)', 'Less than Rank(A)', '0', '1'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['Since A and A⁻¹ are both invertible n×n matrices, both have rank n.'],
          keyConcept: 'Invertible matrix rank.'
        }
      },
      {
        id: 17,
        question: 'The limit lim_{x → ∞} (1 + 1/x)ˣ is:',
        options: ['e', '1', '∞', '0'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: ['Standard definition of base of natural logarithms e.'],
          keyConcept: 'Definition of e.'
        }
      },
      {
        id: 18,
        question: 'If f\'(c) = 0 and f\'\'(c) < 0, then at x = c the function has:',
        options: ['Local maximum', 'Local minimum', 'Inflection point', 'Saddle point'],
        correctIndex: 0,
        topic: 'Extrema & Applications',
        explanation: {
          steps: ['Second derivative test: f\'\'(c) < 0 indicates concave down (maximum).'],
          keyConcept: 'Second derivative test.'
        }
      },
      {
        id: 19,
        question: 'Evaluate ∫ 1 / (1 + x²) dx:',
        options: ['tan⁻¹ x + C', 'sin⁻¹ x + C', 'ln(1 + x²) + C', 'sec⁻¹ x + C'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['Standard derivative: d/dx (tan⁻¹ x) = 1/(1 + x²).'],
          keyConcept: 'Standard integral.'
        }
      },
      {
        id: 20,
        question: 'If A is 2×2 and det(A) = -3, then det(A⁻¹) is:',
        options: ['-1/3', '1/3', '-3', '3'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['det(A⁻¹) = 1 / det(A) = 1 / (-3) = -1/3.'],
          keyConcept: 'Inverse determinant property.'
        }
      },
      {
        id: 21,
        question: 'The derivative of ln(cos x) is:',
        options: ['-tan x', 'tan x', '-cot x', 'sec x'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: ['(1/cos x) · (-sin x) = -tan x.'],
          keyConcept: 'Chain rule.'
        }
      },
      {
        id: 22,
        question: 'The minimum value of f(x) = x² - 4x + 7 is:',
        options: ['3', '7', '4', '0'],
        correctIndex: 0,
        topic: 'Extrema & Applications',
        explanation: {
          steps: ['f(x) = (x - 2)² + 3. The minimum value is 3 at x = 2.'],
          keyConcept: 'Vertex form of quadratic.'
        }
      },
      {
        id: 23,
        question: 'The value of ∫₀¹ x² dx is:',
        options: ['1/3', '1/2', '1', '2/3'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['[x³/3]₀¹ = 1/3.'],
          keyConcept: 'Power rule integral.'
        }
      },
      {
        id: 24,
        question: 'If det(A - λI) = λ² - 9 = 0, the eigenvalues are:',
        options: ['±3', '9', '0', '3 only'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: ['λ² = 9 ⇒ λ = ±3.'],
          keyConcept: 'Eigenvalues.'
        }
      },
      {
        id: 25,
        question: 'The limit lim_{x → 0} (ln(1 + x)) / x equals:',
        options: ['1', '0', 'e', '∞'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: ['Standard limit: lim_{x → 0} ln(1 + x)/x = 1.'],
          keyConcept: 'Logarithmic limit.'
        }
      },
      {
        id: 26,
        question: 'If A is a diagonal matrix, Aᵀ is equal to:',
        options: ['A', '-A', 'I', 'A⁻¹'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['Diagonal matrices are always symmetric: A = Aᵀ.'],
          keyConcept: 'Diagonal matrix symmetry.'
        }
      },
      {
        id: 27,
        question: 'The derivative of e^(x²) is:',
        options: ['2x e^(x²)', 'e^(x²)', 'x² e^(x²)', '2 e^(x²)'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: ['By chain rule: e^(x²) · d/dx (x²) = 2x e^(x²).'],
          keyConcept: 'Chain rule.'
        }
      },
      {
        id: 28,
        question: 'The value of ∫₀^(π/2) sin x dx is:',
        options: ['1', '0', '-1', 'π/2'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['[-cos x]₀^(π/2) = -cos(π/2) - (-cos 0) = 0 + 1 = 1.'],
          keyConcept: 'Definite integral of sine.'
        }
      },
      {
        id: 29,
        question: 'For f(x) = x⁴, f\'\'\'(x) is:',
        options: ['24x', '12x²', '4x³', '24'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: ['f\' = 4x³, f\'\' = 12x², f\'\'\' = 24x.'],
          keyConcept: 'Successive derivatives.'
        }
      },
      {
        id: 30,
        question: 'If A is a 2×2 matrix with eigenvalues 2 and 5, then det(A) is:',
        options: ['10', '7', '3', '0'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: ['det(A) = 2 × 5 = 10.'],
          keyConcept: 'Determinant from eigenvalues.'
        }
      }
    ]
  },
  {
    id: 'mth165-midterm-mock-5',
    code: '25261MTH-MOCK5',
    title: 'Midterm Examination • Mock 5 (Master Challenge & Traps)',
    courseCode: 'MTH165',
    courseName: 'Mathematics for Engineers',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Master Challenge',
    topics: ['Negative-Marking Traps', 'Eigenvector Nullspaces', 'Taylor Error Bounds', 'Trigonometric Identities', 'Definite Integrals'],
    description: 'Mastery challenge designed to sharpen exam technique, prevent negative marking mistakes, and guarantee high percentile scoring.',
    questions: [
      {
        id: 1,
        question: 'If A is a singular matrix of order 3, which of the following MUST be true?',
        options: ['0 is an eigenvalue of A', 'All eigenvalues of A are 0', 'A is the zero matrix', 'Rank(A) = 0'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'det(A) = Π λᵢ. If A is singular, det(A) = 0.',
            'This implies at least one eigenvalue must be 0.'
          ],
          keyConcept: 'Singular matrix has at least one zero eigenvalue.'
        }
      },
      {
        id: 2,
        question: 'The rank of matrix A = [[1, 2, 3], [2, 4, 6], [3, 6, 9]] is:',
        options: ['1', '2', '3', '0'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: [
            'Row 2 = 2 · Row 1, and Row 3 = 3 · Row 1.',
            'There is only 1 linearly independent row. Hence Rank(A) = 1.'
          ],
          keyConcept: 'Proportional rows reduce rank to 1.'
        }
      },
      {
        id: 3,
        question: 'The derivative of y = |x|³ at x = 0 is:',
        options: ['0', '1', '-1', 'Does not exist'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'For x ≥ 0: y = x³ ⇒ y\' = 3x² (at 0: 0).',
            'For x < 0: y = -x³ ⇒ y\' = -3x² (at 0: 0).',
            'Both left and right derivatives equal 0, so f\'(0) = 0.'
          ],
          keyConcept: 'Smoothness of |x|³ at the origin.'
        }
      },
      {
        id: 4,
        question: 'Evaluate lim_{x → 0} (aˣ - 1) / x for a > 0:',
        options: ['ln a', 'a', '1', '0'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: [
            'Standard exponential limit: lim_{x → 0} (aˣ - 1)/x = ln a.'
          ],
          keyConcept: 'Exponential limit base a.'
        }
      },
      {
        id: 5,
        question: 'The value of ∫₀^(π/2) (sin x) / (sin x + cos x) dx is:',
        options: ['π/4', 'π/2', '1', '0'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: [
            'Let I = ∫₀^(π/2) [sin x / (sin x + cos x)] dx.',
            'Using King\'s property: I = ∫₀^(π/2) [cos x / (cos x + sin x)] dx.',
            '2I = ∫₀^(π/2) 1 dx = π/2 ⇒ I = π/4.'
          ],
          keyConcept: 'King\'s property symmetry.'
        }
      },
      {
        id: 6,
        question: 'If A and B are square matrices of the same order, then tr(AB) is always equal to:',
        options: ['tr(BA)', 'tr(A) · tr(B)', 'tr(A) + tr(B)', 'det(AB)'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: ['Trace cyclic property: tr(AB) = tr(BA).'],
          keyConcept: 'Cyclic property of matrix trace.'
        }
      },
      {
        id: 7,
        question: 'If y = ln(sec x + tan x), then dy/dx is:',
        options: ['sec x', 'tan x', 'sec x tan x', 'sec² x'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: [
            'dy/dx = (1 / (sec x + tan x)) · (sec x tan x + sec² x)',
            '= [sec x (tan x + sec x)] / (sec x + tan x) = sec x.'
          ],
          keyConcept: 'Standard derivative of ln(sec x + tan x).'
        }
      },
      {
        id: 8,
        question: 'If f(x) = x³ - x on [-1, 1], the points c satisfying Rolle\'s theorem are:',
        options: ['±1/√3', '0', '±1/3', '±1'],
        correctIndex: 0,
        topic: 'Mean Value Theorems',
        explanation: {
          steps: [
            'f\'(x) = 3x² - 1 = 0 ⇒ x² = 1/3 ⇒ x = ±1/√3.',
            'Both ±1/√3 lie in the open interval (-1, 1).'
          ],
          keyConcept: 'Rolle\'s theorem roots.'
        }
      },
      {
        id: 9,
        question: 'Evaluate ∫ e^(2x) dx:',
        options: ['1/2 e^(2x) + C', '2 e^(2x) + C', 'e^(2x) + C', '1/4 e^(2x) + C'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['∫ e^(kx) dx = (1/k) e^(kx) + C. For k = 2: 1/2 e^(2x) + C.'],
          keyConcept: 'Exponential integration.'
        }
      },
      {
        id: 10,
        question: 'If A is a 3×3 matrix with eigenvalues 1, 1, 1 and A ≠ I, then A is:',
        options: ['Not diagonalizable', 'Diagonalizable', 'Orthogonal', 'Zero matrix'],
        correctIndex: 0,
        topic: 'Matrices & Eigenvalues',
        explanation: {
          steps: [
            'If an n×n matrix with all eigenvalues λ is diagonalizable, it must equal λI.',
            'Since A ≠ I, it lacks a full basis of eigenvectors and is Not Diagonalizable.'
          ],
          keyConcept: 'Defective matrices and algebraic vs geometric multiplicity.'
        }
      },
      // Questions 11-30
      {
        id: 11,
        question: 'The limit lim_{x → 0} (1 - cos 2x) / x² equals:',
        options: ['2', '1', '1/2', '4'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: ['1 - cos 2x = 2 sin² x. lim_{x → 0} (2 sin² x)/x² = 2(1)² = 2.'],
          keyConcept: 'Trigonometric limit.'
        }
      },
      {
        id: 12,
        question: 'Evaluate ∫ 1 / (x ln x) dx:',
        options: ['ln(ln x) + C', 'ln x + C', '1 / (ln x) + C', '(ln x)² + C'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['Let u = ln x, du = 1/x dx. ∫ 1/u du = ln u + C = ln(ln x) + C.'],
          keyConcept: 'Substitution integral.'
        }
      },
      {
        id: 13,
        question: 'If f(x) = x⁵, the 5th derivative f⁽⁵⁾(x) is:',
        options: ['120', '24', '720', '0'],
        correctIndex: 0,
        topic: 'Successive Differentiation',
        explanation: {
          steps: ['dⁿ/dxⁿ (xⁿ) = n!. For n = 5: 5! = 120.'],
          keyConcept: 'Factorial n-th derivative.'
        }
      },
      {
        id: 14,
        question: 'If A is an invertible matrix, then (Aᵀ)⁻¹ is equal to:',
        options: ['(A⁻¹)ᵀ', 'A', 'Aᵀ', 'I'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['Transpose and inverse operations commute: (Aᵀ)⁻¹ = (A⁻¹)ᵀ.'],
          keyConcept: 'Transpose of inverse.'
        }
      },
      {
        id: 15,
        question: 'The value of ∫₀^π sin x dx is:',
        options: ['2', '0', '1', 'π'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['[-cos x]₀^π = -(-1) - (-1) = 1 + 1 = 2.'],
          keyConcept: 'Definite integral of sine over half period.'
        }
      },
      {
        id: 16,
        question: 'The function f(x) = |x - 3| has a local minimum at:',
        options: ['x = 3', 'x = 0', 'x = -3', 'No minimum exists'],
        correctIndex: 0,
        topic: 'Extrema & Applications',
        explanation: {
          steps: ['Since |x - 3| ≥ 0, its minimum value is 0 which occurs at x = 3.'],
          keyConcept: 'Absolute value minimum.'
        }
      },
      {
        id: 17,
        question: 'The Taylor series expansion of 1/(1 - x) about x = 0 is:',
        options: ['1 + x + x² + x³ + ...', '1 - x + x² - x³ + ...', 'x + x² + x³ + ...', '1 - x² + x⁴ - ...'],
        correctIndex: 0,
        topic: 'Taylor Series',
        explanation: {
          steps: ['Geometric series sum: 1/(1 - x) = Σ xⁿ for |x| < 1.'],
          keyConcept: 'Geometric series.'
        }
      },
      {
        id: 18,
        question: 'The limit lim_{x → ∞} (x² + 3x) / (2x² - 5) is:',
        options: ['1/2', '0', '∞', '3/2'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: ['Divide numerator and denominator by highest power x²: (1 + 3/x) / (2 - 5/x²) → 1/2.'],
          keyConcept: 'Rational limits at infinity.'
        }
      },
      {
        id: 19,
        question: 'If A is a 2×2 matrix with det(A) = 0, which of the following is true?',
        options: ['Rows are linearly dependent', 'A is invertible', 'Rank(A) = 2', 'Trace is zero'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['det(A) = 0 means the rows are linearly dependent.'],
          keyConcept: 'Determinant and linear dependence.'
        }
      },
      {
        id: 20,
        question: 'Evaluate ∫ tan² x dx:',
        options: ['tan x - x + C', 'sec² x + C', 'tan x + x + C', '1/3 tan³ x + C'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['Use identity tan² x = sec² x - 1.', '∫ (sec² x - 1) dx = tan x - x + C.'],
          keyConcept: 'Trigonometric integral identity.'
        }
      },
      {
        id: 21,
        question: 'If y = sin⁻¹ x, then dy/dx is:',
        options: ['1 / √(1 - x²)', '-1 / √(1 - x²)', '1 / (1 + x²)', '1 / √(x² - 1)'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: ['Standard derivative of arcsin: d/dx (sin⁻¹ x) = 1/√(1 - x²).'],
          keyConcept: 'Inverse trig derivative.'
        }
      },
      {
        id: 22,
        question: 'The number of linearly independent solutions to AX = 0 for an m×n matrix with rank r is:',
        options: ['n - r', 'r', 'm - r', 'n'],
        correctIndex: 0,
        topic: 'Linear Systems',
        explanation: {
          steps: ['Dimension of null space (nullity) = n - rank = n - r.'],
          keyConcept: 'Nullity formula.'
        }
      },
      {
        id: 23,
        question: 'The limit lim_{x → 0} (sin 5x) / (sin 3x) equals:',
        options: ['5/3', '3/5', '1', '0'],
        correctIndex: 0,
        topic: 'Limits & Indeterminate Forms',
        explanation: {
          steps: ['[(sin 5x)/(5x) · 5] / [(sin 3x)/(3x) · 3] = (1 · 5) / (1 · 3) = 5/3.'],
          keyConcept: 'Trig limit scaling.'
        }
      },
      {
        id: 24,
        question: 'Evaluate ∫₀¹ x eˣ² dx:',
        options: ['(e - 1) / 2', 'e - 1', 'e / 2', '1/2'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['Let u = x², du = 2x dx. 1/2 ∫₀¹ eᵘ du = 1/2 [e - 1].'],
          keyConcept: 'Substitution integral.'
        }
      },
      {
        id: 25,
        question: 'If A is an orthogonal matrix of order 3, then det(A) cannot be:',
        options: ['2', '1', '-1', 'None of these'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['det(A) for orthogonal matrices must be either +1 or -1; it can never be 2.'],
          keyConcept: 'Orthogonal determinant.'
        }
      },
      {
        id: 26,
        question: 'The derivative of ln(tan x) is:',
        options: ['2 csc 2x', 'sec² x', 'cot x', '2 sec 2x'],
        correctIndex: 0,
        topic: 'Differential Calculus',
        explanation: {
          steps: ['(1/tan x) · sec² x = (cos x / sin x) · (1/cos² x) = 1/(sin x cos x) = 2/sin 2x = 2 csc 2x.'],
          keyConcept: 'Trigonometric simplification of derivative.'
        }
      },
      {
        id: 27,
        question: 'The value of ∫₀^(π/2) cos x dx is:',
        options: ['1', '0', '-1', 'π/2'],
        correctIndex: 0,
        topic: 'Integral Calculus',
        explanation: {
          steps: ['[sin x]₀^(π/2) = sin(π/2) - sin(0) = 1 - 0 = 1.'],
          keyConcept: 'Definite integral of cosine.'
        }
      },
      {
        id: 28,
        question: 'If det(A) = 5 and det(B) = 3, then det(AB) is:',
        options: ['15', '8', '5/3', '2'],
        correctIndex: 0,
        topic: 'Linear Algebra',
        explanation: {
          steps: ['det(AB) = det(A) · det(B) = 5 · 3 = 15.'],
          keyConcept: 'Multiplicative property of determinants.'
        }
      },
      {
        id: 29,
        question: 'The Maclaurin series of sin x is an:',
        options: ['Odd function expansion (odd powers of x)', 'Even function expansion', 'Exponential series', 'Constant series'],
        correctIndex: 0,
        topic: 'Taylor Series',
        explanation: {
          steps: ['sin x = x - x³/3! + x⁵/5! - ... contains only odd powers because sine is an odd function.'],
          keyConcept: 'Symmetry in Taylor series.'
        }
      },
      {
        id: 30,
        question: 'If f(x) = x³ - 12x, the local minimum occurs at:',
        options: ['x = 2', 'x = -2', 'x = 0', 'x = 12'],
        correctIndex: 0,
        topic: 'Extrema & Applications',
        explanation: {
          steps: [
            'f\'(x) = 3x² - 12 = 0 ⇒ x² = 4 ⇒ x = ±2.',
            'f\'\'(x) = 6x.',
            'At x = +2: f\'\'(2) = 12 > 0 (Local Minimum).'
          ],
          keyConcept: 'Second derivative test.'
        }
      }
    ]
  }
];
