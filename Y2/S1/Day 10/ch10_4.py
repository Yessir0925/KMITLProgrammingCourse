"""Write a Hashing program with the following operations:

    Find the index of the Table from the sum of the ASCII values of the key, then mod it by the size of the Table.
    If a collision occurs, shift the index using Quadratic Probing.
    If collisions occur up to a defined limit, discard that Data immediately.
    If the Table is full, display This table is full !!!!!!. If this message has already been shown, do not display it again (show it only once).

Explanation of Input:
The Data is divided into two parts using a "/".

    The left side refers to the size of the Table and the MaxCollision limit, respectively.
    The right side contains n sets of Data, where each set of Data is separated by a comma. In each set of Data, the key and value are provided in that order."""