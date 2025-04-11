'''
Jmoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - stego.py
NOTE: USE IMAGE FILE: drdoes.png
'''
# Import the Python Imaging Library (Pillow) for working with images
from PIL import Image

# Main function to hide a secret message inside an image
def hide_message():
    # Ask the user for the original image path
    image_path = input("Enter the path of the original image: ").strip()

    # Ask the user for the secret message to embed
    message = input("Enter the secret message to hide: ").strip()

    # Open the image file and ensure it's in RGB mode
    img = Image.open(image_path)
    img = img.convert('RGB')

    # Convert each character in the message into its 8-bit binary representation
    data = []
    for char in message:
        data.extend(format(ord(char), '08b'))  # Append 8-bit binary string of each char

    pixel_index = 0  # To keep track of how much of the message has been hidden

    # Loop through each pixel in the image
    for i in range(img.width):
        for j in range(img.height):
            pixel = list(img.getpixel((i, j)))  # Get pixel as list of RGB values

            # Modify the least significant bit of each RGB channel
            for color_channel in range(3):
                if pixel_index < len(data):
                    # Replace the LSB with the corresponding bit of the message
                    pixel[color_channel] = int(
                        format(pixel[color_channel], '08b')[:-1] + data[pixel_index], 2
                    )
                    pixel_index += 1

            # Update the pixel in the image
            img.putpixel((i, j), tuple(pixel))

    # Ask the user where to save the stego image
    stego_image_path = input("Enter the path to save the stego image (e.g., stego_image.png): ").strip()
    img.save(stego_image_path, format='PNG')  # Save the image in PNG format to preserve changes

    print("Message hidden successfully!")

# Call the function to run the script
hide_message()
