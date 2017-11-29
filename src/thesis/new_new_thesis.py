from thesis.visitors import *

from kanren import facts, run
from itertools import combinations

import ast
import networkx as nx
import regex as re
import os
from thesis.config import *
from thesis.relations import *


def run_thesis(path_to_file, inputs, goals, **kwargs):

    if 'output_dir' in kwargs:
        output_path = kwargs['output_dir']
    else:
        output_path = "/Users/mneary1/Desktop/IPT/src/thesis/testfiles/outputs/"

    extraneous_dict = {}
    filename = os.path.split(path_to_file)[1]

    # the directed dependency graph (DDG)
    graph = nx.DiGraph()

    # read the original source of the target program
    with open(path_to_file) as f:
        original_src_lines = f.readlines()

    # add a node in the DDG for each line in the source
    graph.add_nodes_from(list(range(1, len(original_src_lines) + 1)))

    # add the is_before fact for every valid pair of lines
    facts(is_before, *combinations(range(1, len(original_src_lines) + 1), 2))

    # turn the original source into an AST
    src_ast = ast.parse("".join(original_src_lines))

    # set parent nodes for everything in the AST
    for node in ast.walk(src_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node
    '''
    #rewrite variables
    t = RewriteVars()
    new_ast = t.visit(src_ast)

    # set parent nodes for everything in the new AST
    for node in ast.walk(new_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    ast_visitor = Visitor()
    ast_visitor.visit(new_ast)
    '''
    ast_visitor = Visitor()
    ast_visitor.visit(src_ast)

    # get the assignments and usages to determine the data dependencies
    # get the structural dependencies
    assignments, usages, outputs, dependencies = ast_visitor.get_data()

    # add assignment facts to the KB
    for variable in assignments:
        facts(assigns, *[(lineno, variable) for lineno in assignments[variable]])

    # add usage facts to the KB
    for variable in usages:
        facts(uses, *[(lineno, variable) for lineno in usages[variable]])


    # add the semantic dependencies of the target program
    if INCLUDE_SEMANTIC:
        a, b = var(), var()
        results = list(run(0, (a, b), depends(a, b)))
    else:
        results = []

    # add structural dependencies of the target program
    if INCLUDE_STRUCTURE:
        for key, val in dependencies.items():
            thing = zip([key]*len(val), val)
            for t in thing:
                results.append(t)

    #try to find the output and determine if it is correct for each given input
    for input_name in inputs:

        # set up the file names appropriately
        output = os.path.join(output_path, filename + ".out")

        # run a trace of the target program with this input, then analyze the output of the trace
        cmd = "python3 -m trace --trace {} < {} > {}".format(path_to_file, input_name, output)
        cmdresult = os.system(cmd)
        if cmdresult != 0:
            raise RuntimeError("Failed to execute a trace of <" + filename + ">")

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
            #print("Failed to find correct output using {}".format(input_name))
            #print("Extraneous lines of code do not exist in unfinished programs.")
            return [], ''

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
            #print(node, len(original_src_lines))
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

    #print("Extraneous lines:", extraneous_lies)n
    source = original_src_lines
    return extraneous_lines, source
