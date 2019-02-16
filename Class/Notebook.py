#from <file> import <classname> or import *
from Note import Note

class Notebook:
    '''
    Represents a collection of Notes
    that can be modified or tagged and/or searched
    '''

    def __init__(self):
        self.__notes = []

    def getNotes(self):
        return self.__notes

    def new_note(self, memo, tags = ''):
        n = Note(memo, tags)
        self.__notes.append(n)
        
    def modify_memo(self,note_id,memo):
        n = self.__find_note(note_id)
        #if not n --> does not have value
        if not n:
            print("Note not found. try again")
        else:
            n.setMemo(memo)

    def modify_tags(self,note_id,tags):
        n = self.__find_note(note_id)
        #if not n --> does not have value
        if not n:
            print("Note not found. try again")
        else:
            n.tags = tags

    def print_note(self,note_id):
        n = self.__find_note(note_id)
        #if not n --> does not have value
        if not n:
            print("Note not found. try again")
        else:
            print("{0}: {1} \n {2}".format(n.getId(),n.getMemo(), n.tags))

    def search(self, filter):
        '''
        find all notes that match the given filter
        :paramm filter - keyword to search on
        return notes
    
        for note in self.__notes:
            if note.match(filter):
                print("matching keyword:",keyword, "node id:",note.getId(), "memo:",note.getMemo(), "tags:",note.tags)
        '''
        return [note for note in self.__notes if note.match(filter)]

    def __find_note(self,note_id):
        for note in self.__notes:
            if note.getId() == note_id:
                return note
        return None

