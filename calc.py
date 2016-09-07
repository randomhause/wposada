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
seconds = 1
minutes = 60 * seconds
hours = 60 * minutes

time_left_house = 6 * hours + 52 * minutes
miles_run_easy_pace = 2 * (8 * minutes + 15 * seconds)
miles_run_fast_pace = 3 * (7 *minutes + 12 * seconds)
#output in seconds

total_time_run = miles_run_easy_pace + miles_run_fast_pace + time_left_house

hours2 = total_time_run // hours
#hour output

part_hour = total_time_run % hours
minutes2 = part_hour // minutes
seconds2 = part_hour % minutes

print('Total time run: {}, Hours: {}, Minutes: {}, Seconds: {}'.format(total_time_run, hours2, minutes2, seconds2))




#proble4
