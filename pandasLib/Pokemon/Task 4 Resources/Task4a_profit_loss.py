import pandas as pd
import datetime


def profit_loss_menu():

    flag = True
    
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show profit/loss for specific products")
        print("2. Show profit/loss for all products")
        print("3. Show quantity sold for product and supplier")
        print("###############################################")

        profit_loss_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(profit_loss_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(profit_loss_choice) 


def get_product_choice():
    flag = True

    product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]
    
    while flag:
        # Refactored and optimized
        print("######################################################")
        print("Please choose a product form the list:")
        print("Please enter the number of the product (1-16)")

        for index,item in enumerate(product_list):
            print(f"{index+1}: {item}")

        print("######################################################")


        product_choice = input("Please enter the number of your choice (1-16): ")

        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name


def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY)')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(start_date, dayfirst=True)


def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY)')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(end_date, dayfirst=True)


def get_date_range_all(start_date, end_date):
    df1 = pd.read_csv("pandasLib/Pokemon/Task 4 Resources/Task4a_data.csv") 

    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date), df1.columns != "Supplier"].copy()
    
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    total = round(results["Profit subtotal"].sum(),2)
    results_print = results.to_string(index=False)
    
    print(results_print)
    print("The overall profit/loss for the selected time frame was £{}".format(total))


def get_date_range_product(start_date, end_date):
    product_name = get_product_choice()
    df2 = pd.read_csv("pandasLib/Pokemon/Task 4 Resources/Task4a_data.csv") 

    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)
   
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    results_print = product_results.to_string(index=False)
    
    print(results_print)
    print("The profit/loss for the {} for selected time frame was £{}".format(product_name, total))


def get_supplier():
    df = pd.read_csv("pandasLib/Pokemon/Task 4 Resources/Task4a_data.csv") 

    suppliers = list(set(df["Supplier"]))

    valid = False

    while not valid:
        for index, sup in enumerate(suppliers):
            print(f"{index+1} {sup}")

        supplier = input("Please enter the number of your choice (1-5): ")

        try:
            int(supplier)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True

        else:
            if int(supplier) < 1 or int(supplier) > 16:
                print("Sorry, you did not enter a valid choice")
                valid = True
            else:
                supplier = suppliers[int(supplier)-1]
                return supplier


def get_product_quantity(start_date,end_date):
    df = pd.read_csv("pandasLib/Pokemon/Task 4 Resources/Task4a_data.csv") 

    supplier = get_supplier()
    product = get_product_choice()


    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
   
    df = df.loc[(df["Date"] >= start_date) & (df["Date"] <= end_date) & (df["Product"] == product) & (df["Supplier"] == supplier)].copy()
    df["Cost Subtotal"] = df["KGs Purchased"] * df["Purchase Price"]
    df["Sales subtotal"] = df["KGs Sold"] * df["Selling Price"]
    df["Profit subtotal"] = df["Sales subtotal"] - df["Cost Subtotal"]

    print(df)

    total = round(df["Profit subtotal"].sum(),2)
    quantity_sold = df["KGs Sold"].sum()

    print(f"Profit: £{total}")
    print(f"Total quantity sold: {quantity_sold}kg")
    

def process_menu_choice(profit_choice, start_date, end_date):
    if profit_choice == 1:
        get_date_range_product(start_date, end_date)

    elif profit_choice == 2:
        get_date_range_all(start_date, end_date)
    
    elif profit_choice == 3:
         get_product_quantity(start_date,end_date)


if __name__ == "__main__":
    start_date = get_start_date() 
    end_date = get_end_date() 
    profit_choice = profit_loss_menu() 
    process_menu_choice(profit_choice, start_date, end_date) 



