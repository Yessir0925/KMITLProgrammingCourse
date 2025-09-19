"""Write a program that takes the height of a pyramid as input.

Then display the pyramid as shown in the example.



Note: in order to display a single back slash, you need ch ="\\"""

""" *** Pyramid-V ***
Enter height : 3
  /\  
 /..\ 
/____\
No indefinate loop
===== End of program ====="""

print(" *** Pyramid-V ***")
h = input("Enter height : ")    
h = int(h)

for r in range(1, h+1, 1):
    print(" "*(h-r),end='')    
    print("/",end='')
    if r != h:
        print("."*((r-1)*2),end='')
    else:
        print("_"*((r-1)*2),end='')
    print("\\", end='')
    print()


print("===== End of program =====")