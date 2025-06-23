from vending_machine import Drink, Snack, Candy
import csv
import os

file_path = "products.txt"
myProducts = []

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if len(row) != 4:
                print(f"Invalid row format: {row}")
                continue
                
            category, name, price, extraAttribute = row
            category = category.lower()
                
            # Define an instance of the right product type
            if category == "drink":
                # The conversion could be better with exception or handle it using more string methods
                price = float(row[2])
                extraAttribute = float(row[3])
                product = Drink(name, price, extraAttribute)
                
            elif category == "snack":
                price = float(row[2])
                extraAttribute = float(row[3])
                product = Snack(name, price, extraAttribute)
                
            elif category == "candy":
                product = Candy(name, price, extraAttribute)
                
            else:
                print(f"{category} is not a valid product type")
                continue

            myProducts.append(product)

else:
    print("File not found!")

# Options Menu
while(True):
    print("Welcome to the Python Vending Machine!\n")
    
    if not myProducts:
        print("No products available!")
    
    print("Please select what you want:\n")
    
    # Iterate through the products list to display them all
    i = 0
    for i in range(len(myProducts)):
        print(f"{i+1}. {myProducts[i].__class__.__name__} - {myProducts[i].get_name()}")

    print(f"{i+2}. Exit\n")
    
    option = input("> ")

    # Check if the option is a valid index and display its info if it 
    if option.isdigit():
        index = int(option)
        
        if index <= len(myProducts) and index > 0:
            myProducts[index-1].display_info()
            print("_____________________\n")
        elif index == len(myProducts) + 1:
            print("Salam (^_^)")
            break
        
        else:
            print("This index does not relate to any product!\n_____________________\n")
    
    else:
        print("Wrong entry!\n_____________________\n")
