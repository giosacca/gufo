""" application module

A module that contains the windows required in a program that manages
job applications.
"""

import tkinter as tk

import window as w

class WindowChoice(w.Window):
    """
    A class that represents a window with a choice of the graphical
    interface.

    Attributes
    ----------

    """

    def __init__(self):

        w.Window.__init__(self)

    def make_window(self):
        """
        Executes all the methods required to make the window.
        """

        self.add_frame()
        self.set_label(self.frames[0], 'Create or load an application')
        self.add_frame()
        self.add_button(self.frames[1], 'New', self.new)
        self.add_button(self.frames[1], 'Load', self.load)
        self.show()

    def new(self):
        """
        Moves to the new window and destroys the choice window.
        """

        self.destroy()

        new = WindowNew()
        new.make_window()

    def load(self):
        """
        Moves to the load window and destroys the choice window.
        """

        self.destroy()

        load = WindowLoad()
        load.make_window()

class WindowLoad(w.Window):
    """
    A class that represents a window to load another object from the
    graphical interface.

    Attributes
    ----------

    """

    def __init__(self):

        w.Window.__init__(self)

    def make_window(self):
        """
        Executes all the methods required to make the window.
        """

        self.add_frame()
        self.set_label(self.frames[0], 'Load an application')
        self.add_frame()
        self.add_entry(self.frames[1], 0, 'uid')
        self.add_frame()
        self.add_button(self.frames[2], 'Load', self.read)
        self.show()

class WindowNew(w.Window):
    """
    A class that represents a window to create another object from the
    graphical interface.

    Attributes
    ----------

    """

    def __init__(self):

        w.Window.__init__(self)

    def add_position(self, frame):
        """
        Adds the position section to the window.

        Parameters
        ----------
        frame : tkinter.Frame
            The frame to which you want to add the checkbutton.
        """

        self.add_entry(frame, 0, 'company')
        self.add_entry(frame, 1, 'position')
        self.add_entry(frame, 2, 'position_type')
        self.add_entry(frame, 3, 'link')

    def add_documents(self, frame):
        """
        Adds the documents section to the window.

        Parameters
        ----------
        frame : tkinter.Frame
            The frame to which you want to add the checkbutton.
        """

        tk.Label(frame, text = 'Documents:').grid(row = 0, column = 0)
        self.add_checkbutton(frame, 1, 0, 'cover_letter')
        self.add_checkbutton(frame, 1, 1, 'cv')
        self.add_checkbutton(frame, 2, 0, 'master_transcript')
        self.add_checkbutton(frame, 2, 1, 'bachelor_transcript')
        self.add_checkbutton(frame, 3, 0, 'work_permit')

    def add_contact(self, frame):
        """
        Adds the contact section to the window.

        Parameters
        ----------
        frame : tkinter.Frame
            The frame to which you want to add the checkbutton.
        """

        tk.Label(frame, text = 'Contact:').grid(row = 0, column = 0)
        self.add_entry(frame, 1, 'name')
        self.add_entry(frame, 2, 'title')
        self.add_entry(frame, 4, 'job_title')
        self.add_entry(frame, 5, 'email')
        self.add_entry(frame, 5, 'phone')
        self.add_entry(frame, 6, 'linkedin')

    def make_window(self):
        """
        Executes all the methods required to make the window.
        """

        self.add_frame()
        self.set_label(self.frames[0], 'Create an application')
        self.add_frame()
        self.add_position(self.frames[1])
        self.add_frame()
        self.add_documents(self.frames[2])
        self.add_frame()
        self.add_contact(self.frames[3])
        self.add_frame()
        self.add_button(self.frames[4], 'Save', self.read)
        self.show()