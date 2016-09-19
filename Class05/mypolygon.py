import turtle
jerry = turtle.Turtle()

'''Excersie 2.1
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(jerry)

'''
'''Excercise 2.3

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(jerry, 7, 70)

'''
'''Excercise 2.4'''
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
   
   polygon(t, n, length)


turtle.mainloop()