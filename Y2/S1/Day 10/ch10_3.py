"""
Chapter : 10 - item : 3 - Fun with hashing

ส่งมาแล้ว 0 ครั้ง

Write a Hashing program with the following operations:

    Find the index of the Table from the sum of the ASCII values of the key, then mod it by the size of the Table.
    If a collision occurs, shift the index using Quadratic Probing.
    If collisions occur up to a defined limit, discard that Data immediately.
    If the Table is full, display This table is full !!!!!!. If this message has already been shown, do not display it again (show it only once).

Explanation of Input:
The Data is divided into two parts using a "/".

    The left side refers to the size of the Table and the MaxCollision limit, respectively.
    The right side contains n sets of Data, where each set of Data is separated by a comma. In each set of Data, the key and value are provided in that order."""

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self, size, max_collision):
        self.size = size
        self.max_collision = max_collision
        self.table = [None] * size
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def insert(self, data):
        start = sum(ord(c) for c in data.key) % self.size
        idx = start
        i = 0
        while self.table[idx] is not None:
            i += 1
            print("collision number {0} at {1}".format(i, idx))
            if i >= self.max_collision:
                print("Max of collisionChain")
                return
            idx = (start + i * i) % self.size
        self.table[idx] = data
        self.count += 1

    def show(self):
        for i in range(self.size):
            print("#{0}\t{1}".format(i + 1, self.table[i]))
        print("---------------------------")

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
size, max_collision = map(int, inp[0].split())
h = hash(size, max_collision)
for item in inp[1].split(','):
    if h.is_full():
        print("This table is full !!!!!!")
        break
    key, value = item.split()
    h.insert(Data(key, value))
    h.show()
else:
    if h.is_full():
        print("This table is full !!!!!!")