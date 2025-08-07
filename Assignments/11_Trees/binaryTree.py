class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if not node.left:
            node.left = Node(data)
        
        elif not node.right:
            node.right = Node(data)
        
        else:
            self._insert(node.left, data) # Simple left-first insertion
    
    def search(self, node, target):
        if node is None:
            return False
        
        if node.data == target:
            return True
        
        return self.search(node.left, target) or self.search(node.right, target)
    
    def delete(self, root, key):
        if root is None:
            return None
        
        if root.data == key:
            # Case 1: Node with no child
            if not root.left and not root.right:
                return None
        
            # Case 2: Node with only one child
            if not root.left:
                return root.right
        
            if not root.right:
                return root.left
            
            # Case 3: Node with two children - replace with inorder successor
            succ_parent = root
            succ = root.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            
            if succ_parent != root:
                succ_parent.left = succ.right
            
            else:
                succ_parent.right = succ.right
        
            root.data = succ.data
            return root
        
        root.left = self.delete(root.left, key)
        root.right = self.delete(root.right, key)
        return root
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)
    
    """########## Assignment balanced methods ##########"""

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, node):
        if not node:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)
    
    """################################################"""
    
# Main

# Balanced tree
bt1 = BinaryTree()    
bt1.root = Node(4)
bt1.root.left = Node(2)
bt1.root.right = Node(6)
bt1.root.left.left = Node(1)
bt1.root.left.right = Node(3)
bt1.root.right.left = Node(5)
bt1.root.right.right = Node(7)
print("Is balanced tree balanced?", bt1.isBalanced(bt1.root))

# Unbalanced tree
bt2 = BinaryTree()
bt2.root = Node(1)
bt2.root.left = Node(2)
bt2.root.left.left = Node(3)
bt2.root.left.left.left = Node(4)
print("Is unbalanced tree balanced?", bt2.isBalanced(bt2.root))
