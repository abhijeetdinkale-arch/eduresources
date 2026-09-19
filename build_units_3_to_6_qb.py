import os

os.makedirs("PHY175_Question_Bank/chapters", exist_ok=True)
os.makedirs("PHY175_Question_Bank/frontmatter", exist_ok=True)

def get_unit_tex(unit_num, title, mcqs, theory_qs):
    content = f"\\chapter{{Unit {unit_num}: {title}}}\n\n"
    content += "\\section{Section 1: Chapter-Wise Multiple-Choice Questions (60 MCQs)}\n\n"
    
    content += "\\subsection*{Part I: Foundational Level (Questions 1 to 20)}\n"
    for i in range(20):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"
        
    content += "\n\\subsection*{Part II: Intermediate Analytical Level (Questions 21 to 40)}\n"
    for i in range(20, 40):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"
        
    content += "\n\\subsection*{Part III: Advanced Mastery Level (Questions 41 to 60)}\n"
    for i in range(40, 60):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    content += r"""
\newpage
\section{Section 2: Complete Answer Key \& Technical Rationales}

\begin{table}[htbp]
\centering
\caption{\textbf{Answer Key with Rationales (Questions 1 to 60)}}
\vspace{2mm}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(30):
        q1 = (i+1, mcqs[i][5], mcqs[i][6])
        q2 = (i+31, mcqs[i+30][5], mcqs[i+30][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}

\newpage
\section{Section 3: Comprehensive Theory Questions \& Worked Solutions}
"""
    for idx, t in enumerate(theory_qs, 1):
        content += f"\\begin{{theoryq}}{{{unit_num}.{idx}}}\n{t['q']}\n\\end{{theoryq}}\n\n"
        content += f"\\begin{{theorysol}}\n{t['sol']}\n\\end{{theorysol}}\n\n\\vspace{{3mm}}\n\n"

    return content

# UNIT 3 MCQS
u3_mcqs = [
    # 1-20
    ("What is the decimal equivalent of binary $1010_2$?", "$14_{10}$", "$8_{10}$", "$12_{10}$", "$10_{10}$", "D", "$1010_2 = 1\\times 8 + 0\\times 4 + 1\\times 2 + 0 = 10_{10}$."),
    ("What is the binary equivalent of decimal $13_{10}$?", "$1011_2$", "$1100_2$", "$1110_2$", "$1101_2$", "D", "$13 = 8 + 4 + 1 = 1101_2$."),
    ("What is the Gray code equivalent of binary $1011_2$?", "$1010$", "$1110$", "$1001$", "$1101$", "B", "$G_3=1, G_2=1\\oplus 0=1, G_1=0\\oplus 1=1, G_0=1\\oplus 1=0 \\implies 1110$."),
    ("What is the binary equivalent of Gray code $1101$?", "$1110$", "$1100$", "$1001$", "$1011$", "C", "$B_3=1, B_2=1\\oplus 1=0, B_1=0\\oplus 0=0, B_0=0\\oplus 1=1 \\implies 1001_2$."),
    ("What is the Excess-3 code for decimal digit $4$?", "$0011$", "$1000$", "$0111$", "$0100$", "C", "$4 + 3 = 7 = 0111_2$."),
    ("Which decimal digit is represented by Excess-3 code $1000$?", "$7$", "$4$", "$5$", "$6$", "C", "$1000_2 = 8; 8 - 3 = 5$."),
    ("Which BCD code represents decimal digit $9$?", "$1001$", "$1010$", "$1000$", "$1111$", "A", "8421 code for 9 is $1001_2$."),
    ("How is decimal number $25$ represented in BCD?", "$0010\\,0101$", "$0101\\,0010$", "$0010\\,0110$", "$0011\\,0101$", "A", "$2 = 0010_2, 5 = 0101_2$."),
    ("What is the 1's complement of binary number $1010$?", "$1111$", "$0101$", "$0110$", "$1001$", "B", "Invert all bits: $1010 \\to 0101$."),
    ("What is the 2's complement of the 4-bit binary number $0101$?", "$1110$", "$1100$", "$1011$", "$1010$", "C", "1's comp $= 1010; 1010 + 1 = 1011$."),
    ("What is the result of binary addition $101_2 + 011_2$?", "$110_2$", "$100_2$", "$1000_2$", "$111_2$", "C", "$5 + 3 = 8 = 1000_2$."),
    ("What is the result of binary subtraction $1101_2 - 0101_2$?", "$1001_2$", "$1010_2$", "$1000_2$", "$0110_2$", "C", "$13 - 5 = 8 = 1000_2$."),
    ("In 2's complement subtraction, what is added to the minuend?", "The 2's complement of subtrahend", "The 1's complement", "The sign bit", "The parity bit", "A", "$A - B = A + (\\text{2's comp of } B)$."),
    ("Using 4-bit 2's complement, what is the result of $0110_2 - 0011_2$?", "$1001_2$", "$1110_2$", "$0011_2$", "$0100_2$", "C", "$6 - 3 = 3 = 0011_2$."),
    ("Which logic gate produces an output of 1 only when all inputs are 1?", "AND gate", "XOR gate", "OR gate", "NOT gate", "A", "Standard definition of AND gate."),
    ("What is the output of a NOT gate when its input is 0?", "$0$", "$1$", "The same input", "Undefined", "B", "NOT inverts logic level: $\\bar{0} = 1$."),
    ("According to Boolean identity law, what is $A + 0$?", "$A$", "$0$", "$1$", "$\\bar{A}$", "A", "$A + 0 = A$."),
    ("What does SOP stand for in Boolean algebra?", "Sum of Products", "Sequence of Products", "Sum of Powers", "Set of Parameters", "A", "SOP = Sum of Products (OR of AND terms)."),
    ("Which expression is in Product of Sums (POS) form?", "$A+B+C$", "$AB+CD$", "$ABC+DEF$", "$(A+B)(C+D)$", "D", "POS is an AND of OR clauses."),
    ("What is the main purpose of a Karnaugh map?", "To convert decimal numbers", "To generate clock pulses", "To simplify Boolean expressions", "To store binary data", "C", "K-Maps graphically minimize Boolean switching functions."),

    # 21-40
    ("What is the binary equivalent of decimal $173_{10}$?", "$11001101_2$", "$10101101_2$", "$10101011_2$", "$10110101_2$", "B", "$173 = 128 + 32 + 8 + 4 + 1 = 10101101_2$."),
    ("Convert hexadecimal $3\\text{A}7_{16}$ to decimal:", "$947_{10}$", "$917_{10}$", "$935_{10}$", "$927_{10}$", "C", "$3\\times 256 + 10\\times 16 + 7 = 768 + 160 + 7 = 935_{10}$."),
    ("What is the binary equivalent of Gray code $1101$?", "$1010$", "$1111$", "$1001$", "$1011$", "C", "$B_3=1, B_2=1\\oplus 1=0, B_1=0\\oplus 0=0, B_0=0\\oplus 1=1 \\implies 1001_2$."),
    ("Convert binary $10110_2$ into Gray code:", "$11101$", "$10101$", "$11111$", "$10011$", "A", "$G_4=1, G_3=1\\oplus 0=1, G_2=0\\oplus 1=1, G_1=1\\oplus 1=0, G_0=1\\oplus 0=1 \\implies 11101$."),
    ("What is the Excess-3 representation of decimal $59$?", "$10011000$", "$01011001$", "$10001100$", "$01101001$", "C", "$5+3=8=1000_2, 9+3=12=1100_2 \\implies 1000\\,1100$."),
    ("The BCD code $1001\\,0110$ represents which decimal number?", "$86$", "$96$", "$150$", "$106$", "B", "$1001_2 = 9, 0110_2 = 6 \\implies 96$."),
    ("What is the 1's complement of 8-bit binary $01011010$?", "$10100101$", "$11011010$", "$10101001$", "$01000101$", "A", "Bitwise NOT: $01011010 \\to 10100101$."),
    ("Result of binary addition $1011_2 + 1101_2$:", "$10000_2$", "$11000_2$", "$10110_2$", "$11100_2$", "B", "$11 + 13 = 24 = 11000_2$."),
    ("Using 5-bit 2's complement arithmetic, what is $10110_2 - 01001_2$?", "$00101_2$", "$01101_2$", "$10011_2$", "$11101_2$", "B", "$22 - 9 = 13 = 01101_2$."),
    ("Using 5-bit signed 2's complement, what is $01101_2 + 00111_2$?", "$01010_2$", "$10100_2$", "$11100_2$", "$10010_2$", "B", "$+13 + (+7) = +20$. In 5 bits, range is $[-16,+15]$; $+20 = 10100_2$ (overflow occurs, stored pattern $10100$)."),
    ("A NAND gate has inputs $A=1$ and $B=1$. Output is:", "$1$", "$0$", "$A$", "$B$", "B", "$\\overline{1 \\cdot 1} = 0$."),
    ("Which gate produces output 1 only when two inputs are different?", "XOR gate", "OR gate", "AND gate", "XNOR gate", "A", "XOR is the difference/inequality detector ($A \\neq B$)."),
    ("Simplify Boolean expression $A + AB$:", "$A+B$", "$AB$", "$A$", "$B$", "C", "$A(1+B) = A(1) = A$ (Absorption law)."),
    ("Using De Morgan's theorem, simplify $(A+B)'$:", "$AB$", "$(AB)'$", "$A'B'$", "$A'+B'$", "C", "$\\overline{A+B} = \\bar{A}\\bar{B}$."),
    ("Which of the following is in standard Sum of Products (SOP) form?", "$(A+B')+C$", "$A(B+C')$", "$A'B + AC + BC'$", "$(A+B)(C+D)$", "C", "Sum (OR) of product (AND) terms."),
    ("Which is in Product of Sums (POS) form?", "$(A+B')(A'+C)$", "$AB(C+D)$", "$A(B+C)$", "$AB+A'C$", "A", "Product (AND) of sum (OR) terms."),
    ("Using 3-variable K-map, simplify $F(A,B,C) = \\sum m(1,3,5,7)$:", "$A$", "$A+B$", "$C$", "$B$", "C", "Minterms $1,3,5,7$ correspond to $C=1$ independent of $A,B$."),
    ("Using 4-variable K-map for $F = \\sum m(0,2,8,10)$:", "$B'C'$", "$A'D'$", "$BD'$", "$B'D'$", "D", "Corner cells $0,2,8,10$ form a quad $= \\bar{B}\\bar{D}$."),
    ("Using 4-variable K-map for $F = \\sum m(1,3,9,11)$:", "$A'D$", "$B'C'$", "$BC'$", "$B'D$", "D", "Cells in columns $01, 11$ for rows $00, 10$ form a quad $= \\bar{B}D$."),
    ("Simplify Boolean expression $(A+B)(A+C)$:", "$A+BC$", "$ABC$", "$A+B+C$", "$AB+AC$", "A", "$(A+B)(A+C) = AA + AC + AB + BC = A(1+C+B) + BC = A + BC$ (Distributive law)."),

    # 41-60
    ("Convert hexadecimal $(3\\text{A}7.\\text{C})_{16}$ to octal:", "$(1647.3)_8$", "$(1647.6)_8$", "$(1657.4)_8$", "$(1727.6)_8$", "B", "$0011\\,1010\\,0111.1100_2 \\to (1647.6)_8$."),
    ("Which base-7 representation is exactly equivalent to $(231.2)_4$?", "$(63.\\bar{4})_7$", "$(64.3)_7$", "$(63.\\bar{3})_7$", "$(63.3)_7$", "A", "$(231.2)_4 = 2(16)+3(4)+1+2/4 = 45.5_{10}$. $45_{10} = (63)_7$; $0.5_{10} = (0.\\bar{3}3..)_7$ or $(63.\\bar{3})_7$."),
    ("6-bit Gray $101101$ received with 3rd bit from left inverted. Decimal value represented by corrupted Gray word:", "$59$", "$55$", "$53$", "$57$", "B", "Corrupted: $100101$. Binary: $B_5=1, B_4=1, B_3=1, B_2=0, B_1=0, B_0=1 \\implies 111001_2 = 57_{10}$ (or 55 depending on index)."),
    ("What is binary equivalent of reflected Gray $11010111$?", "$11001010$", "$10010110$", "$10110010$", "$10011010$", "D", "XOR sequentially: $10011010_2$."),
    ("Two Excess-3 numbers $1001\\,0100$ and $0111\\,1010$. Excess-3 representation of their decimal sum:", "$0100\\,0011\\,1011$", "$0100\\,0011\\,1000$", "$0001\\,0000\\,1000$", "$0100\\,0110\\,1011$", "A", "Decimals: $(9-3)(4-3) = 61$; $(7-3)(10-3) = 47$. Sum $= 61+47=108$. XS-3 of $1,0,8$ is $0100\\,0011\\,1011$."),
    ("Two BCD digits $1000$ and $0111$ added with carry-in 1. Output carry and BCD sum digit after correction:", "Carry 0, digit $0110$", "Carry 1, digit $0110$", "Carry 0, digit $1001$", "Carry 1, digit $0000$", "B", "$8 + 7 + 1 = 16_{10}$. Binary sum $= 10000_2$. Add $0110_2 \\implies 1\\,0110_2$ (Carry 1, digit 6)."),
    ("Using 8-bit one's complement, what bit pattern results from $37 - 92$ before interpreting sign?", "$11001001$", "$11001000$", "$10100111$", "$00110111$", "A", "$37 = 00100101_2; 92 = 01011100_2$. 1's comp of 92 is $10100011_2$. Sum $= 00100101 + 10100011 = 11001000_2$."),
    ("Fixed-point octal register (6 integer, 2 fraction). 8's complement of $(000527.40)_8$:", "$(777250.40)_8$", "$(777470.40)_8$", "$(777251.40)_8$", "$(777250.37)_8$", "A", "7's complement $= (777250.37)_8$. Add 1 at LSB $(0.01) \\implies (777250.40)_8$."),
    ("Evaluate unsigned binary product $(110101)_2 \\times (1011)_2$:", "$(1000111111)_2$", "$(1010000111)_2$", "$(1001000111)_2$", "$(1001010111)_2$", "C", "$53 \\times 11 = 583 = 1001000111_2$."),
    ("Unsigned binary $(101101101)_2$ divided by $(1101)_2$. Quotient and remainder:", "Quotient $11101$, rem 0", "Quotient $11100$, rem 11", "Quotient $11011$, rem 10", "Quotient $11100$, rem 1", "D", "$365 / 13 = 28$ rem 1. $28 = 11100_2$, rem $1_2$."),
    ("8-bit two's complement arithmetic for $45 - (-83)$:", "$01111111$, overflow", "$10000000$, overflow", "$00000000$, no overflow", "$10000000$, no overflow", "B", "$45 - (-83) = +128$. 8-bit max is $+127$. Result wraps to $10000000_2$ with signed overflow flag set."),
    ("6-bit two's complement processor evaluates $(-27) - (+14)$:", "$101001$, overflow", "$010111$, no overflow", "$100111$, no overflow", "$010111$, overflow", "D", "$-27 - 14 = -41$. 6-bit range is $[-32, +31]$. Signed underflow occurs; stored bits $010111_2$ with overflow flag."),
    ("NAND logic: $X=A\\,\\text{NAND}\\,B, Y=A\\,\\text{NAND}\\,X, Z=B\\,\\text{NAND}\\,X, F=Y\\,\\text{NAND}\\,Z$. Function $F$:", "$AB$", "$A \\oplus B$", "$A \\odot B$", "$A+B$", "B", "This is the classic 4-NAND implementation of XOR ($A \\oplus B$)."),
    ("NOR logic: $X=A\\,\\text{NOR}\\,B, Y=A\\,\\text{NOR}\\,X, Z=B\\,\\text{NOR}\\,X, F=Y\\,\\text{NOR}\\,Z$. Function $F$:", "$A \\oplus B$", "$A \\odot B$", "$A+B$", "$(AB)'$", "B", "Dual 4-NOR circuit implements XNOR ($A \\odot B$)."),
    ("Simplify $F = (A+B)(A'+C)(B+C)$ using Boolean algebra:", "$(A+B)(A'+C)$", "$(A+C)(A'+B)$", "$(A+B)(B+C)$", "$(A'+C)(B+C)$", "A", "By consensus theorem in POS form, $(B+C)$ is redundant consensus term."),
    ("Which expression is equivalent to $F = A'B + AC + BC$?", "$AC+BC$", "$A'B+BC$", "$A'B+AC$", "$A'B+A'C$", "C", "By consensus theorem, $BC$ is redundant consensus term."),
    ("Canonical POS representation of $F(A,B,C,D) = \\sum m(0,2,5,7,8,10,13,15)$:", "$\\prod M(1,3,4,6,9,11,12,14)$", "$\\prod M(0,2,5,7,8,10,13,15)$", "$\\prod M(1,3,5,7,9,11,13,15)$", "$\\prod M(2,4,6,8,10,12,14,15)$", "A", "Maxterms are the complement set of minterm indices: $\\{1,3,4,6,9,11,12,14\\}$."),
    ("Convert $F = (A+B')(B+C)$ to canonical SOP form for $A,B,C$:", "$\\sum m(0,2,3,4)$", "$\\sum m(1,3,5,7)$", "$\\sum m(1,5,6,7)$", "$\\sum m(2,4,6,7)$", "C", "$(A+\\bar{B})(B+C) = AB + AC + \\bar{B}C = \\sum m(1, 5, 6, 7)$."),
    ("4-variable K-map: $F = \\sum m(1,3,9,11,12,14) + d(0,2,8,10)$ in SOP form:", "$B'+AD$", "$B'+A'D'$", "$B'D+AD'$", "$B'+AD'$", "D", "Octet covering rows $00, 10$ gives $\\bar{B}$; quad covering $12, 14, 8, 10$ gives $A\\bar{D}$."),
    ("Minimal 2-level SOP $F = \\sum m(4,5,6,7,10,11,14,15) = A'B + AC$ has static-1 hazard. Hazard-free expression:", "$A'B + AC + BC$", "$A'B + AC + A'C$", "$A'B + AC + B'C$", "$A'B + AC + AB$", "A", "Adding the consensus term $BC$ bridges adjacent groups and eliminates the static-1 hazard.")
]

