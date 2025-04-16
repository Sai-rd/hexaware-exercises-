from entity.Account import Account
from exception import *
class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 10000

    def __init__(self, customer, balance):
        super().__init__(customer, "Current", balance)

    def withdraw(self, amount: float):
        try:
            if self.balance - amount >= -self.OVERDRAFT_LIMIT:
                self.balance -= amount
            else:
                raise overDraftLimitExcededException("Exceeded overdraft limit.")
            return self.balance
        except overDraftLimitExcededException as e:
            print(e)
            return self.balance
    def calculate_interest(self):
        return 0  # No interest for current accounts
