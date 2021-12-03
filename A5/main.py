from Expression import Expression
from Environment import Environment
from Interpreter import Interpreter
from Name import Name

class main:

    # 474
    # integer constant
    # Similar to p1 in professor's version
    p1 = Expression.IntConstant(474)

    # 400 + (10 * 4)
    # binary operations
    # Similar to p2 in professor's version
    p2 = Expression.BinOpExpression(
        Expression.BinOpExpression.Operation.PLUS,
        Expression.IntConstant(400),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.TIMES,
            Expression.IntConstant(10),
            Expression.IntConstant(4)
        )
    )

    # (let v1 = 400 in
    #    (let v2 = 70 in v2)
    #    +
    #    4 + v1
    # )
    # introducing and reading variables (let, var)
    # Similar to p5 in professor's version
    p3 = Expression.LetExpression(
        Name("v1"),
        Expression.IntConstant(400),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.LetExpression(
                Name("v2"),
                Expression.IntConstant(70),
                Expression.VariableExpression(Name("v2"))
            ),
            Expression.BinOpExpression(
                Expression.BinOpExpression.Operation.PLUS,
                Expression.IntConstant(4),
                Expression.VariableExpression(Name("v1"))
            )
        )
    )
    # (let divisor = 1 in (divisor == 1))
    # Comparison
    # Similar to p8 in professor's version
    p4 = Expression.LetExpression(
        Name("divisor"),
        Expression.IntConstant(1),
        Expression.EqExpression(
            Expression.VariableExpression(Name("divisor")),
            Expression.IntConstant(1)
        )
    )

#      (let dividend = 474 in
#        (let divisor = 2 in
#          (divisor == 0) ? 0 : dividend / divisor))
#      Conditional execution
#      Similar to p9 in professor's version
    p5 = Expression.LetExpression(
        Name("dividend"),
        Expression.IntConstant(474),
        Expression.LetExpression(
            Name("divisor"),
            Expression.IntConstant(2),
            Expression.IfExpression(
                Expression.EqExpression(
                    Expression.VariableExpression(Name("divisor")),
                    Expression.IntConstant(0)
                ),
                Expression.IntConstant(0),
                Expression.BinOpExpression(
                    Expression.BinOpExpression.Operation.DIV,
                    Expression.VariableExpression(Name("dividend")),
                    Expression.VariableExpression(Name("divisor"))
                )
            )
        )
    )
    # function safeDivision(dividend, divisor) -> (divisor == 0) ? 0 : dividend / divisor))
    # safeDivision(400 + 74,0) + safeDivision(474,1)
    # function definition and invocation
    # similar to p10 in professor's version
    p6 = Expression.FunctionDeclExpression(
        Name("safeDivision"),
        [Name("dividend"),  Name("divisor")],
        Expression.IfExpression(
            Expression.EqExpression(
                Expression.VariableExpression(Name("divisor")),
                Expression.IntConstant(0)
            ),
            Expression.IntConstant(0),
            Expression.BinOpExpression(
                Expression.BinOpExpression.Operation.DIV,
                Expression.VariableExpression(Name("dividend")),
                Expression.VariableExpression(Name("divisor"))
            )
        ),
        Expression.BinOpExpression(
            Expression.BinOpExpression.Operation.PLUS,
            Expression.FunctionCallExpression(
                Name("safeDivision"),
                [
                    Expression.BinOpExpression(
                        Expression.BinOpExpression.Operation.PLUS,
                        Expression.IntConstant(400),
                        Expression.IntConstant(74)
                    ),
                    Expression.IntConstant(0)
                ]
            ),
            Expression.FunctionCallExpression(
                Name("safeDivision"),
                [
                    Expression.IntConstant(474),
                    Expression.IntConstant(2)
                ]
            )
        )
    )

    @staticmethod
    def main():
        environment = Environment(None, None)
        print(Interpreter().eval(main.p2, environment, {}))

main.main()