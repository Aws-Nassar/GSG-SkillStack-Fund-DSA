class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if node is None:
            return BSTNode(data)
        
        if data < node.data:
            node.left = self._insert(node.left, data)
       
        else:
            node.right = self._insert(node.right, data)
        
        return node
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)
    
    def search(self, node, target):
        if node is None:
            return False
        
        if node.data == target:
            return True
        
        elif target < node.data:
            return self.search(node.left, target)
    
        else:
            return self.search(node.right, target)
            
    def delete(self, node, key):
        if node is None:
            return node
        
        if key < node.data:
            node.left = self.delete(node.left, key)
        
        elif key > node.data:
            node.right = self.delete(node.right, key)
        
        else:
            if node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left
            
            temp = self.findMin(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        
        return node
    
    def findMin(self, node):
        current = node
        while current.left:
            current = current.left
        
        return current
    
    """########## Assignment findMax method ##########"""

    def findMax(self, node):
        current = node
        while current.right:
            current = current.right
        
        return current
    
    """###############################################"""

# Main

bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)
    
print("In-order traversal of BST:")
bst.inorder(bst.root)
    
max_node = bst.findMax(bst.root)
print("\nMaximum value in BST:", max_node.data)