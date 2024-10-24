# subtract.py
'''Contains the SubtractCommand class'''

from calculator.operations import subtract

COMMAND = 'subtract'
#pylint: disable=too-few-public-methods
class SubtractCommand:
    '''Subtract the inputs'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        '''Execute the inputs'''
        return subtract(self.a, self.b)
