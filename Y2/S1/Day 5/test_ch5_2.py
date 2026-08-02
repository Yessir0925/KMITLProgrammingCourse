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

def test_case3():
    input_text = "R 0,A 1,A 1,A 2,R 1"
    expected = """Enter Input : R 0,A 1,A 1,A 2,R 1
Not Found!
linked list : 
reverse : 
linked list : 1
reverse : 1
linked list : 1->1
reverse : 1->1
linked list : 1->1->2
reverse : 2->1->1
removed : 1 from index : 0
linked list : 1->2
reverse : 2->1
"""
    assert run_script(input_text) == expected

def test_case4():
    input_text = "R 0, I -1:0, Ab 0, A 1, R 0, I 0:0, A 99, I 3:59, I 0:0, R 99, A 10"
    expected = """Enter Input : R 0, I -1:0, Ab 0, A 1, R 0, I 0:0, A 99, I 3:59, I 0:0, R 99, A 10
Not Found!
linked list : 
reverse : 
Data cannot be added
linked list : 
reverse : 
linked list : 0
reverse : 0
linked list : 0->1
reverse : 1->0
removed : 0 from index : 0
linked list : 1
reverse : 1
index = 0 and data = 0
linked list : 0->1
reverse : 1->0
linked list : 0->1->99
reverse : 99->1->0
index = 3 and data = 59
linked list : 0->1->99->59
reverse : 59->99->1->0
index = 0 and data = 0
linked list : 0->0->1->99->59
reverse : 59->99->1->0->0
removed : 99 from index : 3
linked list : 0->0->1->59
reverse : 59->1->0->0
linked list : 0->0->1->59->10
reverse : 10->59->1->0->0
"""
    assert run_script(input_text) == expected
    
def test_case4():

"""Enter Input : I 0:0,R 0,A 0,A 1,R 0,R 1,Ab 0, Ab 1, R 1, R 0,A 1, Ab 0,R 0,R 1
index = 0 and data = 0
linked list : 0
reverse : 0
removed : 0 from index : 0
linked list : 
reverse : 
linked list : 0
reverse : 0
linked list : 0->1
reverse : 1->0
removed : 0 from index : 0
linked list : 1
reverse : 1
removed : 1 from index : 0
linked list : 
reverse : 
linked list : 0
reverse : 0
linked list : 1->0
reverse : 0->1
removed : 1 from index : 0
linked list : 0
reverse : 0
removed : 0 from index : 0
linked list : 
reverse : 
linked list : 1
reverse : 1
linked list : 0->1
reverse : 1->0
removed : 0 from index : 0
linked list : 1
reverse : 1
removed : 1 from index : 0
linked list : 
reverse : 
"""