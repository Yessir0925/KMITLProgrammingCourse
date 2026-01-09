class User:
    def __init__(self, citizen_id: str, name: str):
        self.citizen_id = citizen_id
        self.name = name
        self.account = None


class Account:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance
        self.card = None
        self.transactions = []


class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.card_number = card_number
        self.account = account
        self.pin = pin


class ATMMachine:
    DAILY_LIMIT = 40000

    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.machine_id = machine_id
        self.cash = initial_amount

    def insert_card(self, bank, card_number: str, pin: str):
        if card_number not in bank.cards:
            return None

        card = bank.cards[card_number]
        if card.pin != pin:
            print("Invalid PIN")
            return None

        return card.account

    def deposit(self, account: Account, amount: float):
        if amount <= 0:
            return "error"

        account.balance += amount
        account.transactions.append(
            f"D-ATM:{self.machine_id}-{amount}-{account.balance}"
        )
        return "success"

    def withdraw(self, account: Account, amount: float):
        if amount <= 0:
            return "error"
        if amount > account.balance:
            return "error"
        if amount > self.DAILY_LIMIT:
            return "error"
        if amount > self.cash:
            return "error"

        account.balance -= amount
        self.cash -= amount
        account.transactions.append(
            f"W-ATM:{self.machine_id}-{amount}-{account.balance}"
        )
        return "success"

    def transfer(self, sender: Account, receiver: Account, amount: float):
        if amount <= 0:
            return "error"
        if amount > sender.balance:
            return "error"

        sender.balance -= amount
        receiver.balance += amount

        receiver.transactions.append(
            f"TD-ATM:{self.machine_id}-{amount}-{receiver.balance}"
        )
        return "success"