#Save this test file in the same folder as where the class is defined to import the class
#You have to specify from <file> import <class>.
#Names are case-sensitive and it needs to match the filename and class name
#You can also do from Note import *

from Notebook import Notebook

nb1 = Notebook()
nb1.new_note("first note in notebook", "tag")
nb1.new_note("second note in notebook", "second")
nb1.new_note("third note in notebook", "third")
nb1.print_note(1)
nb1.print_note(2)
nb1.print_note(3)

nb1.modify_note(2,"modified")
nb1.print_note(1)
nb1.print_note(2)
nb1.print_note(3)

nb1.modify_note(4,"modified note where id does not exist")

nb1.match_note("tag")
nb1.match_note("note")
