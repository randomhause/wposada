#Question 1
""" my_factor: returns list containing the factors of the integer.
        (1) This function only will check the numbers up through the square root of the interger. 
            Because any factor greater than the square root will have the corresponding factor that is 
            less than the quare root.
        (2) if the interger is evenly divided by the number that's being checked, it'll add that number
            as well as the interger that's divided by that number """
    
from math import sqrt

i = float(input('Input interger to be factored:'))

def my_factor(x):
    
    fac_list = []
    x = int(x)
    for num in range(1, int(sqrt(x) + 1)):
        if x % num ==0: 
            fac_list.append(num)
            fac_list.append(int(x / num))
    return fac_list

print(my_factor(i))
