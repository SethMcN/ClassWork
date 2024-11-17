num = int(input("Please enter a number: "))

notPrime = True

for i in range (2,num):
    if num % i == 0:
        print(f"{num} is not prime, it is divisable by {i}")
        notPrime = False
        break


if notPrime:
    print(f"{num} is a prime")