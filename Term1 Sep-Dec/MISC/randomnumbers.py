# import form a library
from random import randint

# inits varables
count = 0
number = 0

while number != 12:
    num1,num2 = randint(1,6),randint(1,6)
    total = num1 + num2 

    if total == 12: break
    
    count += 1

print (f"counts for 12 = {count}")


# stats for each dice role
number = [i for i in range(13)]
counting = [0 for i in range(13)]

# 100000 roles
for i in range(100000):
    num1,num2 = randint(1,6),randint(1,6)
    total = num1 + num2 
    counting[number.index(total)] += 1

for i in range(13):
    print(f"{i} = {round((counting[i]/100000)*100)}%")

