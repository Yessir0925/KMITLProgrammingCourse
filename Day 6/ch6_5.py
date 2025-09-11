print(" *** Rectangle down-left-up-left ***")
col,row = input("Enter width height : ").split()
col,row = int(col),int(row)
matrix = []
num = 1
isInvert = False
for i in range(col):
    newCol = list(range(num,num+row))
    if isInvert :
        newCol = newCol[::-1]
    isInvert = not isInvert
    matrix.insert(0,newCol)
    num = num+row

transposedMatrix = []
for j in range(row) :
    newRow = []
    for k in matrix:
        newRow.append(k[j])
    transposedMatrix.append(newRow)

for l in transposedMatrix :
    strLine = ""
    for m in l:
        if strLine != "" and m < 10:
            strLine = strLine+"  "
        else :
            strLine = strLine+" "
        strLine = strLine+str(m)
    print(strLine)
print("===== End of program =====")