import datetime
#If Python sees a new variable, it considers it a local variable,
#does not match it to the global variable. Always local first
#You have to specifically mention global last_id before using last_id
last_id = 0
class Note:
    #function that begins with __ is private method in Python
    #function that ends with __ is Python defined system function
    #For example init method below is private python defined function
    #YOu want to create the init method only if you want to do more than
    #Creating memory like allocating variables to memory
    #every function in the class will have self as first argument
    #anything associated with self is instance specific (object specific)
    #shared memory (global) needs to be defined outside the class
    def __init__(self, memo, tags=''):
        self.__memo = memo
        self.tags = tags
        self.__creationDate = datetime.date.today()
        global last_id
        last_id += 1
        #preceeding with __ makes the variable private
        self.__id = last_id
        

    #accessor and mutator methods allow to read and write respectively
    def getId(self):
        return self.__id

    def getCreationDate(self):
        return self.__creationDate

    def getMemo(self):
     return self.__memo
     
    def setMemo(self, newMemo):
     self.__memo = newMemo

    def match(self,keyword):
       '''
       Determing if this note matches the keyword text
       :param keyword : search text case sensitive search
       :return true if matches, False otherwise 
       '''

       return keyword in self.__memo or keyword in self.tags
       
        
        
