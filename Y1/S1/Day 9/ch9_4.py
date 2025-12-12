cipher_key = {
    ('A', 'A'): 'b',
    ('A', 'D'): 't',
    ('A', 'F'): 'a',
    ('A', 'G'): 'l',
    ('A', 'X'): 'p',

    ('D', 'A'): 'd',
    ('D', 'D'): 'h',
    ('D', 'F'): 'o',
    ('D', 'G'): 'z',
    ('D', 'X'): 'k',

    ('F', 'A'): 'q',
    ('F', 'D'): 'f',
    ('F', 'F'): 'v',
    ('F', 'G'): 's',
    ('F', 'X'): 'n',

    ('G', 'A'): 'g',
    ('G', 'D'): 'i/j',
    ('G', 'F'): 'c',
    ('G', 'G'): 'u',
    ('G', 'X'): 'x',

    ('X', 'A'): 'm',
    ('X', 'D'): 'r',
    ('X', 'F'): 'e',
    ('X', 'G'): 'w',
    ('X', 'X'): 'y',
}

cipher_text = input("Input ADFGX cipher text: ").strip().upper()
plain_text = ""
pair_1 = ""
pair_2 = ""
curr_index = 0
decryptingFailed = False
for pair in cipher_text:
    if(curr_index % 2 == 0):
        pair_1 = pair
        if(curr_index == len(cipher_text) - 1):
            decryptingFailed = True
            break
    else:
        pair_2 = pair
        if (pair_1, pair_2) in cipher_key:
            plain_text += cipher_key[(pair_1, pair_2)]
        else:
            decryptingFailed = True
            break
    curr_index += 1
if(decryptingFailed):
    print("FAILED TO DECRYPT")
else:
    print(plain_text)