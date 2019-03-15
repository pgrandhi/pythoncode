import random
from pathlib import Path

text = []
numbers = []
def getRandomNumber():
    rand = random.randint(1,100)
    return rand

def writeRandomNumbers(filename):
     outfile = open(filename,"w")
     for num in range(100):
         rand = getRandomNumber()
         outfile.write('{} '.format(rand))
     outfile.close()

def readFromFileAndSort(filename):
    infile = open(filename,"r")    
    filecontent = infile.read()
    numbers =[int(x) for x in filecontent.split()]
    numbers.sort()
    print(numbers)
    infile.close()

filename = input("Enter a filename:")
config = Path(filename)
if config.is_file():
    print("The file already exists")
else:
    writeRandomNumbers(filename)
    readFromFileAndSort(filename)
