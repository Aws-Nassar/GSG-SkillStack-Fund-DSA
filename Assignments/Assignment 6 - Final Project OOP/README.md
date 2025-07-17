## Library Management System

### How to Run
1. Ensure Python 3.7+ is installed
2. Run the program: `python main.py`

### Project Structure
project/
├── main.py
├── models/
│ ├── library_item.py
│ ├── book.py
│ ├── magazine.py
│ ├── dvd.py
│ ├── user.py
│ └── library.py
├── exceptions/
│ └── custom_exceptions.py
├── exceptions/
│ └── items.json
│ └── users.json
└── README.md

### Key Features
1. **Object-Oriented Design**:
   - Abstract classes for library items
   - Interface pattern for reservable items
   - Inheritance for different item types

2. **Exception Handling**:
   - Custom exceptions for specific error cases
   - File error handling
   - Graceful error recovery

3. **Data Persistence**:
   - JSON file storage for items and users
   - Automatic data loading on startup
   - Data saving on exit

4. **User Interface**:
   - Command-line interface (CLI)
   - Intuitive menu system
   - Clear user feedback