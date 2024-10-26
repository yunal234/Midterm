# multiply.py
'''Contains the MultiplyCommand class.'''
import logging
from calculator.operations import multiply

COMMAND = 'multiply'
logger = logging.getLogger(__name__)
#pylint: disable=too-few-public-methods
class MultiplyCommand:
    '''Mutiply the inputs'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        '''Execute the inputs'''
        result = multiply(self.a, self.b)
        logger.info("Executing MultiplyCommand: %s + %s = %s", self.a, self.b, result)
        return result
