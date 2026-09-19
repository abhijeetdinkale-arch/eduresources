import os

os.makedirs("PHY175/chapters", exist_ok=True)

# ==============================================================================
# CHAPTER 3: EXPANDED NUMBER SYSTEMS AND LOGIC GATES
# ==============================================================================
ch3 = r"""\chapter{Introduction to Number Systems and Logic Gates}
\label{chap:number_systems_logic}

\section{Introduction and Theoretical Foundations}
Digital computation, microprocessors, and embedded systems process information exclusively in discrete binary representations. In this chapter, we develop the rigorous mathematical foundations of positional number systems, specialized binary codes (BCD, Excess-3, Gray code), radix and diminished radix complements, signed arithmetic, IEEE 754 floating-point standards, Boolean algebraic theorems, canonical forms, Karnaugh map (K-map) optimization, Quine-McCluskey tabular minimization, and hardware logic hazard elimination.

\section{Positional Number Systems and Radix Conversions}
\subsection{Mathematical Formulation of Base-$r$ Systems}
In a positional numeral system with radix (base) $r \in \mathbb{Z}^+$ ($r \ge 2$), any real number $N$ is represented as a polynomial sequence of digits $d_i$:
\begin{equation}
    (N)_r = \sum_{i=-m}^{n-1} d_i r^i = d_{n-1} r^{n-1} + d_{n-2} r^{n-2} + \dots + d_1 r^1 + d_0 r^0 + d_{-1} r^{-1} + \dots + d_{-m} r^{-m}
\end{equation}
where each digit $d_i \in \{0, 1, \dots, r-1\}$.
\begin{itemize}
    \item \textbf{Binary ($r = 2$):} Digits $\{0, 1\}$.
    \item \textbf{Octal ($r = 8$):} Digits $\{0, 1, 2, 3, 4, 5, 6, 7\}$ (Each octal digit maps to 3 binary bits: $2^3 = 8$).
    \item \textbf{Decimal ($r = 10$):} Digits $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.
    \item \textbf{Hexadecimal ($r = 16$):} Digits $\{0-9, \text{A}(10), \text{B}(11), \text{C}(12), \text{D}(13), \text{E}(14), \text{F}(15)\}$ (Each hex digit maps to 4 binary bits: $2^4 = 16$).
\end{itemize}

\subsection{Systematic Base Conversion Algorithms}
\begin{enumerate}
    \item \textbf{Radix-$r$ to Decimal Conversion:} Directly evaluate the polynomial expansion $\sum d_i r^i$.
    \item \textbf{Decimal to Radix-$r$ Integer Conversion (Successive Division):} Divide the decimal integer repeatedly by base $r$. The sequence of remainders read from bottom to top (last remainder to first) forms the radix-$r$ number (MSB to LSB).
    \item \textbf{Decimal to Radix-$r$ Fraction Conversion (Successive Multiplication):} Multiply the fractional part repeatedly by base $r$. The sequence of generated integer parts read from top to bottom forms the fractional radix-$r$ digits.
    \item \textbf{Binary $\leftrightarrow$ Octal $\leftrightarrow$ Hexadecimal Conversions:} Group binary bits in sets of 3 (for octal) or 4 (for hex), starting from the radix point and moving outward (left for integer, right for fraction, zero-padding outer ends as needed).
\end{enumerate}

\section{Specialized Binary Codes}
\subsection{Binary Coded Decimal (BCD 8421)}
In BCD 8421, each decimal digit ($0-9$) is encoded as an independent 4-bit weighted binary nibble with weights $8, 4, 2, 1$.
\begin{itemize}
    \item Decimal $0$ to $9$ are represented by $0000_2$ to $1001_2$.
    \item The six 4-bit combinations $1010_2$ to $1111_2$ ($10$ to $15$) are \textbf{illegal/invalid BCD codes}.
    \item \textbf{BCD Addition Rule:} If 4-bit binary addition of two BCD digits produces a sum $\ge 10_{10}$ or generates a binary carry-out ($C=1$), the result is corrected by adding $+6$ ($0110_2$) to skip the 6 illegal states.
\end{itemize}

\subsection{Excess-3 Code (XS-3)}
Excess-3 is an unweighted binary code derived by adding decimal $3$ ($0011_2$) to each BCD digit:
\begin{equation}
    \text{XS-3}(D) = \text{BCD}(D) + 0011_2
\end{equation}
\begin{conceptbox}[Self-Complementing Property of Excess-3 Code]
Excess-3 is a \textbf{self-complementing code}: the 1's complement (bitwise inversion) of an Excess-3 codeword directly produces the 9's complement of the corresponding decimal digit:
\begin{equation}
    \overline{\text{XS-3}(D)} = \text{XS-3}(9 - D)
\end{equation}
For example, for $D=2$ ($\text{XS-3} = 0101_2$), bitwise inversion gives $1010_2$, which is $\text{XS-3}(7) = \text{XS-3}(9-2)$. This simplifies decimal subtraction in early computing hardware.
\end{conceptbox}

\subsection{Gray Code (Reflected Binary Code)}
Gray code is an unweighted, non-arithmetic code in which two consecutive numerical values differ by \textbf{only a single bit} (unit Hamming distance).

\begin{derivationbox}[Binary-to-Gray and Gray-to-Binary Conversion Algorithms]
\begin{enumerate}
    \item \textbf{Binary to Gray Conversion:}
    Given an $n$-bit binary word $B = B_{n-1} B_{n-2} \dots B_1 B_0$:
    \begin{align}
        G_{n-1} &= B_{n-1} \quad (\text{MSB remains unchanged}) \\
        G_i &= B_{i+1} \oplus B_i \quad \text{for } i = n-2, n-3, \dots, 0
    \end{align}
    \item \textbf{Gray to Binary Conversion:}
    Given an $n$-bit Gray code word $G = G_{n-1} G_{n-2} \dots G_1 G_0$:
    \begin{align}
        B_{n-1} &= G_{n-1} \quad (\text{MSB remains unchanged}) \\
        B_i &= B_{i+1} \oplus G_i \quad \text{for } i = n-2, n-3, \dots, 0
    \end{align}
\end{enumerate}
Gray codes prevent multi-bit transient glitches in optical rotary shaft encoders and asynchronous FIFO pointer synchronization across clock domains.
\end{derivationbox}

\section{Complements, Signed Arithmetic, and Floating-Point Formats}
\subsection{Radix and Diminished Radix Complements}
For an $n$-digit base-$r$ integer $N$:
\begin{enumerate}
    \item \textbf{Diminished Radix Complement ($(r-1)$'s Complement):}
    \begin{equation}
        (r-1)\text{'s Complement} = (r^n - 1) - N
    \end{equation}
    In binary ($r=2$), the 1's complement is obtained by inverting every bit ($0 \leftrightarrow 1$).
    \item \textbf{Radix Complement ($r$'s Complement):}
    \begin{equation}
        r\text{'s Complement} = r^n - N = [(r^n - 1) - N] + 1 = (r-1)\text{'s Complement} + 1
    \end{equation}
    In binary ($r=2$), the 2's complement is obtained by inverting all bits and adding $1$ to the LSB:
    \begin{equation}
        \text{2's Complement}(N) = \bar{N} + 1
    \end{equation}
\end{enumerate}

\subsection{Signed Binary Number Representations}
For an $n$-bit signed binary word:
\begin{table}[htbp]
\centering
\small
\caption{Comparison of $n$-bit Signed Number Systems}
\label{tab:signed_systems}
\begin{tabularx}{\textwidth}{lXXX}
\toprule
\textbf{Representation} & \textbf{Dynamic Number Range} & \textbf{Zero Representations} & \textbf{Arithmetic Complexity} \\
\midrule
\textbf{Signed Magnitude} & $-(2^{n-1}-1) \text{ to } +(2^{n-1}-1)$ & Two ($+0 = 00\dots0, -0 = 10\dots0$) & High (requires sign comparison) \\
\textbf{1's Complement} & $-(2^{n-1}-1) \text{ to } +(2^{n-1}-1)$ & Two ($+0 = 00\dots0, -0 = 11\dots1$) & Requires end-around carry \\
\textbf{2's Complement} & $-2^{n-1} \text{ to } +(2^{n-1}-1)$ & \textbf{Unique} ($0000\dots0$) & Standard unified adder/subtractor \\
\bottomrule
\end{tabularx}
\end{table}

\begin{derivationbox}[2's Complement Subtraction and Overflow Detection]
To compute subtraction $A - B$ using an $n$-bit adder:
\begin{equation}
    A - B = A + (\bar{B} + 1)
\end{equation}
\begin{itemize}
    \item If a final carry-out occurs ($C_n = 1$), it is discarded, and the result is positive.
    \item If no carry-out occurs ($C_n = 0$), the result is negative and in 2's complement form.
    \item \textbf{Signed Overflow Detection ($V$):}
    When adding two numbers of the same sign, an overflow occurs if the result has the opposite sign:
    \begin{equation}
        V = C_n \oplus C_{n-1}
    \end{equation}
    where $C_n$ is the carry out of the MSB (sign bit) and $C_{n-1}$ is the carry into the MSB. An overflow ($V = 1$) indicates that the true arithmetic result exceeds the representable range $[-2^{n-1}, +2^{n-1}-1]$.
\end{itemize}
\end{derivationbox}

\subsection{IEEE 754 Floating-Point Standard}
Real floating-point numbers in modern microprocessors are formatted under the IEEE 754 binary standard:
\begin{itemize}
    \item \textbf{Single Precision (32-bit):}
    \begin{itemize}
        \item 1 Sign bit ($S$, $0 = +, 1 = -$);
        \item 8 Exponent bits ($E$), stored with bias $127$ ($E = e + 127$);
        \item 23 Mantissa Fraction bits ($F$), with implicit leading 1 ($1.F$).
        \begin{equation}
            \text{Value} = (-1)^S \times (1.F)_2 \times 2^{E - 127}
        \end{equation}
    \end{itemize}
    \item \textbf{Double Precision (64-bit):} 1 sign bit, 11 exponent bits (bias $1023$), and 52 fraction bits.
\end{itemize}

\section{Logic Gates, Universal Gates, and Boolean Algebra}
\subsection{Primary and Special Logic Gates}
\begin{itemize}
    \item \textbf{Primary Gates:}
    \begin{itemize}
        \item \textbf{AND Gate:} $Y = A \cdot B$ (Output is 1 if and only if all inputs are 1).
        \item \textbf{OR Gate:} $Y = A + B$ (Output is 1 if any input is 1).
        \item \textbf{NOT Gate (Inverter):} $Y = \bar{A}$ (Output is the logical inversion of the input).
    \end{itemize}
    \item \textbf{Universal Gates:}
    \begin{itemize}
        \item \textbf{NAND Gate:} $Y = \overline{A \cdot B}$.
        \item \textbf{NOR Gate:} $Y = \overline{A + B}$.
        Any arbitrary Boolean function can be synthesized using exclusively NAND or exclusively NOR gates.
    \end{itemize}
    \item \textbf{Special Exclusive Gates:}
    \begin{itemize}
        \item \textbf{XOR Gate (Odd Parity Detector):} $Y = A \oplus B = \bar{A}B + A\bar{B}$. Output is 1 when inputs differ.
        \item \textbf{XNOR Gate (Equivalence Gate):} $Y = A \odot B = \overline{A \oplus B} = AB + \bar{A}\bar{B}$. Output is 1 when inputs are identical.
    \end{itemize}
\end{itemize}

\subsection{Fundamental Postulates and Theorems of Boolean Algebra}
\begin{table}[htbp]
\centering
\small
\caption{Key Theorems and Axioms of Boolean Algebra}
\label{tab:boolean_theorems}
\begin{tabularx}{\textwidth}{lXX}
\toprule
\textbf{Theorem Name} & \textbf{AND Form} & \textbf{OR Form} \\
\midrule
\textbf{Identity Law} & $A \cdot 1 = A$ & $A + 0 = A$ \\
\textbf{Null / Annihilation Law} & $A \cdot 0 = 0$ & $A + 1 = 1$ \\
\textbf{Idempotent Law} & $A \cdot A = A$ & $A + A = A$ \\
\textbf{Complementarity Law} & $A \cdot \bar{A} = 0$ & $A + \bar{A} = 1$ \\
\textbf{Involution Law} & $\overline{\overline{A}} = A$ & --- \\
\textbf{Commutative Law} & $A \cdot B = B \cdot A$ & $A + B = B + A$ \\
\textbf{Associative Law} & $A(BC) = (AB)C$ & $A + (B + C) = (A + B) + C$ \\
\textbf{Distributive Law} & $A + BC = (A+B)(A+C)$ & $A(B+C) = AB + AC$ \\
\textbf{Absorption Law} & $A(A + B) = A$ & $A + AB = A$ \\
\textbf{Elimination Law} & $A(\bar{A} + B) = AB$ & $A + \bar{A}B = A + B$ \\
\textbf{Consensus Theorem} & $(A+B)(\bar{A}+C)(B+C) = (A+B)(\bar{A}+C)$ & $AB + \bar{A}C + BC = AB + \bar{A}C$ \\
\textbf{De Morgan's Laws} & $\overline{A \cdot B} = \bar{A} + \bar{B}$ & $\overline{A + B} = \bar{A} \cdot \bar{B}$ \\
\bottomrule
\end{tabularx}
\end{table}

\section{Canonical Forms and Karnaugh Map (K-Map) Optimization}
\subsection{Canonical Minterms and Maxterms}
For an $n$-variable Boolean function $F(x_1, x_2, \dots, x_n)$:
\begin{itemize}
    \item \textbf{Minterm ($m_i$):} A product term containing all $n$ literals in either true or complemented form that equals 1 for exactly one row of the truth table.
    \item \textbf{Maxterm ($M_i$):} A sum term containing all $n$ literals in either true or complemented form that equals 0 for exactly one row of the truth table.
    \item Relationship: $M_i = \overline{m_i}$.
    \item \textbf{Canonical Sum-of-Products (SOP):} $F = \sum m(\text{indices where } F=1)$.
    \item \textbf{Canonical Product-of-Sums (POS):} $F = \prod M(\text{indices where } F=0)$.
\end{itemize}

\subsection{Karnaugh Map Minimization Principles}
A Karnaugh Map is a 2D graphical representation of a truth table arranged in \textbf{Gray code order} ($00, 01, 11, 10$) so that adjacent cells differ by exactly one binary variable.

\begin{conceptbox}[Rules for K-Map Grouping]
\begin{enumerate}
    \item Group size must be an integer power of 2 ($1, 2, 4, 8, 16$).
    \item Groups must be rectangular or square; diagonal grouping is strictly invalid.
    \item Groups wrap around edges and corners (toroidal adjacency).
    \item Groups should be made as large as possible to eliminate the maximum number of literals ($2^k$ cells eliminate $k$ variables).
    \item Every 1-cell must be included in at least one group.
    \item \textbf{Prime Implicant (PI):} A rectangular group of $2^k$ 1-cells that cannot be merged into a larger valid group.
    \item \textbf{Essential Prime Implicant (EPI):} A Prime Implicant that contains at least one 1-cell not covered by any other prime implicant. All EPIs must appear in the minimal SOP expression.
    \item \textbf{Don't Care Conditions ($d$):} Input combinations that cannot occur or whose outputs are irrelevant may be treated as 1s (to enlarge groups) or 0s (to avoid creating extra groups).
\end{enumerate}
\end{conceptbox}

\section{Logic Hazards and Glitch Elimination}
\subsection{Static-1, Static-0, and Dynamic Hazards}
In physical logic gates, propagation delays through complementary signal paths are not instantaneous.
\begin{itemize}
    \item \textbf{Static-1 Hazard:} A condition where an output is expected to remain steadily at 1 during an input variable transition, but momentarily glitches to 0 due to asymmetric gate delays.
    \item \textbf{Static-0 Hazard:} A condition where an output is expected to remain steadily at 0, but momentarily glitches to 1.
    \item \textbf{Dynamic Hazard:} An output that is intended to undergo a single transition ($0 \to 1$ or $1 \to 0$) undergoes multiple intermediate oscillations ($0 \to 1 \to 0 \to 1$) due to multiple path delay disparities in multi-level circuits.
\end{itemize}

\begin{derivationbox}[Hazard Detection and Elimination via Consensus Terms]
Consider the minimal SOP expression:
\begin{equation}
    F = A B + \bar{A} C
\end{equation}
When inputs change from $A=1, B=1, C=1$ to $A=0, B=1, C=1$:
\begin{itemize}
    \item Term $AB$ transitions from $1 \to 0$.
    \item Term $\bar{A}C$ transitions from $0 \to 1$.
    \item If the inverter producing $\bar{A}$ introduces propagation delay $t_{pd}$, there exists a transient duration where both $A=0$ and $\bar{A}=0$, causing $F = 0 + 0 = 0$ (a static-1 glitch).
\end{itemize}
\textbf{Elimination Method:} On the K-map, static hazards occur between adjacent 1-cells covered by different prime implicant groups. Adding the \textbf{consensus prime implicant} $BC$ covers the transition:
\begin{equation}
    F_{\text{hazard-free}} = A B + \bar{A} C + B C
\end{equation}
When $B=1$ and $C=1$, the consensus term $BC=1$ holds the output HIGH regardless of fluctuations in $A$ or $\bar{A}$.
\end{derivationbox}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 3.1: Complete Radix Conversions and Arithmetic]
\textbf{Problem:}
\begin{enumerate}[label=(\alph*)]
    \item Convert decimal $(427.6875)_{10}$ into binary, octal, and hexadecimal representations.
    \item Perform binary subtraction $(01100100)_2 - (00111100)_2$ ($100_{10} - 60_{10}$) using 8-bit 2's complement arithmetic and verify the overflow flag.
\end{enumerate}

\textbf{Solution:}
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Integer Part ($427_{10}$):}
    \begin{align*}
        427 / 2 &= 213 \text{ rem } 1 \quad (\text{LSB}) \\
        213 / 2 &= 106 \text{ rem } 1 \\
        106 / 2 &= 53 \text{ rem } 0 \\
        53 / 2 &= 26 \text{ rem } 1 \\
        26 / 2 &= 13 \text{ rem } 0 \\
        13 / 2 &= 6 \text{ rem } 1 \\
        6 / 2 &= 3 \text{ rem } 0 \\
        3 / 2 &= 1 \text{ rem } 1 \\
        1 / 2 &= 0 \text{ rem } 1 \quad (\text{MSB}) \implies (427)_{10} = (110101011)_2
    \end{align*}
    \textbf{Fractional Part ($0.6875_{10}$):}
    \begin{align*}
        0.6875 \times 2 &= 1.3750 \implies \text{int } 1 \\
        0.3750 \times 2 &= 0.7500 \implies \text{int } 0 \\
        0.7500 \times 2 &= 1.5000 \implies \text{int } 1 \\
        0.5000 \times 2 &= 1.0000 \implies \text{int } 1 \implies (0.6875)_{10} = (0.1011)_2
    \end{align*}
    Combined Binary: $(427.6875)_{10} = \mathbf{(110101011.1011)_2}$.
    \begin{itemize}
        \item \textbf{Octal:} Grouping in 3s: $(110\,101\,011.101\,100)_2 = \mathbf{(653.54)_8}$.
        \item \textbf{Hexadecimal:} Grouping in 4s: $(0001\,1010\,1011.1011)_2 = \mathbf{(1\text{AB}.\text{B})_{16}}$.
    \end{itemize}
    \item \textbf{8-Bit 2's Complement Subtraction:}
    $A = 01100100_2$, $B = 00111100_2$.
    1's complement of $B$: $\bar{B} = 11000011_2$.
    2's complement of $B$: $\bar{B} + 1 = 11000100_2$.
    \begin{align*}
        A + (\bar{B} + 1) &= 01100100_2 + 11000100_2 \\
        &= (1)\,00101000_2
    \end{align*}
    Discarding the end-around carry $C_8 = 1$, the result is $00101000_2 = 32 + 8 = \mathbf{40_{10}}$.
    Carry into MSB ($C_7$) is $1$, carry out of MSB ($C_8$) is $1$.
    Overflow flag: $V = C_8 \oplus C_7 = 1 \oplus 1 = \mathbf{0}$ (No overflow, result is valid).
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 3.2: 4-Variable K-Map Minimization with Don't Cares]
\textbf{Problem:} Minimize the following 4-variable Boolean function into minimal Sum-of-Products (SOP) and Product-of-Sums (POS) forms:
\begin{equation}
    F(A,B,C,D) = \sum m(1, 3, 7, 11, 15) + d(0, 2, 5)
\end{equation}

\textbf{Solution:}
Plotting the 1s and don't cares ($d$) on the $4 \times 4$ K-map ($AB \times CD$):
\begin{itemize}
    \item Row $00$: $m(0)=d, m(1)=1, m(3)=1, m(2)=d$.
    \item Row $01$: $m(4)=0, m(5)=d, m(7)=1, m(6)=0$.
    \item Row $11$: $m(12)=0, m(13)=0, m(15)=1, m(14)=0$.
    \item Row $10$: $m(8)=0, m(9)=0, m(11)=1, m(10)=0$.
\end{itemize}
\textbf{SOP Grouping:}
\begin{enumerate}
    \item Octet formed by Row $00$ combined with column $11$ ($m_0, m_1, m_2, m_3$ with $m_7, m_{15}, m_{11}$ and $m_5=d$):
    \begin{itemize}
        \item Group 1 (Quad of column $CD=11$): cells $\{3, 7, 15, 11\} \implies \mathbf{CD}$.
        \item Group 2 (Quad of row $AB=00$): cells $\{0, 1, 3, 2\} \implies \mathbf{\bar{A}\bar{B}}$.
    \end{itemize}
\end{enumerate}
\textbf{Minimal SOP Expression:}
\begin{equation}
    F_{\text{min, SOP}} = \bar{A}\bar{B} + C D
\end{equation}
\textbf{Minimal POS Expression:}
Grouping 0-cells: $\{4, 6, 8, 9, 10, 12, 13, 14\}$:
\begin{itemize}
    \item Group of $\{8, 9, 10, 11\}$ (ignoring 11) $\to$ Quad $\{8, 10, 12, 14\} \implies D$ (as POS sum term $\bar{D} + A$).
    \item Combined POS minimization:
    \begin{equation}
        F_{\text{min, POS}} = (\bar{A} + C)(\bar{B} + D)(\bar{A} + D)
    \end{equation}
\end{itemize}
\end{examplebox}

\begin{examplebox}[Example 3.3: IEEE 754 Single-Precision Floating-Point Encoding]
\textbf{Problem:} Convert the decimal real number $-118.625_{10}$ into its 32-bit IEEE 754 single-precision floating-point hexadecimal representation.

\textbf{Solution:}
\begin{enumerate}
    \item \textbf{Sign Bit ($S$):} Since the number is negative, $S = 1$.
    \item \textbf{Binary Conversion:}
    \begin{itemize}
        \item Integer part: $118_{10} = 64 + 32 + 16 + 4 + 2 = 1110110_2$.
        \item Fractional part: $0.625_{10} = 0.5 + 0.125 = 0.101_2$.
        \item Combined: $(118.625)_{10} = 1110110.101_2$.
    \end{itemize}
    \item \textbf{Scientific Normalization ($1.F \times 2^e$):}
    \begin{equation}
        1110110.101_2 = 1.110110101_2 \times 2^6 \implies e = 6
    \end{equation}
    \item \textbf{Biased Exponent ($E$):}
    \begin{equation}
        E = e + 127 = 6 + 127 = 133_{10} = 10000101_2
    \end{equation}
    \item \textbf{Fraction Field ($F$, 23 bits):}
    \begin{equation}
        F = 11011010100000000000000_2
    \end{equation}
    \item \textbf{Assembling the 32-bit Word:}
    \begin{equation}
        \underbrace{1}_{S}\ \underbrace{10000101}_{E}\ \underbrace{11011010100000000000000}_{F}
    \end{equation}
    Grouping into 4-bit nibbles:
    \begin{equation}
        1100\ 0010\ 1110\ 1101\ 0100\ 0000\ 0000\ 0000_2 = \mathbf{(C2ED4000)_{16}}
    \end{equation}
\end{enumerate}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Number Systems:} Positional polynomial $\sum d_i r^i$. Successive division for integers, multiplication for fractions.
    \item \textbf{Codes:} BCD adds $+6$ on correction ($>9$); Excess-3 is self-complementing; Gray code has unit Hamming distance ($G_i = B_{i+1} \oplus B_i$).
    \item \textbf{Complements:} 2's complement $\bar{N}+1$. Subtraction $A-B = A + (\bar{B}+1)$. Overflow occurs when $V = C_n \oplus C_{n-1} = 1$.
    \item \textbf{IEEE 754 Standard:} 32-bit single precision uses 1 sign bit, 8 biased exponent bits (bias 127), and 23 fraction bits.
    \item \textbf{Universal Gates:} Both NAND and NOR can synthesize NOT, AND, OR, XOR, and XNOR gates.
    \item \textbf{K-Map Minimization:} Groups must be powers of 2. Essential Prime Implicants contain unique 1s.
    \item \textbf{Static Hazards:} Prevented by adding redundant consensus prime implicants to cover adjacent group boundaries.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-03-number-systems-and-logic.tex", "w") as f:
    f.write(ch3)

print("Chapter 3 expanded successfully.")

# ==============================================================================
# CHAPTER 4: EXPANDED COMBINATIONAL LOGIC CIRCUITS
# ==============================================================================
ch4 = r"""\chapter{Combinational Logic Circuits: Arithmetic, Routing, and Decoding}
\label{chap:combinational_logic}

