import logging
import logging.handlers
import os
import sys
from thesis import ExtraneousLineFinder
from thesis.errors import GoalNotFoundError, TraceError

def fmt_type(type, flag):
    return "[X] " + type if flag else "[ ] " + type

DATA_SRC   = "/Users/mneary1/Desktop/IPT/data"
INPUT_SRC  = "/Users/mneary1/Desktop/IPT/tests/inputs"
GOALS_SRC  = "/Users/mneary1/Desktop/IPT/tests/goals"
OUTPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/outputs/"
RESULT_SRC = "/Users/mneary1/Desktop/IPT/results/"
LOG_SRC = "/Users/mneary1/Desktop/IPT/logs"

file = "hw3_294.py" # of the form: hwx_###.py

with_execute = not True
with_structure = True
with_semantic = True

hw = file[:3].upper()
num_inputs = len(os.listdir(os.path.join(INPUT_SRC, hw)))
inputs = [os.path.join(INPUT_SRC, hw, "input{}.txt").format(i) for i in range(1, num_inputs + 1)]
goals = [os.path.join(GOALS_SRC, hw, "goal{}.txt").format(i) for i in range(1, num_inputs + 1)]
output_path = os.path.join(OUTPUT_SRC, hw)
io = dict(zip(inputs, goals))

assignment = os.path.join(DATA_SRC, hw, file)
print("Testing {} with:".format(file))
print(fmt_type("execution", with_execute))
print(fmt_type("semantic", with_semantic))
print(fmt_type("structure", with_structure))
print()

#set up logging
logfilename = "experiment.log"
logger = logging.getLogger("experiment")
logger.setLevel(logging.DEBUG)
fh = logging.handlers.RotatingFileHandler(os.path.join(LOG_SRC, logfilename), mode='w', backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

should_roll_over = os.path.isfile(logfilename)
if should_roll_over:  # log already exists, roll over!
    fh.doRollover()

try:
    with ExtraneousLineFinder(assignment, io, output_path, with_execute, with_structure, with_semantic) as finder:
        try:
            ex = finder.run()
            logger.info("Extraneous Lines for file {}: {}".format(file, str(ex)))
        except TraceError as t:
            logger.warn(t)
        except GoalNotFoundError as g:
            logger.warn(g)
        except Exception as e:
            logger.debug("{}".format(e))

except Exception as e:
    logger.exception(e)

