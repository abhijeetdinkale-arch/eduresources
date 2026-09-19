# -*- coding: utf-8 -*-
import re

def fix_ampersands(text):
    # If & is inside \begin{cases} ... \end{cases} or \begin{matrix} ... \end{matrix} or \begin{tabular...} ... \end{tabular...} or \begin{align...} ... \end{align...} or \begin{split} ... \end{split}, keep it as &.
    # If & is in plain text (like \textbf{A & B} or "A & B"), replace with \&.
    # First, restore any \& inside cases:
    text = re.sub(r'(\\begin\{cases\}.*?\\end\{cases\})', lambda m: m.group(1).replace(r'\&', '&'), text, flags=re.DOTALL)
    text = re.sub(r'(\\begin\{aligned\}.*?\\end\{aligned\})', lambda m: m.group(1).replace(r'\&', '&'), text, flags=re.DOTALL)
    text = re.sub(r'(\\begin\{tabularx\}.*?\\end\{tabularx\})', lambda m: m.group(1).replace(r'\&', '&'), text, flags=re.DOTALL)
    text = re.sub(r'(\\begin\{tabular\}.*?\\end\{tabular\})', lambda m: m.group(1).replace(r'\&', '&'), text, flags=re.DOTALL)
    text = re.sub(r'(\\begin\{align\*?\}.*?\\end\{align\*?\})', lambda m: m.group(1).replace(r'\&', '&'), text, flags=re.DOTALL)
    text = re.sub(r'(\\begin\{bmatrix\}.*?\\end\{bmatrix\})', lambda m: m.group(1).replace(r'\&', '&'), text, flags=re.DOTALL)
    text = re.sub(r'(\\begin\{pmatrix\}.*?\\end\{pmatrix\})', lambda m: m.group(1).replace(r'\&', '&'), text, flags=re.DOTALL)
    return text

