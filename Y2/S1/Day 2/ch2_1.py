"""You are required to implement an AVL Tree, a self-balancing 
binary search tree where the heights of the two child subtrees 
of any node differ by at most one. Your implementation should 
support various operations, including insertion, deletion, and 
tree traversal methods.

Constraints:

    You must implement the AVL Tree structure with proper insertion and deletion logic.
    The tree should maintain its balance after every insertion and deletion.
    The traversal functions should be implemented from scratch, following the AVL Tree principles.

Note:
You may assume that all values inserted into the AVL Tree are integers and that there are no duplicate values.


Enter commands: i 30,i 20,i 40,i 10,i 25,i 35,i 50,print,d 20,in,print
Tree structure:
        50
    40
        35
30
        25
    20
        10
Inorder: 10 25 30 35 40 50 
Tree structure:
        50
    40
        35
30
    25
        10
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rightRotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def leftRotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.value:
            root.left = self.insert(root.left, key)
        elif key > root.value:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        balance = self.balance(root)

        # Left Left
        if balance > 1 and key < root.left.value:
            return self.rightRotate(root)

        # Right Right
        if balance < -1 and key > root.right.value:
            return self.leftRotate(root)

        # Left Right
        if balance > 1 and key > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left
        if balance < -1 and key < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def minValue(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):

        if root is None:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)

        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:

            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.minValue(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        balance = self.balance(root)

        # Left Left
        if balance > 1 and self.balance(root.left) >= 0:
            return self.rightRotate(root)

        # Left Right
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Right
        if balance < -1 and self.balance(root.right) <= 0:
            return self.leftRotate(root)

        # Right Left
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")

    def printTree(self, root, level=0):
        if root is not None:
            self.printTree(root.right, level + 1)
            print("    " * level + str(root.value))
            self.printTree(root.left, level + 1)


tree = AVLTree()
root = None

commands = input("Enter commands: ").split(",")

for cmd in commands:
    cmd = cmd.strip()

    if cmd == "print":
        print("Tree structure:")
        tree.printTree(root)

    elif cmd == "pre":
        print("Preorder:", end=" ")
        tree.preorder(root)
        print()

    elif cmd == "in":
        print("Inorder:", end=" ")
        tree.inorder(root)
        print()

    elif cmd == "post":
        print("Postorder:", end=" ")
        tree.postorder(root)
        print()

    elif cmd.startswith("i "):
        value = int(cmd.split()[1])
        root = tree.insert(root, value)

    elif cmd.startswith("d "):
        value = int(cmd.split()[1])
        root = tree.delete(root, value)