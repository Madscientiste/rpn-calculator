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


def calculate(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in operators:
            try:
                operand2 = stack.pop()
                operand1 = stack.pop()
            except IndexError:
                raise ValueError("Error: Not enough operands in the expression.")

            operation = operators[token]
            result = operation(operand1, operand2)
            stack.append(result)
        elif is_numeric_literal(token):
            stack.append(literal_eval(token))
        else:
            raise ValueError(f"Error: Invalid token '{token}' in the expression.")

    if len(stack) > 1:
        raise ValueError("Error: The expression was not fully evaluated.")

    return stack.pop() if stack else 0
