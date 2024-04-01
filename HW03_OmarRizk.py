"""
Omar Rizk
CS 100 2021S Section 108
HW 03 February 12, 2021
"""
import math
import turtle


# equilateral triangle
t = turtle.Turtle()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# square
s = turtle.Turtle()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)

# regular pentagon

p = turtle.Turtle()
p.forward(100)
p.left(72)
p.forward(100)
p.left(72)
p.forward(100)
p.left(72)
p.forward(100)
p.left(72)
p.forward(100)
p.left(72)

# four concentric circles with radius of 50, 100, 150, 200
c = turtle.Turtle()

c.circle(50)
c.right(90)
c.penup()
c.forward(50)
c.left(90)

c.pendown()
c.circle(100)
c.right(90)
c.penup()
c.forward(50)
c.left(90)

c.pendown()
c.circle(150)
c.right(90)
c.penup()
c.forward(50)
c.left(90)

c.pendown()
c.circle(200)
c.right(90)

# compute and print out 100!, log base 2 of 1,000,000 , and greatest common divisor of 63 and 49
print(math.factorial(100))
print(math.log(1000000, 2))
print(math.gcd(63,49))

