# Python program to draw
# Spiral Square Outside In
# using Turtle Programming Language

import turtle #Outside_In
wn = turtle.Screen()
wn.bgcolor("blue")
sqr = turtle.Turtle()
sqr.color("yellow")

# Create a function to draw

def sqrfunc(size):
    for i in range(4):
        sqr.fd(size)
        sqr.left(90)
        size = size - 5

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
