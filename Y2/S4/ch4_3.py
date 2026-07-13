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

