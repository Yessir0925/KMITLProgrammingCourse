usrinp, num = input("Enter a word and a number: ").split()
num = int(num)
word = ""
if 1 < num < 26:
    for i in usrinp:
        if 'a' <= i <= 'z':
            base = ord('A')
            offset = ord(i) - ord('a')
        elif 'A' <= i <= 'Z':
            base = ord('A')
            offset = ord(i) - ord('A')
        else:
            word += i
            continue
        new_char = chr(base + (offset + num) % 26)
        word += new_char
    print(word)
else:
    print("Number must be between 1-26")