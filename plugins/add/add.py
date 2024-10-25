# add.py
'''This contains the AddCommand class'''
import logging
from calculator.operations import add


COMMAND = 'add'
logger = logging.getLogger(__name__)

#pylint: disable=too-few-public-methods
class AddCommand:
    '''Add the inputs'''
    def __init__(self, a, b):
        self.a = a
        self.b =b

    def execute(self):
        '''execute the inputs'''
        result = add(self.a, self.b)
        logger.info("Executing AddCommand: %s + %s = %s", self.a, self.b, result)
        return result
