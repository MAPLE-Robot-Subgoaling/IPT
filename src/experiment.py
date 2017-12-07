import os, sys
from thesis import ExtraneousLineFinder
from thesis.errors import GoalNotFoundError

DATA_SRC = "/Users/mneary1/Desktop/IPT/data"
INPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/inputs"
GOALS_SRC = "/Users/mneary1/Desktop/IPT/tests/goals"
OUTPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/outputs/"

hw = sys.argv[1]
with_execute = sys.argv[2]
with_structure = sys.argv[3]
with_semantic = sys.argv[4]

assignments = [os.path.join(DATA_SRC, hw, file) for file in os.listdir(os.path.join(DATA_SRC, hw))]
num_inputs = len(os.listdir(os.path.join(INPUT_SRC, hw)))
inputs = [os.path.join(INPUT_SRC, hw, "input{}.txt").format(i) for i in range(1, num_inputs + 1)]
goals = [os.path.join(GOALS_SRC, hw, "goal{}.txt").format(i) for i in range(1, num_inputs + 1)]
output_path = os.path.join(OUTPUT_SRC, hw)
io = dict(zip(inputs, goals))

for assignment in assignments:
    with ExtraneousLineFinder(assignment, io, output_path, with_execute, with_structure, with_semantic) as finder:
        try:
            ex = finder.run()
        except Exception as e:
            print("[!] Something with wrong for assignment {}".format(assignment))
            print("\t[+] {}".format(e))

