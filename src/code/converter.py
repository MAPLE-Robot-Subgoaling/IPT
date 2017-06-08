import ast

class RewriteVars(ast.NodeTransformer):

    def __init__(self):
        super(RewriteVars, self).__init__()
        self.prev = {}
        self.nums = {}

    def get_result(self):
        return self.prev, self.nums

    def visit_Name(self, node):
        new_node = node
        if isinstance(node.ctx, ast.Store):
            if node.id not in self.prev and node.id not in self.nums:
                self.prev[node.id] = node.id
                self.nums[node.id] = 0
                new_node = node
            else:
                self.nums[node.id] += 1
                self.prev[node.id] = node.id + "_" + str(self.nums[node.id])
                new_node = ast.copy_location(ast.Name(id=self.prev[node.id], ctx=node.ctx), node)
        elif isinstance(node.ctx, ast.Load) and node.id in self.prev:
            new_node = ast.copy_location(ast.Name(id=self.prev[node.id], ctx=node.ctx), node)

        if isinstance(node.parent, ast.BinOp):
            if 'left' not in node.parent.__dict__:
                node.parent.left = new_node
            elif 'right' not in node.parent.__dict__:
                node.parent.right = new_node

        return new_node