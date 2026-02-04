import tkinter as tk
from controller import AppController
from gui import ImageEditorGUI

if __name__ == "__main__":
    root = tk.Tk()
    controller = AppController()
    app = ImageEditorGUI(root, controller)
    root.mainloop()

