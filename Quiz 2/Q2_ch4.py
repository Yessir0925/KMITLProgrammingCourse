"""
Enter height: 3
***** |   *  
 ***  |  *** 
  *   | *****
""" 
"""
Enter height: 5
********* |     *
 *******  |    ***
  *****   |   *****
   ***    |  *******
    *     | *********
"""

h = int(input("Enter height: "))

for r in range(h):
    for _ in range(r):
        print(" ",end='')
    for _ in range((-2*r)+((2*h)-1)):
        print("*",end='')
    for _ in range(r):
        print(" ",end='')
    
    print(" | ",end='')

    for _ in range(h-r-1):
        print(" ",end='')
    for _ in range((r*2)+1):
        print("*",end='')
    
    print()