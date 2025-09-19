"""a
 *** Kebab string ***
Enter some words: molnupiravir neW hoPe for prevention and treatmenT
Kebab-case => molnupiravir-new-hope-for-prevention-and-treatment
===== End of program ======
"""

print(" *** Kebab string ***")
usrinpraw = input("Enter some words: ").split()
lengthystr = "-".join(usrinpraw)

Kebabing = ""
for i in range(len(lengthystr)):
    ch = lengthystr[i]
    if ch != "-" and 65 <= ord(ch) <= 90:
        ch = chr(ord(ch) + 32)
    Kebabing += ch

print(f"Kebab-case => {Kebabing}")
print("===== End of program ======")

#65  - 90 is capital
#+32 to uncapitalize