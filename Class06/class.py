#Class06:

#the boolenan expression after IF is called the conditoin. 
#If it is true, the indented statement runs. If not, nothing happends. 
def ex_1():
    age = int(input('How old are you?'))
    if age >= 18:
        print('Your age is', age)
        print('adult')

#alternative execution
def ex_2():
    age = int(input('How old are you?'))
    if age >= 18:
        print('Your age is', age)
        print('adult')
    else: #don't forget this colon
        print('your age is', age)
        print('not an adult')

#Chainged conditionals
#elif = is short for else if 
def ex_3():
    age = int(input('How old are you?'))
    if age >= 18:
        print('adult')
    elif age >= 10:
        print('teenager')
    else:
        print('kid')

#Exercise_1: BMI Calculator
def cat_bmi(): 
    if bmi < 18.5:
        print('You are underweight')
    elif bmi >= 18.5 and bmi <= 24.0:
        print('You are normal weight')
    elif bmi >= 25 and bmi <30:
        print('You are overweight')
    elif bmi >= 30:
        print('You are obese')

def bmi():
    units = input("USA or Metric?")


    if units == USA
        bmi = 703 * (weight / (height ** height))


under_weight = < 18.5
normal_weight = range(18.5, 24.9)
over_weight = range(25, 29.9)
obesity = 30






#print(ex_1())
#print(ex_2())
#print(ex_3())
#print() 