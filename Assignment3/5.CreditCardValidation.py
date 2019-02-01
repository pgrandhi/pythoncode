creditNumber = input("Please enter the credit card Number")
                      
def checkLength(num):
    length = len(num)
    if length < 13 or length > 16:
        return False
    if num[0] == "4" or num[0]=="5" or num[0]=="6" or (num[0]=="3" and num[1]=="7"):
            return True
    else:
        return False

def getDigit(num):
    length = len(num)
    if(length == 1):
        return eval(num)
    else:
        return eval(num[0]) + eval(num[1])
    
    
def sumOfOddPlace(num):
    length = len(num)
    sum = 0
    for i in range(0, length):
        if (i%2 != 0):
            sum += eval(num[i])
    print("Odd number sum:",sum)
    return sum

def sumOfDoubleEvenPlace(num):
    length = len(num)
    sum = 0
    for i in range(0, length):
        if (i%2 == 0):
            doubleNum = eval(num[i])*2            
            sum += getDigit(str(doubleNum))
    print("Even number doubled sum:",sum)
    return sum

def isValid(num):
    if checkLength(num)== False:
        return False
    TotalSum = sumOfOddPlace(num) + sumOfDoubleEvenPlace(num)
    if TotalSum % 10 == 0:
        return True
    
    return False

print("Credit card number",creditNumber, "is valid:", isValid(creditNumber))

    
    

        
        
    
