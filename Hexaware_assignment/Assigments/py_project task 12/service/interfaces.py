from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number): pass

    @abstractmethod
    def deposit(self, account_number, amount): pass

    @abstractmethod
    def withdraw(self, account_number, amount): pass

    @abstractmethod
    def transfer(self, from_account_number, to_account_number, amount): pass

    @abstractmethod
    def get_account_details(self, account_number): pass


class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, acc_type, balance): pass

    @abstractmethod
    def list_accounts(self): pass

    @abstractmethod
    def calculate_interest(self): pass