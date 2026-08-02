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
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None
        self.previous: Node | None = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def isEmpty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        cur = self.head
        out = []

        while cur is not None:
            out.append(str(cur.data))
            cur = cur.next

        return "->".join(out)

    def str_reverse(self) -> str:
        cur = self.tail
        out = []

        while cur is not None:
            out.append(str(cur.data))
            cur = cur.previous

        return "->".join(out)

    def append(self, data: int) -> None:
        node = Node(data)

        if self.head is None:
            self.head = self.tail = node
            return

        assert self.tail is not None

        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def addHead(self, data: int) -> None:
        node = Node(data)

        if self.head is None:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.previous = node
        self.head = node

    def length(self) -> int:
        cnt = 0
        cur = self.head

        while cur is not None:
            cnt += 1
            cur = cur.next

        return cnt

    def insert(self, index: int, data: int) -> None:
        if index < 0 or index > self.length():
            print("Data cannot be added")
            return

        print(f"index = {index} and data = {data}")

        if index == 0:
            self.addHead(data)
            return

        if index == self.length():
            self.append(data)
            return

        cur = self.head

        for _ in range(index):
            assert cur is not None
            cur = cur.next

        assert cur is not None
        assert cur.previous is not None

        node = Node(data)

        prev = cur.previous

        prev.next = node
        node.previous = prev

        node.next = cur
        cur.previous = node

    def remove(self, data: int) -> None:
        cur = self.head
        idx = 0

        while cur is not None:
            if cur.data == data:
                break
            cur = cur.next
            idx += 1

        if cur is None:
            print("Not Found!")
            return

        print(f"removed : {data} from index : {idx}")

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        if cur == self.head:
            self.head = cur.next
            assert self.head is not None
            self.head.previous = None
            return

        if cur == self.tail:
            self.tail = cur.previous
            assert self.tail is not None
            self.tail.next = None
            return

        assert cur.previous is not None
        assert cur.next is not None

        cur.previous.next = cur.next
        cur.next.previous = cur.previous