vowels = ["a","e","i","o","u"]
vowelCount = 0

string = input("Please anter some text: ").lower()

for i in range(len(string)):
    if string[i] in vowels:
        vowelCount += 1

print(f"There are {vowelCount} vowels in the text")


