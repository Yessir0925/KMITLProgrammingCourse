print(" *** Pyramid-V ***")
h = int(input("Enter height : "))

cur = ord('Z')

for r in range(1, h + 1):
    print(" " * (h - r), end="")

    row = ""
    for _ in range(2 * r - 1):
        row += chr(cur)
        cur -= 1
        if cur < ord('A'):
            cur = ord('Z')

    print(row)

print("===== End of program =====")
