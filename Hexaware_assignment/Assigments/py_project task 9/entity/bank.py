from entity.Accounts import *
from entity.current_account import *
from entity.savings_account import *
class Bank:
    def __init__(self):
        self.account = None

    def create_account(self):
        print("\nChoose Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        acc_type = int(input("Enter your choice: "))

        acc_number = input("Enter Account Number: ")
        name = input("Enter Customer Name: ")
        balance = float(input("Enter Initial Balance: "))

        match acc_type:
            case 1:
                self.account = SavingsAccount(acc_number, name, balance)
            case 2:
                self.account = CurrentAccount(acc_number, name, balance)
            case _:
                print("Invalid choice.")

    def operate(self):
        if not self.account:
            print("Please create an account first.")
            return

        while True:
            print("\n---- Bank Menu ----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest")
            print("4. Show Account Info")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            match choice:
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
                    print("Thank you for banking with us.")
                    break
                case _:
                    print("Invalid option.")
