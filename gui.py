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

