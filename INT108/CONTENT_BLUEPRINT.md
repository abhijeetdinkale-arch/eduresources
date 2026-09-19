# INT108: Python Programming — Master Content Blueprint & Syllabus Specification
## Comprehensive University Study & Practical Programming Guide (Semester 1)

**Course Code**: INT108  
**Course Title**: Python Programming  
**Target Audience**: Lovely Professional University (LPU) Semester 1 Engineering Students (Beginners to Intermediate)  
**Document Status**: Authoritative Master Architectural Specification & Pedagogical Blueprint (Phase 1 Complete)  
**Primary Source Authority**: Official LPU INT108 Unit 1 to Unit 6 Source Notes  
**Philosophy**: Code-First Conceptual Mastery, Line-by-Line Mechanics, Visual Tracing, Output Prediction, Debugging Instincts, and University Examination Domination.

---

## 1. Executive Course Overview & Structural Organization

The **INT108: Python Programming** course introduces first-year engineering students to the fundamentals of procedural, functional, and object-oriented programming using Python 3. The syllabus progresses systematically from foundational syntax, variables, operators, and control structures to complex data structures, modular function design, recursion, object-oriented software engineering, file handling, exception management, and text processing via regular expressions.

```text
INT108: Python Programming
├── Part I   / Unit 1: Programming Environment, Variables, Expressions & Statements
├── Part II  / Unit 2: Conditional Statements, Iterative Statements & Algorithms
├── Part III / Unit 3: Functions, Scope, Modules & Recursion
├── Part IV  / Unit 4: Compound Data Structures (Strings, Lists, Tuples & Dictionaries)
├── Part V   / Unit 5: Object-Oriented Programming (Classes, Objects, Inheritance & Encapsulation)
├── Part VI  / Unit 6: File Handling, Exception Handling & Regular Expressions
├── Part VII / Master Python Syntax, Methods & Standard Library Cheatsheet
├── Part VIII/ Cross-Unit Multi-Concept Practical Coding Challenges
└── Part IX  / Full-Length University Mock Examination Papers (100 Marks Each)
```

---

## 2. Standardized Pedagogical Learning Progression

To ensure that first-year engineering students transition seamlessly from basic syntax to writing robust, bug-free Python software, every programming topic across all units must strictly follow the **10-Step Programming Learning Progression**:

```
[1. CONCEPT NAME & PURPOSE]
          │
          ▼
[2. FORMAL SYNTAX & SPECIFICATION]
          │
          ▼
[3. INTUITION & VISUAL MEMORY MODEL (Diagram/Memory State)]
          │
          ▼
[4. MINIMAL / FOUNDATIONAL CODE EXAMPLE]
          │
          ▼
[5. EXACT OUTPUT & TERMINAL BEHAVIOR]
          │
          ▼
[6. LINE-BY-LINE EXECUTION BREAKDOWN (Why & How it works)]
          │
          ▼
[7. ADVANCED / PRACTICAL EXAM-TIER EXAMPLE]
          │
          ▼
[8. COMMON MISTAKES, PITFALLS & RUNTIME TRAPS]
          │
          ▼
[9. EXAM TIPS, OUTPUT PREDICTION & DEBUGGING HEURISTICS]
          │
          ▼
[10. GRADED PRACTICE EXERCISES & COMPLETE WORKED SOLUTIONS]
```

---

## 3. Unit-by-Unit Detailed Content Blueprints

---

### PART I / UNIT 1: Setting up your Programming Environment; Variables, Expression and Statements

#### 1. Unit Metadata & Topic Hierarchy
- **1.1 Unit Overview & Learning Objectives**
- **1.2 Setting up the Programming Environment**:
  - 1.2.1 Python Overview: Interpreted vs. Compiled execution model, dynamic typing, high-level features.
  - 1.2.2 Python Versions: Python 2 (legacy, official deprecation Jan 2020, `print` statement vs function, integer division differences) vs. Python 3 (modern standard, UTF-8 strings, unified division).
  - 1.2.3 Python Installation on Windows/macOS/Linux: Download from python.org, executable setup, **Critical Step: Adding Python to PATH environment variable**, verification via `python --version` / `python3 --version`.
  - 1.2.4 Running Python Programs: Interactive Shell (REPL / IDLE `>>> print("Hello, World!")`) vs. Script Mode (`hello.py` executed via `python hello.py`).
- **1.3 Variables: Naming, Using, and Keywords**:
  - 1.3.1 Definition of Variables: Named references/labels to objects in memory, assignment operator (`=`), dynamic type binding.
  - 1.3.2 Variable Naming Rules:
    1. Must begin with a letter (`a-z`, `A-Z`) or an underscore (`_`).
    2. Cannot begin with a digit (`0-9`).
    3. Can contain alphanumeric characters and underscores.
    4. Case-sensitive (`total`, `Total`, `TOTAL` are distinct variables).
    5. Pythonic Naming Conventions: `snake_case` for variables/functions, `UPPER_CASE` for constants, `PascalCase` for classes.
  - 1.3.3 Python Keywords (Reserved Words): Complete list (`False`, `None`, `True`, `and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield`). Cannot be used as variable identifiers.
  - 1.3.4 Avoiding `NameError`: Definition, causes (misspelled identifiers, using variables before assignment).
- **1.4 Values and Types**:
  - 1.4.1 Fundamental Primitive Types: Integers (`int`), Floating-Point numbers (`float`), Strings (`str`), Booleans (`bool`).
  - 1.4.2 The `type()` Built-in Function: Type inspection, examining numeric vs. quoted string values (e.g., `type(17)` vs. `type("17")`).
