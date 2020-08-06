from Crypto.Cipher import AES
from base64 import b64decode

# ciphertext
ciphertext = b64decode(open("files/7.txt").read())

# cipher
key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)

# ECB MODE
for i in range(16,len(ciphertext),16):
    blockOfCt = ciphertext[i-16:i]
    print(cipher.decrypt(blockOfCt))