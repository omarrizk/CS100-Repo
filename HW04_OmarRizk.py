"""
Omar Rizk
CS 100 2021S Section 108
HW 04 February 19, 2021
"""
import math
import turtle
a = 3
b = 4
c = 5

if(a<b):
    print("OK")
else:
    print("NOT OK")
if(c<b):
    print("OK")
else:
    print("NOT OK")
if((a+b) == c):
    print("OK")
else:
    print("NOT OK");
if((a**2+b**2)==c**2):
    print("OK")
else:
    print("NOT OK")

print("Input the following: a color, line width, line length, and shape");
color = input()
lineWidth = float(input())
lineLength = float(input())
shape = input()
t = turtle.Turtle()
t.color(color)
t.pensize(lineWidth)
t.forward(lineLength)
if(shape == "line"):
    t.forward(lineLength)
elif(shape == "triangle"):
    t.left(120)
    t.forward(lineLength)
    t.left(120)
    t.forward(lineLength)
    t.left(120)
else:
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)


