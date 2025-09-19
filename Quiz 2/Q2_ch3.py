"""Fibonacci Seq"""
a0, a1, n = input("Enter a0, a1, n = ").split()
a0, a1, n = int(a0), int(a1), int(n)
List = [a0, a1]


for i in range(n-2):
    List.append(int(List[i]) + int(List[i+1]))


FinalPrint = ",".join(map(str, List))
print(FinalPrint)