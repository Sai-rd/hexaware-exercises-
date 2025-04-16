from dao import ILoanRepositoryImpl
from entity.loan import Loan
from entity.homeloan import HomeLoan
from entity.carloan import CarLoan
from entity.customer import Customer
from util.dbproperty import PropertyUtil
from exception import InvalidLoanException
import pyodbc

class main:
    def __init__(self):
        connection_string=PropertyUtil.getpropertystring()
        self.dao=ILoanRepositoryImpl(connection_string)
        self.main_menu()
        
    
    def main_menu(self):
        while True:

            print("\n----- Loan Management System -----")
            print("1. Apply for a House Loan")
            print("2. Apply for a Car Loan ")
            print("3. View All Loans")
            print("4. View Loan By ID")
            print("5. Calculate Loan Interest")
            print("6. Calculate Loan EMI")
            print("7. Make Loan Repayment")
            print("8. Check Loan Status")
            print("9.Exit")
            choice=input("Enter Choice :")
            if choice == '1':
                self.apply_home_loan()
            elif choice == '2':
                self.apply_car_loan()
            elif choice == '3':
                self.view_all_loans()
            elif choice == '4':
                self.view_loan_by_id()
            elif choice == '5':
                self.calculate_loan_interest()
            elif choice == '6':
                self.calculate_loan_emi()
            elif choice == '7':
                self.make_loan_repayment()
            elif choice=='8':
                self.check_loan_status()
            elif choice=="9":
                print("Exiting the System")
                break  
            else:
                print("Invalid choice! Please select a valid option (1-10).")
    
    def apply_home_loan(self):
        customer_id = int(input("Enter customer ID: "))
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone_number = input("Enter customer phone number: ")
        address = input("Enter customer address: ")
        credit_score = int(input("Enter customer credit score: "))
        principal_amount = float(input("Enter loan principal amount: "))
        interest_rate = float(input("Enter interest rate (in %): "))
        loan_term = int(input("Enter loan term (in years): "))
        property_address = input("Enter property address: ")
        property_value = float(input("Enter property value: "))
        loanid=int(input("Enter LoanId : "))
        loan_status="Pending"

        customer = Customer(customer_id, name, email, phone_number, address, credit_score)
        loan = HomeLoan(loanid,customer, principal_amount, interest_rate, loan_term,loan_status, property_address, property_value)
        self.dao.applyLoan(loan)
    
    def apply_car_loan(self):
        customer_id = int(input("Enter customer ID: "))
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone_number = input("Enter customer phone number: ")
        address = input("Enter customer address: ")
        credit_score = int(input("Enter customer credit score: "))
        principal_amount = float(input("Enter loan principal amount: "))
        interest_rate = float(input("Enter interest rate (in %): "))
        loan_term = int(input("Enter loan term (in years): "))
        car_model = input("Enter car model: ")
        car_value = float(input("Enter car value: "))
        loanid=int(input("Enter the loan ID : "))
        loanstatus="Pending"
        customer = Customer(customer_id, name, email, phone_number, address, credit_score)
        loan = CarLoan(loanid,customer, principal_amount, interest_rate, loan_term,loanstatus, car_model, car_value)
        self.dao.applyLoan(loan)

    def view_all_loans(self):
        print("\n----- View All Loans -----")
        self.dao.getAllLoans()
    
    def view_loan_by_id(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            self.dao.getLoanById(loan_id)
        except InvalidLoanException as e:
            print(f"Error: {e}")
    
    def calculate_loan_interest(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            interest = self.dao.calculateInterest(loan_id)
            print(f"Loan Interest: {interest}")
        except InvalidLoanException as e:
            print(f"Error: {e}")

    def calculate_loan_emi(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            emi = self.dao.calculateEMI(loan_id)
            print(f"Loan EMI: {emi}")
        except InvalidLoanException as e:
            print(f"Error: {e}")
    
    def make_loan_repayment(self):
        loan_id = int(input("Enter Loan ID: "))
        amount = float(input("Enter Amount to Repay: "))
        try:
            self.dao.loanRepayment(loan_id, amount)
        except InvalidLoanException as e:
            print(f"Error: {e}")
    
    def check_loan_status(self):
        loanid=int(input("Enter Loan ID : "))
        self.dao.loanStatus(loanid)
    
    

    
    

if __name__=="__main__":
    main()




    

        
        