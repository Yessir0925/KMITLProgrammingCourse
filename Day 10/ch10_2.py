"""
 *** Find Empty lines ***
Enter file name : mbox-short.txt
Empty lines => 217
Total lines => 1910
"""

print(" *** Find Empty lines ***")
filename = str(input("Enter file name : "))

emptylines = 0
totallines = 0
try:
    f = open(filename, 'r', encoding="utf-8")
    for line in f:
        lines = f.readlines()
        if line.strip() == "":
            emptylines += 1
        totallines += 1
        
    print(f"Empty lines => {emptylines}")
    print(f"Total lines => {totallines}")

except FileNotFoundError:
    print("File not found")