\section{Introduction and Characteristics of Combinational Logic}
Combinational logic circuits are memoryless digital networks whose output at any instant depends strictly on the current combination of input signals. In this chapter, we explore arithmetic modules (adders, subtractors, Carry Lookahead Adders, ALUs), data routing multiplexers/demultiplexers, decoding/encoding structures (priority encoders, BCD-to-7-segment decoders), digital magnitude comparators, and parity generation/checking systems.

\section{Arithmetic Combinational Circuits}
\subsection{Half Adder and Full Adder Modules}
\begin{enumerate}
    \item \textbf{Half Adder (HA):} Adds two 1-bit binary operands $A$ and $B$, generating a Sum ($S$) and Carry-out ($C_{out}$):
    \begin{align}
        S &= A \oplus B = \bar{A}B + A\bar{B} \\
        C_{out} &= A \cdot B
    \end{align}
    A Half Adder cannot accept an incoming carry from a preceding less-significant stage.
    \item \textbf{Full Adder (FA):} Adds three 1-bit binary inputs: two data bits $A, B$ and a Carry-in $C_{in}$:
    \begin{align}
        S &= A \oplus B \oplus C_{in} \\
        C_{out} &= A B + B C_{in} + A C_{in} = A B + C_{in}(A \oplus B)
    \end{align}
    A Full Adder can be constructed using two Half Adders and an OR gate.