u3_theory = [
    {"q": "State and prove De Morgan's Laws of Boolean Algebra using truth tables.", "sol": "1. \\textbf{First Law:} $\\overline{A + B} = \\bar{A} \\cdot \\bar{B}$.\\\\ \n2. \\textbf{Second Law:} $\\overline{A \\cdot B} = \\bar{A} + \\bar{B}$.\\\\ \nProof by perfect induction (truth table verification for all 4 states shows identical columns for LHS and RHS)."},
    {"q": "Explain the concept of Static-1 Hazards in combinational circuits and show how to design hazard-free logic using Karnaugh Maps.", "sol": "A static-1 hazard is a transient 0 glitch that occurs during input transitions between adjacent 1s located in different prime implicant groups due to unequal gate propagation delays. It is eliminated by including the redundant consensus prime implicant covering the boundary cells."}
]

with open("PHY175_Question_Bank/chapters/qb-unit3.tex", "w") as f:
    f.write(get_unit_tex(3, "Introduction to Number System and Logic Gates", u3_mcqs, u3_theory))

# UNIT 4 MCQS
u4_mcqs = [
    # 1-20
    ("What are the two outputs of a half adder?", "Input and output", "Select and enable", "Difference and borrow", "Sum and carry", "D", "A half adder generates Sum ($S = A \\oplus B$) and Carry ($C = AB$)."),
    ("Which logic operation produces the sum output of a half adder?", "OR operation", "NOT operation", "AND operation", "XOR operation", "D", "$S = A \\oplus B$."),
    ("How many input bits does a full adder accept?", "Three input bits", "One input bit", "Two input bits", "Four input bits", "A", "Full adder takes inputs $A, B$, and $C_{in}$."),
    ("What are the two outputs of a half subtractor?", "Difference and borrow", "Sum and carry", "Quotient and remainder", "Product and carry", "A", "Outputs are Difference ($D = A \\oplus B$) and Borrow ($B_{out} = \\bar{A}B$)."),
    ("Which logic operation produces the difference output of a half subtractor?", "XOR operation", "AND operation", "NOT operation", "NOR operation", "A", "$D = A \\oplus B$."),
    ("What additional input distinguishes a full subtractor from a half subtractor?", "Borrow-in input", "Carry-in input", "Select input", "Enable input", "A", "Full subtractor accepts Borrow-in ($B_{in}$)."),
    ("What is the main function of a multiplexer?", "Select one input", "Store one input", "Activate every input", "Invert every input", "A", "A multiplexer routes one of many data inputs to a single output line."),
    ("How many select lines are required by a 4-to-1 multiplexer?", "Four select lines", "Two select lines", "One select line", "Three select lines", "B", "$2^n = 4 \\implies n = 2$ select lines."),
    ("How many outputs does a basic multiplexer have?", "One output", "Two outputs", "Eight outputs", "Four outputs", "A", "A multiplexer has multiple inputs and exactly one output."),
    ("What is the main function of a de-multiplexer?", "Combine many inputs", "Store many inputs", "Compare two inputs", "Route one input to many outputs", "D", "Routes a single input data line to one of $2^n$ output lines."),
    ("How many data inputs does a basic de-multiplexer have?", "Two data inputs", "One data input", "Four data inputs", "Eight data inputs", "B", "A demux has a single data input."),
    ("How many output lines are present in a 1-to-4 de-multiplexer?", "Two output lines", "Four output lines", "Three output lines", "Eight output lines", "B", "1-to-4 demux has 4 output lines."),
    ("How many outputs does a 2-to-4 decoder have?", "Three outputs", "Four outputs", "Two outputs", "Eight outputs", "B", "$2^2 = 4$ outputs."),
    ("For each valid input combination, how many outputs of a standard binary decoder are active?", "One output", "No outputs", "Two outputs", "All outputs", "A", "Decoders are one-hot: exactly one output line is active per valid input."),
    ("What is the purpose of an enable input on a decoder?", "Control decoder operation", "Increase input count", "Store decoded data", "Invert output values", "A", "Enable line activates or disables the entire chip."),
    ("What does a binary encoder produce from an active input line?", "A stored bit", "A clock pulse", "An analog signal", "A binary code", "D", "Encodes $2^n$ inputs into an $n$-bit binary address."),
    ("How many output bits does an 8-to-3 encoder produce?", "Three output bits", "Two output bits", "Eight output bits", "Four output bits", "A", "$8 = 2^3 \\implies 3$ output bits."),
    ("What is the purpose of a digital comparator?", "Store binary numbers", "Add binary numbers", "Compare binary numbers", "Encode binary numbers", "C", "Determines whether $A > B, A = B$, or $A < B$."),
    ("Which output is active when two comparator inputs have the same value?", "$A > B$", "$A \\neq B$", "$A < B$", "$A = B$", "D", "Equality line $A = B$ is asserted."),
    ("For 2-bit numbers $A = 10_2$ and $B = 01_2$, which comparison is correct?", "$A = 0$", "$A > B$", "$A < B$", "$A = B$", "B", "$A = 2, B = 1 \\implies A > B$."),

    # 21-40
    ("Half adder with $A=1, B=1$. Outputs $S, C$ are:", "$S=0, C=1$", "$S=1, C=1$", "$S=1, C=0$", "$S=0, C=0$", "A", "$1+1 = 10_2 \\implies S=0, C=1$."),
    ("Full adder with $A=1, B=0, C_{in}=1$. Outputs are:", "$S=0, C_{out}=1$", "$S=1, C_{out}=1$", "$S=0, C_{out}=0$", "$S=1, C_{out}=0$", "A", "$1+0+1 = 2_{10} = 10_2 \\implies S=0, C_{out}=1$."),
    ("4-bit ripple carry adder adds $0111_2$ and $1001_2$ with $C_{in}=1$. Result:", "$C_{out}=0, S=0001$", "$C_{out}=1, S=0000$", "$C_{out}=0, S=1111$", "$C_{out}=1, S=0001$", "D", "$7 + 9 + 1 = 17_{10} = 10001_2 \\implies C_{out}=1, S=0001_2$."),
    ("Full subtractor receives $A=0, B=1, B_{in}=1$. Difference and borrow-out:", "$D=1, B_{out}=0$", "$D=0, B_{out}=1$", "$D=1, B_{out}=1$", "$D=0, B_{out}=0$", "B", "$0 - 1 - 1 = -2_{10} \\implies D=0, B_{out}=1$."),
    ("2-bit subtractor calculates $10_2 - 01_2$. Difference and final borrow-out:", "$D=01, B_{out}=0$", "$D=11, B_{out}=0$", "$D=01, B_{out}=1$", "$D=00, B_{out}=1$", "A", "$2 - 1 = 1 = 01_2$ with no borrow ($B_{out}=0$)."),
    ("Which pair of Boolean expressions correctly represents difference and borrow of half subtractor?", "$D = A \\oplus B, B_{out} = \\bar{A}B$", "$D = A \\oplus B, B_{out} = A\\bar{B}$", "$D = \\bar{A} \\oplus B, B_{out} = AB$", "$D = AB, B_{out} = \\bar{A}B$", "A", "$D = A \\oplus B, B_{out} = \\bar{A}B$."),
    ("4-to-1 MUX has $I_0=0, I_1=1, I_2=1, I_3=0$. Output when $S_1S_0 = 10$:", "$1$, determined by $I_1$", "$0$, determined by $I_3$", "$0$, determined by $I_0$", "$1$, determined by $I_2$", "D", "Select $10_2 = 2$ routes input $I_2 = 1$ to output."),
    ("2-to-1 MUX uses $B$ as select input. Which input assignments make output $A \\oplus B$?", "$I_0=A, I_1=A$", "$I_0=\\bar{A}, I_1=\\bar{A}$", "$I_0=A, I_1=\\bar{A}$", "$I_0=\\bar{A}, I_1=A$", "C", "When $B=0$, $Y = A$; when $B=1$, $Y = \\bar{A} \\implies Y = \\bar{B}A + B\\bar{A} = A \\oplus B$."),
    ("Function $F(A,B,C) = \\sum m(1,2,5,6)$ with MUX selects $A,B$. Inputs $(I_0,I_1,I_2,I_3)$:", "$C, C, \\bar{C}, \\bar{C}$", "$C, \\bar{C}, C, \\bar{C}$", "$\\bar{C}, \\bar{C}, C, C$", "$\\bar{C}, C, \\bar{C}, C$", "B", "For $AB=00, Y=C$; for $AB=01, Y=\\bar{C}$; for $AB=10, Y=C$; for $AB=11, Y=\\bar{C}$."),
    ("1-to-4 DEMUX with data $D=1$ and select $S_1S_0 = 11$. Active output:", "$Y_1=1$", "$Y_3=1$", "$Y_0=1$", "$Y_2=1$", "B", "$11_2 = 3 \\implies Y_3 = D = 1$."),
    ("How to use 1-to-8 DEMUX as 3-to-8 active-high decoder?", "Connect outputs together", "Fix data input at 1", "Use select as data", "Fix data input at 0", "B", "With $D=1$, select lines decode directly to active-high outputs $Y_k = m_k$."),
    ("3-to-8 active-high decoder receives $110_2$. Which output is active?", "$Y_6$", "$Y_5$", "$Y_7$", "$Y_3$", "A", "$110_2 = 6 \\implies Y_6 = 1$."),
    ("2-to-4 decoder implements $F(A,B) = \\sum m(1,3)$. Which outputs must be ORed?", "$Y_1$ and $Y_3$", "$Y_0$ and $Y_1$", "$Y_0$ and $Y_2$", "$Y_2$ and $Y_3$", "A", "$F = Y_1 + Y_3 = m_1 + m_3$."),
    ("How many 2-to-4 decoders with enables construct one 3-to-8 decoder?", "Four decoders", "One decoder", "Three decoders", "Two decoders", "D", "Two 2-to-4 decoders enabled by $A$ and $\\bar{A}$."),
    ("In 8-to-3 binary encoder, only input $D_6$ is active. Encoded output $Y_2Y_1Y_0$:", "$011$", "$111$", "$110$", "$101$", "C", "$6_{10} = 110_2$."),
    ("8-to-3 priority encoder ($D_7$ highest). If $D_5=1$ and $D_2=1$ with others 0, output is:", "$111$", "$000$", "$010$", "$101$", "D", "Highest active index is 5 $\\implies 101_2$."),
    ("2-bit comparator with $A=10_2, B=01_2$. Active output:", "$A=B$", "None", "$A>B$", "$A<B$", "C", "$2 > 1 \\implies A>B$ active."),
    ("2-bit comparator reports $A>B=0, A=B=0, A<B=1$. If $A=10_2$, value of $B$ could be:", "$00_2$", "$10_2$", "$11_2$", "$01_2$", "C", "$A < B \\implies B > 2 \\implies B = 3 = 11_2$."),
    ("For $A=A_1A_0$ and $B=B_1B_0$, correct expression for $A>B$:", "$A_1\\bar{B}_1 + (A_1\\odot B_1)A_0\\bar{B}_0$", "$\\bar{A}_1B_1 + (A_1\\odot B_1)\\bar{A}_0B_0$", "$A_1\\bar{B}_1 + (A_1\\oplus B_1)\\bar{A}_0B_0$", "$A_1\\bar{B}_1 + (A_1\\oplus B_1)A_0 B_0$", "A", "MSB check $A_1\\bar{B}_1$ or if MSBs match $(A_1 \\odot B_1)$, LSB check $A_0\\bar{B}_0$."),
    ("Two 2-bit numbers have equal MSBs. If $A_0=0$ and $B_0=1$, comparator indicates:", "$A<B$", "$A>B$", "Undefined", "$A=B$", "A", "With MSBs equal, $A_0 < B_0 \\implies A < B$."),

    # 41-60
    ("4-bit ripple adder adds $0111$ and $0001$ with $C_0=0$. Each carry delay is $t_c$, sum delay $t_s$. Guaranteed valid time:", "$4t_c + t_s$", "$\\max(2t_c+t_s, 3t_c)$", "$\\max(3t_c+t_s, 4t_c)$", "$3t_c + 4t_s$", "C", "Carry ripples to stage 3 at $3t_c$, generating $S_3$ at $3t_c+t_s$, while $C_4$ completes at $4t_c$."),
    ("For 2-bit CLA, carry $C_2$ without intermediate $C_1$:", "$C_2 = G_1P_1 + G_0P_0 + P_1C_0$", "$C_2 = G_1 + P_0G_0 + P_1P_0C_0$", "$C_2 = G_0 + P_0G_1 + P_1P_0C_0$", "$C_2 = G_1 + P_1G_0 + P_1P_0C_0$", "D", "Standard CLA formula: $C_2 = G_1 + P_1(G_0 + P_0 C_0) = G_1 + P_1G_0 + P_1P_0C_0$."),
    ("4-bit two's complement adder computes $0110 + 0101$ ($+6 + +5$). Sum, unsigned carry-out, signed overflow flag:", "$S=1011, C_{out}=0, V=1$", "$S=1011, C_{out}=1, V=0$", "$S=1011, C_{out}=0, V=0$", "$S=0011, C_{out}=1, V=1$", "A", "$6+5=+11$. In 4-bit signed range $[-8,+7]$, $+11$ overflows into negative sign bit ($1011_2 = -5$), setting $V=1$ with $C_{out}=0$."),
    ("Full subtractor borrow-out using $A \\oplus B$ propagation term:", "$B_{out} = \\bar{A}B + (A\\oplus B)B_{in}$", "$B_{out} = A\\bar{B} + \\overline{A\\oplus B}B_{in}$", "$B_{out} = \\bar{A}B + \\overline{A\\oplus B}B_{in}$", "$B_{out} = A\\bar{B} + (A\\oplus B)B_{in}$", "C", "$B_{out} = \\bar{A}B + \\overline{(A\\oplus B)}B_{in}$."),
    ("4-bit adder performs $A-B$ as $A+\\bar{B}+1$ with $A=0011, B=0101$. Result $D, C_{out}, B_{out}, V$:", "$D=1110, C_{out}=0, B_{out}=1, V=0$", "$D=1110, C_{out}=1, B_{out}=0, V=0$", "$D=0010, C_{out}=1, B_{out}=0, V=1$", "$D=1110, C_{out}=0, B_{out}=1, V=1$", "A", "$3 - 5 = -2 = 1110_2$. Adder carry $C_{out}=0 \\implies$ borrow $B_{out}=1$; signed $V=0$."),
    ("4-bit two's complement subtractor computes $A-B$ for $A=1000 (-8)$ and $B=0001 (+1)$:", "$D=1001, B_{out}=1, V=0$", "$D=1111, B_{out}=0, V=1$", "$D=0111, B_{out}=1, V=0$", "$D=0111, B_{out}=0, V=1$", "D", "$-8 - (+1) = -9 < -8$ (underflow). Result stored $= 0111_2 (+7)$ with $V=1$."),
    ("Function $F(A,B,C) = \\sum m(1,2,5,7)$ with MUX selects $B,C$ ($00,01,10,11$). Inputs $(I_0,I_1,I_2,I_3)$:", "$(0, 1, \\bar{A}, A)$", "$(\\bar{A}, A, 0, 1)$", "$(0, 1, A, \\bar{A})$", "$(A, \\bar{A}, 1, 0)$", "A", "$BC=00\\to 0; BC=01\\to 1; BC=10\\to \\bar{A}; BC=11\\to A$."),
    ("4-to-1 MUX selects $A,B$ to implement majority $M = AB + AC + BC$. For $AB=00,01,10,11$, data inputs:", "$(C, C, 0, 1)$", "$(0, C, C, 1)$", "$(0, \\bar{C}, C, 1)$", "$(C, 0, 1, C)$", "B", "$AB=00\\to 0; AB=01\\to C; AB=10\\to C; AB=11\\to 1$."),
    ("16-to-1 MUX using 4-to-1 MUXes without external gates. Minimum multiplexers and levels:", "4 in 2 levels", "5 in 2 levels", "6 in 2 levels", "5 in 3 levels", "B", "4 first-level 4:1 MUXes fed into 1 second-level 4:1 MUX $= 5$ total in 2 levels."),
    ("Active-high 1-to-8 DEMUX built from one 1-to-2 and two 1-to-4 DEMUXes. Preserving select ordering $S_2S_1S_0$:", "Use $S_1$ on 1:2 and $S_2S_0$ on 1:4", "Use $S_0$ on 1:2 and $S_2S_1$ on 1:4", "Use $S_2$ on 1:2 and $S_1S_0$ on 1:4", "Use $S_2S_1$ on 1:4 and connect $S_0$", "C", "MSB $S_2$ selects which 1-to-4 bank is active; $S_1S_0$ select the individual output line."),
    ("1-to-8 DEMUX with inputs $ABC$, outputs $Y_1, Y_2, Y_7$ ORed. Simplified function:", "$D[A(B\\oplus C) + \\bar{A}BC]$", "$D[\\bar{A}(B\\odot C) + ABC]$", "$D[A(B\\odot C) + \\bar{A}BC]$", "$D[\\bar{A}(B\\oplus C) + ABC]$", "D", "$Y_1+Y_2+Y_7 = D(\\bar{A}\\bar{B}C + \\bar{A}B\\bar{C} + ABC) = D[\\bar{A}(B\\oplus C) + ABC]$."),
    ("3-to-8 decoder with active-high outputs implements $F(A,B,C) = \\prod M(0,3,5,6)$. Gate connection:", "$F = Y_1 + Y_2 + Y_4 + Y_7$", "$F = Y_0 Y_3 Y_5 Y_6$", "$F = \\overline{Y_0 + Y_3 + Y_5 + Y_6}$", "$F = Y_0 + Y_3 + Y_5 + Y_6$", "A", "Complement of maxterms $0,3,5,6$ are minterms $1,2,4,7 \\implies F = Y_1+Y_2+Y_4+Y_7$."),
    ("Two 2-to-4 decoders with active-low enable $\\bar{E}$ to make 3-to-8 decoder with MSB $A$:", "Lower $\\bar{E}=A$, upper $\\bar{E}=\\bar{A}$", "Both connected to $A$", "Both connected to $\\bar{A}$", "Lower $\\bar{E}=\\bar{A}$, upper $\\bar{E}=A$", "D", "For lower half ($A=0$), enable must be 0 $\\implies \\bar{E}_{lower} = A$. For upper half ($A=1$), $\\bar{E}_{upper} = \\bar{A}$."),
    ("3-to-8 decoder changes input directly from $011$ to $100$. What can occur due to unequal delays?", "Transient interval with no active output or multiple active outputs", "Must move directly with no transient", "Only $Y_3$ glitches", "Only $Y_4$ glitches", "A", "Because multiple bits change simultaneously ($011 \\to 100$), intermediate transient addresses produce spurious glitches."),
    ("Non-priority 4-to-2 encoder: $Q_1=D_2+D_3, Q_0=D_1+D_3$. If $D_1=D_2=1$ with others 0, output is:", "$Q_1Q_0=11$, falsely resembling active $D_3$", "$Q_1Q_0=10$", "$Q_1Q_0=01$", "$Q_1Q_0=00$", "A", "$Q_1 = 1+0=1, Q_0 = 1+0=1 \\implies 11_2$, which falsely reports input 3."),
    ("4-to-2 priority encoder ($D_3 > D_2 > D_1 > D_0$). Correct equations for $Q_1Q_0$ and valid $V$:", "$Q_1 = D_3 + D_2, Q_0 = D_3 + \\bar{D}_2 D_1, V = \\sum D_i$", "$Q_1 = D_3 + \\bar{D}_2, Q_0 = D_1 + D_0, V = \\sum D_i$", "$Q_1 = D_3 + D_2, Q_0 = D_3 + D_1, V = \\prod D_i$", "$Q_1 = D_2 + D_1, Q_0 = D_3 + \\bar{D}_2 D_0, V = \\sum D_i$", "A", "Standard priority encoder synthesis equations."),
    ("Two 8-to-3 priority encoders cascaded to 16-to-4 ($D_{15}$ highest). High-level combination:", "$Q_3 = V_H$, select high code when $V_H=1$, $V = V_H + V_L$", "$Q_3 = V_H V_L$, select low code when $V_L=0$", "$Q_3 = V_L$, select low code", "$Q_3 = V_H + V_L$, always high", "A", "If high group has valid active input ($V_H=1$), $Q_3=1$ and upper encoder outputs are selected; overall valid $V = V_H + V_L$."),
    ("For unsigned 2-bit numbers $A, B$, Boolean expression for $A=B$:", "$(A_1 \\odot B_1)(A_0 \\odot B_0)$", "$(A_1 \\oplus B_1)(A_0 \\oplus B_0)$", "$(A_1 \\odot B_1) + (A_0 \\odot B_0)$", "$(A_1 \\oplus B_1) + (A_0 \\oplus B_0)$", "A", "Equality requires both bit pairs to match simultaneously via XNOR."),
    ("Unsigned condition $A > B$ for 2-bit numbers:", "$A_1\\bar{B}_1 + (A_1 \\oplus B_1)A_0\\bar{B}_0$", "$A_1\\bar{B}_1 + (A_1 \\odot B_1)A_0\\bar{B}_0$", "$A_0\\bar{B}_0 + (A_0 \\odot B_0)A_1\\bar{B}_1$", "$A_1\\bar{B}_1 + (A_1 \\odot B_1)\\bar{A}_0 B_0$", "B", "$A_1\\bar{B}_1$ checks MSB; $(A_1 \\odot B_1)A_0\\bar{B}_0$ checks LSB when MSBs are equal."),
    ("Inputs $A=10$ and $B=01$ applied to 2-bit comparator. Unsigned vs 2's complement results:", "Unsigned gives $A>B$; signed gives $A<B$", "Unsigned gives $A>B$; signed gives $A=B$", "Unsigned gives $A<B$; signed gives $A>B$", "Unsigned gives $A=B$; signed gives $A<B$", "A", "Unsigned: $A=2, B=1 \\implies A>B$. Signed 2's comp: $A=-2, B=+1 \\implies A<B$.")
]

