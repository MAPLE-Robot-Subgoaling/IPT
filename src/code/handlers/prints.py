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
            for i, arg in enumerate(node.args):
                if isinstance(arg, ast.BinOp):
                    self.expr += "str(" + binOpToString(arg) + ")"
                elif isinstance(arg, ast.Name):
                    self.expr += "str(" + arg.id + ")"
                elif isinstance(arg, ast.Str):
                    self.expr += "'" + arg.s + "'"

                if len(node.args) > 1 and i != len(node.args)-1:
                    self.expr += ' + " " + '
