totalNumber = 100

def getPentagonalNumber(n):
    return round(n*(3*n -1)/2)

def PrintPentagonalNumbers(numToPrint):
    num = 1
    while (num < numToPrint):
        col = 0 
        while(col <10):
            pentagonalNumber = getPentagonalNumber(num+col)
            print(format(pentagonalNumber,"6d"),end='')
            col += 1
        print()
        num += col    


PrintPentagonalNumbers(100)
