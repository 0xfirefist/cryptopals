# Cryptopals - Set 1

Always operate on raw bytes, never on encoded strings.
Only use hex and base64 for pretty-printing.

## Hamming Distance
Hamming distance is the difference in bits position.

For eg, take these two binary strings
```
a=0010
b=1100
```
The hamming distance between these two string is 3 (bit positions - 0,1,2)


Say some another binary string x with length equal to length of a.

The hamming distance between a,b and between a^x,b^x is equal. This can be generalized over binary strings of any length.

## Detecting key size
In this we used hamming distance. But why?

### Intuition
Let the encrypted string is abcdef (a,b,c.... are all variables representing a byte)

Say the size of key is 4. We can say that the hamming distance between a and e will most probably be less than (a,b) (a,c) (a,d). Whaaaattt? Why?

Say the bytes in plaintext is - ghijkl

The hamming distance between g and k will be equal to that between a and e because the key length is 4.

The intuition is hamming distance between printable characters (mostle alphabats) will be less than between non printable characters.

In the above example.
Distance between (a,e) == (g,k) (xor with same byte doesnot matter)

Whereas distance between (a,b) will be different. It will be like that between non printable character and a printable character.Say a^x = g, the hamming distance between (a,b) = (a^x,b^x). Now (a,b) = (g,something non printable(maybe))

I will add other details too. This is my intuition to understand why is this working.