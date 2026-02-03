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