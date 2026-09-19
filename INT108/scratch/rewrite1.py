import os

target_file = "/Users/abhidinkale/Documents/mark p1/INT108/chapters/chapter-08-practical-coding-challenges.tex"

header = r"""\chapter{Cross-Unit Practical Coding Challenges}
\label{chap:practical-coding-challenges}

% ==============================================================================
% SECTION 8.1: OVERVIEW
% ==============================================================================
\section{Multi-Concept Engineering Software Challenges}

University practical examinations and semester capstone tests require integrating multiple Python concepts into unified, robust software systems. This chapter provides a comprehensive suite of 17 multi-topic engineering challenges accompanied by complete, production-grade implementations.

Each challenge is designed to mimic real-world software engineering tasks. By working through these problems, students will develop the ability to decompose complex requirements into modular, maintainable code. The challenges progress from foundational concepts to advanced algorithmic patterns, ensuring a thorough preparation for university assessments and technical interviews.

"""

ch1 = r"""% ==============================================================================
% CHALLENGE 1: STUDENT MANAGEMENT SYSTEM
% ==============================================================================
\section{Challenge 1: Student Record \& Grade Ledger System}

\textbf{Difficulty:} Moderate

\textbf{Algorithmic Explanation:}
The core challenge in building a student management system lies in effectively linking in-memory objects to persistent storage. By representing each student as an instance of a \texttt{Student} class, we encapsulate their attributes (registration number, name, and marks) alongside their behaviors (calculating averages and determining letter grades). This object-oriented approach ensures that validation and computation remain closely tied to the data they operate on.

To handle persistence, the \texttt{StudentDatabase} class manages a dictionary mapping registration numbers to \texttt{Student} objects. This allows for $O(1)$ average time complexity when looking up or updating a student's record. When saving or loading data, we convert the objects to and from comma-separated values (CSV) format. This serialization process is essential for ensuring that data survives program termination, a critical requirement for any real-world ledger system.

\begin{practiceset}[Problem Specification 1]
Design a complete \texttt{StudentManager} class that reads student records from a CSV text file, computes course averages and letter grades using chained conditionals, handles \texttt{FileNotFoundError}, and allows updating records and saving back to disk.

\textbf{Test Cases:}
\begin{itemize}
    \item \textbf{Normal:} Input marks \texttt{88, 92, 95} $\rightarrow$ Output Average \texttt{91.67}, Grade \texttt{A+}
    \item \textbf{Boundary:} Input marks \texttt{50, 50, 50} $\rightarrow$ Output Average \texttt{50.00}, Grade \texttt{D}
    \item \textbf{Error:} Missing file on startup $\rightarrow$ Graceful fallback to empty dictionary.
\end{itemize}
\end{practiceset}

\begin{pythoncode}{Student Grade Management Implementation}
import os

class Student:
    def __init__(self, reg_no, name, m1, m2, m3):
        self.reg_no = reg_no
        self.name = name
        self.marks = [float(m1), float(m2), float(m3)]
        
    def get_average(self):
        return sum(self.marks) / len(self.marks)
        
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else: return "F"
        
    def to_csv_line(self):
        return f"{self.reg_no},{self.name},{self.marks[0]},{self.marks[1]},{self.marks[2]}\n"

class StudentDatabase:
    def __init__(self, filepath="students.csv"):
        self.filepath = filepath
        self.students = {}
        self.load_data()
        
    def load_data(self):
        if not os.path.exists(self.filepath):
            return
        try:
            with open(self.filepath, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 5:
                        s = Student(parts[0], parts[1], parts[2], parts[3], parts[4])
                        self.students[s.reg_no] = s
        except Exception as e:
            print(f"Error loading records: {e}")
            
    def add_student(self, reg_no, name, m1, m2, m3):
        s = Student(reg_no, name, m1, m2, m3)
        self.students[reg_no] = s
        self.save_data()
        print(f"Student {name} (Reg: {reg_no}) registered successfully.")
        
    def save_data(self):
        with open(self.filepath, "w") as f:
            for s in self.students.values():
                f.write(s.to_csv_line())
                
    def display_all(self):
        print(f"\n{'Reg No':<10} {'Name':<15} {'Average':<10} {'Grade':<6}")
        print("-" * 45)
        for s in self.students.values():
            print(f"{s.reg_no:<10} {s.name:<15} {s.get_average():<10.2f} {s.get_grade():<6}")

# Demonstration
db = StudentDatabase("temp_students.csv")
db.add_student("123001", "Aarav Sharma", 88, 92, 95)
db.add_student("123002", "Diya Patel", 72, 68, 75)
db.display_all()
\end{pythoncode}

\begin{outputbox}
Student Aarav Sharma (Reg: 123001) registered successfully.
Student Diya Patel (Reg: 123002) registered successfully.

Reg No     Name            Average    Grade 
---------------------------------------------
123001     Aarav Sharma    91.67      A+    
123002     Diya Patel      71.67      B     
\end{outputbox}

"""

