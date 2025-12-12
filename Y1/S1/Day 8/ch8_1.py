print("*** Permutation ***")

def is_permutation(s1, s2):
    # 1. Check length first
    if len(s1) != len(s2):
        return False
    
    # 2. Count characters in each string
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            return False
    return True


# Input format: str1/str2
s1, s2 = input("Enter two strings: ").split("/")

if is_permutation(s1, s2):
    print("String1 and String2 are permutation")
else:
    print("String1 and String2 are not permutation")

print("===== End of program =====")