while True:

    table = int(input("PLease enter a times table: "))

    num = 0
    while num <= 12:
        print(f"{table} x {num} = {table*num}")
        num += 1