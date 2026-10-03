"""Write a Binary Search using recursion to determine whether a value exists in the list or not. If the value is found, return True; if not, return False.

Explanation of Input:

    On the left, it will be a list of Data.
    On the right, it will be the value we are trying to find."""


def bi_search(l, r, arr, x):
    if l > r:
        return False
    mid = (l + r) // 2
    if arr[mid] == x:
        return True
    if arr[mid] < x:
        return bi_search(mid + 1, r, arr, x)
    return bi_search(l, mid - 1, arr, x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))