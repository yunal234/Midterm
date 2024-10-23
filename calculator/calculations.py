# calculations.py
'''Contains the Calculator class which manages the calculations and history.'''
class Calculator:
    '''Calculator class will perform the calculations and store the history.'''
    def __init__(self):
        '''Initialize the empty history list.'''
        self.history = []

    def execute(self, command):
        '''Execute the commands and store the history to result and 
        return the result of the executed command.'''
        result = command.execute()
        self.history.append((command.__class__.__name__, command.a, command.b, result))
        return result

    def get_history(self):
        '''Get the history of the calculations and return the list of each calculation.'''
        return self.history