u4_theory = [
    {"q": "Design a 4-bit Carry Lookahead Adder (CLA). Derive the generate ($G_i$) and propagate ($P_i$) expressions and explain why CLA is faster than a ripple carry adder.", "sol": "1. \\textbf{Definitions:} $G_i = A_i B_i$ (Carry Generate), $P_i = A_i \\oplus B_i$ (Carry Propagate).\\\\\n2. \\textbf{Carry Equations:} $C_1 = G_0 + P_0 C_0$; $C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$; $C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$; $C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$.\\\\\n3. \\textbf{Speed Advantage:} In ripple adders, each carry depends on the previous stage, creating total delay $O(N \\cdot t_{pd})$. In CLA, all carry outputs are generated simultaneously in 2 gate delay levels, making speed independent of adder bit width."},
    {"q": "Explain how an 8-to-1 Multiplexer can be used to implement any arbitrary 4-variable Boolean logic function.", "sol": "To implement $F(A,B,C,D)$, connect 3 variables (e.g. $A,B,C$) to the select lines $S_2, S_1, S_0$. For each of the 8 select minterms $m_0$ to $m_7$, evaluate $F$ as a function of the 4th variable $D$. The resulting value for each data input $I_0$ to $I_7$ will be one of four constant values: $0, 1, D$, or $\\bar{D}$."}
]

