"""
This is a playground where I test some ideas for working with ASTs.
"""

import ast

# file_name = "../../data/HW3/hw3_121.py"
file_name = "test1.py"
lines = {}
vars_to_lines = {}

# a list of all python keywords
exempt_names = list(dir(__builtins__)) + ["main"]


class NameLister(ast.NodeVisitor):

    def visit_Name(self, node):

        if node.id not in exempt_names:
            lineno = getattr(node, 'lineno')
            print(lineno, node.id)
            if node.id in vars_to_lines:
                vars_to_lines[node.id].append((lineno, node.ctx))
            else:
                vars_to_lines[node.id] = [(lineno, node.ctx)]


def main():

    with open(file_name) as f:
        source = f.read()

    try:
        root = ast.parse(source)
        NameLister().visit(root)

    except SyntaxError:
        err_file_name = file_name.split("/")[-1]
        print("SyntaxError: <{}>".format(err_file_name))

if __name__ == '__main__':
    main()
