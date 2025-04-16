class Account:
    def __init__(self, account_number, account_type, balance, customer):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient balance")

    def print_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ₹{self.balance:.2f}")
        self.customer.print_info()
