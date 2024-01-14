import operator
from ast import literal_eval

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}


def is_numeric_literal(token):
    try:
        literal_eval(token)
        return True
    except (ValueError, SyntaxError):
        return False


class CalculatorError(Exception):
    pass


def calculate(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in operators:
            try:
                operand2 = stack.pop()
                operand1 = stack.pop()
            except IndexError:
                raise CalculatorError("Not enough operands in the expression.")

            operation = operators[token]
            result = operation(operand1, operand2)
            stack.append(result)
        elif is_numeric_literal(token):
            stack.append(literal_eval(token))
        else:
            raise CalculatorError(f"Invalid token '{token}' in the expression.")

    if len(stack) > 1:
        raise CalculatorError(
            "Too many operands. The expression contains more numbers than can be evaluated with the provided operators."
        )

    return stack.pop() if stack else 0
