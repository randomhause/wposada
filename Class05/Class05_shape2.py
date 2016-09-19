#Worked with Teresa, Hunter, Dunca & Rose. 
import turtle
import math
jerry = turtle.Turtle()
jerry.pensize(4)


print(jerry)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length): 
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t,r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n 
    polygon(t, n, lenth)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle /360
    n = int(arc_length / 3) +1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    for i in range(0,2):
        arc(t, r, angle)
        t.lt(180-angle)

for i in range(0,6):
    petal(jerry, 200, 360/6)
    jerry.lt(360/6)
arc(jerry, 200, 360/6)
jerry.lt(61)
circle(jerry,200)



turtle.mainloop()