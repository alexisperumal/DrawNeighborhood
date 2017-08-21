# Alexis Perumal, 2/21/16
# Turtle Example Program
# v2: Add colored area fills (red and yellow) to the houses.
# v3 (7/16/17): Add random color area fills.
# 8/12/17: Used this as a basis for new project in PyCharm, and pushed it to GitHub.

import turtle, random

def randomColors():
    rgb = (random.random(), random.random(), random.random())
    turtle.pencolor(rgb)
    rgb = (random.random(), random.random(), random.random())
    turtle.fillcolor(rgb)

def drawTriangle(x, y, scale=1, restore=False):
    oldX = turtle.xcor()
    oldY = turtle.ycor()
    turtle.penup()
    turtle.setpos(x, y)

#    rgb = (random.random(), random.random(), random.random())
#    turtle.pencolor(rgb)
#    rgb = (random.random(), random.random(), random.random())
#    turtle.fillcolor(rgb)
# Adding a uselsess comment. Editing a comment. Another edit on the first comment.
# Adding a second useless comment.
# Comment added in the branch. Boo!
# Adding another comment with Devin at Starbucks (8/20/17)
# GitHub server side comment with Devin at Starbucks.

    turtle.begin_fill()
    turtle.pendown()
    turtle.setpos(x+scale,y)
    turtle.setpos(x+scale/2, y+scale/2**0.5) # 45, 45, 90 triangle with hight sqrt scale and the hyp as the base.
    turtle.setpos(x, y)
    turtle.end_fill()
    turtle.penup()
    if restore:
        turtle.setpos(oldX, oldY)

def drawRect(x, y, width=1, height=1, scale=1, restore=False):
    oldX = turtle.xcor()
    oldY = turtle.ycor()
    turtle.penup()
    turtle.setpos(x, y)
#    turtle.color('brown', "gold")
    turtle.begin_fill()
    turtle.pendown()
    turtle.setpos(x+width*scale,y)
    turtle.setpos(x+width*scale, y+height*scale)
    turtle.setpos(x, y+height*scale)
    turtle.setpos(x, y)
    turtle.end_fill()
    turtle.penup()
    if restore:
        turtle.setpos(oldX, oldY)

def drawSquare(x, y, scale=1, restore=False):
    drawRect(x, y, 1, 1, scale, restore)

def drawHouse(x=0, y=0, scale=100, restore=False):
    oldX = turtle.xcor()
    oldY = turtle.ycor()
    turtle.penup()
    randomColors()
    drawSquare(x, y, scale)
    randomColors()
    drawTriangle(x,y+scale, scale) # Draw the roof
    randomColors()
    drawRect(x+0.4*scale, y, 0.2*scale, 0.4*scale) # Draw the front door
    randomColors()
    drawSquare(x+0.1*scale, y+0.6*scale, 0.2*scale) # Draw the left window
    drawSquare(x+0.7*scale, y+0.6*scale, 0.2*scale) # Draw the right window
    turtle.penup()
    if restore:
        turtle.setpos(oldX, oldY)

def drawCircle(x=0, y=0, scale=100, restore=False):
    oldX = turtle.xcor()
    oldY = turtle.ycor()
    turtle.penup()        
    turtle.setpos(x, y-scale/2)
    turtle.pendown()
    turtle.circle(scale/2)
    turtle.penup()
    if restore:
        turtle.setpos(oldX, oldY)

def main():
#    drawHouse(-300, -0, 200)
#    drawHouse(0, 0, 100)
#    drawHouse(200, 0, 50)
#    drawCircle(0, 0)
#    drawCircle(0, 0, 20)
#    drawCircle(0, 0, 200)
    turtle.speed(0)

    for i in range(50):
        x = random.randrange(-450, 400)
        y = random.randrange(-450, 400)
        scale = random.randrange(20, 100)
#        drawCircle(x, y, 10)
        drawHouse(x, y, scale)
    
main()
