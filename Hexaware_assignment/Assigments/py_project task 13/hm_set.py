from typing import Set
from functools import cmp_to_key
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
class Account:
    def __init__(self, acc_no, acc_type, balance, customer=None):
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
        self.customer = customer

    def __repr__(self):
        return f"Account({self.acc_no}, {self.acc_type}, {self.balance}, {self.customer})"

    

class HMBank:
    def __init__(self):
        
        self.accounts: Set[Account] = set()

    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float):
       
        account = Account(acc_no, acc_type, balance, customer)
        self.accounts.add(account)

    def list_accounts(self):
       
        account_list = list(self.accounts)
        
        account_list.sort(key=cmp_to_key(self.compare_by_name))
        return account_list

    def compare_by_name(self, acc1: Account, acc2: Account):
       
        name1 = (acc1.customer.first_name + acc1.customer.last_name).lower()
        name2 = (acc2.customer.first_name + acc2.customer.last_name).lower()
        if name1 < name2:
            return -1 
        elif name1 > name2:
            return 1  
        else:
            return 0  




bank = HMBank()
customer1 = Customer(1, 'John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm Street')
customer2 = Customer(2, 'Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak Street')

bank.create_account(customer1, 1001, 'Savings', 1000)
bank.create_account(customer2, 1002, 'Current', 500)

accounts = bank.list_accounts()
for account in accounts:
    print(account)
