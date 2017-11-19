import ast

# a list of all python keywords and exempt names
exempt_names = list(dir(__builtins__)) + ["main", "print"]

class Visitor(ast.NodeVisitor):

    def __init__(self):
        super(Visitor, self).__init__()
        self.assignments = {}
        self.usages = {}
        self.outputs = []
        self.dependencies = {}

    def get_data(self):
        return self.assignments, self.usages, self.outputs, self.dependencies

    def add_usage(self, name, lineno):
        try:
            self.usages[name].append(lineno)
        except KeyError:
            self.usages[name] = [lineno]

    def add_assignment(self, name, lineno):
        try:
            self.assignments[name].append(lineno)
        except KeyError:
            self.assignments[name] = [lineno]

    def add_output(self, lineno):
        try:
            self.outputs.append(lineno)
        except KeyError:
            self.outputs = [lineno]

    def add_dependency(self, lineA, lineB):
        try:
            self.dependencies[lineA].append(lineB)
        except KeyError:
            self.dependencies[lineA] = [lineB]

    def visit_If(self, node):

        # add a dependency between each body line and the condition
        for body_line in node.body:
            self.add_dependency(node.lineno, body_line.lineno)

        if len(node.orelse) > 0:

            # add dependency between each thing in the else clause
            if isinstance(node.orelse[0], ast.If):
                self.add_dependency(node.lineno, node.orelse[0].lineno)
            else:
                # "else:" is one line before the first body line
                else_lineno = node.orelse[0].lineno - 1
                self.add_dependency(node.lineno, else_lineno)
                for body_line in node.orelse:
                    self.add_dependency(else_lineno, body_line.lineno)

        self.generic_visit(node)

    def visit_For(self, node):
        # add the structural dependencies
        for line in node.body:
            self.add_dependency(node.lineno, line.lineno)

        self.generic_visit(node)

    def visit_While(self, node):
        # add the structural dependencies
        for line in node.body:
            self.add_dependency(node.lineno, line.lineno)

        self.generic_visit(node)

    def visit_Name(self, node):
        # TODO: might have to figure out what to do with main
        if node.id in exempt_names:
            return

        # the variable is being loaded somewhere, so it is used
        if isinstance(node.ctx, ast.Load):
            self.add_usage(node.id, node.lineno)

        elif isinstance(node.parent, ast.Assign) and isinstance(node.ctx, ast.Store):
            self.add_assignment(node.id, node.lineno)

        elif isinstance(node.parent, ast.For) and isinstance(node.ctx, ast.Store):
            self.add_assignment(node.id, node.lineno)

        elif isinstance(node.parent, ast.AugAssign) and isinstance(node.ctx, ast.Store):
            self.add_assignment(node.id, node.lineno)
            self.add_usage(node.id, node.lineno)

        else:
            print("ERROR: nothing done with {} in visit_Name".format(node.id))
            print(vars(node))

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            self.add_output(node.lineno)
        self.generic_visit(node)
