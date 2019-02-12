#from <file> import <classname> or import *
from Note import Note

class Notebook:
    '''
    Represents a collection of Notes
    that can be modified or tagged and/or searched
    '''

    def __init__(self):
        self.__notes = []

    def new_note(self, memo, tags = ''):
        n = Note(memo, tags)
        self.__notes.append(n)

    def modify_note(self,note_id,memo):
        n = self.__find_note(note_id)
        #if not n --> does not have value
        if not n:
            print("Note not found. try again")
        else:
            n.setMemo(memo)

    def print_note(self,note_id):
        n = self.__find_note(note_id)
        #if not n --> does not have value
        if not n:
            print("Note not found. try again")
        else:
            print("note id:",n.getId(), "memo:",n.getMemo(), "tags:",n.tags)

    def match_note(self, keyword):
        for note in self.__notes:
            if note.match(keyword):
                print("matching keyword:",keyword, "node id:",note.getId(), "memo:",note.getMemo(), "tags:",note.tags)
    

    def __find_note(self,note_id):
        for note in self.__notes:
            if note.getId() == note_id:
                return note
        return None

