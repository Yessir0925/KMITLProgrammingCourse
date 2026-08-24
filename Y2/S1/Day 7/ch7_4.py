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

    def delete(self, data):
        self.root, found = self._deleteNode(self.root, data)
        return found

    def _deleteNode(self, node, data):
        if node is None:
            return None, False
        if data < node.data:
            node.left, found = self._deleteNode(node.left, data)
        elif data > node.data:
            node.right, found = self._deleteNode(node.right, data)
        else:
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            succ = node.right
            while succ.left is not None:
                succ = succ.left
            node.data = succ.data
            node.right, _ = self._deleteNode(node.right, succ.data)
            found = True
        return node, found

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ')
commands = [c.strip() for c in inp.split(',')]
for c in commands:
    action, value = c.split()
    value = int(value)
    if action == 'i':
        print('insert', value)
        T.insert(value)
        T.printTree(T.root)
    elif action == 'd':
        print('delete', value)
        found = T.delete(value)
        if not found:
            print('Error! Not Found DATA')
        T.printTree(T.root)
