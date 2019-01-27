import turtle

def drawShape(color, start, points):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    x,y = start
    for point in points:
        dx, dy = point
        turtle.goto(x + dx, y + dy)
    turtle.goto(start)
    turtle.penup()

def drawLine(color, start, end):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)
    turtle.penup()
     

print("Using DrawShape method")
rectangleShape = [ (0, 50), (100,50), (100,0)]
drawShape("black",(0, 0), rectangleShape)
rectangleShape2 = [ (25, 75), (125,75), (125,25),(25, 25)]
drawShape("black",(25, 25), rectangleShape)
drawLine("black",(0,0),(25,25))
drawLine("black",(0,50),(25,75))
drawLine("black",(100,50),(125,75))
drawLine("black",(100,0),(125,25))

