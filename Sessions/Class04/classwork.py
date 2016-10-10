from math import sqrt

def my_abs(num):
    if type(num) == int or type(num) == float:
        if num >= 0:
            return num
        else:
            return -num
    else:
        print('invalid value')

def quadratic(a, b, c):
    try:
        x1 = (-b + (sqrt(b**2 - 4*a*c))) / (2*a)
        x2 = (-b - (sqrt(b**2 - 4*a*c))) / (2*a)
        return x1, x2
    except ValueError:
        print('These values will not work')