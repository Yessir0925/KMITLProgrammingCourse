import importlib
import sys
from io import StringIO
from unittest.mock import patch

def test_case1(capsys):
    with patch("builtins.input", return_value="1"):
        if "ch6_1" in sys.modules:
            del sys.modules["ch6_1"]

        import ch6_1

    captured = capsys.readouterr().out

    expected = """ *** Find fibonacci sequence ***
Enter n : 1
fibo(1) = 1
===== End of program =====
"""

    assert captured == expected


""" *** Find fibonacci sequence ***
Enter n : 2
fibo(2) = 1
===== End of program =====

 *** Find fibonacci sequence ***
Enter n : 3
fibo(3) = 2
===== End of program =====

 *** Find fibonacci sequence ***
Enter n : 4
fibo(4) = 3
===== End of program =====

 *** Find fibonacci sequence ***
Enter n : 5
fibo(5) = 5
===== End of program =====

 *** Find fibonacci sequence ***
Enter n : 6
fibo(6) = 8
===== End of program =====
"""