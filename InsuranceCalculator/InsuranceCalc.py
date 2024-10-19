from random import randint #for the cypher encryption 

class InsuranceCalc:
    def __init__(self,name,age,gender,prevAccidents,DrivingExp,CarType,Claims):
        
        # assign values to object properties
        self.name = name
        self.age = age
        self.gender = gender
        self.prevAccidents = prevAccidents
        self.DrivingExp = DrivingExp
        self.CarType = CarType
        self.Claims = Claims
        self.cost = 0

        self.WriteDict = {
            "Name: ":self.name,
            "Age: ":self.age,
            "Gender: ":self.gender,
            "Previous accidents: ":self.prevAccidents,
            "Driving experiance: ":self.DrivingExp,
            "Car Type: ": self.CarType,
        }
        

    def Calc(self):
        print(f"\n Hi {self.name} Welcome to your insurance planner.")
        
        # spesification of the program requires costs to be addded it the user meets certian requirments
        # if age is less then 25 add 100
        # if the user is a male add 50 
        # If you have less than 3 years of driving experience, add £100 to the premium. If you have over 10 years of experience, subtract £50 from the premium. 
        # Add £150 to the premium for sports cars and £75 for SUVs. 
        # has the user had previous accidents then add 75 

        self.cost = 500
        #age check 

        if self.age < 25:
            self.cost += 100

        elif self.age > 65:
            self.cost += 50
        
        #gender check 
        if self.gender.lower() in ["m","male"]:
            self.cost  += 50 
        
        #driving experiance 
        print(self.cost)
        if self.DrivingExp < 3:
            self.cost += 100

        elif self.DrivingExp > 10:
            self.cost -= 50 
        
        print(self.cost)

        #Accidents 
        self.cost  += (self.prevAccidents * 75)
        print(self.cost)
        
        # no claims
        self.cost -= self.Claims*20 
        print(self.cost)
        # Car type
        if self.CarType in {"sports","sport"}: # £150 extra
            self.cost += 150
        
        elif self.CarType in {"suv"}: # £75 extra
            self.cost += 75
            
        print(self.cost)
        return  f"your instrance is £{self.cost}"

    # what is returned when the object is printed 
    def __str__(self):
        return(f"""
        ----------------------------------
        Name: {self.name}
        age: {self.age}
        gender: {self.gender}
        prevAccidents: {self.prevAccidents}
        Driving experiance: {self.DrivingExp}
        Car Type: {self.CarType}
        Claims: {self.Claims}

        cost = £{self.cost}
        ----------------------------------
        """)
        

def check(condition,data):

    #checks data entered is the right type 

        try:
            #string check 
            if condition == "str check":
                if not data.isalpha():
                    print("Only letters please")
                    raise Exception
            # int check 
            elif condition == "int check":
                if not data.isnumeric():
                    print("Only numbers please")
                    raise Exception 

                if int(data) < 0:
                    print("Invalid")
                    raise Exception 
            # gender check 
            elif type(condition) == set:
                if data not in condition:
                    print(f"Only data in {condition} please")
                    raise Exception 
    
        except:
            return False

        else: return True 

# function to encrypt data to write to text file 
def Encrypiton(dict):
    data = []
    shift = randint(1,26)

    for key in (dict.keys()):
        value = ""

        for i in str(dict[key]).lower():
            char = ord(i)+shift
            if char > 122:
                char -= 26

            value += chr(char)
        dict[key] = value

    return dict
        

# start of the program 
while True: # while True for multiple users 

    # name check 
    valid = False
    while not valid:
        name = input("Please enter your name(or STOP to end program)?: ")
        if name.upper() == "STOP":
            exit()
        valid = check("str check",name)

    #age check
    valid = False
    while not valid:
        age = input("Please enter your age?: ")
        valid = check("int check",age)

        if valid:
            age = int(age)

            #if the age is under 17 will calculate how long to wait
            if age < 17:
                print(f'Try again in 1 year' if (age-17 == 1) else f'Try again in {17-age} years')
                valid = False
            
            elif age > 100:
                print("You should not be driving")
                valid = False

    # gender check        
    valid = False
    while not valid:
        gender = input("Please enter your gender?: ").lower()
        valid = check({"Male","Female","f","m"},gender)

    #previous accidents
    valid = False
    while not valid:
        prevAccidents = (input("Please enter your previous accitdents?: "))
        valid = check("int check",prevAccidents)

        if valid:
            prevAccidents = int(prevAccidents)
            
            if prevAccidents > 50:
                print("Too many accidents, we will not accept")
                valid = False

    #driving experiance
    valid = False
    while not valid:
        DrivingExp = input("How many years of driving experiance do you have?: ")
        valid = check("int check",DrivingExp)

        if valid:
            DrivingExp = int(DrivingExp)
            
            if DrivingExp > age-17:
                print("Fraudulent behaviour detected, insurance denied!")
                valid = False

    #driving experiance
    valid = False
    while not valid:
        CarType = input("What type of car will you be driving?: ")
        valid = check({"sport","suv"},CarType)

    # No claims 
    valid = False
    while not valid:
        Claims = input("How many years of no claim?: ")
        valid = check("int check",Claims)
        if valid:
            Claims = int(Claims)
            if Claims > DrivingExp:
                print(f"You've only be diving for {DrivingExp} years")
                valid = False

    dataBase = open(r"T-level\Code\Python School\OOP\DataBase.txt","a") #dataBase to hold object data from class(users data)
    # init all user data 

    name = InsuranceCalc(name,age,gender,prevAccidents,DrivingExp,CarType,Claims)
    cost = name.Calc() # call calculator function
    print(name) # outputs user data to user
    dataEncrypt = Encrypiton(name.WriteDict) # encrypts data with previous cypher work

    dataBase.write("\n------------------------------------")

    for key,val in dataEncrypt.items():
        dataBase.write(f"\n{key}{val}")

    dataBase.close()
