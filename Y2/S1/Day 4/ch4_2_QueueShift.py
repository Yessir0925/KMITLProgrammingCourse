class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


main_q = Queue()
cashier1 = Queue()
cashier2 = Queue()

for ch in input("Enter people : "):
    main_q.enqueue(ch)

time1 = 0
time2 = 0
minute = 0

while not main_q.is_empty():
    minute += 1

    if not cashier1.is_empty():
        time1 += 1
        if time1 == 3:
            cashier1.dequeue()
            time1 = 0

    if not cashier2.is_empty():
        time2 += 1
        if time2 == 2:
            cashier2.dequeue()
            time2 = 0

    person = main_q.dequeue()
    if cashier1.size() < 5:
        cashier1.enqueue(person)
    else:
        cashier2.enqueue(person)

    print(minute, main_q, cashier1, cashier2)
