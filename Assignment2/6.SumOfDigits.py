#Prompt the use to enter a number between 0 and 1000
number = int(input("Enter a number between 0 and 1000:"))

def sumOfDigits(number):
    sum = 0
    num = number
    while (num!=0):
       digit = num % 10
       sum = sum + digit
       num = num//10     
       
    print("The sum of digits is ", sum)

sumOfDigits(number)
    
