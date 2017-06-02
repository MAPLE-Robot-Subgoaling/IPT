from visitor import Visitor
from kanren import Relation, facts, run, var, conde
from itertools import combinations
import ast


filename = "test.py"

#src_ast = ast.parse(src)
#Visitor().visit(src_ast)


def main():

    with open(filename) as f:
        src = f.readlines()

    hasID = Relation()
    isBefore = Relation()

    facts(isBefore, *combinations(range(len(src)), 2))

    for lineno, line in enumerate(src):
        outstr = "[{0: >2}]: {1}".format(lineno, line.strip())
        print(outstr)
        astsrc = ast.parse(line)
        v = Visitor()
        v.visit(astsrc)
        results = v.get_result()
        facts(hasID, *[(lineno, name) for name in results])

    a, b = var(), var()
    print(run(0, (a, b), hasID(a, b)))
    print(run(0, (a, b), isBefore(a, b)))

if __name__ == "__main__":
    main()