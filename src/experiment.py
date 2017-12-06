import os
from thesis import ExtraneousLineFinder

DATA_SRC  = "/Users/mneary1/Desktop/IPT/data"
INPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/inputs"
GOALS_SRC = "/Users/mneary1/Desktop/IPT/tests/goals"
OUTPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/outputs/"

hw = "HW3"
assignment = "hw3_001.py"
num_inputs = 6

file = os.path.join(DATA_SRC, hw, assignment)
inputs = [os.path.join(INPUT_SRC, hw, "input{}.txt").format(i) for i in range(1, num_inputs + 1)]
goals = os.path.join(GOALS_SRC, hw, "goals.txt")
output_path = os.path.join(OUTPUT_SRC, hw)

with ExtraneousLineFinder(file, inputs, goals, output_path, False, True, True) as finder:
    print("In context")
