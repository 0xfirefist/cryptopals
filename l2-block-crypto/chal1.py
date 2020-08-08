# Implement PKCS#7 padding

def pad(byteString, blockSize):
    padLength = blockSize - len(byteString)%blockSize
    padString = byteString
    for _ in range(padLength):
        padString = padString + bytes([padLength])
    return padString

if __name__ == "__main__":
    string = input("Enter string to pad\n")
    blockSize = int(input("Enter block size\n"))
    print(pad(string.encode(),blockSize))

