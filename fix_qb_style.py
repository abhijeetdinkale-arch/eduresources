with open("MTH165_Question_Bank/qb_style.sty", "r") as f:
    text = f.read()

# Replace colback=rgb,255:red,255;green,248;blue,230 with defined color
text = text.replace(r"\definecolor{AlertRed}{RGB}{200, 30, 30}", "\\definecolor{AlertRed}{RGB}{200, 30, 30}\n\\definecolor{TipBg}{RGB}{255, 248, 230}")
text = text.replace(r"colback=rgb,255:red,255;green,248;blue,230,", "colback=TipBg,")

with open("MTH165_Question_Bank/qb_style.sty", "w") as f:
    f.write(text)

print("qb_style.sty fixed.")
