# Python program to draw hexagon
# using Turtle program

import turtle
polygon = turtle.Turtle()

# Creating variables
num_sides = 6
side_length = 70
angle = 360.0 / num_sides

#Using variables as place holders

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
