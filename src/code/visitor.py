import ast

# a list of all python keywords and exempt names
exempt_names = list(dir(__builtins__)) + ["main", "print"]


class Visitor(ast.NodeVisitor):

    def __init__(self):
        super(Visitor, self).__init__()
        self.assignments = {}
        self.usages = {}
        self.outputs = []

    def get_data(self):
        return self.assignments, self.usages, self.outputs

    def visit_If(self, node):
        print("if statement found on line", node.lineno)
        self.generic_visit(node)

    def visit_Assign(self, node):
        #print()
        #print("assignment found on line", node.lineno)
        self.generic_visit(node)

    def visit_Expr(self, node):
        #print()
        #print("expression found on line", node.lineno)
        self.generic_visit(node)

    def visit_For(self, node):
        print("for loop found on line", node.lineno)
        self.generic_visit(node)

    def visit_While(self, node):
        print("while loop found on line", node.lineno)
        self.generic_visit(node)

    def visit_Name(self, node):

        if isinstance(node.parent, ast.Assign) and isinstance(node.ctx, ast.Store):
            #print("id<{}> assigned a value on {}".format(node.id, node.lineno))
            try:
                self.assignments[node.id].append(node.lineno)
            except KeyError:
                self.assignments[node.id] = [node.lineno]

        elif isinstance(node.parent, ast.BinOp) and isinstance(node.ctx, ast.Load):
            #print("id<{}> used in binary op. on {}".format(node.id, node.lineno))
            try:
                self.usages[node.id].append(node.lineno)
            except KeyError:
                self.usages[node.id] = [node.lineno]

        elif isinstance(node.parent, ast.Call) and node.id not in exempt_names:
            print("id<{}> used in func call on {}".format(node.id, node.lineno))
            try:
                self.usages[node.id].append(node.lineno)
            except KeyError:
                self.usages[node.id] = [node.lineno]

    def visit_Call(self, node):
        if node.func.id == 'print':
            try:
                self.outputs.append(node.lineno)
            except KeyError:
                self.outputs = [node.lineno]