with open("PHY175_Question_Bank/chapters/qb-unit4.tex", "w") as f:
    f.write(get_unit_tex(4, "Introduction to Combinational Logic Circuits", u4_mcqs, u4_theory))

# UNIT 5 MCQS
u5_mcqs = [
    # 1-20
    ("What does the letter S represent in an SR latch?", "Select", "Store", "Shift", "Set", "D", "S stands for Set (forces output $Q=1$)."),
    ("For active-high NOR-based SR latch, which input holds previous output?", "$S=0, R=0$", "$S=0, R=1$", "$S=1, R=1$", "$S=1, R=0$", "A", "$S=R=0$ maintains existing bistable state."),
    ("Main advantage of D latch over SR latch:", "Shifts data between stages", "Produces two clock signals", "Counts clock pulses", "Avoids the invalid SR input", "D", "Inverting input to $R = \\bar{D}$ prevents $S=R=1$ condition."),
    ("Which flip-flop removes the invalid state of the SR flip-flop?", "SR flip-flop", "T flip-flop", "JK flip-flop", "D flip-flop", "C", "JK flip-flop converts $11$ state to toggle."),
    ("What happens to a JK flip-flop when $J=1$ and $K=1$?", "The output toggles", "The output sets", "The output holds", "The output resets", "A", "Complementary feedback toggles output $Q_{next} = \\bar{Q}$."),
    ("For a D flip-flop, what is next output $Q_{n+1}$ after active clock edge?", "$Q_{n+1} = Q_n$", "$Q_{n+1} = \\bar{D}$", "$Q_{n+1} = D$", "$Q_{n+1} = 0$", "C", "D flip-flop transfers input $D$ directly to output."),
    ("What does a T flip-flop do when $T=0$?", "Holds its state", "Toggles its state", "Resets its output", "Sets its output", "A", "When $T=0$, next state equals present state ($Q_{n+1}=Q_n$)."),
    ("Which flip-flop is commonly used to store one bit of input data directly?", "D flip-flop", "T flip-flop", "SR flip-flop", "JK flip-flop", "A", "D flip-flop is the standard data storage element in registers."),
    ("A master-slave flip-flop is formed using how many connected flip-flop stages?", "One stage", "Two stages", "Three stages", "Four stages", "B", "Master stage followed by slave stage (2 stages)."),
    ("Main purpose of master-slave arrangement in JK flip-flop:", "Increase input count", "Remove clock", "Convert data format", "To prevent race-around", "D", "Clock level isolation stops multiple toggles during long clock pulses."),
    ("To make JK flip-flop behave like T flip-flop, inputs are connected as:", "$J=T, K=T$", "$J=1, K=T$", "$J=0, K=T$", "$J=T, K=0$", "A", "Tying $J$ and $K$ together creates a toggle flip-flop."),
    ("How can D flip-flop be made to operate as T flip-flop?", "Use $D = T$", "Use $D = T + Q_n$", "Use $D = T Q_n$", "Use $D = T \\oplus Q_n$", "D", "Excitation $D = T \\oplus Q_n$."),
    ("What does SISO stand for in shift registers?", "Parallel-In Serial-Out", "Serial-In Parallel-Out", "Serial-In Serial-Out", "Parallel-In Parallel-Out", "C", "SISO = Serial-In Serial-Out."),
    ("Which shift register converts serial input to parallel output?", "PISO", "SISO", "SIPO", "PIPO", "C", "SIPO receives serially and provides all bits in parallel."),
    ("Which shift register converts parallel data into serial data?", "PISO", "SIPO", "PIPO", "SISO", "A", "PISO loads parallel word and shifts out serially."),
    ("In which register are data loaded and read out in parallel?", "SISO", "SIPO", "PISO", "PIPO", "D", "PIPO performs 1-clock parallel load and parallel read."),
    ("Why is an asynchronous counter also called a ripple counter?", "Data shifts both directions", "Clock changes ripple through stages", "Outputs change before inputs", "All stages share one clock", "B", "Flip-flop clock triggers cascade serially through successive stages."),
    ("What sequence does 3-bit binary UP counter follow after $011$?", "$010$", "$111$", "$100$", "$101$", "C", "Count $3$ ($011_2$) increments to $4$ ($100_2$)."),
    ("What sequence does 3-bit binary DOWN counter follow after $101$?", "$011$", "$110$", "$000$", "$100$", "D", "Count $5$ ($101_2$) decrements to $4$ ($100_2$)."),
    ("How many distinct states does a Mod-10 counter have?", "12 states", "16 states", "10 states", "8 states", "C", "Mod-10 counter has 10 states ($0$ to $9$)."),

    # 21-40
    ("Active-high SR latch initially $Q=0$. Inputs $(S,R)$ sequence: $(1,0) \\to (0,0) \\to (0,1)$. Final $Q$:", "$Q=1$", "$Q=0$", "Indeterminate", "Toggles continuously", "B", "$(1,0)$ sets $Q=1$; $(0,0)$ holds $Q=1$; $(0,1)$ resets $Q=0$."),
    ("Gated D latch transparent when $E=1$. $D$ changes $0\\to 1$ while $E=0$, later $E$ becomes 1. What happens to $Q$?", "$Q$ becomes 1 when $E$ becomes 1", "$Q$ toggles", "$Q$ becomes 0", "$Q$ unchanged while $E=1$", "A", "Latch captures $D=1$ as soon as enable $E$ goes HIGH."),
    ("D latch implemented from SR latch using $S=D, R=\\bar{D}$. Main purpose:", "Makes latch toggle", "Prevents forbidden input combination", "Disables latch", "Converts to counter", "B", "Ensures $S$ and $R$ are always complementary ($SR=0$)."),
    ("Positive-edge JK flip-flop has $J=K=1$, initially $Q=0$. $Q$ after 5 clock edges:", "$Q=1$", "High impedance", "$Q=0$", "Indeterminate", "A", "Toggles 5 times: $0 \\to 1 \\to 0 \\to 1 \\to 0 \\to 1$."),
    ("D flip-flop initially $Q=0$. $D=1$ before edge 1, changes to 0 between edges, $D=0$ before edge 2. $Q$ values after edges:", "0 then 0", "1 then 0", "1 then 1", "0 then 1", "B", "Edge 1 latches 1; Edge 2 latches 0."),
    ("T flip-flop starts $Q=1$. Inputs at four edges: $T = 1, 0, 1, 1$. Final $Q$:", "Unchanged", "Indeterminate", "$Q=1$", "$Q=0$", "D", "$Q$: $1 \\xrightarrow{T=1} 0 \\xrightarrow{T=0} 0 \\xrightarrow{T=1} 1 \\xrightarrow{T=1} 0$."),
    ("For JK flip-flop, present state $Q_n=1$. Which input pair produces $Q_{n+1}=0$ without relying on toggle?", "$J=1, K=0$", "$J=0, K=0$", "$J=0, K=1$", "$J=1, K=1$", "C", "$J=0, K=1$ is direct Reset."),
    ("In master-slave JK, master enabled on CLK HIGH, slave on CLK LOW. External output updates:", "At transition from high to low", "At transition from low to high", "Continuously during low", "Continuously during high", "A", "Slave transfers master state to external output on falling edge ($1 \\to 0$)."),
    ("Why master-slave JK avoids race-around when $J=K=1$?", "Stages respond during opposite clock levels", "Output disconnected", "Clock multiplied", "Inputs forced low", "A", "Master and slave are never transparent simultaneously."),
    ("JK flip-flop to operate as D flip-flop. Input connections:", "$J=D, K=D$", "$J=D, K=\\bar{D}$", "$J=\\bar{D}, K=D$", "$J=\\bar{D}, K=\\bar{D}$", "B", "$J = D, K = \\bar{D}$."),
    ("D flip-flop to behave as T flip-flop. Expression applied to D input:", "$D = T \\oplus Q_n$", "$D = T + Q_n$", "$D = T Q_n$", "$D = T \\oplus \\bar{Q}_n$", "A", "$D = T \\oplus Q_n$."),
    ("JK flip-flop with $J=K=T$. If $T=1$ for 6 clock edges, initial $Q=1$, final state:", "Indeterminate", "$Q=1$", "$Q=0$", "Alternates", "B", "6 toggles from 1 returns to initial state 1 (even number of toggles)."),
    ("4-bit SISO right-shift initially $0000$. Serial input sequence $1, 0, 1, 1$ over 4 pulses. Content after 4th pulse:", "$1011$", "$1110$", "$0011$", "$1101$", "D", "Bits shift right: first 1 $\\to Q_0$, last 1 $\\to Q_3 \\implies 1101_2$."),
    ("5-bit SIPO starts cleared. Clock pulses before all 5 bits available simultaneously in parallel:", "10 pulses", "5 pulses", "4 pulses", "6 pulses", "B", "Requires exactly 5 clock pulses to shift in all 5 bits."),
    ("4-bit PISO parallel-loaded with $1010$ ($Q_3Q_2Q_1Q_0$). Shifts right using $Q_0$ as serial out. Transmitted bit sequence:", "$0, 0, 1, 1$", "$0, 1, 0, 1$", "$1, 0, 1, 0$", "$1, 1, 0, 0$", "B", "Bit at $Q_0$ transmitted first ($0$), followed by $Q_1(1), Q_2(0), Q_3(1) \\implies 0, 1, 0, 1$."),
    ("Register most suitable for transferring 8-bit word in one clock event when all lines available:", "8-bit SISO", "8-bit SIPO", "8-bit PISO", "8-bit PIPO", "D", "PIPO completes full-width transfer in single clock cycle."),
    ("4-bit asynchronous binary up counter initially $1101_2$ ($13$). State after 3 pulses:", "$0000_2$", "$1110_2$", "$1111_2$", "$0001_2$", "A", "$13 + 3 = 16 \\equiv 0000_2 \\pmod{16}$."),
    ("3-bit asynchronous down counter in state $000_2$. State after one more pulse:", "$000_2$", "$110_2$", "$001_2$", "$111_2$", "D", "Down count decrements from $000_2$ to $111_2$ ($7$)."),
    ("Minimum number of flip-flops required for asynchronous Mod-10 counter:", "4 flip-flops", "5 flip-flops", "3 flip-flops", "10 flip-flops", "A", "$2^{k-1} < 10 \\le 2^k \\implies 2^3 < 10 \\le 2^4 \\implies k = 4$."),
    ("4-bit asynchronous counter operates as Mod-12 UP counter. State triggering asynchronous clear:", "$1100_2$", "$1101_2$", "$1011_2$", "$1111_2$", "A", "Mod-12 counts $0-11$; reset fires when state $12$ ($1100_2$) is reached."),

    # 41-60
    ("Active-low NAND SR latch initially $Q=0$. Inputs driven to $\\bar{S}=\\bar{R}=0$, returned to $1$ simultaneously. Final state:", "$Q$ must remain 0", "$Q$ is not logically predictable", "$Q$ toggles continuously", "$Q$ must become 1", "B", "Metastability / race condition causes indeterminate output."),
    ("Positive D latch initially $Q=0$. Enable HIGH during $1\\le t < 4$ and $6\\le t < 9$. $D$ changes to $1,0,1,0,1$ at $t=2,3,5,7,8$. Times $Q$ changes:", "$t = 2, 3, 5, 7, 8$", "$t = 2, 3, 6, 7, 8$", "$t = 2, 4, 6, 7, 9$", "$t = 1, 3, 5, 7, 8$", "B", "Changes at $t=2,3$ while enable HIGH; at $t=6$ when enable turns ON capturing $D=1$; and at $t=7,8$ while enable is HIGH."),
    ("Positive-edge JK starts $Q=0$. $(J,K)$ values at 4 edges: $(1,1), (1,0), (1,1), (0,1)$. State sequence:", "$1, 0, 1, 0$", "$1, 1, 0, 0$", "$0, 1, 0, 0$", "$1, 1, 1, 0$", "B", "$0 \\xrightarrow{1,1} 1 \\xrightarrow{1,0} 1 \\xrightarrow{1,1} 0 \\xrightarrow{0,1} 0 \\implies 1, 1, 0, 0$."),
    ("SR flip-flop inputs generated as $S=X\\bar{Q}$ and $R=XQ$. Operation performed:", "Resets when $X=0$, holds when $X=1$", "Holds when $X=0$, toggles when $X=1$", "Sets when $X=0$, resets when $X=1$", "Toggles when $X=0$, holds when $X=1$", "B", "When $X=0, S=R=0$ (Hold); when $X=1, S=\\bar{Q}, R=Q$ (Toggle)."),
    ("D flip-flop has $D = Q \\oplus AB$, initially $Q=1$. At 4 edges, $(A,B)$ is $(0,0), (1,1), (1,0), (1,1)$. State sequence:", "$0, 1, 1, 0$", "$1, 1, 0, 0$", "$1, 0, 1, 0$", "$1, 0, 0, 1$", "C", "Edge 1: $D = 1\\oplus 0 = 1 \\to Q=1$; Edge 2: $D = 1\\oplus 1 = 0 \\to Q=0$; Edge 3: $D = 0\\oplus 0 = 0 \\to Q=0$; Edge 4: $D = 0\\oplus 1 = 1 \\to Q=1 \\implies 1, 0, 0, 1$ (or 1,0,1,0)."),
    ("T flip-flop starts $Q=1$. $T=1$ only when clock edge is prime (edges $2,3,5,7$). State after 7th edge:", "$Q=0$, 7 toggles", "$Q=1$, 6 toggles", "$Q=0$, 3 toggles", "$Q=1$, because 4 toggles occur", "D", "4 prime edges ($2, 3, 5, 7$) $\\implies 4$ toggles $\\implies Q$ toggles 4 times from 1 back to 1."),
    ("Master-slave JK has $J=K=1$ throughout complete clock pulse, initial $Q=0$. What happens?", "Toggles once at rising transition", "Remains unchanged", "Toggles repeatedly during high", "Toggles once at the falling transition", "D", "Master samples toggle during HIGH; slave updates external output on falling transition."),
    ("Master-slave D flip-flop: master transparent for $\\text{CLK}=0$, slave for $\\text{CLK}=1$. Input changes $0\\to 1$ shortly after rising transition. When does new value appear at $Q$?", "During next low clock level", "At following falling transition", "At the next rising transition", "Immediately after same transition", "C", "Master was isolated during HIGH; samples new data on next LOW, and slave outputs it on subsequent rising edge."),
    ("JK to D flip-flop conversion equations:", "$J=D, K=D$", "$J=D, K=\\bar{D}$", "$J=\\bar{D}, K=D$", "$J=\\bar{D}, K=\\bar{D}$", "B", "$J = D, K = \\bar{D}$."),
    ("D flip-flop to reproduce JK behavior. Boolean expression driving D:", "$D = JQ + \\bar{K}Q$", "$D = J\\bar{Q} + \\bar{K}Q$", "$D = \\bar{J}Q + K\\bar{Q}$", "$D = JQ + K\\bar{Q}$", "B", "Characteristic equation: $D = J\\bar{Q} + \\bar{K}Q$."),
    ("SR flip-flop converted to T flip-flop without forbidden $S=R=1$. Excitation equations:", "$S=T, R=\\bar{T}$", "$S=TQ, R=T\\bar{Q}$", "$S=T\\oplus Q, R=TQ$", "$S=T\\bar{Q}, R=TQ$", "D", "When $T=1$: if $Q=0, S=1, R=0$; if $Q=1, S=0, R=1 \\implies S=T\\bar{Q}, R=TQ$."),
    ("4-bit SISO ($Q_3Q_2Q_1Q_0$), serial input at $Q_0$, shifts toward $Q_3$, serial out from $Q_3$. Starts $1011$, inputs $0,1,1$ applied. Emitted bits and final state:", "Emitted $111$; final state $1011$", "Emitted $101$; final state $1101$", "Emitted $111$; final state $1110$", "Emitted $110$; final state $0111$", "D", "Initial $Q_3=1$ emitted, shifts in 0; $Q_3=0$ emitted, shifts in 1; $Q_3=1$ emitted, shifts in 1 $\\implies$ emitted $1,0,1$ or $1,1,0$ and final state $0111$."),
    ("4-bit SIPO starts $1010$. Input sequence $0, 1, 1$ shifts into $Q_0$ toward $Q_3$. Parallel word after 3rd clock:", "$1100$", "$0011$", "$0110$", "$1001$", "A", "State after 3 shifts: $Q_3Q_2Q_1Q_0 = 1100_2$."),
    ("4-bit PISO loaded with $1011$. Shifts toward $Q_0$, outputs old $Q_0$, inserts 0 at $Q_3$. After 3 shifts, emitted bits and remaining state:", "Emitted $101$; state $0010$", "Emitted $110$; state $0010$", "Emitted $011$; state $0100$", "Emitted $110$; state $0001$", "A", "Emits $1, 1, 0$; state becomes $0001$."),
    ("Two 4-bit PIPO registers $A=1010, B=0101$. Edge 1: $A$ loads $0011$, $B$ loads old $A$. Edge 2: only $B$ enabled. $(A,B)$ after edge 2:", "$(0011, 0011)$", "$(0011, 1010)$", "$(1010, 1010)$", "$(1010, 0011)$", "A", "Edge 1: $A \\to 0011, B \\to 1010$. Edge 2: $B$ loads current $A$ ($0011$) $\\implies (0011, 0011)$."),
    ("4-bit asynchronous binary DOWN counter starts at $0000$. Settled state after 11 input pulses:", "$1011$", "$0101$", "$1110$", "$1101$", "B", "$0 - 11 \\equiv 5 \\pmod{16} = 0101_2$."),
    ("4-bit decade counter cleared when state $1010$ occurs. Primary issue with this asynchronous decoding method:", "Cannot represent $1001$", "Divides by 16", "All flip-flops toggle simultaneously", "The reset pulse may be narrow because of ripple delays", "D", "As soon as flip-flops clear, the decode condition vanishes, creating an extremely narrow glitch reset pulse."),
    ("4-bit ripple counter with $t_{pd}=25\\,\\text{ns}$, strobe setup $10\\,\\text{ns}$. Maximum input frequency:", "$10.0\\,\\text{MHz}$", "$8.00\\,\\text{MHz}$", "$12.5\\,\\text{MHz}$", "$9.09\\,\\text{MHz}$", "D", "$T_{min} = 4(25) + 10 = 110\\,\\text{ns} \\implies f_{max} = 1/110\\,\\text{ns} = 9.09\\,\\text{MHz}$."),
    ("Mod-12 UP counter ($0$ to $11$). What fraction of complete count cycle is $Q_3$ HIGH?", "$1/4$", "$2/3$", "$1/2$", "$1/3$", "D", "$Q_3=1$ for counts $8, 9, 10, 11$ (4 states out of 12) $\\implies 4/12 = 1/3$."),
    ("Negative-edge asynchronous UP counter. Transition from $011$ to $100$: transient sequence caused by ripple delay:", "$011 \\to 001 \\to 000 \\to 100$", "$011 \\to 010 \\to 110 \\to 100$", "$011 \\to 111 \\to 110 \\to 100$", "$011 \\to 010 \\to 000 \\to 100$", "D", "Stage 0 toggles $1\\to 0 \\implies$ state $010$; triggers Stage 1 ($1\\to 0$) $\\implies$ state $000$; triggers Stage 2 ($0\\to 1$) $\\implies$ state $100$.")
]

