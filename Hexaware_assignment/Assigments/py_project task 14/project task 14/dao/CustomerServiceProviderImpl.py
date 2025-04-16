from dao.ICustomerServiceProvider import ICustomerServiceProvider
from exception import *
from datetime import *
from entity.transaction import Transaction
from collections import defaultdict

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}  
        self.transaction_map = defaultdict(list)

    def get_account_balance(self, account_number):
        acc = self.accounts.get(account_number)
        return acc.balance if acc else None

    def deposit(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            acc.deposit(amount)
            transaction = Transaction(account_number, "deposit", amount)
            self.transaction_map[account_number].append(transaction)
            return acc.balance
        return None

    def withdraw(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            result = acc.withdraw(amount)
            if result is not None:
                transaction = Transaction(account_number, "withdraw", amount)
                self.transaction_map[account_number].append(transaction)
                return acc.balance
        return None

    def transfer(self, from_account, to_account, amount):
        try:
            from_acc = self.accounts.get(from_account)
            to_acc = self.accounts.get(to_account)
            if from_acc and to_acc:
                if from_acc.withdraw(amount) is not None:
                    to_acc.deposit(amount)
                    # Log transactions
                    self.transaction_map[from_account].append(Transaction(from_account, "transfer-out", amount))
                    self.transaction_map[to_account].append(Transaction(to_account, "transfer-in", amount))
                    return True
            else:
                if from_acc is None:
                    raise invalidAccountException("Invalid account. Enter a valid from account.")
                elif to_acc is None:
                    raise invalidAccountException("Invalid account. Enter a valid to account.")
                else:
                    raise invalidAccountException("Invalid account. Enter valid from and to accounts.")
        except invalidAccountException as e:
            print(e)
        return False

    def get_account_details(self, account_number):
        return self.accounts.get(account_number, None)

    def get_transactions(self, account_number, from_date, to_date):
        if account_number not in self.transaction_map:
            print("No transactions found for this account.")
            return []

        all_transactions = self.transaction_map[account_number]
        filtered = [
            tx for tx in all_transactions
            if from_date <= tx.get_transaction_date().date() <= to_date
        ]
        return filtered
