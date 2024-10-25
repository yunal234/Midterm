# subtract.py
'''Contains the SubtractCommand class'''
import logging
from calculator.operations import subtract

COMMAND = 'subtract'
logger = logging.getLogger(__name__)

#pylint: disable=too-few-public-methods
class SubtractCommand:
    '''Subtract the inputs'''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        '''Execute the inputs'''
        result = subtract(self.a, self.b)
        logger.info("Executing SubtractCommand: %s + %s = %s", self.a, self.b, result)
        return result
