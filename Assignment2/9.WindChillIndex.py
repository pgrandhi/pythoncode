#Prompt the use to enter the input to calculate energy
temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
windSpeed = eval(input("Enter the wind speed in miles per hour:"))

#constants
TEMP_CONST = 35.74

def calculateWindChillIndex(temp, windSpeed):
    windchill = TEMP_CONST + (0.6215 * temp) - 35.75*(windSpeed ** 0.16) +0.4275 * temp * (windSpeed ** 0.16)
    print("The wind chill index is",round(windchill,5))

calculateWindChillIndex(temperature,windSpeed)
    
