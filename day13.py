class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)
    
    def deleteNode(self, root, key):
        if not root:
            return root
        
        # Find the node to be deleted
        if key < root.value:
            root.left = self.deleteNode(root.left, key)
        elif key > root.value:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(root.right)
            
            # Copy the inorder successor's content to this node
            root.value = temp.value
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.value)
        
        return root
    
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Test the implementation
t1 = Tree()
t1.insert(20)
t1.insert(10)
t1.insert(11)
t1.insert(4)
t1.insert(3)
print(t1.inorder(t1.root))  # Output should be [9, 10, 11, 20]
t1.root = t1.deleteNode(t1.root, 20)
print(t1.inorder(t1.root))  # Output should be [9, 11, 20]
