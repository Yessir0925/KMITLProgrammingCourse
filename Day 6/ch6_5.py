print(" *** Rectangle down-left-up-left ***")
w, h = map(int, input("Enter width height : ").split())

DLMatrix = [[0]*w for _ in range(h)]
val = w*h
for c in range(w):
    if c % 2 == 0:                 # even column: top -> bottom
        for r in range(h):
            DLMatrix[r][c] = val
            val -= 1
    else:                           # odd column: bottom -> top
        for r in range(h-1, -1, -1):
            DLMatrix[r][c] = val
            val -= 1

field = len(str(w*h))
for row in DLMatrix:
    print(" ".join(f"{x:>{field}}" for x in row))
print("===== End of program =====")