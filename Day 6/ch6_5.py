"""
*** Rectangle down-left-up-left ***
Enter width height : 4 3
12  7  6  1
11  8  5  2
10  9  4  3
===== End of program =====
"""
#Simple For Loop

print("*** Rectangle down-left-up-left ***")
w,h = map(int,input("Enter width height : ").split())

Value = 1
DLMatrix = [[None]*w for _ in range(h)]


Switch = False
for c in range(w-1,-1,-1):
    if Switch == False:
        for r in range(0,h,+1):
            DLMatrix[r][c] = Value
            Value += 1
    else:
        for r in range(h-1,-1,-1):
            DLMatrix[r][c] = Value
            Value += 1
    Switch = not Switch

for rows in DLMatrix:
    print(" ".join(f"{pw:>{w}}" for pw in rows))

print("===== End of program =====")