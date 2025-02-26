class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")

account = BankAccount("987654321", "Alice Johnson", 1500)
account.deposit(300)
account.withdraw(200)
account.display_balance()
