# multiply.py
'''Contains the MultiplyCommand class.'''
from calculator.operations import multiply
#pylint: disable=too-few-public-methods
class MultiplyCommand:
    '''Mutiply the inputs'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        '''Execute the inputs'''
        return multiply(self.a, self.b)