- **1.5 Statements, Operators, and Expressions**:
  - 1.5.1 Statements vs. Expressions: Expressions produce values (`2 + 3`); Statements perform actions/state changes (Assignment `x = 5`, Function Call `print(x)`). Interactive evaluation vs. script execution.
  - 1.5.2 Arithmetic Operators and Operands:
    - Addition (`+`), Subtraction (`-`), Multiplication (`*`)
    - True Division (`/`): Always returns a `float` (e.g., `10 / 2 = 5.0`)
    - Floor / Integer Division (`//`): Truncates to floor whole number (e.g., `10 // 3 = 3`, `-10 // 3 = -4`)
    - Modulus (`%`): Computes division remainder (e.g., `10 % 3 = 1`)
    - Exponentiation (`**`): Power operation (e.g., `2 ** 3 = 8`).
  - 1.5.3 Order of Operations (PEMDAS Rules):
    1. Parentheses `()`
    2. Exponentiation `**` (Evaluates **Right-to-Left**: `2 ** 3 ** 2 = 2 ** 9 = 512`)
    3. Multiplication `*`, True Division `/`, Floor Division `//`, Modulus `%` (Left-to-Right)
    4. Addition `+`, Subtraction `-` (Left-to-Right).
- **1.6 Operations on Strings**:
  - 1.6.1 String Concatenation (`+`): Merging strings (`"Python" + " " + "3"`).
  - 1.6.2 String Repetition (`*`): Multiplying string by integer (`"Go! " * 3`).
  - 1.6.3 Prohibited String Arithmetic: Subtraction (`-`), division (`/`), float multiplication raise `TypeError`.
- **1.7 Composition and Comments**:
  - 1.7.1 Composition: Combining nested function calls and expressions (e.g., `print(type(int("25") * 2))`).
  - 1.7.2 Code Comments: Single-line (`#`), Multi-line block comments, Docstrings (`"""..."""`).

#### 2. Visual Memory Models & Diagrams Required
- Diagram 1.1: Python Compilation vs. Bytecode Interpretation Workflow (`.py` $\to$ CPython Bytecode `.pyc` $\to$ PVM Virtual Machine $\to$ CPU).
- Diagram 1.2: Variable Reference Model (Variables as pointers/tags to heap memory objects, dynamic rebinding).
- Diagram 1.3: PEMDAS Precedence Tree & Associativity Resolution.

#### 3. Required Programming Demonstrations & Code Walkthroughs
1. **Program 1.1**: Checking environment details, Python version, and dynamic type allocations.
2. **Program 1.2**: Arithmetic calculation suite demonstrating float vs. floor division, remainder arithmetic, and right-to-left exponentiation.
3. **Program 1.3**: String concatenation and banner repetition formatting.
4. **Program 1.4**: Interactive user input calculation with type casting (`input()`, `int()`, `float()`).
5. **Program 1.5**: Temperature converter (Fahrenheit to Celsius) demonstrating operator precedence.

#### 4. Pedagogical Exam Preparation Elements
- **Exam Tips**: Recognizing that `/` always returns `float`; remembering right-to-left evaluation of `**`; identifying case-sensitivity in keywords (`True` vs `true`).
- **Common Mistakes Box**: Attempting arithmetic on string inputs (`x = input(); print(x + 5)` raises `TypeError`); assigning to keywords (`pass = 10` raises `SyntaxError`); using undefined variables.
- **Output Prediction Suite**: 5 Tricky code snippets testing operator precedence, string repetition, and division semantics.
- **Debugging Challenge**: 3 Buggy snippets containing `NameError`, `SyntaxError`, and `TypeError`.
- **Graded Practice Problems**: 10 Problems (Level 1 Foundation $\to$ Level 4 Challenge).
- **Multiple Choice Questions (MCQs)**: 10 High-Yield MCQs with full analytical answer rationales.
- **25-Mark Unit Test**: Standardized university paper with step-by-step scoring solutions.

---

### PART II / UNIT 2: Conditional Statements, Iterative Statements & Algorithms

#### 1. Unit Metadata & Topic Hierarchy
- **2.1 Unit Overview & Learning Objectives**
- **2.2 The Modulus Operator & Arithmetic Patterns**:
  - 2.2.1 Mechanics of `a % b`.
  - 2.2.2 Core Use Cases: Parity testing (`n % 2 == 0` even, `n % 2 != 0` odd), digit extraction (`n % 10` for units digit, `(n // 10) % 10` for tens digit), cyclic/clock arithmetic (`(hour + k) % 24`).
- **2.3 Pseudorandom Number Generation (`random` Module)**:
  - 2.3.1 Deterministic algorithms vs. Pseudorandomness.
  - 2.3.2 Key Module Functions:
    - `random.random()`: Generates float in $[0.0, 1.0)$.
    - `random.randint(a, b)`: Generates integer $N \in [a, b]$ (inclusive of both endpoints $a$ and $b$).
    - `random.choice(seq)`: Random selection from list, string, or tuple.
    - `random.randrange(start, stop, step)`: Random integer from range.
- **2.4 Boolean Expressions & Relational Operators**:
  - 2.4.1 Boolean Data Type: `True` and `False`.
  - 2.4.2 Relational Comparison Operators: `==` (Equality), `!=` (Inequality), `>` (Strictly Greater), `<` (Strictly Less), `>=` (Greater or Equal), `<=` (Less or Equal).
  - 2.4.3 The Assignment (`=`) vs. Equality (`==`) Trap.
- **2.5 Logical Operators & Short-Circuit Evaluation**:
  - 2.5.1 `and`: True if and only if both operands are True. Short-circuit: if left is False, right is not evaluated.
  - 2.5.2 `or`: True if at least one operand is True. Short-circuit: if left is True, right is not evaluated.
  - 2.5.3 `not`: Unary negation operator.
  - 2.5.4 Logical Precedence: `not` > `and` > `or`.
- **2.6 Conditional Statements (Selection Structures)**:
  - 2.6.1 Simple `if` Statement: Syntax, indentation block, flowchart.
  - 2.6.2 Alternative Execution (`if...else`): Two mutually exclusive paths.
  - 2.6.3 Chained Conditionals (`if...elif...else`): Multi-way branching, evaluation terminates on first True branch.
  - 2.6.4 Nested Conditionals: Multi-level decision trees, refactoring nested `if` statements using logical `and`.
