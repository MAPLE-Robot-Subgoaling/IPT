from handlers import *

from kanren import Relation, facts, run, var, conde
from itertools import combinations

import ast


filename = "test.py"
has_id = Relation()
is_before = Relation()
assigns = Relation()
uses = Relation()


def depends(a, b):
    """there is a dependency between two lines {A, B} if:
    they share an ID X AND
    A comes before B AND
    X is a target for the assignment on line A AND
    B uses X (not just an assignment where X is a target"""
    shared_id = var()
    return conde([is_before(a, b), assigns(a, shared_id), uses(b, shared_id)])


def main():
    with open(filename) as f:
        src = f.readlines()

    facts(is_before, *combinations(range(len(src)), 2))

    print("The input program is:")
    for lineno, line in enumerate(src):

        if line == "\n":
            print("Empty line")
            continue

        outstr = "[{0: >2}]: {1}".format(lineno, line.strip())
        print(outstr)
        astsrc = ast.parse(line)
        line_type = astsrc.body[0]

        if isinstance(line_type, ast.Assign):
            v = AssignVisitor()
            v.visit(astsrc)
            left, right = v.get_results()

            if left:
                facts(assigns, (lineno, left))

            if right:
                facts(uses, *[(lineno, name) for name in right])

        elif isinstance(line_type, ast.Expr):
            v = ExprVisitor()
            v.visit(astsrc)
            vs = v.get_vars_used()
            if vs:
                facts(uses, *[(lineno, name) for name in vs])


    print()
    a, b = var(), var()
    results = run(0, (a, b), depends(a, b))

    print("The lines that have dependencies are:")
    print(results)

    graph = {}
    for result in results:

if __name__ == "__main__":
    main()
