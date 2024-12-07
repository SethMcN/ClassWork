def gridSetup():
    grid = [[chr((i+j)%26+65).lower() for i in range(26)] for j in range(26)]
    return grid

def VigenereDecypher(key, text):

    key = list(key)
    grid = gridSetup()

    decryptedText = ""

    # each letter in the text is decrypted by the key
    for letter in range(len(text)):
        decrypColumn = 0
        # find the column of the letter in the grid
        for col in range(len(grid[0])):
            if grid[0][col] == key[letter%len(key)]:
                decrypColumn = col
                break
        # find the row of the key in the grid
        for row in range(len(grid)):
            if grid[row][decrypColumn] == text[letter]:
                # add the decrypted letter to the decrypted text
                decryptedText += grid[row][0]
                break
    
    return decryptedText


def VigenereCypher(key, text):

    key = list(key)
    grid  = gridSetup()
    
    encryptedText = ""

    # each letter in the text is encrypted by the key
    for letter in range(len(text)):

        encrypColumn = 0
        # find the column of the letter in the grid
        for col in range(len(grid[0])):
            if grid[0][col] == text[letter]:
                encrypColumn = col
                break
        # find the row of the key in the grid
        for row in range(len(grid)):
            if grid[row][0] == key[letter%len(key)]:  

                # add the encrypted letter to the encrypted text
                encryptedText += grid[row][encrypColumn]
                break

    return encryptedText

def main():
    option = int(input("1. Encrypt\n2. Decrypt\n: "))

    if option == 1:
        key = input("Enter the key: ").lower().replace(" ", "")
        text = input("Enter the text to be encrypted: ").lower().replace(" ", "")
        VigenereCypher(key,text)

    elif option == 2:
        key = input("Enter the key: ").lower().replace(" ", "")
        text = input("Enter the text to be decrypted: ")
        VigenereDecypher(key,text)


if __name__ == "__main__":

    while True:
        main()