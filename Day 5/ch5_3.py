""" *** Binary to Decimal ***
Enter binary number : 111
111 ==> 7
===== End of program ======"""

print(" *** Binary to Decimal ***")
s = input("Enter binary number : ")

binary_str = ""
for ch in s:
    if ch == '$':
        break
    if ch == '0' or ch == '1':
        binary_str += ch
    else:
        continue

if binary_str == "":
    print("None")
else:
    decimal = int(binary_str, 2)
    print(f"{binary_str} ==> {decimal}")
print("===== End of program ======")