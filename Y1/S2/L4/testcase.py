##################################################################################
# testcase.py  (rewritten to match YOUR main.py classes with minimal changes)
# Works with: Bank, User, SavingAccount, FixedDeposit, ATMCard, DebitCard,
#             ATMMachine, EDCMachine
##################################################################################

from main import *

# IMPORTANT NOTE:
# Your main.py does NOT have: Seller, FixDepositAccount, ATM_Card, Debit_Card, ATM_machine, EDC_machine
# So this testcase uses YOUR actual class names:
#   FixedDeposit (not FixDepositAccount)
#   ATMCard / DebitCard (not ATM_Card / Debit_Card)
#   ATMMachine (not ATM_machine)
#   EDCMachine (not EDC_machine)
#
# Also, your User supports only ONE account via user.account (not multiple).
# So we keep Hermione fixed deposit as a separate user ID like before, but we don't need it for tests.

##################################################################################
# DATA (same as before)
##################################################################################

user = {
    '1-1101-12345-12-0': ['Harry Potter', 'Savings', '1234567890', 20000, 'ATM', '12345'],
    '1-1101-12345-13-0': ['Hermione Jean Granger', 'Saving', '0987654321', 2000, 'Debit', '12346'],
    '1-1101-12345-14-0': ['Hermione Jean Granger', 'Fix Deposit', '0987654322', 1000, '', ''],
    '9-0000-00000-01-0': ['KFC', 'Savings', '0000000321', 0, '', ''],
    '9-0000-00000-02-0': ['Tops', 'Savings', '0000000322', 0, '', '']
}

atm = {'1001': 1000000, '1002': 200000}

# For EDC, since you don't have Seller class, we create EDC machines directly
EDC = {'2101': "KFC", '2201': "Tops"}


##################################################################################
# SETUP
##################################################################################

scb = Bank('SCB')

# Create users
harry = User('1-1101-12345-12-0', 'Harry Potter')
hermione = User('1-1101-12345-13-0', 'Hermione Jean Granger')
hermione_fd = User('1-1101-12345-14-0', 'Hermione Jean Granger')
kfc_user = User('9-0000-00000-01-0', 'KFC')
tops_user = User('9-0000-00000-02-0', 'Tops')

scb.add_user(harry)
scb.add_user(hermione)
scb.add_user(hermione_fd)
scb.add_user(kfc_user)
scb.add_user(tops_user)

# Create accounts and register to bank
harry_account = SavingAccount('1234567890', 20000)
scb.add_account(harry_account, harry)

hermione_account = SavingAccount('0987654321', 2000)
scb.add_account(hermione_account, hermione)

# (Optional) fixed deposit record - not used in tests but created to match data
hermione_fd_account = FixedDeposit('0987654322', 1000)
scb.add_account(hermione_fd_account, hermione_fd)

kfc_account = SavingAccount('0000000321', 0)
scb.add_account(kfc_account, kfc_user)

tops_account = SavingAccount('0000000322', 0)
scb.add_account(tops_account, tops_user)

# Create cards and register to bank
harry_card = ATMCard('12345', harry_account, '1234')
scb.add_card(harry_card)

hermione_card = DebitCard('12346', hermione_account, '1234')
scb.add_card(hermione_card)

# Create ATMs and register to bank
atm1 = ATMMachine('1001', 1000000)
atm2 = ATMMachine('1002', 200000)
scb.add_atm_machine(atm1)
scb.add_atm_machine(atm2)

# Create EDC machines (no Seller class in your main.py)
kfc_edc = EDCMachine('2101', 'KFC')
tops_edc = EDCMachine('2201', 'Tops')


##################################################################################
# TEST CASE #1: Deposit from ATM using Harry's card
##################################################################################

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
atm_card = harry_account.get_card()

print("Test Case #1")
print("Harry's ATM No : ", atm_card.card_no)
print("Harry's Account No : ", harry_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Harry account before deposit : ", harry_account.amount)
print("Deposit 1000")
atm_machine.deposit(harry_account, 1000)
print("Harry account after deposit : ", harry_account.amount)
print("")


##################################################################################
# TEST CASE #2: Withdraw from ATM using Hermione's card
##################################################################################

atm_machine = scb.search_atm_machine('1002')
hermione_account = scb.search_account_from_card('12346')
atm_card = hermione_account.get_card()

print("Test Case #2")
print("Hermione's ATM No : ", atm_card.card_no)
print("Hermione's Account No : ", hermione_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Hermione account before withdraw : ", hermione_account.amount)
print("withdraw 1000")
atm_machine.withdraw(hermione_account, 1000)
print("Hermione account after withdraw : ", hermione_account.amount)
print("")


##################################################################################
# TEST CASE #3: Transfer 10,000 from Harry -> Hermione at counter
# (No counter class in your main.py, so we use atm1.transfer as the transfer engine)
##################################################################################

harry_account = scb.search_account_from_card('12345')
hermione_account = scb.search_account_from_card('12346')

print("Test Case #3")
print("Harry's Account No : ", harry_account.account_no)
print("Hermione's Account No : ", hermione_account.account_no)
print("Harry account before transfer : ", harry_account.amount)
print("Hermione account before transfer : ", hermione_account.amount)

# Use ATM transfer to simulate counter transfer
atm1.transfer(harry_account, hermione_account, 10000)

print("Harry account after transfer : ", harry_account.amount)
print("Hermione account after transfer : ", hermione_account.amount)
print("")


##################################################################################
# TEST CASE #4: Payment using EDC machine (Hermione pays 500 to KFC)
##################################################################################

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
kfc_account = scb.search_account_from_account_no('0000000321')

print("Test Case #4")
print("Hermione's Debit Card No : ", debit_card.card_no)
print("Hermione's Account No : ", hermione_account.account_no)
print("Seller : ", "KFC")
print("KFC's Account No : ", kfc_account.account_no)
print("KFC account before paid : ", kfc_account.amount)
print("Hermione account before paid : ", hermione_account.amount)

kfc_edc.paid(debit_card, 500, kfc_account)

print("KFC account after paid : ", kfc_account.amount)
print("Hermione account after paid : ", hermione_account.amount)
print("")


##################################################################################
# TEST CASE #5: Electronic payment (Hermione pays 500 to Tops)
##################################################################################

hermione_account = scb.search_account_from_account_no('0987654321')
tops_account = scb.search_account_from_account_no('0000000322')

print("Test Case #5")
print("Hermione's Account No : ", hermione_account.account_no)
print("Tops's Account No : ", tops_account.account_no)
print("Tops account before paid : ", tops_account.amount)
print("Hermione account before paid : ", hermione_account.amount)

tops_edc.transfer(hermione_account, tops_account, 500)

print("Tops account after paid : ", tops_account.amount)
print("Hermione account after paid : ", hermione_account.amount)
print("")


##################################################################################
# TEST CASE #6: Display all transactions of Hermione using a for loop
##################################################################################

print("Test Case #6")
print("Hermione Transactions:")

hermione_account = scb.search_account_from_account_no('0987654321')
for t in hermione_account:
    print(t)

print("")