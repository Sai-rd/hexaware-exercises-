from entity.Customer import Customer
from dao.BankServiceProviderImpl import BankServiceProviderImpl

def main():
    bank = BankServiceProviderImpl("AI Bank", "Cyber City")

    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Get Balance\n6. Get Details\n7. List Accounts\n8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            cid = input("Customer ID: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            addr = input("Address: ")
            customer = Customer(cid, fname, lname, email, phone, addr)
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
            acc = bank.get_account_details(acc_no)
            print(acc if acc else "Account not found.")

        elif choice == "7":
            for acc in bank.list_accounts():
                print(acc)

        elif choice == "8":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
