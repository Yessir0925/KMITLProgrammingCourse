"""
write a program to find the smallest value that is greater than the target value. If no such value exists, display No First Greater Value. The numbers in both lists are guaranteed not to exceed 1,000,000.

Explanation of Test Case 2:
Left : [3, 2, 7, 6, 8] Right : [5, 6, 12]

    Find the smallest value greater than 5 from the list (Left). The result is 6.
    Find the smallest value greater than 6 from the list (Left). The result is 7.
    Find the smallest value greater than 12 from the list (Left). Since no value is greater than 12, the result will be No First Greater Value."""


def first_greater(arr, x):
    l, r = 0, len(arr) - 1
    res = None
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > x:
            res = arr[mid]
            r = mid - 1
        else:
            l = mid + 1
    return res

inp = input('Enter Input : ').split('/')
arr, targets = sorted(map(int, inp[0].split())), list(map(int, inp[1].split()))
for x in targets:
    res = first_greater(arr, x)
    print(res if res is not None else 'No First Greater Value')