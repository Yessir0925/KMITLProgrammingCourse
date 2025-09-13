"""
Create an input for i and N where i is the power and N is the repitition

1+n**1+n**2+n**3=X

"""

print(" ***Start Program***")
x, n = input("Enter i and N = ").split()
x, n  = int(x), int(n)

DisplayLine = ""
#Assign empty string, None doesnt work
TotalSum = 0
for i in range(n):
    PoweredNumber = x**i
    if i != 0:
        DisplayLine = str(DisplayLine) + "+" + str(PoweredNumber)
    else:
        DisplayLine = str(PoweredNumber)
    TotalSum = TotalSum + int(PoweredNumber)

print(DisplayLine + f"={TotalSum}")