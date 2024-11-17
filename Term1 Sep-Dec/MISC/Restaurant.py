items = {
    "Pizza":10.99,
    "Burger":11.99,
    "Milkshake": 4.99,
    "Salad":3.99,
    "Chips":4.50}
    
for x,y in items.items():
    print(f"{x} : £{y}")
    
RunningMeals = []
RunningCost = []
meal = ""

while meal != "stop":
    meal = input("Please enter a meal/item (stop to stop)").capitalize()
    if meal not in items.keys():
        print("Please enter a valid meal")

    else:
        quantity = int(input("Please enter the quantity"))
        RunningMeals.append(f"{meal} x{quantity}")
        RunningCost.append(items[meal]*quantity)
        
payed = "False"
while payed == False:
    print(f"The total cost is £{sum(RunningCost)}")
    money = float(input("Please pay: £"))
    if money < sum(RunningCost):
        print("Please pay the full amount")
    else:
        change = money - sum(RunningCost)
        Payed = True

#Recipt

for x,y in RunningMeals,RunningCost:
    print(f"Item:{x} Cost:{y}")
    