#Save this test file in the same folder as where the class is defined to import the class
#You have to specify from <file> import <class>.
#Names are case-sensitive and it needs to match the filename and class name
#You can also do from Note import *
import sys
from Notebook import Notebook,Note

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        #dictionary - also called object in python and JS
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
            }
        
    def displayMenu(self):
        #to indent in the same way as type here, use """
        print("""
           Notebook Menu

            1. Show all notes
            2. Search notes
            3. Add note
            4. Modify note
            5. Quit
            """)

    def run(self):
        #run forever
        while True:
            self.displayMenu()
            choice = input("Enter an option:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("Thank you for using the notebook.")
        sys.exit(0)

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.getNotes()
        for note in notes:
            self.notebook.print_note(note.getId())

    def search_notes(self):
        filter = input("search for:")
        notes = self.notebook.search(filter)
        show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo:")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        noteId = int(input("Enter the note ID"))
        memo = input("Enter a memo:")
        tags = input("Enter tags:")
        if memo:
            self.notebook.modify_memo(noteId,memo)
        if tags:
          self.notebook.modify_tags(noteId,tags)

menu = Menu()
menu.run()
          
    

    
