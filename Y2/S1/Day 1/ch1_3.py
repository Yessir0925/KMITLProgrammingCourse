"""
Write a program to accept an integer number up to 30 digits and then find the sum of each digit.

Example:

    - Input number 123 => 1+2+3=6

    - Input number 7892 => 7+8+9+2=26

    - Input number 32189657 => 3+2+1+8+9+6+5+7=41

 *** Summation of each digit ***
Enter a positive number : 123
Summation of each digit =  6    
    
"""
print(" *** Summation of each digit ***")
inp = str(input("Enter a positive number : "))
final = 0

try:
    for i in inp:
        final += int(i)
    print(f"Summation of each digit =  {final}")

except ValueError as a:
    print(f"Invalid Input: {a}")
    raise SystemExit