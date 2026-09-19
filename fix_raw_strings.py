import re
import glob

for p in glob.glob("Physics_Question_Bank/chapters/*.tex"):
    with open(p, "r") as f:
        text = f.read()
    # fix control characters
    text = text.replace('\x0b', r'\v')
    text = text.replace('\x0c', r'\f')
    text = text.replace('\x07', r'\a')
    # ensure proper latex
    text = text.replace(r'abla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0', r'\nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0')
    text = text.replace(r'\approx', r'\approx')
    with open(p, "w") as f:
        f.write(text)

print("Control characters fixed.")
