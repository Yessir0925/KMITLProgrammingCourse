"""*** Find fibonacci sequence ***
Enter n : 1
fibo(1) = 1
===== End of program ====="""

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(" *** Find fibonacci sequence ***")
usrinp = input("Enter n : ")
print(f"fibo({usrinp}) = {fibo(int(usrinp))}")
print("===== End of program =====")