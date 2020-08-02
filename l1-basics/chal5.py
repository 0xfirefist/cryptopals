# Implement repeating-key XOR

from chal2 import xorByteStrings

def encrypt(plaintext, key):
    ptInBytes = plaintext.encode()
    kInBytes = key.encode()
    completeKey = kInBytes * (len(ptInBytes)//len(kInBytes)) + kInBytes[0:len(ptInBytes)%len(kInBytes)]

    # encryption
    ciphertext = xorByteStrings(ptInBytes,completeKey)
    return ciphertext

if __name__ == "__main__":
    plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    key = "ICE"
    print(encrypt(plaintext,key).hex())