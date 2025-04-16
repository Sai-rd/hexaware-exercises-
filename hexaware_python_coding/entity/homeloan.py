from entity import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, loan_status, property_address, property_value):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, 'HomeLoan', loan_status)
        self.property_address = property_address
        self.property_value = property_value
    
    def get_loan_id(self):
        return self.loan_id

    def set_loan_id(self, loan_id):
        self.loan_id = loan_id

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_principal_amount(self):
        return self.principal_amount

    def set_principal_amount(self, principal_amount):
        self.principal_amount = principal_amount

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_loan_term(self):
        return self.loan_term

    def set_loan_term(self, loan_term):
        self.loan_term = loan_term

    def get_loan_type(self):
        return self.loan_type

    def set_loan_type(self, loan_type):
        self.loan_type = loan_type

    def get_loan_status(self):
        return self.loan_status

    def set_loan_status(self, loan_status):
        self.loan_status = loan_status

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Property Address: {self.property_address}, Property Value: {self.property_value}"
