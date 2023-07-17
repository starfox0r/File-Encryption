import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_file(file_path, key):
    # Generate a random initialization vector
    iv = get_random_bytes(16)

    # Create the AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the contents of the file in binary mode
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Pad the file data to be a multiple of 16 bytes
    padded_data = pad(file_data, 16)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    # Get the encrypted file name
    encrypted_file_name = f"{file_path}.enc"

    # Write the encrypted data to a new file in binary mode
    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_data)

    # Return the encrypted file name
    return encrypted_file_name


def decrypt_file(file_path, key):
    # Read the contents of the encrypted file in binary mode
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Extract the initialization vector and encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    # Create the AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data and remove the padding
    decrypted_data = unpad(cipher.decrypt(encrypted_data), 16)

    # Get the original file name
    decrypted_file_name = os.path.splitext(file_path)[0]

    # Write the decrypted data to a new file in binary mode
    with open(decrypted_file_name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    # Return the decrypted file name
    return decrypted_file_name


# Prompt for encryption or decryption
action = input("Choose an action (encrypt/decrypt): ")

key = b'!%\xe2\xee\x10\x9da\xd3 t\x06:`O_\x83o\xa9\xbbSQ\x04\x80\x05\xeb%<X\xd0\x19\xfci'

if action.lower() == "encrypt":
    file_path = input("Enter the path of the file to encrypt: ")

    encrypted_file_path = encrypt_file(file_path, key)
    print(f"File encrypted and renamed as: {encrypted_file_path}")

elif action.lower() == "decrypt":
    file_path = input("Enter the path of the file to decrypt: ")

    decrypted_file_path = decrypt_file(file_path, key)
    print(f"File decrypted and renamed as: {decrypted_file_path}")

else:
    print("Invalid action. Please choose either 'encrypt' or 'decrypt'.")
