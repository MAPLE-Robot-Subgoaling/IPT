"""
This is a playground where I test some ideas for working with ASTs.
"""

import ast
from pretty_dump import dump

# file_name = "../../data/HW3/hw3_121.py"
file_name = "test.py"
lines = {}
vars_to_lines = {}

# a list of all python keywords
exempt_names = list(dir(__builtins__)) + ["main"]

class NameLister(ast.NodeVisitor):


    def visit_Name(self, node):

        if node.id not in exempt_names:
            lineno = getattr(node, 'lineno')
            print(lineno, node.id)

            '''
            if node.id in vars_to_lines:
                vars_to_lines[node.id].append((lineno, node.ctx))
            else:
                vars_to_lines[node.id] = [(lineno, node.ctx)]
            '''


class AssignVisitor(ast.NodeVisitor):

    def visit_Assign(self, node):
        for target in node.targets:
            # if the node in the target is a Store, and the value being assigned is a number
            if isinstance(target.ctx, ast.Store):

                if isinstance(node.value, ast.Num):
                    print("Storing {} in id '{}'".format(node.value.n, target.id))
                if isinstance(node.value, ast.BinOp):
                    s = binOpToString(node.value)
                    print("Storing '{}' in id '{}'".format(s, target.id))


def binOpToString(binop):

    if isinstance(binop, ast.Name):
        return binop.id
    if isinstance(binop, ast.Num):
        return str(binop.n)
    if not isinstance(binop, ast.BinOp):
        return "ERR"

    if isinstance(binop.op, ast.Add):
        op = " + "
    elif isinstance(binop.op, ast.Sub):
        op = " - "
    elif isinstance(binop.op, ast.Mult):
        op = " * "
    elif isinstance(binop.op, ast.Div):
        op = " / "
    else:
        op = " ? "

    return binOpToString(binop.left) + op + binOpToString(binop.right)


def main():

    with open(file_name) as f:
        source = f.read()

    try:
        root = ast.parse(source)
        #NameLister().visit(root)
        AssignVisitor().visit(root)

    except SyntaxError:
        err_file_name = file_name.split("/")[-1]
        print("SyntaxError in: <{}>".format(err_file_name))

if __name__ == '__main__':
    main()
