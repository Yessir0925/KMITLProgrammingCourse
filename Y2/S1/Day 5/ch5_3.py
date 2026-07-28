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