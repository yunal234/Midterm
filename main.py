# main.py
'''REPL interface for user interaction'''
from commands.add import AddCommand
from commands.subtract import SubtractCommand
from commands.multiply import MultiplyCommand
from commands.divide import DivideCommand
from calculator.calculations import Calculator

def show_menu():
    '''Display the menu with list of operations'''
    print("\nChoose an operation: Add, Subtract, Multiply, Divide")
    print("Type 'history' to see calculation history.")
    print("Type 'save' to save history, 'load' to load history, 'clear' to clear the history.")
    print("Type 'exit' to quit the calculator application.")

def process_history_commands(operation, calculator):
    '''process the history command operations'''
    if operation == 'history':
        calculator.show_history()
    elif operation == 'save':
        calculator.save_history()
        print("History saved.")
    elif operation == 'load':
        calculator.load_history()
        print("History loaded.")
    elif operation == 'clear':
        calculator.clear_history()
        print("History cleared.")
    else:
        print("Unknown history command.")

def main():
    '''Run the calculator REPL loop'''
    calculator = Calculator()

    while True:
        show_menu()
        operation = input("Enter operation: ").strip().lower()

        if operation == 'exit':
            break

        if operation in ['history', 'save', 'load', 'clear']:
            process_history_commands(operation, calculator)
            continue

        a = input("Enter first number: ").strip()
        b = input("Enter second number: ").strip()

        try:
            if operation == 'add':
                command = AddCommand(a, b)
            elif operation == 'subtract':
                command = SubtractCommand(a, b)
            elif operation == 'multiply':
                command = MultiplyCommand(a, b)
            elif operation == 'divide':
                command = DivideCommand(a, b)
            else:
                print("Unknown Operation. Please choose an operation from the menu")
                continue

            result = calculator.execute(command)
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Invalid. Cannot divide by zero: {e}")

if __name__ == "__main__":
    main()
