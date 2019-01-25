numberOfStars = eval(input("How many stars:"))

def printSameStarsEachRow(numberOfStars):
    currentCount = 0
    currentRow = 0
    while currentRow < numberOfStars:
        currentCount = 0
        while currentCount < numberOfStars:
            print("* ", end=' ')
            currentCount += 1
        print()
        currentRow += 1

def printOneLessStarEachRow(numberOfStars):
    totalStars = numberOfStars
    currentRow = 0
    while currentRow < numberOfStars:
        currentCount = totalStars
        while currentCount > 0:
            print("* ", end=' ')
            currentCount -= 1
        print()
        currentRow += 1
        totalStars -=1

def ForLoop_PrintOneLessStarEachRow(numberOfStars):
    for row in range(numberOfStars):
        for col in range(numberOfStars):
            print("* ", end=' ')
        print()
        numberOfStars -= 1
        
printSameStarsEachRow(numberOfStars)
print()
printOneLessStarEachRow(numberOfStars)
print()
ForLoop_PrintOneLessStarEachRow(numberOfStars)
