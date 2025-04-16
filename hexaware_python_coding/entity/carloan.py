from entity import Loan

class CarLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, loan_status, car_model, car_value):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, 'CarLoan', loan_status)
        self.car_model = car_model
        self.car_value = car_value

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Car Model: {self.car_model}, Car Value: {self.car_value}"
