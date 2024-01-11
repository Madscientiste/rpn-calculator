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
    result = []

    for token in tokens:
        if token in operators:
            if len(result) < 2:
                raise ValueError("Error: Not enough operands in the expression.")
            func = operators[token]
            result[-2:] = [func(result[-2], result[-1])]
        elif is_numeric_literal(token):
            result.append(literal_eval(token))
        else:
            raise ValueError(f"Error: Invalid token '{token}' in the expression.")

    if len(result) > 1:
        raise ValueError("Error: The expression was not fully evaluated.")

    return result[0] if result else 0
