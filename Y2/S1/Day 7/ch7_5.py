class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

OPERATORS = set('+-*/')

def buildTree(postfix):
    stack = []
    for ch in postfix:
        node = Node(ch)
        if ch in OPERATORS:
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop()

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

def infix(node):
    if node.left is None and node.right is None:
        return node.data
    return '(' + infix(node.left) + node.data + infix(node.right) + ')'

def prefix(node):
    if node.left is None and node.right is None:
        return node.data
    return node.data + prefix(node.left) + prefix(node.right)
#The prefix will return both the subtree

postfix = input('Enter Postfix : ')
root = buildTree(postfix)
print('Tree :')
printTree(root)
print('-' * 50)
print('Infix :', infix(root))
print('Prefix :', prefix(root))
