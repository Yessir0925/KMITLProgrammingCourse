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
w, h = int(h), int(w)

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
    if h%2 == 0:
        if slicePointer % 2 == 1:
            DLMatrix[slicePointer] = (DLMatrix[slicePointer])[::-1]
        for IncrementRowPointer in range(w):
            NumList[CounterNumList] = DLMatrix[slicePointer][IncrementRowPointer]
            CounterNumList += 1
    else:
        if slicePointer % 2 == 0:
            DLMatrix[slicePointer] = (DLMatrix[slicePointer])[::-1]
        for IncrementRowPointer in range(w):
            NumList[CounterNumList] = DLMatrix[slicePointer][IncrementRowPointer]
            CounterNumList += 1

"""
12,11,10,9,5,6,7,8,4,3,2,1
12  5  4
11  6  3
10  7  2
9   8  1

[12]  [5]  [4]
[11]  [6]  [3]
[10]  [7]  [2]
[9]  [8]  [1]
"""

w, h = h,w

print(NumList)

DLMatrix = [[None] * w for _ in range(h)]

CounterNumList = 0
for r in range(w):#0,1,2
    for c in range(h): #0,1,2,3
        DLMatrix[c][r] = NumList[CounterNumList]
        CounterNumList += 1

for Rows in DLMatrix:
    print(" ".join(f"{x:>{w}}" for x in Rows))

print("===== End of program =====")