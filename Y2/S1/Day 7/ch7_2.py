class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insertNode(self.root, data)
        return self.root

    def _insertNode(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insertNode(node.left, data)
        else:
            node.right = self._insertNode(node.right, data)
        return node

    def countHeight(self, node):
        if node is None:
            return 0
        
        lcountHeight = self.countHeight(node.left)
        rcountHeight = self.countHeight(node.right)

        return max(lcountHeight, rcountHeight) + 1

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is :", T.countHeight(root) - 1)