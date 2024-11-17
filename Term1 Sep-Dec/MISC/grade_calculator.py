while True:
    # allows user to enter number of marks
    marks = int(input("Please enter your marks:"))

    # range check 
    if marks > 100 or marks < 0:
        print("Impossible")

    #filters the grade by the mark achieved and outputs grade
    elif marks >= 70:
        print("Your grade is an A")
    
    elif marks >= 60:
        print("Your grade is an B")

    elif marks >= 50:
        print("Your grade is an C")

    elif marks >= 40:
        print("Your grade is an D")
    
    else:
        print("You failed")