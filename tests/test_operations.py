# tests/test_operations.py
'''test the operations'''
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    '''Test addition operation'''
    assert add(3, 2) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

def test_subtract():
    '''Test subtraction operation'''
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(-1, -5) == 4

def test_multiply():
    '''Test multiplication operation'''
    assert multiply(4, 2) == 8
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5

def test_divide():
    '''Test division operation'''
    assert divide(8, 2) == 4
    assert divide(-10, 5) == -2

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
