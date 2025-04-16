import datetime

class Transaction:
    transaction_counter = 1000

    def __init__(self, account_id, transaction_type, amount, transaction_date=None):
        self.__transaction_id = Transaction.transaction_counter
        Transaction.transaction_counter += 1

        self.__account_id = account_id 
        self.__transaction_type = transaction_type.lower()
        self.__amount = float(amount)
        self.__transaction_date = transaction_date if transaction_date else datetime.datetime.now()
    
    def get_transaction_id(self):
        return self.__transaction_id

    def get_account_id(self):
        return self.__account_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_transaction_date(self):
        return self.__transaction_date

    def set_transaction_type(self, t_type):
        self.__transaction_type = t_type.lower()

    def set_amount(self, amount):
        self.__amount = float(amount)

    def set_transaction_date(self, date):
        self.__transaction_date = date

    def print_transaction_info(self):
        print(f"Transaction ID: {self.__transaction_id}")
        print(f"Account ID: {self.__account_id}")
        print(f"Type: {self.__transaction_type}")
        print(f"Amount: ₹{self.__amount:.2f}")
        print(f"Date: {self.__transaction_date.strftime('%Y-%m-%d %H:%M:%S')}")
