"""
Receive two integer input. If the product of the two numbers is 
greater than 1000, show the sum of the two numbers. 
If the product is less than or equal to 1000, 
show the product of the two numbers. 

*** multiplication or sum ***
Enter num1 num2 : 20 30
The result is 600

"""

print(f"*** multiplication or sum ***")
num1, num2 = input("Enter num1 num2 : ").split()

try:
    num1 = int(num1)
    num2 = int(num2)
    if (num1 * num2) > 1000:
        print(f"The result is {num1 + num2}")
    else:
        print(f"The result is {num1 * num2}")

except ValueError as a:
    print(f"Invalid Input: {a}")
    raise SystemExit
