"""Create a class funString that will accept a string and a command number as parameters, with the following functions:

    Find the length of the string.
    Toggle case in the string (do not use the upper and lower commands).
    Reverse the string (do not use the reversed command).
    Delete characters that appear earlier in the string."


class funString():

    def __init__(self,string = ""):

        ### Enter Your Code Here ###

    def __str__(self):

        ### Enter Your Code Here ###

    def size(self) :

        ### Enter Your Code Here ###

    def changeSize(self):

        ### Enter Your Code Here ###

    def reverse(self):

        ### Enter Your Code Here ###

    def deleteSame(self):

       ### Enter Your Code Here ###



str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())

Enter String and Number of Function : aAaBbBccCDddd 2
AaAbBbCCcdDDD
"""

class funString:

    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)

    def changeSize(self):
        result = ""
        for ch in self.string:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            elif 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result

    def reverse(self):
        result = ""
        for i in range(len(self.string) - 1, -1, -1):
            result += self.string[i]
        return result

    def deleteSame(self):
        result = ""
        for ch in self.string:
            if ch not in result:
                result += ch
        return result


str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1":
    print(res.size())
elif str2 == "2":
    print(res.changeSize())
elif str2 == "3":
    print(res.reverse())
elif str2 == "4":
    print(res.deleteSame())