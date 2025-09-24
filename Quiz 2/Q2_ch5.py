"""
 *** Spiral Matrix ***
Enter width height : 4 4
01 02 03 04 
12 13 14 05 
11 16 15 06 
10 09 08 07 
===== End of program =====
"""

print(" *** Spiral Matrix ***")
w, h = input("Enter width height : ").split()
w, h = int(w), int(h)

numList = [i for i in range(w*h)]

#Go to end max, Go Down max, Go to start min, Go up min

"""
[0][0] [0][1] [0][2] [0][3]
[1][0] [1][1] [1][2] [1][3]
[2][0] [2][1] [2][2] [2][3]
[3][0] [3][1] [3][2] [3][3]

[0][0] [0][1] [0][2] [0][3] | [1][3] [2][3] [3][3] | [3][2] 
[3][1] | [3][0] [2][0] [1][0] | [1][1] [1][2] | [2][2] [2][1]
    #[0][0,1,2,3]
    #[1,2,3][3]
    #[3][2,1,0]
    #[2,1][0]
    #[1][1,2]
    #[2][2]
    #[2][1]
"""


DLMatrix =  [[w*r + c for c in range(w)] for r in range(h)]

for rows in DLMatrix:
    print(" ".join(str(columns) for columns in rows))