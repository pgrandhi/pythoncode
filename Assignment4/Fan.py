class Fan:
    def __init__(self, speed="SLOW", isOn=False, radius=5, color="blue"):
        self.__speed = speed
        self.__on = isOn
        self.__radius = radius
        self.__color = color
        
    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed

    def getFanOn(self):
        return self.__on

    def setFanOn(self, on):
        self.__on = on

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius
    
    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color = color    

    def print(self):
        print("Speed:",self.getSpeed(),"IsOn:",self.getFanOn(),"Radius:",self.getRadius(),"Color:",self.getColor())
