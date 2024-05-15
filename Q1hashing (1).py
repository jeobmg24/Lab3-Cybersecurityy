import os
import sys
import hashlib

e = "1a0b21fbc13e80dff1b545028fc140f8a30f4b28aaf52e5c1dd9d6d52a1b3da5"
path = "/home/cse/Lab3/Q2files/"
dir_files = os.listdir(path)
print(f'searching through {path}')
for file in dir_files:
  #print(f'{file}: ')
  with open(file, 'rb') as f:
    data = f.read()
  file_hash = hashlib.sha256(data).hexdigest()
  #print(file_hash)
  print("\n")
  if file_hash == e:
    print(file)
  