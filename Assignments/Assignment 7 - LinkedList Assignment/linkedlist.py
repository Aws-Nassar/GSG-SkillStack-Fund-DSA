class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.insert_at_start(data)
            return
        current = self.head
        count = 0
        while current is not None and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of bounds; inserting at the end.")
            self.insert_at_end(data)
        else:
            new_node.next = current.next
            current.next = new_node

    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += f"[{temp.data}]->"
            temp = temp.next
        result += "None"
        return result
    
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def delete_at_start(self):
        if self.head:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    """Assignment Method"""

    def reverse_list(self):
        if self.head is None or self.head.next is None:
            return
        
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


my_list = LinkedList() 

my_list.insert_at_end(10)
my_list.insert_at_end(20)
my_list.insert_at_end(30)
my_list.insert_at_end(40)
my_list.insert_at_end(50)

print("\nOriginal list:\n\n",my_list)

my_list.reverse_list()

print("\n----------------\n\nList after reverse:\n\n",my_list)
