""" *** 3-digit number ***
Enter 3-digit number : 123
123 => Odd Even Odd
1^2 + 2^3 + 3^4 = 90
===== End of program ====="""

def oddoreven(_):
    if int(_) % 2 == 1:
        return "Odd"
    else:
        return "Even"
print(" *** 3-digit number ***")
usrinp = input("Enter 3-digit number : ")
a, b, c = usrinp
CalcResult = (int(a)**2)+(int(b)**3)+(int(c)**4)
Calculation = (f'{a}^2 + {b}^3 + {c}^4 = {CalcResult:,d}')
print(f'{usrinp} => {oddoreven(a)} {oddoreven(b)} {oddoreven(c)}')
print(f"{Calculation}")
print("===== End of program =====")