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
    input_text = "AP I,AP Love,AP KMITL,AP 2020"
    expected = """Enter Input : AP I,AP Love,AP KMITL,AP 2020
Linked List : I Love KMITL 2020 
"""
    assert run_script(input_text) == expected


def test_case2():
    input_text = "AP I,AP Love,AH KMITL,AP 2020"
    expected = """Enter Input : AP I,AP Love,AH KMITL,AP 2020
Linked List : KMITL I Love 2020 
"""
    assert run_script(input_text) == expected


def test_case3():
    input_text = "SE 2020,SI,ID KMITL,PO 1"
    expected = """Enter Input : SE 2020,SI,ID KMITL,PO 1
Not Found 2020 in Empty
Linked List size = 0 : Empty
Index (KMITL) = -1 : Empty
Out of Range | Empty
Linked List : Empty
"""
    assert run_script(input_text) == expected


def test_case4():
    input_text = "AP I,AP Love,AP KMITL,AP 2020,SE 2020,SI,ID KMITL,PO 1"
    expected = """Enter Input : AP I,AP Love,AP KMITL,AP 2020,SE 2020,SI,ID KMITL,PO 1
Found 2020 in I Love KMITL 2020 
Linked List size = 4 : I Love KMITL 2020 
Index (KMITL) = 2 : I Love KMITL 2020 
Success | I Love KMITL 2020 -> I KMITL 2020 
Linked List : I KMITL 2020 
"""
    assert run_script(input_text) == expected


def test_case5():
    input_text = "PO -999,PO 999,PO 0,AP KMITL"
    expected = """Enter Input : PO -999,PO 999,PO 0,AP KMITL
Out of Range | Empty
Out of Range | Empty
Out of Range | Empty
Linked List : KMITL 
"""
    assert run_script(input_text) == expected


def test_case6():
    input_text = (
        "SE KMITL,AH LOVE,AH I,AP KMITL,"
        "SE KMITL,ID KMITL,AP KMITL,"
        "SE KMITL,ID KMITL,AH KMITL,"
        "SE KMITL,ID KMITL"
    )
    expected = """Enter Input : SE KMITL,AH LOVE,AH I,AP KMITL,SE KMITL,ID KMITL,AP KMITL,SE KMITL,ID KMITL,AH KMITL,SE KMITL,ID KMITL
Not Found KMITL in Empty
Found KMITL in I LOVE KMITL 
Index (KMITL) = 2 : I LOVE KMITL 
Found KMITL in I LOVE KMITL KMITL 
Index (KMITL) = 2 : I LOVE KMITL KMITL 
Found KMITL in KMITL I LOVE KMITL KMITL 
Index (KMITL) = 0 : KMITL I LOVE KMITL KMITL 
Linked List : KMITL I LOVE KMITL KMITL 
"""
    assert run_script(input_text) == expected


def test_case7():
    input_text = (
        "SI,AH KMITL,SI,AH LOVE,"
        "SI,AH I,SI,AP 2020,SI"
    )
    expected = """Enter Input : SI,AH KMITL,SI,AH LOVE,SI,AH I,SI,AP 2020,SI
Linked List size = 0 : Empty
Linked List size = 1 : KMITL 
Linked List size = 2 : LOVE KMITL 
Linked List size = 3 : I LOVE KMITL 
Linked List size = 4 : I LOVE KMITL 2020 
Linked List : I LOVE KMITL 2020 
"""
    assert run_script(input_text) == expected


def test_case8():
    input_text = (
        "SE KMITL,AH KMITL,SE KMITL,"
        "AH LOVE,SE KMITL,AH I,"
        "SE 2020,AP 2020,SI"
    )
    expected = """Enter Input : SE KMITL,AH KMITL,SE KMITL,AH LOVE,SE KMITL,AH I,SE 2020,AP 2020,SI
Not Found KMITL in Empty
Found KMITL in KMITL 
Found KMITL in LOVE KMITL 
Not Found 2020 in I LOVE KMITL 
Linked List size = 4 : I LOVE KMITL 2020 
Linked List : I LOVE KMITL 2020 
"""
    assert run_script(input_text) == expected


def test_case9():
    input_text = "ID 1,ID WOW,AP WOW,AP KMITL,ID 1,ID WOW"
    expected = """Enter Input : ID 1,ID WOW,AP WOW,AP KMITL,ID 1,ID WOW
Index (1) = -1 : Empty
Index (WOW) = -1 : Empty
Index (1) = -1 : WOW KMITL 
Index (WOW) = 0 : WOW KMITL 
Linked List : WOW KMITL 
"""
    assert run_script(input_text) == expected