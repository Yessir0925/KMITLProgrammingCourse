print(" *** Digit count and Summation ***")
usrinp = input("Enter an integer : ")
strusrinp = str(usrinp)
print(f"Entered number = {int(usrinp):,}")
x = len(strusrinp)
print(f"Total digits are:  {x}")
total = 0
while 0 < x:
    x = x - 1
    total = total + int((strusrinp)[x])
print(f'Summation = {total}')