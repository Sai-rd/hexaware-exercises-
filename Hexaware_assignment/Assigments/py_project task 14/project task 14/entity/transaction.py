import datetime

class Transaction:
    transaction_counter = 1000

    def __init__(self, transaction_id, account_number, transaction_type, amount, balance_after, transaction_date=None, description=""):
        self.__transaction_id = transaction_id or Transaction.transaction_counter
        Transaction.transaction_counter = max(Transaction.transaction_counter, self.__transaction_id + 1)

        self.__account_number=account_number
        self.__transaction_type = transaction_type
        self.__amount = float(amount)
        self.__balance_after = float(balance_after)
        self.__transaction_date = transaction_date if transaction_date else datetime.datetime.now()
        self.__description = description
    
    # Getters
    def get_transaction_id(self): return self.__transaction_id
    def get_account_number(self): return self.__account_number
    def get_transaction_type(self): return self.__transaction_type
    def get_amount(self): return self.__amount
    def get_balance_after(self): return self.__balance_after
    def get_transaction_date(self): return self.__transaction_date
    def get_description(self): return self.__description

    # Setters
    def set_transaction_type(self, t_type): self.__transaction_type = t_type.lower()
    def set_amount(self, amount): self.__amount = float(amount)
    def set_balance_after(self, bal): self.__balance_after = float(bal)
    def set_transaction_date(self, date): self.__transaction_date = date
    def set_description(self, desc): self.__description = desc

    def print_transaction_info(self):
        print(f"Transaction ID: {self.__transaction_id}")
        print(f"Account Number: {self.__account_number}")
        print(f"Type: {self.__transaction_type}")
        print(f"Amount: {self.__amount:.2f}")
        print(f"Balance After: {self.__balance_after:.2f}")
        print(f"Date: {self.__transaction_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Description: {self.__description}")
