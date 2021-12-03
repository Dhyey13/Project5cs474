class Expression:

    # constant integer
    class IntConstant:
        def __init__(self, c):
            self.c = c
    # binary operator expressions
    class BinOpExpression:
        class Operation:
            PLUS = 1
            MINUS = 2
            TIMES = 3
            DIV = 4

        def __init__(self, op, left, right):
            self.left = left
            self.right = right
            self.op = op
    # let expression
    class LetExpression:
        def __init__(self, variableName, value, body):
            self.variableName = variableName
            self.value = value
            self.body = body
    # variable class expression
    class VariableExpression:
        def __init__(self, variable):
            self.variable = variable
    # equal expression
    class EqExpression:
        def __init__(self, left, right):
            self.left = left
            self.right = right
    # if expression
    class IfExpression:
        def __init__(self, cond, thenSide, elseSide):
            self.cond = cond
            self.thenSide = thenSide
            self.elseSide = elseSide
    # function declaration expression
    class FunctionDeclExpression:
        def __init__(self, name, formalArguments, functionBody, scope):
            self.name = name
            self.formalArguments = formalArguments
            self.functionBody = functionBody
            self.scope = scope 
    # function call expression
    class FunctionCallExpression:
        def __init__(self, name, actualArguments):
            self.name = name
            self.actualArguments = actualArguments
