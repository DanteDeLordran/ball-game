from bank.account import Account


def main():

    accounts : dict[int, Account] = {}
    next_account_number = 0

    print("Bank account system")
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")

    action = input("What would you like to do? ").lower()[0]
    match action:
        case "b":
            print("Getting balance")
            account_number = int(input("Enter account number: "))
            password = input("Enter password: ")
            account = accounts[account_number]
            balance = account.get_balance(password)
            if balance is not None:
                print("Balance: ${0:.2f}".format(balance))

        case "d":
            print("Making a deposit")
            account_number = int(input("Enter account number: "))
            amount = int(input("Enter amount: "))
            password = input("Enter password: ")
            account = accounts[account_number]
            balance = account.deposit(amount, password)
            if balance is not None:
                print("Balance: ${0:.2f}".format(balance))

        case "o":
            print("Opening a new account")
            name = input("Enter account name: ")
            balance = float(input("Enter initial balance: "))
            password = input("Enter password: ")
            account = Account(name, balance, password)
            account.show()

        case "w":
            print("Withdrawal")
            account_number = int(input("Enter account number: "))
            amount = int(input("Enter amount: "))
            password = input("Enter password: ")
            account = accounts[account_number]
            balance = account.withdraw(amount, password)
            print(f"Balance: ${balance}")

        case "s":
            print("Showing all accounts")
            for account in accounts.values():
                account.show()

        case "q":
            print("Quit")


if __name__ == "__main__":
    main()
