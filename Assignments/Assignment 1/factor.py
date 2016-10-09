#Question 1: Re-do

def factor(n):
    for i in range(1, n + 1):
        if n % i == 0: #% used for divsor and remainder
            print(i)

number = int(input('Enter any integer to find out all of its factors:'))
# i wrote int instead of float because it can only a number not a decimal

factor(number)
