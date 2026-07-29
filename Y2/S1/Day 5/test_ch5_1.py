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
    expected = (
        "Enter Input : AP I,AP Love,AP KMITL,AP 2020\n"
        "Linked List : I Love KMITL 2020 \n"
    )
    assert run_script(input_text) == expected


def test_case2():
    input_text = "AP I,AP Love,AH KMITL,AP 2020"
    expected = (
        "Enter Input : AP I,AP Love,AH KMITL,AP 2020\n"
        "Linked List : KMITL I Love 2020 \n"
    )
    assert run_script(input_text) == expected


def test_case3():
    input_text = "SE 2020,SI,ID KMITL,PO 1"
    expected = (
        "Enter Input : SE 2020,SI,ID KMITL,PO 1\n"
        "Not Found 2020 in Empty\n"
        "Linked List size = 0 : Empty\n"
        "Index (KMITL) = -1 : Empty\n"
        "Out of Range | Empty\n"
        "Linked List : Empty\n"
    )
    assert run_script(input_text) == expected


def test_case4():
    input_text = "AP I,AP Love,AP KMITL,AP 2020,SE 2020,SI,ID KMITL,PO 1"
    expected = (
        "Enter Input : AP I,AP Love,AP KMITL,AP 2020,SE 2020,SI,ID KMITL,PO 1\n"
        "Found 2020 in I Love KMITL 2020 \n"
        "Linked List size = 4 : I Love KMITL 2020 \n"
        "Index (KMITL) = 2 : I Love KMITL 2020 \n"
        "Success | I Love KMITL 2020 -> I KMITL 2020 \n"
        "Linked List : I KMITL 2020 \n"
    )
    assert run_script(input_text) == expected


def test_case5():
    input_text = "PO -999,PO 999,PO 0,AP KMITL"
    expected = (
        "Enter Input : PO -999,PO 999,PO 0,AP KMITL\n"
        "Out of Range | Empty\n"
        "Out of Range | Empty\n"
        "Out of Range | Empty\n"
        "Linked List : KMITL \n"
    )
    assert run_script(input_text) == expected


def test_case6():
    input_text = (
        "SE KMITL,AH LOVE,AH I,AP KMITL,"
        "SE KMITL,ID KMITL,AP KMITL,"
        "SE KMITL,ID KMITL,AH KMITL,"
        "SE KMITL,ID KMITL"
    )
    expected = (
        "Enter Input : SE KMITL,AH LOVE,AH I,AP KMITL,"
        "SE KMITL,ID KMITL,AP KMITL,"
        "SE KMITL,ID KMITL,AH KMITL,"
        "SE KMITL,ID KMITL\n"
        "Not Found KMITL in Empty\n"
        "Found KMITL in I LOVE KMITL \n"
        "Index (KMITL) = 2 : I LOVE KMITL \n"
        "Found KMITL in I LOVE KMITL KMITL \n"
        "Index (KMITL) = 2 : I LOVE KMITL KMITL \n"
        "Found KMITL in KMITL I LOVE KMITL KMITL \n"
        "Index (KMITL) = 0 : KMITL I LOVE KMITL KMITL \n"
        "Linked List : KMITL I LOVE KMITL KMITL \n"
    )
    assert run_script(input_text) == expected


def test_case7():
    input_text = (
        "SI,AH KMITL,SI,AH LOVE,"
        "SI,AH I,SI,AP 2020,SI"
    )
    expected = (
        "Enter Input : SI,AH KMITL,SI,AH LOVE,SI,AH I,SI,AP 2020,SI\n"
        "Linked List size = 0 : Empty\n"
        "Linked List size = 1 : KMITL \n"
        "Linked List size = 2 : LOVE KMITL \n"
        "Linked List size = 3 : I LOVE KMITL \n"
        "Linked List size = 4 : I LOVE KMITL 2020 \n"
        "Linked List : I LOVE KMITL 2020 \n"
    )
    assert run_script(input_text) == expected


def test_case8():
    input_text = (
        "SE KMITL,AH KMITL,SE KMITL,"
        "AH LOVE,SE KMITL,AH I,"
        "SE 2020,AP 2020,SI"
    )
    expected = (
        "Enter Input : SE KMITL,AH KMITL,SE KMITL,AH LOVE,SE KMITL,AH I,SE 2020,AP 2020,SI\n"
        "Not Found KMITL in Empty\n"
        "Found KMITL in KMITL \n"
        "Found KMITL in LOVE KMITL \n"
        "Not Found 2020 in I LOVE KMITL \n"
        "Linked List size = 4 : I LOVE KMITL 2020 \n"
        "Linked List : I LOVE KMITL 2020 \n"
    )
    assert run_script(input_text) == expected


def test_case9():
    input_text = "ID 1,ID WOW,AP WOW,AP KMITL,ID 1,ID WOW"
    expected = (
        "Enter Input : ID 1,ID WOW,AP WOW,AP KMITL,ID 1,ID WOW\n"
        "Index (1) = -1 : Empty\n"
        "Index (WOW) = -1 : Empty\n"
        "Index (1) = -1 : WOW KMITL \n"
        "Index (WOW) = 0 : WOW KMITL \n"
        "Linked List : WOW KMITL \n"
    )
    assert run_script(input_text) == expected