print(" *** odd integer summation from 1 to n ***")
total = 0
express = []
pointer = 0
usrinpinp = input("Enter an integer(n) : ")
try:
    usrinp = int(usrinpinp)
    if usrinp > 0:
        while pointer <= usrinp:
            if pointer % 2 == 1:
                total += pointer
                express.append(str(pointer))
            pointer += 1
        print(f"Summation => {'+'.join(express)} = {total}")  
    elif usrinp <= 0:
        print(f"The input [{usrinp}] must be greater than or equal to 1 !!!]")
    print("===== End of program ======")
except ValueError:
    print(f"Invalid input => {usrinpinp}")
    print("===== End of program =====")