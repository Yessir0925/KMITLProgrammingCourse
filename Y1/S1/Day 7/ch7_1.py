"""
Output
 *** Adding number ***
Enter your words : John Martha Smith
John1 ahtraM2 Smith3 
==== End of program =====
"""

print(" *** Adding number ***")
usrinpraw = input("Enter your words : ").split()

usrinp = []
for i in range(len(usrinpraw)):
    word = usrinpraw[i]
    if i % 2 == 1:
        word = word[::-1]
    usrinp.append(word+str(i+1))

print(" ".join(usrinp))
print("==== End of program =====")