filename = input("Enter a file name:")
wordToReplace = input("Enter the string to be removed:")
inFile = open(filename,"r")
text = inFile.read()
text = text.replace(wordToReplace,"")

outFile = open(filename,"w+")
outFile.write(text)
    
inFile.close()
outFile.close()
