print("*** Draw square ***")

def init_square(t, n):
    if t == 0:
        for i in range(n):
            line = ""
            for j in range(n):
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    line += "* "
                else:
                    line += "  "
            print(line.rstrip())
    elif t == 1:
        for i in range(1, n+1):
            line = ""
            for j in range(1, n+1):
                if i == 1:
                    line += f"{j:2d} "
                elif i == n:
                    line += f"{n-j+1:2d} "
                elif j == 1:
                    line += f"{i:2d} "
                elif j == n:
                    line += f"{n-i+1:2d} "
                else:
                    line += "   "
            print(line.rstrip())
    elif t == 2:
        if n % 2 == 0:
            print("Type 2 square doesn't support an even number")
            return
        for i in range(n):
            line = ""
            for j in range(n):
                if i == j or i + j == n-1:
                    line += "* "
                elif i == 0 or i == n-1 or j == 0 or j == n-1:
                    if (i + j) % 2 == 0:
                        line += "* "
                    else:
                        line += "@ "
                else:
                    line += "  "
            print(line.rstrip())

t, n = input("Enter type and size: ").split()
t, n = int(t), int(n)

init_square(t, n)

print("===== End of program =====")