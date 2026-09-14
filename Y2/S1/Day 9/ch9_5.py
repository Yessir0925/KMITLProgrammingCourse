compare = 0

def partition(l, low, high, pivot):
    global compare
    if pivot == 'first':
        p = low
    elif pivot == 'last':
        p = high
    else:
        p = (low + high) // 2
    l[low], l[p] = l[p], l[low]
    key = l[low]
    i = low
    for j in range(low + 1, high + 1):
        compare += 1
        if l[j] < key:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[low], l[i] = l[i], l[low]
    return i

def quickSort(l, low, high, pivot):
    if low < high:
        m = partition(l, low, high, pivot)
        quickSort(l, low, m - 1, pivot)
        quickSort(l, m + 1, high, pivot)

def countCompare(l, pivot):
    global compare
    compare = 0
    quickSort(l[:], 0, len(l) - 1, pivot)
    return compare

print(" *** Quick sort ***")
l = list(map(int, input("Enter a sequence of integers : ").split()))
print()
print("Number of comparisons for each pivot strategy:")
print(f"First Pivot: {countCompare(l, 'first')} comparisons")
print(f"Last Pivot: {countCompare(l, 'last')} comparisons")
print(f"Middle Pivot: {countCompare(l, 'middle')} comparisons")
print("===== End of program =====")
