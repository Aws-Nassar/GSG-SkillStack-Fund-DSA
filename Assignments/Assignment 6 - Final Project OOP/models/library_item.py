from abc import ABC, abstractmethod

# Abstract base class for all library items
class LibraryItem(ABC):
    def __init__(self, item_id, title, author):
        self.item_id = item_id  # Unique item identifier
        self.title = title  # Item title
        self.author = author  # Item author/producer
        self.available = True  # Availability status
    
    @abstractmethod
    def display_info(self):
        """Abstract method to display item information"""
        pass
    
    def check_availability(self):
        """Check if the item is available"""
        return self.available