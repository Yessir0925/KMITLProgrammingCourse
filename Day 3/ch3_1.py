""" *** Number Manipulation ***
Enter a whole number : 256
256 is even.
absolute value of 256 ==> 256"""

print(" *** Number Manipulation ***")
usrinp = int(input("Enter a whole number : "))
if (usrinp%2) == 0:
    print(usrinp,"is even.")
else:
    print(usrinp,"is odd.")
modusrinp = usrinp
if usrinp < 0:
    modusrinp = 0 + (-1*usrinp)
print(f'absolute value of {usrinp} ==> {modusrinp}')
    
