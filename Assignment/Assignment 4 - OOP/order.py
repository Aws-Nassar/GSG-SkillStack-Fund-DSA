from menuItem import MenuItem

# Create Order class with single data member which is list of MenuItem objects
class Order:
    #initialize the List data member
    def __init__(self):
        self.__items = []

    # A method to take a MenuItem object as a parameter and add it to the list of items
    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.__items.append(item)

        else:
            print("You must enter all ordered item info.\n")

    #Calculate the total coast of the order
    def total(self):
        total = 0
        for item in self.__items:
            total += item.get_price()
        
        return total

    # Display the order item/s and price
    def print_order(self):
        for item in self.__items:
            print("- ", item.get_name(), " ($", item.get_price(), ")")
