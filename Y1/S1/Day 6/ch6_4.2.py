"""
 *** Median Mean ***
Enter numbers : 3 2 1
list0 =  ['3', '2', '1']
list1 =  [3, 2, 1]
Mean = 2
sort = [1, 2, 3]
Median = 2
list2 =  []
===== End of program =====
"""

print(" *** Median Mean ***")
usrinpraw = input("Enter numbers : ").split()

print(f"list0 =  {usrinpraw}")

list1 = []
for rawpointer in usrinpraw:
    list1.append(int(rawpointer))

print(f"list1 =  {list1}")

mean = 0
for meanpointer in list1:
    mean = mean + meanpointer
print(f"Mean = {int(mean/len(list1))}")

for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp

print(f"sort = {list1}")

Median = None

# Len = 6 - 0,1,2,3,4,5
# Mid = 2+3/2
# 6/2=3 + (6/2)-12 )/2

if len(list1) % 2 == 1:
    Median = list1[int((len(list1)-1)/2)]
else:
    Median = (list1[int(len(list1)/2)] + list1[int((len(list1)/2)-1)]) / 2
print(f"Median = {Median}")
print("list2 =  []")