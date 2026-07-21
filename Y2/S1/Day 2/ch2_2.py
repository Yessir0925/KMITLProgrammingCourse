"""Create class Spherical that must have function [changeR , findVolume , findArea] and radius variable



class Spherical:
    def __init__(self,r):
        ### Enter Your Code Here ###
    def changeR(self,Radius):
        ### Enter Your Code Here ###
    def findVolume(self):
        ### Enter Your Code Here ###
    def findArea(self):
        ### Enter Your Code Here ###
    def __str__(self):
        return "Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea())

print(" *** Spherical ***")
r1, r2 = input("Enter R : ").split()
PI = 3.1415926
R1 = Spherical(int(r1))
print(type(R1))
print(R1)
R1.changeR(int(r2))
print(R1)

Enter R : 3 4
<class '__main__.Spherical'>
Radius =3 Volumn = 113.09733552923254 Area = 113.09733552923255
Radius =4 Volumn = 268.082573106329 Area = 201.06192982974676

"""

pi = 3.14159265358979323846
class Spherical:

    def __init__(self,r):
        self.radius = r
    def changeR(self,Radius):
        self.radius = Radius
    def findVolume(self):
        return ((4/3) * pi * (self.radius ** 3))
    def findArea(self):
        return (4 * pi * (self.radius ** 2))
    def __str__(self):
        return ("Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea()))

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
