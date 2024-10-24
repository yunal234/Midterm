'''History management to keep track of calculations'''
import os
import pandas as pd

class ManageHistory:
    '''Handle calculation history using pandas'''

    def __init__(self, filename='history.csv'):
        '''Initialize the history manager with the file'''
        self.filename = filename
        self.history_df = pd.DataFrame(columns=['Operation', 'a', 'b', 'Result'])
        if not os.path.exists(self.filename):
            self.save_history()
        else:
            self.load_history()

    def show_history(self):
        '''Show the history'''
        if self.history_df.empty:
            print("No history entries found.")
        else:
            print("Displaying current history:")
            print(self.history_df.to_string(index=False))

    def add_entry(self, operation, a, b, result):
        '''Add new calculation to the history'''
        new_entry = pd.DataFrame([{'Operation': operation, 'a': a, 'b': b, 'Result': result}])
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)
        self.save_history()

    def save_history(self):
        '''Save the current history to a CSV file'''
        self.history_df.to_csv(self.filename, index=False)

    def load_history(self):
        '''Load the history from the file. Create if file does not exist'''
        try:
            self.history_df = pd.read_csv(self.filename)
        except FileNotFoundError:
            print("No history file found.")
            self.history_df = pd.DataFrame(columns=['Operation', 'a', 'b', 'Result'])

    def clear_history(self):
        '''Clear the history of the file and save'''
        self.history_df = pd.DataFrame(columns=['Operation', 'a', 'b', 'Result'])
