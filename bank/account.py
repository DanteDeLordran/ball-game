from colorama import Fore, Style


class Account:

    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    def show(self):
        print(f"{Fore.RED} Name: {self.name}")
        print(f"{Fore.BLUE} Password: {self.password} {Style.RESET_ALL}")