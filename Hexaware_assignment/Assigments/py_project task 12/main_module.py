from entity.customer import Customer
from service.impl import BankServiceProviderImpl
from exception.custom_exception import *

def main():
    bank = BankServiceProviderImpl("HexaBank", "Main Street")
    while True:
        try:
            print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Get Balance\n5. Transfer\n6. Get Account Details\n7. List Accounts\n8. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                cid = input("Enter Customer ID: ")
                fname = input("First Name: ")
                lname = input("Last Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                address = input("Address: ")
                cust = Customer(cid, fname, lname, email, phone, address)
                acc_type = input("Enter Account Type (Savings/Current/ZeroBalance): ")
                balance = float(input("Initial Balance: ")) if acc_type != 'ZeroBalance' else 0
                acc_no = bank.create_account(cust, acc_type, balance)
                print(f"Account created successfully. Account Number: {acc_no}")
            elif choice == '2':
                acc_no = int(input("Account Number: "))
                amt = float(input("Amount: "))
                print(f"New Balance: {bank.deposit(acc_no, amt)}")
            elif choice == '3':
                acc_no = int(input("Account Number: "))
                amt = float(input("Amount: "))
                print(f"New Balance: {bank.withdraw(acc_no, amt)}")
            elif choice == '4':
                acc_no = int(input("Account Number: "))
                print(f"Balance: {bank.get_account_balance(acc_no)}")
            elif choice == '5':
                from_acc = int(input("From Account: "))
                to_acc = int(input("To Account: "))
                amt = float(input("Amount: "))
                bank.transfer(from_acc, to_acc, amt)
                print("Transfer successful")
            elif choice == '6':
                acc_no = int(input("Account Number: "))
                print(bank.get_account_details(acc_no))
            elif choice == '7':
                for acc in bank.list_accounts():
                    print(acc)
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice")
        except (InvalidAccountException, InsufficientFundException, OverDraftLimitExceededException, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == '__main__':
    main()
