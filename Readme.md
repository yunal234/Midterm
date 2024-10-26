# Midterm Project

## Overview

This project is a Python-based calculator application designed with software development practices. The application supports standard arithmetic operations, calculation history management, dynamic plugin loading, and command-line interface (REPL) for real-time interaction.


## Setup Instructions

#### Installation
Clone the repository. Use the syntax below:
```bash
git clone https://github.com/yunal234/Midterm.git
```

Install the Virtual Environment:
```bash
pip install virtualenv
```
Create and Activate the Virtual Environment:
```bash
virtualenv venv
source /venv/bin/activate <- once activated in the terminal you should see (venv) in the terminal.
```
Install the dependencies
```bash
pip install -r requirements.txt
```
Freeze installed packages
```bash
pip freeze > requirements.txt
```
Setup Environment Variables by creating a .env file in the root directory with the below plaintext:
```bash
ENVIRONMENT=DEVELOPMENT
LOG_LEVEL=DEBUG
```

## Design Pattern

The design pattern I used for my program is the **Command Pattern.**
The command pattern was used to encapsulate each operation into separate command class. This allows for easier code readability and flexibility in terms of future modification without breaking the code structure. This pattern is more maintainable.

## Environment Variable & Logging

The environment variables are used to configure the applications runtime environement and logging settings. The `logging.conf` file uses `LOG_LEVEL` to control the verbosity of the log messages. It is set to `DEBUG` for development and captures detailed log messages which is helpful for troubleshooting.

The environment variables are loaded in the `main.py` file using the function `dotenv`, this reads the configuration settings from the `.env` file. This makes the `ENVIRONMENT` and `LOG_LEVEL` accessible throughout the application.

You can find the code for the environment variable in the [main.py](https://github.com/yunal234/Midterm/blob/4286e044dd6a33f8ffa24fd53a8402b040b845c4/main.py)

Logging is used throughout the application. It is used to capture the users interaction with the calculator. The files the logging is incorporated in are `main.py`, `command_handler.py`, and plugin files located in the `plugins` folder. 
Each operation logs the user inputs and results. The logs history helps track usage and debugging.
You can find the code for logging in [logging.conf](https://github.com/yunal234/Midterm/blob/4286e044dd6a33f8ffa24fd53a8402b040b845c4/logging.conf) and [command_handler.py](https://github.com/yunal234/Midterm/blob/4286e044dd6a33f8ffa24fd53a8402b040b845c4/commands/command_handler.py)

## Exception Handling: LBYL & EAFP

Exception handling was incorporated in several parts of the code to manage potential runtime errors and improve robustness in the user experience. Easer to Ask for Forgiveness than Permission (EAFP) was used in the `calculations.py` file. The execute method in the Calculator class attempts to execute the command. If there is an error (eg. `ValueError`, `TypeError`, or `InvalidOperation`), it catches and logs the error and then the `raise` statement is used to re-throw the error to be displayed to the user.
You can find the code in the [calculations.py](https://github.com/yunal234/Midterm/blob/4286e044dd6a33f8ffa24fd53a8402b040b845c4/calculator/calculations.py)

As for Look Before You Leap (LBYL), this was used to check for conditions before performing an operation, to help avoid potential exceptions. LBYL is incorporated in the `command_handler.py` file. In this file the `load_plugins` method checks if each plugin file has a `COMMAND` attribute before loading it. This ensures that only valid plugins are loaded, preventing import errors and improves the overall function of the code.
You can find the code in the [command_handler.py](https://github.com/yunal234/Midterm/blob/4286e044dd6a33f8ffa24fd53a8402b040b845c4/commands/command_handler.py)

## Pandas

Pandas was utilized in the `history.py` file to manage the history of calculations. This allows for efficient storage and manipulation of history data, including saving, loading, clearing, and displaying the calculation history.
See the code [here](https://github.com/yunal234/Midterm/blob/4286e044dd6a33f8ffa24fd53a8402b040b845c4/calculator/history.py)

## Test

To test the functionality:
```
pytest --pylint
```
The virtual environment should be activated before running tests. The testing checks for any errors in the core functions.

## Video
The video recording showing calculator demonstration. Click [here](https://drive.google.com/file/d/1UKzCK8OrRTVKyYFL3XpKqANle7vAN0Ks/view?usp=sharing)