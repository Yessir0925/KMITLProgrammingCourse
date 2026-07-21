"""
Write a function to find the sum of any three terms in an array 
that equal zero, for an array containing real numbers. The array 
must have a length of at least three elements.

Enter Your List : -25 -10 -7 -3 2 4 8 10
[[-10, 2, 8], [-7, -3, 10]]
"""

nums = list(map(int, input("Enter Your List : ").split()))

for i in range(len(nums)-1):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

if len(nums) < 3:
    print("Array Input Length Must More Than 2")
else:
    ans = []

    for i in range(len(nums) - 2):
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s == 0:
                ans.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif s < 0:
                left += 1
            else:
                right -= 1

    print(ans)