"""
 *** Pyramid-V ***
Enter height : 3
  Z      
 YXW     
VUTSR    
===== End of program =====
"""

print(" *** Pyramid-V ***")
h = input("Enter height : ")
h = int(h)

D = ord("Z")
for r in range(1, h+1, +1):
    print(" "*(h-r),end='')

    for j in range(1, (2*r)):
        print(chr(D),end='')
        D -= 1
    print() 

print("===== End of program =====")