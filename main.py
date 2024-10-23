# main.py

from decimal import Decimal
from commands.add import AddCommand
from commands.subtract import SubtractCommand
from commands.multiply import MultiplyCommand
from commands.divide import DivideCommand
from calculator.calculations import Calculator

def show_menu():
    print("\nChoose an operation: Add, Subtract, Multiply, Divide")
    print("Type 'exit' to quit the calculator application."

def main():
    calculator = Calculator()

    while True:
        show_menu()
        operation = input("Enter operation: ").strip().lower()

        if operation == 'exit':
            break

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

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

