import tkinter as tk
from controller import AppController
from gui import ImageEditorGUI

"""
Main Application File

This file starts the image editor program.

It creates the main window, connects the controller and GUI together,
and starts the program so the user can interact with it.
"""

# Main entry point of the application
if __name__ == "__main__":

    """
    This section runs only when the program is started directly.

    It creates the main window, connects controller and GUI,
    and runs the Tkinter loop so the application stays open.
    """

# Creating the main Tkinter window
    root = tk.Tk()

# Creating the controller to handle image logic
    controller = AppController()
    
# Creating the GUI and passing the controller
    app = ImageEditorGUI(root, controller)

# Starting the Tkinter event loop
    root.mainloop()

