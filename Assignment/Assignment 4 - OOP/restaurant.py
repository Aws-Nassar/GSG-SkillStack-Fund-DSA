from order import Order
from menuItem import MenuItem

# Create Restaurant class with two data members which are list of MenuItem objects abnd list of orders
class Restaurant:
    def __init__(self):
        self.__menu = []
        self.__orders = []

    # Add a Order object to orders list
    def add_order(self, order):
        if isinstance(order, Order):
            self.__orders.append(order)

        else:
            print("You must enter all ordered item info.\n")

    # Display the orders list
    def list_orders(self):
        if self.is_orders_empty():
            print("No one order yet.\n")

        else:
            print("Orders:")
            count = 1
            for order in self.__orders:
                print("Order ", count, ":")
                order.print_order()
                print("\n")
                count += 1

    # Display the total coast of all orders
    def total_orders(self):
        if self.is_orders_empty():
            print("No one order yet.\n")

        else:
            total = 0
            for order in self.__orders:
                total += order.total()

            print("Total: ", total)

    # Add a MenuItem object to menu list
    def add_menu_item(self,item):
        if isinstance(item, MenuItem):
            self.__menu.append(item)

        else:
            print("You must enter all menu item info.\n")

    # Display the menu list item/s
    def list_menu_items(self):
        if self.is_menu_empty():
            print("Your menu is empty.\n")

        else:
            print("Menu:")
            count = 1
            for item in self.__menu:
                print(count, ". ", item.get_name(), " ($", item.get_price(), ") ", "[", item.get_category(), "] ")
                count += 1

            print("\n")

    # Return the menu item needed according to the index of the item
    def get_menu_item(self, index):
        if isinstance(index, (int, float)):
            return self.__menu[index-1]

        else:
            return None

    # Return which is the menu list empty or not
    def is_menu_empty(self):
        return len(self.__menu) == 0

    # Return which is the orders list empty or not
    def is_orders_empty(self):
        return len(self.__orders) == 0
