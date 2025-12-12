print(" *** Linear Formula ***")
x1, y1, x2, y2 = input("Enter x1 y1 x2 y2: ").split()
print(f"({x1},{y1}) ==> ({x2},{y2})")

x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

if x1 == x2:
    print(f"Vertical line ==> x = {x1}.")
elif y1 == y2:
    print(f"Horizontal line ==> y = {y1}.")
else:
    a = y2 - y1
    b = x1 - x2
    c = (x2 * y1) - (x1 * y2)

    def gcd_two_numbers(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def gcd_three_numbers(a, b, c):
        return gcd_two_numbers(gcd_two_numbers(a, b), c)

    def casing(j, var):
        if j == 0:
            return ""
        elif j == 1:
            return f"+ {var}"
        elif j == -1:
            return f"- {var}"
        elif j > 0:
            return f"+ {j}{var}"
        else:
            if j < 0:
                o = j*-1
            else:
                o = j
            return f"- {o}{var}"

    print(f"f1 ==> {a}x + {b}y + {c} = 0")

    g = gcd_three_numbers(a, b, c)
    a //= g
    b //= g
    c //= g
    print(f"f2 ==> {a}x + {b}y + {c} = 0")

    if a < 0:
        a *= -1
        b *= -1
        c *= -1

    if a == 0:
        term_a = ""
    elif a == 1:
        term_a = "x"
    elif a == -1:
        term_a = "-x"
    else:
        term_a = str(a) + "x"

    term_b = casing(b, "y")
    term_c = casing(c, "")

    if term_a == "":
        if term_b == "":
            expression = term_c.strip()
        else:
            expression = term_b + " " + term_c
    else:
        expression = term_a + " " + term_b + " " + term_c

    print(f"f3 ==> {expression.strip()} = 0")

print("===== End of program =====")