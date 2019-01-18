import turtle

turtle.pensize(2)

def drawShapeUsingForwardLeft(color):
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)


def drawShape(color, start, points):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.begin_fill()
    x,y = start
    for point in points:
        dx, dy = point
        turtle.goto(x + dx, y + dy)
    turtle.goto(start)
    turtle.end_fill()
    turtle.penup()
    
print("Using Forward Left")
drawShapeUsingForwardLeft("blue")

print("Using DrawShape method")
triangleShape=[(200,0), (100,100),(0,0)]
drawShape("red",(100,-100), triangleShape)


