import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "ch5_3.py"


def run_script(input_text: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
    )

    output = result.stdout
    if output.startswith("Enter 2 Lists : "):
        output = output[len("Enter 2 Lists : "):]

    return f"Enter 2 Lists : {input_text}" + "\n" + output


def test_case1():
    input_text = '1,3,5,7,10,20,22 4,6,7,8,15'
    expected = """Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
LL1 : 1 3 5 7 10 20 22 
LL2 : 4 6 7 8 15 
Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22 
"""
    assert run_script(input_text) == expected

def test_case2():
    input_text = '1,4,5,5,6,7 2,3,6,9,10'
    expected = """Enter 2 Lists : 1,4,5,5,6,7 2,3,6,9,10
LL1 : 1 4 5 5 6 7 
LL2 : 2 3 6 9 10 
Merge Result : 1 2 3 4 5 5 6 6 7 9 10 
"""
    assert run_script(input_text) == expected

def test_case3():
    input_text = '2,2,2,10 1,1,1,1,5,5,5,6,7,8'
    expected = """Enter 2 Lists : 2,2,2,10 1,1,1,1,5,5,5,6,7,8
LL1 : 2 2 2 10 
LL2 : 1 1 1 1 5 5 5 6 7 8 
Merge Result : 1 1 1 1 2 2 2 5 5 5 6 7 8 10 
"""
    assert run_script(input_text) == expected
