"""
 *** Rectangle down-left-up-left ***
Enter width height : 4 4
 16  9  8  1]
 15 10  7  2]
 14 11  6  3]
 13 12  5  4]
===== End of program =====
"""
#Pointer Style

print(" *** Rectangle down-left-up-left ***")
w, h = 4,4
#map(int,input("Enter width height : ").split())

Dir = [(-1,0),(1,0)]
 

    
    
for row in DLMatrix:
    print(" ".join(f"{x:>{w}}" for x in row))

print("===== End of program =====")