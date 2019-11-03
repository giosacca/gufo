""" german module

A module that contains the windows required in a program that manages
german verbs.
"""

import tkinter as tk

import window as w

class WindowVerb(w.Window):
    """
    A class that represents a window to create another object from the
    graphical interface.

    Attributes
    ----------

    """

    def __init__(self):

        w.Window.__init__(self)

    def add_verb(self, frame):
        """
        Adds the verb fields to the window.

        Parameters
        ----------
        frame : tkinter.Frame
            The frame to which you want to add the checkbutton.
        """

        self.add_entry(frame, 0, 'verb')
        self.add_entry(frame, 1, 'praposition_1')
        self.add_entry(frame, 2, 'case_1')
        self.add_entry(frame, 3, 'praposition_2')
        self.add_entry(frame, 4, 'case_2')
        self.add_entry(frame, 5, 'praposition_3')
        self.add_entry(frame, 6, 'case_3')
        self.add_entry(frame, 7, 'example')
        self.add_entry(frame, 8, 'meaning')

    def make_window(self):
        """
        Executes all the methods required to make the window.
        """

        self.add_frame()
        self.set_label(self.frames[0], 'Add a verb')
        self.add_frame()
        self.add_verb(self.frames[1])
        self.add_frame()
        self.add_button(self.frames[2], 'Save', self.read)
        self.show()