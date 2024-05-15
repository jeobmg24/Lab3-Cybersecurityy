import os
import sys
import hashlib

e = "157b6f3fcad54a150794ba01ca8e1f298c89892196cd04eb535aedfc82e5227d"
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
  