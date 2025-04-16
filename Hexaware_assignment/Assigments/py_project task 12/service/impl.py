from exception.custom_exception import *
from bean.account import *
from service.interfaces import ICustomerServiceProvider, IBankServiceProvider

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise InvalidAccountException("Invalid account number")
        return account.balance

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise InvalidAccountException("Invalid account number")
        account.balance += amount
        return account.balance

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise InvalidAccountException("Invalid account number")

        if isinstance(account, CurrentAccount):
            if account.balance + account.overdraft_limit < amount:
                raise OverDraftLimitExceededException("Overdraft limit exceeded")
        elif isinstance(account, SavingsAccount):
            if account.balance - amount < 500:
                raise InsufficientFundException("Minimum balance must be 500")
        else:
            if account.balance < amount:
                raise InsufficientFundException("Insufficient balance")

        account.balance -= amount
        return account.balance

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)

        if not from_account or not to_account:
            raise InvalidAccountException("One or both account numbers are invalid")

        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def get_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise InvalidAccountException("Invalid account number")
        return str(account)


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, acc_type, balance):
        if acc_type == 'Savings':
            account = SavingsAccount(balance, customer)
        elif acc_type == 'Current':
            account = CurrentAccount(balance, customer)
        elif acc_type == 'ZeroBalance':
            account = ZeroBalanceAccount(customer)
        else:
            raise ValueError("Invalid account type")
        self.accounts[account.account_number] = account
        return account.account_number

    def list_accounts(self):
        return [str(acc) for acc in self.accounts.values()]

    def calculate_interest(self):
        result = []
        for acc in self.accounts.values():
            if isinstance(acc, SavingsAccount):
                interest = acc.balance * acc.interest_rate
                result.append((acc.account_number, interest))
        return result