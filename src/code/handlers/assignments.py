import ast
from .helpers import binOpToString

class AssignVisitor(ast.NodeVisitor):

    def __init__(self):
        super(AssignVisitor, self).__init__()
        self.right_side = []
        self.left_side = ''

    def get_results(self):
        return self.left_side, self.right_side

    def visit_Assign(self, node):
        for target in node.targets:
            # if the node in the target is a Store, and the value being assigned is a number
            if isinstance(target.ctx, ast.Store):
                self.left_side = target.id

                if isinstance(node.value, ast.Num):
                    # print("Storing {} in id '{}'".format(node.value.n, target.id))
                    pass

                if isinstance(node.value, ast.BinOp):
                    s = binOpToString(node.value)
                    # print("Storing '{}' in id '{}'".format(s, target.id))

