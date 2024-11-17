def factorial(n):

    fact = n
    for i in range (1,n):
        fact *= n-i

    print(f"The factorial of {n} = {fact}")

while True:
    num = int(input("Please enter a number: "))
    factorial(num)