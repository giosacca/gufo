""" windows module

A module to design a gui for entering simple data.
"""

import tkinter as tk

class Window(tk.Tk):
    """
    A class that represents a general window of the graphical
    interface.

    Attributes
    ----------
    self.frames : list
        A list of frames from top to bottom.
    self.fields : dict
        A dict of the fields to read.
    self.checks : dict
        A dict of the checks to read.
    """

    def __init__(self):

        tk.Tk.__init__(self)

        self.frames = []
        self.fields = {}
        self.checks = {}

    def add_frame(self):
        """
        Makes the frame for the window.
        """

        self.frames.append(tk.Frame(self, width = 500))
        self.frames[-1].pack(anchor = 'c', padx = 10, pady = 2)

    def set_label(self, frame, text):
        """
        Sets a label for the window.
        """

        self.label = tk.Label(
            frame,
            text = text,
            )
        self.label.pack(padx = 10, pady = 10)

    def add_button(self, frame, text, command):
        """
        Adds a button to the window.

        Parameters
        ----------
        frame : tkinter.Frame
            The frame to which you want to add the label.
        text : string
            The message to display on the button.
        command : string
            The method to be executed when the button is pressed.
        """

        self.button = tk.Button(
            frame,
            text = text, 
            fg = 'black',
            command = command,
            width = 5,
        )
        self.button.pack(side = tk.constants.LEFT)

    def show(self):
        """
        Shows the window.
        """

        self.mainloop()

    def add_entry(self, frame, row, field):
        """
        Adds an entry to the window.

        Parameters
        ----------
        frame : tkinter.Frame
            The frame to which you want to add the entry.
        row : int
            The row for the entry.
        field : string
            The message to display next to the entry field.
        """

        self.field = tk.Label(frame, text = field)
        self.field.grid(row = row, column = 0)
    
        self.fields[field] = tk.Entry(frame)
        self.fields[field].grid(row = row, column = 1)

    def add_checkbutton(self, frame, row, column, field):
        """
        Adds a checkbutton to the window.

        Parameters
        ----------
        frame : tkinter.Frame
            The frame to which you want to add the checkbutton.
        row : int
            The row for the checkbutton.
        column : int
            The column for the checkbutton.
        field : string
            The message to display next to the checkbutton field.
        """

        self.checks[field] = tk.BooleanVar()

        self.field = tk.Checkbutton(
            frame,
            text = field,
            var = self.checks[field]
            )
        self.field.grid(
            row = row,
            column = column,
            sticky = tk.constants.W,
            )

    def read(self):
        """
        Reads the data in the window.
        """

        for key in self.fields:
            print('{}: {}'.format(key, self.fields[key].get()))

        for key in self.checks:
            print('{}: {}'.format(key, self.checks[key].get()))

        self.destroy()
        