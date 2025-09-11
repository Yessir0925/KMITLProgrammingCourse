print(" *** Rectangle down-left-up-left ***")
w, h = [int(x) for x in input("Enter width height : ").split()]

rect = [[0] * w for _ in range(h)]
dirs = [(1, 0), (0, -1), (-1, 0), (0, -1)]
d = 0
r, c = 0, w - 1

for val in range(1, w * h + 1):
    rect[r][c] = val
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    if nr < 0 or nr >= h or nc < 0 or nc >= w or rect[nr][nc] != 0:
        d = (d + 1) % 4
        nr, nc = r + dirs[d][0], c + dirs[d][1]
    r, c = nr, nc

for row in rect:
    for x in row:
        print(f"{x:3}", end="")
    print()
print("===== End of program =====")