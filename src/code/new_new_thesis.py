from visitor import Visitor
from handlers import *
from converter import RewriteVars

from kanren import Relation, facts, run, var, conde, eq
from itertools import combinations

import ast
import astor
import networkx as nx
import regex as re
import os
import sys

# constant values below
# flags for what dependencies to include
INCLUDE_EXECUTE = False
INCLUDE_STRUCTURE = True
INCLUDE_SEMANTIC = True

OUTPUT_BASE_DIR = "/Users/mneary1/Desktop/IPT/src/code/testfiles/outputs/"
# location of the intermediate files
INTERMEDIATE_BASE_DIR = "/Users/mneary1/Desktop/IPT/src/code/testfiles/intermediates/"
# names of each input file
INPUT_BASE_DIR = "/Users/mneary1/Desktop/IPT/src/code/testfiles/inputs/"

# declaration of the relations
has_id = Relation()
is_before = Relation()
assigns = Relation()
uses = Relation()
hasOutput = Relation()  # line L has output of value V

# define the data dependency relationship
def depends(a, b):
    '''there is a dependency between two lines {A, B} if:
    they share an ID X AND
    A comes before B AND
    X is a target for the assignment on line A AND
    B uses X (not just an assignment where X is a target'''
    shared_id = var()
    return conde([is_before(a, b), assigns(a, shared_id), uses(b, shared_id)])

def run_thesis(path_to_file, inputs, goals):

    extraneous_dict = {}
    filename = os.path.split(path_to_file)[1]

    # the directed dependency graph (DDG)
    graph = nx.DiGraph()

    # read the original source of the target program
    with open(path_to_file) as f:
        original_src = f.read()
        f.seek(0)
        original_src_lines = f.readlines()

    # add a node in the DDG for each line in the source
    graph.add_nodes_from(list(range(1, len(original_src_lines)+1)))

    # add the is_before fact for every valid pair of lines
    facts(is_before, *combinations(range(1, len(original_src_lines)+1), 2))

    # turn the origianl source into an AST
    src_ast = ast.parse(original_src)

    # set parent nodes for everything in the AST
    for node in ast.walk(src_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    # perform the translation of source AST to intermediate AST
    t = RewriteVars()
    new_tree = t.visit(src_ast)
    
    # write the AST object to a file so it can be written to the screen
    with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py", "w") as w:
        w.write(astor.to_source(new_tree))
    
    # reread the sources
    with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py") as f:
        src = f.read()
        f.seek(0)
        src_lines = f.readlines()
        for i, line in enumerate(original_src_lines):
            if line == "\n" and src_lines[i] != "\n":
                src_lines.insert(i, "\n")
    
    # walk the AST to give each node a parent
    for node in ast.walk(new_tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    ast_visitor = Visitor()
    ast_visitor.visit(new_tree)
    #v = ast.parse(original_src)
    #for node in ast.walk(v):
    #    for child in ast.iter_child_nodes(node):
    #        child.parent = node
    #ast_visitor.visit(v)

    # get the assignments and usages to determine the data dependencies
    # get the structural dependencies
    assignments, usages, outputs, dependencies = ast_visitor.get_data()

    # add assignment facts to the KB
    for variable in assignments:
        facts(assigns, *[(lineno, variable) for lineno in assignments[variable]])

    # add usage facts to the KB
    for variable in usages:
        facts(uses, *[(lineno, variable) for lineno in usages[variable]])

    a, b = var(), var()
    results = []

    # add the semantic dependencies of the target program
    if INCLUDE_SEMANTIC:
        results = list(run(0, (a, b), depends(a, b)))

    # add structural dependencies of the target program
    if INCLUDE_STRUCTURE:
        for key, val in dependencies.items():
            thing = zip([key]*len(val), val)
            for t in thing:
                results.append(t)

    # for each input the the target program
    for input_name in inputs:

        # set up the file names appropriately
        # input = INPUT_BASE_DIR + input_name
        output = input_name + ".out"

        # run a trace of the target program with this input, then analyze the output of the trace
        cmd = "python3 -m trace --trace {} < {} > {}".format(path_to_file, input_name, output)
        os.system(cmd)

        # determine the line number of each line that was executed
        # also determines which print statements are responsible for what output
        executed_lines = []
        lineno = 0
        flag = False
        outputstr = ''

        outf = open(output)
        for line in outf:
            if line.startswith(filename):
                executed_lines.append(int(line[line.index('(') + 1:line.index(')')]))

            if flag and (filename in line or line.startswith(" ---")):
                # TODO: this might make things not work but we'll see
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

        outf.close()

        # determines the execution dependency pairs
        execution_dependencies = []
        for i in range(len(executed_lines) - 1):
            a = executed_lines[i]
            b = executed_lines[i + 1]
            execution_dependencies.append((a, b))

        # get the lines that give correct output
        correct_lines = []
        # get all the lines that output something
        val, l1 = var(), var()
        outputs = run(0, (l1, val), hasOutput(l1, val))

        for line, output in outputs:
            for goal in goals:
                found_goal = re.findall(re.escape(goal), output, overlapped=True)
                if line in executed_lines and len(found_goal) == 1:
                    correct_lines.append((line, output))


        # if no matches were found, terminate execution
        if len(correct_lines) == 0:
            print("Failed to find correct output using {}".format(input_name))
            print("Extraneous lines of code do not exist in unfinished programs.")
            return []

        # Here we create the directed dependency graph (DDG)
        # line pairs flipped so it looks from the goal line(s) to the beginning
        graph.add_edges_from([(b, a) for a, b in results])

        # add execution dependencies to the results
        if INCLUDE_EXECUTE:
            graph.add_edges_from([(u, v) for u, v in execution_dependencies])

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
        # TODO: make it handle functions, this is just a workaround to avoid main
        for i in range(len(unused_nodes)):
            node = unused_nodes[i]
            line = original_src_lines[node - 1]
            if line.isspace() or len(line) == 0:
                extraneous_lines.remove(node)
            elif 'main()' in line or 'def' in line:
                extraneous_lines.remove(node)

        for lineno in extraneous_lines:
            try:
                extraneous_dict[lineno] += 1
            except KeyError:
                extraneous_dict[lineno] = 1

        # remove the execution dependencies from the results for this particular run
        if INCLUDE_EXECUTE:
            graph.remove_edges_from([(u, v) for u, v in execution_dependencies])

    # An extraneous line is one that appears as extraneous for all possible inputs
    extraneous_lines = []
    for key, val in extraneous_dict.items():
        if val == len(inputs):
            extraneous_lines.append(key)

    print("Extraneous lines:", extraneous_lines)
    return extraneous_lines
