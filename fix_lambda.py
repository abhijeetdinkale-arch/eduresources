import os
import subprocess

print("Fixing lambda in Question Bank Unit 6...")

with open("generate_complete_phy175_qb_all.py", "r") as f:
    code = f.read()

# Replace (\\\\lambda with ($\\lambda
code = code.replace(r"(\\\\lambda \approx 700", r"($\lambda \approx 700")
code = code.replace(r"(\\lambda \approx 700", r"($\lambda \approx 700")

with open("generate_complete_phy175_qb_all.py", "w") as f:
    f.write(code)

print("Updated.")
