""" test_window module

A module to test the window module.
"""

import pytest

import context
import window as w

@pytest.fixture(scope = 'module')
def window():
    """
    Creates a Window object for the tests.
    """

    win = w.window.Window()

    return win

def test_window(window):
    """
    Tests the constructor of the Window class.

    Parameters
    ----------
    window : window.window.Window
        The Window object to be tested.
    """

    assert window.frames == []
    assert window.fields == {}
    assert window.checks == {}

def test_add_frame(window):
    """
    Test the add_frame() method.

    Parameters
    ----------
    window : window.window.Window
        The Window object to be tested.
    """

    window.add_frame()
    assert len(window.frames) == 1

    window.add_frame()
    assert len(window.frames) == 2

    window.add_frame()
    assert len(window.frames) == 3

def test_add_button(window):
    """
    Test the add_button() method.

    Parameters
    ----------
    window : window.window.Window
        The Window object to be tested.
    """

    window.add_button(window.frames[0], 'Quit', 'quit')
    assert 'Quit' in window.buttons.keys()

def test_add_entry(window):
    """
    Test the add_entry() method.

    Parameters
    ----------
    window : window.window.Window
        The Window object to be tested.
    """

    window.add_entry(window.frames[1], 0, 'test')
    assert 'test' in window.fields.keys()

def test_add_checkbutton(window):
    """
    Test the add_checkbutton() method.

    Parameters
    ----------
    window : window.window.Window
        The Window object to be tested.
    """

    window.add_checkbutton(window.frames[2], 0, 0, 'test')
    assert 'test' in window.checks.keys()