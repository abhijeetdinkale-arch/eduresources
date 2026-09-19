with open('generate_physics_qb_u2.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace \begin{table}[htbp] \centering \begin{tabular}{lll} ... \end{tabular} \end{table} with tabularx
text = text.replace(r'\begin{table}[htbp]' + '\n' + r'\centering' + '\n' + r'\begin{tabular}{lll}', r'\begin{center}' + '\n' + r'\begin{tabularx}{\linewidth}{|l|X|X|}' + '\n' + r'\hline')
text = text.replace(r'\bottomrule' + '\n' + r'\end{tabular}' + '\n' + r'\end{table}', r'\hline' + '\n' + r'\end{tabularx}' + '\n' + r'\end{center}')
text = text.replace(r'\toprule', r'')
text = text.replace(r'\midrule', r'\hline')

with open('generate_physics_qb_u2.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated generate_physics_qb_u2.py to use tabularx inside center instead of table floats.")
