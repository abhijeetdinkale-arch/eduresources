# -*- coding: utf-8 -*-
import re

with open("INT335/chapters/chapter-03-ideation-and-creative-problem-solving.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace \begin{table}[h!] and \end{table} inside the example box
text = text.replace(r"\begin{table}[h!]", r"\begin{center}")
text = text.replace(r"\caption{Weighted Matrix Evaluation indicating Concept B as the top candidate.}", r"{\small\textbf{Table 3.1:} Weighted Matrix Evaluation indicating Concept B as the top candidate.}")
text = text.replace(r"\end{table}", r"\end{center}")

with open("INT335/chapters/chapter-03-ideation-and-creative-problem-solving.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed table in ch3")