- **2.7 While Statements (Indefinite Iteration)**:
  - 2.7.1 Loop Mechanics: Initialization, Condition check, Loop Body, State Update.
  - 2.7.2 Infinite Loops: Causes (missing update, condition always True), debugging strategies.
  - 2.7.3 Loop Jump Statements:
    - `break`: Abruptly terminates the enclosing loop.
    - `continue`: Skips remainder of current iteration and jumps to condition check.
    - `pass`: Syntactic placeholder / no-op.
  - 2.7.4 The `while...else` Construct: Executes `else` block when loop terminates normally without hitting a `break`.
- **2.8 For Loop Statement (Definite Iteration)**:
  - 2.8.1 Sequence Traversal Syntax: `for item in sequence:`.
  - 2.8.2 The `range()` Function: `range(stop)`, `range(start, stop)`, `range(start, stop, step)`, negative steps for counting down.
  - 2.8.3 Accumulator Pattern: Running sums, running products, counting matches.
- **2.9 Nested Loops**:
  - 2.9.1 Nested `for` Loops: Multi-dimensional iteration, matrix/grid traversal, outer vs. inner loop step execution ($N \times M$).
  - 2.9.2 Nested `while` Loops: Explicit inner loop variable re-initialization.
  - 2.9.3 Printing 2D Patterns (Triangles, pyramids, multiplication tables).
- **2.10 Random Numbers in Loops (Simulations & Games)**:
  - 2.10.1 Number Guessing Game (While loop with `random.randint` and feedback).
  - 2.10.2 1D/2D Random Walk Simulation (Iterative trajectory tracking).
- **2.11 Software Engineering Principles: Encapsulation and Generalization**:
  - 2.11.1 Encapsulation: Wrapping iteration logic into a named function.
  - 2.11.2 Generalization: Replacing hardcoded constants with parameters to extend reusability.

#### 2. Visual Diagrams Required
- Flowchart 2.1: `if...elif...else` Multi-Way Selection Flow.
- Flowchart 2.2: `while` vs `for` Loop Execution Lifecycle (Condition $\leftrightarrow$ Body $\leftrightarrow$ Update).
- Diagram 2.3: `break` vs `continue` Execution Routing in Loops.

#### 3. Required Programming Demonstrations
1. **Program 2.1**: Leap Year determination using compound boolean expressions.
2. **Program 2.2**: Prime number verification using `for...else` and early `break`.
3. **Program 2.3**: Digit extraction, sum of digits, and palindrome number checker via `while` loop.
4. **Program 2.4**: Fibonacci series generation up to $N$ terms.
5. **Program 2.5**: Complete Interactive Number Guessing Game with guess counter and difficulty limits.

#### 4. Pedagogical Exam Preparation Elements
- **Exam Tips**: Understanding `randint(a, b)` includes $b$; remembering `range(a, b)` excludes $b$; tracing `for...else` behavior.
- **Common Mistakes Box**: Forgetting colons `:` after `if`, `while`, `for`; infinite loops from forgetting `i += 1`; confusing `=` with `==`.
- **Output Prediction Suite**: 5 Loop tracing questions with `break`, `continue`, and `range` step variations.
- **Debugging Challenge**: 3 Code snippets containing off-by-one errors and loop variable shadowing.
- **Graded Practice Problems**: 10 Problems.
- **Multiple Choice Questions (MCQs)**: 10 MCQs with analytical explanations.
- **25-Mark Unit Test**: Full paper with scoring rubric and solutions.

---

### PART III / UNIT 3: Functions, Scope, Modules & Recursion

#### 1. Unit Metadata & Topic Hierarchy
- **3.1 Unit Overview & Learning Objectives**
- **3.2 Function Calls & Flow of Execution**:
  - 3.2.1 Function Terminology: Caller vs. Callee, invocation syntax `func(args)`.
  - 3.2.2 Fruitful Functions vs. Void Functions:
    - Fruitful: Returns explicit value via `return`.
    - Void: Executes actions (e.g., printing); returns `None` implicitly.
  - 3.2.3 Flow of Execution: Function call stack, control suspension, execution jump, return value propagation.
- **3.3 Type Conversion and Coercion**:
  - 3.3.1 Type Coercion (Implicit): Automatic numeric promotion (`int + float -> float`).
  - 3.3.2 Type Casting (Explicit): `int(x)` (truncation towards zero, string parsing), `float(x)`, `str(x)`, `bool(x)` (falsy values: `0`, `""`, `[]`, `None`).
- **3.4 The Built-in `math` Module**:
  - 3.4.1 Module Import Syntax: `import math`, `from math import sqrt, pi`.
  - 3.4.2 Essential Mathematical Functions: `ceil()`, `floor()`, `sqrt()`, `pow()`, `fabs()`, `factorial()`, `gcd()`, `log()`, `log10()`, trigonometric functions (`sin()`, `cos()`, `radians()`, `degrees()`).
  - 3.4.3 Constants: `math.pi`, `math.e`, `math.tau`, `math.inf`.
- **3.5 Function Definition & Scope**:
  - 3.5.1 Function Definition Syntax: `def function_name(parameters):`, header, docstrings, return statements.
  - 3.5.2 Variable Scope & Lifetime:
    - Local Scope: Variables created inside functions, destroyed upon return.
    - Global Scope: Variables defined at top-level module script.
    - The `global` Keyword: Modifying global state inside local scopes (and why to avoid it).
    - Scope Resolution Rule: **LEGB Rule** (Local $\to$ Enclosing $\to$ Global $\to$ Built-in).
- **3.6 Function Parameters and Arguments**:
  - 3.6.1 Parameter (Formal placeholder in `def`) vs. Argument (Actual value at call time).
  - 3.6.2 Positional Arguments: Mapped strictly by index position.
  - 3.6.3 Keyword (Named) Arguments: Mapped by `name=value` (order independent).
  - 3.6.4 Default Parameter Values: Syntax `def func(a, b=10):`, default value evaluated once, **Caution with mutable default arguments**.
  - 3.6.5 Arbitrary Argument Lists:
    - `*args`: Variable-length positional arguments packed into a **tuple**.
    - `**kwargs`: Variable-length keyword arguments packed into a **dictionary**.
