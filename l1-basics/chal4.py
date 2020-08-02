# Detect single-character XOR
from pprint import pprint
from chal3 import decrypt

# filter list based on printable character
def filter(decryptedList):
    for decryptedString in decryptedList: 
        for c in decryptedString:
            if c>126 :
                return True
    return False

# this will return a list of possible ciphers 
def detect(ciphers):
    possibleCiphers = []
    for cipher in ciphers:
        possPlain = decrypt(bytes.fromhex(cipher))
        if not filter(possPlain):
            possibleCiphers = possibleCiphers + [cipher]
    return possibleCiphers


# read file input
ciphers = open("files/4.txt").read().split("\n")
pprint(detect(ciphers))