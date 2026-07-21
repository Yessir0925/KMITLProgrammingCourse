"""Write a python program  to creaet a new range() function using just one function

- if there is 1 argument -> range(a)                | start = 0 , end = a , step = 1

- if there are 2 argument -> range(a, b)            | start = a , end = b , step = 1

- if there are 3 argument -> range(a, b, c)        | start = a , end = b , step = c


def RANGE(*args):
    pass

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))

*** New Range ***
Enter Input : 1 7 1.2
(1.0, 2.2, 3.4, 4.6, 5.8)"""

def RANGE(*args):
    if len(args) == 1:
        stop = float(args[0])
        x = []
        i = 0
        while i < stop:
            x.append(float(i))
            i += 1
        return tuple(x)

    elif len(args) == 2:
        start = float(args[0])
        stop = float(args[1])
        x = []
        while start < stop:
            x.append(float(start))
            start += 1
        return tuple(x)

    elif len(args) == 3:
        start = float(args[0])
        stop = float(args[1])
        step = float(args[2])
        x = []
        while start < stop:
            x.append(float("{:.3f}".format(start)))
            start += step
        return tuple(x)




print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))