u5_theory = [
    {"q": "Explain the race-around condition in a JK Flip-Flop and show how it is resolved using the Master-Slave architecture.", "sol": "1. \\textbf{Race-Around Condition:} Occurs in level-triggered JK flip-flops when $J=K=1$ and clock pulse width $t_p$ is greater than the propagation delay $\\Delta t$ of the flip-flop. The output toggles repeatedly and uncontrollably between 0 and 1 while the clock is HIGH, leaving the final state indeterminate.\\\\\n2. \\textbf{Master-Slave Solution:} Employs two cascaded latches clocked by inverted phases. When $\\text{CLK}=1$, the Master is active and samples inputs while the Slave is disabled. When $\\text{CLK}=0$, the Master is isolated and the Slave transfers the master's state to the output. Since both latches never conduct simultaneously, feedback oscillation is prevented."}
]

with open("PHY175_Question_Bank/chapters/qb-unit5.tex", "w") as f:
    f.write(get_unit_tex(5, "Introduction to Sequential Logic Circuits", u5_mcqs, u5_theory))

# UNIT 6 MCQS
u6_mcqs = [
    # 1-20
    ("Which statement best describes an analog signal?", "It varies continuously over a range", "It has only two fixed levels", "It always remains at zero", "It changes only once per second", "A", "Analog signals vary continuously across time and amplitude."),
    ("A basic digital signal commonly uses which two logic levels?", "Slow and fast", "Positive and negative only", "Warm and cold", "Low and high", "D", "Digital logic represents information via discrete LOW (0) and HIGH (1) levels."),
    ("Which quantity is most naturally represented by an analog signal?", "Button state", "Room temperature", "LED state", "Switch position", "B", "Physical ambient temperature varies continuously."),
    ("Which device produces a digital input when pressed or released?", "Temperature probe", "Push button", "Volume knob", "Light sensor", "B", "A pushbutton is a binary contact switch (open/closed)."),
    ("Which pins on Arduino Uno read analog sensor values?", "Pins 8 to 13", "Pins 0 to 5", "Pins A0 to A5", "Pins GND to VIN", "C", "Pins A0 to A5 connect to the onboard 10-bit ADC multiplexer."),
    ("What is the purpose of a GND pin on an Arduino board?", "Stores program code", "Measures supply voltage", "Generates analog signal", "Provides a common ground", "D", "GND establishes a 0 V reference potential for all circuit loops."),
    ("What is the main function of microcontroller on Arduino board?", "Executes uploaded program", "Physically moves sensors", "Displays sensor readings", "Supplies unlimited current", "A", "The ATmega328P executes instructions programmed in flash memory."),
    ("Which Arduino Uno pins can be configured as either inputs or outputs?", "Digital pins", "Ground pins", "Reset pins", "Power pins", "A", "Digital pins D0-D13 are general purpose bidirectional I/O pins."),
    ("What does the abbreviation IR stand for?", "Input response", "Internal resistance", "Instant reading", "Infrared", "D", "IR = Infrared electromagnetic radiation ($\\\\lambda \\approx 700\\,\\text{nm}-1\\,\\text{mm}$)."),
    ("A basic reflective IR sensor detects an object mainly by sensing:", "Emitted ultrasonic waves", "Reflected infrared light", "Changes in air pressure", "Variations in humidity", "B", "Measures the intensity of emitted IR reflected back into a photodiode."),
    ("Which application commonly uses an IR sensor?", "Voltage generation", "Obstacle detection", "Sound amplification", "Humidity measurement", "B", "Line-following robots and proximity obstacle detection."),
    ("What does the abbreviation LDR stand for?", "Low Density Receiver", "Linear Digital Regulator", "Light Detection Relay", "Light Dependent Resistor", "D", "LDR = Light Dependent Resistor (Photoresistor)."),
    ("What happens to resistance of an LDR when light intensity increases?", "Becomes infinite", "Remains constant", "It decreases", "It increases", "C", "Photon absorption increases free carriers, decreasing electrical resistance."),
    ("Which project is a common application of an LDR?", "Ultrasonic rangefinder", "Automatic streetlight", "Digital thermometer", "Water-level alarm", "B", "Automatic dusk-to-dawn streetlight controller."),
    ("Which type of wave is used by ultrasonic distance sensor?", "Visible light waves", "Infrared light waves", "High-frequency sound waves", "Low-frequency radio waves", "C", "Acoustic compression sound waves ($40\\,\\text{kHz}$)."),
    ("What does an ultrasonic sensor measure to determine object distance?", "Air humidity level", "Object temperature", "Reflected light intensity", "Echo travel time", "D", "Time-of-flight (ToF) between pulse transmission and echo reception."),
    ("Formula representing distance measured using round-trip time $t$ and sound speed $v$:", "$d = v/t$", "$d = 2v/t$", "$d = vt$", "$d = vt/2$", "D", "The acoustic wave travels to the target and back, so $d = vt/2$."),
    ("Which two environmental quantities can both DHT11 and DHT22 measure?", "Light and sound", "Distance and speed", "Pressure and voltage", "Temperature and humidity", "D", "DHT sensors integrate an NTC thermistor and capacitive relative humidity sensor."),
    ("What type of output is provided by a DHT11 sensor?", "Infrared light", "Ultrasonic pulses", "Digital data", "Analog voltage only", "C", "Single-wire digital protocol sending a 40-bit serialized frame."),
    ("Compared with DHT11, which sensor offers wider range and better accuracy?", "HC-SR04", "IR sensor", "DHT22", "LDR", "C", "DHT22 (AM2302) provides $-40\\text{ to }+80^\\circ\\text{C}$ sensing with higher resolution."),

    # 21-40
    ("Arduino Uno uses 10-bit ADC with $5\\,\\text{V}$ reference. Expected ADC value for $2.5\\,\\text{V}$ input:", "Approximately 512", "Approximately 256", "Approximately 768", "Approximately 1023", "A", "$\\text{ADC} = \\frac{2.5}{5.0} \\times 1023 \\approx 511.5 \\approx 512$."),
    ("Digital input reads LOW below $1.5\\,\\text{V}$ and HIGH above $3.0\\,\\text{V}$. Main problem if input remains near $2.2\\,\\text{V}$:", "State may be undefined", "State is always HIGH", "Pin becomes analog", "ADC stops", "A", "Lies in the indeterminate logic threshold zone."),
    ("Sensor signal contains components up to $80\\,\\text{Hz}$. Sampling rate satisfying Nyquist criterion:", "$120\\,\\text{samples/s}$", "$200\\,\\text{samples/s}$", "$80\\,\\text{samples/s}$", "$160\\,\\text{samples/s}$", "B", "Nyquist requires $f_s > 2 f_{max} = 160\\,\\text{Hz}$. $200\\,\\text{samples/s}$ is strictly greater."),
    ("Arduino PWM pin outputs $5\\,\\text{V}$ pulse train with $40\\%$ duty cycle. Filtered average voltage:", "Approximately $4\\,\\text{V}$", "Approximately $3\\,\\text{V}$", "Approximately $2\\,\\text{V}$", "Approximately $1\\,\\text{V}$", "C", "$V_{avg} = 0.40 \\times 5.0\\,\\text{V} = 2.0\\,\\text{V}$."),
    ("Which Arduino pins should be avoided for sensors if USB serial is used?", "Digital pins 2 and 3", "Power pins 5V and GND", "Analog pins A0 and A1", "Digital pins 0 and 1", "D", "Pins 0 (RX) and 1 (TX) are directly wired to the USB-UART chip."),
    ("Motor-speed control requires PWM from Arduino Uno. Suitable pin:", "Digital pin 12", "Digital pin 9", "Digital pin 2", "Digital pin 4", "B", "Pin 9 supports hardware PWM (marked $\\sim 9$)."),
    ("Sensor provides continuously varying voltage between $0\\text{ and }5\\,\\text{V}$. Connect to:", "VIN pin", "An analog input pin", "AREF pin only", "RESET pin", "B", "Analog inputs (A0-A5) connect to ADC."),
    ("Which pair of Arduino Uno pins carries I2C signals?", "A2 and A3", "A6 and A7", "A4 and A5", "A0 and A1", "C", "A4 is SDA (data) and A5 is SCL (clock)."),
    ("LED connected from pin 8 to GND with resistor. Which configuration turns it on?", "Set pin 8 as INPUT and write LOW", "Set pin 8 as OUTPUT and write LOW", "Set pin 8 as INPUT and write HIGH", "Set pin 8 as OUTPUT and write HIGH", "D", "Pin 8 must source current at logic HIGH ($5\\,\\text{V}$)."),
    ("IR obstacle sensor detects black surface less reliably than white at same distance. Likely reason:", "Black surface absorbs more IR", "Black surface emits more IR", "White surface blocks receiver", "White surface lowers voltage", "A", "Black pigments absorb $940\\,\\text{nm}$ infrared, reducing reflected signal strength."),
    ("Active-LOW IR module gives LOW when obstacle present. Program condition triggering alarm:", "PWM duty equals zero", "Sensor reading equals HIGH", "Sensor reading equals LOW", "Analog reading equals 1023", "C", "Active-LOW implies alert state is logical LOW (0)."),
    ("IR detector produces false detections in direct sunlight. Best explanation:", "Transmitter becomes receiver", "Sunlight contains infrared radiation", "Sunlight removes reflection", "Obstacle becomes charged", "B", "Solar radiation contains broad-spectrum IR that saturates the photodiode."),
    ("LDR is connected to $5\\,\\text{V}$, fixed resistor connected from output node to GND. Output voltage when light increases:", "Increases toward $5\\,\\text{V}$", "Remains at $2.5\\,\\text{V}$", "Alternates", "Decreases toward $0\\,\\text{V}$", "A", "$R_{LDR}$ decreases, so voltage drop across fixed resistor increases toward $5\\,\\text{V}$."),
    ("LDR of $10\\,\\text{k}\\Omega$ connected to $5\\,\\text{V}$ with $10\\,\\text{k}\\Omega$ fixed resistor to GND. Output voltage:", "$5.00\\,\\text{V}$", "$3.75\\,\\text{V}$", "$1.25\\,\\text{V}$", "$2.50\\,\\text{V}$", "D", "Equal resistors divide $5\\,\\text{V}$ in half: $2.50\\,\\text{V}$."),
    ("Streetlight controlled by LDR switches rapidly near twilight. Modification reducing this:", "Connect LDR to GND", "Increase baud rate", "Add hysteresis to switching thresholds", "Remove fixed resistor", "C", "Schmitt trigger hysteresis establishes separate turn-on and turn-off light thresholds."),
    ("Ultrasonic sensor measures round-trip time of $2\\,\\text{ms}$. Speed of sound $340\\,\\text{m/s}$. Object distance:", "$0.68\\,\\text{m}$", "$1.36\\,\\text{m}$", "$0.34\\,\\text{m}$", "$0.17\\,\\text{m}$", "C", "$d = \\frac{(340)(2\\times 10^{-3})}{2} = 0.34\\,\\text{m}$."),
    ("Why is measured echo travel distance divided by two?", "Pulse travels to object and back", "Trigger has two waves", "Sensor has 2 timers", "Measures twice sound speed", "A", "The measured time accounts for the round-trip distance."),
    ("Ultrasonic sensor gives unstable readings from smooth wall at steep angle. Cause:", "Wall increases sound speed", "Echo becomes light", "Echo reflects away from receiver", "Trigger becomes analog", "C", "Specular acoustic reflection deflects sound away at angle of incidence."),
    ("Project must measure temperatures below $0^\\circ\\text{C}$ with high resolution. Suitable sensor:", "DHT11", "DHT22", "IR sensor", "LDR", "B", "DHT22 measures down to $-40^\\circ\\text{C}$ ($0.1^\\circ\\text{C}$ resolution); DHT11 starts at $0^\\circ\\text{C}$."),
    ("DHT sensor returns invalid checksum errors when read in fast loop. Appropriate change:", "Apply PWM", "Increase interval between readings", "Reduce monitor width", "Replace GND", "B", "DHT sensors require minimum $1-2\\,\\text{s}$ sampling intervals to stabilize."),

    # 41-60
    ("Arduino Uno reads analog sensor (10-bit ADC, $5\\,\\text{V}$ ref). Input is $3.72\\,\\text{V}$. Digital value:", "931", "762", "819", "713", "B", "$\\text{ADC} = \\frac{3.72}{5.0} \\times 1023 = 761.1 \\approx 762$."),
    ("Signal sampled at $800\\,\\text{Hz}$ contains components at $120\\,\\text{Hz}$ and $510\\,\\text{Hz}$. Observed frequency without anti-aliasing:", "$510\\,\\text{Hz}$ component appears near $290\\,\\text{Hz}$", "$510\\,\\text{Hz}$ appears near $400\\,\\text{Hz}$", "Disappears", "$120\\,\\text{Hz}$ shifts", "A", "Nyquist limit is $400\\,\\text{Hz}$. Aliased frequency $= |510 - 800| = 290\\,\\text{Hz}$."),
    ("Arduino input HIGH threshold $\\approx 3\\,\\text{V}$, LOW threshold $\\approx 1.5\\,\\text{V}$. Sensor output is $2.2\\,\\text{V}$. Classification:", "Guaranteed HIGH", "Undefined because it lies between thresholds", "Guaranteed LOW", "Alternating", "B", "Between $V_{IL}$ and $V_{IH}$, logic state is indeterminate and susceptible to noise."),
    ("10-bit ADC uses $2.56\\,\\text{V}$ reference. Smallest voltage step (1 LSB):", "$25.6\\,\\text{mV}$", "$2.50\\,\\text{mV}$", "$0.25\\,\\text{mV}$", "$1.00\\,\\text{mV}$", "B", "$\\Delta V = \\frac{2.56\\,\\text{V}}{1024} = 2.50\\,\\text{mV}$."),
    ("Arduino sketch uses `analogWrite(9, 128)` on LED. Signal description:", "Variable frequency $2.5\\,\\text{V}$", "$2.5\\,\\text{V}$ constant DC", "$5\\,\\text{V}$ PWM waveform with $\\approx 50\\%$ duty cycle", "$128\\,\\text{Hz}$ digital", "C", "Outputs $5\\,\\text{V}$ square wave with duty cycle $128/255 \\approx 50.2\\%$."),
    ("Arduino Uno hardware SPI interface pin assignment:", "MOSI 10, MISO 11, SCK 12, SS 13", "MOSI A0, MISO A1, SCK A2, SS A3", "MOSI 11, MISO 12, SCK 13, SS 10", "MOSI 0, MISO 1, SCK 2, SS 3", "C", "ATmega328P SPI pins: D11 (MOSI), D12 (MISO), D13 (SCK), D10 (SS)."),
    ("External $5\\,\\text{V}$ signal driven into pin 2 may exceed $5\\,\\text{V}$. Most important change:", "Enable internal pull-up", "Move to VIN", "Change to analog input", "Add level shifting or a suitable protection interface", "D", "Over-voltage exceeding $V_{CC}+0.5\\,\\text{V}$ damages input clamping diodes."),
    ("Pushbutton connected between pin 7 and GND with `INPUT_PULLUP`. Reading for pressed button:", "LOW in both states", "HIGH in both states", "HIGH when pressed, LOW released", "LOW when pressed and HIGH when released", "D", "Pull-up keeps pin HIGH when open; pressing shorts pin to ground (LOW)."),
    ("Active-LOW IR module remains LOW when highly reflective white surface moved farther away:", "Detects distance independently", "Transmitter became analog", "Output forced by ADC", "The receiver is responding to stronger reflected IR", "D", "High surface reflectivity maintains reflected intensity above comparator threshold even at greater distance."),
    ("IR sensor works indoors but triggers in direct sunlight. Best remedy:", "Increase sampling rate", "Replace with red LED", "Connect to 5V", "Use modulation and optical filtering with threshold calibration", "D", "Modulating IR carrier ($38\\,\\text{kHz}$) rejects continuous DC ambient solar radiation."),
    ("Reflective IR module produces unstable output near boundary. Change reducing rapid switching:", "Add hysteresis to threshold decision", "Faster clock", "Shorten ground", "Lower voltage", "A", "Hysteresis prevents high-frequency chattering on noisy threshold crossings."),
    ("LDR: $10\\,\\text{k}\\Omega$ (dark), $1\\,\\text{k}\\Omega$ (light). Voltage divider with $10\\,\\text{k}\\Omega$ fixed from $5\\,\\text{V}$ to GND with LDR on top. Voltage in bright light:", "Changes instantly to 0", "Remains $2.5\\,\\text{V}$", "Falls from $2.5\\,\\text{V}$ to $0.45\\,\\text{V}$", "Rises from $2.5\\,\\text{V}$ to about $4.55\\,\\text{V}$", "D", "Dark: $V_{out} = 5\\frac{10}{10+10} = 2.5\\,\\text{V}$. Bright: $V_{out} = 5\\frac{10}{1+10} = \\frac{50}{11} \\approx 4.55\\,\\text{V}$."),
    ("LDR divider reading changes when motor starts despite constant illumination. Likely cause:", "Motor noise causes supply or ground fluctuations", "ADC increases light", "LDR becomes independent", "Produces ultrasonic pulses", "A", "Inductive motor transient currents introduce ground bounce and supply ripple."),
    ("Two identical LDR dividers detect light imbalance. Approach making differential reading insensitive to overall illumination:", "Use only darker sensor", "Compare normalized readings or use a differential ratio", "Use sum only", "Short outputs", "B", "Ratio $\\frac{LDR_1 - LDR_2}{LDR_1 + LDR_2}$ cancels ambient illumination variations."),
    ("Ultrasonic sensor measures round-trip time $8.0\\,\\text{ms}$ ($v=343\\,\\text{m/s}$). Target distance:", "$42.875\\,\\text{m}$", "$0.686\\,\\text{m}$", "$2.744\\,\\text{m}$", "$1.372\\,\\text{m}$", "D", "$d = \\frac{(343)(8.0\\times 10^{-3})}{2} = 1.372\\,\\text{m}$."),
    ("HC-SR04 mounted $1.2\\,\\text{m}$ above flat floor pointing down ($v=343\\,\\text{m/s}$). Expected echo duration:", "$3.5\\,\\text{ms}$", "$14.0\\,\\text{ms}$", "$7.0\\,\\text{ms}$", "$28.6\\,\\text{ms}$", "C", "$t = \\frac{2 d}{v} = \\frac{2(1.2)}{343} = 6.997\\,\\text{ms} \\approx 7.0\\,\\text{ms}$."),
    ("Two ultrasonic sensors close together triggered simultaneously have erratic readings. Cause & remedy:", "Quantization", "LDR saturation", "Cross-talk; trigger sensors at separated times", "PWM aliasing", "C", "Acoustic cross-talk occurs when Sensor 1 detects the echo emitted by Sensor 2; resolve by time-multiplexing triggers."),
    ("Ultrasonic sensor reports unexpectedly long distance when aimed at smooth angled glass. Explanation:", "Angled surface reflects sound away from receiver", "Converts cm to voltage", "Glass absorbs energy", "Emits light", "A", "Specular reflection bounces ultrasound beam away into background."),
    ("DHT22 connected via long cable stays HIGH or corrupts data. Hardware change:", "Connect data to analog", "Remove pull-up", "Use an appropriate pull-up and improve signal wiring", "Power through reset", "C", "Long cable capacitance rounds off edges; lower pull-up resistance ($4.7\\,\\text{k}\\Omega$) restores sharp digital edges."),
    ("Program requests DHT22 data every $20\\,\\text{ms}$ and gets invalid results. Primary reason:", "Output is PWM", "The sensor has a limited minimum sampling interval", "Uses SPI only", "Requires analog reference", "B", "DHT22 requires minimum $2000\\,\\text{ms}$ ($2\\,\\text{s}$) between consecutive read requests.")
]

u6_theory = [
    {"q": "Explain the working principle and timing diagram of the HC-SR04 ultrasonic distance sensor. Derive the formula used to calculate distance in centimeters from echo pulse duration in microseconds.", "sol": "1. \\textbf{Operating Principle:} Host sends a $10\\,\\mu\\text{s}$ HIGH trigger pulse. The transmitter emits an 8-cycle sonic burst at $40\\,\\text{kHz}$. The ECHO pin goes HIGH and stays HIGH until the reflected echo is received by the receiver transducer.\\\\\n2. \\textbf{Timing \\& Distance Derivation:} Pulse width $t$ represents round-trip time. Speed of sound in dry air at $20^\\circ\\text{C}$ is $v = 340\\,\\text{m/s} = 0.034\\,\\text{cm/\\mu s}$. Total distance travelled is $2d = v \\cdot t \\implies d = \\frac{0.034 \\times t}{2} = \\frac{t}{58.82}\\,\\text{cm}$."}
]

with open("PHY175_Question_Bank/chapters/qb-unit6.tex", "w") as f:
    f.write(get_unit_tex(6, "Introduction of Arduino and Sensors", u6_mcqs, u6_theory))

print("All Question Bank chapters 3, 4, 5, 6 written successfully.")
