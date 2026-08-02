import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "ch5_4.py"

"""Kritsada had a brilliant idea to create his own Text Editor similar to VIM, which operates in a single mode called Command Mode (our input). The program includes 5 commands: Insert (I), Left (L), Right (R), Backspace (B), and Delete (D). (The functionality of each command is explained below.) However, Kritsada lacks programming skills, so he requested help from computer engineering students to develop the Text Editor he envisioned. The output should display the remaining word after executing the commands and the position of the cursor.
Explanation of the 5 Input Commands:

    I <word>: Inserts the word at the current cursor position. After inserting the word, the cursor moves to the end of the inserted word.

    L: Moves the cursor one position to the left. If the cursor is already at the leftmost position, nothing happens.

    R: Moves the cursor one position to the right. If the cursor is already at the rightmost position, nothing happens.

    B: Deletes the character to the left of the cursor. If the cursor is already at the leftmost position, nothing happens.

    D: Deletes the character to the right of the cursor. If the cursor is already at the rightmost position, nothing happens."""

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
    input_text = 'I Apple,I Bird,I Cat'
    expected = """Enter Input : I Apple,I Bird,I Cat
Apple Bird Cat | 
"""
    assert run_script(input_text) == expected

def test_case2():
    input_text = 'I Apple,I Bird,I Cat,L'
    expected = """Enter Input : I Apple,I Bird,I Cat,L
Apple Bird | Cat 
"""
    assert run_script(input_text) == expected

def test_case3():
    input_text = 'I Apple,I Bird,I Cat,L,L'
    expected = """Enter Input : I Apple,I Bird,I Cat,L,L
Apple | Bird Cat 
"""
    assert run_script(input_text) == expected

def test_case4():
    input_text = 'I Apple,I Bird,I Cat,L,L,L,L,L'
    expected = """Enter Input : I Apple,I Bird,I Cat,L,L,L,L,L
| Apple Bird Cat 
"""
    assert run_script(input_text) == expected

def test_case5():
    input_text = 'I Apple,I Bird,I Cat,L,L,R'
    expected = """Enter Input : I Apple,I Bird,I Cat,L,L,R
Apple Bird | Cat 
"""
    assert run_script(input_text) == expected

def test_case6():
    input_text = 'I Apple,I Bird,I Cat,L,L,R,B'
    expected = """Enter Input : I Apple,I Bird,I Cat,L,L,R,B
Apple | Cat 
"""
    assert run_script(input_text) == expected

def test_case7():
    input_text = 'I Apple,I Bird,L,L,R,D,D'
    expected = """Enter Input : I Apple,I Bird,L,L,R,D,D
Apple | 
"""
    assert run_script(input_text) == expected

def test_case8():
    input_text = 'L,R,I ABC,I DE,L,I FGHI'
    expected = """Enter Input : L,R,I ABC,I DE,L,I FGHI
ABC FGHI | DE 
"""
    assert run_script(input_text) == expected

def test_case9():
    input_text = 'I A,I B,L,L,R,D,D,L,L,R,I BCD,L,L,B,D,R,R,L,L'
    expected = """Enter Input : I A,I B,L,L,R,D,D,L,L,R,I BCD,L,L,B,D,R,R,L,L
| BCD 
"""
    assert run_script(input_text) == expected

def test_case10():
    input_text = 'I I,I KMITL,L,L,R,I Love'
    expected = """Enter Input : I I,I KMITL,L,L,R,I Love
I Love | KMITL 
"""
    assert run_script(input_text) == expected

def test_case11():
    input_text = 'I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate'
    expected = """Enter Input : I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate
I Hate | DataStructure 
"""
    assert run_script(input_text) == expected
