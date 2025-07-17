from models.library_item import LibraryItem

# Magazine class inheriting from LibraryItem
class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue, publisher):
        super().__init__(item_id, title, author)
        self.issue = issue  # Magazine issue number/date
        self.publisher = publisher  # Publishing company
    
    def display_info(self):
        """Display magazine information"""
        return f"Magazine: {self.title} | ID: {self.item_id} | Issue: {self.issue} | Publisher: {self.publisher} | Available: {self.available}"