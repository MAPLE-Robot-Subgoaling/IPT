import os
import networkx
import regex as re

from itertools import combinations
from kanren import facts, run

from thesis.relations import *
from thesis.visitors import *
from thesis.errors import *


class ExtraneousLineFinder:

    def __init__(self, file, io, output='',
                 with_execute=False,
                 with_structure=False,
                 with_semantic=False):
        """:file:   path to the assignment that will be analyzed
           :io: a mapping of input file to correct output files
           :output: a path to write output to
           :with_semantic: include semantic dependencies
           :with_execute: include execution dependencies
           :with_structure: include structural dependencies"""

        # sanity check to make sure that the given files exist before moving on
        assert os.path.isfile(file), "The assignment file {} doesn't exist.".format(file)

        for goal_file in io.values():
            assert os.path.isfile(goal_file), "The goal file {} doesn't exist.".format(goal_file)

        for input_file in io.keys():
            assert os.path.isfile(input_file), "The input file {} doesn't exist.".format(input_file)

        self.file = file
        self.io = io

        # TODO: turn single goals file into multiple files, one for each input. Read in the goals
        # according to the current input being tested
        #with open(goals) as g:
        #    self.goals = [line.strip() for line in g.readlines()]

        self.extraneous = {}
        self.extraneous_lines = []

        self.with_execute = with_execute
        self.with_structure = with_structure
        self.with_semantic = with_semantic

        if output:
            self.output = output
        else:
            self.output = os.path.join(os.getcwd(), "temp")

        with open(file) as f:
            self.src_lines = f.readlines()
            self.src_ast = ast.parse("".join(self.src_lines))

            # set parent nodes for everything in the AST
            for node in ast.walk(self.src_ast):
                for child in ast.iter_child_nodes(node):
                    child.parent = node

        # add a node in the DDG for each line in the source
        self.ddg = networkx.DiGraph()
        self.ddg.add_nodes_from(list(range(1, len(self.src_lines) + 1)))

    def _bootstrap_facts(self):
        ast_visitor = Visitor()
        ast_visitor.visit(self.src_ast)

        # get the assignments and usages to determine the data dependencies
        # get the structural dependencies
        assignments, usages, outputs, dependencies = ast_visitor.get_data()

        results = []

        # add the is_before fact for every valid pair of lines
        # this is necessary for the dependency relation to work, so it must happen first
        facts(is_before, *combinations(range(1, len(self.src_lines) + 1), 2))

        # add assignment facts to the KB
        for variable in assignments:
            facts(assigns, *[(lineno, variable) for lineno in assignments[variable]])

        # add usage facts to the KB
        for variable in usages:
            facts(uses, *[(lineno, variable) for lineno in usages[variable]])

        # add the semantic dependencies of the target program
        if self.with_semantic:
            a, b = var(), var()
            results += list(run(0, (a, b), depends(a, b)))

        # add structural dependencies of the target program
        if self.with_structure:
            for key, val in dependencies.items():
                thing = zip([key] * len(val), val)
                for t in thing:
                    results.append(t)

        return results

    def _run_trace(self, input_name):
        file_name = os.path.splitext(os.path.basename(self.file))[0]
        output_path = os.path.join(self.output, file_name + ".out")
        cmd = "python3 -m trace --trace {} < {} > {}".format(self.file, input_name, output_path)
        cmd_result = os.system(cmd)

        # TODO: maybe I don't want to raise an exception here
        if cmd_result != 0:
            raise RuntimeError("Failed to execute a trace of <" + self.file + ">")

        # determine the line number of each line that was executed
        # also determines which print statements are responsible for what output
        executed_lines = []
        lineno = 0
        flag = False
        outputstr = ''

        outf = open(output_path)
        for line in outf:
            if line.startswith(file_name):
                executed_lines.append(int(line[line.index('(') + 1:line.index(')')]))

            if flag and (file_name in line or line.startswith(" ---")):
                # TODO: this might make things not work but we'll see
                facts(has_output, (int(lineno), outputstr))
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
        return executed_lines

    def __enter__(self):
        print("File being tested: {}".format(self.file))
        results_so_far = self._bootstrap_facts()

        # find the output and determine its correctness for each input file
        for input_file, goal_file in self.io.items():

            print("Iteration <{}> <{}>".format(input_file, goal_file))

            # read in the corresponding goal file
            with open(goal_file) as f:
                goals = f.readlines()

            # determine the execution dependency pairs
            executed_lines = self._run_trace(input_file)
            execution_dependencies = []
            for i in range(len(executed_lines) - 1):
                a = executed_lines[i]
                b = executed_lines[i + 1]
                execution_dependencies.append((a, b))

            # get all the lines that output something for this particular run
            l1, val = var(), var()
            result_outputs = run(0, (l1, val), has_output(l1, val))

            # get the lines that give correct output
            correct_lines = []
            for line, output in result_outputs:
                for goal in goals:
                    found_goal = re.findall(re.escape(goal), output, overlapped=True)
                    if line in executed_lines and len(found_goal) == 1:
                        correct_lines.append((line, output))

            # if no matches were found, terminate execution
            # TODO: might want to rethink throwing an exception here...
            if len(correct_lines) == 0:
                raise GoalNotFoundError("Correct output not found with input {}".format(input_file))

            # add edges to the directed dependency graph from the semantic and structural depedencies found so far
            # edges between line pairs flipped so it can look from the goal line(s) to the beginning
            # adding an edge that already exists with not add a double edge to the graph
            self.ddg.add_edges_from([(b, a) for a, b in results_so_far])
            # TODO: make sure that the graph nodes are actually working


            # add execution dependencies to the results
            # again, ading edges "backwards" so we can search from the goal forward
            if self.with_execute:
                self.ddg.add_edges_from([(v, u) for u, v in execution_dependencies])

            print("\t edges: {}".format(self.ddg.edges()))
            print()

            #initialize unused nodes to all nodes in the graph currently
            unused_nodes = self.ddg.nodes()

            for correct_line in correct_lines:

                # determine all paths from the goal to other reachable lines
                goal_line = correct_line[0]
                paths = networkx.single_source_shortest_path(self.ddg, goal_line)

                # remove all nodes that are in the path from goal to beginning of the file
                for node in paths:
                    try:
                        unused_nodes.remove(node)
                    except ValueError:
                        pass

            extraneous_lines = list(unused_nodes)

            # thinks that empty lines, and function defs are extraneous
            for i in range(len(unused_nodes)):
                node = unused_nodes[i]
                line = self.src_lines[node - 1]
                if line.isspace() or len(line) == 0:
                    extraneous_lines.remove(node)
                elif 'main()' in line or 'def' in line:
                    extraneous_lines.remove(node)

            # count the lines that were extraneous for each input
            for lineno in extraneous_lines:
                try:
                    self.extraneous[lineno] += 1
                except KeyError:
                    self.extraneous[lineno] = 1

            # remove the execution dependencies from the results for this particular run
            # they should not persist for the next iteration
            if self.with_execute:
                self.ddg.remove_edges_from([(v, u) for u, v in execution_dependencies])

            # this relation needs to be reset so it doesn't carry over any output from previous iterations
            has_output.reset()

        # An extraneous line is one that appears as extraneous for all given inputs
        for key, val in self.extraneous.items():
            if val == len(self.io):
                self.extraneous_lines.append(key)

        # print("Extraneous lines: {}".format(self.extraneous_lines))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        reset_all_relations()
