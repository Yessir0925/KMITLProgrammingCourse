"""
 *** Rectangle down-left-up-left ***
Enter width height : 4 4
 16  9  8  1
 15 10  7  2
 14 11  6  3
 13 12  5  4
===== End of program =====
"""

print(" *** Rectangle down-left-up-left ***")
w, h = input("Enter width height : ").split()
w, h = int(w), int(h)

NumList = []
for numListInsertion in range(1,(w*h)+1,+1):
    NumList.append(numListInsertion)

DLMatrix = [[],[]]
#[Column],[Row]

#Set horPointer to end of column
#Set vertPointer to top of row

#increment vertPointer till finish set
#Minus horPointer and go to top then repeat

"""
1. Sort pointers
2. Figure out flipping
    1. If end of then break? and all in same loop
"""

NumListPointer = 0
for vP in range(h):
    for hP in range(w):
        
