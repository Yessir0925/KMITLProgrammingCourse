class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data, self.left, self.right = data, left, right
            self.setHeight()
        def __str__(self):
            return str(self.data)
        def getHeight(self, node):
            return -1 if node is None else node.height
        def setHeight(self):
            self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
            return self.height
        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)
        
    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def rotateLeftChild(root):
        child = root.left
        root.left = child.right
        child.right = root
        root.setHeight()
        child.setHeight()
        return child
    
    @staticmethod
    def rotateRightChild(root):
        child = root.right
        root.right = child.left
        child.left = root
        root.setHeight()
        child.setHeight()
        return child
    
    @staticmethod
    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)
        root.setHeight()
        if root.balanceValue() < -1:
            if root.left.balanceValue() > 0:
                root.left = AVLTree.rotateRightChild(root.left)
            root = AVLTree.rotateLeftChild(root)
        elif root.balanceValue() > 1:
            if root.right.balanceValue() < 0:
                root.right = AVLTree.rotateLeftChild(root.right)
            root = AVLTree.rotateRightChild(root)
        return root
    
    def add(self, data):
        self.root = self._add(self.root, int(data))

    @staticmethod
    def _postOrder(root):
        if root:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end=' ')

    def postOrder(self):
        print('AVLTree post-order : ', end='')
        self._postOrder(self.root)
        print()

    @staticmethod
    def _printTree(node, level=0):
        if node:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)
            
    def printTree(self):
        self._printTree(self.root)
        print()


avl1 = AVLTree()
for command in input('Enter Input : ').split(','):
    command = command.strip()
    if command[:2] == 'AD':
        avl1.add(command[3:])
    elif command[:2] == 'PR':
        avl1.printTree()
    elif command[:2] == 'PO':
        avl1.postOrder()
