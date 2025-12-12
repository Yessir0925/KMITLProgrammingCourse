print(" *** Maximum occurence ***")
usrinp = input("Enter numbers : ")
splits = usrinp.split()

numlist = []
for s in splits:
    numlist.append(int(s))

print(numlist)

freq = {}
for n in numlist:
    if n == -1:
        break
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

max_count = 0
for value in freq.values():
    if value > max_count:
        max_count = value

max_occ = []
for key in freq:
    if freq[key] == max_count:
        max_occ.append(key)

print(f"Max count = {max_count}")
print(f"Max occurence = {max_occ}")
print("===== End of program =====")