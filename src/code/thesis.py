from handlers import *

from kanren import Relation, facts, run, var, conde, eq
from itertools import combinations

import ast
import networkx as nx
import subprocess

filename = "test.py"
has_id = Relation()
is_before = Relation()
assigns = Relation()
uses = Relation()
hasOutput = Relation()  # line L has output of value V


def depends(a, b):
    """there is a dependency between two lines {A, B} if:
    they share an ID X AND
    A comes before B AND
    X is a target for the assignment on line A AND
    B uses X (not just an assignment where X is a target"""
    shared_id = var()
    return conde([is_before(a, b), assigns(a, shared_id), uses(b, shared_id)])


def run_code(name):
    p = subprocess.Popen("python3 " + name, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    out_str = out.decode("utf-8")
    return out_str.strip()


def main():
    with open(filename) as f:
        src = f.readlines()

    # run the student's code to get their output
    code_result = run_code(filename)

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
            out = v.isOut()
            if vs:
                facts(uses, *[(lineno, name) for name in vs])

            # add output as a fact
            # this will need to be fixed for programs with >1 print statement
            if out:
                facts(hasOutput, (lineno, code_result))


    print()
    print("Solution result:", code_result)
    print()
    goal_output = "31"
    val, l1 = var(), var()

    print("Line that has the correct output: ")
    correct_line = run(0, (l1, val), hasOutput(l1, val), eq(val, goal_output))[0]
    print(correct_line)

    print()

    a, b = var(), var()
    results = run(0, (a, b), depends(a, b))

    print("The lines that have dependencies are:")
    print(results)

    # dependency chain to goal
    goal_line = correct_line[0]

    # directed graph, flipped line pairs
    graph = nx.DiGraph()
    graph.add_nodes_from(list(range(len(src))))
    graph.add_edges_from([(b, a) for a, b in results])
    paths = nx.single_source_shortest_path(graph, goal_line)
    unused_nodes = graph.nodes()

    for node in paths:
        unused_nodes.remove(node)

    print("Extraneous lines of code:")
    print(unused_nodes)

if __name__ == "__main__":
    main()
