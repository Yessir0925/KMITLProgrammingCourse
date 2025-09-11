print(" *** Pyramid-V ***")
usrinp = int(input("Enter height : ")) - 1
pyramid = []
pointer = 0

while pointer <= usrinp - 1:
    spaces = ' ' * (usrinp - pointer)
    print(f"{spaces}/{''.join(pyramid)}\\")
    pyramid.append("..")
    pointer += 1

print(f"/{'_' * (usrinp * 2)}\\")

print("===== End of program =====")