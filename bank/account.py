from colorama import Fore, Style


class Account:

    def __init__(self, name: str, balance: float, password: str):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount: float, password: str) -> float | None:
        if password != self.password:
            return None
        if amount < 0:
            return None
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float, password: str) -> float | None:
        if password != self.password:
            return None
        if amount > self.balance:
            return None
        if amount < 0:
            return None
        self.balance -= amount
        return self.balance

    def get_balance(self, password : str) -> float | None:
        if password != self.password:
            return None
        return self.balance

    def show(self):
        print(f"{Fore.RED} Name: {self.name}")
        print(f"{Fore.CYAN} Balance: {self.balance}")
        print(f"{Fore.BLUE} Password: {self.password} {Style.RESET_ALL}")