pt_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# When hacking the shift cipher the only argument is the ciphertext
# Since we do not yet know the key!
def shift_hack(ciphertext):
    # For each possible key value 0-25
    for key in range(26):
        # Attempt to decrypt the ciphertext using this key
        # by calling the previously defined decrypt function
        test = decrypt(ciphertext, key)

        # Print out the decryption attempt
        line = 'Key #' + str(key) + ': ' + test
        print(line)

def decrypt(ciphertext, key):
    # Create the ciphertext alphabet
    ct_alph = pt_alph[key:] + pt_alph[:key]
    
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
    uin = input("What would you like to decrypt? ")
    # Change all inputs to uppercase
    uin = uin.upper()

    pt = shift_hack(uin)
    print(pt)


main()
