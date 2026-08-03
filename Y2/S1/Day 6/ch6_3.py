def gcd(a, b):
    #Implement Euclidean algorithm to find the GCD of two numbers
    if a == 0 and b == 0:
        print("Error! must be not all zero.")
        raise SystemExit

    if b == 0:
        return abs(a)
    else:
        moddy = a % b
        return gcd(b, moddy)

a, b = map(int, input("Enter Input : ").split())
if a > b:
    print(f"The gcd of {a} and {b} is : {gcd(a, b)}")
else:
    print(f"The gcd of {b} and {a} is : {gcd(b, a)}")