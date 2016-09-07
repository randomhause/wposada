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
#message = 'Total wholesale cost for 60 copies is ', wholesale
#print(message)
 
#problem3
#mile_1_and_last = 16.3
#mile_4 = 21.36
#start_time = 6.52 

start_time = date.time(hour = 6, minute = 52)
elapse_time = date.time(hour = 0, minute = 37, second = 66)
finish_time = start_time + elapse_time
print(finish_time)