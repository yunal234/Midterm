# calculations.py
'''Contains the Calculator class which manages the calculations and history.'''
from decimal import InvalidOperation
from calculator.history import ManageHistory

class Calculator:
    '''Calculator class will perform the calculations and store the history.'''
    def __init__(self):
        '''Initialize history class.'''
        self.history = ManageHistory()

    def execute(self, command):
        '''Execute the commands and store the history to result and 
        return the result of the executed command.'''
        try:
            result = command.execute()
            self.history.add_entry(command.__class__.__name__, command.a, command.b, result)
            return result
        except (ValueError, TypeError, InvalidOperation) as e:
            print(f"Error executing command: {e}")
            raise

    def show_history(self):
        '''show the history'''
        self.history.show_history()

    def save_history(self):
        '''save the history'''
        self.history.save_history()

    def load_history(self):
        '''load the history'''
        self.history.load_history()

    def clear_history(self):
        '''clear the history'''
        self.history.clear_history()
