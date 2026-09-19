import re
import glob

for p in glob.glob("Physics_Question_Bank/chapters/*.tex"):
    with open(p, "r") as f:
        text = f.read()
    text = re.sub(r'#(\d+)', r'No. \1', text)
    with open(p, "w") as f:
        f.write(text)

print("Hash signs replaced in QB.")
