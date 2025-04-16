from entity.Accounts import *
class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance, interest_rate=0.045):
        super().__init__(account_number, customer_name, balance)
        self.__interest_rate = interest_rate

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount:.2f} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount:.2f} successfully.")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest = self._balance * self.__interest_rate
        self._balance += interest
        print(f"Interest of ₹{interest:.2f} added to balance.")
