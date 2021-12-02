from Expression import Expression
from Value import Value

class Interpreter:
    def eval(self, c, e, known_function={}):
        cond = type(c).__name__
        # print(cond)
        if cond == "IntConstant":
            intConst = c.c
            return Value.IntValue(intConst)

        elif cond == "BinOpExpression":
            left = self.eval(c.left, e, known_function)
            right = self.eval(c.right, e, known_function)
            if c.op == Expression.BinOpExpression.Operation.PLUS:
                return Value.IntValue(left.val + right.val)
            elif c.op == Expression.BinOpExpression.Operation.MINUS:
                return Value.IntValue(left.val - right.val)
            elif c.op == Expression.BinOpExpression.Operation.TIMES:
                return Value.IntValue(left.val * right.val)
            elif c.op == Expression.BinOpExpression.Operation.DIV:
                return Value.IntValue(left.val / right.val)

        elif cond == "LetExpression":
            val = self.eval(c.value, e, known_function)
            newE = e.bind(c.variableName, val)

            return self.eval(c.body, newE, known_function)

        elif cond == "VariableExpression":
            return e.lookup(c.variable)

        elif cond == "EqExpression":
            left = self.eval(c.left, e, known_function)
            right = self.eval(c.right, e, known_function)

            if left.val == right.val:
                return Value.BoolValue(1)

            return Value.BoolValue(0)

        elif cond == "IfExpression":
            value = self.eval(c.cond, e, known_function)
            if value.val == 1:
                return self.eval(c.thenSide, e, known_function)
            return self.eval(c.elseSide, e, known_function)

        elif cond == "FunctionDeclExpression":
            def f(actualValues):
                env_that_knows_the_arguement = e
                for i in range(len(actualValues)):
                    env_that_knows_the_arguement = env_that_knows_the_arguement.bind(
                        c.formalArguments[i], actualValues[i])
                return self.eval(c.functionBody, env_that_knows_the_arguement, known_function)

            known_function[c.name.theName] = f

            return self.eval(c.scope, e, known_function)

        elif cond == "FunctionCallExpression":
            if c.name.theName in known_function:
                py_function = known_function[c.name.theName]
                actualValues = []
                for i in range(len(c.actualArguments)):
                    actualValues.append(
                        self.eval(c.actualArguments[i], e, known_function))
                return py_function(actualValues)
            else:
                raise Exception("Function Not Exist")

    def apply(self):
        raise Exception ("I don't know the expression")
