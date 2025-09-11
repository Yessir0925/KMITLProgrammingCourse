""" *** Alphabet Sequence (a-z) ***
Enter character step length : a 1 26
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z
===== End of program ====="""

print(" *** Alphabet Sequence (a-z) ***")
a, b, c = input("Enter character step length : ").split()

b = int(b)  
c = int(c)   

if ('a' <= a <= 'z') and (b >= 0):
    start = ord(a)
    for i in range(c):
        char = chr(((start - ord('a') + i * b) % 26) + ord('a'))
        if i < c - 1:
            print(f"{char}-", end="")
        else:
            print(f"{char}", end="")
    print("\n===== End of program =====")
else:
    print("Invalid input !!!", end="")
