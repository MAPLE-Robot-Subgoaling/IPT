import ast

# a list of all python keywords and exempt names
exempt_names = list(dir(__builtins__)) + ["main", "print"]


class Visitor(ast.NodeVisitor):

    def __init__(self):
        super(Visitor, self).__init__()
        self.results = []

    def visit_Name(self, node):
        if node.id not in exempt_names:
            self.results.append(node.id)

    def get_result(self):
        return self.results
