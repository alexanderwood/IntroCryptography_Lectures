# This program implements the Caeser 3-shift cipher

pt_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ct_alph = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

def encrypt(plaintext):
    # Initialize the ciphertext to an empty string
    ciphertext = ''

    for letter in plaintext:
        # Skip any punctuation and pass it as is to the ciphertext
        if letter not in pt_alph:
            ciphertext += letter
            continue # Skip ahead to the next iteration

            
        # Find the index of the letter in the plaintext alphabet
        index = pt_alph.index(letter)

        # Find the letter in the ciphertext alphabet at this index
        # Concatenate it to the ciphertext
        ciphertext += ct_alph[index]
    
    return ciphertext


def decrypt(ciphertext):
    # Initialize the ciphertext to an empty string
    plaintext = ''

    for letter in ciphertext:
        # Skip any punctuation and pass it as is to the plaintext
        if letter not in ct_alph:
            plaintext += letter
            continue # Skip ahead to the next iteration

            
        # Find the index of the letter in the ciphertext alphabet
        index = ct_alph.index(letter)

        # Find the letter in the plaintext alphabet at this index
        # Concatenate it to the plaintext
        plaintext += pt_alph[index]
    
    return plaintext



def main():
    uin = input("What would you like to encrypt? ")
    # Change all inputs to uppercase
    uin = uin.upper()

    ct = encrypt(uin)
    print(ct)


    uin = input("What would you like to decrypt? ")
    # Change all inputs to uppercase
    uin = uin.upper()

    pt = decrypt(uin)
    print(pt)


main()









    
