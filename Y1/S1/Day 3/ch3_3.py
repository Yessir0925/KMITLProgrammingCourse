""" *** Data type integer float string ***
Enter a word : 13
13 * 2 = 26"""

print(" *** Data type integer float string ***")
usrinp = input("Enter a word : ")
try:
    usrinp = int(usrinp)
    print(f'{usrinp} * 2 = {usrinp * 2}')
except ValueError:
    try: 
        usrinp = float(usrinp)
        print(f'{usrinp:.3f} / 3 = {(usrinp/3):.3f}')
    except ValueError:
        print(usrinp, usrinp, usrinp, sep=' ')