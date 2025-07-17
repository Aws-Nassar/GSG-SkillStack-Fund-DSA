import json
from .book import Book
from .magazine import Magazine
from .dvd import DVD
from .user import User
from .reservable import Reservable
from exceptions.custom_exceptions import ItemNotFoundError, UserNotFoundError, ItemNotAvailableError, AlreadyReservedError

class Library:
    def __init__(self):
        self.items = {}
        self.users = {}
    
    def add_item(self, item):
        self.items[item.item_id] = item
    
    def remove_item(self, item_id):
        if item_id not in self.items:
            raise ItemNotFoundError("Item not found")
        del self.items[item_id]
    
    def add_user(self, user):
        self.users[user.user_id] = user
    
    def remove_user(self, user_id):
        if user_id not in self.users:
            raise UserNotFoundError("User not found")
        del self.users[user_id]
    
    def borrow_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError("User not found")
        if item_id not in self.items:
            raise ItemNotFoundError("Item not found")
        if not self.items[item_id].available:
            raise ItemNotAvailableError("Item not available")
        
        self.items[item_id].available = False
        self.users[user_id].borrowed_items.append(item_id)
    
    def return_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError("User not found")
        if item_id not in self.items:
            raise ItemNotFoundError("Item not found")
        
        self.items[item_id].available = True
        if item_id in self.users[user_id].borrowed_items:
            self.users[user_id].borrowed_items.remove(item_id)
    
    def reserve_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError("User not found")
        if item_id not in self.items:
            raise ItemNotFoundError("Item not found")
        
        item = self.items[item_id]
        if isinstance(item, Reservable):
            item.reserve(self.users[user_id])
        else:
            raise TypeError("Item is not reservable")
    
    def load_items(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item_data in data:
                    if item_data['type'] == 'book':
                        item = Book(
                            item_data['item_id'],
                            item_data['title'],
                            item_data['author'],
                            item_data['isbn'],
                            item_data['genre']
                        )
                    elif item_data['type'] == 'magazine':
                        item = Magazine(
                            item_data['item_id'],
                            item_data['title'],
                            item_data['author'],
                            item_data['issue'],
                            item_data['publisher']
                        )
                    elif item_data['type'] == 'dvd':
                        item = DVD(
                            item_data['item_id'],
                            item_data['title'],
                            item_data['author'],
                            item_data['duration'],
                            item_data['rating']
                        )
                    self.items[item.item_id] = item
        except FileNotFoundError:
            print("Items file not found, starting with empty library")
        except Exception as e:
            print(f"Error loading items: {str(e)}")
    
    def load_users(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for user_data in data:
                    user = User(
                        user_data['user_id'],
                        user_data['name'],
                        user_data['email']
                    )
                    user.borrowed_items = user_data.get('borrowed_items', [])
                    self.users[user.user_id] = user
        except FileNotFoundError:
            print("Users file not found, starting with no users")
        except Exception as e:
            print(f"Error loading users: {str(e)}")
    
    def save_items(self, filename):
        items_data = []
        for item in self.items.values():
            item_data = {
                'item_id': item.item_id,
                'title': item.title,
                'author': item.author,
                'available': item.available,
                'type': item.__class__.__name__.lower()
            }
            if isinstance(item, Book):
                item_data.update({
                    'isbn': item.isbn,
                    'genre': item.genre,
                    'reserved': item.reserved
                })
            elif isinstance(item, Magazine):
                item_data.update({
                    'issue': item.issue,
                    'publisher': item.publisher
                })
            elif isinstance(item, DVD):
                item_data.update({
                    'duration': item.duration,
                    'rating': item.rating,
                    'reserved': item.reserved
                })
            items_data.append(item_data)
        
        try:
            with open(filename, 'w') as f:
                json.dump(items_data, f, indent=4)
        except Exception as e:
            print(f"Error saving items: {str(e)}")
    
    def save_users(self, filename):
        users_data = []
        for user in self.users.values():
            users_data.append({
                'user_id': user.user_id,
                'name': user.name,
                'email': user.email,
                'borrowed_items': user.borrowed_items
            })
        
        try:
            with open(filename, 'w') as f:
                json.dump(users_data, f, indent=4)
        except Exception as e:
            print(f"Error saving users: {str(e)}")