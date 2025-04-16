class InvalidLoanException(Exception):
    def __init__(self, message="Invalid Loan operation!"):
        super().__init__(message)
