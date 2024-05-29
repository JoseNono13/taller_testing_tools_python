import pytest

from taller_testing_tools_python.app.calculator import Calculator
from taller_testing_tools_python.app.exceptions import MathematicalException

@pytest.fixture()
def calculator() -> Calculator:
    return Calculator()

@pytest.mark.parametrize('operation, result_expected', [
    ((1,2,'add'), 3),
    ((1,2,'substraction'), -1),
    ((1,2,'multiplication'), 2),
    ((1,2,'division'), 0),
])
def test_calculator_is_working(operation, result_expected, calculator: Calculator):
    assert calculator.calculate(operation) == result_expected

def test_calculator_error_division_by_zero(calculator: Calculator):

    with pytest.raises(MathematicalException, match='The mathematical operation is not correct: .*'):
    assert calculator.calculate(0,0,'division')