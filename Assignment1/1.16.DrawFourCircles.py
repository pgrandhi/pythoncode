import turtle

turtle.pensize(5)

def drawCircle(color, x, y, radius=45):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)



drawCircle("black",45,0)
drawCircle("black",-45,0)
drawCircle("black",45,-90)
drawCircle("black",-45,-90)