- **3.7 Recursion and Recursive Problem Solving**:
  - 3.7.1 Recursive Function Anatomy:
    1. **Base Case(s)**: Termination condition returning directly without self-calls.
    2. **Recursive Case(s)**: Self-invocation with reduced parameters converging to base case.
  - 3.7.2 Call Stack Mechanics: Stack frames, pushing activation records, stack unwinding, `RecursionError` on stack overflow (default limit 1000).
  - 3.7.3 Classic Recursive Algorithms:
    - Factorial Calculation: $n! = n \times (n-1)!$ with $0! = 1$.
    - Fibonacci Sequence: $F(n) = F(n-1) + F(n-2)$ with $F(0)=0, F(1)=1$.
    - Greatest Common Divisor (Euclid's Algorithm): $\text{gcd}(a, b) = \text{gcd}(b, a \% b)$.
    - Sum of digits / String reversal via recursion.
  - 3.7.4 Recursion vs. Iteration: Time/space tradeoffs, call overhead, optimization via memoization.

#### 2. Visual Diagrams Required
- Diagram 3.1: Call Stack Frame Progression for `factorial(4)` (Pushing frames $4 \to 3 \to 2 \to 1$ and unwinding returns $1 \to 2 \to 6 \to 24$).
- Diagram 3.2: LEGB Scope Resolution Hierarchy.

#### 3. Required Programming Demonstrations
1. **Program 3.1**: Fruitful functions calculating compound interest and geometry formulas with `math` module.
2. **Program 3.2**: Variable scope demonstration contrasting local variables, global variables, and `global` keyword.
3. **Program 3.3**: Flexible utility function utilizing positional, keyword, default, and `*args` parameters.
4. **Program 3.4**: Recursive and iterative factorial implementations with stack trace printing.
5. **Program 3.5**: Recursive Euclid's GCD algorithm and Tower of Hanoi solver.

#### 4. Pedagogical Exam Preparation Elements
- **Exam Tips**: Differentiating parameters vs. arguments; identifying default parameters must follow non-default parameters (`def f(a=1, b):` is invalid `SyntaxError`); identifying void functions return `None`.
- **Common Mistakes Box**: Forgetting `return` statement in fruitful functions (defaults to `None`); modifying mutable default arguments across multiple calls; infinite recursion from missing/incorrect base cases.
- **Output Prediction Suite**: 5 Tricky recursive and scope-tracing code snippets.
- **Debugging Challenge**: 3 Functions with scope errors and recursion depth traps.
- **Graded Practice Problems**: 10 Problems.
- **Multiple Choice Questions (MCQs)**: 10 MCQs with analytical explanations.
- **25-Mark Unit Test**: Full paper with scoring rubric and solutions.

---

### PART IV / UNIT 4: Strings, Lists, Tuples & Dictionaries (Compound Data Structures)

#### 1. Unit Metadata & Topic Hierarchy
- **4.1 Unit Overview & Learning Objectives**
- **4.2 Strings as Compound Data Types**:
  - 4.2.1 Immutability of Strings, character encoding (ASCII/Unicode).
  - 4.2.2 Indexing & Length: Zero-based positive indexing (`0` to `len-1`), negative indexing (`-1` to `-len`).
  - 4.2.3 String Traversal: `for char in text:` vs. `for i in range(len(text)):`.
  - 4.2.4 Slicing Mechanics: `text[start:stop:step]`, boundary defaults, string inversion `text[::-1]`.
  - 4.2.5 Lexicographical Comparison: Comparison operators (`==`, `!=`, `<`, `>`) based on ASCII values (Uppercase < Lowercase).
  - 4.2.6 Built-in String Methods: `find()`, `index()`, `count()`, `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`, `startswith()`, `endswith()`.
  - 4.2.7 Looping & Counting Patterns: Character frequency counting, vowel/consonant counter.
- **4.3 Lists (Mutable Sequences)**:
  - 4.3.1 Definition, heterogenous elements, zero-based indexing.
  - 4.3.2 List Operations: Concatenation (`+`), Repetition (`*`), Membership (`in`, `not in`).
  - 4.3.3 List Slicing & Slice Assignment: In-place sub-list modification (`nums[1:3] = [20, 30]`).
  - 4.3.4 Deletion Methods:
    - `pop(index)`: Removes and returns element at index (defaults to last).
    - `del list[index]`: Removes element or slice by index without returning.
    - `remove(value)`: Searches and removes first occurrence of value (`ValueError` if absent).
    - `clear()`: Empties the list.
  - 4.3.5 Built-in List Methods: `append()`, `extend()`, `insert()`, `sort()`, `reverse()`, `index()`, `count()`.
  - 4.3.6 Passing Lists to Functions: Pass-by-object-reference, in-place modification vs. creating new lists.
  - 4.3.7 Nested Lists & 2D Matrices: Matrix representation, nested indexing `matrix[row][col]`, matrix addition/multiplication.
- **4.4 Tuples (Immutable Sequences)**:
  - 4.4.1 Definition, immutability, parenthesis syntax `()`.
  - 4.4.2 Single-Element Tuple Syntax: Trailing comma requirement `(item,)` vs. integer grouping `(item)`.
  - 4.4.3 Tuple Assignment (Unpacking): `a, b, c = (1, 2, 3)`, variable swapping `x, y = y, x`.
  - 4.4.4 Tuples as Return Values: Returning compound results (e.g., `divmod()`, `min_max()`).
  - 4.4.5 Tuple Immutability & Hashability (Tuples as dictionary keys).
- **4.5 Dictionaries (Key-Value Hash Mappings)**:
  - 4.5.1 Definition, mapping structure, key uniqueness, key immutability requirement (strings, numbers, tuples).
  - 4.5.2 Operations: Lookup `d[key]`, Assignment/Update `d[key] = val`, Deletion `del d[key]`, Membership testing on keys (`k in d`).
  - 4.5.3 Dictionary Methods: `keys()`, `values()`, `items()`, `get(key, default)` (safe lookup avoiding `KeyError`), `update()`, `pop()`.
  - 4.5.4 Sparse Matrix Representation: Storing non-zero matrix elements as `{(row, col): val}` to optimize memory.
- **4.6 Memory Semantics: Aliasing and Copying**:
  - 4.6.1 Aliasing: Multiple variables pointing to the identical memory address (`b = a`); mutations through `b` mutate `a`.
  - 4.6.2 Shallow Copy: Copying outer container references (`b = a[:]`, `b = list(a)`, `b = a.copy()`).
  - 4.6.3 Deep Copy: Recursive copying of all nested data structures via `copy.deepcopy()`.

#### 2. Visual Memory Models Required
- Diagram 4.1: List Memory Model (Contiguous reference array pointing to heap objects).
- Diagram 4.2: Aliasing vs. Shallow Copy vs. Deep Copy Memory Architecture.
- Diagram 4.3: Sparse Matrix 2D Grid vs. Dictionary Coordinate Map.

#### 3. Required Programming Demonstrations
1. **Program 4.1**: String parsing, palindrome check, vowel counter, and word capitalizer.
2. **Program 4.2**: List statistics suite (Mean, Median, Mode, Max, Min) and duplicate removal while preserving order.
3. **Program 4.3**: 2D Matrix addition, transpose, and matrix multiplication using nested lists.
4. **Program 4.4**: Word frequency counter for text files/paragraphs using dictionaries.
5. **Program 4.5**: Sparse matrix multiplication and addition using coordinate dictionaries.

#### 4. Pedagogical Exam Preparation Elements
- **Exam Tips**: Remembering tuples are immutable while lists are mutable; using `d.get(k, 0)` to prevent `KeyError`; identifying that single-element tuples require a comma `(5,)`.
- **Common Mistakes Box**: Trying to modify strings in-place (`s[0] = 'a'` raises `TypeError`); unintended side effects through list aliasing (`b = a`); confusing `append([1,2])` with `extend([1,2])`.
- **Output Prediction Suite**: 5 Slicing, aliasing, and dictionary mutation puzzles.
- **Debugging Challenge**: 3 Snippets with dictionary `KeyError`, list index out of range, and shallow copy bugs.
- **Graded Practice Problems**: 10 Problems.
- **Multiple Choice Questions (MCQs)**: 10 MCQs with analytical explanations.
- **25-Mark Unit Test**: Full paper with scoring rubric and solutions.

---

### PART V / UNIT 5: Object-Oriented Programming (Classes, Objects, Inheritance & Encapsulation)

#### 1. Unit Metadata & Topic Hierarchy
- **5.1 Unit Overview & Learning Objectives**
- **5.2 Introduction to Object-Oriented Programming (OOP)**:
  - 5.2.1 Programming Paradigms: Procedural vs. Object-Oriented paradigm.
  - 5.2.2 Core OOP Terminology:
    - **Class**: User-defined blueprint/prototype for creating objects.
    - **Object / Instance**: Concrete entity instantiated from a class with distinct state and shared behavior.
    - **Method**: Function defined inside a class operating on instances.
    - **Attribute**: Data variable bound to a class or instance.
- **5.3 Creating Classes and Instance Initialization**:
  - 5.3.1 Class Definition Syntax: `class ClassName:`.
  - 5.3.2 The `__init__()` Constructor Method: Automatic invocation upon instantiation, initializing object state.
  - 5.3.3 The `self` Parameter: Explicit reference to the current instance, attribute binding, method dispatching.
  - 5.3.4 Class Attributes (shared across all instances) vs. Instance Attributes (isolated in `self.__dict__`).
- **5.4 Creating and Using Instance Objects**:
  - 5.4.1 Instantiation syntax `obj = ClassName(args)`.
  - 5.4.2 Accessing attributes and invoking methods using the dot operator (`obj.attr`, `obj.method()`).
  - 5.4.3 Modifying and dynamically adding instance attributes.
  - 5.4.4 Standard Special Methods: `__str__()` (user-readable string), `__repr__()` (developer representation), `__len__()`, `__del__()`.
- **5.5 Class Inheritance**:
  - 5.5.1 Concepts: Base/Parent class vs. Derived/Child class, code reuse, "is-a" relationship.
  - 5.5.2 Inheritance Syntax: `class ChildClass(ParentClass):`.
  - 5.5.3 Single Inheritance, Multi-level Inheritance, Hierarchical Inheritance.
  - 5.5.4 The `isinstance()` and `issubclass()` built-in inspection functions.
- **5.6 Method Overriding & Superclass Delegation**:
  - 5.6.1 Method Overriding: Child class providing specialized implementation of parent method with identical name.
  - 5.6.2 The `super()` Function: Delegating calls to parent class methods (e.g., `super().__init__(...)`), Method Resolution Order (MRO).
- **5.7 Data Hiding & Encapsulation**:
  - 5.7.1 Encapsulation: Bundling data and methods into a single unit, restricting direct external access.
  - 5.7.2 Python Access Conventions:
    - **Public**: `self.name` (accessible anywhere).
    - **Protected**: `self._id` (single underscore, internal convention).
    - **Private**: `self.__pin` (double underscore, triggers **Name Mangling** to `_ClassName__pin`).
  - 5.7.3 Getters and Setters: Controlled attribute access and data validation.
- **5.8 Function & Method Overloading in Python**:
  - 5.8.1 Clarification of Python Language Mechanics: Python **does NOT support traditional method overloading** by parameter signature (subsequent `def` overwrites preceding definitions).
  - 5.8.2 Simulating Overloading in Python:
    1. Using Default Arguments (`b=None, c=None`).
    2. Using Variable-Length Arguments (`*args`).
    3. Type checking via `isinstance()`.

#### 2. Visual Diagrams Required
- Diagram 5.1: Class vs. Object Blueprint Architecture.
- Diagram 5.2: Inheritance Hierarchy & `super()` Call Propagation Tree.
- Diagram 5.3: Name Mangling & Encapsulation Memory Layout.

#### 3. Required Programming Demonstrations
1. **Program 5.1**: `Student` class with class attributes, instance attributes, methods, and `__str__` formatting.
2. **Program 5.2**: `BankAccount` class implementing private attributes (`__balance`), deposit/withdrawal validation, and getter methods.
3. **Program 5.3**: `Employee` parent class and `Manager` child class demonstrating single inheritance, `super().__init__()`, and method overriding.
4. **Program 5.4**: Shape hierarchy (`Shape` $\to$ `Rectangle`, `Circle`) demonstrating polymorphism and overridden `area()` methods.
5. **Program 5.5**: `Calculator` class demonstrating simulated method overloading via default arguments and `*args`.

#### 4. Pedagogical Exam Preparation Elements
- **Exam Tips**: Remembering `self` is the first parameter of every instance method; identifying that double underscore attributes are mangled to `_Class__attr`; knowing Python does not support multiple methods with the same name.
- **Common Mistakes Box**: Omitting `self` in method definitions; modifying class variables through an instance creating shadowing instance variables; forgetting to call `super().__init__()` in derived constructors.
- **Output Prediction Suite**: 5 OOP tracing questions testing inheritance, method overriding, and class vs. instance attributes.
- **Debugging Challenge**: 3 Broken OOP programs with `TypeError` and attribute shadowing errors.
- **Graded Practice Problems**: 10 Problems.
- **Multiple Choice Questions (MCQs)**: 10 MCQs with analytical explanations.
- **25-Mark Unit Test**: Full paper with scoring rubric and solutions.

---

### PART VI / UNIT 6: Files, Exception Handling & Regular Expressions

#### 1. Unit Metadata & Topic Hierarchy
- **6.1 Unit Overview & Learning Objectives**
- **6.2 File Handling (I/O Operations)**:
  - 6.2.1 Text Files vs. Binary Files, character encodings (UTF-8).
  - 6.2.2 Opening Files: The `open(filename, mode)` function. Modes:
    - `'r'`: Read (default, error if missing)
    - `'w'`: Write (creates new or truncates existing)
    - `'a'`: Append (writes at end)
    - `'r+'`: Read and Write
    - `'rb'`, `'wb'`: Binary read/write.
  - 6.2.3 The `with open(...) as f:` Context Manager: Automatic resource deallocation and guaranteed file closure.
  - 6.2.4 Writing Data to Files: `write(string)` vs. `writelines(list_of_strings)`. Converting variables to strings (`str()`, f-strings).
  - 6.2.5 Reading Data from Files: `read(size)`, `readline()`, `readlines()`, memory-efficient line iteration `for line in f:`.
  - 6.2.6 File Pointer Manipulation: `tell()` (current byte offset), `seek(offset, whence)` (repositioning pointer).
  - 6.2.7 Directory Operations (`os` Module): `os.getcwd()`, `os.mkdir()`, `os.listdir()`, `os.path.exists()`, `os.path.join()`, `os.remove()`.
  - 6.2.8 Object Serialization / Pickling (`pickle` Module): Pickling (`pickle.dump(obj, file)`) to byte stream in `'wb'` mode; Unpickling (`pickle.load(file)`) in `'rb'` mode.
- **6.3 Exception Handling**:
  - 6.3.1 Errors vs. Exceptions: Syntax errors (parsing time) vs. Exceptions (runtime errors).
  - 6.3.2 The `try-except` Architecture: Catching and handling runtime exceptions.
  - 6.3.3 Standard Built-in Exceptions: `ZeroDivisionError`, `FileNotFoundError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `AttributeError`, `IOError`.
  - 6.3.4 Multiple `except` Clauses: Handling specific exception types separately.
  - 6.3.5 The `else` and `finally` Blocks:
    - `else`: Executes only if `try` block completes with **no exceptions**.
    - `finally`: Guaranteed execution regardless of whether an exception occurred or was handled (cleanup tasks).
  - 6.3.6 Raising Exceptions: The `raise` keyword and custom error messages.
- **6.4 Regular Expressions (Pattern Matching with `re` Module)**:
  - 6.4.1 Concept of Regular Expressions: String searching, pattern matching, data validation.
  - 6.4.2 Metacharacters:
    - `.` Any character except newline
    - `^` Start of string, `$` End of string
    - `*` Zero or more, `+` One or more, `?` Zero or one
    - `{n,m}` Repetition bounds
    - `[]` Character set (e.g., `[a-zA-Z0-9]`, `[^0-9]`)
    - `|` Alternation (OR), `()` Grouping.
  - 6.4.3 Special Sequences: `\d` (digit), `\D` (non-digit), `\w` (word char), `\W` (non-word), `\s` (whitespace), `\S` (non-whitespace), `\b` (word boundary).
  - 6.4.4 Core `re` Module Functions:
    - `re.match(pattern, text)`: Matches **strictly at the start** of the string.
    - `re.search(pattern, text)`: Searches anywhere in the string for first match.
    - `re.findall(pattern, text)`: Returns list of all non-overlapping matches.
    - `re.finditer(pattern, text)`: Returns iterator of match objects with span indices.
    - `re.sub(pattern, replacement, text)`: Replaces matching patterns.
  - 6.4.5 Practical Web Scraping & Text Mining: Extracting email addresses (`r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]+"`), phone numbers, URLs from HTML/text.

