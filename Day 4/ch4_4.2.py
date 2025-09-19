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

FillerType = ""
print(" *** Pyramid-V ***")
height = input("Enter height : ")
height = int(height)

for r in range(height):
  for c in range(height - r - 1, 0, -1):
    print(" ", end='')
  if r == 0:
    print("/\\",end='')
  else:
    Filler = r * 2
    print("/",end="")
    if r == height - 1:
      FillerType = "_"
    else:
      FillerType = "."
    for BFill in range(Filler):
      print(f"{FillerType}",end='')
    print("\\",end="")
  print()