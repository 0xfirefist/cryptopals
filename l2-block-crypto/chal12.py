# Byte-at-a-time ECB decryption (Simple)

# An ECB/CBC detection oracle
from chal10 import aesBlockEncrypt
from chal9 import pad
import random
from base64 import b64decode

def ecbEncrypt(ptext,key):
    padPText = pad(ptext,16)
    ctext = b""
    for index in range(0,len(padPText),16):
        ctext = ctext + aesBlockEncrypt(padPText[index:index+16],key)
    return ctext

def oracle(ptext,key):
    ptext = ptext + b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    return ecbEncrypt(ptext,key)

def attack():
    key = bytes([random.randint(0,127) for i in range(16)])
    # block size 
    blockSize = 16
    # no of blocks in unknown string
    noOfBlocks = len(oracle(b'',key))//blockSize

    ptext = b''

    preBlock = b'a'*16
    for nblock in range(noOfBlocks):
        decodedText = b''
        # for block 0
        for l in range(16):
            aa = preBlock[l+1:16]
            fblock = oracle(aa,key)[nblock*16:16*(nblock+1)]
            for i in range(128):
                newa = aa + decodedText + bytes([i])
                if oracle(newa,key)[0:16] == fblock:
                    decodedText = decodedText + bytes([i])
                    break
        preBlock = decodedText
        ptext = ptext + decodedText
    
    
    print(ptext.decode())

if __name__ == "__main__":
    attack()