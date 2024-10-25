# main.py
'''REPL interface for user interaction'''
import os
import logging
import logging.config
from dotenv import load_dotenv
from calculator.calculations import Calculator
from commands.command_handler import CommandHandler

load_dotenv()

log_file_path = os.getenv('LOG_FILE_PATH', 'logs/calculator.log')
log_dir = os.path.dirname(log_file_path)

'''Make sure the log directory exits and if it doesnt, create it'''
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

logger.info("Logging setup complete")

def show_menu(handler):
    '''Display the menu with list of operations'''
    print("\nChoose an operation:")
    for command in handler.plugins:
        print(f"- {command}")
    print("\nType 'history' to see your calculation history.")
    print("Type 'clear' to clear history.")
    print("Type 'save' to save your inputs.")
    print("\nType 'exit' to quit the calculator application.")

def process_history_commands(operation, calculator):
    '''process the history command operations'''
    if operation == 'history':
        calculator.history.show_history()
        logger.info("History displayed: \n%s", calculator.history.history_df)
    elif operation == 'save':
        calculator.save_history()
        print("History saved.")
        logger.info("History saved")
    elif operation == 'load':
        calculator.load_history()
        print("History loaded.")
        logger.info("History loaded")
    elif operation == 'clear':
        calculator.clear_history()
        print("History cleared.")
        logger.info("History cleared")
    else:
        print("Unknown history command.")
        logger.warning("Unknown command: %s", operation)

def main():
    '''Run the calculator REPL loop'''
    print("Current working directory:", os.getcwd())
    calculator = Calculator()
    handler = CommandHandler()
    handler.load_plugins()

    show_menu(handler)

    while True:
        operation = input("\nEnter operation: ").strip().lower()

        if operation == 'exit':
            logger.info("Exiting calculator")
            break

        if operation in ['history', 'save', 'load', 'clear']:
            process_history_commands(operation, calculator)
            continue

        a = input("Enter first number: ").strip()
        b = input("Enter second number: ").strip()

        try:
            result = handler.execute_command(operation, a, b)
            print(f"Result: {result}")
            logger.info("Operation: %s, Inputs: %s, %s, Result: %s", operation, a, b, result)

            calculator.history.add_entry(operation, a, b, result)

        except ValueError as e:
            print(f"Error: {e}")
            logger.error("ValueError: %s", e)
        except ZeroDivisionError as e:
            print(f"Invalid. Cannot divide by zero: {e}")

if __name__ == "__main__":
    main()
