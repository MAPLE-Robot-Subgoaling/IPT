SRC = "../../../data/HW3/"
HW = SRC + "hw3_110.py"

with open(HW) as f:
    src = f.read()
    src_lines = src.split("\n")

print(src)