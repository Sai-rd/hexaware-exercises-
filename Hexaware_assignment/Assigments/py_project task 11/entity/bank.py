from .Account import *
class Bank:
    def __init__(self):
        self.accounts = {}
        self.current_account_number = 1001

    def create_account(self, customer, acc_type, balance):
        acc_no = self.current_account_number
        self.current_account_number += 1
        new_account = Account(acc_no, acc_type, balance, customer)
        self.accounts[acc_no] = new_account
        print(f"Account created successfully with Account Number: {acc_no}")
        return acc_no

    def get_account_balance(self, acc_no):
        if acc_no in self.accounts:
            return self.accounts[acc_no].balance
        raise ValueError("Account not found")

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            return self.accounts[acc_no].deposit(amount)
        raise ValueError("Account not found")

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            return self.accounts[acc_no].withdraw(amount)
        raise ValueError("Account not found")

    def transfer(self, from_acc, to_acc, amount):
        if(from_acc==to_acc):
            raise ValueError("Same source and destination")
        if from_acc in self.accounts and to_acc in self.accounts:
            self.withdraw(from_acc, amount)
            self.deposit(to_acc, amount)
        else:
            raise ValueError("One or both accounts not found")

    def get_account_details(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].print_info()
        else:
            raise ValueError("Account not found")
