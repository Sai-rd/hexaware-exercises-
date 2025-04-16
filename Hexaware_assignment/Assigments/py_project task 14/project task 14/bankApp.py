from dao.BankRepositoryImpl import BankRepositoryImpl
from entity.Customer import Customer
from datetime import datetime

class BankApp:
    
    def __init__(self):
        self.bank_repo = BankRepositoryImpl()

    def main(self):
        while True:
            print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Get Balance\n6. Get Details\n7. List Accounts\n8. Get Transactions\n9. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                acc_no = int(input("Account Number: "))
                amt = float(input("Amount: "))
                print(f"Balance after deposit: {self.bank_repo.deposit(acc_no, amt)}")

            elif choice == "3":
                acc_no = int(input("Account Number: "))
                amt = float(input("Amount: "))
                print(f"Balance after withdrawal: {self.bank_repo.withdraw(acc_no, amt)}")

            elif choice == "4":
                from_acc = int(input("From Account Number: "))
                to_acc = int(input("To Account Number: "))
                amt = float(input("Amount: "))
                self.bank_repo.transfer(from_acc, to_acc, amt)
                print("Transfer successful.")

            elif choice == "5":
                acc_no = int(input("Account Number: "))
                print(f"Balance: {self.bank_repo.get_account_balance(acc_no)}")

            elif choice == "6":
                acc_no = int(input("Account Number: "))
                details = self.bank_repo.get_account_details(acc_no)
                if(details):
                    for x in details:
                        print(x,":",details[x])
                else:
                    print("Account Not Found")

            elif choice == "7":
                accounts = self.bank_repo.list_accounts()
                for acc in accounts:
                    print(acc)

            elif choice == "8":
                acc_no = int(input("Account Number: "))
                from_date = input("From Date (YYYY-MM-DD): ")
                to_date = input("To Date (YYYY-MM-DD): ")
                transactions = self.bank_repo.get_transactions(acc_no, from_date, to_date)
                for tx in transactions:
                    tx.print_transaction_info()

            elif choice == "9":
                break

            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        acc_type = input("Account Type (Savings/Current/ZeroBalance): ")
        if acc_type.lower() not in ["savings", "current", "zerobalance"]:
            print("Invalid account type.")
            return
        fname = input("First Name: ")
        lname = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        addr = input("Address: ")

        customer = Customer( None,fname, lname, email, phone, addr)
        balance = float(input("Initial Balance: ")) if acc_type.lower() != "zerobalance" else 0
        self.bank_repo.create_account(customer, acc_type, balance)
        print(f"Account created successfully.")

if __name__ == "__main__":
    app = BankApp()
    app.main()
