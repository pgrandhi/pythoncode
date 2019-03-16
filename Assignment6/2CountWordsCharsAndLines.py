filename = input("Enter a file name:")
inFile = open(filename,"r")
numLines = 0
numWords = 0
numChars = 0

for line in inFile:
    numLines +=1
    wordList = line.split()
    numWords += len(wordList)
    numChars += len(line)

print (numChars, "chars")
print (numWords, "words")
print (numLines, "lines")
