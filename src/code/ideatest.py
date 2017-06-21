import astor, ast
from converter import RewriteVars

filename = "/Users/mneary1/Desktop/IPT/src/code/testfiles/test2.py"

with open(filename) as f:
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

#reread the sources
with open("/Users/mneary1/Desktop/IPT/src/code/testfiles/new_test.py") as f:
    src = f.read()
    src_lines = src.split("\n")

for l in src_lines:
    print(l)