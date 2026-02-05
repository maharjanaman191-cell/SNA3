import cv2
from image import Image

"""
AppController Class

This class works as a middle layer between the GUI and image processing class.

It controls how images are loaded, edited, and stored.
It also manages undo and redo operations by saving image history.
"""

# This class connects the GUI with image processing
class AppController:

    """
    Constructor that creates the image processor object
    and prepares lists to store image history for undo and redo.
    """
# Create Image object
    def __init__(self):
        self.processor = Image()
        
# Store image hitory for undo
        self.history = []

# store redo image 
        self.redo_stack = []


    """
    Loads an image from the computer and stores it inside the processor.

    Also saves the original image so undo can return to it.
    """
# load image from computer
    def load_image(self, path):
        image = cv2.imread(path)

# Save image inside image
        self.processor.set_image(image)

# Save first version of image 
        self.history = [image.copy()]
        return image
    

    """
    Saves edited image after applying any filter.

    Stores the new image in history and clears redo stack
    because a new action has been performed.
    """
# Save new image after applying a filter
    def apply(self, new_image):
        self.history.append(new_image.copy())
        self.processor.set_image(new_image)

# Clear redo when new change happens
        self.redo_stack.clear()
        return new_image
    

    """
    Returns image to previous editing state.

    Moves last image from history into redo stack.
    """
# Go back to previous image
    def undo(self):
        if len(self.history) > 1:
            self.redo_stack.append(self.history.pop())
            self.processor.set_image(self.history[-1])
        return self.processor.get_image()


    """
    Restores last undone change.

    Moves image from redo stack back into history.
    """
# Go forward to undone image
    def redo(self):
        if self.redo_stack:
            img = self.redo_stack.pop()
            self.history.append(img)
            self.processor.set_image(img)
        return self.processor.get_image()
