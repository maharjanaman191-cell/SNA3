import cv2
from image_processor import ImageProcessor

# This class connects the GUI with image processing
class AppController:
# Create Image object
    def __init__(self):
        self.processor = Image()
# Store image hitory for undo
        self.history = []
# store redo image 
        self.redo_stack = []

# load image from computer
    def load_image(self, path):
        image = cv2.imread(path)
# Save image inside image
        self.processor.set_image(image)
# Save first version of image 
        self.history = [image.copy()]
        return image
# Save new image after applying a filter
     def apply(self, new_image):
        self.history.append(new_image.copy())
        self.processor.set_image(new_image)
 # Clear redo when new change happens
        self.redo_stack.clear()
        return new_image
 # Go back to previous image
    def undo(self):
        if len(self.history) > 1:
            self.redo_stack.append(self.history.pop())
            self.processor.set_image(self.history[-1])
        return self.processor.get_image()

 # Go forward to undone image
    def redo(self):
        if self.redo_stack:
            img = self.redo_stack.pop()
            self.history.append(img)
            self.processor.set_image(img)
        return self.processor.get_image()