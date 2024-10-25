'''Test for the ManageHistory function'''

import os
import pytest
from calculator.history import ManageHistory

@pytest.fixture(scope="function")
def history_file():
    '''Provide a clean test file setup and teardown after each test'''
    filename = 'test_history.csv'
    if os.path.exists(filename):
        os.remove(filename)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

def test_add_entry(history_file):
    '''Test adding an entry to the history'''
    history = ManageHistory(history_file)
    history.add_entry('add', 2, 3, 5)

    assert not history.history_df.empty
    assert history.history_df.iloc[-1].to_dict() == {
        'Operation': 'add', 'a': 2, 'b': 3, 'Result': 5}

def test_clear_history(history_file):
    '''Test clearing the history'''
    history = ManageHistory(history_file)
    history.add_entry('add', 2, 3, 5)
    history.clear_history()

    assert history.history_df.empty

def test_load_history(history_file):
    '''Test loading history from a file'''
    history = ManageHistory(history_file)
    history.add_entry('subtract', 5, 3, 2)
    history.save_history()

    new_history = ManageHistory(history_file)
    assert not new_history.history_df.empty
    assert new_history.history_df.iloc[-1].to_dict() == {
        'Operation': 'subtract', 'a': 5, 'b': 3, 'Result': 2}

def test_save_history_creates_file(history_file):
    '''Test that save_history creates a file if one does not exist'''
    history = ManageHistory(history_file)
    history.save_history()
    assert os.path.exists(history_file)

def test_load_empty_history_when_file_missing(history_file):
    '''Test loading history when file is missing initializes an empty history'''
    if os.path.exists(history_file):
        os.remove(history_file)
    history = ManageHistory(history_file)
    assert history.history_df.empty