#### 2. Visual Diagrams Required
- Diagram 6.1: File Access Modes Decision Tree (`r` vs `w` vs `a` vs `r+`).
- Diagram 6.2: Complete `try...except...else...finally` Execution Flowchart.
- Diagram 6.3: Regular Expression Matching Engine Progression (`re.match` vs `re.search` vs `re.findall`).

#### 3. Required Programming Demonstrations
1. **Program 6.1**: File copy utility that reads source text file, counts words/lines, and writes formatted uppercase output.
2. **Program 6.2**: Binary serialization using `pickle` to save and reload a dictionary database of student records.
3. **Program 6.3**: Robust mathematical calculator with full exception handling (`ZeroDivisionError`, `ValueError`, `try-except-else-finally`).
4. **Program 6.4**: Form validator checking email addresses, 10-digit mobile numbers, and passwords using Regex.
5. **Program 6.5**: Web scraping script extracting all email addresses and hyperlinks (`<a href="...">`) from raw HTML source.

#### 4. Pedagogical Exam Preparation Elements
- **Exam Tips**: Differentiating `re.match()` (only at start) from `re.search()` (anywhere); knowing `'w'` mode wipes existing content; remembering `pickle` requires binary modes (`wb`/`rb`).
- **Common Mistakes Box**: Forgetting to convert integers to strings before `f.write()`; opening non-existent files in `'r'` mode without `try-except`; confusing `re.match()` returning `None` with `re.findall()` returning `[]`.
- **Output Prediction Suite**: 5 File pointer (`seek`/`tell`), exception flow, and regex match puzzles.
- **Debugging Challenge**: 3 Programs with file leakage, uncaught exceptions, and faulty regex patterns.
- **Graded Practice Problems**: 10 Problems.
- **Multiple Choice Questions (MCQs)**: 10 MCQs with analytical explanations.
- **25-Mark Unit Test**: Full paper with scoring rubric and solutions.

