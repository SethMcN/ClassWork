from random import randint 

# gens random number
num = randint(1,100)

# inits guess
guess = 0
while guess != num:
    # user input 
    guess = int(input("Guess a number: "))

    # too high and too low outputs 
    if guess > num:
        print("Too high!")

    elif guess < num:
        print("Too low!")

# winning output 
print("Correct well done!")