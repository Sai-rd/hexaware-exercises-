from entity.bank import *
from entity.Accounts import *
from entity.Customer import *
from entity.transaction import *
def main():
    bank = Bank()

    while True:
        print("\n=== Bank Menu ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                cid = input("Enter Customer ID: ")
                fname = input("Enter First Name: ")
                lname = input("Enter Last Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone (10 digits): ")
                address = input("Enter Address: ")

                customer = Customer(cid, fname, lname, "", "", address)
                customer.set_email(email)
                customer.set_phone(phone)

                print("Account Types: Savings / Current")
                acc_type = input("Enter Account Type: ")
                balance = float(input("Enter Initial Balance: "))
                bank.create_account(customer, acc_type, balance)

            elif choice == "2":
                acc_no = int(input("Enter Account Number: "))
                amount = float(input("Enter Amount to Deposit: "))
                bal = bank.deposit(acc_no, amount)
                print(f"Updated Balance: ₹{bal:.2f}")

            elif choice == "3":
                acc_no = int(input("Enter Account Number: "))
                amount = float(input("Enter Amount to Withdraw: "))
                bal = bank.withdraw(acc_no, amount)
                print(f"Updated Balance: ₹{bal:.2f}")

            elif choice == "4":
                acc_no = int(input("Enter Account Number: "))
                bal = bank.get_account_balance(acc_no)
                print(f"Current Balance: ₹{bal:.2f}")

            elif choice == "5":
                from_acc = int(input("From Account Number: "))
                to_acc = int(input("To Account Number: "))
                amount = float(input("Enter Amount to Transfer: "))
                bank.transfer(from_acc, to_acc, amount)
                print("Transfer successful.")

            elif choice == "6":
                acc_no = int(input("Enter Account Number: "))
                bank.get_account_details(acc_no)

            elif choice == "7":
                print("Exiting... Thank you!")
                break

            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
