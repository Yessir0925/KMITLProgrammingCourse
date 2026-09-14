l = list(map(int, input("Enter Input : ").split()))

# only the slots holding positive integers and zero take part in the sort
slot = [i for i in range(len(l)) if l[i] >= 0]
for i in range(len(slot) - 1):
    small = i
    for j in range(i + 1, len(slot)):
        if l[slot[j]] < l[slot[small]]:
            small = j
    l[slot[i]], l[slot[small]] = l[slot[small]], l[slot[i]]

print(*l)