ch2 = r"""% ==============================================================================
% CHALLENGE 2: SECURE BANKING TRANSACTION LEDGER
% ==============================================================================
\section{Challenge 2: Secure Banking System with Pickling}

\textbf{Difficulty:} Moderate

\textbf{Algorithmic Explanation:}
In banking systems, data integrity and encapsulation are paramount. This implementation utilizes Python's name mangling (\texttt{\_\_balance}) to create private attributes, ensuring that the account balance cannot be modified externally without passing through the \texttt{deposit} and \texttt{withdraw} validation methods.

To handle complex error states, we define a custom exception, \texttt{InsufficientFundsError}. This allows the caller to distinguish between a routine validation failure (like withdrawing more than the balance) and a system-level error. For persistence, we use Python's \texttt{pickle} module, which directly serializes Python objects into a binary stream, preserving the class structure perfectly across executions.

\begin{practiceset}[Problem Specification 2]
Implement an object-oriented \texttt{BankAccount} class hierarchy with private attributes, deposit/withdrawal validation, custom exception handling for overdrafts, and binary persistence using the \texttt{pickle} module.

\textbf{Test Cases:}
\begin{itemize}
    \item \textbf{Normal:} Deposit 2000 to initial 5000 $\rightarrow$ Balance 7000.
    \item \textbf{Boundary:} Withdraw exact balance $\rightarrow$ Balance becomes 0.
    \item \textbf{Error:} Withdraw 8000 from 7000 $\rightarrow$ Raises \texttt{InsufficientFundsError}.
\end{itemize}
\end{practiceset}

\begin{pythoncode}{Secure Banking System with Binary Serialization}
import pickle
import os

class InsufficientFundsError(Exception):
    """Custom exception raised when withdrawal exceeds balance."""
    pass

class BankAccount:
    def __init__(self, acc_number, holder_name, initial_balance=0.0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.__balance = float(initial_balance) # Private attribute
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be strictly positive.")
        self.__balance += amount
        return self.__balance
        
    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError(f"Cannot withdraw Rs. {amount}. Available: Rs. {self.__balance}")
        self.__balance -= amount
        return self.__balance
        
    def get_balance(self):
        return self.__balance

# Bank Storage Engine
DB_FILE = "accounts.pkl"

def save_accounts(accounts_dict):
    with open(DB_FILE, "wb") as f:
        pickle.dump(accounts_dict, f)

def load_accounts():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "rb") as f:
        return pickle.load(f)

# Testing Banking Workflow
accounts = load_accounts()
acc1 = BankAccount("LPU-101", "Kavya Singh", 5000.0)
acc1.deposit(2000.0)

try:
    acc1.withdraw(8000.0) # Triggers custom exception
except InsufficientFundsError as err:
    print("Security Alert:", err)

accounts[acc1.acc_number] = acc1
save_accounts(accounts)
print("Account balance safely serialized to disk:", acc1.get_balance())
\end{pythoncode}

\begin{outputbox}
Security Alert: Cannot withdraw Rs. 8000.0. Available: Rs. 7000.0
Account balance safely serialized to disk: 7000.0
\end{outputbox}

"""

ch3 = r"""% ==============================================================================
% CHALLENGE 3: WEB SERVER LOG FILE ANALYZER
% ==============================================================================
\section{Challenge 3: Web Server Log File Analyzer with Regex}

\textbf{Difficulty:} Hard

\textbf{Algorithmic Explanation:}
Parsing unstructured text data like server logs requires robust pattern matching. Regular expressions provide an elegant, $O(N)$ solution to extract specific fields like IP addresses and HTTP status codes without relying on brittle string splitting logic. 

The algorithm iterates over the regex matches and builds a frequency distribution using a hash map (dictionary). The dictionary's \texttt{get()} method simplifies the counting process by providing a default value of zero for unseen elements, ensuring the time complexity remains dominated by the regex engine's parsing phase rather than the aggregation logic.

\begin{practiceset}[Problem Specification 3]
Build a log analysis engine that scans an access log using regular expressions, extracts client IP addresses and HTTP status codes, counts error occurrences (404 and 500), and outputs a summary report.

\textbf{Test Cases:}
\begin{itemize}
    \item \textbf{Normal:} Valid IPv4 strings and 3-digit HTTP status codes.
    \item \textbf{Boundary:} Log entries with missing fields or malformed data format.
    \item \textbf{Error:} Passing an empty string should result in empty reports without crashing.
\end{itemize}
\end{practiceset}

\begin{pythoncode}{Web Log Regex Parser}
import re

log_data = """
192.168.1.10 - - [29/Aug/2026:10:15:32] "GET /index.html HTTP/1.1" 200 4502
10.0.0.15 - - [29/Aug/2026:10:16:01] "POST /login HTTP/1.1" 404 320
192.168.1.10 - - [29/Aug/2026:10:17:12] "GET /dashboard HTTP/1.1" 200 8920
172.16.0.5 - - [29/Aug/2026:10:18:45] "GET /api/data HTTP/1.1" 500 120
10.0.0.15 - - [29/Aug/2026:10:19:10] "GET /about HTTP/1.1" 200 2400
"""

def analyze_logs(log_text):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    status_pattern = r'"\s+(\d{3})\s+'
    
    ips = re.findall(ip_pattern, log_text)
    status_codes = re.findall(status_pattern, log_text)
    
    ip_frequency = {}
    for ip in ips:
        ip_frequency[ip] = ip_frequency.get(ip, 0) + 1
        
    status_frequency = {}
    for code in status_codes:
        status_frequency[code] = status_frequency.get(code, 0) + 1
        
    print("--- Traffic Analysis by IP Address ---")
    for ip, count in ip_frequency.items():
        print(f"IP: {ip:<15} | Requests: {count}")
        
    print("\n--- HTTP Status Code Summary ---")
    for code, count in status_frequency.items():
        print(f"Status Code {code}: {count} responses")

analyze_logs(log_data)
\end{pythoncode}

\begin{outputbox}
--- Traffic Analysis by IP Address ---
IP: 192.168.1.10    | Requests: 2
IP: 10.0.0.15       | Requests: 2
IP: 172.16.0.5      | Requests: 1

--- HTTP Status Code Summary ---
Status Code 200: 3 responses
Status Code 404: 1 responses
Status Code 500: 1 responses
\end{outputbox}

"""

