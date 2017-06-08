from visitor import Visitor

from kanren import Relation, facts, run, var, conde, eq
from itertools import combinations

import ast
import networkx as nx
import subprocess

filename = "testfiles/test1.py"
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
        src = f.read()

    # run the student's code to get their output
    code_result = run_code(filename)

    # add the is_beofre fact for every valid pair of lines
    facts(is_before, *combinations(range(len(src)), 2))

    print("The input program is:")
    for lineno, line in enumerate(src.split("\n"), 1):

        if line == "\n":
            print("Empty line")
            continue

        outstr = "[{0: >2}]: {1}".format(lineno, line.strip())
        print(outstr)


    src_ast = ast.parse(src)

    # walk the AST to give each node a parent
    for node in ast.walk(src_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    ast_visitor = Visitor()
    ast_visitor.visit(src_ast)

    assignments, usages, outputs = ast_visitor.get_data()

    # add assignment facts to the KB
    for variable in assignments:
        # print(*[(lineno, var) for lineno in assignments[var]])
        facts(assigns, *[(lineno, variable) for lineno in assignments[variable]])

    # add usage facts to the KB
    for variable in usages:
        # print(*[(lineno, var) for lineno in usages[var]])
        facts(uses, *[(lineno, variable) for lineno in usages[variable]])

    # add output fact to the KB
    print(outputs)
    # evaluate the output line to get the result
    # if any variable is reused at any point in the program,
    # copy the program and rename the reuses to different names,
    # that way they printed expression will not change as is is at
    # time is was printed
    # later, you can derive what the expression would have been from
    # a dependency graph, so you dont have to edit their code at all




    '''
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
    '''

if __name__ == "__main__":
    main()
