# -*- coding: utf-8 -*-
import os

for root, dirs, files in os.walk('INT335'):
    for f in files:
        if f.endswith('.tex') or f.endswith('.sty'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as file:
                content = file.read()
            content = content.replace("₹", "Rs.~")
            # Replace math shift in subsection titles if any
            content = content.replace(r"\subsection{The Impact--Effort 2$\times$2 Grid}", r"\subsection{The Impact--Effort 2x2 Grid}")
            with open(p, 'w', encoding='utf-8') as file:
                file.write(content)

print("Unicode characters fixed.")
