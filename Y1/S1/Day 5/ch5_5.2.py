"""
 *** Alphabet Sequence (a-z) ***
Enter character step length : a 1 26
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z
===== End of program =====
"""

print(" *** Alphabet Sequence (a-z) ***")
FL, SL, RS = input("Enter character step length : ").split()
STRBUILD = ""

FL = ord(FL)
RS, SL = int(RS), int(SL)

for i in range(RS):
    if i != 0:
        STRBUILD = STRBUILD + "-" + str(chr(FL))
    else:
        STRBUILD = str(chr(FL))
    FL += SL

print(STRBUILD)
print("===== End of program =====")