"""Write a class for a Doubly Linked List which includes the following methods:

    def __init__(self): Initializes the linked list.

    def __str__(self): Returns a string representing the values in the linked list.

    def str_reverse(self): Returns a string representing the values in the linked list from back to front.

    def isEmpty(self): Returns whether the list is empty.

    def append(self, data): Adds a node with the given data to the end of the linked list.

    def insert(self, index, data): Inserts data at the specified index.

    def remove(self, data): Removes and returns the node with the given data.
        When inserting, the new data replaces the position of the old data, and the old data is moved to follow the new data.

Input format is as follows:

    append -> A
    add_before -> Ab
    insert -> I
    remove -> R

******* Use the Node class to implement the Linked List. Do not use Python's built-in list.*********


Enter Input : A 3,A 4,Ab 0,I 1:2
linked list : 3
reverse : 3
linked list : 3->4
reverse : 4->3
linked list : 0->3->4
reverse : 4->3->0
index = 1 and data = 2
linked list : 0->2->3->4
reverse : 4->3->2->0"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None