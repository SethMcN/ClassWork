
# This function takes a string and a salt value and returns a 32-bit hash value as a hex string


def hash_string(string,salt="s@lt123"):

    string += salt
    hashValue = 0

    for char in string:
        asciiValue = ord(char)

        # Xor the hash value with the ascii value of the character
        hashValue ^= asciiValue

        # Shift the hash value left by 6 bits and add the hash value right shifted by 27 bits
        hashValue = (hashValue << 6) + (hashValue >> 27)

        # Mask the hash value to 32 bits
        hashValue &= 0xFFFFFFFF

    # Return the hash value as a hex string
    return hex(hashValue)

def main():
    test = input("Enter a string to hash: ")

    print(hash_string(test))

if __name__ == '__main__':
    main()