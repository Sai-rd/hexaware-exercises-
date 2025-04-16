class Account:
    def __init__(self, acc_number=None, acc_type="Generic", balance=0.0):
        self._account_number = acc_number
        self._account_type = acc_type
        self._account_balance = float(balance)

    # Overloaded deposit
    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            if amount > 0:
                self._account_balance += float(amount)
                print(f"Deposited ₹{amount:.2f} successfully.")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Invalid type for deposit amount.")

    # Overloaded withdraw
    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if amount <= self._account_balance:
                self._account_balance -= float(amount)
                print(f"Withdrawn ₹{amount:.2f} successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid type for withdrawal amount.")

    def calculate_interest(self):
        print("Generic accounts do not accrue interest.")

    def print_account_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Account Type: {self._account_type}")
        print(f"Account Balance: ₹{self._account_balance:.2f}")

    def get_balance(self):
        return self._account_balance

    def set_balance(self, balance):
        self._account_balance = balance

class SavingsAccount(Account):
    def __init__(self, acc_number, balance, interest_rate=0.045):
        super().__init__(acc_number, "Savings", balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._account_balance * self.__interest_rate
        self._account_balance += interest
        print(f"Interest ₹{interest:.2f} added to balance.")

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 10000  # Fixed overdraft limit

    def __init__(self, acc_number, balance):
        super().__init__(acc_number, "Current", balance)

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if amount <= self._account_balance + self.OVERDRAFT_LIMIT:
                self._account_balance -= float(amount)
                print(f"Withdrawn ₹{amount:.2f} successfully.")
            else:
                print("Overdraft limit exceeded.")
        else:
            print("Invalid type for withdrawal amount.")

    def calculate_interest(self):
        print("Current accounts do not accrue interest.")
