import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "ch5_5.py"

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

Make sure to test your implementation to verify that it meets the above requirements."""

def run_script(input_text: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
    )

    output = result.stdout
    if output.startswith("Enter Input : "):
        output = output[len("Enter Input : "):]

    return f"Enter Input : {input_text}\n{output}"


def test_case1():
    input_text = '64 8 216 512 27 729 0 1 343 125'
    expected = """Enter Input : 64 8 216 512 27 729 0 1 343 125
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1 
2 : 512 
3 : 343 
4 : 64 
5 : 125 
6 : 216 
7 : 27 
8 : 8 
9 : 729 
------------------------------------------------------------
Round : 2
0 : 8 1 0 
1 : 216 512 
2 : 729 27 125 
3 : 
4 : 343 
5 : 
6 : 64 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 64 27 8 1 0 
1 : 125 
2 : 216 
3 : 343 
4 : 
5 : 512 
6 : 
7 : 729 
8 : 
9 : 
------------------------------------------------------------
3 Time(s)
Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
After  Radix Sort : 729 -> 512 -> 343 -> 216 -> 125 -> 64 -> 27 -> 8 -> 1 -> 0
"""
    assert run_script(input_text) == expected

def test_case2():
    input_text = '-123 -789 0 -50385 1561 668 -1'
    expected = """Enter Input : -123 -789 0 -50385 1561 668 -1
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1561 -1 
2 : 
3 : -123 
4 : 
5 : -50385 
6 : 
7 : 
8 : 668 
9 : -789 
------------------------------------------------------------
Round : 2
0 : 0 -1 
1 : 
2 : -123 
3 : 
4 : 
5 : 
6 : 668 1561 
7 : 
8 : -50385 -789 
9 : 
------------------------------------------------------------
Round : 3
0 : 0 -1 
1 : -123 
2 : 
3 : -50385 
4 : 
5 : 1561 
6 : 668 
7 : -789 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 668 0 -1 -123 -50385 -789 
1 : 1561 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 5
0 : 1561 668 0 -1 -123 -789 
1 : 
2 : 
3 : 
4 : 
5 : -50385 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
5 Time(s)
Before Radix Sort : -123 -> -789 -> 0 -> -50385 -> 1561 -> 668 -> -1
After  Radix Sort : 1561 -> 668 -> 0 -> -1 -> -123 -> -789 -> -50385
"""
    assert run_script(input_text) == expected

def test_case3():
    input_text = '-1 -9 -3 -6 -5 -4 -7 0 -8 -2 3 2 5 1 4 9 8 7 6'
    expected = """Enter Input : -1 -9 -3 -6 -5 -4 -7 0 -8 -2 3 2 5 1 4 9 8 7 6
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1 -1 
2 : 2 -2 
3 : 3 -3 
4 : 4 -4 
5 : 5 -5 
6 : 6 -6 
7 : 7 -7 
8 : 8 -8 
9 : 9 -9 
------------------------------------------------------------
1 Time(s)
Before Radix Sort : -1 -> -9 -> -3 -> -6 -> -5 -> -4 -> -7 -> 0 -> -8 -> -2 -> 3 -> 2 -> 5 -> 1 -> 4 -> 9 -> 8 -> 7 -> 6
After  Radix Sort : 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> -1 -> -2 -> -3 -> -4 -> -5 -> -6 -> -7 -> -8 -> -9
"""
    assert run_script(input_text) == expected

def test_case4():
    input_text = '15 -15'
    expected = """Enter Input : 15 -15
------------------------------------------------------------
Round : 1
0 : 
1 : 
2 : 
3 : 
4 : 
5 : 15 -15 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 2
0 : 
1 : 15 -15 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
2 Time(s)
Before Radix Sort : 15 -> -15
After  Radix Sort : 15 -> -15
"""
    assert run_script(input_text) == expected

def test_case5():
    input_text = '0 0 0 0 0 0 0'
    expected = """Enter Input : 0 0 0 0 0 0 0
------------------------------------------------------------
0 Time(s)
Before Radix Sort : 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
After  Radix Sort : 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
"""
    assert run_script(input_text) == expected

def test_case6():
    input_text = '100 0 10'
    expected = """Enter Input : 100 0 10
------------------------------------------------------------
Round : 1
0 : 100 0 10 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 2
0 : 100 0 
1 : 10 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 10 0 
1 : 100 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
3 Time(s)
Before Radix Sort : 100 -> 0 -> 10
After  Radix Sort : 100 -> 10 -> 0
"""
    assert run_script(input_text) == expected
