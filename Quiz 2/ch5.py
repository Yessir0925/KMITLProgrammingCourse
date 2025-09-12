print(" *** Spiral Matrix ***")
w, h = input("Enter width height : ").split()
w, h = int(w), int(h)

# create empty matrix
matrix = [[0]*w for _ in range(h)]

# directions: right, down, left, up
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0   # start going right
r, c = 0, 0

for val in range(1, w*h+1):
    matrix[r][c] = val
    # next cell
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    # if next step is outside or filled, turn direction
    if nr < 0 or nr >= h or nc < 0 or nc >= w or matrix[nr][nc] != 0:
        d = (d+1) % 4
        nr, nc = r + dirs[d][0], c + dirs[d][1]
    r, c = nr, nc

# print nicely
for row in matrix:
    for x in row:
        print(f"{x:02}", end=" ")
    print()

print("===== End of program =====")
