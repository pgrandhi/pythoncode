#Prompt the use to enter the input to calculate energy
weightInKgs = eval(input("Enter the amount of water in kilograms:"))
initialTemp = eval(input("Enter the initial temperature:"))
finalTemp = eval(input("Enter the final temperature:"))

#constants
ENERGY_CONST = 4184

def calculateEnergy(weightInKgs, initialTemp, finalTemp):
    energy = weightInKgs * (finalTemp - initialTemp)* ENERGY_CONST
    print("The energey needed is",energy)

calculateEnergy(weightInKgs,initialTemp,finalTemp)
    
