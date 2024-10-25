# tests/test_command_handler.py

import pytest
from commands.command_handler import CommandHandler

@pytest.fixture
def command_handler():
    '''Fixture for CommandHandler object'''
    handler = CommandHandler()
    handler.load_plugins()
    return handler

def test_load_plugins(command_handler):
    '''Test that plugins are loaded correctly'''
    assert 'add' in command_handler.plugins
    assert 'subtract' in command_handler.plugins
    assert 'multiply' in command_handler.plugins
    assert 'divide' in command_handler.plugins

def test_execute_add_command(command_handler):
    '''Test executing the Add command'''
    result = command_handler.execute_command('add', 10, 5)
    assert result == 15

def test_execute_subtract_command(command_handler):
    '''Test executing the Subtract command'''
    result = command_handler.execute_command('subtract', 10, 5)
    assert result == 5

def test_execute_multiply_command(command_handler):
    '''Test executing the Multiply command'''
    result = command_handler.execute_command('multiply', 10, 5)
    assert result == 50

def test_execute_divide_command(command_handler):
    '''Test executing the Divide command'''
    result = command_handler.execute_command('divide', 10, 5)
    assert result == 2

def test_execute_divide_by_zero(command_handler):
    '''Test divide by zero error handling'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command_handler.execute_command('divide', 10, 0)

def test_unknown_command(command_handler):
    '''Test handling of unknown commands'''
    with pytest.raises(ValueError, match="Unknown operation"):
        command_handler.execute_command('modulus', 10, 5)
