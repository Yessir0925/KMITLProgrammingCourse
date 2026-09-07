class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None) -> None:
        self.root = root

    def get_successor(self, curr):
        pass

    def search_subtree(self, root, key):
        pass

    def insert(self, root, key):
        pass

    def delete_subtree(self, root, key):
        pass

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent, root.val)
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.height = 1  # Height of the node

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, root, key):
        pass

    def left_rotate(self, z):
        pass

    def right_rotate(self, z):
        pass

    def get_height(self, root):
        pass

    def get_balance(self, root):
        pass

    def bst_to_avl(self, bst_root):
        # Convert BST to sorted list via in-order traversal
        sorted_values = self.inorder_traversal(bst_root)

        # Insert elements into the AVL tree
        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        # Helper function to perform in-order traversal and return a sorted list
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.val]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)


inp1, inp2 = input(
    "Enter the key of tree and node to cut: "
).split("/")
bst = BST()
for i in inp1.split():
    bst.root = bst.insert(bst.root, int(i))
print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

# Convert the found subtree into an AVL tree
print("Subtree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree90(avl1.root)

# Convert the remaining BST (after deletion) into an AVL tree
print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree90(avl2.root