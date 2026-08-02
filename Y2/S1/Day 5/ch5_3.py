"""
Instructions for Merging Two Linked Lists Without Creating a LinkedList Class

    Node Class:
        Ensure you have a Node class that contains a value and a reference to the next Node.

    Functions to Implement:
        createList(): Creates a LinkedList from a given list of values and returns the head of the LinkedList.
        printList(): Prints all the elements of a LinkedList starting from the given head.
        mergeOrderList(): Merges two LinkedLists into one in ascending order of their values and returns the head of the merged LinkedList.


****Using sort() is prohibited. If found, no points will be awarded.****

****Creating a LinkedList class is prohibited.****
class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
    def __str__(self):
        ### Code Here ###

def createList(l=[]):
    ### Code Here ###

def printList(H):
    ### Code Here ###

def mergeOrderesList(p,q):
    ### Code Here ###

#################### FIX comand ####################   
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)


Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
LL1 : 1 3 5 7 10 20 22 
LL2 : 4 6 7 8 15 
Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22 """

class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next: "Node | None" = None


def createList(values):
    head: "Node | None" = None
    tail: "Node | None" = None

    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node

    return head


def printList(head):
    cur = head
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    print()


def mergeOrderList(head1, head2):
    dummy = Node(0)
    tail = dummy

    p1 = head1
    p2 = head2

    while p1 is not None and p2 is not None:

        if p1.data <= p2.data:
            tail.next = Node(p1.data)
            p1 = p1.next
        else:
            tail.next = Node(p2.data)
            p2 = p2.next
        assert tail.next is not None
        tail = tail.next

    while p1 is not None:
        tail.next = Node(p1.data)
        assert tail.next is not None
        tail = tail.next
        p1 = p1.next

    while p2 is not None:

        tail.next = Node(p2.data)
        assert tail.next is not None
        tail = tail.next
        p2 = p2.next

    return dummy.next


inp = input("Enter 2 Lists : ").split()

list1 = []
list2 = []

if len(inp) > 0 and inp[0] != "":
    list1 = inp[0].split(",")

if len(inp) > 1 and inp[1] != "":
    list2 = inp[1].split(",")

head1 = createList(list1)
head2 = createList(list2)

print("LL1 :", end=" ")
printList(head1)

print("LL2 :", end=" ")
printList(head2)

merged = mergeOrderList(head1, head2)

print("Merge Result :", end=" ")
printList(merged)