---

## 4. Supplementary Pedagogical Parts Specification

### PART VII: Master Python Syntax, Methods & Standard Library Cheatsheet
- Complete quick-reference synthesis:
  - Table 7.1: Master Python Operators & Precedence Matrix
  - Table 7.2: Built-in Data Types, Mutability & Hashability Reference
  - Table 7.3: String, List, Tuple & Dictionary Built-in Methods Reference
  - Table 7.4: Math, Random & OS Standard Library Function Reference
  - Table 7.5: Exception Hierarchy & Common Built-in Error Types
  - Table 7.6: Regular Expression Metacharacters, Sequences & Methods Table.

### PART VIII: Cross-Unit Multi-Concept Practical Coding Challenges
- 15 Comprehensive, Multi-Unit Exam-Style Programming Problems integrating concepts across functions, data structures, OOP, file handling, and regex (e.g., Student Management System, Banking Transaction Ledger, Log File Parser with Regex).

### PART IX: Full-Length University Mock Examination Papers (100 Marks Each)
- **Mock Exam 1 (Mid-Term / End-Term University Standard - 100 Marks - 3 Hours)**:
  - Section A: 10 Short-Answer Compulsory Conceptual/Syntax Questions ($10 \times 2 = 20$ Marks)
  - Section B: 6 Medium Analytical / Output-Prediction / Code Problems ($6 \times 5 = 30$ Marks)
  - Section C: 5 Long Comprehensive Design & Implementation Programs ($5 \times 10 = 50$ Marks)
  - **Complete Worked Step-by-Step Scoring Solutions & Mark Distribution Rubrics**.