ch4 = r"""% ==============================================================================
% CHALLENGE 4: MATRIX CALCULATOR SUITE
% ==============================================================================
\section{Challenge 4: 2D Matrix Mathematics Calculator}

\textbf{Difficulty:} Hard

\textbf{Algorithmic Explanation:}
Matrix operations represent standard linear algebra fundamentals. Multiplication is computed using a triple-nested loop, resulting in a time complexity of $O(N^3)$. Proper dimensional validation ($cols\_A == rows\_B$) is performed beforehand to avoid \texttt{IndexError} at runtime.

The determinant logic expands from the simple ad-bc formula for $2 \times 2$ matrices to cofactor expansion for $3 \times 3$ matrices. The $3 \times 3$ determinant is computed by recursively isolating the sub-matrices, calculating their determinants, and combining them with alternating signs, demonstrating the mathematical concept of minors and cofactors.

\begin{practiceset}[Problem Specification 4]
Design a matrix computation module supporting matrix addition, multiplication ($O(N^3)$ algorithm), and determinant calculation for $2 \times 2$ and $3 \times 3$ matrices using nested lists and validation.

\textbf{Test Cases:}
\begin{itemize}
    \item \textbf{Normal:} Multiply $2 \times 2$ with $2 \times 2$, compute det of $3 \times 3$.
    \item \textbf{Boundary:} Matrices with zero elements.
    \item \textbf{Error:} Incompatible matrix dimensions for multiplication.
\end{itemize}
\end{practiceset}

\begin{pythoncode}{Matrix Math Suite Implementation}
class MatrixMath:
    @staticmethod
    def multiply(A, B):
        rA, cA = len(A), len(A[0])
        rB, cB = len(B), len(B[0])
        if cA != rB:
            raise ValueError(f"Incompatible dimensions: ({rA}x{cA}) and ({rB}x{cB})")
        
        res = [[0] * cB for _ in range(rA)]
        for i in range(rA):
            for j in range(cB):
                for k in range(cA):
                    res[i][j] += A[i][k] * B[k][j]
        return res
        
    @staticmethod
    def det2x2(M):
        return (M[0][0] * M[1][1]) - (M[0][1] * M[1][0])

    @staticmethod
    def det3x3(M):
        if len(M) != 3 or any(len(row) != 3 for row in M):
            raise ValueError("Matrix must be exactly 3x3")
        
        a, b, c = M[0]
        # Calculate cofactors
        det_a = a * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        det_b = b * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        det_c = c * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
        
        return det_a - det_b + det_c

mat1 = [[1, 2], [3, 4]]
mat2 = [[2, 0], [1, 2]]
prod = MatrixMath.multiply(mat1, mat2)

mat3 = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]

print("Matrix Product:", prod)
print("Determinant mat1 (2x2):", MatrixMath.det2x2(mat1))
print("Determinant mat3 (3x3):", MatrixMath.det3x3(mat3))
\end{pythoncode}

\begin{outputbox}
Matrix Product: [[4, 4], [10, 8]]
Determinant mat1 (2x2): -2
Determinant mat3 (3x3): -306
\end{outputbox}

"""

with open("generate_script_part1.py", "w") as f:
    f.write("header = r'''" + header + "'''\n")
    f.write("ch1 = r'''" + ch1 + "'''\n")
    f.write("ch2 = r'''" + ch2 + "'''\n")
    f.write("ch3 = r'''" + ch3 + "'''\n")
    f.write("ch4 = r'''" + ch4 + "'''\n")
    f.write(f"with open('{target_file}', 'w') as f:\n")
    f.write("    f.write(header + ch1 + ch2 + ch3 + ch4)\n")

os.system("python3 generate_script_part1.py")
