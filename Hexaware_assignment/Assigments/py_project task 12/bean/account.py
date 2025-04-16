class Account:
    lastAccNo = 1000

    def __init__(self, account_type, balance, customer):
        Account.lastAccNo += 1
        self.account_number = Account.lastAccNo
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def __str__(self):
        return (f"Account[Number={self.account_number}, Type={self.account_type}, "
                f"Balance={self.balance}, {self.customer}]")
class SavingsAccount(Account):
    def __init__(self, balance, customer, interest_rate=0.03):
        if balance < 500:
            raise ValueError("Minimum balance for Savings Account is 500")
        super().__init__('Savings', balance, customer)
        self.interest_rate = interest_rate


class CurrentAccount(Account):
    def __init__(self, balance, customer, overdraft_limit=1000):
        super().__init__('Current', balance, customer)
        self.overdraft_limit = overdraft_limit


class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__('ZeroBalance', 0.0, customer)