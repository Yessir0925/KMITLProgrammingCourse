print(" *** Reverse Even ***")
usrinp = input("Enter integers : ")
parts = usrinp.split()

nums = []
for p in parts:
    nums.append(int(p))

print(nums)


evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
evens.reverse()


j = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums[i] = evens[j]
        j += 1

print(nums)
print("===== End of program =====")