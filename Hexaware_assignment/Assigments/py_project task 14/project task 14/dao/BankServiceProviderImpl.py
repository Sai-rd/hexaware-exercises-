from dao.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from dao.IBankServiceProvider import IBankServiceProvider
from entity.SavingsAccount import SavingsAccount
from entity.CurrentAccount import CurrentAccount
from entity.ZeroBalanceAccount import ZeroBalanceAccount
from entity.transaction import Transaction  # Make sure to import Transaction class

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address
        self.accounts = {}  # Dictionary to store accounts
        self.transactionList = []  # List to store transaction objects

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

    def get_account_balance(self, account_number):
        acc = self.accounts.get(account_number)
        return acc.balance if acc else None

    def getAccountDetails(self, account_number):
        # Fetch the account using account_number
        acc = self.accounts.get(account_number)
        if acc:
            customer_details = {
                "customer_id": acc.customer.customer_id,
                "first_name": acc.customer.first_name,
                "last_name": acc.customer.last_name,
                "email": acc.customer.email,
                "phone": acc.customer.phone,
                "address": acc.customer.address
            }
            account_details = {
                "account_number": acc.account_number,
                "account_type": acc.account_type,
                "balance": acc.balance
            }
            return {"customer_details": customer_details, "account_details": account_details}
        else:
            return None

    def add_transaction(self, transaction):
        self.transactionList.append(transaction)

    def get_transactions(self, account_number, from_date, to_date):
        transactions = []
        for transaction in self.transactionList:
            if transaction.get_account_id() == account_number and from_date <= transaction.get_transaction_date().date() <= to_date:
                transactions.append(transaction)
        return transactions
