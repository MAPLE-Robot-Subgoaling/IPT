from visitor import Visitor
from handlers import *
from converter import RewriteVars

from kanren import Relation, facts, run, var, conde, eq
from itertools import combinations

import ast
import astor
import networkx as nx
import subprocess

filename = "testfiles/test3.py"

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

with open(filename) as f:
    src = f.read()
    src_lines = src.split("\n")

# run the student's code to get their output
# code_result = run_code(filename)

src_ast = ast.parse(src)

# set parent nodes for every child
for node in ast.walk(src_ast):
    for child in ast.iter_child_nodes(node):
        child.parent = node

t = RewriteVars()
new_tree = t.visit(src_ast)

with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py", "w") as w:
    w.write(astor.to_source(new_tree))

#reread the source
with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py") as f:
    src = f.read()
    src_lines = src.split("\n")

# add the is_before fact for every valid pair of lines
facts(is_before, *combinations(range(len(src)), 2))

print("The input program is:")
for lineno, line in enumerate(src.split("\n"), 1):

    if line == "\n":
        print("Empty line")
        continue

    outstr = "[{0: >2}]: {1}".format(lineno, line.strip())
    print(outstr)

# walk the AST to give each node a parent
for node in ast.walk(new_tree):
    for child in ast.iter_child_nodes(node):
        child.parent = node

ast_visitor = Visitor()
ast_visitor.visit(new_tree)

assignments, usages, outputs = ast_visitor.get_data()

# add assignment facts to the KB
for variable in assignments:
    #print(*[(lineno, variable) for lineno in assignments[variable]])
    facts(assigns, *[(lineno, variable) for lineno in assignments[variable]])

# print()

# add usage facts to the KB
for variable in usages:
    #print(*[(lineno, variable) for lineno in usages[variable]])
    facts(uses, *[(lineno, variable) for lineno in usages[variable]])

# add output fact to the KB
# evaluate the output line to get the result
# if any variable is reused at any point in the program,
# copy the program and rename the reuses to different names,
# that way they printed expression will not change as is is at
# time is was printed
# later, you can derive what the expression would have been from
# a dependency graph, so you dont have to edit their code at all

import sys
old = sys.stdout
sys.stdout = None
from testfiles.new_test import *
sys.stdout = old

for line in outputs:
    actual_line = src_lines[line - 1]
    if len(actual_line) == 0:
        continue

    p = PrintVisitor()
    p.visit(ast.parse(actual_line))
    expr = p.get_expr()
    #print("Expression:", expr)
    #print("Evals to:", eval(expr))
    facts(hasOutput, (line, eval(expr)))


goal_output = 72
val, l1 = var(), var()

print("Line that has the correct output: ")
correct_line = run(0, (l1, val), hasOutput(l1, val), eq(val, goal_output))[0]
print(correct_line)

#print()

a, b = var(), var()
results = run(0, (a, b), depends(a, b))

print("The lines that have dependencies are:")
print(results)

# dependency chain to goal
goal_line = correct_line[0]

# directed graph, flipped line pairs
graph = nx.DiGraph()
graph.add_nodes_from(list(range(1, len(src_lines)+1)))
graph.add_edges_from([(b, a) for a, b in results])
paths = nx.single_source_shortest_path(graph, goal_line)
unused_nodes = graph.nodes()
#print(paths)

for node in paths:
    unused_nodes.remove(node)

print()
print("Extraneous lines of code:")
print(unused_nodes)
