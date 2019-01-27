import turtle

turtle.pensize(2)

def drawLine(color, start, end):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.write(str(start),True) 
    turtle.pendown()
    turtle.goto(end)
    turtle.penup()
    turtle.write(str(end),True) 

drawLine("red",(-39,48),(50,-50))

