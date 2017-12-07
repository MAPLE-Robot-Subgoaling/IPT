import os
from thesis import ExtraneousLineFinder

DATA_SRC = "/Users/mneary1/Desktop/IPT/data"
INPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/inputs"
GOALS_SRC = "/Users/mneary1/Desktop/IPT/tests/goals"
OUTPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/outputs/"

hw = "HW5"
assignment = "hw5_001.py"
num_inputs = len(os.listdir(os.path.join(INPUT_SRC, hw)))

file = os.path.join(DATA_SRC, hw, assignment)
inputs = [os.path.join(INPUT_SRC, hw, "input{}.txt").format(i) for i in range(1, num_inputs + 1)]
goals = [os.path.join(GOALS_SRC, hw, "goal{}.txt").format(i) for i in range(1, num_inputs + 1)]
output_path = os.path.join(OUTPUT_SRC, hw)
io = dict(zip(inputs, goals))

with ExtraneousLineFinder(file, io, output_path, False, True, True) as finder:
    ex = finder.extraneous_lines
    print(ex)

