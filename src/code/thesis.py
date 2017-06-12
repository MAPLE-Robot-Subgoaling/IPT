from visitor import Visitor
from handlers import *
from converter import RewriteVars

from kanren import Relation, facts, run, var, conde, eq
from itertools import combinations

import ast
import astor
import networkx as nx
import subprocess

filename = "testfiles/test2.py"

has_id = Relation()
is_before = Relation()
assigns = Relation()
uses = Relation()
hasOutput = Relation()  # line L has output of value V

#goal_output = 41 #test1
#goal_output = 17 #test3
goal_output = "good" #test2
#goal_output = 72 #test3
#goal_output = 2 #test3
goals = [17, "good"]

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
    original_src = f.read()
    original_src_lines = original_src.split("\n")

src_ast = ast.parse(original_src)

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
for lineno, line in enumerate(original_src.split("\n"), 1):

    if line == "\n":
        print("Empty line")
        continue

    outstr = "[{0: >2}]: {1}".format(lineno, line.strip("\n"))
    print(outstr)

# walk the AST to give each node a parent
for node in ast.walk(new_tree):
    for child in ast.iter_child_nodes(node):
        child.parent = node

ast_visitor = Visitor()
ast_visitor.visit(new_tree)

assignments, usages, outputs, dependencies = ast_visitor.get_data()

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
    actual_line = src_lines[line - 1].strip()
    if len(actual_line) == 0:
        continue
    #print("actual:", actual_line)
    p = PrintVisitor()
    p.visit(ast.parse(actual_line))
    expr = p.get_expr()

    if len(expr) == 0:
        continue

    facts(hasOutput, (line, eval(expr)))

val, l1 = var(), var()

print()
print("Line that has the correct output: ")
correct_lines = []
for goal in goals:
    correct = run(0, (l1, val), hasOutput(l1, val), eq(val, goal))

    if len(correct) > 0:
        correct_line = correct[0]
    else:
        #TODO: issue, if they dont ahve a line that outputs the correct thing, it will think that everything is extraneous
        correct_line = None
        print("Failed to find correct output line")
        print("Perhaps goal_output is wrong")
        sys.exit(1)

    correct_lines.append(correct_line)

print(correct_lines)
a, b = var(), var()
results = list(run(0, (a, b), depends(a, b)))

# add known dependencies to the results
for key, val in dependencies.items():
    thing = zip([key]*len(val), val)
    for t in thing:
        results.append(t)

print("The lines that have dependencies are:")
print("results:", results)


# directed graph, flipped line pairs
graph = nx.DiGraph()
graph.add_nodes_from(list(range(1, len(src_lines)+1)))
graph.add_edges_from([(b, a) for a, b in results])
unused_nodes = graph.nodes()

#for every correct line that was found
for correct_line in correct_lines:

    # dependency chain to goal line
    goal_line = correct_line[0]
    paths = nx.single_source_shortest_path(graph, goal_line)

    # remove all nodes that are not in the path from goal to beginning
    # of the file
    for node in paths:
        try:
            unused_nodes.remove(node)
        except ValueError:
            pass

#thinks that empty lines are extraneous
for node in unused_nodes:
    if len(src_lines[node-1]) == 0:
        unused_nodes.remove(node)

print()
print("Extraneous lines of code:")
print(unused_nodes)
