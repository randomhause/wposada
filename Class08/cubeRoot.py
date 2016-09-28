#Only Possivite Intergers 
'''
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans)) '''

#Possivite & Negative Intergers (HW)

x = int(input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans ** 3 == abs(x):
        break
if ans ** 3 != abs(x): 
    print(str(x), 'is not a perfect cube!')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))



