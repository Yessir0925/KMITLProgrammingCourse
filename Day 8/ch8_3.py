print(" *** Recite the multiplication table ***")

tokens_str = input("Enter pattern for child 1 to 3 (-1 for sep) : ").split()
tokens = []
for t in tokens_str:
    tokens.append(int(t))

patterns = [[], [], []]
ci = 0
for x in tokens:
    if x == -1:
        if ci < 2:
            ci += 1
        else:
            break
    else:
        patterns[ci].append(x)

s0 = " ".join(str(v) for v in patterns[0])
s1 = " ".join(str(v) for v in patterns[1])
s2 = " ".join(str(v) for v in patterns[2])

if len(s0) > 0:
    s0 += " "
if len(s1) > 0:
    s1 += " "
if len(s2) > 0:
    s2 += " "

print("")
print("Pattern for child 1 : " + s0)
print("Pattern for child 2 : " + s1)
print("Pattern for child 3 : " + s2)

if len(patterns[0]) == 0 or len(patterns[1]) == 0 or len(patterns[2]) == 0:
    print("This year they never recite same multiplication table !!!")
else:
    day_found = 0
    for day in range(1, 366):
        a = patterns[0][(day - 1) % len(patterns[0])]
        b = patterns[1][(day - 1) % len(patterns[1])]
        c = patterns[2][(day - 1) % len(patterns[2])]
        if a == b and b == c:
            day_found = day
            break
    if day_found == 0:
        print("This year they never recite same multiplication table !!!")
    else:
        print(f"They recite same multiplication table in {day_found} days")