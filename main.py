import tkinter as tk
from controller import AppController
from gui import ImageEditorGUI

# Main entry point of the application
if __name__ == "__main__":

# Creating the main Tkinter window
    root = tk.Tk()

# Creating the controller to handle image logic
    controller = AppController()
    
# Creating the GUI and passing the controller
    app = ImageEditorGUI(root, controller)

# Starting the Tkinter event loop
    root.mainloop()

