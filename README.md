This lab was all about Cryptography and Ransomware. We learned the risks of ransomware by seeing how an attack is carried out as well as how learning how to defend against it. 

In the first two questions, we experimented with crypography hash functions, namely the SHA-256 function. We then were given a directory of files in Q2 and we had to write a function to see which had the same SHA-256 hash value as the file Q2hash

In the third question, we learned about digital signatures, which provide authenticity that the software came from the stated authors. The way this works is one key is used by the signer, to sign files and therefore must be kept private. The other
key is made public. In this question, we had to find which file was correctly signed.

In question four, we were given the Encrypted program, R4.py, and we had to write the corresponding decryption program, D4.py. In question 5, we were given an encryption program, however the teachers were not so nice and obfuscated the file. It was harder to understand, yet we still 
had to write the decryption program

Question 6 tied the whole lab together by having US write the ransomware, R6.py. There4 were many steps to the answer though. We had to write a key-generation program, KG6.py, which generated a public (e) and private (d) key and saved them both. Then we encrypted all the files 
in the directory using R6.py. Then we wrote the attackers' decryption program, AD6.py, which used the private decryption key, and finally wrote program D6.py which was the victim's decryption program to decrypt all the encrypted files in the directory. 
