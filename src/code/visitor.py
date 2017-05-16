import ast

# a list of all python keywords and exempt names
exempt_names = list(dir(__builtins__)) + ["main"]


class Visitor(ast.NodeVisitor):

    def __init__(self):
        super(Visitor, self).__init__()
        self.results = []

    def visit_Name(self, node):
        #print(node.id)
        self.results.append(node.id)

    def visit_Expr(self, node):
        pass

    def get_result(self):
        return self.results

