import ast

exempt_names = ['main'] + ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

class RewriteVars(ast.NodeTransformer):

    def __init__(self):
        super(RewriteVars, self).__init__()
        self.prev = {}
        self.nums = {}

        self.next = {}
        self.known_vars = []

        self.paused = []

    def get_result(self):
        return self.prev, self.nums

    def visit_While(self, node):

        # visit the node normally
        self.generic_visit(node)

        #remove all paused names
        self.paused = []

        # done with special case
        return node

    def visit_If(self, node):
        print("Visiting If")
        self.generic_visit(node)
        return node

    def visit_Name(self, node, **kwargs):
        new_node = node

        #print(vars(node))

        # all these checks are for the test in a while loop
        # we have to pause the update of variable names to make it work

        # while test is just this name
        if isinstance(node.parent, ast.While):
            self.paused.append(node.id)

        # while test is a just a binop
        if isinstance(node.parent, ast.BinOp) and isinstance(node.parent.parent, ast.While):
            self.paused.append(node.id)

        # while test is just a single comparison
        if isinstance(node.parent, ast.Compare) and isinstance(node.parent.parent, ast.While):
            self.paused.append(node.id)

        # while test is a boolop with just names
        if isinstance(node.parent, ast.BoolOp) and isinstance(node.parent.parent, ast.While):
            self.paused.append(node.id)

        if node.id in exempt_names or node.id in self.paused:
            return new_node

        if isinstance(node.ctx, ast.Store):
            if node.id not in self.known_vars:
                self.known_vars.append(node.id)
                self.nums[node.id] = 0
                self.prev[node.id] = node.id
                self.next[node.id] = node.id
            else:
                self.nums[node.id] += 1
                self.prev[node.id] = self.next[node.id]
                self.next[node.id] = node.id + "_" + str(self.nums[node.id])
                new_node = ast.copy_location(ast.Name(id=self.next[node.id], ctx=node.ctx), node)

        elif isinstance(node.ctx, ast.Load):
            if isinstance(node.parent, ast.Assign):
                new_node = ast.copy_location(ast.Name(id=self.prev[node.id], ctx=node.ctx), node)
            else:
                new_node = ast.copy_location(ast.Name(id=self.next[node.id], ctx=node.ctx), node)

        #if its a binop then you need to reset the left and right parents
        if isinstance(node.parent, ast.BinOp):
            if 'left' not in node.parent.__dict__:
                node.parent.left = new_node
            elif 'right' not in node.parent.__dict__:
                node.parent.right = new_node

        return new_node
