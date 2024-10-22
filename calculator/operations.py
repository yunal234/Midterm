# operations.py

from decimal import Decimal

def add(a,b):
    return Decimal(a) + Decimal(b)

def subtract(a, b):
    return Decimal(a) - Decimal(b)

def multiply(a, b):
    return Decimal(a) * Decimal(b)

def divide(a, b):
    if b == 0:
        raise Value Error("Cannot divide by zero")
    return Decimal(a) / Decimal(b)
