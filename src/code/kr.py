'''
Use Python3
'''

from kanren import Relation, facts, run, var
import ast
from visitor import Visitor
from pretty_dump import dump
from itertools import combinations

def main():

    hasID = Relation()

    #should this be a Relation?
    dependent = Relation()
    some_var = var()

    var_tracker = {}

    with open("test.py") as f:

        for num, line in enumerate(f, 1):
            v = Visitor()
            src = line.strip()
            ast_src = ast.parse(src)
            print("[{0: >2}]: {1}".format(num, src))
            #print(dump(ast_src))
            #print()
            v.visit(ast_src)
            for id in v.get_result():
                try:
                    var_tracker[id].append(num)
                except:
                    var_tracker[id] = [num]


    print(var_tracker)

    for id in var_tracker:
        l = list(combinations(var_tracker[id], 2))
        for lineno in var_tracker[id]:
            facts(hasID, (lineno, id))

        for item in l:
            facts(sharesID, item)

    x = var()
    print(run(0, x, sharesID(x, 4)))
    print(run(0, x, hasID(x,"var2")))

if __name__ == '__main__':
    main()

#test.py
#goal: output 34


