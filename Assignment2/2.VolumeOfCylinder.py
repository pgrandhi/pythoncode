#Prompt the use to enter radius and length
radius,length = map(float, input("Enter the radius and length of a cylinder:").split(","))

#constant
PI = 3.1417

def volumeOfCylinder(radius,length):
    area = PI * (radius ** 2)
    volume = area * length
    print("The area is ", round(area,4), " The volume is ", round(volume,1))

volumeOfCylinder(radius,length)     
