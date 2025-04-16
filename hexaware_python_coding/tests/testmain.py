import unittest
from unittest.mock import MagicMock
from dao import ILoanRepositoryImpl
from entity import Loan,Customer,CarLoan,HomeLoan

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.dao=ILoanRepositoryImpl("Dummy String")
    
    #Test case 1: Adding a house Loan
    def test_add_home_loan(self):
        
        customer = Customer(1, "Alice", "alice@example.com", "1234567890", "Green Street", 750)
        home_loan = HomeLoan(
            loan_id=101,
            customer=customer,
            principal_amount=500000,
            interest_rate=7.5,
            loan_term=20,
            loan_status="Pending",
            property_address="123 Maple Street",
            property_value=600000
        )

       
        self.dao.applyLoan = MagicMock(return_value=True)

        result = self.dao.applyLoan(home_loan)
        self.assertTrue(result)
    
    #Test Case 2: Adding A Car Loan
    def test_add_car_loan(self):
        customer = Customer(2, "Bob", "bob@example.com", "9876543210", "Blue Avenue", 700)
        car_loan = CarLoan(
            loan_id=102,
            customer=customer,
            principal_amount=300000,
            interest_rate=8.0,
            loan_term=5,
            loan_status="Pending",
            car_model="Toyota Corolla",
            car_value=350000
        )
        self.dao.applyLoan = MagicMock(return_value=True)
        result = self.dao.applyLoan(car_loan)
        self.assertTrue(result)
    
    #Test Case 3:Calculating Intrest
    def test_calculate_interest_with_params(self):
        principal_amount = 100000
        interest_rate = 10  
        loan_term = 12  
        expected_interest = (principal_amount * interest_rate * loan_term) / 12
        self.dao.calculateInterestWithParams = MagicMock(return_value=expected_interest)
        result = self.dao.calculateInterestWithParams(principal_amount, interest_rate, loan_term)
        self.assertEqual(result, expected_interest)
    
    #Test Case 4:Calculating EMI
    def test_calculate_emi_with_params(self):
        principal_amount = 100000  
        interest_rate = 12  
        loan_term = 12 
        r = interest_rate / 100 / 12
        n = loan_term
        expected_emi = (principal_amount * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        actual_emi = self.dao.calculateEMIWithParams(principal_amount, interest_rate, loan_term)
        self.assertAlmostEqual(actual_emi, expected_emi, places=2)

if __name__ == "__main__":
    unittest.main()
 
