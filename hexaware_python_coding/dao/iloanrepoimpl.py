import pyodbc
from entity.customer import Customer
from dao.iloanrepo import ILoanRepository
from entity.loan import Loan
from entity.homeloan import HomeLoan
from entity.carloan import CarLoan
from exception.invalidloanexception import InvalidLoanException
from decimal import Decimal
class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
    
    def get_connection(self):
        return pyodbc.connect(self.connection_string)
    
    def applyLoan(self, loan: Loan):
        conn = self.get_connection()
        cursor = conn.cursor()

        confirmation = input(f"Do you want to apply for a {loan.loan_type}? (Yes/No): ").strip().lower()
        if confirmation != 'yes':
            print("Loan application canceled.")
            return

        try:
            cursor.execute("""
                INSERT INTO Customer (customer_id, name, email, phone_number, address, credit_score)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (loan.customer.customer_id, loan.customer.name, loan.customer.email, loan.customer.phone_number,
                  loan.customer.address, loan.customer.credit_score))

            
            cursor.execute("""
                INSERT INTO Loan (loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (loan.loan_id, loan.customer.customer_id, loan.principal_amount, loan.interest_rate,
                  loan.loan_term, loan.loan_type, 'Pending'))

            
            if isinstance(loan, HomeLoan):
                cursor.execute("""
                    INSERT INTO HomeLoan (loan_id, property_address, property_value)
                    VALUES (?, ?, ?)
                """, (loan.loan_id, loan.property_address, loan.property_value))
            elif isinstance(loan, CarLoan):
                cursor.execute("""
                    INSERT INTO CarLoan (loan_id, car_model, car_value)
                    VALUES (?, ?, ?)
                """, (loan.loan_id, loan.car_model, loan.car_value))
            
            conn.commit()
            print(f"Loan with ID {loan.loan_id} has been successfully applied.")

        except Exception as e:
            
            print(f"Error applying loan: {e}")

    
    def calculateInterest(self, loanId: int):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Loan WHERE loan_id = ?', loanId)
            loan = cursor.fetchone()
            if not loan:
                raise InvalidLoanException("Loan not found!")
            interest = interest = (loan[2] * loan[3] * loan[4]) / 12

            return interest
        finally:
            conn.close()
    
    def calculateInterestWithParams(self, principal_amount: float, interest_rate: float, loan_term: int):
        return (principal_amount * interest_rate * loan_term) / 12
    

    def loanStatus(self, loanId: int):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Loan WHERE loan_id = ?', loanId)
            loan = cursor.fetchone()
            if not loan:
                raise InvalidLoanException("Loan not found!")

            cursor.execute('SELECT * FROM Customer WHERE customer_id = ?', loan[1])
            customer = cursor.fetchone()
            status = 'Approved' if customer[5] >= 650 else 'Rejected'

            cursor.execute('UPDATE Loan SET loan_status = ? WHERE loan_id = ?', status, loanId)
            conn.commit()
            print(f"Loan Status: {status}")
        finally:
            conn.close()
    
    def calculateEMI(self, loanId: int):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Loan WHERE loan_id = ?', loanId)
            loan = cursor.fetchone()
            if not loan:
                raise InvalidLoanException("Loan not found!")

            r = loan[3] / 100 / 12
            n = loan[4]
            emi = (loan[2] * r * (1 + r) ** n) / ((1 + r) ** n - 1)
            return emi
        finally:
            conn.close()
    
    def calculateEMIWithParams(self, principal_amount: float, interest_rate: float, loan_term: int):
        r = interest_rate / 100 / 12
        emi = (principal_amount * r * (1 + r) ** loan_term) / ((1 + r) ** loan_term - 1)
        return emi
    
    def loanRepayment(self, loanId: int, amount: float):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Loan WHERE loan_id = ?', loanId)
            loan = cursor.fetchone()
            if not loan:
                raise InvalidLoanException("Loan not found!")

            emi = self.calculateEMI(loanId)
            if amount < emi:
                print("Amount is less than a single EMI. Payment rejected.")
                return

            emi_count = int(Decimal(amount) // emi)
            print(f"Amount can pay {emi_count} EMIs.")
            cursor.execute('UPDATE Loan SET loan_status = ? WHERE loan_id = ?', 'Repaid', loanId)
            conn.commit()
        finally:
            conn.close()
    
    def getAllLoans(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Loan')
            loans = cursor.fetchall()
            for loan in loans:
                print(f"Loan ID: {loan[0]}, Status: {loan[6]}, Amount: {loan[2]}")
                if loan[5] == 'HomeLoan':
                    cursor.execute('SELECT * FROM HomeLoan WHERE loan_id = ?', loan[0])
                    home = cursor.fetchone()
                    print(f"  Property Address: {home[1]}, Value: {home[2]}")
                    print('______________________________________________________')
                elif loan[5] == 'CarLoan':
                    cursor.execute('SELECT * FROM CarLoan WHERE loan_id = ?', loan[0])
                    car = cursor.fetchone()
                    print(car)
                    print(f"Car Model: {car[1]}, Value: {car[2]}")
                    print("______________________________________________________")
        finally:
            conn.close()
    
    def getLoanById(self, loanId: int):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM Loan WHERE loan_id = ?', loanId)
            loan = cursor.fetchone()
            if not loan:
                raise InvalidLoanException("Loan not found!")

            print(f"Loan ID: {loan[0]}, Status: {loan[6]}, Amount: {loan[2]}")
            if loan[5] == 'HomeLoan':
                cursor.execute('SELECT * FROM HomeLoan WHERE loan_id = ?', loan[0])
                home = cursor.fetchone()
                print(f"  Property Address: {home[1]}, Value: {home[2]}")
                print('______________________________________________________')
            elif loan[5] == 'CarLoan':
                cursor.execute('SELECT * FROM CarLoan WHERE loan_id = ?', loan[0])
                car = cursor.fetchone()
                print(f"  Car Model: {car[1]}, Value: {car[2]}")
                print('______________________________________________________')
        finally:
            conn.close()
    
    

        
    
