from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import MD5

BLOCKSIZE = 256
h = MD5.new()
count = 0
with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)

# creating key
hf = h.digest()

with open('Encrypted5', 'rb') as f:
        iv = f.read(16)
        ct = f.read()

cipher = AES.new(hf, AES.MODE_CBC, iv=iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)
pt = pt.decode('utf-8')
print(pt)
