# divide.py
'''Contains the DivdeCommand class.'''
import logging
from calculator.operations import divide

COMMAND = 'divide'
logger = logging.getLogger(__name__)

#pylint: disable=too-few-public-methods
class DivideCommand:
    '''Divide the inputs.'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        '''execute the inputs'''
        result = divide(self.a, self.b)
        logger.info("Executing DivideCommand: %s + %s = %s", self.a, self.b, result)
        return result
