# Implement CBC mode
from chal1 import pad
from Crypto.Cipher import AES

# input bytes output bytes
def xorByteStrings(byteString1,byteString2):
    # passing an iterable to the bytes constructor => a^b returns an integer
    xordString = bytes(a^b for a,b in zip(byteString1,byteString2))
    return xordString

# block aes encryption
def aesBlockEncrypt(byteString,key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(byteString)
# block aes decryption
def aesBlockDecrypt(byteString,key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(byteString)

# encrypt in cbc mode
def encrypt(iv,ptext,key):
    padPText = pad(ptext,16)
    ctext = b""
    for index in range(0,len(padPText),16):
        ctextI = aesBlockEncrypt(xorByteStrings(iv,padPText[index:index+16]),key)
        ctext = ctext + ctextI
        iv = ctextI
    return ctext

# decrypt in cbc mode
def decrypt(iv,ctext,key):
    ptext = b""
    for index in range(0,len(ctext),16):
        ptextI = aesBlockDecrypt(ctext[index:index+16],key)
        ptext = ptext + xorByteStrings(ptextI,iv)
        iv = ctext[index:index+16]
    return ptext

if __name__ == "__main__":
    # block size = 16bytes
    iv = b"0123456789876543"
    ptext = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut metus elit, varius vitae erat et, luctus hendrerit arcu. Quisque fringilla, nulla id aliquam fermentum, nibh tortor dapibus risus, vel auctor odio dui id lectus. Aliquam ornare euismod nulla id aliquam. Vivamus vel enim magna. Ut auctor nunc quis erat faucibus rhoncus. Cras porttitor elementum nisl, sit amet mollis tortor sagittis eu. Curabitur suscipit auctor ligula sed laoreet. Vestibulum quis mollis orci, efficitur posuere diam. Donec sit amet erat in enim ultricies accumsan. Aenean ullamcorper neque leo, nec vestibulum eros faucibus eget. Proin at tellus condimentum, blandit purus nec, gravida leo. Vivamus mollis in quam at porta. Aenean et hendrerit ante. Proin aliquam tempor justo, sit amet laoreet ante mollis at. "
    key = b"YELLOW SUBMARINE"
    ctext = encrypt(iv,ptext,key)
    print(ctext.hex())
    print(decrypt(iv,ctext,key))