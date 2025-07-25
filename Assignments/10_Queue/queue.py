import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Arriving: {data}")# New code here
 
    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Serving: {value}")# New code here
        return value
 
    def peek(self):
        return None if self.front is None else self.front.data
 
    def is_empty(self):
        return self.front is None
 
    def clear(self):
        self.front = self.rear = None

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        
        current = self.front
        names = []

        while current is not None:
            names.append(current.data)
            current = current.next

        return "Queue: " + str(names)


customer = LinkedQueue()
customer.enqueue("Alice")
customer.enqueue("Bob")
customer.enqueue("Carol")
customer.dequeue()
customer.dequeue()
customer.dequeue()
if customer.is_empty():
    print("All customers served.")



"""Extra: Dynamic customer service system"""
# using menu and sleep method
customerQueue = LinkedQueue()
stopFlag = False
while not stopFlag:
    print("***************Customer service system***************\n")
    print("1.Add a new customer.")
    print("2.Serve the next customer.")
    print("3.Display the current queue.")
    print("4.Exit.")
    
    option = input("Please enter the number of your option: ")

    if option == "1":
        customerName = input("Enter customer name: ")

        if customerName.strip() == "":
            print("\nInvalid name, please enter a valid name. :)")
        
        else:
            customerQueue.enqueue(customerName)
    
    elif option == "2":
        if customerQueue.is_empty():
            print("\nNo customers to serve.")
        
        else:
            customerQueue.dequeue()
            time.sleep(1)
    
    elif option == "3":
        print(customerQueue)

    elif option == "4":
        if customerQueue.is_empty():
            print("\nAll customers served.")
            print("\nSalam, :)")
            stopFlag = True

        else:
            print("\nThere are some customers who still need to be served.")

    else:
        print("\nWrong entry try again, :)")
    
    print("\n#########################################################\n")