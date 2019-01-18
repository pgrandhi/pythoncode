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

drawLine("red",(40,-69.28), (-40,-69.28))
drawLine("red", (-40,-69.28),(-80,-9.8))
drawLine("red",(-80,-9.8), (-40,69))
drawLine("red",(-40,69), (40,69))
drawLine("red",(40,69),(80,0))
drawLine("red",(80,0),(40,-69.28))
         


