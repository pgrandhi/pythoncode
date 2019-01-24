import turtle

turtle.pensize(5)

def drawCircle(color, x, y, radius=45):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)

drawCircle("blue",-110,-25)
drawCircle("black",0,-25)
drawCircle("red",110,-25)
drawCircle("yellow",-55,-75)
drawCircle("green",55,-75)

