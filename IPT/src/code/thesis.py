from ast_playground import NameLister
import os, ast

DIR = "../../data/HW4"
FILES = os.listdir(DIR)


def run_file(file_name):
    cmd = "python3 " + file_name
    try:
        os.system(cmd)
    except:
        print("Failure")

run_file(os.path.join(DIR,"hw4_122.py"))