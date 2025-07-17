# Custom exceptions for library system
class ItemNotFoundError(Exception):
    """Raised when an item is not found in the library"""
    pass

class UserNotFoundError(Exception):
    """Raised when a user is not found"""
    pass

class ItemNotAvailableError(Exception):
    """Raised when trying to borrow an unavailable item"""
    pass

class AlreadyReservedError(Exception):
    """Raised when trying to reserve an already reserved item"""
    pass