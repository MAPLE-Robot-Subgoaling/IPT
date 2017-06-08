import ast


def binOpToString(binop):
    if isinstance(binop, ast.Name):
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

    return binOpToString(binop.left) + op + binOpToString(binop.right)