from restaurant import Restaurant
from order import Order
from menuItem import MenuItem

if __name__ == "__main__":
    my_restaurant = Restaurant()
    print("Welcome to the Restaurant Management System!")
    stop_flag = False # flag to break the loop if the user choose exit
    
    while(not stop_flag):
        print("Choose an option:")
        print("1. Add menu item.")
        print("2. View menu.")
        print("3. Create new order.")
        print("4. List all orders.")
        print("5. Exit.")
        option = input("> ")

        # Get the MenuItem values and then store them in Resturant menu list 
        if option == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            category = input("Enter item category: ")

            item = MenuItem(name, price, category)
            my_restaurant.add_menu_item(item)
            print("Menu item added successfully.\n")

        elif option == "2":
            my_restaurant.list_menu_items()

        elif option == "3":
            if my_restaurant.is_menu_empty():
                print("The resturant does not contain a menu item/s yet.\n")
                continue

            choices = input("Enter item numbers for the order separated by commas (e.g., 1,2): ")
            new_order = Order()

            for index in choices.split(","):
                cleaned_index = index.strip()
                int_index = int(cleaned_index)
                item = my_restaurant.get_menu_item(int_index)
                new_order.add_item(item)
            
            my_restaurant.add_order(new_order)
            print("Order created and added successfully.\n")

        elif option == "4":
            if my_restaurant.is_orders_empty():
                print("No orders yet\n")
                continue

            my_restaurant.list_orders()
            my_restaurant.total_orders()

        elif option == "5":
            print("Thank you for using the Restaurant Management System!")
            stop_flag = True # Break the loop

        # Any other input than 1 - 5
        else:
            print("Wrong entry, try again!\n")

# User Entry try/except needed