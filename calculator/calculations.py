# calculations.py

class calculator:
    def __init__(self):
        self.history = []

    def execute(self, command):
        result = command.execute()
        self.history.append((command.__class__.__name__, command.a, command.b, result))
        return result

    def get_history(self):
        return self.history
