import turtle
def drawGrid(startx, starty,width, height, color):
    print("startx:", startx, "starty:",starty, "width:",width, "height:",height)
    turtle.penup()
    turtle.pencolor('black')
    turtle.fillcolor(color)
    turtle.goto(startx, starty)
    turtle.pendown()
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    
def drawChessboard(startx, endx, starty, endy):
    width = (endx-startx)/8
    height = (endy-starty)/8
    for row in range(8):
        for column in range(8):
            if ((row+column) %2 ==0):
                color='black'
                drawGrid(startx + column * width, starty+row*height, width,height,color)
            else:
                color='white'
                drawGrid(startx + column * width, starty+row*height, width,height,color)
    
    
drawGrid(30,30,30, 30, 'black')
drawChessboard(0,0,240,240)

