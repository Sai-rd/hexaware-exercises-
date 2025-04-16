from dao.ICustomerServiceProvider import ICustomerServiceProvider

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        acc = self.accounts.get(account_number)
        return acc.balance if acc else None

    def deposit(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            return acc.deposit(amount)
        return None

    def withdraw(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            return acc.withdraw(amount)
        return None

    def transfer(self, from_account, to_account, amount):
        from_acc = self.accounts.get(from_account)
        to_acc = self.accounts.get(to_account)
        if from_acc and to_acc:
            if from_acc.withdraw(amount) is not None:
                to_acc.deposit(amount)
                return True
        return False

    def get_account_details(self, account_number):
        return self.accounts.get(account_number, None)
