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
        #print("if statement found on line", node.lineno)

        '''
        if isinstance(node.test, ast.BoolOp):
            print("test is a boolop")
        elif isinstance(node.test, ast.Compare):
            print("test is a compare")
        elif isinstance(node.test, ast.Name):
            print("test is just a name")
            self.add_usage(node.test.id, node.lineno)

        for thing in node.test.comparators:
            if isinstance(thing, ast.Name):
                print("Name in the comparators")
            elif isinstance(thing, ast.BinOp):
                print("Binop in the comparators")
        '''

        for body_line in node.body:
            self.add_dependency(node.lineno, body_line.lineno)

        if not isinstance(node.orelse, ast.If):
            for body_line in node.orelse:
                self.add_dependency(node.lineno, body_line.lineno)

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
        # print(type(node), type((node.parent)))

        # TODO: might have to figure out what to do with main
        if node.id in exempt_names:
            return

        if isinstance(node.parent, ast.Assign) and isinstance(node.ctx, ast.Store):
            #print("id<{}> assigned a value on {}".format(node.id, node.lineno))
            self.add_assignment(node.id, node.lineno)

        elif isinstance(node.parent, ast.BinOp) and isinstance(node.ctx, ast.Load):
            #print("id<{}> used in binary op. on {}".format(node.id, node.lineno))
            self.add_usage(node.id, node.lineno)

        elif isinstance(node.parent, ast.Call):
            #print("id<{}> used in func<{}> call on {}".format(node.id, node.parent.func.id, node.lineno))
            self.add_usage(node.id, node.lineno)

        elif isinstance(node.parent, ast.Compare) and isinstance(node.ctx, ast.Load):
            # print("id<{}> used in  test<{}> call on {}".format(node.id, node.parent, node.lineno))
            self.add_usage(node.id, node.lineno)
        elif isinstance(node.parent, ast.If) and isinstance(node.ctx, ast.Load):
            self.add_usage(node.id, node.lineno)
        else:
            print("ERROR: nothing done with {} in visit_Name".format(node.id))

    def visit_Call(self, node):
        if node.func.id == 'print':
            self.add_output(node.lineno)
        self.generic_visit(node)
