from visitor import Visitor
from handlers import *
from converter import RewriteVars

from kanren import Relation, facts, run, var, conde, eq
from itertools import combinations

import ast
import astor
import networkx as nx
import os
import sys

# figure out which lines are actually executed when the code is run
outf_name = "/Users/mneary1/Desktop/IPT/src/code/out.txt"

code_name_prefix = "/Users/mneary1/Desktop/IPT/src/code/testfiles/"
code_file_name = "test4.py"
code_file = code_name_prefix + code_file_name

inputf_name = "/Users/mneary1/Desktop/IPT/src/code/test4_input2"

# declaration of the relations
has_id = Relation()
is_before = Relation()
assigns = Relation()
uses = Relation()
hasOutput = Relation()  # line L has output of value V

# run a trace of the target program, then analyze the output of the trace
cmd = "python3 -m trace --trace {} < {} > {}".format(code_file, inputf_name, outf_name)
os.system(cmd)

# determine the line number of each line that was executed
# also determines which print statements are responsible for what output
executed_lines = []
lineno = 0
flag = False
outputstr = ''

outf = open(outf_name)
for line in outf:
    if line.startswith(code_file_name):
        executed_lines.append(int(line[line.index('(') + 1:line.index(')')]))

    if flag and (code_file_name in line or line.startswith(" ---")):
        facts(hasOutput, (int(lineno), outputstr))
        flag = False
        outputstr = ''

    if flag:
        outputstr += line

    if 'print' in line:
        flag = True
        left = line.index("(")
        right = line.index(")")
        lineno = line[left + 1:right]


# determines the execution dependency pairs
execution_dependencies = []
for i in range(len(executed_lines)-1):
    a = executed_lines[i]
    b = executed_lines[i+1]
    execution_dependencies.append((a, b))

#goal_output = 41 #test1
#goal_output = 17 #test3
#goal_output = "good" #test2
#goal_output = 72 #test3
#goal_output = 2 #test3
#goals = [17, "good"]
#goals = ["y is: 19 17"]
goals = ["At this temperature, water is a liquid"]
#goals = ["31"]
#goals = ['191\n']
#goals = ['***', '**', '*']

def depends(a, b):
    '''there is a dependency between two lines {A, B} if:
    they share an ID X AND
    A comes before B AND
    X is a target for the assignment on line A AND
    B uses X (not just an assignment where X is a target'''
    shared_id = var()
    return conde([is_before(a,b), assigns(a, shared_id), uses(b, shared_id)])

with open(code_file) as f:
    original_src = f.read()
    f.seek(0)
    original_src_lines = f.readlines()

src_ast = ast.parse(original_src)

# set parent nodes for every child
for node in ast.walk(src_ast):
    for child in ast.iter_child_nodes(node):
        child.parent = node


t = RewriteVars()
new_tree = t.visit(src_ast)

with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py", "w") as w:
    w.write(astor.to_source(new_tree))

# reread the sources
with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py") as f:
    src = f.read()
    f.seek(0)
    src_lines = f.readlines()
    for i, line in enumerate(original_src_lines):
        if len(line) == 0:
            src_lines.insert(i, "\n")

# add the is_before fact for every valid pair of lines
facts(is_before, *combinations(range(1, len(src_lines)+1), 2))

print("The input program is:")
for lineno, line in enumerate(original_src_lines, 1):
    outstr = "[{0: >2}]: {1}".format(lineno, line.strip("\n"))
    print(outstr)

print()
print("The altered input program is:")
for lineno, line in enumerate(src_lines, 1):
    outstr = "[{0: >2}]: {1}".format(lineno, line.strip("\n"))
    print(outstr)

print()
print("The executed lines are:")
print(executed_lines)

# walk the AST to give each node a parent
for node in ast.walk(new_tree):
    for child in ast.iter_child_nodes(node):
        child.parent = node

ast_visitor = Visitor()
ast_visitor.visit(new_tree)

assignments, usages, outputs, dependencies = ast_visitor.get_data()

# add assignment facts to the KB
for variable in assignments:
    facts(assigns, *[(lineno, variable) for lineno in assignments[variable]])


# add usage facts to the KB
for variable in usages:
    facts(uses, *[(lineno, variable) for lineno in usages[variable]])

# get the lines that give correct output
val, l1 = var(), var()

print()
print("Line(s) that have the correct output: ")
correct_lines = []
# get all the lines that output something
outputs = run(0, (l1, val), hasOutput(l1, val))
import regex as re
for line, output in outputs:
    for goal in goals:
        found_goal = re.findall(re.escape(goal), output, overlapped=True)
        if line in executed_lines and len(found_goal) == 1:
            correct_lines.append((line, output))

print(correct_lines)

# if no matches were found, terminate execution
if len(correct_lines) == 0:
    print("Failed to find correct output line")
    print("Extraneous lines of code do not exist in unfinished programs.")
    sys.exit(1)


a, b = var(), var()
results = list(run(0, (a, b), depends(a, b)))

# add structural dependencies to the results
for key, val in dependencies.items():
    thing = zip([key]*len(val), val)
    for t in thing:
        results.append(t)

# add execution dependencies to the results
# results += execution_dependencies

print()
print("Lines that have dependencies:")
print(results)

# Here we create the directed dependency graph (DDG)
# line pairs flipped so it looks from the goal line(s) to the beginning
graph = nx.DiGraph()
graph.add_nodes_from(list(range(1, len(src_lines)+1)))
graph.add_edges_from([(b, a) for a, b in results])
unused_nodes = graph.nodes()

# for every correct line that was found
for correct_line in correct_lines:

    # dependency chain to goal line
    goal_line = correct_line[0]
    paths = nx.single_source_shortest_path(graph, goal_line)

    # remove all nodes that are in the path from goal to beginning of the file
    for node in paths:
        try:
            unused_nodes.remove(node)
        except ValueError:
            pass

extraneous_lines = list(unused_nodes)

# thinks that empty lines are extraneous
for i in range(len(unused_nodes)):
    node = unused_nodes[i]
    line = original_src_lines[node-1]
    if len(line) == 1 and line == '\n':
        extraneous_lines.remove(node)

print()
print("Extraneous lines of code:")
print(extraneous_lines)
