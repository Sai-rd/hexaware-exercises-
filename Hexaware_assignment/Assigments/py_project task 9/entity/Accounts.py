from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number="", customer_name="", balance=0.0):
        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = balance

    # Getters and Setters
    def get_account_number(self):
        return self._account_number

    def set_account_number(self, number):
        self._account_number = number

    def get_customer_name(self):
        return self._customer_name

    def set_customer_name(self, name):
        self._customer_name = name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

    def print_account_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Customer Name: {self._customer_name}")
        print(f"Balance: ₹{self._balance:.2f}")

    # Abstract Methods
    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
