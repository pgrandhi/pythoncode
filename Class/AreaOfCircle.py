# get radius from the user
radius = eval(input("Enter the radius of the circle: "))

#constant
PI = 3.1417

def printAreaOfCircle(radius):
    area = PI * (radius ** 2)
    print("Area of the circle: ", area)
    
#power of 2
#area = PI * (radius ** 2)

printAreaOfCircle(radius)
