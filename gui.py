import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

class ImageEditorGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
# Setting the title and size of the application window
        self.root.title("HIT137 Image Editor")
        self.root.geometry("1000x600")
        
# Main frame that holds all other components     
        self.main = tk.Frame(self.root)
        self.main.pack(fill=tk.BOTH, expand=True)

# Left side frame used to display the image      
        self.canvas_frame = tk.Frame(self.main, bg="black")
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
 # Canvas where the image is shown
        self.canvas = tk.Canvas(self.canvas_frame, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
# Right side panel that contains buttons and sliders
        self.control_panel = tk.Frame(self.main, width=220)
        self.control_panel.pack(side=tk.RIGHT, fill=tk.Y)
        
# Status bar to show image information
        self.status = tk.Label(
            self.root,
            text="No image loaded",
            bd=1,
            relief=tk.SUNKEN
        )
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.create_menu()
        self.create_controls()
        
    def create_menu(self):
        menu = tk.Menu(self.root)
 # File menu options
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save As", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
# Edit menu options
        edit_menu = tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Edit", menu=edit_menu)

 # Adding menus to the menu bar
        self.root.config(menu=menu)

    def create_controls(self):
 # Button to convert image to grayscale
        tk.Button(self.control_panel, text="Grayscale",command=self.grayscale).pack(fill=tk.X, padx=5, pady=2)
        
# Button to blur the image        
        tk.Button(self.control_panel, text="Blur",command=lambda: self.blur(5)).pack(fill=tk.X, padx=5, pady=2)
        
 # Button to detect edges in the image
        tk.Button(self.control_panel, text="Edges",command=self.edges).pack(fill=tk.X, padx=5, pady=2)
        
# Button to rotate the image by 90 degrees
        tk.Button(self.control_panel, text="Rotate 90°",command=lambda: self.rotate(90)).pack(fill=tk.X, padx=5, pady=2)
        
# Button to flip the image horizontally
        tk.Button(self.control_panel, text="Flip Horizontal",command=lambda: self.flip("Horizontal")).pack(fill=tk.X, padx=5, pady=2)
        
# Slider to control brightness level
        tk.Label(self.control_panel, text="Brightness").pack(pady=(10, 0))
        self.brightness = tk.Scale(
            self.control_panel,
            from_=-100, to=100,
            orient=tk.HORIZONTAL,
            command=self.adjust_brightness
        )
        self.brightness.pack(fill=tk.X, padx=5)
        
# Slider to control contrast level
        tk.Label(self.control_panel, text="Contrast").pack(pady=(10, 0))
        self.contrast = tk.Scale(
            self.control_panel,
            from_=1, to=100,
            orient=tk.HORIZONTAL,
            command=self.adjust_contrast
        )
        self.contrast.pack(fill=tk.X, padx=5)
        
    def display(self, image):
        
# Convert image from OpenCV format to Tkinter format     
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        
# Getting canvas width and height
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        
# Resize image to fit inside the canvas       
        if canvas_w > 1 and canvas_h > 1:
            img.thumbnail((canvas_w, canvas_h))

        self.tk_img = ImageTk.PhotoImage(img)
        
# Clearing previous image and displaying new one
        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_w // 2,
            canvas_h // 2,
            image=self.tk_img,
            anchor=tk.CENTER
        )
# Displaying image size in the status bar      
        h, w = image.shape[:2]
        self.status.config(text=f"Image Size: {w} x {h}")
        
    def open_image(self):
        
# Opens file dialog to select an image
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.png *.bmp")]
        )
        if path:
            image = self.controller.load_image(path)
            self.display(image)

    def save_image(self):
        
# Saves the edited image to selected location
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            cv2.imwrite(path, self.controller.processor.get_image())
            messagebox.showinfo("Saved", "Image saved successfully")
            
# Converts image to grayscale
    def grayscale(self):
        img = self.controller.processor.grayscale()
        self.display(
            self.controller.apply(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR))
        )
# Applies blur effect to the image
    def blur(self, value):
        img = self.controller.processor.blur(value)
        self.display(self.controller.apply(img))
        
# Detects edges in the image
    def edges(self):
        img = self.controller.processor.edge_detection()
        self.display(
            self.controller.apply(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR))
        )
        
# Rotates image by given angle
    def rotate(self, angle):
        img = self.controller.processor.rotate(angle)
        self.display(self.controller.apply(img))
        
# Applies blur effect to the image
    def flip(self, mode):
        img = self.controller.processor.flip(mode)
        self.display(self.controller.apply(img))
        
# Adjusts brightness using slider value
    def adjust_brightness(self, value):
        img = self.controller.processor.adjust_brightness(int(value))
        self.display(img)
        
# Adjusts contrast using slider value
    def adjust_contrast(self, value):
        img = self.controller.processor.adjust_contrast(int(value))
        self.display(img)
        
# Reverts to the previous image state
    def undo(self):
        self.display(self.controller.undo())
        
# Restores the last undone action
    def redo(self):
        self.display(self.controller.redo())


