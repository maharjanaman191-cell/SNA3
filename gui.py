import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

class ImageEditorGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("HIT137 Image Editor")
        self.root.geometry("1000x600")
        
         self.main = tk.Frame(self.root)
        self.main.pack(fill=tk.BOTH, expand=True)
        
        self.canvas_frame = tk.Frame(self.main, bg="black")
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.control_panel = tk.Frame(self.main, width=220)
        self.control_panel.pack(side=tk.RIGHT, fill=tk.Y)

        self.status = tk.Label(
            self.root,
            text="No image loaded",
            bd=1,
            relief=tk.SUNKEN
        )
        self.status.pack(side=tk.BOTTOM, fill=tk.X)


