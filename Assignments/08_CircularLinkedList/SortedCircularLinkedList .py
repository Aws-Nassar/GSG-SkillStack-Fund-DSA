class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SortedCircularLinkedList:
    def __init__(self):
        self.head = None

    """--------------------------------Assignment Method's--------------------------------"""
    def insert(self, data):
        new_node = Node(data)
        
        # When the list is empty
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            return
        
        # When the new data is less than head node data
        if new_node.data < self.head.data:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
            return

        # Insert in the middle or on the end node        
        temp = self.head
        while temp.next != self.head and temp.next.data < new_node.data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def __str__(self):
        if self.head is None:
            return "[]"
        
        result = ""
        temp = self.head
        while True:
            result += f"[{temp.data}]->"
            temp = temp.next
            if temp == self.head:
                break
        result += "head"
        return result
    
    """--------------------------------*******************--------------------------------"""

    
    def length(self):
        if self.head is None:
            return 0
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head is None:
            return
        
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next

                temp.next = self.head.next
                self.head = self.head.next
            return
        
        prev = self.head
        temp = self.head.next
        while temp != self.head and temp.data != key:
            prev = temp
            temp = temp.next
        if temp == self.head: 
            return
        prev.next = temp.next

    def search(self, key):
        if self.head is None:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False


my_list = SortedCircularLinkedList() 

my_list.insert(7)

print("\nThe List:\n\n",my_list)

my_list.insert(3)

print("\nThe List:\n\n",my_list)

my_list.insert(9)

print("\nThe List:\n\n",my_list)

my_list.insert(1)

print("\nThe List:\n\n",my_list)

my_list.insert(4)

print("\nThe List:\n\n",my_list)

