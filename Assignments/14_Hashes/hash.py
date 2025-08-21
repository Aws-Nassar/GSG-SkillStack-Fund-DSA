class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    TOMBSTONE = object()

    def __init__(self, initial_size=11):
        """Initialize hash table with initial size"""
        self.size = self._next_prime(initial_size)
        self.table = [None] * self.size
        self.count = 0
        self.deleted_count = 0
        self.threshold = 0.7

    def _hash(self, key):
        """Compute hash value for key"""
        return hash(key) % self.size

    def _probe_sequence(self, key, i):
        """Quadratic probing sequence"""
        return (self._hash(key) + i*i) % self.size

    def _is_prime(self, n):
        """Check if a number is prime"""
        if n < 2:
            return False
        
        if n == 2:
            return True
        
        if n % 2 == 0:
            return False
        
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            
            i += 2

        return True

    def _next_prime(self, n):
        """Find the next prime number >= n"""
        if n <= 2:
            return 2
        
        candidate = n
        if candidate % 2 == 0:
            candidate += 1

        while not self._is_prime(candidate):
            candidate += 2
            
        return candidate

    def load_factor(self):
        """Calculate current load factor (active entries + tombstones)"""
        return (self.count + self.deleted_count) / self.size

    def insert(self, key, value):
        """Insert key-value pair into hash table"""
        if self.load_factor() >= self.threshold:
            self._rehash()
        
        i = 0
        while i < self.size:
            idx = self._probe_sequence(key, i)
            # Empty slot or tombstone found
            if self.table[idx] is None or self.table[idx] is self.TOMBSTONE:
                self.table[idx] = Node(key, value)
                self.count += 1

                if self.table[idx] is self.TOMBSTONE:
                    self.deleted_count -= 1

                return
            # Key already exists, update value
            if self.table[idx] is not self.TOMBSTONE and self.table[idx].key == key:
                self.table[idx].value = value
                return
            
            i += 1

        raise Exception("Hash table is full")

    def search(self, key):
        """Search for key and return its value if found"""
        i = 0
        while i < self.size:
            idx = self._probe_sequence(key, i)
            if self.table[idx] is None:
                return None  # Key not found
            
            if self.table[idx] is not self.TOMBSTONE and self.table[idx].key == key:
                return self.table[idx].value  # Return value
            
            i += 1

        return None  # Key not found

    def delete(self, key):
        """Delete key from hash table"""
        i = 0
        while i < self.size:
            idx = self._probe_sequence(key, i)
            if self.table[idx] is None:
                return False  # Key not found
            
            if self.table[idx] is not self.TOMBSTONE and self.table[idx].key == key:
                self.table[idx] = self.TOMBSTONE
                self.count -= 1
                self.deleted_count += 1
                return True
            
            i += 1

        return False  # Key not found

    def _rehash(self):
        """Resize table and reinsert all active entries"""
        old_table = self.table
        old_size = self.size
        new_size = self._next_prime(self.size * 2)
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0
        self.deleted_count = 0
        for entry in old_table:
            if entry is not None and entry is not self.TOMBSTONE:
                self.insert(entry.key, entry.value)

    def __str__(self):
        """String representation of hash table"""
        items = []
        for i, entry in enumerate(self.table):
            if entry is None:
                items.append(f"{i}: None")

            elif entry is self.TOMBSTONE:
                items.append(f"{i}: TOMBSTONE")

            else:
                items.append(f"{i}: {entry.key} -> {entry.value}")

        return "\n".join(items)



# Create hash table
ht = HashTable()
    
# Insert key-value pairs
pairs = [
    (50, "A"), 
    (700, "B"), 
    (76, "C"), 
    (85, "D"), 
    (92, "E"), 
    (73, "F"), 
    (101, "G"), 
    (202, "H"), 
    (303, "I")
    ]
    
for key, value in pairs:
    ht.insert(key, value)
    print(f"Inserted {key} -> {value}")
    print(f"Load factor: {ht.load_factor():.2f}")
    print()
    
# Search for keys
print("Search results:")
print(f"92 -> {ht.search(92)}")
print(f"100 -> {ht.search(100)}")
print(f"73 -> {ht.search(73)}")
print()
    
# Delete a key
print("Deleting key 76:")
print(f"Success: {ht.delete(76)}")
print(f"Search for 76: {ht.search(76)}")
print()
    
# Show final table state
print("Final hash table:")
print(ht)