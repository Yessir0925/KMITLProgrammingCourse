"""Kritsada had a brilliant idea to create his own Text Editor similar to VIM, which operates in a single mode called Command Mode (our input). The program includes 5 commands: Insert (I), Left (L), Right (R), Backspace (B), and Delete (D). (The functionality of each command is explained below.) However, Kritsada lacks programming skills, so he requested help from computer engineering students to develop the Text Editor he envisioned. The output should display the remaining word after executing the commands and the position of the cursor.
Explanation of the 5 Input Commands:

    I <word>: Inserts the word at the current cursor position. After inserting the word, the cursor moves to the end of the inserted word.

    L: Moves the cursor one position to the left. If the cursor is already at the leftmost position, nothing happens.

    R: Moves the cursor one position to the right. If the cursor is already at the rightmost position, nothing happens.

    B: Deletes the character to the left of the cursor. If the cursor is already at the leftmost position, nothing happens.

    D: Deletes the character to the right of the cursor. If the cursor is already at the rightmost position, nothing happens.


Enter Input : I Apple,I Bird,I Cat
Apple Bird Cat | """

class Node:
    def __init__(self, data):
        self.data = data
        self.prev: "Node | None" = None
        self.next: "Node | None" = None


class TextEditor:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None
        self.cursor: "Node | None" = None  # node to the right of the cursor

    def insert(self, data):
        node = Node(data)

        # insert at end
        if self.cursor is None:
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                assert self.tail is not None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            return

        # insert before cursor
        node.next = self.cursor
        node.prev = self.cursor.prev

        if self.cursor.prev is not None:
            self.cursor.prev.next = node
        else:
            self.head = node

        self.cursor.prev = node

    def left(self):
        if self.cursor is None:
            self.cursor = self.tail
        elif self.cursor.prev is not None:
            self.cursor = self.cursor.prev

    def right(self):
        if self.cursor is None:
            return

        if self.cursor.next is None:
            self.cursor = None
        else:
            self.cursor = self.cursor.next

    def backspace(self):
        # nothing left of cursor
        if self.cursor == self.head:
            return

        # delete last node
        if self.cursor is None:
            if self.tail is None:
                return

            delete = self.tail
            self.tail = delete.prev

            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
            return

        delete = self.cursor.prev

        if delete is None:
            return

        if delete.prev is None:
            self.head = self.cursor
            self.cursor.prev = None
        else:
            delete.prev.next = self.cursor
            self.cursor.prev = delete.prev

    def delete(self):
        if self.cursor is None:
            return

        delete = self.cursor

        if delete.prev is None:
            self.head = delete.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        else:
            delete.prev.next = delete.next
            if delete.next is not None:
                delete.next.prev = delete.prev
            else:
                self.tail = delete.prev

        self.cursor = delete.next

    def display(self):
        cur = self.head

        while cur is not None and cur != self.cursor:
            print(cur.data, end=" ")
            cur = cur.next

        print("|", end=" ")

        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next

        print()


editor = TextEditor()

commands = input("Enter Input : ").split(",")

for cmd in commands:
    if cmd.startswith("I "):
        editor.insert(cmd[2:])
    elif cmd == "L":
        editor.left()
    elif cmd == "R":
        editor.right()
    elif cmd == "B":
        editor.backspace()
    elif cmd == "D":
        editor.delete()

editor.display()