import os

content = r'''\chapter{Conditional Statements, Iterative Statements \& Algorithms}
\label{chap:conditionals-loops-algorithms}

% ==============================================================================
% SECTION 2.1: OVERVIEW \& OBJECTIVES
% ==============================================================================
\section{Unit Overview \& Learning Objectives}

\begin{conceptbox}[Unit 2 Academic Scope \lpuBadge]
Control flow structures form the decision-making and iterative backbone of computer algorithms. This unit covers relational and logical operators with short-circuit evaluation, branching selection structures (\texttt{if}, \texttt{if-else}, \texttt{if-elif-else}, and ternary conditional expressions), indefinite iteration via \texttt{while} loops, definite iteration via \texttt{for} loops and \texttt{range()}, nested multi-loop mechanics, 2D pattern generation, number theory algorithms, pseudorandom simulations, and software engineering abstractions (encapsulation and generalization).
\end{conceptbox}

\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Modulus \& Number Theory}: Utilize remainder arithmetic for parity checking, digit stripping, Armstrong/palindrome verification, cyclic arithmetic, and negative modulus calculations.
    \item \textbf{Pseudorandom Generation}: Implement randomized algorithms and Monte Carlo approximations using the standard \texttt{random} module.
    \item \textbf{Boolean Logic \& Branching}: Evaluate truth expressions, truthy/falsy values, prevent short-circuit evaluation traps, and build multi-way selection trees.
    \item \textbf{Iterative Loops}: Design terminating \texttt{while} and \texttt{for} loops, utilize \texttt{break}, \texttt{continue}, and \texttt{pass}, and trace nested loops with sentinel control.
    \item \textbf{2D Pattern Generation}: Program right-angled triangles, full pyramids, diamonds, and Pascal's triangle.
    \item \textbf{Algorithmic Abstraction}: Apply encapsulation and generalization to refactor repetitive code into reusable, parameterized functions.
\end{itemize}

% ==============================================================================
% SECTION 2.2: MODULUS OPERATOR APPLICATIONS
% ==============================================================================
\section{The Modulus Operator \& Number Theory Applications}

In mathematical computations, we often care not just about the quotient of a division, but the exact remainder left over. This is exactly what the modulus operator provides. At its core, modulus is the foundation for determining cyclic patterns, checking divisibility, and stripping digits from numbers---making it one of the most heavily tested concepts in computer science problem solving. 

When you perform division, for example $14 \div 3$, the quotient is $4$ and the remainder is $2$. In Python, you can extract these two components separately using the floor division (\texttt{//}) and modulus (\texttt{\%}) operators. While it may seem like a simple mathematical tool, the modulus operator serves as the logical backbone for parity checking (is it even or odd?), cyclic bounds (clock wrapping), and parsing numerical structures without converting them to strings.

Understanding the modulus operator requires a firm grasp of how Python handles division, especially when dealing with negative integers. This is a common point of confusion for students and a frequent source of exam traps.

\begin{syntaxbox}[Modulus Operator]
remainder = dividend % divisor
\end{syntaxbox}

\subsection{Negative Operand Modulus (The Floor Division Trap)}

Unlike languages such as C or Java which use truncated division, Python uses \textbf{floor division} under the hood. Floor division always rounds \textit{down} (towards negative infinity). Because of the mathematical identity \texttt{dividend = quotient * divisor + remainder}, the remainder must have the same sign as the \textbf{divisor}.

Let us examine what happens when negative numbers are involved. If we evaluate \texttt{-7 // 3}, the true mathematical division is $-2.333\dots$. Rounding down towards negative infinity yields $-3$. Therefore, the remainder is \texttt{-7 - (-3 * 3) = -7 - (-9) = 2}. 

\begin{pythoncode}{Negative Modulus Behavior}
# Positive dividend and divisor
print("7 % 3   =", 7 % 3)

# Negative dividend, positive divisor (Result takes sign of divisor: Positive)
print("-7 % 3  =", -7 % 3)

# Positive dividend, negative divisor (Result takes sign of divisor: Negative)
print("7 % -3  =", 7 % -3)

# Negative dividend and divisor
print("-7 % -3 =", -7 % -3)
\end{pythoncode}

\begin{outputbox}
7 % 3   = 1
-7 % 3  = 2
7 % -3  = -2
-7 % -3 = -1
\end{outputbox}

\begin{examtip}[Negative Modulus Rule]
In Python, the result of \texttt{a \% b} always takes the algebraic sign of the \textbf{divisor} \texttt{b}, regardless of the sign of \texttt{a}. If you see \texttt{x \% 3}, the answer will always be $0, 1,$ or $2$. If you see \texttt{x \% -3}, the answer will always be $0, -1,$ or $-2$.
\end{examtip}

\subsection{Essential Computational Patterns}
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Parity Testing (Even / Odd)}:
    \begin{pythoncode}{Even and Odd Verification}
n = 14
if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")
    \end{pythoncode}
    \begin{outputbox}
14 is Even
    \end{outputbox}

    \item \textbf{Digit Extraction \& Number Reversal}:
    \begin{itemize}
        \item \texttt{n \% 10} extracts the last (units) digit of integer $n$.
        \item \texttt{n // 10} removes the last digit from $n$.
    \end{itemize}
    \begin{pythoncode}{Reversing an Integer via Modulus}
number = 1234
reversed_num = 0

while number > 0:
    digit = number % 10          # Extract right-most digit
    reversed_num = (reversed_num * 10) + digit
    number = number // 10        # Truncate right-most digit

print("Reversed Number:", reversed_num)
    \end{pythoncode}
    \begin{outputbox}
Reversed Number: 4321
    \end{outputbox}
    \item \textbf{Cyclic \& Clock Arithmetic}:
    Wrap-around calculations (such as days of the week or 24-hour clocks) use modulus:
    \begin{equation*}
        \text{future\_hour} = (\text{current\_hour} + \text{hours\_elapsed}) \pmod{24}
    \end{equation*}
\end{enumerate}

% ==============================================================================
% SECTION 2.3: RANDOM NUMBERS
% ==============================================================================
\section{Pseudorandom Number Generation (\texttt{random} Module)}

Computers are inherently deterministic machines, meaning that given the exact same input and initial state, they will consistently produce the exact same output. This predictability is a cornerstone of computing, but it poses a challenge when we want to simulate unpredictability---such as rolling a die, dealing cards in a game, or modeling chaotic physical systems. To introduce randomness into our programs, we rely on software algorithms that generate sequences of numbers that only \textit{appear} to be random.

Python accomplishes this via the built-in \texttt{random} module. The randomness generated is technically \textbf{pseudorandom}, as it is generated by a complex deterministic algorithm known as the Mersenne Twister. By default, it uses the current system time as a "seed" to kick off the mathematical sequence, ensuring that each execution of the program yields a seemingly unpredictable, unique set of numbers.

Using random numbers allows programmers to simulate Monte Carlo approximations, build intelligent adversary bots in video games, and test algorithms under varying inputs. A solid grasp of the \texttt{random} module's functions is essential for crafting interactive, dynamic applications.

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{l>{\raggedright\arraybackslash}Xl}
\toprule
\textbf{Function Call} & \textbf{Mathematical Range \& Behavior} & \textbf{Example Output} \\
\midrule
\texttt{random.random()} & Floating-point number $x \in [0.0, 1.0)$ & \texttt{0.73291...} \\
\texttt{random.randint(a, b)} & Integer $N \in [a, b]$ (\textbf{Both $a$ and $b$ inclusive!}) & \texttt{random.randint(1, 6)} $\to$ \texttt{4} \\
\texttt{random.randrange(start, stop, step)} & Integer from \texttt{range(start, stop, step)} & \texttt{random.randrange(0, 10, 2)} $\to$ \texttt{6} \\
\texttt{random.choice(sequence)} & Random element from non-empty list, string, or tuple & \texttt{random.choice(['H', 'T'])} $\to$ \texttt{'H'} \\
\bottomrule
\end{tabularx}
\caption{Key Functions in Python's Standard \texttt{random} Module.}
\label{tab:random-functions}
\end{table}

\begin{examtip}[\texttt{randint} vs. \texttt{randrange} Endpoint Trap]
\begin{itemize}
    \item \texttt{random.randint(1, 10)} CAN return \textbf{10} (inclusive of upper bound).
    \item \texttt{random.randrange(1, 10)} will ONLY return values from $1$ to $9$ (exclusive of upper bound $10$, following standard \texttt{range()} rules).
\end{itemize}
\end{examtip}

% ==============================================================================
% SECTION 2.4: BOOLEAN EXPRESSIONS \& LOGIC
% ==============================================================================
\section{Boolean Expressions \& Logical Operators}

Programming frequently requires algorithms to verify conditions before proceeding with an execution path. Is the user's age greater than 18? Is the calculated score above the passing threshold? Has the game reached level 10? These questions are mathematically answered using Boolean logic, a subset of algebra formalized by George Boole. In Python, logical questions evaluate down to one of two fundamental truth values represented by the \texttt{bool} type: \texttt{True} or \texttt{False}.

Relational operators form the building blocks of Boolean expressions by allowing us to compare two operands. Once we have primitive comparison results, we use logical operators (\texttt{and}, \texttt{or}, \texttt{not}) to combine them into complex, multifaceted conditions. However, Python's implementation of logic contains powerful nuances---such as truthy/falsy evaluation and short-circuiting---that extend far beyond basic arithmetic comparisons.

\subsection{Relational (Comparison) Operators}

Relational operators compare two operands and evaluate to a Boolean truth value (\texttt{True} or \texttt{False}):

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\linewidth}{cllX}
\toprule
\textbf{Operator} & \textbf{Description} & \textbf{True Example} & \textbf{False Example} \\
\midrule
\texttt{==} & Equal to & \texttt{5 == 5} $\to$ \texttt{True} & \texttt{5 == 3} $\to$ \texttt{False} \\
\texttt{!=} & Not equal to & \texttt{5 != 3} $\to$ \texttt{True} & \texttt{5 != 5} $\to$ \texttt{False} \\
\texttt{>} & Strictly Greater than & \texttt{8 > 3} $\to$ \texttt{True} & \texttt{3 > 8} $\to$ \texttt{False} \\
\texttt{<} & Strictly Less than & \texttt{2 < 7} $\to$ \texttt{True} & \texttt{7 < 2} $\to$ \texttt{False} \\
\texttt{>=} & Greater than or equal to & \texttt{5 >= 5} $\to$ \texttt{True} & \texttt{4 >= 5} $\to$ \texttt{False} \\
\texttt{<=} & Less than or equal to & \texttt{3 <= 5} $\to$ \texttt{True} & \texttt{6 <= 5} $\to$ \texttt{False} \\
\bottomrule
\end{tabularx}
\caption{Python Relational Comparison Operators.}
\label{tab:relational-ops}
\end{table}

\subsection{Truthy and Falsy Values}

Python evaluates all objects in a boolean context implicitly. You do not always need a strict relational comparison like \texttt{x == 0}. Instead, Python designates certain "empty" or "zero" values as \textbf{falsy}, while almost everything else is \textbf{truthy}.

The following values inherently evaluate to \texttt{False}:
\begin{itemize}
    \item Numeric zero types: \texttt{0}, \texttt{0.0}
    \item Empty sequences/collections: \texttt{""} (empty string), \texttt{[]} (empty list), \texttt{\{\}} (empty dictionary)
    \item The \texttt{None} singleton
\end{itemize}

\begin{pythoncode}{Truthy and Falsy Contexts}
name = ""
if name:
    print(f"Hello {name}")
else:
    print("Name is an empty string (Falsy value!)")

items = [1, 2]
if items:
    print("The list has elements (Truthy value!)")
\end{pythoncode}
\begin{outputbox}
Name is an empty string (Falsy value!)
The list has elements (Truthy value!)
\end{outputbox}

\subsection{Logical Operators: Operand Returns and Short-Circuit Evaluation}

A critical detail missed by many beginners is that Python's \texttt{and} / \texttt{or} operators \textbf{do not necessarily return \texttt{True} or \texttt{False}}. Instead, they return one of the actual operands being evaluated based on their truthiness.

\begin{itemize}[leftmargin=1.5em]
    \item \textbf{\texttt{or} Operator}: Returns the \textbf{first truthy operand}, or the last operand if all are falsy.
    \item \textbf{\texttt{and} Operator}: Returns the \textbf{first falsy operand}, or the last operand if all are truthy.
\end{itemize}

\begin{pythoncode}{Logical Operators Returning Operands}
# OR returns the first truthy value
result1 = "cat" or "dog"
print("'cat' or 'dog' ->", result1)

result2 = 0 or "text"
print("0 or 'text'    ->", result2)

# AND returns the first falsy value (or last if all truthy)
result3 = 0 and "text"
print("0 and 'text'   ->", result3)

result4 = "apple" and "banana"
print("'apple' and 'banana' ->", result4)
\end{pythoncode}
\begin{outputbox}
'cat' or 'dog' -> cat
0 or 'text'    -> text
0 and 'text'   -> 0
'apple' and 'banana' -> banana
\end{outputbox}

\begin{examtip}[Logical Operator Returns]
Never assume \texttt{and}/\texttt{or} return \texttt{bool}. \texttt{"apple" and "banana"} evaluates to \texttt{"banana"} because both are truthy, and \texttt{and} returns the final evaluated operand. \texttt{"" or "cherry"} returns \texttt{"cherry"} because the first operand is falsy.
\end{examtip}

\textbf{Short-Circuit Rule}:
\begin{itemize}
    \item In \texttt{A and B}, if \texttt{A} is \texttt{False}, Python immediately returns \texttt{A} without evaluating \texttt{B}.
    \item In \texttt{A or B}, if \texttt{A} is \texttt{True}, Python immediately returns \texttt{A} without evaluating \texttt{B}.
\end{itemize}

\begin{pythoncode}{Short-Circuit Evaluation Preventing Division by Zero}
x = 0
y = 10

# Safe short-circuit: x != 0 evaluates to False, so y / x is NEVER computed
if x != 0 and (y / x) > 2:
    print("Condition met")
else:
    print("Safely avoided ZeroDivisionError via short-circuiting!")
\end{pythoncode}
\begin{outputbox}
Safely avoided ZeroDivisionError via short-circuiting!
\end{outputbox}

% ==============================================================================
% SECTION 2.5: CONDITIONAL STATEMENTS
% ==============================================================================
\section{Conditional Execution (Selection Structures)}

In linear programming, instructions are executed one after the other in top-to-bottom sequence. Conditional statements disrupt this strict sequential flow by allowing programs to dynamically choose which blocks of code to execute based on runtime evaluations. This capability—referred to as a selection structure or a branch—makes programs reactive and intelligent.

Whenever a program encounters a decision point, it evaluates a boolean condition. If the condition is met (\texttt{True}), the program branches down a specific path. If not (\texttt{False}), it can fall back to alternative paths. Python relies strictly on whitespace indentation to define which lines of code belong to which path, eschewing the curly braces \texttt{\{\}} found in C and Java. 

\subsection{The \texttt{if}, \texttt{if-else}, and \texttt{if-elif-else} Statements}

The simplest selection structure is the standalone \texttt{if} statement, which executes a block of code only when the condition is truthy. The \texttt{if-else} statement adds a mutually exclusive alternative. For more complex, multi-way decisions, we use the \texttt{if-elif-else} chain, ensuring that only the \textit{first} true condition triggers its block, skipping all subsequent checks.

\begin{syntaxbox}[Chained Conditional Structure]
if condition\_1:
    statement\_block\_1
elif condition\_2:
    statement\_block\_2
elif condition\_3:
    statement\_block\_3
else:
    fallback\_statement\_block
\end{syntaxbox}

\begin{pythoncode}{Student Grade Classification Program}
# Grade evaluation using chained conditionals
score = float(input("Enter exam score (0-100): "))
# Let's assume input was 75 for this example run

if score >= 90:
    grade = "A+ (Outstanding)"
elif score >= 80:
    grade = "A (Excellent)"
elif score >= 70:
    grade = "B (Good)"
elif score >= 60:
    grade = "C (Satisfactory)"
elif score >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Re-appear)"

print(f"Final Academic Grade: {grade}")
\end{pythoncode}
\begin{outputbox}
Enter exam score (0-100): 75
Final Academic Grade: B (Good)
\end{outputbox}

\subsection{Conditional Expressions (Ternary Operator)}
Python supports concise inline conditional expressions, often referred to as the ternary operator. This is exceptionally useful for variable assignments that depend on a simple binary condition, reducing four lines of \texttt{if-else} logic into a single expressive line.

\begin{syntaxbox}[Ternary Expression]
result\_value = true\_value if condition else false\_value
\end{syntaxbox}

\begin{pythoncode}{Ternary Operator in Action}
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Inline parity check
num = 15
parity = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {parity}")
\end{pythoncode}
\begin{outputbox}
Status: Adult
15 is Odd
\end{outputbox}

% ==============================================================================
% SECTION 2.6: ITERATIVE STATEMENTS (WHILE \& FOR LOOPS)
% ==============================================================================
\section{Iterative Statements: While and For Loops}

While conditionals allow a program to make decisions, iteration allows a program to perform repetitive tasks efficiently. Without loops, processing one thousand student records would require writing one thousand identical blocks of code. Iteration constructs abstract away this redundancy.

Python provides two primary looping architectures: \textbf{indefinite iteration} (\texttt{while} loops) and \textbf{definite iteration} (\texttt{for} loops). A \texttt{while} loop runs an unknown number of times until a specific condition fails, making it ideal for event-driven programming and validating user input. A \texttt{for} loop, conversely, iterates over a pre-determined collection of elements or a fixed numerical range, making it perfect for traversing arrays, strings, and mathematical series.

Additionally, Python provides specialized loop control keywords—\texttt{break}, \texttt{continue}, \texttt{pass}, and an unusual loop-\texttt{else} construct—that grant granular control over the iteration lifecycle.

\subsection{While Loops (Indefinite Iteration)}

A \texttt{while} loop evaluates its boolean condition before every single pass. As long as the condition remains \texttt{True}, the body executes. If the condition never becomes \texttt{False}, the loop runs infinitely, which is a classic logical error causing programs to freeze.

\begin{syntaxbox}[While Loop Syntax]
initialization
while loop\_condition:
    loop\_body\_statements
    state\_update
\end{syntaxbox}

\begin{conceptbox}[The Four Essential Components of a Loop]
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Initialization}: Setting control variable(s) before loop entry (e.g., \texttt{count = 0}).
    \item \textbf{Evaluation}: Testing condition before each iteration (e.g., \texttt{count < 5}).
    \item \textbf{Body Execution}: Performing the computational task.
    \item \textbf{State Update}: Modifying the control variable toward termination (e.g., \texttt{count += 1}). Missing this causes an **Infinite Loop**.
\end{enumerate}
\end{conceptbox}

\subsection{For Loops \& The \texttt{range()} Function (Definite Iteration)}

A \texttt{for} loop iterates over a predetermined sequence of elements. In Python, counting loops are driven by the built-in \texttt{range()} sequence generator:

\begin{syntaxbox}[The range() Function Generator]
range(stop)                \# Generates: 0, 1, 2, ..., stop - 1
range(start, stop)         \# Generates: start, start + 1, ..., stop - 1
range(start, stop, step)   \# Generates: start, start + step, ..., up to stop - 1
\end{syntaxbox}

\begin{pythoncode}{Using range() in For Loops}
# 1. Basic 0 to 4
for i in range(5):
    print(i, end=" ")
print()

# 2. Start from 2 up to 10 with step 2
for even in range(2, 11, 2):
    print(even, end=" ")
print()

# 3. Counting down from 5 to 1
for countdown in range(5, 0, -1):
    print(countdown, end=" ")
print("-> Blast off!")
\end{pythoncode}

\begin{outputbox}
0 1 2 3 4 
2 4 6 8 10 
5 4 3 2 1 -> Blast off!
\end{outputbox}

\subsection{Accumulator Patterns}

Loops are frequently used to aggregate data over multiple iterations. The \textbf{accumulator pattern} initializes a variable outside the loop, then incrementally updates it within the loop to compute a running sum, product, or count.

\begin{pythoncode}{Accumulator Pattern Variations}
# Sum and Product Accumulators
total_sum = 0
total_product = 1
even_count = 0

for num in range(1, 6):
    total_sum += num         # Running sum
    total_product *= num     # Running product
    if num % 2 == 0:
        even_count += 1      # Counter

print("Sum (1 to 5):", total_sum)
print("Product (1 to 5):", total_product)
print("Even numbers count:", even_count)
\end{pythoncode}
\begin{outputbox}
Sum (1 to 5): 15
Product (1 to 5): 120
Even numbers count: 2
\end{outputbox}

\subsection{Loop Control Statements: \texttt{break}, \texttt{continue}, \texttt{pass}, and \texttt{else}}

\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{\texttt{break}}: Terminates loop execution immediately and transfers control to the statement following the loop.
    \item \textbf{\texttt{continue}}: Immediately stops the current iteration and jumps directly to the next iteration's condition test.
    \item \textbf{\texttt{pass}}: A null operation placeholder. Used when the syntax requires a statement, but no logical action is needed.
    \item \textbf{The Loop \texttt{else} Clause}: An optional block attached to a \texttt{for} or \texttt{while} loop that executes **only if the loop completes normally without encountering a \texttt{break}**.
\end{enumerate}

\begin{pythoncode}{Standalone break, continue, and pass}
print("--- Continue Demo (Skip 3) ---")
for i in range(1, 6):
    if i == 3:
        continue  # Skip printing 3
    print(i, end=" ")

print("\n\n--- Pass Demo ---")
for i in range(2):
    pass  # Placeholder, does nothing
print("Pass successfully executed without syntax error.")
\end{pythoncode}
\begin{outputbox}
--- Continue Demo (Skip 3) ---
1 2 4 5 

--- Pass Demo ---
Pass successfully executed without syntax error.
\end{outputbox}

\begin{pythoncode}{Prime Number Testing Using for...else}
# Prime check using loop else clause
num = 29
is_prime = True

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is composite (divisible by {i})")
            break
    else:
        # Executes ONLY if no 'break' was hit
        print(f"{num} is a PRIME number!")
else:
    print(f"{num} is not prime.")
\end{pythoncode}
\begin{outputbox}
29 is a PRIME number!
\end{outputbox}

\subsection{Sentinel-Controlled Loops}

Sometimes the termination condition is not known until the middle of the loop. A \textbf{sentinel-controlled loop} utilizes the \texttt{while True:} idiom with an internal \texttt{if condition: break} statement.

\begin{pythoncode}{Sentinel-Controlled Loop}
total = 0
print("Enter numbers to sum (type 0 to stop).")
# For this example run, inputs are: 5, 8, 0

while True:
    val = int(input("> "))
    if val == 0:
        print("Sentinel value detected. Stopping.")
        break
    total += val

print("Final Total:", total)
\end{pythoncode}
\begin{outputbox}
Enter numbers to sum (type 0 to stop).
> 5
> 8
> 0
Sentinel value detected. Stopping.
Final Total: 13
\end{outputbox}

% ==============================================================================
% SECTION 2.7: NESTED LOOPS \& 2D PATTERNS
% ==============================================================================
\section{Nested Loops \& 2D Pattern Generation}

Complex algorithms often require multi-dimensional traversal, such as processing rows and columns in a spreadsheet or rendering pixels on a screen. We achieve this by nesting loops. When a loop resides inside another loop, the \textbf{inner loop completes all of its iterations from start to finish for every single step of the outer loop}.

To master nested loops, you must be able to mentally trace variable state changes. Loop invariants and trace tables are vital tools for mapping how inner bounds depend dynamically on the outer loop index.

\begin{pythoncode}{Generating Classic Geometric Patterns}
# 1. Centered Full Star Pyramid
n = 5
print("--- Centered Pyramid ---")
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# 2. Diamond Pattern
print("\n--- Diamond Pattern ---")
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# 3. Floyd's Number Triangle
print("\n--- Floyd's Triangle ---")
val = 1
for r in range(1, 5):
    for c in range(1, r + 1):
        print(f"{val:2d}", end=" ")
        val += 1
    print()
\end{pythoncode}

\begin{outputbox}
--- Centered Pyramid ---
    *
   ***
  *****
 *******
*********

--- Diamond Pattern ---
   *
  ***
 *****
*******
 *****
  ***
   *

--- Floyd's Triangle ---
  1 
  2  3 
  4  5  6 
  7  8  9 10 
\end{outputbox}

% ==============================================================================
% SECTION 2.8: NUMBER THEORY \& SIMULATIONS
% ==============================================================================
\section{Number Theory Algorithms \& Randomized Simulations}

\subsection{Armstrong and Palindrome Number Verification}

Many classic interview and exam problems involve integer parsing without casting variables to strings. Using modulus and floor division within a while loop allows us to efficiently extract digits.

\begin{pythoncode}{Armstrong and Palindrome Verification via Modulus}
def is_armstrong(n):
    '''Checks if sum of digits raised to power of digit count equals n.'''
    temp = n
    digit_count = len(str(n))  # Just to get the power
    digit_sum = 0
    
    while temp > 0:
        digit = temp % 10
        digit_sum += digit ** digit_count
        temp //= 10
        
    return digit_sum == n

def is_palindrome_num(n):
    '''Checks if integer reads the same forwards and backwards using arithmetic.'''
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n //= 10
    return original == reversed_num

print("153 Armstrong?", is_armstrong(153))    # 1^3 + 5^3 + 3^3 = 153 -> True
print("1634 Armstrong?", is_armstrong(1634))  # 1^4 + 6^4 + 3^4 + 4^4 = 1634 -> True
print("12321 Palindrome?", is_palindrome_num(12321)) # True
\end{pythoncode}
\begin{outputbox}
153 Armstrong? True
1634 Armstrong? True
12321 Palindrome? True
\end{outputbox}

\subsection{Number Guessing Game (Interactive Loop Simulation)}

Combining the \texttt{random} module with a \texttt{while} loop produces dynamic simulations and games.

\begin{pythoncode}{Number Guessing Game}
import random

target = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10!")
# Simulating user input loop for 5, then 7
guesses = [5, 7] 

for guess in guesses:
    attempts += 1
    print(f"\nAttempt {attempts}: User guessed {guess}")
    
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print(f"Correct! You found it in {attempts} tries.")
        break
\end{pythoncode}
\begin{outputbox}
Guess the number between 1 and 10!

Attempt 1: User guessed 5
Too low!

Attempt 2: User guessed 7
Correct! You found it in 2 tries.
\end{outputbox}

\subsection{Monte Carlo \texorpdfstring{$\pi$}{Pi} Approximation Simulation}
\begin{pythoncode}{Monte Carlo Pi Simulation using random.random()}
import random

def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = random.random() # Float in [0, 1)
        y = random.random() # Float in [0, 1)
        # Distance from origin in unit square quadrant
        if (x**2 + y**2) <= 1.0:
            inside_circle += 1
    # Ratio of quadrant area to square area is pi / 4
    pi_estimate = 4 * (inside_circle / num_samples)
    return pi_estimate

print(f"Estimated Pi (100,000 samples): {estimate_pi(100000):.4f}")
\end{pythoncode}
\begin{outputbox}
Estimated Pi (100,000 samples): 3.1419
\end{outputbox}

% ==============================================================================
% SECTION 2.9: ENCAPSULATION AND GENERALIZATION
% ==============================================================================
\section{Encapsulation and Generalization}

Writing scripts directly in the global scope leads to messy, unmaintainable spaghetti code. As your algorithms grow in complexity, you must modularize them. Software abstraction involves identifying reusable logic and formalizing it so it can be deployed flexibly. Two fundamental principles guide this process: Encapsulation and Generalization.

Encapsulation packages a specific set of operations into an isolated, named functional block. It separates the implementation details (\textit{how} something is done) from the execution (\textit{when} it is done). Generalization extends this concept by substituting fixed, hardcoded values with variable parameters, dramatically expanding the utility of the encapsulated code across diverse problem scenarios.

\begin{conceptbox}[Software Abstraction Workflow]
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Encapsulation}: Isolating a block of code (such as a pattern generator or mathematical algorithm) inside a named function.
    \item \textbf{Generalization}: Replacing hardcoded constants (e.g., repeating 4 times for a square) with dynamic parameters (\texttt{n} sides and \texttt{length}) so the function solves a broader class of problems (any regular polygon).
\end{itemize}
\end{conceptbox}

\begin{pythoncode}{Encapsulation and Generalization Progression}
# Step 1: Raw Unencapsulated Code
for _ in range(4):
    print("*" * 4)

# Step 2: Encapsulated Function (Hardcoded for 4x4 Square)
def print_square():
    for _ in range(4):
        print("*" * 4)

# Step 3: Generalized Function (Handles any NxM Rectangle with any Character)
def print_rectangle(rows, cols, symbol="*"):
    '''Prints a generalized rectangle of size rows x cols using symbol.'''
    for _ in range(rows):
        print(symbol * cols)

print_rectangle(3, 8, "#")
\end{pythoncode}
\begin{outputbox}
########
########
########
\end{outputbox}

% ==============================================================================
% SECTION 2.10: EXAM TIPS \& PITFALLS
% ==============================================================================
\section{Exam Tips \& Common Student Pitfalls}

\begin{examtip}[Unit 2 University Traps]
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Logical Operands}: Remember that \texttt{and}/\texttt{or} return the operand values, not \texttt{True}/\texttt{False}. \texttt{0 or 5} returns \texttt{5}.
    \item \textbf{Relational vs Assignment}: Writing \texttt{if x = 5:} causes an immediate \texttt{SyntaxError}. Always use \texttt{if x == 5:}.
    \item \textbf{The \texttt{range()} Exclusion}: \texttt{range(1, 5)} generates numbers $1, 2, 3, 4$ (NOT $5$).
    \item \textbf{Loop \texttt{else} Execution}: The \texttt{else} block of a loop is skipped ONLY when the loop exits via an executed \texttt{break} statement. If the loop condition is False on the first check, \texttt{else} runs immediately.
    \item \textbf{Negative Modulus}: \texttt{-5 \% 3} evaluates to \texttt{1}, because the remainder takes the sign of the divisor.
\end{itemize}
\end{examtip}

% ==============================================================================
% SECTION 2.11: OUTPUT PREDICTION \& DEBUGGING
% ==============================================================================
\section{Output Prediction \& Debugging Challenges}

\begin{outputprediction}[Nested Loops and Break Tracing]
\textbf{Question}: What will be printed by the following code?
\begin{lstlisting}[language=Python3]
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue
        if i + j == 5:
            break
        print(f"{i}-{j}", end=" ")
    print()
\end{lstlisting}
\textbf{Answer \& Step Tracing}:
\begin{itemize}
    \item $i=1$: $j=1$ (skip due to $i==j$), $j=2$ (prints \texttt{1-2}), $j=3$ (prints \texttt{1-3}). Output line 1: \texttt{1-2 1-3}
    \item $i=2$: $j=1$ (prints \texttt{2-1}), $j=2$ (skip due to $i==j$), $j=3$ ($i+j=5 \implies$ break inner loop). Output line 2: \texttt{2-1}
    \item $i=3$: $j=1$ (prints \texttt{3-1}), $j=2$ ($i+j=5 \implies$ break inner loop). Output line 3: \texttt{3-1}
\end{itemize}
\end{outputprediction}

\begin{outputprediction}[Logical Returns]
\textbf{Question}: What is the output of \texttt{print("Apple" and "" or 0 or [1])}? \\
\textbf{Answer}: \texttt{[1]}. Tracing: \texttt{"Apple" and ""} returns \texttt{""} (first falsy). Next, \texttt{"" or 0} returns \texttt{0} (last falsy). Finally, \texttt{0 or [1]} returns \texttt{[1]} (first truthy).
\end{outputprediction}

\begin{outputprediction}[Range Slicing Loop]
\textbf{Question}: Output of \texttt{for i in range(10, 0, -3): print(i, end=" ")}? \\
\textbf{Answer}: \texttt{10 7 4 1}.
\end{outputprediction}

\begin{outputprediction}[While Else Trap]
\textbf{Question}: What is printed?
\begin{lstlisting}[language=Python3]
x = 5
while x < 5:
    print(x)
    x += 1
else:
    print("Done")
\end{lstlisting}
\textbf{Answer}: \texttt{Done}. The loop condition is False immediately, so the loop doesn't run, but no \texttt{break} is hit, so the \texttt{else} block executes immediately.
\end{outputprediction}

\begin{outputprediction}[Truthy Modulus]
\textbf{Question}: \texttt{if 12 \% 3: print("A") else: print("B")} \\
\textbf{Answer}: \texttt{B}. \texttt{12 \% 3} is \texttt{0}, which is falsy, executing the \texttt{else} block.
\end{outputprediction}

\begin{debuggingbox}[Fixing Infinite While Loops]
\textbf{Buggy Code}:
\begin{lstlisting}[language=Python3]
# Sum all even numbers between 1 and 10
total = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        total += i
        i += 1
print("Even Sum:", total)
\end{lstlisting}
\textbf{Diagnosis \& Correction}:
When $i=1$, $i\%2 == 0$ is False. The \texttt{i += 1} inside the \texttt{if} block is skipped, so $i$ remains $1$ forever, resulting in an **infinite loop**. The increment \texttt{i += 1} must occur outside the \texttt{if} block:
\begin{lstlisting}[language=Python3]
total = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        total += i
    i += 1 # Correct: Increments on every iteration
print("Even Sum:", total)
\end{lstlisting}
\end{debuggingbox}

\begin{debuggingbox}[Variable Shadowing]
\textbf{Buggy Code}:
\begin{lstlisting}[language=Python3]
for i in range(3):
    for i in range(2):
        print(i, end=" ")
\end{lstlisting}
\textbf{Diagnosis \& Correction}: The inner loop shadows the outer loop variable \texttt{i}, which resets its value. Rename the inner loop variable to \texttt{j}.
\end{debuggingbox}

\begin{debuggingbox}[Incorrect Equality Checks]
\textbf{Buggy Code}: \texttt{if name = "Admin": print("Welcome")} \\
\textbf{Diagnosis}: Assignment \texttt{=} instead of equality \texttt{==} causes a \texttt{SyntaxError}.
\end{debuggingbox}

% ==============================================================================
% SECTION 2.12: GRADED PRACTICE PROBLEMS \& SOLUTIONS
% ==============================================================================
\section{Graded Programming Practice Problems \& Solutions}

\begin{practiceset}[Unit 2 Programming Exercises]
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Level 1 (Foundation)}: Write a program that checks whether a given year is a **Leap Year** (divisible by 4, but not 100 unless also divisible by 400).
    \item \textbf{Level 1 (Foundation)}: Write a program that prints the multiplication table for any input integer up to multiplier 12 using a \texttt{for} loop.
    \item \textbf{Level 2 (Standard)}: Write a Python program to calculate the factorial of an integer $N$ using a \texttt{while} loop.
    \item \textbf{Level 2 (Standard)}: Write a program to check if an input integer is an **Armstrong Number** (e.g., $153 = 1^3 + 5^3 + 3^3$) using digit extraction.
    \item \textbf{Level 3 (Exam Tier)}: Write a program to find and display all prime numbers in a user-defined interval $[A, B]$ using nested loops.
    \item \textbf{Level 3 (Exam Tier)}: Write a program to print Pascal's Triangle up to $N$ rows using nested loops.
    \item \textbf{Level 4 (Challenge)}: Implement a complete automated Rock-Paper-Scissors game against the computer with best-of-5 scoring using the \texttt{random} module and \texttt{while} loops.
\end{enumerate}
\end{practiceset}

\subsection{Complete Step-by-Step Worked Solutions \& Test Cases}

\begin{solutionbox}[Solutions to Unit 2 Practice Problems]

\noindent\textbf{Problem 1: Leap Year Logic}
\begin{lstlisting}[language=Python3]
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a LEAP YEAR.")
else:
    print(f"{year} is NOT a leap year.")
\end{lstlisting}
\textbf{Test Cases}:
\begin{tabular}{|l|l|l|}
\hline Input & Expected Output & Logic \\
\hline 2024 & LEAP YEAR & Div by 4, not 100 \\
\hline 1900 & NOT a leap year & Div by 100, not 400 \\
\hline 2000 & LEAP YEAR & Div by 400 \\
\hline
\end{tabular}

\vspace{10pt}
\noindent\textbf{Problem 2: Multiplication Table}
\begin{lstlisting}[language=Python3]
n = int(input("Enter number: "))
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")
\end{lstlisting}
\textbf{Test Cases}:
\begin{tabular}{|l|l|l|}
\hline Input & Expected Output & Type \\
\hline 5 & 5 x 1 = 5 ... 5 x 12 = 60 & Normal \\
\hline 0 & 0 x 1 = 0 ... 0 x 12 = 0 & Edge Case \\
\hline
\end{tabular}

\vspace{10pt}
\noindent\textbf{Problem 3: Factorial via While Loop}
\begin{lstlisting}[language=Python3]
n = int(input("Enter positive integer: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial is: {fact}")
\end{lstlisting}
\textbf{Test Cases}:
\begin{tabular}{|l|l|l|}
\hline Input & Expected Output & Type \\
\hline 5 & 120 & Normal \\
\hline 0 & 1 & Base Case \\
\hline
\end{tabular}

\vspace{10pt}
\noindent\textbf{Problem 4: Armstrong Number}
\begin{lstlisting}[language=Python3]
n = int(input("Enter number: "))
temp = n
power = len(str(n))
total = 0
while temp > 0:
    total += (temp % 10) ** power
    temp //= 10
if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")
\end{lstlisting}
\textbf{Test Cases}:
\begin{tabular}{|l|l|l|}
\hline Input & Expected Output & Logic \\
\hline 153 & Armstrong & $1^3+5^3+3^3 = 153$ \\
\hline 1634 & Armstrong & $1^4+6^4+3^4+4^4 = 1634$ \\
\hline 100 & Not Armstrong & $1^3+0+0 \neq 100$ \\
\hline
\end{tabular}

\vspace{10pt}
\noindent\textbf{Problem 5: Prime Range Filter}
\begin{lstlisting}[language=Python3]
start = int(input("Enter start: "))
end = int(input("Enter end: "))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()
\end{lstlisting}
\textbf{Test Cases}:
\begin{tabular}{|l|l|l|}
\hline Input & Expected Output & Type \\
\hline 10, 20 & 11 13 17 19 & Normal Range \\
\hline -5, 5 & 2 3 5 & Negatives \\
\hline
\end{tabular}

\vspace{10pt}
\noindent\textbf{Problem 6: Pascal's Triangle}
\begin{lstlisting}[language=Python3]
n = int(input("Rows: "))
for i in range(n):
    print(" " * (n - i), end="")
    c = 1
    for j in range(i + 1):
        print(c, end=" ")
        c = c * (i - j) // (j + 1)
    print()
\end{lstlisting}
\textbf{Test Cases}: Input 3 => `   1 \n  1 1 \n 1 2 1`.

\vspace{10pt}
\noindent\textbf{Problem 7: Rock-Paper-Scissors Best of 5}
\begin{lstlisting}[language=Python3]
import random
choices = ['Rock', 'Paper', 'Scissors']
user_score = comp_score = rounds = 0

while user_score < 3 and comp_score < 3:
    rounds += 1
    comp = random.choice(choices)
    user = input("Rock, Paper, or Scissors? ").capitalize()
    
    if user == comp:
        print("Tie!")
    elif (user=='Rock' and comp=='Scissors') or \
         (user=='Paper' and comp=='Rock') or \
         (user=='Scissors' and comp=='Paper'):
        user_score += 1
        print("You win this round!")
    else:
        comp_score += 1
        print("Computer wins this round!")

print(f"Final Score -> You: {user_score}, Computer: {comp_score}")
\end{lstlisting}
\end{solutionbox}

% ==============================================================================
% SECTION 2.13: MULTIPLE CHOICE QUESTIONS
% ==============================================================================
\section{Multiple Choice Questions (MCQs)}

\begin{enumerate}[leftmargin=1.5em]
    \item Which operator checks whether two expressions are equal?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{=} \quad (b) \texttt{==} \quad (c) \texttt{is equal} \quad (d) \texttt{:=}
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{\texttt{==} is the relational equality comparison operator.}

    \item What is the range of values produced by \texttt{random.randint(1, 5)}?
    \begin{enumerate}[label=(\alph*)]
        \item 1, 2, 3, 4 \quad (b) 1, 2, 3, 4, 5 \quad (c) 0, 1, 2, 3, 4 \quad (d) 0, 1, 2, 3, 4, 5
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{\texttt{randint(a, b)} includes both endpoints $a$ and $b$.}

    \item Which logical operator has the highest precedence in Python?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{and} \quad (b) \texttt{or} \quad (c) \texttt{not} \quad (d) \texttt{xor}
    \end{enumerate}
    \textbf{Answer}: (c) --- \textit{\texttt{not} precedes \texttt{and}, which precedes \texttt{or}.}

    \item What happens when \texttt{break} is executed inside a nested inner loop?
    \begin{enumerate}[label=(\alph*)]
        \item Terminates all loops \quad (b) Terminates only the innermost loop \quad (c) Skips one iteration \quad (d) Restarts the outer loop
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{\texttt{break} terminates only the innermost enclosing loop.}

    \item How many times will the loop \texttt{for i in range(1, 10, 3):} execute?
    \begin{enumerate}[label=(\alph*)]
        \item 3 times \quad (b) 4 times \quad (c) 10 times \quad (d) 2 times
    \end{enumerate}
    \textbf{Answer}: (a) --- \textit{Values generated are $1, 4, 7$ (total 3 iterations).}

    \item What is printed by: \texttt{for i in range(2): pass; print(i)}?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{0} \quad (b) \texttt{1} \quad (c) \texttt{2} \quad (d) Error
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{The loop completes at $i=1$; \texttt{pass} does nothing; \texttt{1} is printed.}

    \item In a \texttt{while...else} structure, when does the \texttt{else} block execute?
    \begin{enumerate}[label=(\alph*)]
        \item Always \quad (b) Only if loop terminates without \texttt{break} \quad (c) Only if loop condition was False initially \quad (d) Never
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{The \texttt{else} block executes only upon normal loop termination.}

    \item What is the value of \texttt{15 \% 4}?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{3} \quad (b) \texttt{3.75} \quad (c) \texttt{4} \quad (d) \texttt{1}
    \end{enumerate}
    \textbf{Answer}: (a) --- \textit{$15 = (4 \times 3) + 3$, so remainder is $3$.}

    \item What is the term for wrapping code inside a reusable function?
    \begin{enumerate}[label=(\alph*)]
        \item Generalization \quad (b) Encapsulation \quad (c) Polymorphism \quad (d) Recursion
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{Encapsulation is packaging code into a named function.}

    \item What is the output of \texttt{False or not False and True}?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{False} \quad (b) \texttt{True} \quad (c) \texttt{None} \quad (d) \texttt{Error}
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{\texttt{not False} is \texttt{True}; \texttt{True and True} is \texttt{True}; \texttt{False or True} is \texttt{True}.}
\end{enumerate}

% ==============================================================================
% SECTION 2.14: SELF-ASSESSMENT UNIT TEST
% ==============================================================================
\section{Self-Assessment Unit Test}

\begin{chaptertest}[Unit 2 Examination (25 Marks --- 45 Minutes)]
\noindent\textbf{Section A: Short Answer Concepts ($3 \times 2 = 6\text{ Marks}$)}
\begin{enumerate}
    \item Explain short-circuit evaluation in Python with a code example.
    \item Differentiate between the \texttt{break} and \texttt{continue} statements.
    \item What is the purpose of the \texttt{else} clause in a \texttt{for} loop?
\end{enumerate}

\medskip
\noindent\textbf{Section B: Code Tracing \& Output Prediction ($3 \times 3 = 9\text{ Marks}$)}
\begin{enumerate}[start=4]
    \item Predict the output of the following code:
    \begin{lstlisting}[language=Python3]
x = 1
while x < 20:
    x = x * 2 + 1
    if x % 3 == 0:
        continue
    print(x, end=" ")
    \end{lstlisting}
    \item Trace the output of this nested loop:
    \begin{lstlisting}[language=Python3]
for i in range(3, 0, -1):
    print("*" * i)
    \end{lstlisting}
    \item Differentiate \texttt{random.randint(1, 6)} and \texttt{random.randrange(1, 6)}.
\end{enumerate}

\medskip
\noindent\textbf{Section C: Comprehensive Programming Problem ($1 \times 10 = 10\text{ Marks}$)}
\begin{enumerate}[start=7]
    \item Write a complete Python program to generate the first $N$ terms of the Fibonacci sequence ($0, 1, 1, 2, 3, 5, 8, \dots$), validate that $N > 0$ using an \texttt{if} condition, and compute the running sum of all even-valued Fibonacci terms generated.
\end{enumerate}
\end{chaptertest}

\subsection{Unit Test Complete Solutions \& Rubric}

\begin{solutionbox}[Complete Solutions for Unit 2 Test]
\noindent\textbf{Section A Solutions}:
\begin{enumerate}
    \item \textbf{Short-Circuit Evaluation} [2 Marks]: Python stops evaluating logical expressions as soon as the outcome is determined. In \texttt{A and B}, if \texttt{A} is \texttt{False}, \texttt{B} is never evaluated. In \texttt{A or B}, if \texttt{A} is \texttt{True}, \texttt{B} is skipped.
    \item \textbf{Break vs. Continue} [2 Marks]: \texttt{break} terminates the loop completely; \texttt{continue} skips only the remaining statements of the current iteration and jumps to the next iteration.
    \item \textbf{Loop Else Clause} [2 Marks]: The \texttt{else} block of a loop executes when the loop finishes all iterations naturally without being terminated by a \texttt{break}.
\end{enumerate}

\noindent\textbf{Section B Solutions}:
\begin{enumerate}[start=4]
    \item \textbf{While Loop Tracing} [3 Marks]:
    \begin{itemize}
        \item Start $x=1$. Iter 1: $x = 1(2)+1 = 3$. $3\%3==0 \implies$ skip print.
        \item Iter 2: $x = 3(2)+1 = 7$. $7\%3 \ne 0 \implies$ prints \texttt{7}.
        \item Iter 3: $x = 7(2)+1 = 15$. $15\%3==0 \implies$ skip print.
        \item Iter 4: $x = 15(2)+1 = 31$. $31\%3 \ne 0 \implies$ prints \texttt{31}.
        \item Next check: $x < 20$ fails ($31 \not< 20$). Printed: \texttt{7 31}.
    \end{itemize}
    \item \textbf{Nested Star Output} [3 Marks]:
    \begin{itemize}
        \item $i=3 \implies \texttt{***}$
        \item $i=2 \implies \texttt{**}$
        \item $i=1 \implies \texttt{*}$
    \end{itemize}
    \item \textbf{Random Endpoint Analysis} [3 Marks]: \texttt{randint(1, 6)} generates integers in $\{1,2,3,4,5,6\}$ (both inclusive). \texttt{randrange(1, 6)} generates in $\{1,2,3,4,5\}$ ($6$ is excluded).
\end{enumerate}

\noindent\textbf{Section C Solution}:
\begin{enumerate}[start=7]
    \item \textbf{Fibonacci \& Even Sum Program} [10 Marks]:
\begin{lstlisting}[language=Python3]
n = int(input("Enter number of terms N: "))

if n <= 0:
    print("Invalid input! N must be a positive integer.")
else:
    a, b = 0, 1
    even_sum = 0
    print("Fibonacci Sequence:", end=" ")
    
    for i in range(n):
        print(a, end=" ")
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b
        
    print(f"\nSum of Even Fibonacci terms: {even_sum}")
\end{lstlisting}
\textbf{Marking Scheme}: Input validation: 2M; Loop \& Fibonacci update logic: 5M; Even check \& sum calculation: 3M.
\end{enumerate}
\end{solutionbox}
'''

with open("/Users/abhidinkale/Documents/mark p1/INT108/chapters/chapter-02-conditionals-loops-algorithms.tex", "w", encoding="utf-8") as f:
    f.write(content)

print("Chapter updated successfully.")
