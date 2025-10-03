"""
 *** Histogram ***
Enter file name and word : license.txt in
Number of "in" => 8
Sum of line number => 34
Total lines => 21
 i  => **************************** 28
 t  => ************************     24
 o  => ************************     24
===== End of program =====
"""

print(" *** Histogram ***")
filename, word = input("Enter file name and word : ").split()

totallines = 0
try:
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            lines = f.readlines()
            totallines += 1


except FileNotFoundError:
    print("File not found")