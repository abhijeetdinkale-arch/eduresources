# -*- coding: utf-8 -*-
import re

# Questions for each unit
# We will parse the markdown files in INT335_Question_Bank/UnitX_MCQs.md or write directly as LaTeX!

def parse_markdown_mcqs(unit_num):
    filepath = f"INT335_Question_Bank/Unit{unit_num}_MCQs.md"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title
    title_match = re.search(r"## Unit \d+: (.*?) \(30 MCQs\)", content)
    title = title_match.group(1) if title_match else f"Unit {unit_num}"

    # Extract Questions
    q_blocks = re.findall(r"\*\*Q(\d+)\.\s*(.*?)\*\*\n+A\)\s*(.*?)\n+B\)\s*(.*?)\n+C\)\s*(.*?)\n+D\)\s*(.*?)\n+", content)

    # Extract Answer table
    table_rows = re.findall(r"\|\s*\*\*Q(\d+)\*\*\s*\|\s*\*\*([A-D])\*\*\s*\|\s*(.*?)\s*\|", content)

    # Build LaTeX
    tex = f"\\chapter{{Unit {unit_num}: {title}}}\n\\label{{chap:unit{unit_num}_qb}}\n\n"
    tex += f"\\section*{{Practice Question Set (30 MCQs)}}\n\\addcontentsline{{toc}}{{section}}{{Practice Question Set (30 MCQs)}}\n\n"

    for qnum, qtext, optA, optB, optC, optD in q_blocks:
        # Clean text for LaTeX
        qtext = qtext.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("₹", "Rs.~")
        optA = optA.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("₹", "Rs.~")
        optB = optB.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("₹", "Rs.~")
        optC = optC.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("₹", "Rs.~")
        optD = optD.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("₹", "Rs.~")
        tex += f"\\mcqitem{{{qnum}}}{{{qtext}}}{{{optA}}}{{{optB}}}{{{optC}}}{{{optD}}}\n\n"

    # Quick Answer Key Table
    tex += f"\n\\newpage\n\\section*{{Answer Key \\& Step-by-Step Explanations}}\n\\addcontentsline{{toc}}{{section}}{{Answer Key \\& Explanations}}\n\n"
    tex += f"\\begin{{answerkeytable}}{{Unit {unit_num}: Quick Answer Key}}\n"
    tex += "\\begin{tabular}{c c c c c c c c c c}\n\\toprule\n"
    
    # 3 rows of 10
    for r in range(3):
        headers = [f"\\textbf{{Q{r*10 + i + 1}}}" for i in range(10)]
        keys = []
        for i in range(10):
            idx = r*10 + i
            if idx < len(table_rows):
                keys.append(f"\\textbf{{{table_rows[idx][1]}}}")
            else:
                keys.append("-")
        tex += " & ".join(headers) + " \\\\\n"
        tex += " & ".join(keys) + " \\\\\n"
        if r < 2:
            tex += "\\midrule\n"
    tex += "\\bottomrule\n\\end{tabular}\n\\end{answerkeytable}\n\n"

    # Detailed Explanations
    tex += "\\begin{expbox}[Detailed Pedagogical Explanations]\n\\begin{enumerate}[leftmargin=6mm, itemsep=2.5mm]\n"
    for qnum, ans, exp in table_rows:
        exp = exp.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("₹", "Rs.~")
        tex += f"  \\item \\textbf{{[Q{qnum}: Option {ans}]}} {exp}\n"
    tex += "\\end{enumerate}\n\\end{expbox}\n"

    return tex

for u in range(1, 7):
    tex_content = parse_markdown_mcqs(u)
    with open(f"INT335_Question_Bank/chapters/unit{u}_mcqs.tex", "w", encoding="utf-8") as f:
        f.write(tex_content)
    print(f"Generated unit{u}_mcqs.tex")

print("All Question Bank chapter tex files created.")
