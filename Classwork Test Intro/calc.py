#ClassWork
    #print(42*60 + 45) #question 1
    #print(10/1.60934) #question 2
    #question 3
    #print(2565/6.21371) #avg time in sec/m
    #print(412.7968637094425/60) #avg time in min/m
    #print(60/6.879947728490708) #mph

#Class 2_Exercise 1
    #problem1
        #message = 'Enter the Radius of the Sphere: '
        #print(message)
        #radius = float(input())
        #pi = 3.14
        #volume = (4/3) * (pi * radius ** 3)
        #print('Volume is: ', volume)

    #problem2
        #price = 24.95
        #discount = price * .4
        #quantity = 60
        #shipping = 3 + ((quantity-1) * .75)
        #wholesale = (price - discount) * quantity + shipping 
        #message = 'Total wholesale cost for 60 copies is:', wholesale
        #print(message)
        
    #problem3
       # easy_time = 2 * 8.25
        #tempo_time = 3 * 7.2
        #total = easy_time + tempo_time
        #end_minutes = total - 8 #the amount of min past 7am
        #message = 'Home for breakfast: 7:%d' % end_minutes
        #print(message)

    #problem4
    #   increase = 89 - 82
    #   inc = increase / 82
    #    PercInc = inc * 100
    #    message = 'Percent Increase: %.1f%%' % PercInc
    #    print(message) 

#Session04_Excercise_1_9/13

from math import sqrt

def quadratic(a, b, c):
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    
    d = (b**2) - (4*a*c) #discriminant
    
    try:
        pos = (-b + (sqrt(d)) / (2*a)
        neg = (-b - (sqrt(d)) / (2*a)
        return pos, neg
 





