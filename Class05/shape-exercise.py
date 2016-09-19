import turtle
import math
tpen = turtle.Turtle()
tpen.pensize(4)

#Excercise_3_question1
print(tpen)

#shape one
def twotris(t):
    t.lt(30)
    t.fd(200)
    t.rt(120)
    t.fd(200)
    t.rt(120)
    t.fd(400)
    t.lt(120)
    t.fd(200)
    t.lt(120)
    t.fd(200)

twotris(tpen)

tpen.lt(60)
twotris(tpen)

tpen.fd(200)
tpen.lt(91)
tpen.circle(200)
tpen.lt(90)
tpen.fd(100)
tpen.circle(55)

tpen.fd(100)
tpen.lt(30)

tpen.fd(100)
tpen.circle(55)

tpen.lt(180)
tpen.fd(100)

tpen.rt(270)
tpen.fd(100)
tpen.circle(55)

tpen.lt(180)
tpen.fd(100)

tpen.rt(270)
tpen.fd(100)
tpen.circle(55)






turtle.mainloop()