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


Enter width, height, and room: 6 4 
F__###,
##_###,
##__##,
###__O
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

class Queue:
    def __init__(self, item=None):
        if item is None:
            self._items = []
        elif isinstance(item, list):
            self._items = list(item)
        else:
            self._items = [item]

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)


def shape_validate(size):
    col_size, row_size = size

    if row_size != len(room_shape):
        return False

    for row in room_shape:
        if len(row) != col_size:
            return False

    # The map must contain a starting point
    return find_starting_point() is not None


def find_starting_point():
    for row_idx, row in enumerate(room_shape):
        for col_idx, cell in enumerate(row):
            if cell == "F":
                return col_idx, row_idx

    return None


def report_queue(queue):
    print(f"Queue: {queue}")


def find_exit():
    starting_point = find_starting_point()

    visited = {starting_point}
    queue = Queue(starting_point)

    report_queue(queue)

    while not queue.is_empty():
        found_exit = walk(queue, visited)

        if found_exit:
            print("Found the exit portal.")
            return

        # Do not display an empty queue
        if not queue.is_empty():
            report_queue(queue)

    print("Cannot reach the exit portal.")


def walk(queue, visited):
    curr_col, curr_row = queue.dequeue()

    # North, East, South, West
    directions = {
        "up": (curr_col, curr_row - 1),
        "right": (curr_col + 1, curr_row),
        "down": (curr_col, curr_row + 1),
        "left": (curr_col - 1, curr_row)
    }

    for direction in walk_sequence:
        next_col, next_row = directions[direction]

        # Check room boundaries
        if not (
            0 <= next_col < room_size[0]
            and 0 <= next_row < room_size[1]
        ):
            continue

        next_point = (next_col, next_row)

        if next_point in visited:
            continue

        point_char = room_shape[next_row][next_col]

        # Stop immediately when the exit is found
        if point_char == "O":
            return True

        if check_walkable(point_char):
            visited.add(next_point)
            queue.enqueue(next_point)

    return False


def check_walkable(point):
    # Only "_" represents a normal walkable cell
    return point == "_"


walk_sequence = ["up", "right", "down", "left"]

try:
    xyz = "6 4 F__###,##_###,##__##,###__O"
    room_setup = xyz.split(maxsplit=2)

    room_size = [
        int(room_setup[0]),
        int(room_setup[1])
    ]

    room_shape = room_setup[2].split(",")

except (ValueError, IndexError):
    print("Invalid map input.")

else:
    if not shape_validate(room_size):
        print("Invalid map input.")
    else:
        find_exit()
