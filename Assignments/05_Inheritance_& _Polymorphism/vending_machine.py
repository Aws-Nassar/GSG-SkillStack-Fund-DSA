# Parent Class
class Product:
    def __init__(self, pName = None, pPrice = 0):
        self.__name = None
        self.__price = 0
        
        if pName is not None:
            self.set_name(pName)

        if not pPrice == 0:
            self.set_price(pPrice)
        
    # Setter for name attribute
    def set_name(self, pName):
        if isinstance(pName, str):
            self.__name = pName

    # Setter for price attribute
    def set_price(self, pPrice):
        if isinstance(pPrice, (int, float)):
            self.__price = pPrice

    # Getter for name attribute
    def get_name(self):
        return self.__name
    
    # Getter for price attribute
    def get_price(self):
        return self.__price
    
    # Display product info
    def display_info(self):
        print(f"\nProduct Information:\nProduct: {self.get_name()}, Price: ${self.get_price()}")


# Subclass Drink
class Drink (Product):
    def __init__(self, dName = None, dPrice = 0, dVolume = 0):
        super().__init__(dName, dPrice)
        
        self.__volume = 0
        
        if not dVolume == 0:
            self.set_volume(dVolume)

    # Setter for volume attribute
    def set_volume(self, dVolume):
        if isinstance(dVolume, (int, float)):
            self.__volume = dVolume

    # Getter for volume attribute
    def get_volume(self):
        return self.__volume

    # Display drink info
    def display_info(self):
        super().display_info()
        print(f"Volume: {self.get_volume()}ml")


# Subclass Snack
class Snack (Product):
    def __init__(self, sName = None, sPrice = 0, sCalories = 0):
        super().__init__(sName,sPrice)
        
        self.__calories = 0
        
        if not sCalories == 0:
            self.set_calories(sCalories)

    # Setter for calories attribute
    def set_calories(self, sCalories):
        if isinstance(sCalories, (int, float)):
            self.__calories = sCalories

    # Getter for calories attribute
    def get_calories(self):
        return self.__calories

    # Display Snack info
    def display_info(self):
        super().display_info()
        print(f"Calories: {self.get_calories()}cal")


# Subclass Candy
class Candy (Product):
    def __init__(self, cName = None, cPrice = 0, cFlavor = None):
        super().__init__(cName,cPrice)
        
        self.__flavor = None
        
        if cFlavor is not None:
            self.set_flavor(cFlavor)

    # Setter for flavor attribute
    def set_flavor(self, cFlavor):
        if isinstance(cFlavor, str):
            self.__flavor = cFlavor

    # Getter for flavor attribute
    def get_flavor(self):
        return self.__flavor
        
    # Display Candy info
    def display_info(self):
        super().display_info()
        print(f"Flavor: {self.get_flavor()}")

