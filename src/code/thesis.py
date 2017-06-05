from handlers import *

from kanren import Relation, facts, run, var, conde
from itertools import combinations

import ast
import networkx as nx

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

    # dependency chain to goal
    goal_line = 5  # TODO: change this to a logic rule

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
