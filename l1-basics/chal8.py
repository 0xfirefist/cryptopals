# Detect AES in ECB mode

# pass the hex decoded string
def score(hexCode):
    sc = 0
    hexBlocks = [hexCode[i-32:i] for i in range(32,len(hexCode),32)]
    for i in range(len(hexBlocks)):
        for j in range(i+1,len(hexBlocks)):
            if hexBlocks[i] == hexBlocks[j]:
                sc = sc+1
    
    return sc

if __name__ == "__main__":
    hexCodes = open("files/8.txt").read().split("\n")
    ecbCode = hexCodes[0]
    sc = 0

    for i in hexCodes:
        newsc = score(i)
        if newsc > sc :
            sc = newsc
            ecbCode = i

    print(ecbCode)