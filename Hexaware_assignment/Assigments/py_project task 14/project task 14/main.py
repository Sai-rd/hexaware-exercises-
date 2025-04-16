from entity.Customer import Customer
from dao.BankServiceProviderImpl import BankServiceProviderImpl
from exception import *
from datetime import *
def main():
    bank = BankServiceProviderImpl("AI Bank", "Cyber City")

    while True:
        try:
            print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Get Balance\n6. Get Details\n7. List Accounts\n8. Get Transactions\n9. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                fname = input("First Name: ")
                lname = input("Last Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                addr = input("Address: ")
                customer = Customer( fname, lname, email, phone, addr)
                acc_type = input("Account Type (Savings/Current/ZeroBalance): ")
                balance = float(input("Initial Balance: ")) if acc_type.lower() != "zerobalance" else 0
                acc = bank.create_account(customer, acc_type, balance)
                if acc:
                    print("Account created:", acc.account_number)
                else:
                    print("Invalid account type.")

            elif choice == "2":
                acc_no = int(input("Account Number: "))
                amt = float(input("Amount: "))
                print("Balance:", bank.deposit(acc_no, amt))

            elif choice == "3":
                acc_no = int(input("Account Number: "))
                amt = float(input("Amount: "))
                print("Balance:", bank.withdraw(acc_no, amt))

            elif choice == "4":
                from_acc = int(input("From Account Number: "))
                to_acc = int(input("To Account Number: "))
                amt = float(input("Amount: "))
                if bank.transfer(from_acc, to_acc, amt):
                    print("Transfer Successful.")
                else:
                    print("Transfer Failed.")

            elif choice == "5":
                acc_no = int(input("Account Number: "))
                print("Balance:", bank.get_account_balance(acc_no))

            elif choice == "6":
                acc_no = int(input("Account Number: "))
                account_details = bank.getAccountDetails(acc_no)
                if account_details:
                    print("\nAccount and Customer Details:")
                    print(f"Account Number: {account_details['account_details']['account_number']}")
                    print(f"Account Type: {account_details['account_details']['account_type']}")
                    print(f"Balance: ₹{account_details['account_details']['balance']:.2f}")
                    print("Customer Details:")
                    customer = account_details['customer_details']
                    print(f"Customer ID: {customer['customer_id']}")
                    print(f"Name: {customer['first_name']} {customer['last_name']}")
                    print(f"Email: {customer['email']}")
                    print(f"Phone: {customer['phone']}")
                    print(f"Address: {customer['address']}")
                else:
                    print("Account not found.")


            elif choice == "7":
                for acc in bank.list_accounts():
                    print(acc)
            elif choice == "8":
                try:
                    acc_no = int(input("Enter Account Number: "))
                    from_date_str = input("Enter From Date (YYYY-MM-DD): ")
                    to_date_str = input("Enter To Date (YYYY-MM-DD): ")
                    
                    from_date = datetime.strptime(from_date_str, "%Y-%m-%d").date()
                    to_date = datetime.strptime(to_date_str, "%Y-%m-%d").date()

                    transactions = bank.get_transactions(acc_no, from_date, to_date)
                    if not transactions:
                        print("No transactions found in this date range.")
                    else:
                        print(f"\nTransactions for Account {acc_no} from {from_date} to {to_date}:")
                        for tx in transactions:
                            tx.print_transaction_info()
                            print("-" * 30)
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            elif choice == "9":
                break

            else:
                raise nullPointerException("Invalid choice.")
        except nullPointerException as e:
            print(e)

if __name__ == "__main__":
    main()
