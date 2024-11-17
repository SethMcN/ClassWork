target = int(input("Please enter a number: "))

seq = [0,1]
num = 0 

for i in range (target):
    num = seq[i] + seq[i+1]

    if num > target:
        break

    else:
        seq.append(num)


print(seq)