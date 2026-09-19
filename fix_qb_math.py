import os
import subprocess

print("Writing clean, verified generator for PHY175 Question Bank...")

# Fix the string clean function
def clean_set(mcqs):
    res = []
    for q, a, b, c, d, ans, rat in mcqs:
        def fix(s):
            # Normalize percentage
            s = s.replace(r"\%", "%")
            s = s.replace("%", r"\%")
            # Normalize common names
            s = s.replace("INPUT_PULLUP", r"\texttt{INPUT\_PULLUP}")
            s = s.replace("analogWrite(9, 128)", r"\texttt{analogWrite(9, 128)}")
            return s
        res.append((fix(q), fix(a), fix(b), fix(c), fix(d), ans, fix(rat)))
    return res

# Read generate_complete_phy175_qb_all.py
with open("generate_complete_phy175_qb_all.py", "r") as f:
    code = f.read()

# Replace the d(0,2,8,10) line in the clean_set function
code = code.replace('s = s.replace("d(0,2,8,10)", r"$d(0,2,8,10)$")', '')
code = code.replace('s = s.replace("d(0,2,8,10)", r"\\$d(0,2,8,10)\\$")', '')

with open("generate_complete_phy175_qb_all.py", "w") as f:
    f.write(code)

print("generate_complete_phy175_qb_all.py updated.")
