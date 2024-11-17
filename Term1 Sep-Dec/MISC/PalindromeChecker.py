def Palindrome_Checker(word):
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    
    else:
        print(f"{word} is not palindrome")


word = input("Please enter a word: ")

Palindrome_Checker(word)