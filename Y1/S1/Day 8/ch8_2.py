print("*** Sort avoid negative number ***")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def sort_avoid_negative_num(arr):
    # Extract positive numbers
    positives = []
    for x in arr:
        if x >= 0:
            positives.append(x)
    
    bubble_sort(positives)
    
    result = []
    pos_index = 0
    for x in arr:
        if x < 0:
            result.append(x)
        else:
            result.append(positives[pos_index])
            pos_index += 1
    return result


arr = []

rawinput = input("Enter Input : ").split()
for sliceinput in rawinput:
    arr.append(int(sliceinput))


normal_sorted = bubble_sort(arr[:]) 

avoid_sorted = sort_avoid_negative_num(arr[:])

print("Normal sort : ")
print(normal_sorted)
print("sort avoid negative number : ")
print(avoid_sorted)
print("===== End of program =====")