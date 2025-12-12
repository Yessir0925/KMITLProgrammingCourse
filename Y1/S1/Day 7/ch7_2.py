"""
 *** Remove ODD characters ***
Enter a string : abcdef
Even characters = bdf
===== End of program =====
"""

print(" *** Remove ODD characters ***")
usrinpraw = input("Enter a string : ")

output = []
for i in range(len(usrinpraw)):
    if i % 2 == 1:
        output.append(usrinpraw[i])

finalout = "".join(output)
print(f"Even characters = {finalout}")
print("===== End of program =====")