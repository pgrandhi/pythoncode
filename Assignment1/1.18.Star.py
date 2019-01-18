import turtle

turtle.pensize(2)

def drawStar(color,size):
    turtle.pencolor(color)
    count = 0
    angle = 144
    while count <= 5:
        turtle.forward(size)
        turtle.right(angle)
        count += 1
    return


drawStar("blue",100)
         


