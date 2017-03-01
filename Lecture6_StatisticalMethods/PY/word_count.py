# The alphabet as a global variable string
pt_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create a dictionary
def create_dictionary():
    # First, create a dictionary
    alph = {}

    # Create the dictionary from the string above
    # to avoid having to write the whole thing out.
    for letter in pt_alph:
        alph[letter] = 0

    return alph


# This function counts the number of each letter in
# a string and stores the values in a dictionary.
# INPUT: String and empty Dictionary
# OUTPUT: Dictionary
def letter_count(text, alph):
    for letter in text: # iterate through each character in the string
        if letter in alph: # If the letter is in the alphabet
            alph[letter] += 1 # Increment the associated entry in dictionary

    return alph # Return the updated alphabet.

# This is an alternative method of counting the letters
# which uses a built-in python method.
# INPUT: String and dictionary
# OUTPUT: Dictionary
def letter_count2(text, alph):
    for letter in alph:
        # Use the count method, which returns the
        # where text.count(letter) returns the number
        # of occurences of letter in text.
        alph[letter] = text.count(letter)

    return alph

# The main function.
def main():
    # Initialize the alphabet dictionary
    alphabet = create_dictionary()

    # Open file in READ ONLY mode
    fin = open('invisible_man.txt', 'r')

    # Read the ENTIRE file and store as "text"
    text = fin.read()
    text = text.upper()  # Capitalize all text

    # Close the file.
    fin.close()

    # Call the letter_count function, which returns the updated dictionary
    alphabet = letter_count(text, alphabet)

    # Alternatively, uncomment the line below to use method 2, which
    # uses a built-in python method
    # alphabet = letter_count2(text, alphabet)

    # Create file to store output
    fout = open('wordcount_im.txt', 'w')

    # Write the values in the dictionary into this file
    for letter in pt_alph:
        line = letter + '\t' + str(alphabet[letter]) + '\n'
        fout.write(line)

    # Close the file
    fout.close()


# Call the main function
main()
# Note that this program will not print anything! However check the
# file's directory and you will find 'wordcount.txt' with the
# count of each word saved. :)
