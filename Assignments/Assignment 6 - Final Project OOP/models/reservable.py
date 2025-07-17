from abc import ABC, abstractmethod

# Interface class for reservable items
class Reservable(ABC):
    @abstractmethod
    def reserve(self, user):
        """Reserve the item for a user"""
        pass