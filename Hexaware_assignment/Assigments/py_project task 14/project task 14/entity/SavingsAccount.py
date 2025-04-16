from entity.Account import Account
from exception import *

class SavingsAccount(Account):
    def __init__(self, customer, balance, interest_rate=4.5):
        super().__init__(customer, "Savings", max(balance, 500))
        self.interest_rate = interest_rate
        self.min_balance=500

    def withdraw(self, amount: float):
        try:
            if self.balance - amount >= 500:
                self.balance -= amount
            else:
                raise insufficientFundException("Insufficient balance. To withdraw.")
            return self.balance
        except insufficientFundException as e:
            print(e)
            return self.balance
    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return interest
