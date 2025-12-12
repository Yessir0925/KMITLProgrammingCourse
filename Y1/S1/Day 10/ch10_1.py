"""
 *** Find Total lines ***
Enter file name : license.txt
property => <_io.TextIOWrapper name='license.txt' mode='r' encoding='UTF-8'>
Total lines : 21
===== End of progam =====
"""

print(" *** Find Total lines ***")
filename = str(input("Enter file name : "))

linesint = 0
try:
    f = open(filename, 'r', encoding="utf-8")
    print(f"property => <_io.TextIOWrapper name='{filename}' mode='r' encoding='UTF-8'>")
    for lines in f.readlines():
        linesint += 1
    print(f"Total lines : {linesint:,}")
except FileNotFoundError:
    print("File not found")

print("===== End of progam =====")