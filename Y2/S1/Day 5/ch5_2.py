"""Write a class for a Doubly Linked List which includes the following methods:

    def __init__(self): Initializes the linked list.

    def __str__(self): Returns a string representing the values in the linked list.

    def str_reverse(self): Returns a string representing the values in the linked list from back to front.

    def isEmpty(self): Returns whether the list is empty.

    def append(self, data): Adds a node with the given data to the end of the linked list.

    def insert(self, index, data): Inserts data at the specified index.
    When inserting, the new data replaces the position of the old data, and the old data is moved to follow the new data.

    def remove(self, data): Removes and returns the node with the given data.

Input format is as follows:

    append -> A
    add_before -> Ab
    insert -> I
    remove -> R

******* Use the Node class to implement the Linked List. Do not use Python's built-in list.*********


    expected = (
        "Enter Input : A 3,A 4,Ab 0,I 1:2\n"
        "linked list : 3\n"
        "reverse : 3\n"
        "linked list : 3->4\n"
        "reverse : 4->3\n"
    )
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None
        self.previous: "Node | None" = None

class LinkedList:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None
        self.length = 0

    def __str__(self):
        if self.head is None:
            return ""
        cur = self.head
        parts = [str(cur.data)]
        while cur.next is not None:
            cur = cur.next
            parts.append(str(cur.data))
        return "->".join(parts)

    def str_reverse(self):
        if self.tail is None:
            return ""
        cur = self.tail
        parts = [str(cur.data)]
        while cur.previous is not None:
            cur = cur.previous
            parts.append(str(cur.data))
        return "->".join(parts)

    def isEmpty(self):
        return self.head is None and self.tail is None

    def append(self, data):
        #Command - A
        new = Node(data)
        self.length += 1
        if self.head is None:
            self.head = new
        if self.tail is None:
            self.tail = new
            return
        cur = self.tail
        cur.next = new
        new.previous = cur
        self.tail = new

    def insert(self, index, data):
        #Command - I
    
        new = Node(data)
        if self.head is None or index <= 0:
            new.next = self.head
            if self.head is not None:
                self.head.previous = new
            self.head = new
            if self.tail is None:
                self.tail = new
            self.length += 1
            return

        cur = self.head
        counter = 0
        while counter < index and cur.next is not None:
            cur = cur.next
            counter += 1

        if counter == index:
            new.previous = cur.previous
            new.next = cur
            cur.previous.next = new
            cur.previous = new
        else:
            new.previous = self.tail
            self.tail.next = new
            self.tail = new
        self.length += 1

    def remove(self, data):
        index = 0
        if self.head is None:
            return "Not Found!"
        cur = self.head

        while True:
            if cur.data == data:
                if cur.next is None:
                    cur.previous.next = None
                    return index
                cur.next.previous = cur.previous
                if index == 0:
                    self.head = cur.next
                    return index
                cur.previous.next = cur.next
                return index
            if cur.next is None:
                return "Not Found!"
            cur = cur.next
            index += 1
        return "Not Found!"

    

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    i = i.strip()
    cmd, arg = i.split(" ", 1)
    if cmd == "A":
        L.append(arg)
        print(f"linked list : {L}")
        print(f"reverse : {L.str_reverse()}")
    elif cmd == "Ab":
        if int(arg) < 0:
            print("Data cannot be added")
            raise SystemExit
        L.insert(0, arg)
        print(f"linked list : {L}")
        print(f"reverse : {L.str_reverse()}")
    elif cmd == "I":
        index, data = arg.split(":")
        index = int(index)
        if index < 0 or index > L.length:
            print("Data cannot be added")
        else:
            L.insert(index, data)
            print(f"index = {index} and data = {data}")
        print(f"linked list : {L}")
        print(f"reverse : {L.str_reverse()}")
    elif cmd == "R":
        removed = L.remove(arg)
        if removed == "Not Found!":
            print("Not Found!")
            print(f"linked list : ")
            print(f"reverse : ")
            continue
        print(f"removed : {arg} from index : {removed}" )
        #1 from index : 0
        print(f"linked list : {L}")
        print(f"reverse : {L.str_reverse()}")