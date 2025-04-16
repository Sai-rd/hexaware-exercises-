from entity.Accounts import Account
from entity.Customer import Customer
from entity.transaction import Transaction
class Bank:
    def __init__(self, customer: Customer, account: Account):
        self.customer = customer
        self.account = account

    def perform_operations(self):
        print("\n--- Customer Information ---")
        self.customer.print_customer_info()
        print("\n--- Account Information ---")
        self.account.print_account_info()

        print("\n--- Performing Transactions ---")
        self.account.deposit(2000)
        self.account.withdraw(500)
        self.account.calculate_interest()

        print("\n--- Final Account Info ---")
        self.account.print_account_info()



if __name__ == "__main__":
    customer = Customer(1001, "Alice", "Johnson", "alice@example.com", "9876543210", "123 Main St")
    account = Account(20001, "Savings", 10000)
    bank = Bank(customer, account)
    bank.perform_operations()
    txn1 = Transaction(account_id="12345", transaction_type="Deposit", amount=1500)
    txn2 = Transaction(account_id="12345", transaction_type="Withdrawal", amount=500)

    txn1.print_transaction_info()
    print()
    txn2.print_transaction_info()
