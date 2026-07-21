"""
Write a program to check if an expression has complete parentheses using a Stack to solve the problem.

The program should be able to indicate the cause of the error, if any:

    Mismatched opening and closing parentheses
    Excess closing parentheses
    Excess opening parentheses

Then display the result according to the example.

Enter expresion : [[)))))
[[))))) Unmatch open-close  

Enter expresion : [[))
[[)) Unmatch open-close

Enter expresion : (())))
(()))) close paren excess

Enter expresion : (((
((( open paren excess   3 : (((

Enter expresion : (a+c)(a-b)*c(-a
(a+c)(a-b)*c(-a open paren excess   1 : (

Enter expresion : (([]))
(([])) MATCH
"""

usrinp = input("Enter expresion : ")
stack = []

for ch in usrinp:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack:
            print(usrinp, "close paren excess")
            break

        top = stack[-1]
        if (ch == ')' and top == '(') or (ch == ']' and top == '[') or (ch == '}' and top == '{'):
            stack.pop()
        else:
            print(usrinp, "Unmatch open-close")
            break
else:
    if stack:
        print(usrinp, "open paren excess   {} : {}".format(len(stack), ''.join(stack)))
    else:
        print(usrinp, "MATCH")