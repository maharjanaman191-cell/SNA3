import cv2
import numpy as np

"""
Image Class

This class handles all image processing operations using OpenCV.

It stores the image and provides functions to apply different
editing effects such as grayscale, blur, edge detection,
brightness, contrast, rotation, flipping and resizing.
"""
 # This class does all image editing work using OpenCV
class Image:
   
    """
    This constructor runs when the class is created.
    It stores the image inside the class so it can be used later.
    """
# It stores the image inside the class  
    def __init__(self, image=None):
        self.image = image
     
    """
    Stores a new image inside the class.
    """
# Save a new image into the class
    def set_image(self, image):
        self.image = image

    """
    Returns the current image stored in the class.
    """
# Return the current image
    def get_image(self):
        return self.image
    
    """
    Converts the image into black and white.
    """
# Change the image to black and white
    def grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
     
    """
    Applies blur effect to make the image smoother.
    """
# Apply blur to the image
    def blur(self, intensity): 
        k = max(1, int(intensity) * 2 + 1)
        return cv2.GaussianBlur(self.image, (k, k), 0)

    """
    Detects edges in the image to highlight object boundaries.
    """
# Find edges in the image
    def edge_detection(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)
    
    """
    Changes brightness of the image.
    Positive values increase brightness and negative values decrease it.
    """
# Increase or decrease brightness
    def adjust_brightness(self, value):
        return cv2.convertScaleAbs(self.image, alpha=1, beta=value)
   
    """
    Adjusts contrast of the image.
    Higher value increases contrast difference.
    """
# Change image contrast
    def adjust_contrast(self, value):
        alpha = value / 50
        return cv2.convertScaleAbs(self.image, alpha=alpha, beta=0)

    """
    Rotates the image based on selected angle.
    """
# Rotate image based on selected angle
    def rotate(self, angle):
        if angle == 90:
            return cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            return cv2.rotate(self.image, cv2.ROTATE_180)
        elif angle == 270:
            return cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    """
    Flips the image horizontally or vertically like a mirror.
    """
#  Flip image left-right or up-down
    def flip(self, mode):
        if mode == "Horizontal":
            return cv2.flip(self.image, 1)
        elif mode == "Vertical":
            return cv2.flip(self.image, 0)

    """
    Resizes the image using scale percentage.
    """
# Resize image using scale value
    def resize(self, scale):
        width = int(self.image.shape[1] * scale)
        height = int(self.image.shape[0] * scale)
        return cv2.resize(self.image, (width, height))   

    