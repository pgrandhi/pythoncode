import random
from collections import namedtuple

rankArr = ["assistant", "associate", "full"]

def getRandomRank():
    return random.choice(rankArr)
    

def getRandomNumber(start, stop):
    return random.uniform(start,stop)
    
def getSalary(rank):
    if rank == "assistant":
        return getRandomNumber(50000.00, 80000.00)
    elif rank == "associate":
        return getRandomNumber(60000.00, 110000.00)
    elif rank == "full":
        return getRandomNumber(75000.00, 130000.00)

def generateLargeDataSet(filename):
    outfile = open(filename,"w")
    for i in range(1, 1001):       
        rank = getRandomRank()
        salary = round(getSalary(rank),2)
        outfile.write('FirstName{} LastName{} {} {}'.format(i, i, rank,salary))
        outfile.write("\n")        

filename = input("Enter a filename:")
generateLargeDataSet(filename)
