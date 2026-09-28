"""Write a Binary Search using recursion to determine whether a value exists in the list or not. If the value is found, return True; if not, return False.

Explanation of Input:

    On the left, it will be a list of Data.
    On the right, it will be the value we are trying to find."""


def bi_search(l, r, arr, x):
    # Code Here

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))