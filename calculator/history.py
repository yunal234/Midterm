# history.py
'''History management to keep track of calculations'''
import pandas as pd

class ManageHistory:
    '''Handle calculation history using pandas'''

    def __init__(self, filename='history.csv'):
        '''Initialize the history manager with the file'''
        self.filename = filename
        self.history_df = self.load_history()

    def add_entry(self, operation, a, b, result):
        '''Add new calculation to the history'''
        new_entry = {'Operation': operation, 'a': a, 'b': b, 'Result': result}
        self.history_df = self.history_df.append(new_entry, ignore_index=True)
        self.save_history()

    def save_history(self):
        '''Save the current history to a CSV file'''
        self.history_df.to_csv(self.filename, index=False)

    def load_history(self):
        '''Load the history from the file. Create if file does not exist'''
        try:
            return pd.read_csv(self.filename)
        except FileNotFoundError:
            return pd.DataFrame(columns=['Operation', 'a', 'b', 'Result'])

    def show_history(self):
        '''show the history'''
        print(self.history_df)

    def clear_history(self):
        '''Clear the history of the file and save'''
        self.history_df = pd.DataFrame(columns=['Operation', 'a', 'b', 'Result'])
        self.save_history()

    def get_history(self):
        '''return the history data frame'''
        return self.history_df
