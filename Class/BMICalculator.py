#Prompt the user for weight in lbs
weight = eval(input("Enter weight in pounds:"))

#Prompt the user for height in in
height = eval(input("Enter height in inches:"))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weightInKg = KILOGRAMS_PER_POUND * weight
heightInMeters = METERS_PER_INCH * height

#Compute BMI = WgightInKg/(heightInMeters squared)
bmi = weightInKg /(heightInMeters ** 2)

print("BMI is: ", bmi)

if(bmi <18.5):
    print("Under-weight")
elif (bmi <25):
     print("Normal weight")
elif (bmi <30):
    print("Over-weight")
else:
    print("Obese")
     