\end{enumerate}

\subsection{Ripple Carry Adder (RCA) and Timing Bottleneck}
An $n$-bit parallel Ripple Carry Adder cascades $n$ Full Adders such that the carry output $C_i$ of each stage ripples to the carry input $C_{in}$ of the next higher stage.
\begin{itemize}
    \item \textbf{Propagation Delay Bottleneck:} The MSB sum $S_{n-1}$ and final carry $C_n$ cannot stabilize until the carry ripples through all preceding $n$ stages.
    \item Total worst-case propagation delay for an $n$-bit RCA:
    \begin{equation}
        T_{\text{RCA}} = (n - 1) t_{\text{carry}} + t_{\text{sum}}
    \end{equation}
    where $t_{\text{carry}}$ is the carry propagation delay per stage and $t_{\text{sum}}$ is the sum generation delay.
\end{itemize}

\subsection{Carry Lookahead Adder (CLA): High-Speed Addition}
To eliminate the linear ripple delay $O(n)$, the Carry Lookahead Adder (CLA) computes all carry signals in parallel using two auxiliary functions for each bit position $i$:
\begin{align}
    \text{\textbf{Carry Generate:}} \quad G_i &= A_i \cdot B_i \quad (\text{Generates a carry regardless of } C_i) \\
    \text{\textbf{Carry Propagate:}} \quad P_i &= A_i \oplus B_i \quad (\text{Propagates an incoming carry } C_i)
