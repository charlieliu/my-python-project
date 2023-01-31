# Import math Library
import math
import turtle
import random

# print('Convert different degrees into radians:', math.radians(180))

def printAngle(angle):
    print('Return the sine value of ' + str(angle) + ' degrees:', math.sin(math.radians(angle)))
    print('Return the cosine value of ' + str(angle) + ' degrees', math.cos(math.radians(angle)))
    print('Return the sine value\'s power of ' + str(angle) + ' degrees:', math.sin(math.radians(angle))**2)
    print('Return the cosine value\'s power of ' + str(angle) + ' degrees', math.cos(math.radians(angle))**2)

# printAngle(0)
# printAngle(60)
# printAngle(180)
# printAngle(360)

max_x = float(0)
min_x = float(0)
max_y = float(0)
min_y = float(0)
 
def drawPolygon(shapes):
    list = {}
    global max_x
    global min_x
    global max_y
    global min_y
    for shapes in range(3, shapes+1):
        list[shapes] = getPoints(shapes)
    gap = 256 / shapes
    b = random.random()
    length = math.floor(500 / (max_x - min_x))
    x, y = ((max_x+min_x)/2*-1)*length, ((max_y+min_y)/2*-1)*length
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for shapes in list:
        r = math.floor(gap * shapes) / 255
        if r > 1: r = 1
        if r < 0: r = 0
        g = 1 - r
        turtle.pencolor(r, g, b)
        print('shapes:', shapes, 'r, g, b', r, g, b)
        print('shapes:', shapes, 'points:', list[shapes])
        for pos in list[shapes]:
            turtle.goto(x + pos[0] * length, y + pos[1] * length)
    turtle.hideturtle()
            
def getPoints(shapes):
    global max_x
    global min_x
    global max_y
    global min_y
    points = []
    angle = 360 / shapes
    cross = 0
    x, y = 0, 0
    for i in range(shapes):
        cross += angle
        x += math.cos(math.radians(cross))
        y += math.sin(math.radians(cross))
        if float(x) > max_x: max_x = float(x)
        if float(x) < min_x: min_x = float(x)
        if float(y) > max_y: max_y = float(y)
        if float(y) < min_y: min_y = float(y)
        points.append([x, y])
    print('shapes:', shapes, 'width:', (max_x - min_x), 'height:', (min_y - min_x), points)
    print('shapes:', shapes, 'max_x:', max_x, 'min_x:', min_x, 'max_y:', max_y, 'min_y:', min_y)
    return points
    
def drawCenterPolygon(shapes):
    list = {}
    max_x
    min_x
    max_y
    min_y
    for shapes in range(3, shapes+1):
        list[shapes] = getCenterPoints(shapes)
    gap = 256 / shapes
    b = random.random()
    length = math.floor(500 / (max_x - min_x))
    turtle.penup()
    for shapes in list:
        r = math.floor(gap * shapes) / 255
        if r > 1: r = 1
        if r < 0: r = 0
        g = 1 - r
        turtle.pencolor(r, g, b)
        print('shapes:', shapes, 'r, g, b', r, g, b)
        print('shapes:', shapes, 'points:', list[shapes])
        for (x, y) in list[shapes]:
            turtle.goto(x * length, y * length)
            if turtle.isdown() == False:
                turtle.pendown()
        turtle.penup()
    turtle.hideturtle()

def getCenterPoints(shapes):
    global max_x
    global min_x
    global max_y
    global min_y
    points = []
    angle = 360 / shapes
    cross = 90
    x, y = 0, 0
    for i in range(shapes+1):
        cross += angle
        x = math.cos(math.radians(cross)) * shapes
        y = math.sin(math.radians(cross)) * shapes
        if float(x) > max_x: max_x = float(x)
        if float(x) < min_x: min_x = float(x)
        if float(y) > max_y: max_y = float(y)
        if float(y) < min_y: min_y = float(y)
        points.append((x, y))
    print('shapes:', shapes, 'width:', (max_x - min_x), 'height:', (min_y - min_x), points)
    print('shapes:', shapes, 'max_x:', max_x, 'min_x:', min_x, 'max_y:', max_y, 'min_y:', min_y)
    return points
    
screen = turtle.Screen()
screen.setup(800,600)
drawPolygon(50)
# drawCenterPolygon(50)
screen.mainloop()