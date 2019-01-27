import turtle

def drawShape(color, start, points):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    x,y = start
    for point in points:
        dx, dy = point
        turtle.goto(x + dx, y + dy)
    turtle.goto(start)
    turtle.penup()

print("Using DrawShape method")
squareShape = [ (0, 50), (50, 50), (50, 0),(0, 0)]
drawShape("blue",(0, 0), squareShape)
squareShape = [(-50,0), (-50, 50), (0, 50),(0,0)]
drawShape("blue",(0, 0), squareShape)
squareShape3 = [(-50, 0), (-50, -50), (0, -50), (0, 0)]
drawShape("blue",(0, 0), squareShape3)
squareShape4 = [(50,0), (50, -50), (0,-50), (0, 0)]
drawShape("blue",(0, 0), squareShape4)


