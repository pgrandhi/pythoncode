import turtle

turtle.pensize(2)

def drawLine(color, start, end):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(end)
    turtle.end_fill()
    turtle.penup()

print("-39,48")
drawLine("red",(-39,48),(50,-50))
print("50,-50")
