import logging
import logging.handlers
import os, sys
from thesis import ExtraneousLineFinder
from thesis.errors import GoalNotFoundError

DATA_SRC = "/Users/mneary1/Desktop/IPT/data"
INPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/inputs"
GOALS_SRC = "/Users/mneary1/Desktop/IPT/tests/goals"
OUTPUT_SRC = "/Users/mneary1/Desktop/IPT/tests/outputs/"
LOG_SRC = "/Users/mneary1/Desktop/IPT/logs"

hw = sys.argv[1]
with_execute = bool(int(sys.argv[2])) #cmd line '0' or '1'
with_structure = bool(int(sys.argv[3])) #cmd line '0' or '1'
with_semantic = bool(int(sys.argv[4])) #cmd line '0' or '1'

assignments = [os.path.join(DATA_SRC, hw, file) for file in os.listdir(os.path.join(DATA_SRC, hw))]
num_inputs = len(os.listdir(os.path.join(INPUT_SRC, hw)))
inputs = [os.path.join(INPUT_SRC, hw, "input{}.txt").format(i) for i in range(1, num_inputs + 1)]
goals = [os.path.join(GOALS_SRC, hw, "goal{}.txt").format(i) for i in range(1, num_inputs + 1)]
output_path = os.path.join(OUTPUT_SRC, hw)
io = dict(zip(inputs, goals))
successful_runs = 0

#set up logging
logfilename = "experiment_all.log"
logger = logging.getLogger("experiment")
logger.setLevel(logging.DEBUG)
fh = logging.handlers.RotatingFileHandler(os.path.join(LOG_SRC, logfilename), mode='w', backupCount=5)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

should_roll_over = os.path.isfile(logfilename)
if should_roll_over:  # log already exists, roll over!
    fh.doRollover()

for assignment in assignments:
    logger.info("Assignment: {}".format(assignment))
    try:
        with ExtraneousLineFinder(assignment, io, output_path, with_execute, with_structure, with_semantic) as finder:
            try:
                ex = finder.run()
                successful_runs += 1
            except GoalNotFoundError as g:
                logger.warn(g)
            except Exception as e:
                logger.exception(e)
    except Exception as e:
        logger.exception(e)

logger.info("Successful runs: {}/{}".format(successful_runs, len(assignments)))

