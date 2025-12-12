""" *** Maximum value ***
Enter some numbers : 1 2 3
Max value = 3
===== End of program ====="""

print(" *** Maximum value ***")
usrinp = input("Enter some numbers : ").split()

max_val = None

for i in usrinp:
    if i == "stop":      
        break
    if i == "-1": 
        break
    try:
        num = int(i)
        if (max_val is None) or (num > max_val):
            max_val = num
    except:
        continue

print(f"Max value = {max_val}")
print("===== End of program =====")