##
##Let’s use ASCII and modular arithmetic to write a function,
##alph_to_num, which takes a capital letter as input and
##converts it to a number between 0 and 25 using ASCII codes
##and modular arithmetic.
def alph_to_num(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        return ord(letter) - 65
    else:
        print('Invalid input')
        return None 

##Let’s use ASCII and modular arithmetic to write a function,
##num_to_alph, which takes a number modulo 26 as input and
##converts it to the corresponding letter in the alphabet using
##ASCII.
def num_to_alph(number):
    return chr((number % 26) + 65)

    
