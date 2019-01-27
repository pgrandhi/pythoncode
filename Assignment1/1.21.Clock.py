import turtle
turtle.pensize(2)
def drawCircle(color, x, y, radius=50):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)

def drawLine(color, start, end):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)
    turtle.penup()
    
drawCircle("black",0,0)
drawLine("black",(0,50),(50,50))
drawLine("black",(0,50),(0,100))

