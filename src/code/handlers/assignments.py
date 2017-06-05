import ast


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
                    s = self.binOpToString(node.value)
                    # print("Storing '{}' in id '{}'".format(s, target.id))

    def binOpToString(self, binop):

        if isinstance(binop, ast.Name):
            self.right_side.append(binop.id)
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

        return self.binOpToString(binop.left) + op + self.binOpToString(binop.right)
