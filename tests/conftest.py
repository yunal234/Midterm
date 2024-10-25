# conftest.py
'''Configuration for test fixtures for the calculator project'''
from decimal import Decimal
import pytest
from calculator.calculations import Calculator

@pytest.fixture
def test_data():
    '''Fixture to generate test data'''
    return [
        (Decimal(2), Decimal(3), 'add', Decimal(5)),
        (Decimal(5), Decimal(3), 'subtract', Decimal(2)),
        (Decimal(4), Decimal(2), 'multiply', Decimal(8)),
        (Decimal(8), Decimal(2), 'divide', Decimal(4))
    ]

@pytest.fixture
def test_calculator():
    '''Fixture for Calculator object'''
    calculator = Calculator()
    return calculator
