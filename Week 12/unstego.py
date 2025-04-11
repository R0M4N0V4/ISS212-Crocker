'''
Jmoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - stego.py
NOTE: USE STEGO IMAGE FILE: drdoes-steg.png
'''

# Import the PIL library to open and read image data
from PIL import Image

# Function to extract a hidden message from a stego image
def extract_message():
    print("Stego Image Extraction Script")

    # Ask user to enter the path to the image that contains the hidden message
    stego_image_path = input("Enter the path of the stego image: ").strip()

    # Open the stego image
    img = Image.open(stego_image_path)

    data = ''  # Will hold all the least significant bits extracted from the image
    terminator = '11111111'  # Special marker used to signal the end of the hidden message

    # Loop through all pixels in the image to collect the hidden bits
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))  # Get RGB values of the pixel
            for color_channel in range(3):  # Loop through R, G, and B
                # Extract the least significant bit from each channel
                data += format(pixel[color_channel], '08b')[-1]

    # Find the position where the terminator sequence appears
    terminator_index = data.find(terminator)

    # Convert the binary data back to readable characters, stopping at the terminator
    message = ''.join([chr(int(data[i:i+8], 2)) for i in range(0, terminator_index, 8)])

    # Print the extracted secret message
    print(f"Extracted Message: {message}")

# Run the function only if the script is executed directly
if __name__ == "__main__":
    extract_message()
