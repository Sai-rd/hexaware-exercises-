class Account:
    def __init__(self, acc_number=None, acc_type="Savings", balance=0.0):
        self.__account_number = acc_number
        self.__account_type = acc_type
        self.__account_balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def get_account_balance(self):
        return self.__account_balance

    def set_account_number(self, acc_number):
        self.__account_number = acc_number

    def set_account_type(self, acc_type):
        self.__account_type = acc_type

    def set_account_balance(self, balance):
        self.__account_balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount:.2f} successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrawn ₹{amount:.2f} successfully.")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        if self.__account_type.lower() == "savings":
            interest = self.__account_balance * 0.045
            self.__account_balance += interest
            print(f"Interest ₹{interest:.2f} added to balance.")
        else:
            print("Interest applicable only for Savings account.")

    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Account Balance: ₹{self.__account_balance:.2f}")
