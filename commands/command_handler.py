# command_handler.py
'''The CommandHandler class is responsible for loading and
executing dynamically loaded plugins'''
import os
import importlib

class CommandHandler:
    '''This class will manage the plugins'''
    def __init__(self, plugin_dir='plugins'):
        '''Initialize the CommandHandler'''
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        '''Load plugin from the plugin_dir.
        Each plugin file should correspond with its specified attribute'''
        # Look before you leap
        for root, _, files in os.walk(self.plugin_dir):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    module_name = f"{root.replace('/', '.')}.{file[:-3]}"
                    module = importlib.import_module(module_name)

                    if hasattr(module, 'COMMAND'):
                        command_class_name = module.COMMAND + "Command"
                        command_class = getattr(module, command_class_name)
                        self.plugins[module.COMMAND.lower()] = command_class

    def execute_command(self, operation, a,b):
        '''Execute the command of the operation and return the result.
        If there command is not found than return an error.'''
        if operation in self.plugins:
            command_class = self.plugins[operation]
            command = command_class(a, b)
            return command.execute()

        raise ValueError(f"Unknown operation: {operation}")
