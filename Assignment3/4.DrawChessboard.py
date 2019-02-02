import turtle
def drawGrid(startx, starty,width, height, color):
    turtle.penup()
    turtle.pencolor('black')
    turtle.fillcolor(color)
    turtle.goto(startx, starty)
    turtle.pendown()
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def drawChessboardByWidthAndHeight(startx, starty, width, height):
    for row in range(0,8):
        for column in range(0,8):
            if ((row+column) %2 ==0):
                color='black'
            else:
                color='white'
            drawGrid(startx + column * width, starty + row*height, width, height,  color)

            
def drawChessboard(startx, starty, endx, endy):
    width = (endx - startx)/8
    height = (endy - starty)/8
    drawChessboardByWidthAndHeight(startx, starty, width, height)
    
drawChessboard(-240, -180, 0, 60)
drawChessboard(40, -180, 280, 60)
turtle.done()

