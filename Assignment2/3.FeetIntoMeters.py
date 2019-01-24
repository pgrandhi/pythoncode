#Prompt the use to enter distance in feet
distanceInFeet = eval(input("Enter a value for feet:"))

ONE_FOOT = 0.305

#Comput meters = feet * 0.305 

distanceInMeters = distanceInFeet * ONE_FOOT

print(distanceInFeet, " feet is ", distanceInMeters, " meters")
