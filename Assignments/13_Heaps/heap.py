class MaxHeap:
    def __init__(self, initial_data=None):
        """Initialize the max-heap"""
        self.data = []
        if initial_data:
            self.data = list(initial_data)
            self.build_heap()

    def left_child(self, index):
        """Return index of left child"""
        return 2 * index + 1

    def right_child(self, index):
        """Return index of right child"""
        return 2 * index + 2

    def parent(self, index):
        """Return index of parent"""
        return (index - 1) // 2

    def heapify_down(self, index):
        """Maintain max-heap property downward from given index"""
        size = len(self.data)
        while True:
            left = self.left_child(index)
            right = self.right_child(index)
            largest = index

            # Find largest among node and its children
            if left < size and self.data[left] > self.data[largest]:
                largest = left
            if right < size and self.data[right] > self.data[largest]:
                largest = right

            # Heap property satisfied
            if largest == index:
                break

            # Swap and continue downward
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            index = largest

    def heapify_up(self, index):
        """Maintain max-heap property upward from given index"""
        while index > 0:
            parent_idx = self.parent(index)
            # Stop if parent is larger
            if self.data[index] <= self.data[parent_idx]:
                break
                
            # Swap with parent and move up
            self.data[index], self.data[parent_idx] = self.data[parent_idx], self.data[index]
            index = parent_idx

    def build_heap(self):
        """Build max-heap from unordered array (bottom-up)"""
        start_index = (len(self.data) - 2) // 2
        for i in range(start_index, -1, -1):
            self.heapify_down(i)

    def push(self, value):
        """Insert value into heap"""
        self.data.append(value)
        self.heapify_up(len(self.data) - 1)

    def pop(self):
        """Remove and return maximum element"""
        if not self.data:
            raise IndexError("pop from empty heap")
            
        # Swap root with last element
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        max_value = self.data.pop()
        
        # Maintain heap property if elements remain
        if self.data:
            self.heapify_down(0)
            
        return max_value

    def __len__(self):
        """Return number of elements in heap"""
        return len(self.data)

    def __repr__(self):
        """String representation of heap"""
        return f"MaxHeap({self.data})"



# Create max-heap with initial data
heap = MaxHeap([4, 10, 3, 5, 1, 8, 2])
print("Initial heap:", heap)
    
# Insert more values
heap.push(15)
heap.push(7)
print("After pushing 15 and 7:", heap)
    
# Pop all elements
print("\nPopping elements in descending order:")
while heap:
    print(heap.pop(), end=" → ")

print("END")
