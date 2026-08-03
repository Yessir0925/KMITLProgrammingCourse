"""Directions for Using Linked List to Perform Radix Sort in Descending Order

    Create a Linked List Class:
        Implement a Linked List class.

    Implement Radix Sort:
        Use the Linked List class to perform Radix Sort.
        Follow the algorithm steps as outlined in the last two slides of the lecture.

    Sort Order:
        Ensure the Radix Sort is done in descending order.

    Output Requirements:
        Display the result of each round of the Radix Sort.
        Ensure the sorting is done with the minimum number of rounds possible.
        In the last three lines of the output, include:
            The minimum number of rounds taken.
            The data before performing Radix Sort.
            The data after performing Radix Sort.

Make sure to test your implementation to verify that it meets the above requirements.


Directions for Using Linked List to Perform Radix Sort in Descending Order

    Create a Linked List Class:
        Implement a Linked List class.

    Implement Radix Sort:
        Use the Linked List class to perform Radix Sort.
        Follow the algorithm steps as outlined in the last two slides of the lecture.

    Sort Order:
        Ensure the Radix Sort is done in descending order.

    Output Requirements:
        Display the result of each round of the Radix Sort.
        Ensure the sorting is done with the minimum number of rounds possible.
        In the last three lines of the output, include:
            The minimum number of rounds taken.
            The data before performing Radix Sort.
            The data after performing Radix Sort.

Make sure to test your implementation to verify that it meets the above requirements."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None


class LinkedList:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node

    def popFront(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        node.next = None
        return node

    def clear(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur = self.head
        out = ""

        while cur is not None:
            out += str(cur.data)
            if cur.next is not None:
                out += " -> "
            cur = cur.next

        return out

    def printBucket(self):
        cur = self.head

        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()


def digit(value, place):
    value = abs(value)
    return (value // (10 ** place)) % 10


def maxDigit(values):
    maximum = 0

    for value in values:
        if abs(value) > maximum:
            maximum = abs(value)

    if maximum == 0:
        return 0

    count = 0
    while maximum > 0:
        maximum //= 10
        count += 1

    return count


def reorderBucket(bucket):
    #Non-negative values keep their relative order first, then negative values.
    merged = LinkedList()

    cur = bucket.head
    while cur is not None:
        if cur.data >= 0:
            merged.append(cur.data)
        cur = cur.next

    cur = bucket.head
    while cur is not None:
        if cur.data < 0:
            merged.append(cur.data)
        cur = cur.next

    return merged


def rebuild(buckets):
    ll = LinkedList()

    for i in range(9, -1, -1):
        cur = buckets[i].head
        while cur is not None:
            if cur.data >= 0:
                ll.append(cur.data)
            cur = cur.next

    for i in range(10):
        cur = buckets[i].head
        while cur is not None:
            if cur.data < 0:
                ll.append(cur.data)
            cur = cur.next

    return ll


nums = list(map(int, input("Enter Input : ").split()))
original = LinkedList()
for n in nums:
    original.append(n)
rounds = maxDigit(nums)
print("-" * 60)
if rounds == 0:
    print("0 Time(s)")
    print("Before Radix Sort :", original)
    print("After  Radix Sort :", original)
    exit()

current = LinkedList()

for n in nums:
    current.append(n)

for r in range(rounds):
    buckets = []
    for _ in range(10):
        buckets.append(LinkedList())

    cur = current.head
    while cur is not None:
        d = digit(cur.data, r)
        buckets[d].append(cur.data)
        cur = cur.next

    buckets = [reorderBucket(bucket) for bucket in buckets]
    print("Round :", r + 1)

    for i in range(10):
        print(str(i) + " :", end=" ")
        buckets[i].printBucket()

    print("-" * 60)
    current = rebuild(buckets)

print(f"{rounds} Time(s)")
print("Before Radix Sort :", original)
print("After  Radix Sort :", current)