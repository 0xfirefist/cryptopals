# Single-byte XOR cipher
# cearser cipher with bytes instead of alphabats

from pprint import pprint

# the string with the highest score
# How to score?
# Using character frequency
# in this case i take the number of printable character in a string 
## (as per the ascii table)
# it can be made better if the particular characters are given
def score(byteString):
    score = 0
    for i in byteString:
        if i>=32 and i<=126:
            score+=1
    return score
# one issue is there can be multiple strings with same score

# decrypt ceaser cipher for bytes
def decrypt(byteString):
    # initializing max score byte strings
    maxScoreList=[byteString]
    maxScore = score(byteString)

    # xor the bytestring with a byte 
    for i in range(256):
        # get new decoded string
        newString = bytes((i^byte for byte in byteString))
        # get score 
        newScore = score(newString)
        # update max elements accordingly
        if  newScore > maxScore:
            maxScoreList = [newString]
            maxScore = newScore
        elif newScore == maxScore:
            maxScoreList = maxScoreList + [newString]
            
    return maxScoreList

# given strings
hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
byteString = bytes.fromhex(hexString)

pprint(decrypt(byteString))
