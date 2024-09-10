import cv2
import numpy as np
from PIL import Image

def convert_to_grayscale(image_path):
    """Converts an image to grayscale."""
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def resize_image(image_path, width, height):
    """Resizes the image to the given width and height."""
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    return resized_image

def blur_image(image_path, blur_strength=5):
    """Applies a blur effect to the image."""
    image = cv2.imread(image_path)
    blurred_image = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)
    return blurred_image

# You can add more functions here as needed
