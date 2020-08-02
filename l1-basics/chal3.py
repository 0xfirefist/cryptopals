# Single-byte XOR cipher
# cearser cipher with bytes instead of alphabats

from pprint import pprint

# the string with the highest score
# How to score?
# in this case i take the number of printable character in a string 
## (as per the ascii table)
# it can be made better if the particular characters are given
# def score(byteString):
#     score = 0
#     for i in byteString:
#         if i>=32 and i<=126:
#             score+=1
#     return score
# one issue is there can be multiple strings with same score


# a better way to get score by using englist character frequencies
def score(input_bytes):
    # character frequencies
    characterFrequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([characterFrequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

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

if __name__ == "__main__":
    # # given strings
    hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    byteString = bytes.fromhex(hexString)

    pprint(decrypt(byteString))
