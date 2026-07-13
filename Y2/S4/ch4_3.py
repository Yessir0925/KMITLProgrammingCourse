"""Accept a single line of input where each sequence is indicated by a 
letter followed by the number of times the action should be performed. 
'E' indicates an enqueue operation, and 'D' indicates a dequeue operation. 
If the letter is something else, count it as an error input.

You must report how many ineffective dequeues occur in sequence and 
show how the queue changes at each step.

input : D3,E2,E3,D9,E2,ff
Step : D3
Dequeue : []
Error Dequeue : 3
Error input : 0
--------------------
Step : E2
Enqueue : ['*0', '*1']
Error Dequeue : 3
Error input : 0
--------------------
Step : E3
Enqueue : ['*0', '*1', '*2', '*3', '*4']
Error Dequeue : 3
Error input : 0
--------------------
Step : D9
Dequeue : []
Error Dequeue : 7
Error input : 0
--------------------
Step : E2
Enqueue : ['*5', '*6']
Error Dequeue : 7
Error input : 0
--------------------
Step : ff
['*5', '*6']
Error Dequeue : 7
Error input : 1
--------------------
"""

usrinp = input("input : ")
usrlist = [x for x in usrinp.split(',')]
error_dequeue = 0
error_input = 0
counter = 0
queue = []

for step in usrlist:

    if step[0] == 'E':
        try:
            count = int(step[1:])
            for i in range(count):
                queue.append(f'*{counter}')
                counter += 1
        except ValueError:
            error_input += 1
    elif step[0] == 'D':
        try:
            count = int(step[1:])
            for i in range(count):
                if queue:
                    queue.pop()
                else:
                    error_dequeue += 1
        except ValueError:
            error_input += 1
    else:
        error_input += 1

    print(f"Step : {step}")
    if step[0] == 'E':
        print(f"Enqueue : {queue}")
    elif step[0] == 'D':
        print(f"Dequeue : {queue}")
    else:
        print(f"{queue}")
    print(f"Error Dequeue : {error_dequeue}")
    print(f"Error input : {error_input}")
    print("--------------------")
