from dao.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from dao.IBankServiceProvider import IBankServiceProvider
from entity.SavingsAccount import SavingsAccount
from entity.CurrentAccount import CurrentAccount
from entity.ZeroBalanceAccount import ZeroBalanceAccount

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, acc_type, balance):
        if acc_type.lower() == "savings":
            acc = SavingsAccount(customer, balance)
        elif acc_type.lower() == "current":
            acc = CurrentAccount(customer, balance)
        elif acc_type.lower() == "zerobalance":
            acc = ZeroBalanceAccount(customer)
        else:
            return None
        self.accounts[acc.account_number] = acc
        return acc

    def list_accounts(self):
        return list(self.accounts.values())

    def calculate_interest(self):
        for acc in self.accounts.values():
            acc.calculate_interest()
