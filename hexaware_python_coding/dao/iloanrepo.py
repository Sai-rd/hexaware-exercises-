from entity.loan import Loan
from entity.homeloan import HomeLoan
from entity.carloan import CarLoan
from exception.invalidloanexception import InvalidLoanException

from abc import ABC, abstractmethod

class ILoanRepository(ABC):
    
    @abstractmethod
    def applyLoan(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass

    @abstractmethod
    def calculateInterestWithParams(self):
        pass

    @abstractmethod
    def loanStatus(self):
        pass

    @abstractmethod
    def calculateEMI(self):
        pass

    @abstractmethod
    def calculateEMIWithParams(self):
        pass

    @abstractmethod
    def loanRepayment(self):
        pass

    @abstractmethod
    def getAllLoans(self):
        pass

    @abstractmethod
    def getLoanById(self):
        pass

    
