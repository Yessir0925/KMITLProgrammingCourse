"""Write a Hashing program with the following operations:

    Find the index of the Table from the sum of the ASCII values of the key, then mod it by the size of the Table.
    If a collision occurs, shift the index using Quadratic Probing.
    If collisions occur up to a defined limit, discard that Data immediately.
    If the Table is full, display This table is full !!!!!!. If this message has already been shown, do not display it again (show it only once).

Explanation of Input:
The Data is divided into two parts using a "/".

    The left side refers to the size of the Table and the MaxCollision limit, respectively.
    The right side contains n sets of Data, where each set of Data is separated by a comma. In each set of Data, the key and value are provided in that order."""


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

class Hash:

    def __init__(self, size, max_collision, threshold):
        self.size = size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * size
        self.items = []  # insertion order, used when rehashing

    def place(self, x):
        start = x % self.size
        idx = start
        i = 0
        while self.table[idx] is not None:
            i += 1
            print("collision number {0} at {1}".format(i, idx))
            if i >= self.max_collision:
                return False
            idx = (start + i * i) % self.size
        self.table[idx] = x
        return True

    def rehash(self):
        size = self.size * 2
        while not is_prime(size):
            size += 1
        self.size = size
        self.table = [None] * size
        for x in self.items:
            if not self.place(x):
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                return

    def add(self, x):
        self.items.append(x)
        if len(self.items) * 100 / self.size > self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
        elif not self.place(x):
            print("****** Max collision - Rehash !!! ******")
            self.rehash()

    def show(self):
        for i in range(self.size):
            print("#{0}\t{1}".format(i + 1, self.table[i]))
        print("----------------------------------------")

print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
size, max_collision, threshold = map(int, inp[0].split())
h = Hash(size, max_collision, threshold)
print("Initial Table :")
h.show()
for x in map(int, inp[1].split()):
    print("Add : {0}".format(x))
    h.add(x)
    h.show()