# Create MenuItem class with three data members
class MenuItem:

    # Create a constructor to work with different cases (to deal with object initialize with/without parameters)
    def __init__(self,new_name, new_price, new_category):
        # Create the private data members
        self.__name = None
        self.__price = None
        self.__category = None

        # if the user pass parameters so it will be stored inside the variables
        if new_name is not None:
            self.set_name(new_name)

        if new_price is not None:
            self.set_price(new_price)

        if new_category is not None:
            self.set_category(new_category)

    # Getter for the Item_Name
    def get_name(self):
        return self.__name

    # Setter for the Item_Name
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name

        else:
            print("Name must be a string.\n")

    # Getter for the Item_Price 
    def get_price(self):
        return self.__price

    # Setter for the Item_Price 
    def set_price(self, new_price):
        if isinstance(new_price, (int, float)):
            self.__price = new_price

        else:
            print("Price must be a number.\n")

    # Getter for the Item_Catergory
    def get_category(self):
            return self.__category

    # Setter for the Item_Catergory
    def set_category(self, new_category):
        if isinstance(new_category, str): 
            self.__category = new_category

        else:
            print("Category must be a string.\n")
