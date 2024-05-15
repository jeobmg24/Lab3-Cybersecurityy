import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

def verify_sign(public_key, filename):
  with open(filename, 'rb') as f:
    data = f.read() 
    h = SHA256.new(data)
    
  sf = filename + '.sign'
  
  with open(sf, 'rb') as g:
    priv_key = g.read()
  
  try:
    pkcs1_15.new(public_key).verify(h, priv_key)
    return True
  except:
    return False

if __name__ == '__main__':
  os.chdir('/home/cse/Lab3/')
  with open("Q3pk.pem", "rb") as f:
        key = RSA.import_key(f.read())
  path = "/home/cse/Lab3/Q3files/"
  dir_files = os.listdir(path)
  os.chdir(path)
  for filename in dir_files:
    #if filename.endswith(".exe.sign") and filename == "Q3.py":
      #continue
    if filename.endswith(".exe"):
      if verify_sign(key, filename):
        print(filename)
      else:
        print("no\n")
    