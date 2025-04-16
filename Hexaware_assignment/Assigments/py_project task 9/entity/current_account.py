from entity.Accounts import *
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 10000

    def __init__(self, account_number, customer_name, balance):
        super().__init__(account_number, customer_name, balance)

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount:.2f} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount: float):
        if amount <= self._balance + self.OVERDRAFT_LIMIT:
            self._balance -= amount
            print(f"Withdrawn ₹{amount:.2f} successfully.")
        else:
            print("Overdraft limit exceeded.")

    def calculate_interest(self):
        print("No interest is calculated on current accounts.")
