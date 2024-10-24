# add.py
'''This contains the AddCommand class'''
from calculator.operations import add
#pylint: disable=too-few-public-methods
class AddCommand:
    '''Add the inputs'''
    def __init__(self, a, b):
        self.a = a
        self.b =b

    def execute(self):
        '''execute the inputs'''
        return add(self.a, self.b)
