# -*- coding: utf-8 -*-
"""
Master Orchestrator for PHY110 Engineering Physics Master Question Bank:
Generates 100% authentic, comprehensive, and unique chapters for all 6 units:
- Unit 1: Electromagnetic Theory and Vector Calculus
- Unit 2: Lasers and Optical Applications
- Unit 3: Fiber Optics and Waveguides
- Unit 4: Quantum Mechanics and Wave-Particle Duality
- Unit 5: Semiconductor Physics and Solid State Devices
- Unit 6: Engineering Materials (Dielectrics, Magnetism, Superconductivity & Nanotech)

Total Output: 600 unique MCQs + 120 detailed theory questions with derivations.
"""

import os
import re

import generate_physics_qb_u1
import generate_physics_qb_u2
import generate_physics_qb_u3
import generate_physics_qb_u4
import generate_physics_qb_u5
import generate_physics_qb_u6

import append_u4_theory
import append_u5_theory

CHAPTERS_META = [
    {
        "unit_num": 1,
        "title": "Unit 1: Electromagnetic Theory and Vector Calculus",
        "file_name": "chapter-01-electromagnetic-theory-qb.tex",
        "getter": generate_physics_qb_u1.get_unit_1_content
    },
    {
        "unit_num": 2,
        "title": "Unit 2: Lasers and Optical Applications",
        "file_name": "chapter-02-lasers-qb.tex",
        "getter": generate_physics_qb_u2.get_unit_2_content
    },
    {
        "unit_num": 3,
        "title": "Unit 3: Fiber Optics and Waveguides",
        "file_name": "chapter-03-fiber-optics-qb.tex",
        "getter": generate_physics_qb_u3.get_unit_3_content
    },
    {
        "unit_num": 4,
        "title": "Unit 4: Quantum Mechanics and Wave-Particle Duality",
        "file_name": "chapter-04-quantum-mechanics-qb.tex",
        "getter": generate_physics_qb_u4.get_unit_4_content
    },
    {
        "unit_num": 5,
        "title": "Unit 5: Semiconductor Physics and Solid State Devices",
        "file_name": "chapter-05-semiconductor-physics-qb.tex",
        "getter": generate_physics_qb_u5.get_unit_5_content
    },
    {
        "unit_num": 6,
        "title": "Unit 6: Engineering Materials (Dielectrics, Magnetism, Superconductivity \\& Nanomaterials)",
        "file_name": "chapter-06-engineering-materials-qb.tex",
        "getter": generate_physics_qb_u6.get_unit_6_content
    }
]

def clean_ans_letter(ans_str):
    """Normalize answer string to (a), (b), (c), or (d)."""
    ans_str = str(ans_str).strip()
    match = re.search(r'([a-dA-D])', ans_str)
    if match:
        return f"({match.group(1).lower()})"
    return f"({ans_str})"

def balance_environments(text):
    """Ensure all itemize, enumerate, and other list environments are closed."""
    diff_item = text.count(r'\begin{itemize}') - text.count(r'\end{itemize}')
    diff_enum = text.count(r'\begin{enumerate}') - text.count(r'\end{enumerate}')
    
    additions = []
    if diff_item > 0:
        additions.append('\n' + ('\\end{itemize}\n' * diff_item))
    if diff_enum > 0:
        additions.append('\n' + ('\\end{enumerate}\n' * diff_enum))
        
    return text + ''.join(additions)

def sanitize_text(text):
    """Clean unescaped text ampersands in headings / descriptions while preserving math."""
    lines = text.split('\n')
    sanitized = []
    in_math_align = False

    for line in lines:
        if any(tok in line for tok in ['\\begin{cases}', '\\begin{aligned}', '\\begin{align}', '\\begin{align*}', '\\begin{matrix}', '\\begin{bmatrix}', '\\begin{pmatrix}', '\\begin{tabular', '\\begin{tabularx}']):
            in_math_align = True
        
        if not in_math_align:
            # Escape & in prose (like "A & B" -> "A \& B")
            line = re.sub(r'(?<!\\)&', r'\\&', line)

        if any(tok in line for tok in ['\\end{cases}', '\\end{aligned}', '\\end{align}', '\\end{align*}', '\\end{matrix}', '\\end{bmatrix}', '\\end{pmatrix}', '\\end{tabular}', '\\end{tabularx}']):
            in_math_align = False

        sanitized.append(line)
    
    res = '\n'.join(sanitized)
    return balance_environments(res)

