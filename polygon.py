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

max_sides = 0
list = {}
max_x = float(0)
min_x = float(0)
max_y = float(0)
min_y = float(0)

def setPolygon(sides=3):
    global max_sides
    global list
    global max_x
    global min_x
    global max_y
    global min_y
    max_sides = sides
    for i in range(3, sides+1):
        list[i] = []
        angle = 360 / i
        cross = 0
        x, y = 0, 0
        for j in range(i):
            cross += angle
            x += math.cos(math.radians(cross))
            y += math.sin(math.radians(cross))
            if float(x) > max_x: max_x = float(x)
            if float(x) < min_x: min_x = float(x)
            if float(y) > max_y: max_y = float(y)
            if float(y) < min_y: min_y = float(y)
            list[i].append([x, y])
        
def drawPolygon():
    global max_sides
    global list
    global max_x
    global min_x
    global max_y
    global min_y
    gap = 256 / max_sides
    b = random.random()
    length = math.floor(500 / (max_x - min_x))
    x, y = ((max_x+min_x)/2*-1)*length, ((max_y+min_y)/2*-1)*length
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for sides in list:
        r = math.floor(gap * sides) / 255
        if r > 1: r = 1
        if r < 0: r = 0
        g = 1 - r
        turtle.pencolor(r, g, b)
        print('r, g, b', r, g, b)
        for pos in list[sides]:
            turtle.goto(x + pos[0] * length, y + pos[1] * length)
    turtle.hideturtle()
    
screen = turtle.Screen()
screen.setup(800,600)
setPolygon(20)
# print('max_x', max_x, 'min_x', min_x)
# print('max_y', max_y, 'min_y', min_y)
# print('list', list)
drawPolygon()
screen.mainloop()