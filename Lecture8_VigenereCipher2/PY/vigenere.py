import ascii_modulus_converter as acm # Make sure this file is in directory
import string # For format checking

def keygen():
    while True:
        uin = input('Keyword: ')
        uin = uin.upper() # Capitalize all

        # Break out of loop if keyword is only uppercase letters
        if all((j in string.ascii_uppercase) for j in uin):
            break
           
    return uin

def encrypt(plaintext, keyword):
    # Remove all spaces.
    plaintext = plaintext.replace(' ', '')

    # Capitalize.
    plaintext = plaintext.upper()
    keyword = keyword.upper()

    # Initialize the ciphertext
    ciphertext = ''

    # Let L be the length of the key.
    L = len(keyword)
    # Variable for iterating over the keyword.
    l = 0

    for letter in plaintext:
        # For punctuation, etc, just copy to ciphertext as-is.
        if not(letter in string.ascii_uppercase):
            ciphertext += letter

        # Encode all letters using Vigenere.
        else:
            temp = (acm.alph_to_num(letter) + (acm.alph_to_num(keyword[l]))) % 26
            ciphertext += acm.num_to_alph(temp)

        # Move on to next letter in keyword, or loop back around.
        l = (l+1) % L

    return ciphertext
            

def decrypt(ciphertext, keyword):
    plaintext = ''  # Initalize to empty string

    # Length of key
    L = len(keyword)
    l = 0

    for letter in ciphertext:
        if not(letter in string.ascii_uppercase):
            plaintext += letter
        else:
            temp = (acm.alph_to_num(letter) - acm.alph_to_num(keyword[l])) % 26
            plaintext += acm.num_to_alph(temp)
        l = (l+1)%L

    return plaintext
    

def main():
    # Generate the key
    key = keygen()

    m = input("What would you like to encrypt: ")
    ans = encrypt(m, key)
    print(ans)

    ans = decrypt(ans, key)
    print(ans)
main()

    

    

    