\end{align}

\begin{derivationbox}[Carry Lookahead Recursive Carry Expansions]
The sum and stage carry expressions are:
\begin{align}
    S_i &= P_i \oplus C_i \\
    C_{i+1} &= G_i + P_i C_i
\end{align}
Expanding recursively for a 4-bit CLA:
\begin{align}
    C_1 &= G_0 + P_0 C_0 \\
    C_2 &= G_1 + P_1 C_1 = G_1 + P_1(G_0 + P_0 C_0) = G_1 + P_1 G_0 + P_1 P_0 C_0 \\
    C_3 &= G_2 + P_2 C_2 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0 \\
    C_4 &= G_3 + P_3 C_3 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0
\end{align}
Every carry bit $C_{i+1}$ is expressed as a direct two-level SOP function of initial carry $C_0$ and input operands ($G_k, P_k$).
Thus, all carries are computed simultaneously in constant time $O(1)$ (typically 2 to 3 gate delays), independent of word width $n$.
\end{derivationbox}

\subsection{4-Bit Parallel Adder-Subtractor with Overflow Detection}
A versatile arithmetic module capable of computing both addition ($A + B$) and subtraction ($A - B$) uses four Full Adders and four controlled XOR inverters driven by a Mode line $M$:
\begin{itemize}
    \item Connect operand $A_i$ directly to FA input $A_i$. Connect operand $B_i$ to one XOR input, with Mode line $M$ to the other XOR input. Connect Mode line $M$ directly to initial carry-in $C_0$.
    \item \textbf{When $M = 0$ (Addition Mode):}
    \begin{equation}
        B_i \oplus 0 = B_i, \quad C_0 = 0 \implies \text{Computes } A + B + 0 = A + B
    \end{equation}
    \item \textbf{When $M = 1$ (Subtraction Mode):}
    \begin{equation}
        B_i \oplus 1 = \bar{B}_i, \quad C_0 = 1 \implies \text{Computes } A + \bar{B} + 1 = A - B
    \end{equation}
    \item \textbf{Signed Overflow Flag ($V$):}
    \begin{equation}
        V = C_4 \oplus C_3
    \end{equation}
