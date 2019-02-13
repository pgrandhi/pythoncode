from Account import Account 

account1 = Account(1122, 20000, 4.5)
print("Account created")
print("Id:",account1.getId(), "Balance:", account1.getBalance(), "Monthly Interest rate: ",account1.getMonthlyInterestRate(),"  Monthly Interest:",account1.getMonthlyInterest())
account1.withdraw(2500)
account1.deposit(3000)
print ("Account balance after withdrawing $2500 and depositing $3000")
print("Id:",account1.getId(), "Balance:",account1.getBalance(), "Monthly Interest rate: ",account1.getMonthlyInterestRate(),"  Monthly Interest:",account1.getMonthlyInterest())
