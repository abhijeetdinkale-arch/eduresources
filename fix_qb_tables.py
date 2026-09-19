import re
import glob

for p in glob.glob("Physics_Question_Bank/chapters/*.tex"):
    with open(p, "r") as f:
        text = f.read()
    text = text.replace(r"\textbf{Q#}", r"\textbf{Q\#}")
    with open(p, "w") as f:
        f.write(text)

with open("Physics_Question_Bank/qb_style.sty", "r") as f:
    text = f.read()
text = text.replace(r"headheight=22pt", r"headheight=25pt")
with open("Physics_Question_Bank/qb_style.sty", "w") as f:
    f.write(text)

print("Q# fixed in QB tables and headheight updated.")
