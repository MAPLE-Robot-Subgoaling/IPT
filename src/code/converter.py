import ast

exempt_names = list(dir(__builtins__)) + ["main", "print", "range"]

class RewriteVars(ast.NodeTransformer):

    def __init__(self):
        super(RewriteVars, self).__init__()
        self.prev = {}
        self.nums = {}

        self.next = {}
        self.known_vars = []

    def get_result(self):
        return self.prev, self.nums

    def visit_Name(self, node):
        new_node = node

        if node.id in exempt_names:
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
