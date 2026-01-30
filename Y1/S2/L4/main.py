NewYear = False

class Bank:
    def __init__(self, name: str = "Bank"):
        self.name = name
        self.cards = {}          
        self.users = {}          
        self.accounts = {}       
        self.atms = {}           

    def add_user(self, user: "User"):
        self.users[user.citizen_id] = user

    def search_user_from_id(self, citizen_id: str):
        return self.users.get(citizen_id)

    def add_account(self, account: "Account", owner: "User" = None):
        self.accounts[account.account_number] = account
        if owner is not None:
            owner.account = account 

    def search_account_from_account_no(self, account_number: str):
        return self.accounts.get(account_number)

    def add_card(self, card: "ATMCard"):
        # store card in bank registry
        self.cards[card.card_number] = card

        if isinstance(card, DebitCard):
            card.account.debit = card
        else:
            card.account.card = card

    def search_account_from_card(self, card_number: str):
        card = self.cards.get(card_number)
        return card.account if card else None

    def add_atm_machine(self, atm: "ATMMachine"):
        self.atms[atm.machine_id] = atm

    def search_atm_machine(self, machine_id: str):
        return self.atms.get(machine_id)


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
        self.debit = None
        self.transactions = []

    @property
    def account_no(self):
        return self.account_number

    @property
    def amount(self):
        return self.balance

    def get_card(self):
        return self.debit if self.debit is not None else self.card

    def __iter__(self):
        return iter(self.transactions)


class SavingAccount(Account):
    def __init__(self, account_number: str, balance: float):
        super().__init__(account_number, balance)
        if NewYear:
            self.balance *= (1 - (0.5 / 100))


class FixedDeposit(Account):
    def __init__(self, account_number: str, balance: float):
        super().__init__(account_number, balance)
        if NewYear:
            self.balance *= (1 - (2.5 / 100))


# Saving - 0.5
# Fixed Deposit - 2.5


class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.card_number = card_number
        self.account = account
        self.pin = pin
        if NewYear:
            self.account.balance -= 150

    @property
    def card_no(self):
        return self.card_number


class DebitCard(ATMCard):
    def __init__(self, card_number: str, account: Account, pin: str):
        super().__init__(card_number, account, pin)
        if NewYear:
            self.account.balance -= 300


# Debit Card - 300B
# ATM - 150B


class ATMMachine:
    DAILY_LIMIT = 40000

    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.machine_id = machine_id
        self.cash = initial_amount

    def insert_card(self, arg1, arg2=None, arg3=None):
        if isinstance(arg1, ATMCard) and isinstance(arg2, str) and arg3 is None:
            card = arg1
            pin = arg2
            if card.pin != pin:
                print("Invalid PIN")
                return None
            return "Success"

        bank = arg1
        card_number = arg2
        pin = arg3

        if card_number not in bank.cards:
            return None

        card = bank.cards[card_number]
        if card.pin != pin:
            print("Invalid PIN")
            return None

        return "Success"

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

        sender.transactions.append(
            f"TW-ATM:{self.machine_id}-{amount}-{sender.balance}"
        )
        receiver.transactions.append(
            f"TD-ATM:{self.machine_id}-{amount}-{receiver.balance}"
        )
        return "success"


class EDCMachine:
    def __init__(self, serial: str, seller: str):
        self.serial = serial
        self.seller = seller

    def paid(self, card: ATMCard, amount: float, receiver: Account):
        return self.transfer(card.account, receiver, amount)

    def transfer(self, sender: Account, receiver: Account, amount: float):
        if amount <= 0:
            return "error"
        if amount > sender.balance:
            return "error"

        sender.balance -= amount
        receiver.balance += amount

        sender.transactions.append(f"TW-EDC:{self.serial}-{amount}-{sender.balance}")
        receiver.transactions.append(f"TD-EDC:{self.serial}-{amount}-{receiver.balance}")
        return "success"