import ast
import astor
from visitor import Visitor
from handlers import *
from converter import RewriteVars
from kanren import var, eq, Relation, run, facts

hasOutput = Relation()

filename = "/Users/mneary1/Desktop/IPT/src/code/testfiles/test3.py"
with open(filename) as f:
    src = f.read()
    src_ast = ast.parse(src)

    # set parent nodes for every child
    for node in ast.walk(src_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    t = RewriteVars()
    new_tree = t.visit(src_ast)
    with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py", "w") as w:
        w.write(astor.to_source(new_tree))

# don't write to stdout when importing code
import sys
old = sys.stdout
sys.stdout = None
from testfiles.new_test import *
sys.stdout = old

filename = "/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py"
with open(filename) as f:
    src = f.read()
    src_lines = src.split("\n")
    src_ast = ast.parse(src)

    # set parent nodes for every child
    for node in ast.walk(src_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    v = Visitor()
    v.visit(src_ast)
    assignments, usages, outputs = v.get_data()

    for line in outputs:
        actual_line = src_lines[line-1]
        if len(actual_line) == 0:
            continue

        p = PrintVisitor()
        p.visit(ast.parse(actual_line))
        expr = p.get_expr()
        print("Expression:", expr)
        print("Evals to:", eval(expr))
        facts(hasOutput, (line, eval(expr)))

    n = var()
    goal = 72
    print(run(0, n, hasOutput(n, goal)))
