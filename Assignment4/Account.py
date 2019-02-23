import datetime
class Account:
    def __init__(self, accountId = 0, balance=100, annualInterestRate=0):        
        self.__id = accountId
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id
    
    def setId(self, accountId):
        self.__id = accountId

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getBalance(self):
        return self.__balance
     
    def setBalance(self, balance):
        self.__balance = balance

    def getMonthlyInterestRate(self):
        '''
        returns monthly interest rate = annual interest rate /12
        '''
        return (self.__annualInterestRate/12)

    def getMonthlyInterest(self):
        '''
        returns monthly interest = monthy interest rate * balance
        '''
        return (self.getMonthlyInterestRate()/100) * self.__balance

    def withdraw(self, amount):
        self.__balance -=amount

    def deposit(self, amount):
        self.__balance +=amount

    
        
       
        
        
