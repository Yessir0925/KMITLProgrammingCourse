h = int(input("Enter height: "))
W = 2*h - 1   # width per pyramid

for r in range(h):              # row
    # Left pyramid (inverted)
    for c in range(W):
        if r <= c <= W-r-1:
            print("*", end="")
        else:
            print(" ", end="")

    print(" | ", end="")        # separator

    # Right pyramid (upright)
    for c in range(W):
        if h-r-1 <= c <= h+r-1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
