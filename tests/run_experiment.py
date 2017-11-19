import os
import importlib
import thesis.new_new_thesis
from thesis.config import *

#RESULTS = "/Users/mneary1/Desktop/IPT/data/results_hw3/all.txt"
from thesis.config import GOALS_SRC

RESULTS = "/Users/mneary1/Desktop/IPT/results/HW5/nodata.txt"

#HW_NAME = "HW3"
HW_NAME = "HW5"

path_to_goals = os.path.join(GOALS_SRC, HW_NAME)
path_to_inputs = os.path.join(INPUT_SRC, HW_NAME)
path_to_outputs = os.path.join(OUTPUT_DEST, HW_NAME)
path_to_programs = os.path.join(DATA_SRC, HW_NAME)

inputs = [os.path.join(path_to_inputs, x) for x in os.listdir(path_to_inputs)]
goals = os.path.join(path_to_goals, "goals.txt")
resultsfile = open(RESULTS, 'w')

print(HW_NAME + " here we go...")
for hw in os.listdir(path_to_programs):
    path_to_hw = os.path.join(path_to_programs, hw)

    try:
        results, _ = new_new_thesis.run_thesis(path_to_hw, inputs, goals, output_dir=path_to_outputs)
        if results == -1:
            resultsfile.write(str(hw) + ":ERROR\n")
        elif len(results) != 0:
            resultsfile.write(str(hw) + ":" + str(results) + ",\n")
        else:
            resultsfile.write(str(hw) + ":XXXXX\n")

    except Exception as e:
        resultsfile.write(str(hw) + ":ERROR\n")

    # need to reload the module so variables and stuff are redone
    importlib.reload(new_new_thesis)
resultsfile.close()

