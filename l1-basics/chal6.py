# Break repeating-key XOR
import base64

# break into blocks of keysize
def getBlocks(byteString,keySize):
    byteBlocks = []
    for i in range(0,len(byteString),keySize):
        if i+keySize > len(byteString):
            byteBlocks = byteBlocks + [byteString[i:len(byteString)]]
        else:
            byteBlocks = byteBlocks + [byteString[i:i+keySize]]
    return byteBlocks

# calculate hamming distance of given blocks
def calHamDist(byteBlocks):
    hamDist = 0
    for i in range(1,len(byteBlocks)):
        b1,b2 = byteBlocks[i-1],byteBlocks[i]
        score = 0
        for x,y in zip(b1,b2):
            xor = x^y
            for a in bin(xor):
                if a=='1': 
                    score += 1
        hamDist += score
    return hamDist 

# detect key size 
def guessSize(byteString):
    # initializing
    guessedSize = 2
    minHamDist = 1000000

    # start guessing
    for keySize in range(2,40):
        # get blocks for key size k
        byteBlocks = getBlocks(byteString,keySize)
        # calculate hamming distance for these blocks
        hamDist = calHamDist(byteBlocks)
        # average hamming distance
        hamDist = hamDist // len(byteBlocks) 
        # normalizing based on key size
        hamDist = hamDist// keySize
        # update values
        if hamDist < minHamDist:
            guessedSize = keySize
            minHamDist = hamDist
        
    return guessedSize

# TODO
def decrypt(cbytes,guessedSize):
    oneSizeKeyCiphers = []
    for byte in range(cbytes):


if __name__ == "__main__":
    # testing hamming distance
    assert(calHamDist([b'this is a test',b'wokka wokka!!!'])==37)
    ctext = open("/home/devil/AUGUST/cryptopals/l1-basics/files/6.txt").read()
    cbyte = base64.b64decode(ctext)
    print(guessSize(cbyte))