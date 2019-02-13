import datetime
class StopWatch:
    def __init__(self):
        self.__startTime = datetime.datetime.now()
        self.__endTime = datetime.datetime.now()
        
    def start(self):
        self.__startTime = datetime.datetime.now()

    def stop(self):
        self.__endTime = datetime.datetime.now()

    def getElapsedTime(self):
        delta = self.__endTime - self.__startTime
        return int(delta.total_seconds() * 1000) #milliseconds 
        

    
        
