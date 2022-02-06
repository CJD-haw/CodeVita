
"""
Problem Statement:
    The Caesar cipher is a type of substitution cipher in which each alphabet in the plaintext or messages,
     which is shifted by a number of places down the alphabet.

For example:
    With a shift of 1, P would be replaced by Q, Q would become R, and so on.

    To pass an encrypted message from one person to another,
    It is first necessary that both parties have the ‘Key’ for the cipher,
    So that the sender may encrypt and the receiver may decrypt it.

    Key is the number of OFFSET to shift the cipher alphabet.
    Key can have basic shifts from 1 to 25 positions as there are 26 total alphabets.

    As we are designing custom Caesar Cipher, in addition to alphabets, we are considering numeric digits from 0 to 9.
    Digits can also be shifted by key places.

For Example:
    If a given plain text contains any digit with values 5 and key =2,
    Then 5 will be replaced by 7, “-”(minus sign) will remain as it is.
    Key value less than 0 should result into “INVALID INPUT”

Example 1:
Enter your PlainText: All the best
Enter the Key: 1

The encrypted Text is: Bmm uif Cftu
"""

"""
def ceaser(text,key):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) + key-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        elif char.isdigit():
            result += str(int(char) + key)
        elif char == '-':
            result += '-'
        elif char.isspace():
            result += " "
    return result


text = input("Enter your plain text:")
key = int(input("Enter the key:"))
print(ceaser(text, key))
"""

# print(chr((ord(text) + 1 - 97) % 26 + 97))

message, key = input('Enter Message : '), int(input('Enter Shift Key : '))
lower, upper, special = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*()_+[]{};:,.<>/?\'\"\\'
result = ''

for m in message:
    if m.islower():
        for c, l in enumerate(lower):   # c = lower.index(l)
            if m == l:
                result += lower[(c + key) % len(lower)]
    elif m.isupper():
        for c, u in enumerate(upper):   # c = upper.index(l)
            if m == u:
                result += upper[(c + key) % len(upper)]
    elif m.isdigit():
        result += str(int(m) + key)
    elif m in special:
        result += m
print('Encrypted Message : ', result)
