# main.py
'''REPL interface for user interaction'''
from calculator.calculations import Calculator
from commands.command_handler import CommandHandler

def show_menu(handler):
    '''Display the menu with list of operations'''
    print("\nChoose an operation:")
    print("\nAdd\nSubtract\nMultiply\nDivide")
    for command in handler.plugins:
        print(f"- {command.capitalize()} (plugin)")
    print("\nType 'history' to see your calculation history.")
    print("\nType 'exit' to quit the calculator application.")

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
    handler = CommandHandler()
    handler.load_plugins()

    while True:
        show_menu(handler)
        operation = input("\nEnter operation: ").strip().lower()

        if operation == 'exit':
            break

        if operation in ['history', 'save', 'load', 'clear']:
            process_history_commands(operation, calculator)
            continue

        a = input("Enter first number: ").strip()
        b = input("Enter second number: ").strip()

        try:
            result = handler.execute_command(operation, a, b)
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Invalid. Cannot divide by zero: {e}")

if __name__ == "__main__":
    main()
