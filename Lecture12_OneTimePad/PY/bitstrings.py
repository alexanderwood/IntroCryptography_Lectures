def ToBits(charstring):
    bitstring = '' # Initialize to empty

    for letter in charstring:
        bit = bin(ord(letter)) # Convert to binary
        bit = bit[2:] # Chop off the '0b'

        # Now if the length of bit is less than 8 (one byte),
        # pad it with in front zeros to make the length 8.
        # Example: 10001 -> 00010001
        zeropadding = '00000000'
        L = len(bit)
        bit = zeropadding[L:] + bit

        # Concatenate to the bitstring :)
        bitstring += bit

    return bitstring

def ToChar(bitstring):
    charstring = '' # Initialize to empty

    # We want to go through bitstring by 8's!
    for i in range(0, len(bitstring), 8):
        bit = '0b' + bitstring[i:i+8] # Express as binary string
        char = chr(int(bit, 2)) # Convert to a letter
        charstring += char # Concatenate to charstring

    return charstring


        
