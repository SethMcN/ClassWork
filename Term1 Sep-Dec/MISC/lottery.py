from random import randint

numbers = []

for i in range (6):
    randnum = randint(1,59)
    if randnum not in numbers:
        numbers.append(randnum)

for i in range(6):
    print(f"number {i+1} is {numbers[i]}")