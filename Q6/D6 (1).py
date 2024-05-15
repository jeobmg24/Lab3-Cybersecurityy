import os
import sys
import ast
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(AES.block_size)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

if __name__ == "__main__":
    key_input = input("Enter decryption key: ")
    key = ast.literal_eval(key_input)
    path = "/home/cse/Lab3/Q6files/"
    current_dir = os.listdir(path)
    encrypted_files = [f for f in os.listdir(current_dir) if f.endswith("encrypted")]

    for encrypted_file in encrypted_files:
        filename = encrypted_file[:-10]
        input_file = os.path.join(current_dir, encrypted_file)
        output_file = os.path.join(current_dir, filename)

        decrypt_file(input_file, output_file, key)
        print(f"{filename} has been restored")