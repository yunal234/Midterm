# tests/test_calculations.py
'''Test the Calculator class history management and the execution of the commands'''

from decimal import Decimal
import pytest
from calculator.calculations import Calculator
from calculator.operations import add, subtract, multiply, divide

class TestOperation: # pylint: disable=too-few-public-methods
    '''Test operation command execution'''
    __test__ = False # added to prevent pytest class warnings
    def __init__(self, a, b, operation):
        self.a = Decimal(a)
        self.b = Decimal(b)
        self.operation = operation

    def execute(self):
        '''Execute the operation'''
        return self.operation(self.a, self.b)

def execute_operation(calculator, a, b, operation):
    '''Create and execute operation'''
    command = TestOperation(a, b, operation)
    return calculator.execute(command)

@pytest.mark.parametrize("a, b, operation, expected", [
    (2, 3, add, 5),
    (5, 3, subtract, 2),
    (4, 2, multiply, 8),
    (8, 2, divide, 4),
])
def test_calculator_operations(a, b, operation, expected):
    '''Test each operation on the calculator'''
    calculator = Calculator()
    result = execute_operation(calculator, a, b, operation)
    assert result == Decimal(expected)

def test_division_by_zero():
    '''Test division raises an error'''
    calculator = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        execute_operation(calculator, 1, 0, divide)
