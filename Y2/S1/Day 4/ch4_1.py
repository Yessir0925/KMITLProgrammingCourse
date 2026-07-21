"""Have the students write a program that accepts two types of input and uses a QUEUE to solve the problem.


E <value> takes the value and places it in the QUEUE, then displays the enqueueed value and the index of the added value.

D. Dequeue the leading character in the queue and display the removed character's number and the queue size.

After dequeueing.

***Finally, if there is still a value in the queue, display it. If there is no value, display "Empty".*** 

Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Add 50 index is 3
Add 60 index is 4
Pop 20 size in queue is 4
Pop 30 size in queue is 3
Pop 40 size in queue is 2
Pop 50 size in queue is 1
Pop 60 size in queue is 0
-1
Empty
"""

usrinp = input("Enter Input : ")
usrinplist = [x.strip() for x in usrinp.split(',') if x.strip()]


class Queue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def runtasks(self, tasklist):
            while tasklist:
                task = tasklist.pop(0)
                if task == "D":
                    self.dequeue()
                elif task.startswith("E"):
                    value = task.split()[1]
                    self.enqueue(value)

    def enqueue(self, value):
        self.queue.append(value)
        print(f"Add {value} index is {self.counter}")
        self.counter += 1

    def dequeue(self):
        if self.queue:
            value = self.queue.pop(0)
            self.counter -= 1
            print(f"Pop {value} size in queue is {self.counter}")
        else:
            print("-1")

    def __str__(self):
        return f"Number in Queue is :  {self.queue}"


NewQueue = Queue()
NewQueue.runtasks(usrinplist)

if NewQueue.queue:
    print(NewQueue)
else:
    print("Empty")