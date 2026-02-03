import cv2
import numpy as np

 # This class does all image editing work using OpenCV

class Image:
   
        # It stores the image inside the class  
    def __init__(self, image=None):
        self.image = image
     
  # Save a new image into the class
    def set_image(self, image):
        self.image = image

# Return the current image
    def get_image(self):
        return self.image
    
 # Change the image to black and white
    def grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
     
     # Apply blur to the image
    def blur(self, intensity): 
        k = max(1, int(intensity) * 2 + 1)
        return cv2.GaussianBlur(self.image, (k, k), 0)

   # Find edges in the image
    def edge_detection(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)
    
       # Increase or decrease brightness
    def adjust_brightness(self, value):
        return cv2.convertScaleAbs(self.image, alpha=1, beta=value)
   
    # Change image contrast
    def adjust_contrast(self, value):
        alpha = value / 50
        return cv2.convertScaleAbs(self.image, alpha=alpha, beta=0)

# Rotate image based on selected angle
    def rotate(self, angle):
        if angle == 90:
            return cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            return cv2.rotate(self.image, cv2.ROTATE_180)
        elif angle == 270:
            return cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)

#  Flip image left-right or up-down
    def flip(self, mode):
        if mode == "Horizontal":
            return cv2.flip(self.image, 1)
        elif mode == "Vertical":
            return cv2.flip(self.image, 0)

# Resize image using scale value
    def resize(self, scale):
        width = int(self.image.shape[1] * scale)
        height = int(self.image.shape[0] * scale)
        return cv2.resize(self.image, (width, height))   
    