def format_chapter(unit_info):
    unit_num = unit_info["unit_num"]
    title = unit_info["title"]
    res = unit_info["getter"]()

    if len(res) == 4:
        _, _, raw_mcqs, raw_theory = res
    else:
        raw_mcqs, raw_theory = res

    # Append additional theory questions if needed for U4 and U5
    if unit_num == 4 and len(raw_theory) == 10:
        raw_theory = raw_theory + append_u4_theory.additional_tqs
    elif unit_num == 5 and len(raw_theory) == 10:
        raw_theory = raw_theory + append_u5_theory.additional_tqs_u5

    # Normalize MCQs: list of dicts with keys: num, text, a, b, c, d, ans, rationale
    normalized_mcqs = []
    for idx, item in enumerate(raw_mcqs):
        q_num = idx + 1
        if len(item) == 8:
            _, q_text, opt_a, opt_b, opt_c, opt_d, ans, rationale = item
        elif len(item) == 7:
            q_text, opt_a, opt_b, opt_c, opt_d, ans, rationale = item
        else:
            raise ValueError(f"Unknown MCQ format in unit {unit_num} item {idx}: {item}")
        
        # In rationale, make sure any literal & is escaped as \&
        clean_rat = re.sub(r'(?<!\\)&', r'\\&', str(rationale).strip())

        normalized_mcqs.append({
            "num": q_num,
            "text": sanitize_text(str(q_text).strip()),
            "a": sanitize_text(str(opt_a).strip()),
            "b": sanitize_text(str(opt_b).strip()),
            "c": sanitize_text(str(opt_c).strip()),
            "d": sanitize_text(str(opt_d).strip()),
            "ans": clean_ans_letter(ans),
            "rationale": clean_rat
        })

    # Normalize Theory: list of dicts with keys: num, question, solution
    normalized_theory = []
    for idx, item in enumerate(raw_theory):
        t_num = idx + 1
        if isinstance(item, dict):
            t_q = item.get("question", "")
            t_sol = item.get("solution", "")
        elif isinstance(item, (list, tuple)):
            t_q = item[0]
            t_sol = item[1]
        else:
            raise ValueError(f"Unknown theory format in unit {unit_num} item {idx}")

        normalized_theory.append({
            "num": t_num,
            "question": sanitize_text(str(t_q).strip()),
            "solution": sanitize_text(str(t_sol).strip())
        })

    # Build LaTeX Document
    lines = []
    lines.append(f"\\chapter{{{title}}}\n")
    lines.append("\\section{Section 1: 100 Chapter-Wise Multiple-Choice Questions (MCQs)}\n")

    # Part I: Foundational (Q1-Q50)
    lines.append("\\subsection*{Part I: Foundational Level (Questions 1 to 50)}\n")
    for q in normalized_mcqs[:50]:
        lines.append(f"\\mcqitem{{{q['num']}}}{{{q['text']}}}{{{q['a']}}}{{{q['b']}}}{{{q['c']}}}{{{q['d']}}}")

    # Part II: Intermediate (Q51-Q80)
    lines.append("\n\\subsection*{Part II: Intermediate Analytical Level (Questions 51 to 80)}\n")
    for q in normalized_mcqs[50:80]:
        lines.append(f"\\mcqitem{{{q['num']}}}{{{q['text']}}}{{{q['a']}}}{{{q['b']}}}{{{q['c']}}}{{{q['d']}}}")

    # Part III: Advanced (Q81-Q100)
    lines.append("\n\\subsection*{Part III: Advanced \\& Numerical Problems (Questions 81 to 100)}\n")
    for q in normalized_mcqs[80:]:
        lines.append(f"\\mcqitem{{{q['num']}}}{{{q['text']}}}{{{q['a']}}}{{{q['b']}}}{{{q['c']}}}{{{q['d']}}}")

    # Section 2: Complete Answer Key (Divided into 4 clean 25-row tables for perfect page fitting)
    lines.append("\n\\newpage\n\\section{Section 2: Complete Answer Key with Detailed Rationales}\n")
    
    ranges = [(0, 25, "1 to 25"), (25, 50, "26 to 50"), (50, 75, "51 to 75"), (75, 100, "76 to 100")]
    for start_idx, end_idx, label in ranges:
        lines.append(f"\\subsection*{{Master Answer Key (Questions {label})}}\n")
        lines.append("{\\small")
        lines.append("\\noindent\\begin{tabularx}{\\textwidth}{|c|c|X|}")
        lines.append("\\hline")
        lines.append("\\textbf{Q\\#} & \\textbf{Ans} & \\textbf{Technical Rationale \\& Calculation} \\\\")
        lines.append("\\hline")
        for q in normalized_mcqs[start_idx:end_idx]:
            lines.append(f"\\textbf{{{q['num']}}} & \\textbf{{{q['ans']}}} & {q['rationale']} \\\\ \\hline")
        lines.append("\\end{tabularx}")
        lines.append("}\n")
        if end_idx < 100:
            lines.append("\\newpage\n")

    # Section 3: Theory Questions and Derivations
    lines.append("\n\\newpage\n\\section{Section 3: 20 Comprehensive Theory Questions with Analytical Derivations}\n")
    for tq in normalized_theory:
        lines.append(f"\\begin{{theoryq}}{{{tq['num']}}}")
        lines.append(f"{tq['question']}")
        lines.append("\\end{theoryq}")
        lines.append("\\begin{theorysol}")
        lines.append(f"{tq['solution']}")
        lines.append("\\end{theorysol}")
        lines.append("\\vspace{4mm}\n")

    return "\n".join(lines), len(normalized_mcqs), len(normalized_theory)

def main():
    chapters_dir = "/Users/abhidinkale/Documents/mark p1/Physics_Question_Bank/chapters"
    os.makedirs(chapters_dir, exist_ok=True)

    total_mcqs = 0
    total_theory = 0

    for ch in CHAPTERS_META:
        file_path = os.path.join(chapters_dir, ch["file_name"])
        content, n_mcqs, n_theory = format_chapter(ch)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        total_mcqs += n_mcqs
        total_theory += n_theory
        print(f"Generated {ch['file_name']}: {n_mcqs} MCQs, {n_theory} Theory Questions.")

    print(f"\n==========================================")
    print(f"SUCCESS: Generated {total_mcqs} unique MCQs and {total_theory} Theory Questions across 6 Units!")
    print(f"==========================================")

if __name__ == '__main__':
    main()
