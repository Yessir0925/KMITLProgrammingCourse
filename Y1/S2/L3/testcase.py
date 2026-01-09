# testcase.py
import unittest
import io
from contextlib import redirect_stdout

import main  # main.py must contain the classes you pasted


class SimpleBank:
    """Minimal bank container to match ATMMachine.insert_card(bank, card_number, pin)."""
    def __init__(self):
        self.cards = {}  # card_number -> ATMCard

    def add_card(self, card):
        self.cards[card.card_number] = card


def build_fixture():
    """
    Create:
    - Harry: balance 20000, account 1234567890, card 12345, pin 1234
    - Hermione: balance 1000,  account 0987654321, card 12346, pin 1234
    - ATM #1001 cash 1,000,000
    - ATM #1002 cash 200,000
    """
    bank = SimpleBank()

    harry_user = main.User("1-1101-12345-12-0", "Harry Potter")
    harry_acc = main.Account("1234567890", 20000)
    harry_user.account = harry_acc
    harry_card = main.ATMCard("12345", harry_acc, "1234")
    harry_acc.card = harry_card
    bank.add_card(harry_card)

    hermione_user = main.User("1-1101-12345-13-0", "Hermione Jean Granger")
    hermione_acc = main.Account("0987654321", 1000)
    hermione_user.account = hermione_acc
    hermione_card = main.ATMCard("12346", hermione_acc, "1234")
    hermione_acc.card = hermione_card
    bank.add_card(hermione_card)

    atm1 = main.ATMMachine("1001", 1_000_000)
    atm2 = main.ATMMachine("1002", 200_000)

    return bank, harry_acc, hermione_acc, atm1, atm2


class TestATMSystem(unittest.TestCase):
    # Test case #1
    def test_1_insert_harry_card(self):
        bank, harry, _, atm1, _ = build_fixture()
        acc = atm1.insert_card(bank, "12345", "1234")
        self.assertIsNotNone(acc)
        self.assertEqual(acc.account_number, "1234567890")
        self.assertEqual(acc.card.card_number, "12345")

    # Test case #2
    def test_2_deposit_1000_to_hermione(self):
        bank, _, hermione, _, atm2 = build_fixture()
        self.assertEqual(hermione.balance, 1000)
        result = atm2.deposit(hermione, 1000)
        self.assertEqual(result, "success")
        self.assertEqual(hermione.balance, 2000)
        self.assertEqual(hermione.transactions[-1], "D-ATM:1002-1000-2000")

    # Test case #3
    def test_3_deposit_negative(self):
        bank, _, hermione, _, atm2 = build_fixture()
        result = atm2.deposit(hermione, -1)
        self.assertEqual(result, "error")
        self.assertEqual(hermione.balance, 1000)
        self.assertEqual(len(hermione.transactions), 0)

    # Test case #4
    def test_4_withdraw_500_from_hermione(self):
        bank, _, hermione, _, atm2 = build_fixture()
        # make Hermione 2000 first to match prompt flow
        self.assertEqual(atm2.deposit(hermione, 1000), "success")
        self.assertEqual(hermione.balance, 2000)

        result = atm2.withdraw(hermione, 500)
        self.assertEqual(result, "success")
        self.assertEqual(hermione.balance, 1500)
        self.assertEqual(hermione.transactions[-1], "W-ATM:1002-500-1500")

    # Test case #5
    def test_5_withdraw_2000_from_hermione_should_error(self):
        bank, _, hermione, _, atm2 = build_fixture()
        # make Hermione 1500 first to match prompt flow
        self.assertEqual(atm2.deposit(hermione, 1000), "success")  # 2000
        self.assertEqual(atm2.withdraw(hermione, 500), "success")  # 1500

        result = atm2.withdraw(hermione, 2000)
        self.assertEqual(result, "error")
        self.assertEqual(hermione.balance, 1500)

    # Test case #6
    def test_6_transfer_10000_harry_to_hermione(self):
        bank, harry, hermione, _, atm2 = build_fixture()
        # prerequisite: Hermione = 1500
        self.assertEqual(atm2.deposit(hermione, 1000), "success")  # 2000
        self.assertEqual(atm2.withdraw(hermione, 500), "success")  # 1500

        self.assertEqual(harry.balance, 20000)
        self.assertEqual(hermione.balance, 1500)

        result = atm2.transfer(harry, hermione, 10000)
        self.assertEqual(result, "success")
        self.assertEqual(harry.balance, 10000)
        self.assertEqual(hermione.balance, 11500)
        self.assertEqual(hermione.transactions[-1], "TD-ATM:1002-10000-11500")

    # Test case #7
    def test_7_hermione_transactions_log(self):
        bank, harry, hermione, _, atm2 = build_fixture()
        # Deposit 1000 -> Withdraw 500 -> Transfer 10000 to Hermione
        self.assertEqual(atm2.deposit(hermione, 1000), "success")   # 2000
        self.assertEqual(atm2.withdraw(hermione, 500), "success")   # 1500
        self.assertEqual(atm2.transfer(harry, hermione, 10000), "success")  # 11500

        expected = [
            "D-ATM:1002-1000-2000",
            "W-ATM:1002-500-1500",
            "TD-ATM:1002-10000-11500",
        ]
        self.assertEqual(hermione.transactions, expected)

    # Test case #8
    def test_8_incorrect_pin(self):
        bank, _, _, atm1, _ = build_fixture()
        buf = io.StringIO()
        with redirect_stdout(buf):
            acc = atm1.insert_card(bank, "12345", "9999")
        out = buf.getvalue()

        self.assertIsNone(acc)
        self.assertIn("Invalid PIN", out)

    # Test case #9
    def test_9_withdraw_over_daily_limit(self):
        bank, harry, _, atm1, _ = build_fixture()
        # Your withdraw() returns "error" when exceeding limit.
        result = atm1.withdraw(harry, 45000)
        self.assertEqual(result, "error")
        self.assertEqual(harry.balance, 20000)

    # Test case #10
    def test_10_withdraw_atm_insufficient_funds(self):
        bank, harry, _, _, atm2 = build_fixture()  # atm2 has 200,000
        # Your withdraw() returns "error" when ATM doesn't have enough cash.
        result = atm2.withdraw(harry, 250000)
        self.assertEqual(result, "error")
        self.assertEqual(harry.balance, 20000)
        self.assertEqual(atm2.cash, 200000)


if __name__ == "__main__":
    unittest.main(verbosity=2)