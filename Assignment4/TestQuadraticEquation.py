from QuadraticEquation import QuadraticEquation 

a = eval(input("Enter the value for a:"))
b = eval(input("Enter the value for b:"))
c = eval(input("Enter the value for c:"))


equation = QuadraticEquation(a,b,c)
discriminant = equation.getDiscriminant()
print ("discriminant",discriminant)
if(discriminant>0):
    print ("root1 : ", equation.getRoot1(), "root2 :",equation.getRoot2())
elif (discriminant==0):
    print ("root1 : ", equation.getRoot1())
else:
    print ("the equation has no roots")