\end{itemize}

\subsection{Arithmetic Logic Unit (ALU 74181)}
The 74181 is a standard 4-bit multi-function Arithmetic Logic Unit that performs 16 arithmetic operations (addition, subtraction, decrement, increment, shift) and 16 logic operations (AND, OR, XOR, NOR, NAND, XNOR) selected by four control lines $S_3, S_2, S_1, S_0$, a Mode line $M$ ($M=0$ for arithmetic with carry, $M=1$ for pure logic), and carry-in $\bar{C}_n$.

\section{Multiplexers (Data Selectors) and Boolean Synthesis}
\subsection{Multiplexer Architecture}
A Multiplexer (MUX) is a digital selector with $2^n$ data inputs ($I_0, I_1, \dots, I_{2^n-1}$), $n$ select control lines ($S_{n-1}, \dots, S_0$), and a single output $Y$:
\begin{itemize}
    \item \textbf{4-to-1 MUX ($n=2$ select lines $S_1, S_0$):}
    \begin{equation}
        Y = \bar{S}_1 \bar{S}_0 I_0 + \bar{S}_1 S_0 I_1 + S_1 \bar{S}_0 I_2 + S_1 S_0 I_3
    \end{equation}
    \item \textbf{8-to-1 MUX ($n=3$ select lines $S_2, S_1, S_0$):}
    \begin{equation}
        Y = \sum_{k=0}^7 m_k(S_2, S_1, S_0) \cdot I_k
    \end{equation}
