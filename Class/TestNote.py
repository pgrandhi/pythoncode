#Save this test file in the same folder as where the class is defined to import the class
#You have to specify from <file> import <class>.
#Names are case-sensitive and it needs to match the filename and class name
#You can also do from Note import *

from Note import Note

n1 = Note("This is my first note")
n2 = Note("This is my second note", "second")

print("n1.id:",n1.id," n1.memo:",n1.memo," n1.tags:",n1.tags," n1.creationDate:",n1.creationDate)
print("n2.id:",n2.id," n2.memo:",n2.memo," n2.tags:",n2.tags," n2.creationDate:",n2.creationDate)
