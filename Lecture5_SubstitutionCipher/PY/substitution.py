alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

import random

def key_gen():
    return random.sample(alphabet, k=len(alphabet))

def encrypt(plaintext, key):
    ciphertext = ''

    plaintext = plaintext.upper()
    
    for letter in plaintext:
        if letter in alphabet:
            i = alphabet.index(letter)
            ciphertext += key[i]

        else:
            ciphertext += letter

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''

    for letter in ciphertext:
        if letter in key:
            i = key.index(letter)
            plaintext += alphabet[i]

        else:
            plaintext += letter

    return plaintext



def main():
    k = key_gen()

    c = encrypt('a b c d e f g h i j k l m n o p q r s t u v w x y z', k)
    
    print(c)

    d = decrypt(c, k)
    print(d)

main()
