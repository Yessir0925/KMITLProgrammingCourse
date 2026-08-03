def staircase(n):
    if n == 0:
        print("Not Draw!")
        return

    step(createString(n), n)


def createString(n):
    if n > 0:
        return "_" * (n - 1) + "#"
    return "#" * abs(n)


def step(myString, n):
    print(myString)

    if n > 0 and "_" in myString:
        index = myString.rfind("_")
        myString = myString[:index] + "#" + myString[index + 1:]
        step(myString, n)

    elif n < 0 and myString.count("#") > 1:
        index = myString.find("#")
        myString = myString[:index] + "_" + myString[index + 1:]
        step(myString, n)


print(" *** Stair case ***")
staircase(int(input("Enter Input : ")))
print("===== End of program =====")