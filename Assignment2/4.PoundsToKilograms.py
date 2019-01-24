#Prompt the use to enter weight in pounds(lbs)
weightInPounds = eval(input("Enter a value in pounds:"))

ONE_POUND = 0.454

#Comput kg = pound * 0.454 

weightInKg = weightInPounds * ONE_POUND

print(weightInPounds, " pounds is ", weightInKg, " kilograms")
