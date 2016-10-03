#Question 3 & 5

"""The drunkard function takes n, the number of moves the drunkard will take. 
    (1) It will create variables for the north/south and east/west directions. 
    (2) It will creates variables for the direction that the drunkard will have at  the end of his journey.
    (3) For n moves, a random number between 0 and 4 is generated, each corresponds to a cardinal direction.
        a. The north/south or east/west value is changed depending on the generated number.
        b. The direction is printed for the User.
        c. Set the turtle's heading to that direction and move it forward.
        d. Stamp the turtle's shape so the user can see where it is going.
    (4) Final directions from the origin are translated."""

import random
import turtle
import math
jerry = turtle.Turtle()

print(jerry)

def drunkard(n): 
    #Drawing Circle 
    jerry.circle(5)
    NS = 0
    EW = 0
    NS_direction = ''
    EW_direction = ''

    for block in range(n):
        direction = random.randrange(0,4)
       
        if direction == 0: 
            NS += 1
            print("The Drunkard walk North ")
            jerry.setheading(90)
        elif direction == 1: 
            EW += 1
            print("The Drunkard walk East ")
            jerry.setheading(0)
        elif direction == 2:
            NS -= 1
            print("The Drunkard walk South ")
            jerry.setheading(270)
        else: 
            EW -= 1
            print("The Drunkard walk West ")
            jerry.setheading(180)
        jerry.fd(30)
        jerry.stamp()
    
    if NS >= 0:
        NS_direction = 'North'
    else:
        NS_direction = 'South'
    if EW >= 0:
        EW_direction = 'East'
    else:
        EW_direction = 'West'

    print('The Drunkard has moved a totla distance of %s block(s) to the %s block(s) to the %s' %(abs(ns), NS_direction, abs(EW), EW_direction))
    #Rotates the turtle slowly
    while True: 
        jerry.lt(2)

drunkard(70)

turtle.mainloop()
