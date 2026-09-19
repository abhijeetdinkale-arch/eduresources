with open('generate_physics_qb_u3.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'loss at \\textbf{$\\approx 0.15\\text{--}0.18\\text{ dB/km}$ at $1550\\text{ nm}$."""'
replacement = 'loss at \\textbf{$\\approx 0.15\\text{--}0.18\\text{ dB/km}$ at $1550\\text{ nm}$.}"""'

if target in text:
    text = text.replace(target, replacement)
    with open('generate_physics_qb_u3.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully replaced in generate_physics_qb_u3.py")
else:
    print("Target not found!")
