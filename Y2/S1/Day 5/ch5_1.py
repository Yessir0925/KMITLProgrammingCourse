"""Instructions for Implementing a Singly Linked List Class

Write a class for a Singly Linked List that includes the following methods:

    __init__(self): Initializes the head to indicate the starting point of the Linked List.
    __str__(self): Returns a string representation of the Linked List, showing all elements from head to tail.
    isEmpty(self): Checks if the Linked List is empty and returns True or False.
    append(self, data): Adds an item to the end of the Linked List. Does not return a value.
    addHead(self, data): Adds an item to the front of the Linked List. Does not return a value.
    search(self, data): Searches for the desired item in the Linked List and returns Found or Not Found.
    index(self, data): Searches for the desired item in the Linked List and returns its index (0, 1, 2, 3, 4, ...). If not found, returns -1.
    size(self): Returns the size of the Linked List.
    pop(self, pos): Removes the item at the given index pos from the Linked List and returns Success or Out of Range

append -> AP
addHead -> AH
search -> SE
index -> ID
size -> SI
pop -> PO
    

Enter Input : SE 2020,SI,ID KMITL,PO 1
Not Found 2020 in Empty
Linked List size = 0 : Empty
Index (KMITL) = -1 : Empty
Out of Range | Empty
Linked List : Empty
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next: "Node | None" = None

class LinkedList:
    def __init__(self):
        self.head: "Node | None" = None

    def __str__(self):
        if self.head is None:
            return "Empty"
        cur = self.head
        s = str(cur.value) + " "
        while cur.next is not None:
            cur = cur.next
            s += str(cur.value) + " "
        return s

    def isEmpty(self):
        return self.head is None

    def addHead(self, item):
        new = Node(item)
        new.next = self.head
        self.head = new

    def append(self, item):
        if self.head is None:
            self.addHead(item)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def index(self, item):
        if self.head is None:
            return -1
        counter = 0
        cur = self.head
        while True:
            if cur.value == item:
                return counter
            if cur.next is None:
                return -1
            cur = cur.next
            counter += 1

    def search(self, item):
        if self.index(item) == -1:
            return "Not Found"
        return "Found"

    def size(self):
        if self.head is None:
            return 0
        c = 1
        cur = self.head
        while cur.next is not None:
            c += 1
            cur = cur.next
        return c

    def pop(self, pos):
        if self.head is None or pos < 0:
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
            return "Success"

        cur = self.head
        for _ in range(pos - 1):
            if cur.next is None:
                return "Out of Range"
            cur = cur.next
        if cur.next is None:
            return "Out of Range"
        removed = cur.next
        cur.next = removed.next
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    i = i.strip()
    cmd, arg = i[:2], i[3:]
    if cmd == "AP":
        L.append(arg)
    elif cmd == "AH":
        L.addHead(arg)
    elif cmd == "SE":
        print(f"{L.search(arg)} {arg} in {L}")
    elif cmd == "SI":
        print(f"Linked List size = {L.size()} : {L}")
    elif cmd == "ID":
        print(f"Index ({arg}) = {L.index(arg)} : {L}")
    elif cmd == "PO":
        before = f"{L}"
        k = L.pop(int(arg))
        if k == "Success":
            print(f"{k} | {before}-> {L}")
        else:
            print(f"{k} | {before}")

print("Linked List :", L)
