import pytest
from utils.calc import calculate


def test_addition():
    assert calculate("3 4 +") == 7


def test_subtraction():
    assert calculate("3 4 -") == -1


def test_multiplication():
    assert calculate("3 4 *") == 12


def test_division():
    assert calculate("4 2 /") == 2


def test_complex_expression_1():
    assert calculate("3 4 5 + *") == 27


def test_complex_expression_2():
    assert calculate("3 4 + 5 *") == 35


def test_complex_expression_3():
    assert calculate("3 4 + 5 6 - *") == -7


def test_float_values():
    assert calculate("3.14 2.72 +") == pytest.approx(5.86)


def test_exponentiation():
    assert calculate("3 4 ^") == 81


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("3 0 /")


def test_not_enough_operands():
    with pytest.raises(ValueError, match="Error: Not enough operands in the expression."):
        calculate("3 +")


def test_invalid_token():
    with pytest.raises(ValueError, match="Error: Invalid token 'a' in the expression."):
        calculate("3 a +")


def test_expression_not_fully_evaluated():
    with pytest.raises(ValueError, match="Error: The expression was not fully evaluated."):
        calculate("3 4 + 5")
