"""Enter Input : 8 4
The gcd of 8 and 4 is : 4

Enter Input : 10 20
The gcd of 20 and 10 is : 10

Enter Input : 12 18
The gcd of 18 and 12 is : 6

Enter Input : 9 7
The gcd of 9 and 7 is : 1

Enter Input : 0 5
The gcd of 5 and 0 is : 5

Enter Input : -6 9
The gcd of 9 and -6 is : 3

Enter Input : -24 -36
The gcd of -24 and -36 is : 12

Enter Input : 0 0
Error! must be not all zero.

Enter Input : -11 -45
The gcd of -11 and -45 is : 1
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "ch5_1.py"


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
    input_text = "8 4"
    expected = """Enter Input : 8 4
The gcd of 8 and 4 is : 4
"""
    assert run_script(input_text) == expected

def test_case2():
    input_text = "10 20"
    expected = """Enter Input : 10 20
The gcd of 20 and 10 is : 10

"""
    assert run_script(input_text) == expected

def test_case3():
    input_text = "12 18"
    expected = """Enter Input : 12 18
The gcd of 18 and 12 is : 6
"""
    assert run_script(input_text) == expected

def test_case4():
    input_text = "9 7"
    expected = """Enter Input : 9 7
The gcd of 9 and 7 is : 1
"""
    assert run_script(input_text) == expected

def test_case5():
    input_text = "0 5"
    expected = """Enter Input : 0 5
The gcd of 5 and 0 is : 5
"""
    assert run_script(input_text) == expected

def test_case6():
    input_text = "-6 9"
    expected = """Enter Input : -6 9
The gcd of 9 and -6 is : 3
"""
    assert run_script(input_text) == expected

def test_case7():
    input_text = "-24 -36"
    expected = """Enter Input : -24 -36
The gcd of -24 and -36 is : 12
"""
    assert run_script(input_text) == expected

def test_case8():
    input_text = "0 0"
    expected = """Enter Input : 0 0
Error! must be not all zero.
"""
    assert run_script(input_text) == expected

def test_case9():
    input_text = "-11 -45"
    expected = """Enter Input : -11 -45
The gcd of -11 and -45 is : 1
"""
    assert run_script(input_text) == expected