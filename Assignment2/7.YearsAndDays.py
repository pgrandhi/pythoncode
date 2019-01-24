#Prompt the use to enter the minutes
minutes = eval(input("Enter the number of minutes:"))

#constants
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_YEAR = 365

def numberOfYearsAndDays(minutes):
    minutesInADay = MINUTES_IN_HOUR * HOURS_IN_DAY
    daysInGivenMinutes = minutes/minutesInADay
    yearsInGivenMinutes = round(daysInGivenMinutes//DAYS_IN_YEAR)
    remainingDays = round(daysInGivenMinutes % DAYS_IN_YEAR)
    print(minutes, "minutes is approximately", yearsInGivenMinutes, "years and", remainingDays,"days ")

numberOfYearsAndDays(minutes)
    
