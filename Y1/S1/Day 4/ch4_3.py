print(" *** Fibonacci sequence ***")
a0, a1, n = input("Enter a0 a1 n : ").split(" ")
a0 = str(a0)
a1 = str(a1)
n = int(n)
fiboout = [a0, a1]
x = 0
y = 1
while y <= n-2:
    sub = int(fiboout[x]) + int(fiboout[y])
    fiboout.append(str(sub))
    x += 1
    y += 1

print(', '.join(fiboout))  
print("===== End of program =====")