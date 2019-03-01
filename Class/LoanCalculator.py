from tkinter import *
#tkinter library provides capability to create UI controls

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")

        Label(window, text="Annual Interest Rate").grid(row=1,column=1,sticky=W)
        Label(window, text="Number of Years").grid(row=2,column=1,sticky=W)
        Label(window, text="Loan Amount").grid(row=3,column=1,sticky=W)
        Label(window, text="Monthly Payment").grid(row=4,column=1,sticky=W)
        Label(window, text="Total Payment").grid(row=5,column=1,sticky=W)

        #anything binding to controls should be a string. So all are stringVars
        self.annualInterestRateVar = StringVar()
        Entry(window,textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1,column=2)

        self.numberOfYearsVar = StringVar()
        Entry(window,textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2,column=2)
        
        self.loanAmountVar = StringVar()
        Entry(window,textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3,column=2)

        self.monthlyPaymentVar = StringVar()
        Label(window, textvariable=self.monthlyPaymentVar).grid(row=4,column=2,sticky=E)

        self.totalPaymentVar = StringVar()
        Label(window, textvariable=self.totalPaymentVar).grid(row=5,column=2,sticky = E)

        Button(window,text="Compute Payment",command=self.computePayment).grid(row=6,column=2,sticky=E)

        window.mainloop()
        

    def computePayment(self):
        numberOfYears = int(self.numberOfYearsVar.get())
        monthlyInterestRate = float(self.annualInterestRateVar.get())/12
        monthlyInterestRate /= 100
        monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),
                                                monthlyInterestRate,
                                                numberOfYears)
        
        totalPayment = monthlyPayment * 12 * numberOfYears
        self.monthlyPaymentVar.set(format(monthlyPayment,"10.2f"))
        self.totalPaymentVar.set(format(totalPayment,"10.2f"))
            
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1/((1+ monthlyInterestRate) ** (numberOfYears * 12)))
        return monthlyPayment
        
LoanCalculator()
        
