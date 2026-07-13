"""Sunfong received an assignment from the teacher to create a programming problem for the 
students. He went home to think about it and found himself in a dark room. He can see and 
walk to adjacent areas (in 4 directions: North, South, East, West). Sunfong must find the
exit door from the dream to deliver the assignment to the teacher. He decided to use the 
Breadth First Search (BFS) method, starting from the initial point, checking and remembering
the path in the order of North, East, South, and West. Then, he walks to the next cell and 
repeats the process.

Sunfong needs a program to tell him if he can reach the exit or if he will be stuck in the
dream forever. He is too lazy to write the code himself, so he wants the students to write 
it for him in a neat and concise manner.
Program Details:

Input:

    Receive the width, height, and the map. Each line of the map is separated by a comma.
    Example input: 3 3 F__,##_,O__

This means the map is 3 wide and 3 high, and it looks like this

F__
##_
O__

    In the map:
        'F' represents Sunfong's starting position.
        'O' represents the exit door.
        '_' represents walkable areas.
        Any other characters represent walls and are not walkable.

Output:

    If there is no 'F' in the room or the map input does not match the specified
width, display "Invalid map input."
    Show the queue status while searching for the exit.
    If the exit is found, display "Found the exit portal."
    If the exit cannot be found, display "Cannot reach the exit portal."


Enter width, height, and room: 6 4 F__###,##_###,##__##,###__O
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(2, 1)]
Queue: [(2, 2)]
Queue: [(3, 2)]
Queue: [(3, 3)]
Queue: [(4, 3)]
Found the exit portal.
"""