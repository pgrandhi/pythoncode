import turtle

turtle.pensize(2)

def drawLine(color, start, end):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)
    turtle.penup()

drawLine("black",(40,-69.28), (-40,-69.28))
drawLine("black", (-40,-69.28),(-80,-9.8))
drawLine("black",(-80,-9.8), (-40,69))
drawLine("black",(-40,69), (40,69))
drawLine("black",(40,69),(80,0))
drawLine("black",(80,0),(40,-69.28))
         


