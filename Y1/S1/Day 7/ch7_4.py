"""
 *** String Rotation ***
Enter string / step : abc / 1
The rotation times = 3
0 ==> abc
1 ==> bca
2 ==> cab
3 ==> abc
===== End of program =====
"""

print(" *** String Rotation ***")
line = input("Enter string / step : ")
slash_pos = line.find("/")
if slash_pos == -1:
    left = line.strip()
    right = "0"
else:
    left = line[:slash_pos].strip()
    right = line[slash_pos + 1:].strip()
String = left
Step = int(right)
n = len(String)
a = n
b = Step if Step >= 0 else -Step
while b != 0:
    tmp = a % b
    a = b
    b = tmp
g = a if a != 0 else 1
rotationtime = 0
if n != 0:
    rotationtime = n // g
print("The rotation times = " + str(rotationtime))
k = 0
if n != 0:
    k = Step % n
width = len(str(rotationtime))

i = 0
while i <= rotationtime:
    show = True
    if rotationtime > 20 and not (i < 5 or i > rotationtime - 5):
        if i == 5:
            print(" . . . . .")
        show = False
    if show:
        idx = str(i)
        while len(idx) < width:
            idx = "0" + idx
        if n == 0:
            rotated = ""
        else:
            shift = (i * k) % n
            rotated = String[shift:] + String[:shift]
        print(idx + " ==> " + rotated)
    i += 1

print("===== End of program =====")