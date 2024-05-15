import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


with open(os.path.join("/home/cse/Lab3/Q4files", "Encrypted4"), 'rb') as f:
    iv = f.read(16)
    ciphertext = f.read()
key = b'$\x01\xfd\xe8\xe7\xb0\xe9\xfc\r9\xd7\x02\xbcH\xa9)'
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
with open('Q4a', 'a') as f:
    f.write(plaintext.decode())