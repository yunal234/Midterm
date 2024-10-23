# operations.py
'''Contains basic operations for the calculator'''
from decimal import Decimal

def add(a,b):
    '''Add function'''
    return Decimal(a) + Decimal(b)

def subtract(a, b):
    '''Subtract function'''
    return Decimal(a) - Decimal(b)

def multiply(a, b):
    '''Multiply function'''
    return Decimal(a) * Decimal(b)

def divide(a, b):
    '''Divide function. Return an error if the division has zero'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return Decimal(a) / Decimal(b)
