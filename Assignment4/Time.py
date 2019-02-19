import datetime
from datetime import timedelta
class Time:
    def __init__(self):        
        self.__hour = datetime.datetime.now().hour
        self.__minute = datetime.datetime.now().minute
        self.__second = datetime.datetime.now().second
        
    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elapseTime):
        '''
        sets time
        @param elapsedTime: elapsed time in seconds
        '''
        d = self.__now + timedelta(seconds=elapseTime)
        self.__hour = d.hour
        self.__minute = d.minute
        self.__second = d.second
        

    def print(self):
        print (self.__hour,":",self.__minute,":",self.__second)
        

    
        
