import ast
from .helpers import binOpToString

class PrintVisitor(ast.NodeVisitor):
    def __init__(self):
        super(PrintVisitor, self).__init__()
        self.expr = ''

    def get_expr(self):
        return self.expr

    def visit_Call(self, node):
        if node.func.id == 'print':
            for arg in node.args:
                if isinstance(arg, ast.BinOp):
                    self.expr += binOpToString(arg)
                elif isinstance(arg, ast.Name):
                    self.expr += arg.id
