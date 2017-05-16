from visitor import Visitor
import ast


filename = "test.py"

with open(filename) as f:
    src = f.read()

src_ast = ast.parse(src)
Visitor().visit(src_ast)