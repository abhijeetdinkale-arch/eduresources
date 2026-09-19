# -*- coding: utf-8 -*-
import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix in style.sty hyperref
    content = content.replace("Design & Practice", "Design and Practice")
    content = content.replace("Study & Practice", "Study and Practice")

    # In section/subsection/chapter titles, replace unescaped & with \&
    def rep_title(match):
        text = match.group(0)
        # replace unescaped & with \&
        fixed = re.sub(r'(?<!\\)&', r'\&', text)
        return fixed

    content = re.sub(r'\\(chapter|section|subsection|subsubsection|title|titleformat|fancyhead|fancyfoot)(\[[^\]]*\])?\{[^\}]*\}', rep_title, content)
    
    # Specific known instances
    content = content.replace(r'\subsection{User Personas & Target Archetypes}', r'\subsection{User Personas \& Target Archetypes}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk('INT335'):
    for f in files:
        if f.endswith('.tex') or f.endswith('.sty'):
            fix_file(os.path.join(root, f))

print("Fixed unescaped ampersands.")
