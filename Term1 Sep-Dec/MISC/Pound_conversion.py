pounds = float(input("Please enter amount £"))

conversions = {"Dollars":(1.47,"$"),
               "Euro":(0.71,"€"),
               "rouble":(5.93,"₽")}

for Currancy,y in conversions.items():
    print(f"Pounds in {Currancy} = {pounds*y[0]}{y[1]}")
