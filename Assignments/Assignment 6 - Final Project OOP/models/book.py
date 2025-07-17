from models.library_item import LibraryItem
from models.reservable import Reservable
from exceptions.custom_exceptions import AlreadyReservedError

# Book class inheriting from LibraryItem and Reservable
class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, isbn, genre):
        super().__init__(item_id, title, author)
        self.isbn = isbn  # International Standard Book Number
        self.genre = genre  # Book genre
        self.reserved = False  # Reservation status
    
    def display_info(self):
        """Display book information"""
        return f"Book: {self.title} by {self.author}  | ID: {self.item_id} | ISBN: {self.isbn} | Genre: {self.genre} | Available: {self.available} | Reserved: {self.reserved}"
    
    def reserve(self, user):
        """Reserve the book if not already reserved"""
        if self.reserved:
            raise AlreadyReservedError("Book is already reserved")
        self.reserved = True