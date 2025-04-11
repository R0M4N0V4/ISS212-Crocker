'''
Jmoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - de-txt.py
NOTE: USE AES KEY IN **TXT** FILE TO DECRYPT FILE: sup3rs3cr37.txt.enc
'''

# Import AES cipher from the pycryptodome library
from Crypto.Cipher import AES

# Function to decrypt an AES-encrypted file using EAX mode
def decrypt_file_aes(encrypted_file_path, key):
    # Open the encrypted file in binary read mode
    with open(encrypted_file_path, 'rb') as encrypted_file:
        # Read the nonce (first 16 bytes), which was used during encryption
        nonce = encrypted_file.read(16)
        # Read the authentication tag (next 16 bytes) to verify integrity
        tag = encrypted_file.read(16)
        # Read the remaining data — the actual encrypted content
        ciphertext = encrypted_file.read()

    # Recreate the cipher using the same key and nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Decrypt and verify the ciphertext using the tag
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # Save the decrypted plaintext to a new file
    with open(encrypted_file_path[:-4] + '_decrypted.txt', 'wb') as decrypted_file:
        decrypted_file.write(plaintext)

# Main block that runs the script
if __name__ == "__main__":
    # Ask the user to enter the AES key used during encryption (in hex format)
    aes_key = bytes.fromhex(input("Enter the AES key (hexadecimal format): "))

    # Ask the user for the encrypted file they want to decrypt
    file_to_decrypt = input("Enter the name of the file to decrypt: ")

    # Call the function to decrypt the file using the provided key
    decrypt_file_aes(file_to_decrypt, aes_key)

    # Confirm that the file has been successfully decrypted
    print(f'File "{file_to_decrypt}" decrypted.')
