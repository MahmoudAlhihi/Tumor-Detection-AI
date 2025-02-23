import cv2
import os

# Define the path to an image file (Change this to an actual image in your dataset)
image_path = "dataset//Testing/glioma/Te-gl_0024.jpg"  

# Check if the file exists before loading
if not os.path.exists(image_path):
    print("Error: Image file not found! Please check the path.")
else:
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Check if the image loaded correctly
    if img is None:
        print("Error: Unable to load image. Please check the file format.")
    else:
        # Print the image dimensions
        print("Image Dimensions (Height, Width, Channels):", img.shape)
