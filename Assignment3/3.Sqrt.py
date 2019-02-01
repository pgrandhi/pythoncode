number = eval(input("Enter the number you want to compute square root of:"))

DELTA = 0.000001

def sqrt(num):
    lastGuess = 1/4 * num
    nextGuess = (lastGuess + (num/lastGuess)) /2
    while ((nextGuess - lastGuess) >= DELTA):
        lastGuess = nextGuess
        nextGuess = (lastGuess + (num/lastGuess))/2        
    return nextGuess

print("Square Root of ", number, "is ", sqrt(number))
    
