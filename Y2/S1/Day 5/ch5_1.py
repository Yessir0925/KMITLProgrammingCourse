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
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def addHead(self, item):
        if self.head == None:
            self.head = Node(item)
        elif self.head != None:
            new = Node(item)
            new.next = self.head
            self.head = new

    def append(self, item):
        if self.head == None:
            self.addHead(item)
        else:
            cur = self.head
            while True:
                if cur.next == None:
                    cur.next = Node(item)
                    return
                cur = cur.next

    def index(self, item):
        if self.isEmpty():
            return -1
        counter = 0
        cur = self.head
        while True:
            if cur.next == None and cur.value != item:
                return -1
            elif cur.value == item:
                return counter
            else:
                cur = cur.next
                counter += 1

    def search(self, item):
        if self.isEmpty():
            return "Not Found"
        cur = self.head
        if self.index(item) == -1:
            return "Not Found"
        else:
            return "Found"

    def size(self):
        if self.isEmpty():
            return 0
        c = 1
        cur = self.head
        while True:
            if cur.next == None:
                return c
            else:
                c += 1
                cur = cur.next
                
    def pop(self, pos):
        if self.isEmpty() or pos < 0:
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
            return "Success"

        cur = self.head
        for i in range(pos-1):
            if cur.next != None:
                cur = cur.next
            else:
                return "Out of Range"
        if cur.next == None:
            return "Out of Range"
        cur.next = cur.next.next
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
