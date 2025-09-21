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

NumList = NumList[::-1]

DLMatrix = [[None] * w for _ in range(h)]

CounterNumList = 0
for hDP in range(h):
    for wDP in range(w):
        DLMatrix[hDP][wDP] = NumList[CounterNumList]
        CounterNumList += 1

CounterNumList = 0
for slicePointer in range(len(DLMatrix)):
    if slicePointer % 2 == 1:
        DLMatrix[slicePointer] = (DLMatrix[slicePointer])[::-1]
    for IncrementRowPointer in range(h):
        NumList[CounterNumList] = DLMatrix[slicePointer][IncrementRowPointer]
        CounterNumList += 1

CounterNumList = 0
for hDP in range(h):
    for wDP in range(w):
        DLMatrix[wDP][hDP] = NumList[CounterNumList]
        CounterNumList += 1

for row in DLMatrix:
    print(" ".join(f"{x:>{w}}" for x in row))

print("===== End of program =====")