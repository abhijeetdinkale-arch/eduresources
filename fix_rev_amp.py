# -*- coding: utf-8 -*-
import os

for root, dirs, files in os.walk('INT335_Revision_Book'):
    for f in files:
        if f.endswith('.tex') or f.endswith('.sty'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace("Formula & PDCA", "Formula \\& PDCA")
            content = content.replace("Prioritization & Pivots", "Prioritization \\& Pivots")
            content = content.replace("Mapping & POV", "Mapping, POV")
            content = content.replace("Screening & Prioritization", "Screening \\& Prioritization")
            content = content.replace("Conventions & User", "Conventions \\& User")
            content = content.replace("Conduct & Feedback", "Conduct \\& Feedback")
            with open(p, 'w', encoding='utf-8') as file:
                file.write(content)

print("Fixed ampersands in revision book.")
