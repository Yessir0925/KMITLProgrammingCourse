# testcase.py
# Run: python3 -u testcase.py

import io
from contextlib import redirect_stdout
import main  # main.py must contain your classes


class SimpleBank:
    """Minimal bank container to match ATMMachine.insert_card(bank, card_number, pin)."""
    def __init__(self):
        self.cards = {}  # card_number -> ATMCard

    def add_card(self, card):
        self.cards[card.card_number] = card


def build_fixture():
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


def run_tests_print_style():
    print("--------------------------")
    print("     Start Test Cases     ")
    print("--------------------------")

    # Fresh setup
    bank, harry, hermione, atm1, atm2 = build_fixture()

    # -------------------------
    # Test case #1
    # -------------------------
    print("Test case #1: Insert Harry's ATM card into ATM machine #1")
    acc = atm1.insert_card(bank, "12345", "1234")
    if acc is None:
        print("Ans: Error")
    else:
        print(f"Ans: {acc.card.card_number}, {acc.account_number}, Success")
    print("-------------------------")

    # -------------------------
    # Test case #2
    # -------------------------
    print("Test case #2: Deposit 1000 Baht into Hermione's account using ATM machine #2")
    print(f"Hermione's account before test: {hermione.balance}")
    result = atm2.deposit(hermione, 1000)
    if result == "success":
        print(f"Hermione's account after test: {hermione.balance}")
        print(f"Transaction: {hermione.transactions[-1]}")
    else:
        print("Error")
    print("-------------------------")

    # -------------------------
    # Test case #3
    # -------------------------
    print("Test case #3: Deposit -1 Baht into Hermione's account using ATM machine #2")
    result = atm2.deposit(hermione, -1)
    print("Error" if result != "success" else "Success")
    print("-------------------------")

    # -------------------------
    # Test case #4
    # -------------------------
    print("Test case #4: Withdraw 500 Baht from Hermione's account using ATM machine #2")
    print(f"Hermione's account before test: {hermione.balance}")
    result = atm2.withdraw(hermione, 500)
    if result == "success":
        print(f"Hermione's account after test: {hermione.balance}")
        print(f"Transaction: {hermione.transactions[-1]}")
    else:
        print("Error")
    print("-------------------------")

    # -------------------------
    # Test case #5
    # -------------------------
    print("Test case #5: Withdraw 2000 Baht from Hermione's account using ATM machine #2")
    result = atm2.withdraw(hermione, 2000)
    print("Error" if result != "success" else "Success")
    print("-------------------------")

    # -------------------------
    # Test case #6
    # -------------------------
    print("Test case #6: Transfer 10,000 Baht from Harry to Hermione using ATM machine #2")
    print(f"Harry's account before test: {harry.balance}")
    print(f"Hermione's account before test: {hermione.balance}")
    result = atm2.transfer(harry, hermione, 10000)
    if result == "success":
        print(f"Harry's account after test: {harry.balance}")
        print(f"Hermione's account after test: {hermione.balance}")
        print(f"Transaction (Hermione): {hermione.transactions[-1]}")
    else:
        print("Error")
    print("-------------------------")

    # -------------------------
    # Test case #7
    # -------------------------
    print("Test case #7: Display all of Hermione's transactions.")
    print("Hermione's transaction log:")
    for t in hermione.transactions:
        print(t)
    print("-------------------------")

    # -------------------------
    # Test case #8
    # -------------------------
    print("Test case #8: Insert card with incorrect PIN (Harry card, PIN=9999)")
    buf = io.StringIO()
    with redirect_stdout(buf):
        _ = atm1.insert_card(bank, "12345", "9999")
    out = buf.getvalue().strip()
    # Your insert_card prints "Invalid PIN"
    print(out if out else "No output")
    print("-------------------------")

    # -------------------------
    # Test case #9
    # -------------------------
    print("Test case #9: Withdraw more than daily limit (40,000 Baht).")
    print(f"Harry's account before test: {harry.balance}")
    print("Attempting to withdraw 45,000 Baht...")
    result = atm1.withdraw(harry, 45000)
    print("Expected result: Exceeds daily withdrawal limit of 40,000 Baht")
    print(f"Actual result: {result}")
    print(f"Harry's account after test: {harry.balance}")
    print("-------------------------")

    # -------------------------
    # Test case #10
    # -------------------------
    print("Test case #10: Withdrawal when ATM has insufficient funds.")
    print(f"ATM machine balance before: {atm2.cash}")
    print("Attempting to withdraw 250,000 Baht...")
    result = atm2.withdraw(harry, 250000)
    print("Expected result: ATM has insufficient funds.")
    print(f"Actual result: {result}")
    print(f"ATM machine balance after: {atm2.cash}")
    print("-------------------------")


if __name__ == "__main__":
    run_tests_print_style()