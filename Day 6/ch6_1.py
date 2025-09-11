"""Write a Python program to receive an integer and calculate the sum based on the following conditions:

If the number is odd, add it to the sum.
If the number is even, subtract it from the sum.
if the number is -1, stop the calculation"""

""" *** Sum odd / Subtract even ***
Enter numbers : 47 89 63
Sum is 199
===== End of program ====="""


print(" *** Sum odd / Subtract even ***")
usrinp = input("Enter numbers : ")
parts = usrinp.split()
numbers = []
for y in parts:
    numbers.append(int(y))


total = 0
for i in numbers:
    if i == -1:
        break
    elif i % 2 == 0:
        total -= i
    elif i % 2 == 1:
        total += i
print(f"Sum is {total:,}")
print("===== End of program =====")