# -*- coding: utf-8 -*-
import re

def sanitize_title(title):
    # Remove any unescaped &
    t = re.sub(r'(?<!\\)&', r'\\&', title)
    t = re.sub(r'(?<!\\)%', r'\\%', t)
    # Remove newlines
    t = t.replace('\n', ' ')
    return t

def sanitize_body(body):
    # In prose lines (lines that don't contain tabularx or matrix or align), escape naked &
    lines = body.split('\n')
    sanitized = []
    in_table = False
    in_align = False

    for line in lines:
        if '\\begin{tabular' in line or '\\begin{array' in line or '\\begin{pmatrix' in line or '\\begin{bmatrix' in line or '\\begin{matrix' in line:
            in_table = True
        if '\\begin{align' in line or '\\begin{split' in line:
            in_align = True

        if not in_table and not in_align:
            # Escape & if not already escaped
            line = re.sub(r'(?<!\\)&', r'\\&', line)
            # Escape % if not already escaped (unless comment line, but let's be careful)
            # line = re.sub(r'(?<!\\)%', r'\\%', line)

        if '\\end{tabular' in line or '\\end{array' in line or '\\end{pmatrix' in line or '\\end{bmatrix' in line or '\\end{matrix' in line:
            in_table = False
        if '\\end{align' in line or '\\end{split' in line:
            in_align = False

        sanitized.append(line)

    return '\n'.join(sanitized)

