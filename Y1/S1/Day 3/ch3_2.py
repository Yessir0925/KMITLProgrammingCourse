""" *** Min Max Avg ***
Enter 3 numbers : 1 2 3
min, mid, max ==> 1.0, 2.0, 3.0
Average ==> 2.00"""

print(" *** Min Max Avg ***")
usrinpa, usrinpb, usrinpc = map(float,(input("Enter 3 numbers : ").split()))
list = [usrinpa, usrinpb, usrinpc]
for i in range(2):
    for j in range(2 - i):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp


avr = (usrinpa + usrinpb + usrinpc)/3
print(f"min, mid, max ==> {list[0]}, {list[1]}, {list[2]}")
print(f'Average ==> {avr:.2f}')