- **Mock Exam 2 (Challenging University Practical & Theory Pattern - 100 Marks - 3 Hours)**:
  - Sections A, B, and C with full marking schemes and verified executable solutions.

---

## 5. Comprehensive Syllabus Coverage & Audit Matrix

| Source Topic (from Units 1–6 Notes) | Blueprint Chapter & Section | Status | Notes & Clarifications |
| :--- | :--- | :---: | :--- |
| **Python Versions (Python 2 vs 3)** | Chapter 1 (Section 1.2.2) | ✓ INCLUDED | Preserves source history; highlights print & division differences |
| **Python Setup & PATH on Windows** | Chapter 1 (Section 1.2.3) | ✓ INCLUDED | Explains CLI PATH configuration and verification |
| **Running Hello World (REPL & Script)** | Chapter 1 (Section 1.2.4) | ✓ INCLUDED | Covers both IDLE/CMD interactive and `.py` script execution |
| **Variable Naming, Types & Keywords** | Chapter 1 (Section 1.3, 1.4) | ✓ INCLUDED | Exhaustive keyword list; `NameError` analysis |
| **Statements, Operators & PEMDAS** | Chapter 1 (Section 1.5) | ✓ INCLUDED | Floor division `//`, true division `/`, right-to-left `**` |
| **String Concatenation & Repetition** | Chapter 1 (Section 1.6) | ✓ INCLUDED | `+` and `*` operations; prohibited operations |
| **Composition & Comments** | Chapter 1 (Section 1.7) | ✓ INCLUDED | Single `#` and docstring `"""` comments |
| **Modulus Operator Applications** | Chapter 2 (Section 2.2) | ✓ INCLUDED | Parity, digit extraction, cyclic arithmetic |
| **Random Numbers (`random` module)** | Chapter 2 (Section 2.3) | ✓ INCLUDED | `random()`, `randint(a,b)`, `choice()` |
| **Boolean Expressions & Relational Ops** | Chapter 2 (Section 2.4) | ✓ INCLUDED | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| **Logic Operators (`and`, `or`, `not`)** | Chapter 2 (Section 2.5) | ✓ INCLUDED | Short-circuit evaluation rules and truth tables |
| **Conditionals (`if`, `if-else`, `if-elif`)** | Chapter 2 (Section 2.6) | ✓ INCLUDED | Single, alternative, chained, and nested conditionals |
| **While Loops, Infinite Loops, Break/Continue** | Chapter 2 (Section 2.7) | ✓ INCLUDED | Indefinite iteration; loop control jump statements |
| **For Loops & `range()` Function** | Chapter 2 (Section 2.8) | ✓ INCLUDED | Definite iteration; `range(start, stop, step)` |
| **Nested Loops (For & While)** | Chapter 2 (Section 2.9) | ✓ INCLUDED | 2D matrix/coordinate traversal, pattern printing |
| **Random Numbers in Loops (Games/Walks)** | Chapter 2 (Section 2.10) | ✓ INCLUDED | Guessing game and random walk algorithms |
| **Encapsulation & Generalization** | Chapter 2 (Section 2.11) | ✓ INCLUDED | Function wrapping and parameter generalization |
| **Function Calls & Flow of Execution** | Chapter 3 (Section 3.2) | ✓ INCLUDED | Caller vs callee, call stack, fruitful vs void (`None`) |
| **Type Conversion & Coercion** | Chapter 3 (Section 3.3) | ✓ INCLUDED | Implicit promotion vs explicit casting (`int`, `float`, `str`) |
| **Math Functions (`math` module)** | Chapter 3 (Section 3.4) | ✓ INCLUDED | `ceil`, `floor`, `sqrt`, `pow`, `fabs`, `sin`, `pi`, `e` |
| **Adding New Functions & Variable Scope** | Chapter 3 (Section 3.5) | ✓ INCLUDED | `def`, local vs global scope, LEGB resolution rule |
| **Parameters & Arguments (Positional/Keyword/Default/\*args)** | Chapter 3 (Section 3.6) | ✓ INCLUDED | All 4 argument types clearly distinguished |
| **Recursion, Base Case & Call Stack** | Chapter 3 (Section 3.7) | ✓ INCLUDED | Factorial, Fibonacci, GCD; stack overflow analysis |
| **Strings: Immutability, Traversal, Slices, Find** | Chapter 4 (Section 4.2) | ✓ INCLUDED | Zero-based indexing, slicing `[::]`, `find()`, counting |
| **Lists: Access, Operations, Slices, Deletion, Loops** | Chapter 4 (Section 4.3) | ✓ INCLUDED | `pop()`, `del`, `remove()`, nested 2D matrices |
| **Tuples: Immutability, Assignment Unpack, Returns** | Chapter 4 (Section 4.4) | ✓ INCLUDED | Trailing comma `(a,)`, swapping `a,b=b,a`, multiple returns |
| **Dictionaries: Keys, Operations, Methods, Sparse Matrices** | Chapter 4 (Section 4.5) | ✓ INCLUDED | `keys()`, `values()`, `items()`, `get()`, coordinate sparse maps |
| **Aliasing, Shallow Copy & Deep Copy** | Chapter 4 (Section 4.6) | ✓ INCLUDED | Pass-by-reference mutations vs `copy.deepcopy()` |
| **OOP Terminology: Class, Object, Instance, Method, Attr** | Chapter 5 (Section 5.2) | ✓ INCLUDED | Core OOP architectural foundations |
| **Creating Classes, `__init__`, `self`** | Chapter 5 (Section 5.3) | ✓ INCLUDED | Instance initialization, class vs instance attributes |
| **Creating Instances & Accessing Attributes** | Chapter 5 (Section 5.4) | ✓ INCLUDED | Dot operator, dynamic attributes, special methods |
| **Class Inheritance (Single/Multilevel)** | Chapter 5 (Section 5.5) | ✓ INCLUDED | Derived classes, code reuse, `isinstance` |
| **Overriding Methods & `super()`** | Chapter 5 (Section 5.6) | ✓ INCLUDED | Method overriding and superclass delegation |
| **Data Hiding, Private Attributes & Name Mangling** | Chapter 5 (Section 5.7) | ✓ INCLUDED | `_protected`, `__private`, `_Class__private` mangling |
| **Function Overloading Nuance & Simulation** | Chapter 5 (Section 5.8) | ✓ INCLUDED | Explains Python's lack of true overloading; simulates via defaults/\*args |
| **File Handling: Open, Read, Write, `with`** | Chapter 6 (Section 6.2) | ✓ INCLUDED | Modes `r`, `w`, `a`, `r+`, `read`, `readline`, `readlines` |
| **Directories (`os` module) & Pickling (`pickle`)** | Chapter 6 (Section 6.2) | ✓ INCLUDED | `getcwd`, `mkdir`, `dump`, `load`, binary modes `wb`/`rb` |
| **Exception Handling (`try-except-else-finally`)** | Chapter 6 (Section 6.3) | ✓ INCLUDED | `ZeroDivisionError`, `FileNotFoundError`, `ValueError` |
| **Regular Expressions (`re` module, Metacharacters)** | Chapter 6 (Section 6.4) | ✓ INCLUDED | `\d`, `\w`, `\s`, `*`, `+`, `?`, `[]`, `^`, `$` |
| **`re.match()`, `re.search()`, `re.findall()`** | Chapter 6 (Section 6.4) | ✓ INCLUDED | Strict start matching vs global search |
| **Web Scraping via Regex** | Chapter 6 (Section 6.4) | ✓ INCLUDED | Extracting emails, links, and structured tags from HTML |

