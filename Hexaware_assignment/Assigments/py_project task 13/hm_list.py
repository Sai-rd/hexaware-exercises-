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
        self.accounts = []

    def create_account(self, customer, acc_no, acc_type, balance):
        account = Account(acc_no, acc_type, balance, customer)
        self.accounts.append(account)

    def list_accounts(self):
        return self.accounts


# Example usage:
bank = HMBank()

customer1 = Customer(1, 'John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm Street')
customer2 = Customer(2, 'Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak Street')

bank.create_account(customer1, 1001, 'Savings', 1000)
bank.create_account(customer2, 1002, 'Current', 500)

accounts = bank.list_accounts()
for account in accounts:
    print(account)
