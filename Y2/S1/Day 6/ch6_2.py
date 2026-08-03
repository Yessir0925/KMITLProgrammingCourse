
"""Write a function that works like the len() function to find the length of a string and 
display the result as shown in the example (printing each character alternated with special 
symbols in odd and even positions).

Restrictions:

    Do not use len, for, while, do while, or split commands.
    The function must have only one parameter.

Note: The function should only have one parameter.



def length(txt):     
    #Code Here
print("\n",length(input("Enter Input : ")),sep="")
#print(you can modify this line)
 
 *** Length of string (Recursion) ***
Enter Input : data structure is easy
d*a~t*a~ *s~t*r~u*c~t*u~r*e~ *i~s* ~e*a~s*y~
length of 'data structure is easy' is 22 
"""

def length(txt, bool=False):   
    if txt == "":
        return 0
    else:
        print(txt[0], end="")
        if bool == False:
            print("*", end="")
        else:
            print("~", end="")
        return 1 + length(txt[1:], not bool)
        

print(" *** Length of string (Recursion) ***")
usrinp = input("Enter Input : ")
print(f"\nlength of '{usrinp}' is {length(usrinp)}")

#take each term first letter and print with * or ~ then call the function again with the 
# rest of the string until the string is empty
