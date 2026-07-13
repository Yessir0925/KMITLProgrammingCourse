"""Receive input in Infix notation and display 
the result in Postfix notation. The operators used are: +, -, *, /, ^.

Enter Infix : a+b
Postfix : ab+

Enter Infix : a+b*c
Postfix : abc*+

Enter Infix : a+b*c-(d/e+f)*g
Postfix : abc*+de/f+g*-
"""

Stack = []

dwa = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

usrinp = input("Enter Infix : ")

print("Postfix : ", end='')

for ch in usrinp:

    if ch.isalnum():
        print(ch, end='')

    elif ch == '(':
        Stack.append(ch)

    elif ch == ')':
        while Stack and Stack[-1] != '(':
            print(Stack.pop(), end='')
        Stack.pop()

    else:
        while (Stack and Stack[-1] != '(' and (dwa[Stack[-1]] > dwa[ch] or (dwa[Stack[-1]] == dwa[ch] and ch != '^'))):

            print(Stack.pop(), end='')

        Stack.append(ch)

while Stack:
    print(Stack.pop(), end='')
