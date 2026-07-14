"""Have the students write a program that accepts two types of input and uses a QUEUE to solve the problem.


E <value> takes the value and places it in the QUEUE, then displays the enqueueed value and the index of the added value.

D. Dequeue the leading character in the queue and display the removed character's number and the queue size.

After dequeueing.

***Finally, if there is still a value in the queue, display it. If there is no value, display "Empty".*** 

Enter Input : E 10,E 20,E 30,E 40,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Pop 20 size in queue is 2
Number in Queue is :  ['30', '40']
"""

usrinp = input("Enter Input : ")
usrinplist = [x for x in usrinp.split(',')]

class Queue:
    def __init__(self):
        self.queue = []
        self.counter = 0
    
    def runtasks(self, tasklist):
        for i in range(len(tasklist)):
            try:
                if tasklist[0] == "D":
                    self.dequeue()
                elif (tasklist[0].split())[0] == "E":
                    self.enqueue(tasklist)
            except Exception as e:
                print("Error: ", e)

    def enqueue(self, tasklist):
        if tasklist:
            taskrun = (tasklist[0].split())[1]
            tasklist.pop(0)
            self.queue.append(taskrun)
            print(f"Add {taskrun} index is {self.counter}")
            self.counter += 1
        else:
            print("Empty")
    
    def dequeue(self):
        if self.queue:
            self.counter -= 1
            print(f"Pop {self.queue.pop(0)} size in queue is {self.counter}")
        else:
            print("Empty")

    def __str__(self):
        return f"Number in Queue is :  {self.queue}"

NewQueue = Queue()
NewQueue.runtasks(usrinplist)
print(NewQueue)