"""
Write a program to receive input in the form of brackets. The opening brackets are: ( and [ and the closing brackets are: ) and ].

        Determine if the brackets can be paired correctly.
        Display the number of brackets needed to complete the pairs if they are incomplete.
        If all pairs are complete, display "Perfect".

Enter Input : [](]
2
"""

usrinp = input("Enter Input : ")
stack = []
needed = 0
pairs = {')': '(', ']': '['}

for ch in usrinp:
    if ch in '([':
        stack.append(ch)
    elif ch in ')]':
        if stack and stack[-1] == pairs[ch]:
            stack.pop()
        elif stack:
            needed += 1
            stack.pop()
            if stack and stack[-1] == pairs[ch]:
                stack.pop()
            else:
                needed += 1
        else:
            needed += 1

needed += len(stack)

if needed == 0:
    print(needed)
    print("Perfect ! ! !")
else:
    print(needed)