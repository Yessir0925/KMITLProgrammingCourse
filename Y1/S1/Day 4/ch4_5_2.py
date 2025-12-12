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

    # GCD of three numbers (inline, no def)
    a_abs = abs(a)
    b_abs = abs(b)
    c_abs = abs(c)

    while b_abs:
        a_abs, b_abs = b_abs, a_abs % b_abs
    gcd_ab = a_abs

    a_abs = gcd_ab
    b_abs = c_abs
    while b_abs:
        a_abs, b_abs = b_abs, a_abs % b_abs
    g = a_abs

    a //= g
    b //= g
    c //= g

    print(f"f1 ==> {a * g}x + {b * g}y + {c * g} = 0")
    print(f"f2 ==> {a}x + {b}y + {c} = 0")

    if a < 0:
        a *= -1
        b *= -1
        c *= -1

    # Casing logic (inline)
    if a == 0:
        term_a = ""
    elif a == 1:
        term_a = "x"
    elif a == -1:
        term_a = "-x"
    else:
        term_a = str(a) + "x"

    if b == 0:
        term_b = ""
    elif b == 1:
        term_b = "+ y"
    elif b == -1:
        term_b = "- y"
    elif b > 0:
        term_b = f"+ {b}y"
    else:
        term_b = f"- {abs(b)}y"

    if c == 0:
        term_c = ""
    elif c > 0:
        term_c = f"+ {c}"
    else:
        term_c = f"- {abs(c)}"

    # Build final expression
    if term_a == "":
        if term_b == "":
            expression = term_c.strip()
        else:
            expression = term_b + " " + term_c
    else:
        expression = term_a + " " + term_b + " " + term_c

    print(f"f3 ==> {expression.strip()} = 0")

print("===== End of program =====")