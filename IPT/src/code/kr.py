'''
Use Python3
'''

from kanren import Relation
from ast_playground import NameLister

def main():

    same_var = Relation()
    var_tracker = {}

    with open("test1.py") as f:

        for num, line in enumerate(f, 1):

            src = line.strip()
            print("[{0: >2}]: {1}".format(num, src))

if __name__ == '__main__':
    main()

#test.py
#goal: output 34