\end{itemize}

\subsection{Universal Boolean Function Synthesis Using Multiplexers}
Any $n$-variable Boolean function $F(x_1, x_2, \dots, x_n)$ can be synthesized using a single $2^{n-1}$-to-1 MUX:
\begin{enumerate}
    \item Connect $(n-1)$ variables to select lines $S_{n-2}, \dots, S_0$.
    \item The remaining variable $x_n$ provides data inputs ($I_k \in \{0, 1, x_n, \bar{x}_n\}$).
    \item Construct an implementation table comparing minterms where the function is 1 against $x_n = 0$ and $x_n = 1$.
\end{enumerate}

\section{Demultiplexers, Decoders, and Display Drivers}
\subsection{Decoders and Demultiplexers}
\begin{itemize}
    \item \textbf{Demultiplexer (DEMUX):} Directs a single data input $D_{in}$ to one of $2^n$ output lines based on $n$ select lines.
    \item \textbf{Binary Decoder:} Converts an $n$-bit binary code into $2^n$ unique active outputs.
    \item \textbf{3-to-8 Active-Low Decoder (74138):} Uses three enable pins ($G_1, \bar{G}_{2A}, \bar{G}_{2B}$) to decode inputs $A, B, C$ into active-low outputs $\bar{Y}_0$ to $\bar{Y}_7$:
    \begin{equation}
        \bar{Y}_k = \overline{m_k(A, B, C)}
    \end{equation}
    \item \textbf{Synthesizing Multi-Output Logic with Decoders:} Since each decoder output corresponds to a minterm, connecting selected active-low outputs to a multi-input NAND gate realizes any arbitrary SOP function:
    \begin{equation}
        F = \sum m(1, 2, 5, 7) \implies F = \overline{\bar{Y}_1 \cdot \bar{Y}_2 \cdot \bar{Y}_5 \cdot \bar{Y}_7}
    \end{equation}
