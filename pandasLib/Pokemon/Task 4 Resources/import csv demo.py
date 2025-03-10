import csv
#Make use of the CSV file handling library

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each element in the row
            processed_row = []
            for element in row:
                # Try to convert element to a float (currency)
                try:
                    element = float(element)

                except ValueError:
                    pass  # If it fails, keep original string

                # Try to convert element to an integer
                try:
                    element = int(element)

                except ValueError:
                    pass  # If it fails, keep the original string

                processed_row.append(element)

            # Add the processed row to the data list
            data.append(processed_row)

    return data


# Example usage:
file_path = 'C:\\Temp\\Task4a_data.csv' # Assuming CSV downloaded
csv_data = read_csv_file(file_path)
# print(csv_data)

# Assuming csv_data is obtained from the previous example

def calculate_total_weight(data,name_of_item):
    total = 0

    for row in data:
        # The third element [2] in each row is KG purchased
        if row[0] == name_of_item:
            try:
                total += int(row[2])
                
            except ValueError:
                print(row[2])
            
    return total

def get_product_choice():
    flag = True
    while flag:
        print("######################################################")
        print("Please choose a product form the list:")
        print("Please enter the number of the product (1-16)")
        print("1.  Potatoes")
        print("2.  Carrots")
        print("3.  Peas")
        print("4.  Lettuce")
        print("5.  Onions")
        print("6.  Apples")
        print("7.  Oranges")
        print("8.  Pears")
        print("9.  Lemons")
        print("10. Limes")
        print("11. Melons")
        print("12. Cabbages")
        print("13. Asparagus")
        print("14. Broccoli")
        print("15. Cauliflower")
        print("16. Celery")
        print("######################################################")

        product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]

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
      
            
# Example usage:
item=get_product_choice()
total_value = calculate_total_weight(csv_data,item)
print("Total weight of ",item," purchased:", total_value,"Kg")
