# An ECB/CBC detection oracle
from chal10 import encrypt as cbcEncrypt
from chal10 import aesBlockEncrypt
from chal9 import pad
import random

def ecbEncrypt(ptext,key):
    padPText = pad(ptext,16)
    ctext = b""
    for index in range(0,len(padPText),16):
        ctext = ctext + aesBlockEncrypt(padPText[index:index+16],key)
    return ctext
    
def oracle(ptext):
    # add bytes to ptext
    noOfBytes = random.randint(5,10)                                # random between(5-10)

    # adding random bytes to plaintext
    ptext = bytes([random.randint(0,127) for i in range(noOfBytes)]) + ptext
    ptext = ptext + bytes([random.randint(0,127) for i in range(noOfBytes)])

    mode = random.randint(0,1)                                      # random mode
    key = bytes([random.randint(0,127) for i in range(16)])         # random key
    if mode:
        iv = bytes([random.randint(0,127) for i in range(16)])      # random iv
        print("Encrypted with CBC")
        return cbcEncrypt(iv,ptext,key)
    else:
        print("Encrypted with ECB")
        return ecbEncrypt(ptext,key)


# pass the hex decoded string
def score(hexCode):
    sc = 0
    hexBlocks = [hexCode[i-32:i] for i in range(32,len(hexCode),32)]
    for i in range(len(hexBlocks)):
        for j in range(i+1,len(hexBlocks)):
            if hexBlocks[i] == hexBlocks[j]:
                sc = sc+1
    
    return sc

def detect(ctext):
    mode = 1
    if score(ctext.hex())>0:
        mode = 0
    
    if mode:
        print("CBC")
    else :
        print("ECB")

if __name__ == "__main__":
    ptext = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ctext = oracle(ptext)
    detect(ctext)