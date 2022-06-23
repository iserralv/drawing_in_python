# Python program to draw square
# using Turtle Programming Language
import turtle
sqr = turtle.Turtle()

for i in range (4):
    sqr.forward(50) #forward turtle by 50 units
    sqr.right(90) # Turn turtle by 90 degrees
turtle.done()

# Second Loop Approach

import turtle
t = turtle.Turtle()

length = int(input("Enter the length of the Rectangle: "))
width = int(input("Enter the width of the Rectangle: "))

for i in range(4):
    #Drawing length
    if i % 2 == 0:
        t.forward(length) # Forward turttle by length unit
        t.left(90) # Turn turtle by 90 degrees

    #Drawing width
    else:
        t.forward(width) # Forward turtle by width units
        t.left(90) # Turn turtle by 90 degrees
