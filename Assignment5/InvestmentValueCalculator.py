from tkinter import *

class InvestmentValueCalculator:
    def __init__(self):
        window = Tk()
        window.title("Investment-Value Calculator")

        Label(window, text="Investment Amount").grid(row=1,column=1,sticky=W)
        Label(window, text="Number of Years").grid(row=2,column=1,sticky=W)
        Label(window, text="Annual Interest Rate").grid(row=3,column=1,sticky=W)
        Label(window, text="Future Value").grid(row=4,column=1,sticky=W)
        
        #anything binding to controls should be a string. So all are stringVars
        self.investmentAmountVar = StringVar()
        Entry(window,textvariable=self.investmentAmountVar, justify=RIGHT).grid(row=1,column=2)

        self.numberOfYearsVar = StringVar()
        Entry(window,textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2,column=2)
        
        self.annualInterestRateVar = StringVar()
        Entry(window,textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=3,column=2)

        self.futureValueVar = StringVar()
        Label(window, textvariable=self.futureValueVar).grid(row=4,column=2,sticky=E)

        Button(window,text="Calculate",command=self.computeFutureValue).grid(row=5,column=2,sticky=E)

        window.mainloop()
        

    def computeFutureValue(self):        
        numberOfYears = int(self.numberOfYearsVar.get())
        investmentAmount = float(self.investmentAmountVar.get())
        monthlyInterestRate = float(self.annualInterestRateVar.get())/12
        monthlyInterestRate /= 100        
       
        futureValue = investmentAmount * ( 1 + monthlyInterestRate ) ** (numberOfYears * 12)
        self.futureValueVar.set(format(futureValue,"10.2f"))

    def futureValue(investmentAmount, monthlyInterestRate, numberOfMonths):
        '''
        The formula is as follows:
        F = investmentAmount x ( 1 + monthlyInterestRate ) ^ (number of months)        
        '''
        futureValue = investmentAmount * ( 1 + monthlyInterestRate ) ** numberOfMonths
        return futureValue
        
InvestmentValueCalculator()
        
