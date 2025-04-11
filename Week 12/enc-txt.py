'''
Jmoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - enc-txt.py
NOTE: REMEMBER TO SAVE AES KEY IN **TXT** FILE TO USE FOR DECRYPTION!
'''

# Import AES cipher for encryption and a secure random key generator
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Function to generate a random AES key of a given size (e.g., 256 bits)
def generate_aes_key(key_size):
    return get_random_bytes(key_size // 8)  # Divide by 8 to convert bits to bytes

# Function to encrypt a file using AES encryption (EAX mode)
def encrypt_file_aes(file_path, key):
    # Create a new AES cipher object using the key and EAX mode
    cipher = AES.new(key, AES.MODE_EAX)

    # Open the file to be encrypted in binary read mode
    with open(file_path, 'rb') as file:
        plaintext = file.read()  # Read the file contents

        # Encrypt the data and generate a message authentication code (tag)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Save the encrypted content to a new file with ".enc" extension
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(cipher.nonce)     # Write the nonce (random value used once)
        encrypted_file.write(tag)              # Write the authentication tag
        encrypted_file.write(ciphertext)       # Write the actual encrypted content

# Main part of the script that runs if the file is executed directly
if __name__ == "__main__":
    # Generate a 256-bit AES key
    aes_key = generate_aes_key(256)

    # Ask the user to enter the file path for the file to encrypt
    file_to_encrypt = input("Enter the name of the file to encrypt: ")

    # Encrypt the file using the generated AES key
    encrypt_file_aes(file_to_encrypt, aes_key)

    print(f'File "{file_to_encrypt}" encrypted.')

    # Display the AES key in hexadecimal format — this must be saved to decrypt later
    print(f'AES Key (Hex): {aes_key.hex()}')
