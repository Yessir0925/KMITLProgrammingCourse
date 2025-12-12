print(' *** Number Fun ***')
inp = input("Enter a 3-digit number : ")
num = int(inp)

Original = num
Flipped = 0
while Original > 0:
    Range = Original % 10
    Flipped = Flipped * 10 + Range
    Original = Original // 10

print(f"\nYou have entered     => {num}")
print(f"Square               => {num ** 2:,}")
print(f"25% 3 decimal places => {round(num * 0.25, 3):.3f}%")
print(f"Flipping             => {Flipped}")
flt = float(inp)
print(f"Hexadecimal          => {num:x} or {num:X}")
print(f"Binary               => {num:b}")
Binary = f'{num:08b}'
print(f"Binary right 8-digit => {Binary[:4]} {Binary[4:]}")