from entity.Account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__(customer, "ZeroBalance", 0)

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")
        return self.balance

    def calculate_interest(self):
        return 0  # No interest for zero balance accounts
