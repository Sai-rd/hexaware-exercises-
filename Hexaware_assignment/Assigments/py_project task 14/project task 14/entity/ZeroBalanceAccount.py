from entity.Account import Account
from exception import *
class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__(customer, "ZeroBalance", 0)

    def withdraw(self, amount: float):
        try:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise insufficientFundException("Insufficient balance. To withdraw.")
            return self.balance
        except insufficientFundException as e:
            print(e)
            return self.balance
    def calculate_interest(self):
        return 0  # No interest for zero balance accounts
