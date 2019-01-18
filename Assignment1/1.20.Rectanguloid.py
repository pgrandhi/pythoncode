import turtle

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

print("Using DrawShape method")
rectangleShape = [ (0, 50), (100,50), (100,0),(0, 0)]
drawShape("red",(0, 0), rectangleShape)

