from models.library_item import LibraryItem
from models.reservable import Reservable
from exceptions.custom_exceptions import AlreadyReservedError

# DVD class inheriting from LibraryItem and Reservable
class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration, rating):
        super().__init__(item_id, title, author)
        self.duration = duration  # Duration in minutes
        self.rating = rating  # Content rating
        self.reserved = False  # Reservation status
    
    def display_info(self):
        """Display DVD information"""
        return f"DVD: {self.title} | ID: {self.item_id} | Duration: {self.duration} min | Rating: {self.rating} | Available: {self.available} | Reserved: {self.reserved}"
    
    def reserve(self, user):
        """Reserve the DVD if not already reserved"""
        if self.reserved:
            raise AlreadyReservedError("DVD is already reserved")
        self.reserved = True