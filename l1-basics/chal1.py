# Convert hex to base64

#### CRYPTOPALS RULE ####
# Always operate on raw bytes, never on encoded strings. 
# Only use hex and base64 for pretty-printing. 

import base64

def hexTobase64(hexString):
    # get bytes from hex
    byteString = bytes.fromhex(hexString)
    # base64 encoding
    encodedString = base64.b64encode(byteString)
    # encoded byte string 
    return encodedString

if __name__ == "__main__":
    # input hex string
    hexString = input()

    print(hexTobase64(hexString).decode())