import os
import subprocess

print("Fixing ampersand in question bank strings...")

with open("generate_complete_phy175_qb_all.py", "r") as f:
    code = f.read()

# Make sure all bare '&' in text strings get replaced by '\&'
new_clean_set = '''def clean_set(mcqs):
    res = []
    for q, a, b, c, d, ans, rat in mcqs:
        def fix(s):
            # Normalize percentage
            s = s.replace(r"\\%", "%")
            s = s.replace("%", r"\\%")
            # Normalize ampersands
            s = s.replace(r"\\&", "&")
            s = s.replace("&", r"\\&")
            # Normalize common names
            s = s.replace("INPUT_PULLUP", r"\\texttt{INPUT\\_PULLUP}")
            s = s.replace("analogWrite(9, 128)", r"\\texttt{analogWrite(9, 128)}")
            return s
        res.append((fix(q), fix(a), fix(b), fix(c), fix(d), ans, fix(rat)))
    return res'''

import re
code = re.sub(r'def clean_set\(mcqs\):[\s\S]*?return res', new_clean_set, code)

with open("generate_complete_phy175_qb_all.py", "w") as f:
    f.write(code)

print("Updated generate_complete_phy175_qb_all.py")