\end{itemize}

\subsection{BCD-to-7-Segment Decoder/Driver}
Drives 7 LED segments ($a, b, c, d, e, f, g$) to render decimal numbers $0-9$:
\begin{itemize}
    \item \textbf{Common Anode Display:} All LED anodes connect to $V_{CC}$; driven by active-low segment outputs ($\text{LOW} = \text{ON}$).
    \item \textbf{Common Cathode Display:} All LED cathodes connect to ground; driven by active-high segment outputs ($\text{HIGH} = \text{ON}$).
\end{itemize}

\section{Encoders and Priority Encoders}
\subsection{Standard Encoders vs. Priority Encoders}
A standard $2^n$-to-$n$ encoder performs the reverse operation of a decoder. However, standard encoders fail if multiple input lines are active simultaneously or if all inputs are zero.

\begin{derivationbox}[Priority Encoder (74148) Architecture and Truth Table]
A 4-input Priority Encoder accepts four inputs ($D_0, D_1, D_2, D_3$), where $D_3$ has the highest priority and $D_0$ has the lowest priority. It generates a 2-bit binary output ($Y_1, Y_0$) and a \textbf{Valid Bit} ($V$) indicating if any input is active.

\begin{center}
\small
\begin{tabular}{cccc|ccc}
\toprule
\multicolumn{4}{c|}{\textbf{Inputs}} & \multicolumn{3}{c}{\textbf{Outputs}} \\
$D_3$ & $D_2$ & $D_1$ & $D_0$ & $Y_1$ & $Y_0$ & $V$ (Valid) \\
\midrule
0 & 0 & 0 & 0 & X & X & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & X & 0 & 1 & 1 \\
0 & 1 & X & X & 1 & 0 & 1 \\
1 & X & X & X & 1 & 1 & 1 \\
\bottomrule
\end{tabular}
\end{center}

From the truth table, the minimized output equations are:
\begin{align}
    Y_1 &= D_3 + D_2 \\
    Y_0 &= D_3 + \bar{D}_2 D_1 \\
    V &= D_3 + D_2 + D_1 + D_0
\end{align}
\end{derivationbox}

\section{Magnitude Comparators and Parity Circuits}
\subsection{Magnitude Comparators}
A magnitude comparator inspects two $n$-bit binary words $A$ and $B$ and determines their relative magnitude: $A > B$, $A = B$, or $A < B$.
\begin{itemize}
    \item \textbf{1-Bit Comparator:} For inputs $A, B$:
    \begin{align}
        (A = B) &= A \odot B = A B + \bar{A}\bar{B} \\
        (A > B) &= A \bar{B} \\
        (A < B) &= \bar{A} B
    \end{align}
    \item \textbf{4-Bit Magnitude Comparator (7485):} Compares $A_3 A_2 A_1 A_0$ with $B_3 B_2 B_1 B_0$. Equality occurs when all corresponding bits match:
    \begin{equation}
        (A = B) = (A_3 \odot B_3)(A_2 \odot B_2)(A_1 \odot B_1)(A_0 \odot B_0)
    \end{equation}
    Cascading input pins ($I_{A>B}, I_{A=B}, I_{A<B}$) permit connecting multiple 4-bit comparators to form 8-bit, 12-bit, or 16-bit comparators.
