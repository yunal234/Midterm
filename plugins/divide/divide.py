# divide.py
'''Contains the DivdeCommand class.'''

from calculator.operations import divide

COMMAND = 'divide'
#pylint: disable=too-few-public-methods
class DivideCommand:
    '''Divide the inputs.'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        '''execute the inputs'''
        return divide(self.a, self.b)
