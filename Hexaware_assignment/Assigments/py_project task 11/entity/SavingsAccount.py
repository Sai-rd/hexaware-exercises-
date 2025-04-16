from entity.Account import Account

class SavingsAccount(Account):
    def __init__(self, customer, balance, interest_rate=4.5):
        super().__init__(customer, "Savings", max(balance, 500))
        self.interest_rate = interest_rate

    def withdraw(self, amount: float):
        if self.balance - amount >= 500:
            self.balance -= amount
        else:
            print("Insufficient balance. Minimum balance of ₹500 required.")
        return self.balance

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return interest