---

## 6. Ambiguities & Technical Clarifications Identified in Source Material

1. **Method Overloading in Python (Unit 5)**:
   - *Source Observation*: Unit 5 includes a section titled "Function Overloading".
   - *Technical Fact*: Python does **not** natively support traditional compile-time function overloading by parameter signature (a subsequent function definition with the same name replaces the previous one).
   - *Blueprint Resolution*: The blueprint accurately explains this Python language design decision and formally teaches how to **simulate overloading** using default arguments (`None`), variable-length positional arguments (`*args`), and type inspection (`isinstance()`), matching both LPU exam expectations and Python reality.
2. **Python 2 Legacy References (Unit 1)**:
   - *Source Observation*: Unit 1 notes discuss differences between Python 2 and Python 3.
   - *Technical Fact*: Python 2 was officially sunset on January 1, 2020.
   - *Blueprint Resolution*: Python 2 differences (e.g., `print` as statement vs function, integer division truncation `3/2 = 1` vs `1.5`) are treated as historical context and exam comparison points, while all actual code and syntax throughout the textbook strictly adhere to modern Python 3 standards.
3. **Single-Element Tuples (Unit 4)**:
   - *Source Observation*: Trailing comma syntax is easily missed by students.
   - *Blueprint Resolution*: Explicitly highlighted in syntax boxes and common mistakes (`t = (5)` is an `int`, while `t = (5,)` is a `tuple`).

---

## 7. Textbook Dimensions & Production Scope

- **Total Academic Units**: 6 Core Units + 3 Supplementary Reference/Exam Modules (9 Parts total)
- **Estimated Book Length**: **160–220 Pages** (Unconstrained by artificial page limits, prioritizing complete line-by-line code explanations, visual ASCII/memory models, and complete solutions).
- **Target Typesetting Engine**: Two-pass `pdflatex` via `INT108/Makefile`.