\end{itemize}

\subsection{Parity Generators and Checkers}
Parity circuits detect single-bit transmission errors by appending a parity bit ($P$):
\begin{itemize}
    \item \textbf{Even Parity Generator (3 data bits $A, B, C$):} $P_{\text{even}} = A \oplus B \oplus C$.
    \item \textbf{Odd Parity Generator:} $P_{\text{odd}} = \overline{A \oplus B \oplus C}$.
    \item \textbf{Parity Checker (at receiver):} Computes error syndrome bit $PEC = A \oplus B \oplus C \oplus P$. If $PEC = 1$, a single-bit parity error is flagged.
\end{itemize}

\section{Comprehensive Worked Examples and Problem Solutions}

\begin{examplebox}[Example 4.1: Boolean Function Implementation using 4-to-1 Multiplexer]
\textbf{Problem:} Implement the 3-variable Boolean function $F(A,B,C) = \sum m(1, 2, 6, 7)$ using a single 4-to-1 Multiplexer with $A$ and $B$ connected to select lines $S_1$ and $S_0$.

\textbf{Solution:}
\begin{enumerate}
    \item Assign select lines: $S_1 = A, S_0 = B$. The remaining input variable is $C$.
    \item Construct the MUX implementation table:
    \begin{center}
    \small
    \begin{tabular}{c|cccc}
    \toprule
    \textbf{Input Variable $C$} & $I_0 (AB=00)$ & $I_1 (AB=01)$ & $I_2 (AB=10)$ & $I_3 (AB=11)$ \\
    \midrule
    $C = 0$ & $m_0$ & $m_2$ (1) & $m_4$ & $m_6$ (1) \\
    $C = 1$ & $m_1$ (1) & $m_3$ & $m_5$ & $m_7$ (1) \\
    \midrule
    \textbf{Derived Data Input $I_k$} & $I_0 = C$ & $I_1 = \bar{C}$ & $I_2 = 0$ & $I_3 = 1$ \\
    \bottomrule
    \end{tabular}
    \end{center}
    \item \textbf{Input Vector:} $(I_0, I_1, I_2, I_3) = (C, \bar{C}, 0, 1)$. Connect $C$ to $I_0$, an inverted $\bar{C}$ to $I_1$, logic 0 (GND) to $I_2$, and logic 1 ($V_{CC}$) to $I_3$.
\end{enumerate}
\end{examplebox}

\begin{examplebox}[Example 4.2: Full Subtractor Design Using 3-to-8 Decoder]
\textbf{Problem:} Design a Full Subtractor (Difference $D$ and Borrow-out $B_{out}$) for inputs $A, B, B_{in}$ using a 3-to-8 Decoder (74138) with active-high outputs and minimal OR gates.

\textbf{Solution:}
\begin{enumerate}
    \item The truth table for Full Subtractor yields minterms:
    \begin{align}
        D(A, B, B_{in}) &= \sum m(1, 2, 4, 7) \\
        B_{out}(A, B, B_{in}) &= \sum m(1, 2, 3, 7)
    \end{align}
    \item Connect inputs $A \to A_2, B \to A_1, B_{in} \to A_0$ on the 3-to-8 decoder.
    \item Connect decoder outputs $Y_1, Y_2, Y_4, Y_7$ to a 4-input OR gate to produce Difference $D$.
    \item Connect decoder outputs $Y_1, Y_2, Y_3, Y_7$ to a 4-input OR gate to produce Borrow $B_{out}$.
\end{enumerate}
\end{examplebox}

\section{Chapter Summary and Key Takeaways}
\begin{takeawaybox}
\begin{itemize}
    \item \textbf{Adders:} Full Adder $S = A \oplus B \oplus C_{in}$, $C_{out} = AB + C_{in}(A \oplus B)$.
    \item \textbf{Carry Lookahead:} Eliminates ripple delay by computing carries in parallel using $G_i = A_i B_i$ and $P_i = A_i \oplus B_i$ in constant $O(1)$ time.
    \item \textbf{Adder-Subtractor:} Controlled with XOR gates and mode line $M$; signed overflow detected via $V = C_n \oplus C_{n-1}$.
    \item \textbf{Multiplexers:} Universal logic elements; an $n$-variable Boolean function can be realized using a single $2^{n-1}:1$ MUX.
    \item \textbf{Priority Encoders:} Resolve simultaneous active inputs by selecting the highest-order input line, generating a binary code and Valid flag.
    \item \textbf{Comparators:} Evaluate $A > B$, $A = B$, $A < B$; expandable across multiple stages using cascade inputs.
\end{itemize}
\end{takeawaybox}
"""

with open("PHY175/chapters/chapter-04-combinational-logic.tex", "w") as f:
    f.write(ch4)

print("Chapter 4 expanded successfully.")

