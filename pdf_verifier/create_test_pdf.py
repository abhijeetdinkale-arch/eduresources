"""
Create a sample test PDF with a mix of correct formulas,
an intentional error, and factual claims — to test the verifier.
"""
from fpdf import FPDF
from fpdf.enums import XPos, YPos

pdf = FPDF()
pdf.set_margins(15, 15, 15)
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 12, "Sample Math & Science Textbook", align="C",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(5)

pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 10, "Chapter 1: Algebra & Trigonometry",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", "", 11)

lines = [
    "The Pythagorean theorem states that a**2 + b**2 = c**2.",
    "For any angle theta, sin(theta)**2 + cos(theta)**2 = 1.",
    "The quadratic formula: x = (-b + sqrt(b**2 - 4*a*c)) / (2*a).",
    "Euler identity: e**(i*pi) + 1 = 0.",
    "The derivative of sin(x) is cos(x).",
    "We define pi = 3.14159265358979.",
    "",
    "INTENTIONAL ERRORS BELOW:",
    "sin(x)**2 + cos(x)**2 = 2",
    "",
    "The area of a circle is A = pi * r**2.",
    "The sum of angles in a triangle is 180 degrees.",
    "E = m * c**2 is Einstein mass-energy equivalence.",
    "The speed of light is approximately 3e8 m/s.",
    "The boiling point of water at sea level is 100 degrees Celsius.",
    "log(a * b) = log(a) + log(b).",
    "e = 2.718281828459045.",
    "sqrt(144) = 12",
    "2 + 2 = 5",
    "The integral of x dx = x**2 / 2 + C.",
]

for line in lines:
    if line == "":
        pdf.ln(4)
    elif line.startswith("INTENTIONAL"):
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(180, 0, 0)
        pdf.cell(0, 7, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "", 11)
    else:
        pdf.multi_cell(180, 7, line)

pdf.output("test_book.pdf")
print("test_book.pdf created!")
