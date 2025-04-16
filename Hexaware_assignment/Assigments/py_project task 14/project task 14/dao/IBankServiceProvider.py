from abc import ABC, abstractmethod

class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, acc_type, balance): pass

    @abstractmethod
    def list_accounts(self): pass

    @abstractmethod
    def calculate_interest(self): pass

    @abstractmethod
    def get_account_balance(self, account_number):
        pass
    
    @abstractmethod
    def getAccountDetails(self, account_number):
        pass