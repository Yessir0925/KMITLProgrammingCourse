print(" *** Center-starting Spiral Rectangle ***")
size, direction = input("Enter side direction: ").strip().split()
size = int(size)

# Direction order (clockwise): right, down, left, up
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
name_to_idx = {"right": 0, "down": 1, "left": 2, "up": 3}
d_idx = name_to_idx[direction]

grid = [[0] * size for _ in range(size)]

# Start: odd -> center; even -> top-left of the 2x2 center
if size % 2 == 0:
    r = c = size // 2 - 1
else:
    r = c = size // 2

cur = 1
total = size * size
grid[r][c] = cur
cur += 1
placed = 1
step_len = 1

while placed < total:
    for _ in range(2):  # two legs per step length
        dr, dc = dirs[d_idx]
        for _ in range(step_len):
            if placed >= total:
                break
            r += dr
            c += dc
            if 0 <= r < size and 0 <= c < size and grid[r][c] == 0:
                grid[r][c] = cur
                cur += 1
                placed += 1
        d_idx = (d_idx + 1) % 4
    step_len += 1

# Column alignment width
w = len(str(total))
for row in grid:
    print(" ".join(str(v).rjust(w) for v in row) + " ")
print("===== End of program ======")