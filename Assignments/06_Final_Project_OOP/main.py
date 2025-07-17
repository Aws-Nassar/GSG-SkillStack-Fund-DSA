from models.library import Library
from models.user import User
from exceptions.custom_exceptions import ItemNotFoundError, UserNotFoundError, ItemNotAvailableError, AlreadyReservedError

def main():
    """Main function to run the library management system"""
    library = Library()
    # Load initial data
    library.load_items("data/items.json")
    library.load_users("data/users.json")
    
    while True:
        # Display main menu
        print("\n===== Library Management System =====")
        print("1. View all available items")
        print("2. Search item by title or type")
        print("3. Register a new user")
        print("4. Borrow an item")
        print("5. Reserve an item")
        print("6. Return an item")
        print("7. Exit and Save")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # View available items
            print("\nAvailable Items:")
            available_found = False
            for item in library.items.values():
                if item.available:
                    print(item.display_info())
                    available_found = True
            if not available_found:
                print("No available items found")
        
        elif choice == '2':
            # Search items by keyword
            keyword = input("Enter search keyword: ").lower()
            print("\nSearch Results:")
            results_found = False
            for item in library.items.values():
                # Check the item name, author and type
                item_type = item.__class__.__name__.lower() if hasattr(item, '__class__') else ""
                
                if (keyword in item.title.lower() or 
                    keyword in item.author.lower() or 
                    keyword in item_type):
                    print(item.display_info())
                    results_found = True
        
            if not results_found:
                print("No matching items found")
        
        elif choice == '3':
            # Register new user
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            user_id = str(len(library.users) + 1)
            new_user = User(user_id, name, email)
            library.add_user(new_user)
            print(f"User registered successfully! Your ID is: {user_id}")
        
        elif choice == '4':
            # Borrow an item
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to borrow: ")
            try:
                library.borrow_item(user_id, item_id)
                print("Item borrowed successfully!")
            except (UserNotFoundError, ItemNotFoundError, ItemNotAvailableError) as e:
                print(f"Error: {str(e)}")
        
        elif choice == '5':
            # Reserve an item
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to reserve: ")
            try:
                library.reserve_item(user_id, item_id)
                print("Item reserved successfully!")
            except (UserNotFoundError, ItemNotFoundError, AlreadyReservedError, TypeError) as e:
                print(f"Error: {str(e)}")
        
        elif choice == '6':
            # Return an item
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to return: ")
            try:
                library.return_item(user_id, item_id)
                print("Item returned successfully!")
            except (UserNotFoundError, ItemNotFoundError) as e:
                print(f"Error: {str(e)}")
        
        elif choice == '7':
            # Save data and exit
            library.save_items("data/items.json")
            library.save_users("data/users.json")
            print("Data saved. Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-7")

if __name__ == "__main__":
    main()