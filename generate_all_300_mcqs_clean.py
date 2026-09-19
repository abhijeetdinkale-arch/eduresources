import os
import re

def escape_latex(s):
    # If text is already formatted as latex math or command, be careful.
    # Replace bare % with \%
    s = re.sub(r'(?<!\\)%', r'\%', s)
    # Replace bare $ with \$ if not intended for math
    # Replace bare & with \&
    s = re.sub(r'(?<!\\)&', r'\&', s)
    # Replace bare _ with \_
    s = re.sub(r'(?<!\\)_', r'\_', s)
    # Replace bare ^ with \^{}
    s = re.sub(r'(?<!\\)\^', r'\^{}', s)
    # Replace < and >
    s = s.replace('<', '$<$').replace('>', '$>$')
    return s

def create_mcq(num, level, q_text, opt_a, opt_b, opt_c, opt_d):
    q_text = escape_latex(q_text)
    opt_a = escape_latex(opt_a)
    opt_b = escape_latex(opt_b)
    opt_c = escape_latex(opt_c)
    opt_d = escape_latex(opt_d)
    return f"\\mcqitem{{{num}}}{{[{level}] {q_text}}}{{{opt_a}}}{{{opt_b}}}{{{opt_c}}}{{{opt_d}}}\n"

def build_unit_latex(unit_num, title, easy_q, med_q, hard_q, theory_q, code_q):
    content = f"\\chapter{{Unit {unit_num}: {title}}}\n\n"
    content += "\\section{Section 1: 50 Chapter-Wise Multiple-Choice Questions (MCQs)}\n\n"
    content += "\\subsection*{Part I: Foundational Level (Questions 1 to 25 --- 50\\% Easy)}\n"

    q_idx = 1
    ans_key = []

    for item in easy_q:
        content += create_mcq(q_idx, "Easy", item[0], item[1], item[2], item[3], item[4])
        ans_key.append((q_idx, item[5], escape_latex(item[6])))
        q_idx += 1

    content += "\n\\subsection*{Part II: Intermediate Analytical Level (Questions 26 to 40 --- 30\\% Medium)}\n"
    for item in med_q:
        content += create_mcq(q_idx, "Medium", item[0], item[1], item[2], item[3], item[4])
        ans_key.append((q_idx, item[5], escape_latex(item[6])))
        q_idx += 1

    content += "\n\\subsection*{Part III: Advanced Mastery Level (Questions 41 to 50 --- 20\\% Hard)}\n"
    for item in hard_q:
        content += create_mcq(q_idx, "Hard", item[0], item[1], item[2], item[3], item[4])
        ans_key.append((q_idx, item[5], escape_latex(item[6])))
        q_idx += 1

    content += r"""
\newpage
\section{Section 2: Complete Answer Key \& Explanations}

\begin{answerkeytable}{Unit """ + str(unit_num) + r""": 50 Questions Answer Key}
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(25):
        q1 = ans_key[i]
        q2 = ans_key[i+25]
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{answerkeytable}

\section{Section 3: Conceptual Theory \& Coding Questions}
"""
    content += theory_q + "\n" + code_q + "\n"
    return content

# Read datasets from previous script or definitions
# Let's import the data from generate_units_2_to_6.py and build_full_300_mcqs.py
import build_full_300_mcqs
import generate_units_2_to_6

# Unit 1
u1_easy = build_full_300_mcqs.easy_q if hasattr(build_full_300_mcqs, 'easy_q') else []
