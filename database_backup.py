from PIL import Image
import os

# Replace 'input_image.jpg' with the path to your input image
input_image_path = 'input_mountain.jpg'

# Load the input image
input_image = Image.open(input_image_path)

# Replace 'output_image.png' with the desired output image path and name
output_image_path = 'output_newmount.png'

# Save the image in PNG format
input_image.save(output_image_path)
