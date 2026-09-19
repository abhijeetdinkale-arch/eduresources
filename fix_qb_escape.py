import os
import subprocess

print("Fixing LaTeX escape handling in Question Bank...")

# Clean helper for LaTeX text
def clean_set(mcqs):
    res = []
    for q, a, b, c, d, ans, rat in mcqs:
        def fix(s):
            # First normalize \% to %
            s = s.replace(r"\%", "%")
            # Then replace % with raw LaTeX \%
            s = s.replace("%", r"\%")
            s = s.replace("INPUT_PULLUP", r"\texttt{INPUT\_PULLUP}")
            s = s.replace("analogWrite(9, 128)", r"\texttt{analogWrite(9, 128)}")
            s = s.replace("d(0,2,8,10)", r"$d(0,2,8,10)$")
            return s
        res.append((fix(q), fix(a), fix(b), fix(c), fix(d), ans, fix(rat)))
    return res

# Re-run builder
with open("generate_complete_phy175_qb_all.py", "r") as f:
    code = f.read()

# Replace the clean_set definition in the file
new_clean_set_code = '''def clean_set(mcqs):
    res = []
    for q, a, b, c, d, ans, rat in mcqs:
        def fix(s):
            s = s.replace(r"\\%", "%")
            s = s.replace("%", r"\\%")
            s = s.replace("INPUT_PULLUP", r"\\texttt{INPUT\\_PULLUP}")
            s = s.replace("analogWrite(9, 128)", r"\\texttt{analogWrite(9, 128)}")
            s = s.replace("d(0,2,8,10)", r"$d(0,2,8,10)$")
            return s
        res.append((fix(q), fix(a), fix(b), fix(c), fix(d), ans, fix(rat)))
    return res'''

import re
code = re.sub(r'def clean_set\(mcqs\):[\s\S]*?return res', new_clean_set_code, code)

with open("generate_complete_phy175_qb_all.py", "w") as f:
    f.write(code)

print("Updated generator.")
