from bank.account import Account


class Bank:

    def __init__(self):
        self.accounts : dict[int, Account] = {}
        self.next_account_number = 0

    def create_account(self, name : str, amount : float, password : str) -> int:
        account = Account(name, amount, password)
        self.accounts[self.next_account_number] = account
        self.next_account_number += 1
        return self.next_account_number - 1

    def open_account(self):
        name = input("Name of the user account: ")
        password = input("Password for the user account: ")
        balance = float(input("Initial balance for the user account: "))
        account_number = self.create_account(name, balance, password)
        print(f"Account number: {account_number}")

    def close_account(self):
        print("Closing the account")
        account_number = int(input("Account number: "))
        password = input("Password for the user account: ")
        account = self.accounts[account_number]
        if password != account.password:
            print("Wrong password")
            return
        if account.balance != 0:
            print(f"Your balance is not zero, please withdraw all first (current balance: {account.balance})")
            return
        self.accounts.pop(account_number)

    def balance(self):
        print("Balance of the account")
        account_number = int(input("Account number: "))
        password = input("Password for the user account: ")
        account = self.accounts[account_number]
        if password != account.password:
            print("Wrong password")
            return
        print(f"Your balance is {account.balance}")

    def deposit(self):
        print("Deposit of the account")
        account_number = int(input("Account number: "))
        password = input("Password for the user account: ")
        amount = float(input("Amount to deposit: "))
        account = self.accounts[account_number]
        balance = account.deposit(amount, password)
        if balance is not None:
            print(f"Your balance is {balance}")

    def show_all(self):
        print("Accounts:")
        for account in self.accounts.values():
            account.show()