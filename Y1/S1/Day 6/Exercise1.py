print("*** The number of distinct remainders ***")

# input example: "5 / 1 2 3 4 5"
raw = input("Enter a divisor / a sequence : ")
divisor, seq = raw.split("/", 1)  # split at "/"
divisor = int(divisor.strip())
numbers = list(map(int, seq.split()))

# compute remainders
remainders = {n % divisor for n in numbers}  # set comprehension

print("Distinct remainders =", len(remainders))
print("===== End of program =====")