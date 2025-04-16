from abc import ABC, abstractmethod
from entity.Customer import Customer

class Account(ABC):
    last_acc_no = 1000

    def __init__(self, customer: Customer, acc_type: str, balance: float):
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.account_type = acc_type
        self.balance = balance
        self.customer = customer

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount: float):
        self.balance += amount
        return self.balance

    def __str__(self):
        return (f"Account No: {self.account_number} | Type: {self.account_type} | Balance: {self.balance:.2f}\n"
                f"{str(self.customer)}")
