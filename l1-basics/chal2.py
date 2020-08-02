# Fixed XOR

# input bytes output bytes
def xorByteStrings(byteString1,byteString2):
    # passing an iterable to the bytes constructor => a^b returns an integer
    xordString = bytes(a^b for a,b in zip(byteString1,byteString2))
    return xordString

if __name__ == "__main__":
    # one way to do this is 
    hexString1 = "1c0111001f010100061a024b53535009181c"
    int1 = int(hexString1,16)
    hexString2 = "686974207468652062756c6c277320657965"
    int2 = int(hexString2,16)

    print(hex(int1^int2))

    # but we will be following the cryptopals rule
    # pretty print using hex or base64
    # work on bytes

    # getting bytes strings
    byteString1 = bytes.fromhex(hexString1)
    byteString2 = bytes.fromhex(hexString2)

    # getting xor of the two byte strings
    xordString = xorByteStrings(byteString1,byteString2)

    # hex encoding bytes string for pretty print
    hexString = xordString.hex()
    print(hexString)