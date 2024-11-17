# init variables
password = ""
wrong_pass = 0

#while loop for password entering
while password != "mash" and wrong_pass < 3:
    password = input("Enter password: ")

    # if password is wrong tell user and add to wrong pass count
    if password != "mash":
        print("Wrong")
        wrong_pass += 1

# would lock a user out for too many wrong atempts 
if wrong_pass == 3: 
    print("Too many atempts!")

