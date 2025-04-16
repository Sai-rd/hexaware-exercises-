from .Accounts import *
from .Customer import Customer
from .transaction import Transaction
class Bank:
    def __init__(self):
        self.account = None

    def create_account(self):
        print("Choose Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        choice = int(input("Enter your choice (1 or 2): "))

        acc_number = input("Enter Account Number: ")
        balance = float(input("Enter Initial Balance: "))

        match choice:
            case 1:
                self.account = SavingsAccount(acc_number, balance)
            case 2:
                self.account = CurrentAccount(acc_number, balance)
            case _:
                print("Invalid choice. Account not created.")

    def operate(self):
        if not self.account:
            print("No account found. Please create one first.")
            return

        while True:
            print("\n--- Bank Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest")
            print("4. Show Account Info")
            print("5. Exit")
            option = int(input("Enter your choice: "))

            match option:
                case 1:
                    amount = float(input("Enter amount to deposit: "))
                    self.account.deposit(amount)
                case 2:
                    amount = float(input("Enter amount to withdraw: "))
                    self.account.withdraw(amount)
                case 3:
                    self.account.calculate_interest()
                case 4:
                    self.account.print_account_info()
                case 5:
                    print("Thank you for using the bank system.")
                    break
                case _:
                    print("Invalid option.")
