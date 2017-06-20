import ast
import astor
from visitor import Visitor
from handlers import *
from converter import RewriteVars
from kanren import var, eq, Relation, run, facts

hasOutput = Relation()

read_file = "/Users/mneary1/Desktop/IPT/src/code/testfiles/test1.py"
out_file = "/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py"
with open(read_file) as f:
    src = f.read()
    src_ast = ast.parse(src)

    # set parent nodes for every child
    for node in ast.walk(src_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    t = RewriteVars()
    new_tree = t.visit(src_ast)
    with open(out_file, "w") as w:
        w.write(astor.to_source(new_tree))

with open(out_file) as f:
    src = f.read()
    src_ast = ast.parse(src)

    # set parent nodes for every child
    for node in ast.walk(src_ast):
        for child in ast.iter_child_nodes(node):
            child.parent = node
    v = Visitor()
    v.visit(src_ast)
    a, u, o, d = v.get_data()
    print()
    print(a)
    print(u)
    print(o)
    print(d)

