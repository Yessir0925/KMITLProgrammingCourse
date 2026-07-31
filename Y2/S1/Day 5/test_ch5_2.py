import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "ch5_2.py"


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
    input_text = "A 3,A 4,Ab 0,I 1:2"
    expected = """Enter Input : A 3,A 4,Ab 0,I 1:2
linked list : 3
reverse : 3
linked list : 3->4
reverse : 4->3
linked list : 0->3->4
reverse : 4->3->0
index = 1 and data = 2
linked list : 0->2->3->4
reverse : 4->3->2->0
"""
    assert run_script(input_text) == expected

def test_case2():
    input_text = "I -1:0,I 10:10,I 0:0"
    expected = """Enter Input : I -1:0,I 10:10,I 0:0
Data cannot be added
linked list : 
reverse : 
Data cannot be added
linked list : 
reverse : 
index = 0 and data = 0
linked list : 0
reverse : 0
"""
    assert run_script(input_text) == expected