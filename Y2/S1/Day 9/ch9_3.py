def bubbleSort(l):
    l = l[:]
    for last in range(len(l) - 1, 0, -1):
        for j in range(last):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

digit = [int(c) for c in input("Enter Input : ").strip()]
asc = bubbleSort(digit)
desc = asc[::-1]

repeat = False
for i in range(len(asc) - 1):
    if asc[i] == asc[i + 1]:
        repeat = True

if asc[0] == asc[-1]:
    print("Repdrome")
elif digit == asc:
    print("Plaindrome" if repeat else "Metadrome")
elif digit == desc:
    print("Nialpdrome" if repeat else "Katadrome")
else:
    print("Nondrome")
