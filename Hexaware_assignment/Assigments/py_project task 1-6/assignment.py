'''Task 1'''
credit=int(input("Enter the credit score : "))
annual=int(input("Enter the annual income : "))
if(credit>700 and annual>=50000):
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

'''Task 2'''
def atm():
    bal=float(input("Enter Balance Amt : "))
    while True:
        print("1.Check Balance")
        print("2.Withdraw")
        print("3.Deposit")
        print("4.Exit")
        ch=int(input("Enter your choice : "))
        if ch==1:
            print(f"Your Current Balance is {bal} rs")
        elif ch==2:
            amt=int(input("Enter the amount you want to withdraw : "))
            if(amt<0):
                print("Enter a valid amount to withdraw : ")
            elif(amt%100!=0):
                print("Enter amt in multiples of 100 and 500 ")
            elif(amt>bal):
                print("Insufficient balance ")
            else:
                bal-=amt 
                print(f"Withdrawal successfull new balance is {bal}")
        elif ch==3:
            dep=int(input("Enter the amount to be deposited : "))
            if dep<0:
                print("Enter a valid amount : ")
            else:
                bal+=dep 
                print(f"{dep} rs deposited the new balance is {bal}")
        elif ch==4:
            break
        else:
            print("Enter a valid choice input")

atm()

'''Task 3'''
n = int(input("Enter the number of customers: "))

for i in range(n):
    print(f"\nFor Customer {i + 1}:")
    
    ib = float(input("Enter the initial balance: "))
    air = float(input("Enter the annual interest rate (%): "))
    ny = int(input("Enter the number of years: "))
    
    fb = ib * ((1 + air / 100) ** ny)
    
    print(f"The future balance of customer {i + 1} is ₹{fb:.2f}")

'''Task 4'''

accounts = {
    "1001": 25000.50,
    "1002": 15000.00,
    "1003": 3400.75,
    "1004": 78000.20,
    "1005": 500.00
}

print("Welcome to the Bank Balance Checker")

while True:
    account = input("Enter your account number (or type 'exit' to quit): ")

    if account.lower() == 'exit':
        print("Thank you for using the service. Goodbye!")
        break

    if account in accounts:
        print(f" Account found. Your current balance is ₹{accounts[acc_no]:.2f}")
        break
    else:
        print(" Invalid account number. Please try again.")


'''Task 5'''
def password_validation(password):
    length = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    
    if length and uppercase and digit:
        print("Password is valid.")
    else:
        print("Password is invalid.")
        if not length:
            print("- Password must be at least 8 characters long.")
        if not uppercase:
            print("- Password must contain at least one uppercase letter.")
        if not digit:
            print("- Password must contain at least one digit.")

password_validation("12345hhbc")

'''Task 6'''
def transaction_tracker():
    transactions = []
    print("Welcome to Your Bank Transaction Tracker!")

    while True:
        print("\nChoose a transaction:")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Display transaction")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            transactions.append(("Deposit", amount))
            print(f"{amount} deposited successfully.")

        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            transactions.append(("Withdrawal", amount))
            print(f"{amount} withdrawn successfully.")

        elif choice=='3':
            for x in transactions:
                print(x)
            print("")
        elif choice == '4':
            print("\n Exiting... Here is your transaction history:")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\n Transaction History:")
    if not transactions:
        print("No transactions made.")
    else:
        for i, (t_type, amt) in enumerate(transactions, start=1):
            print(f"{i}. {t_type} - {amt}")

transaction_tracker()
 


