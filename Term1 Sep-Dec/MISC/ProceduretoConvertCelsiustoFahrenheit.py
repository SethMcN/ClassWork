def convert (temp,conversion):
    if conversion.lower() in ["fahrenheit","f"]:
        print(f"{temp}°C = {(temp * 9/5) + 32}°F")

    if conversion.lower() in ["celsius","c"]:
        print(f"{temp}°F = {(temp - 32) * 5/9}°C")


temp = int(input("Please enter the temperature: "))
con = input("Please enter the which temperature you want to convert to: ")

convert (temp,con)