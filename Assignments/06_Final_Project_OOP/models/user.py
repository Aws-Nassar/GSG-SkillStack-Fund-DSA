# User class for library patrons
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id  # Unique user identifier
        self.name = name  # User's full name
        self.email = email  # User's email address
        self.borrowed_items = []  # List of borrowed item IDs
    
    def __str__(self):
        """String representation of user"""
        return f"User ID: {self.user_id} | Name: {self.name} | Email: {self.email}"