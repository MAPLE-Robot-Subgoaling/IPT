import ast


class ExprVisitor(ast.NodeVisitor):

    def __init__(self):
        super(ExprVisitor, self).__init__()
        self.variables_used = []

    def get_vars_used(self):
        return self.variables_used

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Call):
            for arg in node.value.args:
                if isinstance(arg, ast.Name):
                    self.variables_used.append(arg.id)