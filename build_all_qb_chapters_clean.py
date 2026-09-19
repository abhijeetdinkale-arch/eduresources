import os
import subprocess

# Load the units builder
from build_clean_phy175_qb import make_clean_unit_tex
from build_all_phy175_qb_units import u1_mcqs, u1_theory, u2_mcqs, u2_theory
from build_units_3_to_6_qb import u3_mcqs, u3_theory, u4_mcqs, u4_theory, u5_mcqs, u5_theory, u6_mcqs, u6_theory

print("Writing and escaping all Question Bank units...")

# Clean helper for LaTeX text
def clean_mcqs(mcqs):
    cleaned = []
    for m in mcqs:
        q, a, b, c, d, ans, rat = m
        # clean escapes in strings
        def fix_str(s):
            # replace lone % with \%
            s = s.replace("%", "\\%")
            # replace unescaped underscores
            s = s.replace("INPUT_PULLUP", "\\texttt{INPUT\\_PULLUP}")
            s = s.replace("analogWrite(9, 128)", "\\texttt{analogWrite(9, 128)}")
            s = s.replace("d(0,2,8,10)", "$d(0,2,8,10)$")
            return s
        cleaned.append((fix_str(q), fix_str(a), fix_str(b), fix_str(c), fix_str(d), ans, fix_str(rat)))
    return cleaned

make_clean_unit_tex(1, "Solid State Physics", clean_mcqs(u1_mcqs), u1_theory)
make_clean_unit_tex(2, "Fundamentals of Electricity and Devices", clean_mcqs(u2_mcqs), u2_theory)
make_clean_unit_tex(3, "Introduction to Number System and Logic Gates", clean_mcqs(u3_mcqs), u3_theory)
make_clean_unit_tex(4, "Introduction to Combinational Logic Circuits", clean_mcqs(u4_mcqs), u4_theory)
make_clean_unit_tex(5, "Introduction to Sequential Logic Circuits", clean_mcqs(u5_mcqs), u5_theory)
make_clean_unit_tex(6, "Introduction of Arduino and Sensors", clean_mcqs(u6_mcqs), u6_theory)

print("All 6 Question Bank chapters written cleanly!")
